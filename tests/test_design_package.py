from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / 'plugins/design'


class DesignPackageTests(unittest.TestCase):
    def test_active_package_has_no_original_connector_bindings(self):
        portable = json.loads((DESIGN / 'plugin.json').read_text())
        self.assertNotIn('apps', portable.get('extensions', {}).get('com.openai', {}))
        for name in ('.app.json', '.mcp.json', 'mcp.json'):
            self.assertFalse((DESIGN / name).exists(), name)



if __name__ == '__main__':
    unittest.main()
