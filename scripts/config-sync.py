#!/usr/bin/env python3
"""Merge selected JSON settings, shortcuts, and guidance; install editor extensions."""
import argparse
import copy
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def parse_jsonc(text):
    # Strip comments and trailing commas without changing quoted strings.
    out = []
    i = 0
    while i < len(text):
        if text[i] == '"':
            start = i
            i += 1
            while i < len(text):
                if text[i] == '\\':
                    i += 2
                elif text[i] == '"':
                    i += 1
                    break
                else:
                    i += 1
            out.append(text[start:i])
        elif text.startswith('//', i):
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
        elif text.startswith('/*', i):
            end = text.find('*/', i + 2)
            if end < 0:
                raise ValueError('Unterminated JSON comment')
            out.append(' ')
            i = end + 2
        else:
            if text[i] == ',':
                # Comments can occur after a trailing comma; strip first.
                out.append(',')
            else:
                out.append(text[i])
            i += 1
    text = ''.join(out)
    out = []
    i = 0
    quoted = False
    while i < len(text):
        c = text[i]
        if quoted and c == '\\':
            out.extend(text[i:i + 2]); i += 2; continue
        if c == '"':
            quoted = not quoted
        if not quoted and c == ',':
            j = i + 1
            while j < len(text) and text[j].isspace():
                j += 1
            if j < len(text) and text[j] in '}]':
                i += 1; continue
        out.append(c)
        i += 1
    return json.loads(''.join(out))


def merge_format(live, wanted, kind):
    if kind == 'vscode-keys':
        keys = {(normalized_key(item['key']), item.get('when')) for item in wanted}
        return [item for item in live if (normalized_key(item['key']), item.get('when')) not in keys] + wanted
    if kind == 'claude-keys':
        result = copy.deepcopy(live)
        blocks = result.setdefault('bindings', [])
        for block in wanted['bindings']:
            matches = [entry for entry in blocks if entry['context'] == block['context']]
            owned_keys = {normalized_key(key) for key in block['bindings']}
            for entry in matches:
                entry['bindings'] = {key: action for key, action in entry['bindings'].items()
                                     if normalized_key(key) not in owned_keys}
            blocks.append(copy.deepcopy(block))
        # Fold contexts so repeating sync doesn't append duplicate blocks.
        merged = {}
        for block in blocks:
            merged.setdefault(block['context'], {}).update(block['bindings'])
        result['bindings'] = [{'context': context, 'bindings': bindings} for context, bindings in merged.items()]
        return result
    if kind == 'karabiner':
        result = copy.deepcopy(live)
        profiles = result.setdefault('profiles', [{'name': 'Default', 'selected': True}])
        selected = [profile for profile in profiles if profile.get('selected')]
        if len(selected) != 1:
            raise ValueError('Karabiner needs exactly one selected profile')
        profile = selected[0]
        rules = profile.setdefault('complex_modifications', {}).setdefault('rules', [])
        wanted_rule = wanted['rules'][0]
        for item in profile.get('simple_modifications', []):
            if item.get('from', {}).get('key_code') == 'caps_lock':
                raise ValueError('Existing Caps Lock simple modification needs integration')
        for device in profile.get('devices', []):
            if any(item.get('from', {}).get('key_code') == 'caps_lock' for item in device.get('simple_modifications', [])):
                raise ValueError('Existing device Caps Lock modification needs integration')
        for rule in rules:
            if any(item.get('from', {}).get('key_code') == 'caps_lock' for item in rule.get('manipulators', [])):
                if rule.get('manipulators') == wanted_rule['manipulators']:
                    return result
                raise ValueError('Existing Caps Lock rule differs; integrate before applying')
        rules.append(copy.deepcopy(wanted_rule))
        return result
    return overlay(live, wanted)


def normalized_key(key):
    aliases = {'command': 'cmd', 'control': 'ctrl', 'option': 'alt', 'meta': 'alt', 'super': 'cmd'}
    return tuple(tuple(sorted(aliases.get(part.lower(), part.lower()) for part in chord.split('+')))
                 for chord in key.split())


def overlay(live, wanted):
    result = dict(live)
    for key, value in wanted.items():
        if isinstance(value, dict):
            current = result.get(key, {})
            if not isinstance(current, dict):
                raise ValueError(f'Cannot merge object into scalar setting: {key}')
            result[key] = overlay(current, value)
        else:
            result[key] = value
    return result


def merge_codex_keys(wanted, live):
    commands = {item['command'] for item in wanted}
    result = [item for item in live if item['command'] not in commands]
    for item in wanted:
        if item['key'] is not None:
            for other in result:
                if other['key'] is not None and normalized_key(other['key']) == normalized_key(item['key']):
                    raise ValueError(f"Shortcut conflict: {item['key']} already belongs to {other['command']}")
        result.append(item)
    return result


START = '<!-- fleet:shared-guidance:start -->'
END = '<!-- fleet:shared-guidance:end -->'


def merge_guidance(current, guidance):
    block = f'{START}\n{guidance.strip()}\n{END}'
    if current.count(START) != current.count(END) or current.count(START) > 1:
        raise ValueError('Ambiguous Fleet guidance markers; repair them before syncing')
    if START in current:
        first, last = current.index(START), current.index(END)
        if last < first:
            raise ValueError('Fleet guidance markers are reversed')
        return current[:first] + block + current[last + len(END):]
    return current.rstrip() + ('\n\n' if current.strip() else '') + block + '\n'


def sync_extensions(wanted, operation, dry_run):
    code = shutil.which('code')
    if code is None:
        print('VS Code CLI missing: enable the code command on PATH.')
        return 0 if dry_run else 1
    result = subprocess.run([code, '--list-extensions'], capture_output=True, text=True, check=True)
    installed = {line.strip().lower() for line in result.stdout.splitlines()}
    missing = [extension for extension in wanted if extension.lower() not in installed]
    if operation == 'status':
        print('Missing VS Code extensions: ' + ', '.join(missing) if missing else 'Current VS Code extensions')
        return int(bool(missing))
    for extension in missing:
        if dry_run:
            print(f'Would install VS Code extension {extension}')
        else:
            subprocess.run([code, '--install-extension', extension], check=True)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['apply', 'status'])
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--target', type=Path)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--format', choices=['settings', 'codex-keys', 'vscode-keys',
                                            'claude-keys', 'karabiner', 'guidance', 'extensions'],
                        default='settings')
    args = parser.parse_args()
    if args.format == 'extensions':
        return sync_extensions(json.loads(args.source.read_text()), args.operation, args.dry_run)
    if args.target is None:
        parser.error('--target is required for file sync')
    before = args.target.read_bytes() if args.target.exists() else None
    if args.format == 'guidance':
        live = before.decode('utf-8') if before is not None else ''
        after = merge_guidance(live, args.source.read_text())
        data = after.encode('utf-8')
    else:
        live = parse_jsonc(before.decode('utf-8-sig')) if before is not None else (
            [] if args.format in {'codex-keys', 'vscode-keys'} else {})
        wanted = json.loads(args.source.read_text())
        after = merge_codex_keys(wanted, live) if args.format == 'codex-keys' else merge_format(live, wanted, args.format)
        data = (json.dumps(after, indent=2) + '\n').encode('utf-8')
    if after == live and args.target.is_file() and not args.target.is_symlink():
        print(f'Current {args.target}')
        return 0
    if args.operation == 'status':
        print(f'Drift {args.target}')
        return 1
    if args.dry_run:
        print(f'Would merge {args.format} into {args.target}')
        return 0
    args.target.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=args.target.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
        current = args.target.read_bytes() if args.target.exists() else None
        if current != before:
            raise ValueError('Live file changed during sync; retry')
        if before is not None:
            stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            backup = args.target.with_name(args.target.name + '.bak.' + stamp)
            backup.write_bytes(before)
            backup.chmod(0o600)
        os.replace(temporary, args.target)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print(f'Applied {args.format} to {args.target}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
