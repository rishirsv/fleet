#!/usr/bin/env python3
"""Read-only checks for Fleet prerequisites; optionally inspect configuration drift."""
import argparse
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def inspect(profile=None):
    checks = [('Python 3.10+', sys.version_info >= (3, 10), 'Use Python 3.10 or newer.')]
    for command in ('git', 'zsh', 'uv', 'codex', 'node', 'claude', 'code'):
        checks.append((command, shutil.which(command) is not None,
                       f'Install {command} or add it to PATH.'))
    profiles = [Path(profile or os.environ.get('CODEX_HOME', Path.home() / '.codex'))]
    personal = Path.home() / '.codex-personal'
    if not profile and personal.is_dir() and personal not in profiles:
        profiles.append(personal)
    for directory in profiles:
        selection = directory / 'dots-plugin-source'
        source = selection.read_text().strip() if selection.is_file() else 'local'
        checks.append((f'{directory.name} plugin source: {source}', source in {'cloud', 'local'},
                       'Choose cloud or local with sync-plugins.sh --codex --source.'))
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--configs', action='store_true', help='also run read-only config drift checks')
    parser.add_argument('--profile', type=Path, help='select a Codex profile')
    args = parser.parse_args()
    checks = inspect(args.profile)
    failed = sum(not passed for _, passed, _ in checks)
    for name, passed, remedy in checks:
        print(f'{"OK" if passed else "MISSING"}  {name}' + ('' if passed else f' — {remedy}'))
    if shutil.which('git'):
        result = subprocess.run(['git', '-C', str(ROOT), 'config', '--get', 'core.hooksPath'],
                                capture_output=True, text=True)
        configured = result.stdout.strip()
        if not configured:
            print('INFO  Fleet hooks not installed: run scripts/install-hooks.sh if wanted.')
        else:
            path = Path(configured).expanduser()
            if not path.is_absolute():
                path = ROOT / path
            if path.resolve() != (ROOT / 'scripts/git-hooks').resolve():
                print('INFO  Custom Git hooks: integrate them before installing Fleet hooks.')
            else:
                print('OK  Fleet hooks installed for this checkout')
    if platform.system() == 'Darwin':
        for name, path in [('Ghostty', Path('/Applications/Ghostty.app')),
                           ('Karabiner-Elements', Path('/Applications/Karabiner-Elements.app')),
                           ('Paper Mono', Path.home() / 'Library/Fonts/PaperMono-Regular.otf')]:
            present = path.exists() or (name != 'Paper Mono' and (Path.home() / 'Applications' / path.name).exists())
            print(f'{"OK" if present else "INFO"}  {name}' + ('' if present else ' is not installed.'))
        print('INFO  Verify Karabiner input/accessibility permissions in macOS settings; file checks cannot confirm them.')
    else:
        print('INFO  Caps Lock mapping and font installation are currently macOS-only.')
    print('INFO  App sign-ins and Tunnel authorization remain app-managed; doctor does not change them.')
    if args.configs:
        command = ['zsh', str(ROOT / 'scripts/sync-configs.sh'), '--status']
        if args.profile:
            command.extend(['--profile', str(args.profile)])
        if shutil.which('zsh'):
            failed += subprocess.run(command, check=False).returncode != 0
    print(f'Doctor: {failed} prerequisite/config check(s) need attention.' if failed else 'Doctor: prerequisites passed.')
    return int(bool(failed))


if __name__ == '__main__':
    raise SystemExit(main())
