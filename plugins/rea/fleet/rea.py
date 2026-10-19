#!/usr/bin/env python3
"""Launch upstream REA without changing its CLI or rebuilding during MCP startup."""
import os
import subprocess
import sys
from runtime import ensure_runtime

try:
    root, node, env = ensure_runtime(build=False)
    os.execve(node, [node, str(root / 'scripts/rea.mjs'), *sys.argv[1:]], env)
except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
    print(f'Fleet REA: {error}', file=sys.stderr)
    sys.exit(1)
