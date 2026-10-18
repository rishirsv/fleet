#!/usr/bin/env python3
"""Merge only Fleet's selected macOS and Tinycast Space shortcuts."""
import argparse
import datetime
import json
from pathlib import Path
import plistlib
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def read_domain(domain):
    result = subprocess.run(['defaults', 'export', domain, '-'], capture_output=True)
    if result.returncode:
        raise RuntimeError(f'Cannot read preferences: {domain}')
    return plistlib.loads(result.stdout)


def changes(wanted, native, tinycast):
    edits = []
    for key, value in wanted['AppleSymbolicHotKeys'].items():
        if native.get('AppleSymbolicHotKeys', {}).get(key) != value:
            edits.append(('com.apple.symbolichotkeys', key, value))
    if tinycast is not None:
        for key, value in wanted['tinycast'].items():
            if (key in tinycast if value is None else tinycast.get(key) != value):
                edits.append(('com.tinycast.app', key, value))
    return edits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['apply', 'status'])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if sys.platform != 'darwin':
        return 0
    wanted = json.loads((ROOT / 'configs/macos/spaces.json').read_text())
    native = read_domain('com.apple.symbolichotkeys')
    tiny_path = Path.home() / 'Library/Preferences/com.tinycast.app.plist'
    tinycast = read_domain('com.tinycast.app') if tiny_path.exists() else None
    edits = changes(wanted, native, tinycast)
    if not edits:
        print('Current: Space shortcuts')
        return 0
    if args.operation == 'status' or args.dry_run:
        for domain, key, _ in edits:
            print(f'Drift: {domain} {key}')
        return int(args.operation == 'status')
    backup = Path.home() / 'Library/Application Support/Fleet/backups' / datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    backup.mkdir(parents=True, mode=0o700)
    for domain in sorted({edit[0] for edit in edits}):
        subprocess.run(['defaults', 'export', domain, str(backup / (domain + '.plist'))], check=True, capture_output=True)
        (backup / (domain + '.plist')).chmod(0o600)
    # defaults uses CFPreferences so running preference daemons cannot overwrite
    # a directly edited plist. Never replace unrelated shortcut entries.
    for domain, key, value in edits:
        if domain == 'com.apple.symbolichotkeys':
            xml = plistlib.dumps(value).decode()
            command = ['defaults', 'write', domain, 'AppleSymbolicHotKeys', '-dict-add', key, xml]
        elif value is None:
            command = ['defaults', 'delete', domain, key]
        else:
            command = ['defaults', 'write', domain, key, '-string', value]
        subprocess.run(command, check=True)
    activate = Path('/System/Library/PrivateFrameworks/SystemAdministration.framework/Resources/activateSettings')
    subprocess.run([str(activate), '-u'], check=True)
    print(f'Applied Space shortcuts. Backup: {backup}')
    print('Restart Tinycast to reload its shortcuts; log out/in if macOS retains old bindings.')
    remaining = changes(wanted, read_domain('com.apple.symbolichotkeys'),
                        read_domain('com.tinycast.app') if tinycast is not None else None)
    if remaining:
        raise RuntimeError('Space shortcut verification failed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
