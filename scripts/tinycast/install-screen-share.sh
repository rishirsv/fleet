#!/bin/bash
# Build the native Screen Sharing helper for a Tinycast custom command.
# Command: "$HOME/.local/share/pstack/tinycast/screen-share" SSH_ALIAS 3440 1440
# Requires Tinycast Accessibility permission, SSH key authentication, an
# existing Keychain screen-sharing login, and displayplacer on the remote Mac.
# Run on the matching ultrawide monitor. The helper checks the resulting size.
set -euo pipefail
source_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
install_dir="${1:-$HOME/.local/share/pstack/tinycast}"
mkdir -p "$install_dir"
build_path="$(mktemp "$install_dir/screen-share-build.XXXXXX")"
trap 'rm -f "$build_path"' EXIT
/usr/bin/swiftc -O "$source_dir/screen-share.swift" -o "$build_path"
chmod 755 "$build_path"
mv -f "$build_path" "$install_dir/screen-share"
printf 'Installed Screen Sharing helper.\n'
