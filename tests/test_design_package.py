from pathlib import Path
import hashlib
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / 'plugins/design'


class DesignPackageTests(unittest.TestCase):
    def test_owned_references_and_runtime_remain_complete(self):
        self.assertFalse((DESIGN / 'references/upstream').exists())
        for name in ('critique', 'accessibility', 'ux-copy', 'handoff',
                     'design-system', 'research-planning', 'research-synthesis'):
            self.assertTrue((DESIGN / 'references' / (name + '.md')).is_file())
        for path in DESIGN.rglob('*.md'):
            text = path.read_text().lower()
            if path == DESIGN / 'design-system/artifact-type/reference/format.md':
                # Exact forbidden filenames are part of the preserved runtime contract.
                text = text.replace('claude.local.md', '').replace('claude.md', '')
            self.assertNotIn('claude', text, str(path))
        # The bundled implementation retains its host contract during relocation.
        origin = json.loads((ROOT / 'docs/maintainers/design-provenance/origin.json').read_text())
        for name in ('index.html', 'artifact-type/app.js', 'artifact-type/app.css',
                     'artifact-type/demo.json', 'artifact-type/reference/sample-seazar-tokens.json'):
            expected = origin['sha256']['references/upstream/claude-design-system/' + name]
            self.assertEqual(hashlib.sha256((DESIGN / 'design-system' / name).read_bytes()).hexdigest(), expected)

    def test_active_package_has_no_original_connector_bindings(self):
        portable = json.loads((DESIGN / 'plugin.json').read_text())
        self.assertNotIn('apps', portable.get('extensions', {}).get('com.openai', {}))
        for name in ('.app.json', '.mcp.json', 'mcp.json'):
            self.assertFalse((DESIGN / name).exists(), name)
        self.assertEqual({p.parent.name for p in (DESIGN / 'skills').glob('*/SKILL.md')},
                         {'design', 'design-review', 'design-context', 'design-research'})
        self.assertFalse((ROOT / 'plugins/dots/skills/ui-design').exists())
        self.assertFalse((ROOT / 'plugins/dots/skills/ui-review').exists())


if __name__ == '__main__':
    unittest.main()
