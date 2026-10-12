"""Real stdio routing and isolation; no account, network or SSH required."""
import asyncio
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from mcp_types import CallToolRequestParams, CallToolResult, TextContent

from router import Handles, create_router, load_computers
from runtime import server_command, validate_folders
from test_protocol import Wire


class RouterWire(Wire):
    def __init__(self, config):
        self.process = subprocess.Popen(
            [sys.executable, str(Path(__file__).with_name('router.py')), '--config', str(config)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        self.sequence = 0


class RouterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='tunnel-router-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.computers = {}
        for name in ('mac', 'akira'):
            root = self.base / name
            root.mkdir()
            (root / 'note.txt').write_text(name + '\n')
            self.computers[name] = {
                'command': [sys.executable, str(Path(__file__).with_name('server.py')),
                            '--mount', f'Code={root}', '--state', str(self.base / (name + '-recovery'))],
                'expected_host': platform.node()}
        self.config = self.base / 'router.json'
        self.start()

    def start(self):
        self.config.write_text(json.dumps({'computers': self.computers}))
        self.wire = RouterWire(self.config)
        self.addCleanup(self.wire.close)

    def tool(self, name, arguments):
        result = self.wire.send('tools/call', {'name': name, 'arguments': arguments})
        self.assertNotIn('error', result, result)
        return result['result']

    def test_catalog_is_available_without_connecting_and_requires_computer(self):
        catalog = self.wire.send('tools/list')['result']['tools']
        self.assertEqual(catalog[0]['name'], 'list_computers')
        for tool in catalog[1:]:
            self.assertIn('computer', tool['inputSchema']['required'])
            self.assertEqual(tool['inputSchema']['properties']['computer']['enum'], ['mac', 'akira'])
        data = self.tool('list_computers', {})['structuredContent']
        self.assertEqual([item['computer'] for item in data['computers']], ['mac', 'akira'])
        for arguments in ({'path': 'Code/note.txt'}, {'computer': 'other', 'path': 'Code/note.txt'},
                          {'computer': 'mac', 'path': 'Code/note.txt', 'endpoint': '/tmp/anything'}):
            self.assertTrue(self.tool('read_file', arguments)['isError'])

    def test_identical_paths_edits_stale_revisions_and_switch_back(self):
        first = self.tool('read_file', {'computer': 'akira', 'path': 'Code/note.txt'})['structuredContent']
        self.assertEqual(first['content'], 'akira\n')
        patch = '*** Begin Patch\n*** Update File: Code/note.txt\n@@\n-akira\n+edited\n*** End Patch'
        result = self.tool('apply_patch', {'computer': 'akira', 'input': patch, 'expected_revision': first['revision']})
        self.assertFalse(result.get('isError', False), result)
        self.assertEqual((self.base / 'akira/note.txt').read_text(), 'edited\n')
        self.assertEqual((self.base / 'mac/note.txt').read_text(), 'mac\n')
        self.assertTrue(self.tool('apply_patch', {'computer': 'akira', 'input': patch,
                                                'expected_revision': first['revision']})['isError'])
        for computer, expected in (('mac', 'mac\n'), ('akira', 'edited\n')):
            result = self.tool('read_file', {'computer': computer, 'path': 'Code/note.txt'})
            self.assertEqual(result['structuredContent']['content'], expected)
            self.assertEqual(result['_meta']['dots/computer'], computer)
        workflow = self.tool('get_workflow', {'computer': 'akira'})['structuredContent']
        self.assertIn('Every tool call requires computer', workflow['skill'])
        self.assertTrue(self.tool('read_file', {'computer': 'akira', 'path': 'Code/.env'})['isError'])
        self.assertTrue(self.tool('exec_command', {'computer': 'akira', 'cmd': 'true'})['isError'])

    def test_host_mismatch_fails_before_mutation_and_other_host_survives(self):
        self.computers['akira']['expected_host'] = 'definitely-not-this-host.invalid'
        self.start()
        result = self.tool('manage_files', {'computer': 'akira', 'action': 'write',
                                           'path': 'Code/new.txt', 'content': 'must not be written'})
        self.assertTrue(result['isError'])
        self.assertFalse((self.base / 'akira/new.txt').exists())
        self.assertFalse((self.base / 'mac/new.txt').exists())
        result = self.tool('read_file', {'computer': 'mac', 'path': 'Code/note.txt'})
        self.assertEqual(result['structuredContent']['content'], 'mac\n')

    def test_offline_host_is_not_replaced_by_other_host(self):
        self.computers['akira']['command'] = ['/usr/bin/false']
        self.start()
        self.assertTrue(self.tool('read_file', {'computer': 'akira', 'path': 'Code/note.txt'})['isError'])
        self.assertEqual(self.tool('read_file', {'computer': 'mac', 'path': 'Code/note.txt'})['structuredContent']['content'], 'mac\n')
        self.assertTrue(self.tool('read_file', {'computer': 'akira', 'path': 'Code/note.txt'})['isError'])

    def test_recovery_copy_is_bound_to_computer_and_text_matches(self):
        first = self.tool('read_file', {'computer': 'akira', 'path': 'Code/note.txt'})['structuredContent']
        deleted = self.tool('manage_files', {'computer': 'akira', 'action': 'delete',
                                            'path': 'Code/note.txt', 'expected_revision': first['revision']})
        recovery = deleted['structuredContent']['recovery_copy']
        self.assertEqual(json.loads(deleted['content'][0]['text'])['recovery_copy'], recovery)
        denied = self.tool('manage_files', {'computer': 'mac', 'action': 'restore',
                                           'path': 'Code/copy.txt', 'recovery_copy': recovery})
        self.assertTrue(denied['isError'])
        self.assertFalse((self.base / 'mac/copy.txt').exists())
        restored = self.tool('manage_files', {'computer': 'akira', 'action': 'restore',
                                             'path': 'Code/note.txt', 'recovery_copy': recovery})
        self.assertFalse(restored.get('isError', False), restored)
        self.assertEqual((self.base / 'akira/note.txt').read_text(), 'akira\n')

    def test_config_rejects_tool_config_and_nonabsolute_executable(self):
        for config in ({}, {'computers': {}}, {'computers': {'mac': {'command': ['python'], 'expected_host': 'mac'}}},
                       {'computers': {'mac': {'command': ['/bin/true'], 'expected_host': 'mac', 'env': {}}}}):
            self.config.write_text(json.dumps(config))
            with self.assertRaises(ValueError):
                load_computers(self.config)

    def test_runtime_selects_router_and_protects_its_configuration(self):
        config = {'python': sys.executable, 'mounts': {'Code': str(self.base / 'mac')},
                  'state': str(self.base / 'recovery'), 'router_config': str(self.config)}
        command = server_command(config)
        self.assertEqual(Path(command[1]).name, 'router.py')
        self.assertEqual(command[2:], ['--config', str(self.config)])
        config['router_config'] = str(self.base / 'mac/router.json')
        with self.assertRaisesRegex(ValueError, 'overlaps trusted'):
            validate_folders(config)

    def test_worker_can_load_saved_config_without_mount_arguments(self):
        directory = self.base / 'private'
        directory.mkdir()
        (directory / 'config.json').write_text(json.dumps({
            'tunnel_id': 'existing-identity', 'python': sys.executable,
            'mounts': {'Code': str(self.base / 'mac')}, 'state': str(self.base / 'recovery'),
            'approved_parents': [str(self.base / 'mac')]}))
        self.computers['mac']['command'] = [sys.executable, str(Path(__file__).with_name('server.py')),
                                            '--config-directory', str(directory)]
        self.start()
        result = self.tool('read_file', {'computer': 'mac', 'path': 'Code/note.txt'})
        self.assertEqual(result['structuredContent']['content'], 'mac\n')

    def test_coordinator_configuration_cannot_be_remotely_mounted(self):
        state = self.base.parent / (self.base.name + '-recovery')
        self.addCleanup(shutil.rmtree, state, True)
        self.computers['mac']['command'] = [sys.executable, str(Path(__file__).with_name('server.py')),
                                            '--mount', f'Code={self.base}', '--state', str(state)]
        self.start()
        result = self.tool('read_file', {'computer': 'mac', 'path': 'Code/router.json'})
        self.assertTrue(result['isError'])


class HandleTests(unittest.IsolatedAsyncioTestCase):
    async def test_colliding_backend_ids_are_translated_and_wrong_host_is_not_called(self):
        calls = []

        async def fake_call(backend, name, arguments):
            calls.append((backend.name, name, arguments))
            data = {'session_id': 7, 'operation_id': 9}
            return CallToolResult(content=[TextContent(type='text', text=json.dumps(data))], structured_content=data)

        router = await create_router({name: {'command': ['/bin/false'], 'expected_host': name} for name in ('mac', 'akira')})
        handler = router._request_handlers['tools/call'].handler

        async def call(name, **arguments):
            return await handler(None, CallToolRequestParams(name=name, arguments=arguments))

        with patch('router.Backend.call', fake_call):
            mac = await call('exec_command', computer='mac', cmd='true')
            akira = await call('exec_command', computer='akira', cmd='true')
            self.assertNotEqual(mac.structured_content['session_id'], akira.structured_content['session_id'])
            self.assertEqual(json.loads(mac.content[0].text), mac.structured_content)
            before = len(calls)
            denied = await call('write_stdin', computer='akira', session_id=mac.structured_content['session_id'])
            self.assertTrue(denied.is_error)
            self.assertEqual(len(calls), before)
            await call('write_stdin', computer='mac', session_id=mac.structured_content['session_id'])
            self.assertEqual(calls[-1], ('mac', 'write_stdin', {'session_id': 7}))
            await call('tunnel_manage', computer='akira', action='result', operation_id=akira.structured_content['operation_id'])
            self.assertEqual(calls[-1][2]['operation_id'], 9)
            denied = await call('tunnel_manage', computer='mac', action='result', operation_id=akira.structured_content['operation_id'])
            self.assertTrue(denied.is_error)

    async def test_nested_status_and_handle_types_keep_identity(self):
        handles = Handles()
        data = handles.result('mac', {'execution': {'active_operations': [9], 'retained_results': [9]}})
        self.assertEqual(data['execution']['active_operations'], data['execution']['retained_results'])
        identifier = data['execution']['active_operations'][0]
        self.assertEqual(handles.decode('mac', 'operation_id', identifier), 9)
        for host, kind in (('akira', 'operation_id'), ('mac', 'session_id')):
            with self.assertRaises(ValueError):
                handles.decode(host, kind, identifier)


if __name__ == '__main__':
    unittest.main()
