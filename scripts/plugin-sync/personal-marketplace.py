#!/usr/bin/env python3
"""Register Fleet as personal plugins and retain local/cloud identity links."""

import json
from pathlib import Path
import sys

import tomlkit


root, profile = (Path(arg).resolve() for arg in sys.argv[1:])
home = Path.home().resolve()
catalog_path = home / ".agents/plugins/marketplace.json"
catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text())
for entry in catalog["plugins"]:
    source = (root / entry["source"]["path"]).resolve()
    entry["source"]["path"] = "./" + str(source.relative_to(home))

if catalog_path.exists():
    previous = json.loads(catalog_path.read_text())
    if previous.get("name") != catalog["name"]:
        raise SystemExit(f"Personal marketplace already belongs to {previous.get('name')}")
    owned = {entry["name"] for entry in catalog["plugins"]}
    catalog["plugins"] += [entry for entry in previous["plugins"] if entry["name"] not in owned]

config_path = profile / "config.toml"
before = config_path.read_text()
config = tomlkit.parse(before)
marketplace = config.get("marketplaces", {}).get(catalog["name"])
if marketplace is not None:
    if marketplace.get("source_type") != "local" or marketplace.get("source") not in {str(root), str(home)}:
        raise SystemExit("Fleet marketplace has another source; refusing to replace it")
    marketplace["source"] = str(home)

catalog_path.parent.mkdir(parents=True, exist_ok=True)
catalog_path.write_text(json.dumps(catalog, indent=2) + "\n")
after = tomlkit.dumps(config)
if after != before:
    # Reuse Fleet's config backup and atomic-write behavior.
    import importlib.util
    spec = importlib.util.spec_from_file_location("fleet_merge", Path(__file__).with_name("merge-codex-config.py"))
    merger = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = merger
    spec.loader.exec_module(merger)
    merger.backup_target(config_path)
    merger.atomic_write(config_path, after.encode(), 0o600)

identities_path = profile / "plugin-local-identities.json"
if identities_path.exists():
    identities = json.loads(identities_path.read_text())
    links_path = profile / ".tmp/plugin-share-local-paths-v1.json"
    links = json.loads(links_path.read_text()) if links_path.exists() else {}
    paths = links.setdefault("localPluginPathsByRemotePluginId", {})
    for entry in catalog["plugins"]:
        if entry["name"] in identities:
            paths[identities[entry["name"]]] = str((home / entry["source"]["path"]).resolve())
    links_path.parent.mkdir(parents=True, exist_ok=True)
    links_path.write_text(json.dumps(links, indent=2) + "\n")
