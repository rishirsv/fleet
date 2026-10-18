"""Portable gesture patches preserve unrelated profiles and device assignments."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('logi_spaces', ROOT / 'scripts/logi-options/sync-spaces.py')
logi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(logi)


class LogiSpacesTests(unittest.TestCase):
    def setUp(self):
        self.wanted = json.loads((ROOT / 'configs/logi-options-plus/spaces.json').read_text())
        self.slot = {'slotId': 'mx-master-4-other-model-id_c416', 'card': {
            'selectedNestedCard': 'media_control',
            'nestedCards': {'media_control': {'unrelated': True}, 'custom_gesture': {
                'gestureInfo': {'sensitivity': 42},
                'nestedCards': {key: {'old': key} for key in ['click', 'up', 'down', 'left', 'right']}}}}}

    def test_all_profiles_patch_without_copying_private_ids_or_other_settings(self):
        live = {'private-profile-1': {'assignments': [self.slot, {'slotId': 'unrelated', 'value': 123}]},
                'private-profile-2': {'assignments': [copy.deepcopy(self.slot)]}, 'account': 'keep-local'}
        original = copy.deepcopy(live)
        result, count = logi.merge_gestures(live, self.wanted)
        self.assertEqual(count, 2)
        self.assertEqual(live, original)
        for key in ['private-profile-1', 'private-profile-2']:
            card = result[key]['assignments'][0]['card']
            self.assertEqual(card['selectedNestedCard'], 'custom_gesture')
            custom = card['nestedCards']['custom_gesture']
            for direction in ['click', 'up', 'down']:
                self.assertEqual(custom['nestedCards'][direction], {'old': direction})
            self.assertEqual(custom['gestureInfo'], {'sensitivity': 42})
            self.assertEqual(card['nestedCards']['media_control'], {'unrelated': True})
        self.assertEqual(result['account'], 'keep-local')
        self.assertEqual(result['private-profile-1']['assignments'][1], original['private-profile-1']['assignments'][1])
        self.assertEqual(logi.merge_gestures(result, self.wanted), (result, 2))

    def test_unsupported_mouse_untouched(self):
        self.slot['slotId'] = 'other-mouse_c416'
        self.assertEqual(logi.merge_gestures(self.slot, self.wanted), (self.slot, 0))

    def test_incomplete_schema_fails_before_mutating_input(self):
        del self.slot['card']['nestedCards']['custom_gesture']['nestedCards']['up']
        before = copy.deepcopy(self.slot)
        with self.assertRaisesRegex(ValueError, 'Incomplete'):
            logi.merge_gestures(self.slot, self.wanted)
        self.assertEqual(self.slot, before)
