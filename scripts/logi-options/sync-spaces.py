#!/usr/bin/env python3
"""Merge portable MX Master 4 Space gestures into every local Options+ profile."""
import argparse
import copy
import datetime
import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
PLIST = '/Library/LaunchAgents/com.logi.optionsplus.plist'
AGENT = '/Library/Application Support/Logitech.localized/LogiOptionsPlus/logioptionsplus_agent.app/Contents/MacOS/logioptionsplus_agent'
UI = '/Applications/logioptionsplus.app/Contents/MacOS/logioptionsplus'


def merge_gestures(live, wanted):
    """Match model slots, never profile UUIDs or paired-device identities."""
    result = copy.deepcopy(live)
    count = 0

    def visit(item):
        nonlocal count
        if isinstance(item, dict):
            if re.fullmatch(wanted['slotPattern'], item.get('slotId', '')):
                card = item['card']
                selected = wanted['selectedGesture']
                custom = card['nestedCards'][selected]
                nested = custom['nestedCards']
                if not all(key in nested for key in ('click', 'up', 'down', 'left', 'right')):
                    raise ValueError('Incomplete Logitech custom gesture schema; no settings written')
                card['selectedNestedCard'] = selected
                for direction, assignment in wanted['directions'].items():
                    nested[direction] = copy.deepcopy(assignment)
                count += 1
                return
            for value in item.values():
                visit(value)
        elif isinstance(item, list):
            for value in item:
                visit(value)
    visit(result)
    return result, count


def read_settings(db):
    rows = db.execute('SELECT file FROM data WHERE _id=1').fetchall()
    if len(rows) != 1:
        raise ValueError('Expected one Logitech settings row')
    return json.loads(rows[0][0])


def running(executable):
    return subprocess.run(['pgrep', '-f', '^' + re.escape(executable) + r'( --launchd)?$'],
                          stdout=subprocess.DEVNULL).returncode == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['apply', 'status'])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if sys.platform != 'darwin':
        return 0
    path = Path.home() / 'Library/Application Support/LogiOptionsPlus/settings.db'
    if not path.exists():
        print('Skipped Logitech gestures: Options+ database is not installed')
        return 0
    wanted = json.loads((ROOT / 'configs/logi-options-plus/spaces.json').read_text())
    with sqlite3.connect(f'file:{path}?mode=ro', uri=True) as db:
        live = read_settings(db)
    desired, count = merge_gestures(live, wanted)
    if not count:
        print('Skipped Logitech gestures: no configured MX Master 4 gesture slots')
        return 0
    if live == desired:
        print(f'Current Logitech Space gestures: {count} profile(s)')
        return 0
    if args.dry_run or args.operation == 'status':
        print(f'Drift: Logitech Space gestures in {count} profile(s)')
        return int(args.operation == 'status')

    service = f'gui/{os.getuid()}/com.logi.cp-dev-mgr'
    was_running = subprocess.run(['launchctl', 'print', service], capture_output=True).returncode == 0
    ui_running = running(UI)
    stopped = False
    try:
        if ui_running:
            subprocess.run(['pkill', '-TERM', '-f', '^' + re.escape(UI) + '$'], check=True)
        if was_running:
            subprocess.run(['launchctl', 'bootout', service], check=True)
            stopped = True
        for _ in range(50):
            if not running(AGENT) and not running(UI):
                break
            time.sleep(0.1)
        else:
            raise RuntimeError('Options+ did not stop; no settings written')
        # Re-read after shutdown; Options+ can flush changes while exiting.
        with sqlite3.connect(path) as db:
            live = read_settings(db)
            desired, count = merge_gestures(live, wanted)
            backup = path.with_name('settings.db.bak.spaces.' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
            backup.touch(mode=0o600, exist_ok=False)
            with sqlite3.connect(backup) as saved:
                db.backup(saved)
            backup.chmod(0o600)
            db.execute('UPDATE data SET file=? WHERE _id=1', (json.dumps(desired),))
        print(f'Applied Logitech Space gestures to {count} profile(s). Backup: {backup}')
    finally:
        if stopped:
            subprocess.run(['launchctl', 'bootstrap', f'gui/{os.getuid()}', PLIST], check=True)
        if ui_running:
            subprocess.run(['open', '/Applications/logioptionsplus.app'], check=True)
    # Verify persisted state after the agent has had a chance to load it.
    time.sleep(1)
    with sqlite3.connect(f'file:{path}?mode=ro', uri=True) as db:
        live = read_settings(db)
    if merge_gestures(live, wanted)[0] != live:
        raise RuntimeError('Logitech gestures changed after restart; verification failed')
    if was_running and not running(AGENT):
        raise RuntimeError('Logitech agent has not restarted')
    print('Verified saved Logitech gestures and agent restart; physical gesture test still required')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
