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

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/rea'
spec = importlib.util.spec_from_file_location('rea_update', ROOT / 'scripts/update-rea.py')
update = importlib.util.module_from_spec(spec)
spec.loader.exec_module(update)


class ReaPackageTests(unittest.TestCase):
    def test_import_and_skills_match_upstream(self):
        origin = update.check()
        package = json.loads((PLUGIN / 'package.json').read_text())
        lock = json.loads((PLUGIN / 'package-lock.json').read_text())
        self.assertEqual(package['dependencies'], lock['packages']['']['dependencies'])
        self.assertIn('src/main.ts', origin['files'])

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
            wrapper = plugin / 'fleet/skills/rea-growth'
            wrapper.mkdir(parents=True)
            (wrapper / 'SKILL.md').write_text('Fleet growth skill\n')
            (wrapper / 'LICENSE').write_text('third-party license\n')
            update.package_skills(plugin)
            (plugin / 'plugin.json').write_text('Fleet manifest')
            (plugin / 'removed.txt').write_text('local edit\n')
            with self.assertRaisesRegex(RuntimeError, 'Upstream file differs'):
                update.refresh('HEAD', plugin)
            (plugin / 'removed.txt').write_text('old\n')
            (repo / 'removed.txt').unlink()
            (repo / 'added.txt').write_text('new\n')
            (repo / '.codex-plugin').mkdir()
            (repo / '.codex-plugin/plugin.json').write_text('upstream manifest')
            (plugin / '.codex-plugin').mkdir()
            (plugin / '.codex-plugin/plugin.json').write_text('Fleet manifest')
            (source / 'rea-tool-design/SKILL.md').write_text('updated skill\n')
            git('add', '.')
            git('commit', '--quiet', '-m', 'update')
            update.refresh('HEAD', plugin)
            self.assertFalse((plugin / 'removed.txt').exists())
            self.assertEqual((plugin / 'added.txt').read_text(), 'new\n')
            self.assertEqual((plugin / 'plugin.json').read_text(), 'Fleet manifest')
            self.assertEqual((plugin / '.codex-plugin/plugin.json').read_text(), 'Fleet manifest')
            self.assertEqual((plugin / 'skills/rea-tool-design/SKILL.md').read_text(), 'updated skill\n')
            update.check(plugin)
            self.assertEqual((plugin / 'skills/rea-growth/SKILL.md').read_text(), 'Fleet growth skill\n')
            self.assertEqual((plugin / 'skills/rea-growth/LICENSE').read_text(), 'third-party license\n')
            # A source build/cache restore can erase the whole exported tree.
            shutil.rmtree(plugin / 'skills')
            update.package_skills(plugin)
            update.check(plugin)
            self.assertEqual((plugin / 'skills/rea-growth/LICENSE').read_text(), 'third-party license\n')
            (plugin / 'skills/rea-growth/LICENSE').write_text('drift')
            with self.assertRaisesRegex(RuntimeError, 'Packaged skills differ'):
                update.check(plugin)
            update.package_skills(plugin)
            (source / 'rea-growth').mkdir()
            (source / 'rea-growth/SKILL.md').write_text('upstream collision')
            git('add', '.')
            git('commit', '--quiet', '-m', 'skill collision')
            with self.assertRaisesRegex(RuntimeError, 'collides with upstream'):
                update.refresh('HEAD', plugin)
            self.assertEqual((plugin / 'skills/rea-growth/SKILL.md').read_text(), 'Fleet growth skill\n')
            self.assertEqual((plugin / 'fleet/upstream.json').read_text(), json.dumps(update.check(plugin), indent=2) + '\n')
            shutil.rmtree(source / 'rea-growth')
            (repo / 'plugin.json').write_text('collision')
            git('add', '.')
            git('commit', '--quiet', '-m', 'collision')
            with self.assertRaisesRegex(RuntimeError, 'package boundary'):
                update.refresh('HEAD', plugin)
            self.assertEqual((plugin / 'plugin.json').read_text(), 'Fleet manifest')

    def test_wrapper_collision_preserves_exports(self):
        with tempfile.TemporaryDirectory() as tmp:
            plugin = Path(tmp)
            upstream = plugin / '.agents/skills/rea-growth'
            wrapper = plugin / 'fleet/skills/rea-growth'
            exported = plugin / 'skills/rea-growth'
            for path in (upstream, wrapper, exported):
                path.mkdir(parents=True)
                (path / 'SKILL.md').write_text('keep this export')
            with self.assertRaisesRegex(RuntimeError, 'collides with upstream'):
                update.package_skills(plugin)
            self.assertEqual((exported / 'SKILL.md').read_text(), 'keep this export')

    def test_new_computer_setup_refuses_existing_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            cli = Path(tmp) / 'codex'
            cli.write_text('#!/usr/bin/env python3\nimport json,sys\nassert sys.argv[1:]==["plugin","list","--json"]\nprint(json.dumps({"installed":[{"pluginId":"rea@pstack"}]}))\n')
            cli.chmod(0o755)
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/setup-rea.py'), '--client', 'codex'],
                                    env={**os.environ, 'PATH': tmp + os.pathsep + os.environ['PATH']}, text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Refusing to replace', result.stderr)


if __name__ == '__main__':
    unittest.main()
