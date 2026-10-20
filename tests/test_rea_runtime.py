from pathlib import Path
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/rea'
spec = importlib.util.spec_from_file_location('rea_update', ROOT / 'scripts/update-rea.py')
update = importlib.util.module_from_spec(spec)
spec.loader.exec_module(update)
sys.path.insert(0, str(PLUGIN / 'fleet'))
import runtime


class ReaPackageTests(unittest.TestCase):
    def test_host_provider_environment_preserves_process_overrides(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / 'rea/environment.json'
            config.parent.mkdir()
            inherited = {'XDG_CONFIG_HOME': tmp, 'JAVA_HOME': '/process/jdk'}
            with patch.dict(os.environ, inherited, clear=True):
                self.assertEqual(runtime.configured_environment(), inherited)
                config.write_text(json.dumps({'JAVA_HOME': '/local/jdk', 'REA_ADB_PATH': '/local/adb'}))
                environment = runtime.configured_environment()
                self.assertEqual(environment['JAVA_HOME'], '/process/jdk')
                self.assertEqual(environment['REA_ADB_PATH'], '/local/adb')
                self.assertNotIn('REA_ADB_PATH', os.environ)

    def test_host_provider_environment_rejects_invalid_settings(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / 'rea/environment.json'
            config.parent.mkdir()
            with patch.dict(os.environ, {'XDG_CONFIG_HOME': tmp}, clear=True):
                for value in ([], {'PATH': '/replacement'}, {'REA_ADB_PATH': False}):
                    config.write_text(json.dumps(value))
                    with self.assertRaises(RuntimeError):
                        runtime.configured_environment()
                config.write_text('{')
                with self.assertRaises(ValueError):
                    runtime.configured_environment()

    def test_import_and_skills_match_upstream(self):
        origin = update.check()
        package = json.loads((PLUGIN / 'package.json').read_text())
        lock = json.loads((PLUGIN / 'package-lock.json').read_text())
        self.assertEqual(package['dependencies'], lock['packages']['']['dependencies'])
        self.assertIn('src/main.ts', origin['files'])
        self.assertEqual(len(list((PLUGIN / '.agents/skills').glob('*/SKILL.md'))), 5)
        self.assertEqual(len(list((PLUGIN / 'skills').rglob('SKILL.md'))), 5)

    def test_export_changes_only_links_for_the_new_directory_depth(self):
        original = (PLUGIN / '.agents/skills/rea-tool-design/SKILL.md').read_bytes()
        exported = update.exported_skills(PLUGIN)[Path('rea-tool-design/SKILL.md')]
        self.assertIn(b'(../../../docs/tool-design.md)', original)
        self.assertIn(b'(../../docs/tool-design.md)', exported)
        self.assertEqual(exported.replace(b'(../../', b'(../../../'), original)

    def test_refresh_preserves_packaging_and_refuses_local_edits_and_collisions(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, plugin = Path(tmp) / 'upstream', Path(tmp) / 'plugin'
            repo.mkdir()
            def git(*args):
                return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.DEVNULL)
            git('init', '--quiet')
            git('config', 'user.name', 'Fixture')
            git('config', 'user.email', 'fixture@example.invalid')
            source = repo / '.agents/skills'
            for name in ('reverse-engineer-anything', 'rea-tool-design'):
                (source / name).mkdir(parents=True)
                (source / name / 'SKILL.md').write_text('upstream skill\n')
            (repo / 'removed.txt').write_text('old\n')
            git('add', '.')
            git('commit', '--quiet', '-m', 'initial')
            shutil.copytree(repo, plugin, ignore=shutil.ignore_patterns('.git'))
            shutil.copytree(plugin / '.agents/skills/rea-tool-design', plugin / 'skills/rea-tool-design')
            (plugin / 'fleet').mkdir()
            files = {p.relative_to(repo).as_posix(): dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(), mode='100644')
                     for p in repo.rglob('*') if p.is_file() and '.git' not in p.relative_to(repo).parts}
            (plugin / 'fleet/upstream.json').write_text(json.dumps(dict(repository=str(repo), files=files)))
            (plugin / 'plugin.json').write_text('Fleet manifest')
            (plugin / 'removed.txt').write_text('local edit\n')
            with self.assertRaisesRegex(RuntimeError, 'Upstream file differs'):
                update.refresh('HEAD', plugin)
            (plugin / 'removed.txt').write_text('old\n')
            (repo / 'removed.txt').unlink()
            (repo / 'added.txt').write_text('new\n')
            (source / 'rea-tool-design/SKILL.md').write_text('updated skill\n')
            git('add', '.')
            git('commit', '--quiet', '-m', 'update')
            update.refresh('HEAD', plugin)
            self.assertFalse((plugin / 'removed.txt').exists())
            self.assertEqual((plugin / 'added.txt').read_text(), 'new\n')
            self.assertEqual((plugin / 'plugin.json').read_text(), 'Fleet manifest')
            self.assertEqual((plugin / 'skills/rea-tool-design/SKILL.md').read_text(), 'updated skill\n')
            update.check(plugin)
            (repo / 'plugin.json').write_text('collision')
            git('add', '.')
            git('commit', '--quiet', '-m', 'collision')
            with self.assertRaisesRegex(RuntimeError, 'package boundary'):
                update.refresh('HEAD', plugin)
            self.assertEqual((plugin / 'plugin.json').read_text(), 'Fleet manifest')

    def test_new_computer_setup_refuses_existing_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            cli = Path(tmp) / 'codex'
            cli.write_text('#!/usr/bin/env python3\nimport json,sys\nassert sys.argv[1:]==["plugin","list","--json"]\nprint(json.dumps({"installed":[{"pluginId":"rea@dots"}]}))\n')
            cli.chmod(0o755)
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/setup-rea.py'), '--client', 'codex'],
                                    env={**os.environ, 'PATH': tmp + os.pathsep + os.environ['PATH']}, text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Refusing to replace', result.stderr)


if __name__ == '__main__':
    unittest.main()
