"""Selected desktop bindings must not absorb unrelated preferences."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('spaces', ROOT / 'scripts/sync-spaces.py')
spaces = importlib.util.module_from_spec(spec)
spec.loader.exec_module(spaces)


class SpaceSyncTests(unittest.TestCase):
    def setUp(self):
        self.wanted = json.loads((ROOT / 'configs/macos/spaces.json').read_text())

    def test_only_selected_keys_change(self):
        native = {'AppleSymbolicHotKeys': {'99': {'enabled': True}}}
        tiny = {'unrelated': 'preserve', **{key: 'old' for key in self.wanted['tinycast']}}
        edits = spaces.changes(self.wanted, native, tiny)
        self.assertEqual([(d, k) for d, k, _ in edits], [
            ('com.apple.symbolichotkeys', '79'), ('com.apple.symbolichotkeys', '81'),
            ('com.tinycast.app', 'hotkey.windowCommand.previous-space'),
            ('com.tinycast.app', 'hotkey.windowCommand.next-space')])
        self.assertEqual(native['AppleSymbolicHotKeys']['99'], {'enabled': True})
        self.assertEqual(tiny['unrelated'], 'preserve')

    def test_absent_tinycast_keys_are_current_but_assigned_keys_are_removed(self):
        native = {'AppleSymbolicHotKeys': self.wanted['AppleSymbolicHotKeys']}
        self.assertEqual(spaces.changes(self.wanted, native, {}), [])
        self.assertEqual(spaces.changes(self.wanted, native, None), [])
        key = 'hotkey.windowCommand.next-space'
        self.assertEqual(spaces.changes(self.wanted, native, {key: 'old'}),
                         [('com.tinycast.app', key, None)])
