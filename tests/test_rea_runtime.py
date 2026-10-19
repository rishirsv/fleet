from pathlib import Path
import hashlib
import importlib.util
import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/rea'
spec = importlib.util.spec_from_file_location('fleet_rea_runtime', PLUGIN / 'scripts/runtime.py')
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


class ReaRuntimeTests(unittest.TestCase):
    def test_snapshot_is_the_build_source_and_has_locked_dependencies(self):
        origin, archive = runtime.source_identity()
        with zipfile.ZipFile(archive) as source:
            package = json.loads(source.read(origin['archive_root'] + '/package.json'))
            lock = json.loads(source.read(origin['archive_root'] + '/package-lock.json'))
            self.assertEqual(package['version'], origin['version'])
            self.assertEqual(package['dependencies'], lock['packages']['']['dependencies'])
            self.assertIsNotNone(source.getinfo(origin['archive_root'] + '/src/main.ts'))

    def test_rejects_modified_source_before_building(self):
        with tempfile.TemporaryDirectory() as tmp:
            plugin = Path(tmp)
            (plugin / 'runtime').mkdir()
            (plugin / 'runtime/source.zip').write_bytes(b'modified')
            (plugin / 'runtime/origin.json').write_text(json.dumps({'archive': 'source.zip', 'archive_sha256': 'incorrect'}))
            with self.assertRaisesRegex(RuntimeError, 'checksum'):
                runtime.source_identity(plugin)
            self.assertFalse((plugin / 'node_modules').exists())

    def test_archive_extraction_rejects_escapes_and_symlinks(self):
        for name, link in [('rea-main/../../escaped', False), ('/absolute', False),
                           ('rea-main/link', True), ('rea-main/..\\escaped', False)]:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                archive = Path(tmp) / 'source.zip'
                with zipfile.ZipFile(archive, 'w') as source:
                    info = zipfile.ZipInfo(name)
                    info.external_attr = (stat.S_IFLNK | 0o777) << 16 if link else 0
                    source.writestr(info, '../outside')
                with self.assertRaisesRegex(RuntimeError, 'Unsafe'):
                    runtime.extract_source(archive, Path(tmp) / 'out', 'rea-main')
                self.assertFalse((Path(tmp) / 'out').exists())

    def test_extraction_preserves_nested_files_and_executable_bits(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / 'source.zip'
            with zipfile.ZipFile(archive, 'w') as source:
                info = zipfile.ZipInfo('rea-main/scripts/rea.mjs')
                info.external_attr = (stat.S_IFREG | 0o755) << 16
                source.writestr(info, '#!/usr/bin/env node\n')
            destination = Path(tmp) / 'source'
            runtime.extract_source(archive, destination, 'rea-main')
            self.assertEqual((destination / 'scripts/rea.mjs').read_text(), '#!/usr/bin/env node\n')
            self.assertTrue((destination / 'scripts/rea.mjs').stat().st_mode & stat.S_IXUSR)

    def test_unsupported_node_does_not_create_a_build(self):
        result = subprocess.CompletedProcess([], 0, json.dumps(dict(version='25.5.0', abi='141', platform='darwin', arch='arm64')))
        with patch.object(runtime.shutil, 'which', return_value='/node'), patch.object(runtime.subprocess, 'run', return_value=result):
            with self.assertRaisesRegex(RuntimeError, 'unsupported'):
                runtime.toolchain()

    def test_ready_build_can_be_reused_without_npm_and_without_absolute_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            plugin = Path(tmp)
            identity = dict(source='digest', node_abi='137', platform='linux', arch='x64',
                            builder=hashlib.sha256(Path(runtime.__file__).read_bytes()).hexdigest())
            key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()[:24]
            build = plugin / 'node_modules/.fleet-rea' / key
            for relative in ['scripts/rea.mjs', 'dist/mcp/main.js', 'dist/cli-runtime/cli.js', 'node_modules/.package-lock.json']:
                p = build / relative
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('fixture')
            (build / '.fleet-ready.json').write_text(json.dumps(identity))
            with patch.object(runtime, 'source_identity', return_value=({'archive_sha256': 'digest'}, Path('/source.zip'))), \
                 patch.object(runtime, 'toolchain', return_value=('/node', {}, dict(abi='137', platform='linux', arch='x64'))), \
                 patch.object(runtime, 'run', side_effect=AssertionError('must not run npm')):
                self.assertEqual(runtime.ensure_runtime(plugin=plugin, build=False)[0], build)

    def test_new_computer_registration_refuses_an_existing_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            cli = Path(tmp) / 'codex'
            cli.write_text('#!/usr/bin/env python3\nimport json,sys\nassert sys.argv[1:]==["plugin","list","--json"]\nprint(json.dumps({"installed":[{"pluginId":"rea@dots"}]}))\n')
            cli.chmod(0o755)
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/setup-rea.py'), '--client', 'codex'],
                                    env={**os.environ, 'PATH': tmp + os.pathsep + os.environ['PATH']},
                                    text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Refusing to replace', result.stderr)
            self.assertNotIn('Building Fleet REA', result.stderr)


if __name__ == '__main__':
    unittest.main()
