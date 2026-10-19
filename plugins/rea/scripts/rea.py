#!/usr/bin/env python3
"""Run Fleet's source-built REA from any working directory."""
import os
import subprocess
import sys

from runtime import ensure_runtime

try:
    root, node, env = ensure_runtime()
    os.execve(node, [node, str(root / 'scripts/rea.mjs'), *sys.argv[1:]], env)
except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
    print(f'Fleet REA: {error}', file=sys.stderr)
    sys.exit(1)
