#!/usr/bin/env python3
"""Verify the unmodified REA import, or fetch a revision and refresh the package."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import sys

PLUGIN = Path(__file__).resolve().parents[1] / 'plugins/rea'
LOCK = 'fleet/upstream.json'
# Upstream's distribution manifests target its npm package. Fleet owns the
# corresponding plugin configuration and launches the bundled source build.
UPSTREAM_PACKAGING = {'.claude-plugin/marketplace.json', '.claude-plugin/plugin.json',
                      '.codex-plugin/mcp.json', '.codex-plugin/plugin.json'}
sys.path.insert(0, str(PLUGIN / 'fleet'))
from skill_exports import exported_skills, package_skills


def check(plugin=PLUGIN):
    origin = json.loads((plugin / LOCK).read_text())
    for name, expected in origin['files'].items():
        path = plugin / name
        if (not path.is_file() or path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != expected['sha256']
                or bool(path.stat().st_mode & 0o111) != (expected['mode'] == '100755')):
            raise RuntimeError(f'Upstream file differs: {name}. Preserve it separately before updating.')
    packaged = plugin / 'skills'
    expected = exported_skills(plugin)
    package_files = {p.relative_to(packaged) for p in packaged.rglob('*')
                     if p.is_file() and p.relative_to(packaged).parts[0] != 'reverse-engineer-anything'}
    if set(expected) != package_files or any((packaged / p).read_bytes() != data for p, data in expected.items()):
        raise RuntimeError('Packaged skills differ from upstream .agents/skills; regenerate them.')
    return origin


def refresh(ref, plugin=PLUGIN):
    old = check(plugin)
    with tempfile.TemporaryDirectory(prefix='fleet-rea-upstream-') as tmp:
        checkout = Path(tmp)
        def git(*args):
            return subprocess.check_output(['git', '-C', str(checkout), *args])
        git('init', '--quiet')
        git('fetch', '--quiet', '--depth=1', old['repository'], ref)
        commit = git('rev-parse', 'FETCH_HEAD').decode().strip()
        files, submodules = {}, {}
        for entry in git('ls-tree', '-rz', '--full-tree', commit).split(b'\0'):
            if not entry:
                continue
            header, name = entry.split(b'\t', 1)
            mode, kind, digest = header.decode().split()
            name = name.decode()
            if name in UPSTREAM_PACKAGING:
                continue
            if kind == 'commit':
                submodules[name] = digest
            elif mode in ('100644', '100755'):
                files[name] = {'blob': digest, 'mode': mode}
            else:
                raise RuntimeError(f'Unsupported upstream entry {name}: {mode}')
        # New upstream paths must never overwrite Fleet's manifests or helpers.
        for name in files:
            if name.startswith(('fleet/', 'skills/', '.codex-plugin/', '.claude-plugin/')) or name in ('plugin.json', 'mcp.json', '.mcp.json'):
                raise RuntimeError(f'Upstream now owns {name}; review the package boundary before updating.')
            if name not in old['files'] and (plugin / name).exists():
                raise RuntimeError(f'New upstream path collides with a local file: {name}')
        staging = checkout / 'source'
        staging.mkdir()
        with tarfile.open(fileobj=io.BytesIO(git('archive', commit))) as archive:
            archive.extractall(staging, filter='data')
        for name in files:
            files[name]['sha256'] = hashlib.sha256((staging / name).read_bytes()).hexdigest()
        for name in old['files'].keys() - files.keys():
            (plugin / name).unlink()
        for name in files:
            destination = plugin / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(staging / name, destination)
        package_skills(plugin)
        origin = dict(repository=old['repository'], commit=commit,
                      tree=git('rev-parse', commit + '^{tree}').decode().strip(),
                      files=files, submodules=submodules)
        (plugin / LOCK).write_text(json.dumps(origin, indent=2) + '\n')
    check(plugin)
    return commit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref', help='Upstream tag, branch or commit to fetch; omission verifies only.')
    args = parser.parse_args()
    try:
        revision = refresh(args.ref) if args.ref else check()['commit']
        print(f'REA upstream and maintainer skills verified: {revision}')
        if args.ref:
            print('Run python3 scripts/setup-rea.py to build REA and regenerate its public skill.')
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'{error}\n')
