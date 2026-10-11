#!/usr/bin/env zsh
set -euo pipefail
ROOT="${0:A:h:h}"
current=$(git -C "$ROOT" config --get core.hooksPath || true)
if [[ -n "$current" && "$current" != "$ROOT/scripts/git-hooks" ]]; then
  echo "Existing hooksPath ($current) must be integrated before installing Fleet hooks." >&2
  exit 1
fi
for hook in post-commit post-merge post-rewrite; do
  existing=$(git -C "$ROOT" rev-parse --path-format=absolute --git-path "hooks/$hook")
  if [[ -f "$existing" && "$current" != "$ROOT/scripts/git-hooks" ]]; then
    echo "Existing $hook hook must be integrated before installing Fleet hooks." >&2
    exit 1
  fi
done
git -C "$ROOT" config --local core.hooksPath "$ROOT/scripts/git-hooks"
echo "Installed Fleet hooks for $ROOT"
