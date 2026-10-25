#!/usr/bin/env python3
"""Build Fleet's bundled REA; optionally register it on a new computer."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'plugins/rea/fleet'))
from runtime import ensure_runtime


def prepare_installed(client: str, built: Path) -> None:
    """Prime only the installation just created, before the client starts MCP."""
    version = json.loads((ROOT / 'plugins/rea/plugin.json').read_text())['version']
    if client == 'codex':
        home = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
        installed = home / 'plugins/cache/pstack/rea' / version
    else:
        home = Path(os.environ.get('CLAUDE_CONFIG_DIR', str(Path.home() / '.claude')))
        registry = json.loads((home / 'plugins/installed_plugins.json').read_text())
        entries = registry['plugins']['rea@pstack']
        entry = next(p for p in entries if p['scope'] == 'user')
        installed = Path(entry.get('readFromFolder') or entry['installPath'])
    # Do not write into an unrelated or unexpectedly resolved package.
    for relative in ('mcp.json', 'fleet/upstream.json', 'fleet/runtime.py'):
        if (installed / relative).read_bytes() != (ROOT / 'plugins/rea' / relative).read_bytes():
            raise RuntimeError(f'{client} installed a different REA package at {installed}; leaving it untouched.')
    # Only prime the installation this invocation just created. Upstream's
    # normal build produces these relocatable outputs; no alternate build recipe.
    for relative in ('node_modules', 'dist', 'skills/reverse-engineer-anything'):
        destination = installed / relative
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(built / relative, destination, symlinks=True)
    ensure_runtime(plugin=installed, build=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--client', choices=('none', 'codex', 'claude', 'both'), default='none',
                        help='Register only REA with this client; default none leaves installed plugins/config unchanged.')
    args = parser.parse_args()
    clients = ['codex', 'claude'] if args.client == 'both' else ([] if args.client == 'none' else [args.client])
    for client in clients:
        if not shutil.which(client):
            parser.error(f'{client} CLI is required for --client {args.client}; install it separately.')
        command = [client, 'plugin', 'list', '--json']
        listing = subprocess.run(command, check=True, text=True, capture_output=True)
        data = json.loads(listing.stdout)
        installed = data.get('installed', []) if isinstance(data, dict) else data
        if any(p.get('name') == 'rea' or p.get('pluginId', p.get('id', '')).split('@', 1)[0] == 'rea' for p in installed):
            parser.error(f'{client} already has REA installed. Refusing to replace an installation that other projects may use. Run without --client to prepare Fleet only; migrate explicitly after those projects finish.')
    subprocess.run([sys.executable, str(ROOT / 'scripts/update-rea.py')], check=True)
    runtime, node, env = ensure_runtime()
    for client in clients:
        # REA alone: never invoke the Fleet-wide sync or upstream `rea setup`.
        if client == 'codex':
            commands = [[client, 'plugin', 'marketplace', 'add', str(ROOT)],
                        [client, 'plugin', 'add', 'rea@pstack']]
        else:
            commands = [[client, 'plugin', 'marketplace', 'add', str(ROOT), '--scope', 'user'],
                        [client, 'plugin', 'install', 'rea@pstack', '--scope', 'user']]
        for command in commands:
            subprocess.run(command, check=True, env=env)
        prepare_installed(client, runtime)
    print(f'Fleet REA ready: {runtime}')
    print('Launch: python3 plugins/rea/fleet/rea.py mcp')
    if clients:
        print('Registered and prepared for ' + ', '.join(clients) + '. Start a new chat when ready.')
    else:
        print('Repository-only setup complete; installed plugins and client configuration were not changed.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        print(f'Fleet REA setup failed: {error}', file=sys.stderr)
        raise SystemExit(1)
