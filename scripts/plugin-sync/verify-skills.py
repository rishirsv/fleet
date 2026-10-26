#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["tomlkit==0.13.3"]
# ///
"""Verify the selected Fleet plugin source through Codex's actual skill loader."""

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import selectors
import subprocess
import sys
import time

import tomlkit


EXCLUSION_MARKER = "# fleet:source-exclusion "


def reconcile_source_exclusions(config, skills, policy):
    """Work around loaders ignoring plugin.enabled; own only marked path rows."""
    before = config.read_text()
    doc = tomlkit.parse(before)
    rows = doc.get("skills", {}).get("config", [])
    unwanted = {
        skill["path"]: skill for skill in skills
        if skill.get("pluginId") in policy
        and not policy[skill["pluginId"]]["enabled"]
    }
    # A running desktop can still hold a cloud catalog that a fresh loader omits.
    # Cover every cached version until it is removed or the source is selected.
    for plugin_id, settings in policy.items():
        if settings["enabled"]:
            continue
        name, marketplace = plugin_id.rsplit("@", 1)
        cache = config.parent / "plugins" / "cache" / marketplace / name
        for path in sorted(cache.glob("*/skills/*/SKILL.md")):
            unwanted.setdefault(str(path), {
                "path": str(path), "pluginId": plugin_id,
                "name": f"{name}:{path.parent.name}", "enabled": True,
            })
    # Source switches and removed cache versions retire only unchanged entries.
    for index in range(len(rows) - 1, -1, -1):
        row = rows[index]
        marker = row.trivia.comment
        if not marker.startswith(EXCLUSION_MARKER):
            continue
        parts = marker[len(EXCLUSION_MARKER):].split()
        if len(parts) != 2:
            continue
        owner, path_hash = parts
        if set(row) != {"path", "enabled"} or row["enabled"] is not False:
            continue  # A user changed the entry; do not take it over.
        if hashlib.sha256(row["path"].encode()).hexdigest() != path_hash:
            continue
        skill = unwanted.get(row["path"])
        if skill is None or skill["pluginId"] != owner:
            del rows[index]
    existing_paths = {row.get("path") for row in rows}
    existing_names = {row.get("name") for row in rows}
    for path, skill in unwanted.items():
        if not skill["enabled"] or path in existing_paths or skill["name"] in existing_names:
            continue  # Preserve explicit user choices, even if verification fails.
        if "skills" not in doc:
            doc["skills"] = tomlkit.table()
        if "config" not in doc["skills"]:
            doc["skills"]["config"] = tomlkit.aot()
            rows = doc["skills"]["config"]
        row = tomlkit.table()
        path_hash = hashlib.sha256(path.encode()).hexdigest()
        row.comment(f"{EXCLUSION_MARKER.removeprefix('# ')}{skill['pluginId']} {path_hash}")
        row["path"] = path
        row["enabled"] = False
        rows.append(row)
        existing_paths.add(path)
    after = tomlkit.dumps(doc)
    if after == before:
        return False
    # Reuse the config merger's backup and atomic-write behavior.
    spec = importlib.util.spec_from_file_location(
        "fleet_config_merge", Path(__file__).with_name("merge-codex-config.py"))
    merger = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = merger
    spec.loader.exec_module(merger)
    if config.read_text() != before:
        raise RuntimeError("Codex config changed during sync; retry after the other writer finishes")
    merger.backup_target(config)
    merger.atomic_write(config, after.encode(), 0o600)
    print(f"Reconciled Fleet skill source exclusions in {config}")
    return True


def loaded_skills(cwd):
    process = subprocess.Popen(
        ["codex", "app-server"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL, text=True,
    )
    selector = selectors.DefaultSelector()
    selector.register(process.stdout, selectors.EVENT_READ)
    pending = b""

    def request(request_id, method, params):
        nonlocal pending
        process.stdin.write(json.dumps({"id": request_id, "method": method, "params": params}) + "\n")
        process.stdin.flush()
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            if b"\n" not in pending:
                if not selector.select(max(0, deadline - time.monotonic())):
                    break
                chunk = os.read(process.stdout.fileno(), 65536)
                if not chunk:
                    raise RuntimeError("Codex exited before returning its skill inventory")
                pending += chunk
                continue
            line, pending = pending.split(b"\n", 1)
            response = json.loads(line)
            if response.get("id") == request_id:
                if "error" in response:
                    raise RuntimeError(str(response["error"]))
                return response["result"]
        raise RuntimeError("Codex skill inventory timed out")

    try:
        request(1, "initialize", {
            "clientInfo": {"name": "pstack_skill_verification", "version": "1.0"},
            "capabilities": {"experimentalApi": True},
        })
        # The desktop loads account plugins explicitly. A fresh CLI server
        # otherwise sees only local plugins and can falsely certify duplicates
        # as absent. Fetch the same account catalog before scanning skills.
        request(2, "plugin/list", {
            "marketplaceKinds": ["local", "created-by-me-remote"],
            "forceRefetch": True,
        })
        result = request(3, "skills/list", {"cwds": [str(cwd)], "forceReload": True})
        return [skill for entry in result["data"] for skill in entry["skills"]]
    finally:
        selector.close()
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        process.stdin.close()
        process.stdout.close()


def verify(skills, policy):
    enabled = [skill for skill in skills if skill["enabled"] and skill.get("pluginId") in policy]
    present = {skill["pluginId"] for skill in enabled}
    errors = []
    for plugin_id, settings in policy.items():
        if settings["enabled"] and plugin_id not in present:
            errors.append(f"{plugin_id}: selected plugin has no enabled skills")
        elif not settings["enabled"] and plugin_id in present:
            errors.append(f"{plugin_id}: duplicate copy is still enabled")
    names = {}
    for skill in skills:
        if not skill["enabled"]:
            continue
        name = skill["name"]
        names.setdefault(name, []).append(skill["path"])
    for name, paths in names.items():
        if len(paths) > 1:
            errors.append(f"{name}: loaded {len(paths)} copies")
    return errors, len(enabled)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--cwd", type=Path, required=True)
    parser.add_argument("--repair-source-exclusions", action="store_true",
                        help="Maintain profile-local path exclusions when the loader ignores plugin policy")
    args = parser.parse_args()
    policy = tomlkit.parse(args.policy.read_text()).unwrap()["plugins"]
    skills = loaded_skills(args.cwd)
    if args.repair_source_exclusions:
        home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
        if reconcile_source_exclusions(home / "config.toml", skills, policy):
            skills = loaded_skills(args.cwd)  # A fresh process must prove the repair.
    errors, count = verify(skills, policy)
    if errors:
        raise SystemExit("Codex skill verification failed:\n  " + "\n  ".join(errors))
    print(f"Codex loaded {count} Fleet plugin skills from the selected source, with zero duplicate skill names across all sources")


if __name__ == "__main__":
    main()
