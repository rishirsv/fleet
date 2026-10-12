from __future__ import annotations

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MERGER = ROOT / "scripts/plugin-sync/merge-codex-config.py"


class BrowserSyncTests(unittest.TestCase):
    def run_sync(self, source, target, *options):
        return subprocess.run(
            ["uv", "run", "--quiet", "--script", str(MERGER), "apply", "--browser",
             "--source", str(source), "--target", str(target), *options],
            capture_output=True, text=True,
        )

    def test_merge_preserves_rules_backs_up_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "browser/config.toml"
            target.parent.mkdir()
            before = 'approval_mode = "always_ask"\nwebmcp_enabled = false\n\n[origins]\n"https://example.com" = "deny"\n'
            target.write_text(before)
            source = ROOT / "configs/codex/browser.toml"
            preview = self.run_sync(source, target, "--dry-run")
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertEqual(target.read_text(), before)
            applied = self.run_sync(source, target)
            self.assertEqual(applied.returncode, 0, applied.stderr)
            self.assertIn('approval_mode = "never_ask"', target.read_text())
            self.assertIn('webmcp_enabled = false', target.read_text())
            self.assertIn('"https://example.com" = "deny"', target.read_text())
            self.assertEqual(list(target.parent.glob("config.toml.bak.*"))[0].read_text(), before)
            self.assertEqual(os.stat(target).st_mode & 0o777, 0o600)
            again = self.run_sync(source, target)
            self.assertEqual(again.returncode, 0, again.stderr)
            self.assertIn("Current", again.stdout)
            self.assertEqual(len(list(target.parent.glob("config.toml.bak.*"))), 1)

    def test_creates_missing_browser_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "browser/config.toml"
            result = self.run_sync(ROOT / "configs/codex/browser.toml", target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(target.read_bytes(), (ROOT / "configs/codex/browser.toml").read_bytes())

    def test_invalid_or_nonportable_source_does_not_change_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp) / "source.toml", Path(tmp) / "target.toml"
            target.write_text('approval_mode = "always_ask"\n')
            before = target.read_bytes()
            for invalid in ('approval_mode = "invalid"', 'full_cdp_access_enabled = 1',
                            '[origins]\n"https://example.com" = "allow"'):
                with self.subTest(source=invalid):
                    source.write_text(invalid)
                    result = self.run_sync(source, target)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertEqual(target.read_bytes(), before)
            self.assertFalse(list(target.parent.glob("target.toml.bak.*")))


if __name__ == "__main__":
    unittest.main()
