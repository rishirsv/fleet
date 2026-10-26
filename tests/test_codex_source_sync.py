"""Exercise source reconciliation through the CLI with an isolated Codex loader."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / 'scripts/plugin-sync/verify-skills.py'
FAKE_CODEX = '''#!/usr/bin/env python3
import json, os, sys, tomllib
from pathlib import Path
for line in sys.stdin:
    request = json.loads(line)
    result = {}
    if request['method'] == 'skills/list':
        config = tomllib.loads((Path(os.environ['CODEX_HOME']) / 'config.toml').read_text())
        rows = config.get('skills', {}).get('config', [])
        skills = json.loads(os.environ['TEST_SKILLS'])
        for skill in skills:
            for row in rows:
                if row.get('path') == skill['path'] or row.get('name') == skill['name']:
                    skill['enabled'] = row['enabled']
        result = {'data': [{'skills': skills}]}
    print(json.dumps({'id': request['id'], 'result': result}), flush=True)
'''


class CodexSourceSyncTests(unittest.TestCase):
    def test_cached_cloud_versions_stay_excluded_when_fresh_loader_omits_them(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / 'codex'
            binary.write_text(FAKE_CODEX)
            binary.chmod(0o755)
            config = root / 'config.toml'
            config.write_text('model = "unchanged"\n')
            policy = root / 'policy.toml'
            policy.write_text('[plugins."pstack@created-by-me-remote"]\nenabled = false\n')
            cached = []
            for version in ('1', '2'):
                path = root / 'plugins/cache/created-by-me-remote/pstack' / version / 'skills/bro/SKILL.md'
                path.parent.mkdir(parents=True)
                path.write_text('---\nname: bro\n---\n')
                cached.append(path)
            env = {**os.environ, 'CODEX_HOME': str(root),
                   'PATH': f'{root}:' + os.environ['PATH'], 'TEST_SKILLS': '[]'}
            args = ['uv', 'run', '--quiet', '--script', str(VERIFIER),
                    '--policy', str(policy), '--cwd', str(root), '--repair-source-exclusions']
            for _ in range(2):
                result = subprocess.run(args, env=env, text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                for path in cached:
                    self.assertIn(str(path), config.read_text())
            self.assertEqual(len(list(root.glob('config.toml.bak.*'))), 1)
            # Retire only a version actually removed from the cache.
            cached[0].unlink()
            result = subprocess.run(args, env=env, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn(str(cached[0]), config.read_text())
            self.assertIn(str(cached[1]), config.read_text())

    def test_local_runtime_coexists_with_cloud_skills_and_excludes_legacy_copy(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / 'codex'
            binary.write_text(FAKE_CODEX)
            binary.chmod(0o755)
            config = root / 'config.toml'
            config.write_text('model = "unchanged"\n')
            policy = root / 'policy.toml'
            policy.write_text(
                '[plugins."pstack@created-by-me-remote"]\nenabled = true\n'
                '[plugins."rea@pstack"]\nenabled = true\n'
                '[plugins."rea@rea-local"]\nenabled = false\n')
            skills = [
                dict(name='pstack:pstack', path='/cloud/pstack/SKILL.md', enabled=True,
                     pluginId='pstack@created-by-me-remote'),
                dict(name='rea:reverse-engineer-anything', path='/fleet/rea/SKILL.md',
                     enabled=True, pluginId='rea@pstack'),
                dict(name='rea:reverse-engineer-anything', path='/legacy/rea/SKILL.md',
                     enabled=True, pluginId='rea@rea-local'),
            ]
            env = {**os.environ, 'CODEX_HOME': str(root),
                   'PATH': f'{root}:' + os.environ['PATH'], 'TEST_SKILLS': json.dumps(skills)}
            args = ['uv', 'run', '--quiet', '--script', str(VERIFIER),
                    '--policy', str(policy), '--cwd', str(root)]
            failed = subprocess.run(args, env=env, text=True, capture_output=True)
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn('loaded 2 copies', failed.stderr)
            repaired = subprocess.run(args + ['--repair-source-exclusions'], env=env,
                                      text=True, capture_output=True)
            self.assertEqual(repaired.returncode, 0, repaired.stderr)
            self.assertIn('loaded 2 Fleet plugin skills', repaired.stdout)
            self.assertIn('/legacy/rea/SKILL.md', config.read_text())
            self.assertNotIn('/fleet/rea/SKILL.md', config.read_text())
            self.assertNotIn('/cloud/pstack/SKILL.md', config.read_text())
            self.assertIn('model = "unchanged"', config.read_text())

    def test_repair_upgrade_source_switch_and_user_ownership(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / 'codex'
            binary.write_text(FAKE_CODEX)
            binary.chmod(0o755)
            config = root / 'config.toml'
            user_rows = '\n[[skills.config]]\npath = "/user/disabled"\nenabled = false\n'
            config.write_text('model = "unchanged"\n' + user_rows)
            policy = root / 'policy.toml'
            def set_policy(cloud):
                policy.write_text('[plugins."pstack@pstack"]\nenabled = ' + str(not cloud).lower() +
                                  '\n[plugins."pstack@created-by-me-remote"]\nenabled = ' + str(cloud).lower())
            def run(version='1', repair=True):
                skills = [dict(name='pstack:pstack', path=f'/cloud/{version}/SKILL.md', enabled=True,
                               pluginId='pstack@created-by-me-remote'),
                          dict(name='pstack:pstack', path='/local/SKILL.md', enabled=True, pluginId='pstack@pstack')]
                env = {**os.environ, 'CODEX_HOME': str(root), 'PATH': f'{root}:' + os.environ['PATH'],
                       'TEST_SKILLS': json.dumps(skills)}
                args = ['uv', 'run', '--quiet', '--script', str(VERIFIER), '--policy', str(policy), '--cwd', str(root)]
                if repair:
                    args.append('--repair-source-exclusions')
                return subprocess.run(args, env=env, text=True, capture_output=True)
            set_policy(False)
            failed = run(repair=False)
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn('loaded 2 copies', failed.stderr)
            result = run()
            self.assertEqual(result.returncode, 0, result.stderr)
            first = config.read_text()
            self.assertIn('# fleet:source-exclusion pstack@created-by-me-remote', first)
            self.assertIn(user_rows, first)
            self.assertIn('model = "unchanged"', first)
            self.assertEqual(len(list(root.glob('config.toml.bak.*'))), 1)
            self.assertEqual(run().returncode, 0)
            self.assertEqual(first, config.read_text())
            self.assertEqual(len(list(root.glob('config.toml.bak.*'))), 1)
            upgraded = run('2')
            self.assertEqual(upgraded.returncode, 0, upgraded.stderr)
            self.assertNotIn('/cloud/1/', config.read_text())
            self.assertIn('/cloud/2/', config.read_text())
            set_policy(True)
            switched = run('2')
            self.assertEqual(switched.returncode, 0, switched.stderr)
            self.assertNotIn('/cloud/', config.read_text())
            self.assertIn('/local/SKILL.md', config.read_text())
            self.assertIn(user_rows, config.read_text())
            config.write_text(config.read_text().replace('/local/SKILL.md', '/user/changed'))
            set_policy(False)
            edited = run('2')
            self.assertEqual(edited.returncode, 0, edited.stderr)
            self.assertIn('/user/changed', config.read_text())
            # A conflicting user-owned rule must fail visibly, never be overwritten.
            set_policy(True)
            config.write_text('[[skills.config]]\npath = "/local/SKILL.md"\nenabled = true\n')
            before = config.read_text()
            self.assertNotEqual(run('2').returncode, 0)
            self.assertEqual(config.read_text(), before)


if __name__ == '__main__':
    unittest.main()
