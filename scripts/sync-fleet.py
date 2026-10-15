#!/usr/bin/env python3
"""Pull/apply Fleet locally and on explicitly configured SSH peers."""
import argparse
import os
from pathlib import Path
import shlex
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(*args, capture=False):
    return subprocess.run(args, cwd=ROOT, check=True, text=True,
                          stdout=subprocess.PIPE if capture else None,
                          env={**os.environ, "FLEET_SYNC_ACTIVE": "1"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--after-commit', action='store_true')
    mode.add_argument('--after-pull', action='store_true')
    parser.add_argument('--local', action='store_true', help='do not contact peers')
    parser.add_argument('--expect', help='require this revision after pulling (peer verification)')
    args = parser.parse_args()
    if args.after_commit:
        branch = run('git', 'symbolic-ref', '--short', 'HEAD', capture=True).stdout.strip()
        run('git', 'push', '--set-upstream', 'origin', branch)
    elif not args.after_pull:
        run('git', 'pull', '--ff-only')
    revision = run('git', 'rev-parse', 'HEAD', capture=True).stdout.strip()
    if args.expect and args.expect != revision:
        raise RuntimeError('Peer checkout differs from the requested revision; reconcile its branch manually.')

    failures = []
    for script, option in [('sync-configs.sh', '--apply'), ('sync-plugins.sh', '--all')]:
        try:
            run(str(ROOT / 'scripts' / script), option)
        except subprocess.CalledProcessError:
            failures.append(script)
    if not args.local and not args.after_pull:
        peers = subprocess.run(['git', 'config', '--local', '--get-all', 'fleet.syncPeer'],
                               cwd=ROOT, text=True, stdout=subprocess.PIPE, check=False)
        if peers.returncode not in (0, 1):
            raise RuntimeError('Cannot read Fleet peer configuration')
        for peer in peers.stdout.splitlines():
            # Private host aliases and absolute checkout paths live in .git/config.
            host, separator, path = peer.partition(':')
            if not separator or not host or host.startswith('-') or not path.startswith('/'):
                failures.append(f'invalid peer: {peer}')
                continue
            command = (f'cd {shlex.quote(path)} && '
                       'FLEET_SYNC_ACTIVE=1 git pull --ff-only && '
                       f'python3 scripts/sync-fleet.py --after-pull --local --expect {shlex.quote(revision)}')
            print(f'Fleet: syncing {host}', flush=True)
            try:
                run('ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=10', host,
                    'zsh -lc ' + shlex.quote(command))
            except subprocess.CalledProcessError:
                failures.append(host)
    if failures:
        raise RuntimeError('Sync incomplete: ' + ', '.join(failures) + '. Retry scripts/sync-fleet.py.')


if __name__ == '__main__':
    try:
        main()
    except (subprocess.CalledProcessError, RuntimeError) as error:
        print(f'Fleet: {error}', file=sys.stderr)
        sys.exit(1)
