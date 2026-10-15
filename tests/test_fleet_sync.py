"""Publishing must precede apply; peer failures must remain visible."""
import importlib.util
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('fleet_sync', Path(__file__).resolve().parents[1] / 'scripts/sync-fleet.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class FleetSyncTests(unittest.TestCase):
    def result(self, stdout=''):
        return subprocess.CompletedProcess([], 0, stdout=stdout)

    def test_current_pull_still_applies_both_targets(self):
        with patch('sys.argv', ['sync', '--local']), patch.object(sync, 'run', side_effect=[self.result(), self.result('abc\n'), self.result(), self.result()]) as run:
            sync.main()
        self.assertEqual(run.call_args_list[0].args, ('git', 'pull', '--ff-only'))
        self.assertEqual([call.args[-1] for call in run.call_args_list[2:]], ['--apply', '--all'])

    def test_failed_push_prevents_apply(self):
        with patch('sys.argv', ['sync', '--after-commit']), patch.object(sync, 'run', side_effect=[self.result('main\n'), subprocess.CalledProcessError(1, 'push')]) as run:
            with self.assertRaises(subprocess.CalledProcessError):
                sync.main()
        self.assertEqual(run.call_count, 2)

    def test_wrong_peer_revision_prevents_apply(self):
        with patch('sys.argv', ['sync', '--local', '--expect', 'wanted']), patch.object(sync, 'run', side_effect=[self.result(), self.result('different\n')]) as run:
            with self.assertRaisesRegex(RuntimeError, 'differs'):
                sync.main()
        self.assertEqual(run.call_count, 2)

    def test_failed_target_does_not_skip_peers(self):
        peer = self.result('peer:/repo\n')
        with patch('sys.argv', ['sync', '--after-pull']):
            # Pull hooks deliberately remain local to avoid propagation loops.
            with patch.object(sync, 'run', side_effect=[self.result('abc'), subprocess.CalledProcessError(1, 'config'), self.result()]) as run:
                with self.assertRaisesRegex(RuntimeError, 'sync-configs'):
                    sync.main()
            self.assertEqual(run.call_count, 3)
        with patch('sys.argv', ['sync']), patch.object(sync.subprocess, 'run', return_value=peer), patch.object(sync, 'run', side_effect=[self.result(), self.result('abc'), subprocess.CalledProcessError(1, 'config'), self.result(), self.result()]) as run:
            with self.assertRaisesRegex(RuntimeError, 'sync-configs'):
                sync.main()
            self.assertEqual(run.call_args_list[-1].args[0], 'ssh')
            self.assertIn('--after-pull --local --expect abc', run.call_args_list[-1].args[-1])


if __name__ == '__main__':
    unittest.main()
