from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/plugin-sync/claude-cache.py"
SPEC = importlib.util.spec_from_file_location("claude_cache", SCRIPT)
assert SPEC and SPEC.loader
cache = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cache)


class ClaudeSyncTests(unittest.TestCase):
    def test_detects_changed_added_and_retired_files_at_same_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp) / "source", Path(tmp) / "target"
            source.mkdir()
            target.mkdir()
            (source / "SKILL.md").write_text("current")
            (target / "SKILL.md").write_text("current")
            plugin = {"version": "1.0", "installPath": str(target)}
            self.assertTrue(cache.verify(source, plugin))
            (target / "SKILL.md").write_text("old")
            self.assertFalse(cache.verify(source, plugin))
            (target / "SKILL.md").write_text("current")
            (source / "new.md").write_text("new")
            self.assertFalse(cache.verify(source, plugin))
            (source / "new.md").unlink()
            (target / "retired.md").write_text("retired")
            self.assertFalse(cache.verify(source, plugin))

    def test_runtime_files_do_not_trigger_repair_and_local_source_is_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp) / "source", Path(tmp) / "target"
            source.mkdir()
            target.mkdir()
            for root in (source, target):
                (root / "SKILL.md").write_text("current")
            for marker in (".in_use", ".orphaned_at"):
                (target / marker).write_text("runtime")
            (target / "__pycache__").mkdir()
            (target / "__pycache__/module.pyc").write_bytes(b"bytecode")
            self.assertTrue(cache.verify(source, {"installPath": str(target)}))
            self.assertTrue(cache.verify(source, {
                "installPath": str(target / "missing"), "readFromFolder": str(source),
            }))

    def test_repair_uses_cli_preserves_data_and_disabled_state_then_verifies(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            (source / ".claude-plugin").mkdir()
            (source / ".claude-plugin/plugin.json").write_text("{}")
            plugin = {"version": "1.0", "enabled": False}
            with patch.object(cache, "installed_plugin", return_value=plugin), \
                 patch.object(cache, "verify", side_effect=[False, True]), \
                 patch.object(cache.subprocess, "run") as run:
                cache.sync(source, "pstack@pstack")
            self.assertEqual([call.args[0] for call in run.call_args_list], [
                ["claude", "plugin", "uninstall", "pstack@pstack", "--scope", "user", "--keep-data"],
                ["claude", "plugin", "install", "pstack@pstack", "--scope", "user"],
                ["claude", "plugin", "disable", "pstack@pstack", "--scope", "user"],
            ])
            with patch.object(cache, "installed_plugin", return_value=plugin), \
                 patch.object(cache, "verify", side_effect=[False, False]), \
                 patch.object(cache.subprocess, "run"):
                with self.assertRaisesRegex(ValueError, "still differs"):
                    cache.sync(source, "pstack@pstack")

    def test_only_user_installation_is_selected(self):
        user = {"id": "pstack@pstack", "scope": "user"}
        project = {"id": "pstack@pstack", "scope": "project"}
        with patch.object(cache.subprocess, "check_output", return_value=json.dumps([project, user])):
            self.assertEqual(cache.installed_plugin("pstack@pstack"), user)
        with patch.object(cache.subprocess, "check_output", return_value=json.dumps([project])):
            with self.assertRaisesRegex(ValueError, "one user installation"):
                cache.installed_plugin("pstack@pstack")

    def test_current_cache_does_not_reinstall(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            (source / ".claude-plugin").mkdir()
            (source / ".claude-plugin/plugin.json").write_text("{}")
            with patch.object(cache, "installed_plugin", return_value={}), \
                 patch.object(cache, "verify", return_value=True), \
                 patch.object(cache.subprocess, "run") as run:
                cache.sync(source, "pstack@pstack")
            run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
