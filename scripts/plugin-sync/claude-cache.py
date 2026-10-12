#!/usr/bin/env python3
"""Verify a user plugin against its refreshed marketplace, repairing stale caches."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


# Claude adds lifecycle markers; runtimes may add bytecode and dependencies.
IGNORED = {".git", ".in_use", ".orphaned_at", "__pycache__", "node_modules"}


def contents(root: Path) -> dict[str, bytes]:
    if not root.is_dir():
        raise ValueError(f"Plugin directory is missing: {root}")
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file() and not IGNORED.intersection(path.relative_to(root).parts)
    }


def installed_plugin(plugin_id: str) -> dict:
    plugins = json.loads(subprocess.check_output(
        ["claude", "plugin", "list", "--json"], text=True,
    ))
    matches = [p for p in plugins if p.get("id") == plugin_id and p.get("scope") == "user"]
    if len(matches) != 1:
        raise ValueError(f"Expected one user installation of {plugin_id}, got {len(matches)}")
    return matches[0]


def verify(source: Path, plugin: dict) -> bool:
    # Local marketplaces can load directly from their source directory.
    target = Path(plugin.get("readFromFolder") or plugin["installPath"])
    return target.is_dir() and contents(source) == contents(target)


def sync(source: Path, plugin_id: str) -> None:
    # Validate the source before changing an installation.
    if not (source / ".claude-plugin" / "plugin.json").is_file():
        raise ValueError(f"Missing Claude plugin manifest: {source}")
    plugin = installed_plugin(plugin_id)
    if not verify(source, plugin):
        print(f"Repairing stale Claude cache for {plugin_id} (version {plugin['version']})", flush=True)
        disabled = plugin.get("enabled") is False
        subprocess.run([
            "claude", "plugin", "uninstall", plugin_id, "--scope", "user", "--keep-data",
        ], check=True)
        try:
            subprocess.run(["claude", "plugin", "install", plugin_id, "--scope", "user"], check=True)
        finally:
            if disabled:
                subprocess.run(["claude", "plugin", "disable", plugin_id, "--scope", "user"], check=True)
        if not verify(source, installed_plugin(plugin_id)):
            raise ValueError(f"Claude cache still differs from the refreshed marketplace: {plugin_id}")
    print(f"Claude cache content verified: {plugin_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("plugin_id")
    args = parser.parse_args()
    try:
        sync(args.source, args.plugin_id)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Claude cache verification failed: {exc}\n")


if __name__ == "__main__":
    main()
