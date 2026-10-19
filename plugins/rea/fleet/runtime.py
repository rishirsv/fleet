"""Thin adapter around REA's documented source build and CLI."""
from pathlib import Path
import json
import os
import shutil
import subprocess
from skill_exports import package_skills

PLUGIN = Path(__file__).resolve().parents[1]


def toolchain():
    node = shutil.which(os.environ.get('FLEET_REA_NODE', 'node'))
    if not node:
        raise RuntimeError('Install the Node.js version in REA .nvmrc, with npm.')
    env = dict(os.environ)
    env['PATH'] = str(Path(node).parent) + os.pathsep + env.get('PATH', '')
    return node, env


def ensure_runtime(*, plugin=PLUGIN, build=True):
    node, env = toolchain()
    identity = json.loads(subprocess.check_output([
        node, '-p', 'JSON.stringify({node:process.versions.node,platform:process.platform,arch:process.arch})',
    ], text=True))
    identity['source'] = json.loads((plugin / 'fleet/upstream.json').read_text())['commit']
    marker = plugin / 'node_modules/.fleet-ready.json'
    required = ('dist/mcp/main.js', 'dist/cli-runtime/cli.js', 'node_modules/.package-lock.json')
    if (marker.is_file() and json.loads(marker.read_text()) == identity
            and all((plugin / p).is_file() for p in required)):
        return plugin, node, env
    if not build:
        raise RuntimeError('Run python3 scripts/setup-rea.py in Fleet before starting REA.')
    npm = shutil.which('npm', path=env['PATH'])
    if not npm:
        raise RuntimeError('Install npm alongside the supported Node.js runtime.')
    # Keep Fleet hooks and shared npm caches untouched. All build logic is upstream.
    env.update(HUSKY='0', npm_config_engine_strict='true',
               npm_config_cache=str((plugin / 'fleet/.cache/npm').resolve()),
               TURBO_TELEMETRY_DISABLED='1')
    subprocess.run([npm, 'ci'], cwd=plugin, env=env, check=True)
    subprocess.run([npm, 'run', 'build:cached'], cwd=plugin, env=env, check=True)
    # Turbo may restore an entire skills output tree. Assemble the five public
    # plugin exports after that restoration, without changing upstream sources.
    package_skills(plugin)
    subprocess.run([node, str(plugin / 'fleet/smoke.mjs'), str(plugin)], cwd=plugin, env=env, check=True)
    marker.write_text(json.dumps(identity, sort_keys=True) + '\n')
    return plugin, node, env
