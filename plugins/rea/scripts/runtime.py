"""Build and locate Fleet's bundled REA source; never install into a user profile."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile

PLUGIN = Path(__file__).resolve().parents[1]


def run(command: list[str], *, cwd: Path, env: dict[str, str], capture: bool = False):
    # Build progress belongs on stderr: the launcher also serves MCP over stdout.
    return subprocess.run(command, cwd=cwd, env=env, check=True, text=True,
                          stdout=subprocess.PIPE if capture else sys.stderr)


def toolchain() -> tuple[str, dict[str, str], dict]:
    selected = os.environ.get('FLEET_REA_NODE', 'node')
    node = shutil.which(selected)
    if not node:
        raise RuntimeError('Install a supported Node.js with npm, or set FLEET_REA_NODE to its node executable.')
    result = subprocess.run([node, '-p', 'JSON.stringify({version:process.versions.node,abi:process.versions.modules,platform:process.platform,arch:process.arch})'],
                            check=True, capture_output=True, text=True)
    info = json.loads(result.stdout)
    major, minor, _ = map(int, info['version'].split('.'))
    if not ((major == 22 and minor >= 19) or (major == 24 and minor >= 11) or major >= 26):
        raise RuntimeError(f"Node {info['version']} is unsupported. Install Node 24 LTS (>=24.11), 22 >=22.19, or 26+. Node 23/25 are unsupported.")
    env = dict(os.environ)
    env['PATH'] = str(Path(node).parent) + os.pathsep + env.get('PATH', '')
    env.update(HUSKY='0', TURBO_TELEMETRY_DISABLED='1', npm_config_audit='false',
               npm_config_fund='false', npm_config_update_notifier='false', npm_config_engine_strict='true')
    return node, env, info


def source_identity(plugin: Path = PLUGIN) -> tuple[dict, Path]:
    origin = json.loads((plugin / 'runtime/origin.json').read_text())
    archive = plugin / 'runtime' / origin['archive']
    if archive.parent != plugin / 'runtime' or not archive.is_file():
        raise RuntimeError('Bundled REA source archive is missing or outside runtime/.')
    actual = hashlib.sha256(archive.read_bytes()).hexdigest()
    if actual != origin['archive_sha256']:
        raise RuntimeError('Bundled REA archive checksum does not match runtime/origin.json; refusing to build.')
    return origin, archive


def extract_source(archive: Path, destination: Path, prefix: str) -> None:
    """Extract only regular files/directories within the declared snapshot root."""
    with zipfile.ZipFile(archive) as source:
        members = []
        for entry in source.infolist():
            path = PurePosixPath(entry.filename)
            mode = entry.external_attr >> 16
            if (path.is_absolute() or '..' in path.parts or '\\' in entry.filename
                    or not path.parts or path.parts[0] != prefix
                    or stat.S_ISLNK(mode)
                    or (stat.S_IFMT(mode) not in (0, stat.S_IFREG, stat.S_IFDIR))):
                raise RuntimeError(f'Unsafe source archive member: {entry.filename}')
            members.append((entry, path.parts[1:]))
        for entry, parts in members:
            if not parts:
                continue
            target = destination.joinpath(*parts)
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with source.open(entry) as inp, target.open('wb') as out:
                    shutil.copyfileobj(inp, out)
                target.chmod(0o755 if (entry.external_attr >> 16) & 0o111 else 0o644)


def ensure_runtime(*, plugin: Path = PLUGIN, build: bool = True) -> tuple[Path, str, dict[str, str]]:
    origin, archive = source_identity(plugin)
    node, env, info = toolchain()
    # No absolute checkout or interpreter paths: a ready build can move with Fleet.
    identity = dict(source=origin['archive_sha256'], node_abi=info['abi'],
                    platform=info['platform'], arch=info['arch'],
                    builder=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()[:24]
    store = plugin / 'node_modules/.fleet-rea'
    root = store / key
    marker = root / '.fleet-ready.json'
    required = ('scripts/rea.mjs', 'dist/mcp/main.js', 'dist/cli-runtime/cli.js',
                'node_modules/.package-lock.json')
    if marker.is_file() and json.loads(marker.read_text()) == identity and all((root / p).is_file() for p in required):
        return root, node, env
    if root.exists():
        raise RuntimeError(f'Incomplete REA build at {root}. Preserve any needed diagnostics, remove that generated directory, then rerun setup.')
    if not build:
        raise RuntimeError('Fleet REA is not built yet. Run python3 scripts/setup-rea.py from Fleet.')
    npm = shutil.which('npm', path=env['PATH'])
    if not npm:
        raise RuntimeError('npm is missing. Install npm alongside the supported Node.js runtime.')
    store.mkdir(parents=True, exist_ok=True)
    # Dependency downloads never populate or prune the shared ~/.npm cache.
    env['npm_config_cache'] = str((store / 'npm-cache').resolve())
    with tempfile.TemporaryDirectory(prefix='.build-', dir=store) as temporary:
        staging = Path(temporary) / 'source'
        staging.mkdir()
        extract_source(archive, staging, origin['archive_root'])
        package = json.loads((staging / 'package.json').read_text())
        if package['name'] != 'rea-agents' or package['version'] != origin['version']:
            raise RuntimeError('Bundled package identity does not match provenance.')
        print(f"Building Fleet REA {origin['version']} from its verified source snapshot…", file=sys.stderr)
        # Explicit build steps avoid upstream prepare/husky and unrelated installers.
        run([npm, 'ci', '--ignore-scripts', '--no-audit', '--no-fund'], cwd=staging, env=env)
        run([npm, 'run', 'metadata:check'], cwd=staging, env=env)
        run([npm, 'run', 'compile'], cwd=staging, env=env)
        run([npm, 'run', 'artifacts:skills'], cwd=staging, env=env)
        run([node, 'scripts/rea.mjs', '--version'], cwd=staging, env=env)
        # Exercise the real MCP adapter before publishing this generation.
        run([node, str(plugin / 'scripts/smoke.mjs'), str(staging)], cwd=staging, env=env)
        (staging / '.fleet-ready.json').write_text(json.dumps(identity, sort_keys=True) + '\n')
        try:
            staging.rename(root)
        except OSError:
            # Another setup may have published the same complete generation.
            if not marker.is_file() or json.loads(marker.read_text()) != identity:
                raise
    return root, node, env
