"""One stdio MCP interface, explicit computer selection, isolated backend sessions.

Run only from trusted deployment with an operator-owned configuration. Backend
commands are fixed locally; tool callers cannot supply commands or endpoints.
"""
import argparse
import asyncio
from contextlib import asynccontextmanager
from copy import deepcopy
import json
from pathlib import Path
import platform
import re
import secrets
import sys

import anyio
from jsonschema import validate
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp_types import CallToolResult, ListToolsResult, TextContent, Tool, ToolAnnotations

from server import create_server
from branding import icons


def load_computers(path):
    """Local-only startup configuration; never read from tool arguments."""
    computers = json.loads(path.read_text()).get('computers')
    if not isinstance(computers, dict) or not 1 <= len(computers) <= 8:
        raise ValueError('Configure between one and eight computers')
    for name, config in computers.items():
        if not re.fullmatch(r'[a-z][a-z0-9-]{0,31}', name):
            raise ValueError('Computer names must be lowercase identifiers')
        if not isinstance(config, dict) or set(config) != {'command', 'expected_host'}:
            raise ValueError('Each computer needs command and expected_host only')
        command, host = config['command'], config['expected_host']
        if (not isinstance(command, list) or not command
                or not all(isinstance(arg, str) and arg and '\x00' not in arg for arg in command)
                or not Path(command[0]).is_absolute()
                or not isinstance(host, str) or not host):
            raise ValueError('Use an absolute executable, string arguments, and a nonempty expected_host')
    return computers


def failure(computer, message):
    return CallToolResult(is_error=True, content=[TextContent(type='text', text=f'{computer}: {message}')])


class Handles:
    """Router handles never collide across hosts or leak backend handles."""
    def __init__(self):
        self.forward = {}
        self.reverse = {}

    def encode(self, computer, kind, value):
        key = (computer, kind, value)
        if key not in self.reverse:
            public = secrets.token_hex(24) if kind == 'recovery_copy' else secrets.randbits(53)
            while (kind, public) in self.forward:
                public = secrets.token_hex(24) if kind == 'recovery_copy' else secrets.randbits(53)
            self.reverse[key] = public
            self.forward[kind, public] = (computer, value)
        return self.reverse[key]

    def decode(self, computer, kind, value):
        host, backend = self.forward.get((kind, value), (None, None))
        if host != computer:
            raise ValueError('Handle belongs to another computer or router process')
        return backend

    def result(self, computer, value):
        if isinstance(value, list):
            return [self.result(computer, item) for item in value]
        if not isinstance(value, dict):
            return value
        result = {}
        for key, item in value.items():
            if key in {'session_id', 'operation_id', 'recovery_copy'} and item is not None:
                result[key] = self.encode(computer, key, item)
            elif key in {'active_operations', 'retained_results'} and isinstance(item, list):
                result[key] = [self.encode(computer, 'operation_id', identifier) for identifier in item]
            else:
                result[key] = self.result(computer, item)
        return result


class Backend:
    """A single owner task enters/exits SDK cancel scopes and retains handles.

    A failed connection stays failed until operator restart. No automatic
    reconnect, mutation replay, or fallback to another computer.
    """
    def __init__(self, name, config, protected_paths=()):
        self.name, self.config = name, config
        self.protected_paths = [Path(__file__).resolve().parent, *protected_paths]
        self.queue = asyncio.Queue(maxsize=16)
        self.task = None
        self.failed = False

    async def call(self, name, arguments):
        if self.failed:
            return failure(self.name, 'Connection unavailable; inspect effects before retrying. Operator restart required.')
        future = asyncio.get_running_loop().create_future()
        try:
            self.queue.put_nowait((name, arguments, future))
        except asyncio.QueueFull:
            return failure(self.name, 'Too many queued requests; this request was not sent.')
        if self.task is None:
            self.task = asyncio.create_task(self.run())
        # Cancellation cannot safely establish whether a mutation took effect.
        # Keep its result collector alive, and never replay the operation.
        return await asyncio.shield(future)

    async def run(self):
        current = None
        try:
            command = self.config['command']
            async with stdio_client(StdioServerParameters(command=command[0], args=command[1:])) as streams:
                async with ClientSession(*streams, read_timeout_seconds=360) as session:
                    with anyio.fail_after(20):
                        await session.initialize()
                        catalog = await session.list_tools()
                        workflow = await session.call_tool('get_workflow', {})
                    if workflow.is_error or not workflow.structured_content:
                        raise ValueError('Backend cannot identify itself')
                    if workflow.structured_content.get('host') != self.config['expected_host']:
                        raise ValueError('Backend host does not match expected_host')
                    if self.config['expected_host'] == platform.node():
                        for root in workflow.structured_content.get('roots', {}).values():
                            root = Path(root).resolve()
                            if any(root == path or root in path.parents for path in self.protected_paths):
                                raise ValueError('Local mount exposes trusted router source or configuration')
                    supported = {tool.name: tool.input_schema for tool in catalog.tools}
                    while True:
                        name, arguments, current = await self.queue.get()
                        if name not in supported:
                            result = failure(self.name, 'Tool unavailable on this computer; request was not sent.')
                        else:
                            validate(arguments, supported[name])
                            result = await session.call_tool(name, arguments)
                            if not isinstance(result, CallToolResult):
                                raise ValueError('Interactive MCP result is unsupported')
                            result = result.model_copy(deep=True)
                            result.meta = {**(result.meta or {}), 'dots/computer': self.name}
                            if name == 'get_workflow' and result.structured_content:
                                result.structured_content['skill'] = (
                                    'This is a multi-computer Tunnel. Every tool call requires computer. '
                                    'Use only the computer the user named; ask if none is selected. '
                                    'Keep paths, revisions, recovery copies, session IDs and operation IDs '
                                    'paired with that computer. Never fall back to another host.\n\n'
                                    + result.structured_content.get('skill', ''))
                        if not current.done():
                            current.set_result(result)
                        current = None
        except asyncio.CancelledError:
            raise
        except Exception:
            # Do not expose configured commands, SSH diagnostics or local paths.
            self.failed = True
        finally:
            self.failed = True
            result = failure(self.name, 'Connection failed or identity mismatch. Effects may be uncertain; no operation was replayed. Operator restart required.')
            if current is not None and not current.done():
                current.set_result(result)
            while not self.queue.empty():
                _, _, future = self.queue.get_nowait()
                if not future.done():
                    future.set_result(result)

    async def close(self):
        if self.task is not None:
            self.task.cancel()
            await asyncio.gather(self.task, return_exceptions=True)


async def create_router(computers, protected_paths=()):
    backends = {name: Backend(name, config, protected_paths) for name, config in computers.items()}
    handles = Handles()
    # Reuse the maintained server's schemas without opening files or starting
    # execution. These placeholders are never invoked; only list_tools is used.
    templates = await create_server(None, execution=object()).list_tools()
    tools = []
    for template in templates:
        tool = template.model_copy(deep=True)
        tool.input_schema = deepcopy(tool.input_schema)
        tool.input_schema['properties']['computer'] = {'type': 'string', 'enum': list(computers)}
        tool.input_schema['required'] = ['computer', *tool.input_schema.get('required', [])]
        tool.input_schema['additionalProperties'] = False
        tool.description = 'On the explicitly selected computer. ' + (tool.description or '')
        tools.append(tool)
    tools.insert(0, Tool(name='list_computers', description='List configured computer names and expected identities. Does not probe reachability or select a default.',
                         input_schema={'type': 'object', 'properties': {}, 'additionalProperties': False},
                         annotations=ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)))
    schemas = {tool.name: tool.input_schema for tool in tools}

    async def listing(ctx, params):
        if params and params.cursor:
            raise ValueError('Unknown tool cursor')
        return ListToolsResult(tools=tools)

    async def calling(ctx, params):
        arguments = dict(params.arguments or {})
        computer = arguments.get('computer', 'unselected')
        try:
            if params.name not in schemas:
                raise ValueError('Unknown tool')
            validate(arguments, schemas[params.name])
        except Exception:
            return failure(str(computer), 'Invalid tool arguments. Choose a configured computer explicitly; request was not sent.')
        if params.name == 'list_computers':
            data = {'computers': [{'computer': name, 'expected_host': config['expected_host']}
                                  for name, config in computers.items()]}
            return CallToolResult(content=[TextContent(type='text', text=json.dumps(data))], structured_content=data)
        arguments.pop('computer')
        try:
            for kind in ('session_id', 'operation_id', 'recovery_copy'):
                if arguments.get(kind) is not None:
                    arguments[kind] = handles.decode(computer, kind, arguments[kind])
        except ValueError:
            return failure(computer, 'Handle belongs to another computer or router process; request was not sent.')
        result = await backends[computer].call(params.name, arguments)
        if result.structured_content is not None:
            result.structured_content = handles.result(computer, result.structured_content)
            # The normal backend repeats structured JSON in a text block. Replace
            # that copy as well so callers cannot accidentally use raw handles.
            for block in result.content:
                if isinstance(block, TextContent):
                    try:
                        data = json.loads(block.text)
                    except ValueError:
                        continue
                    block.text = json.dumps(handles.result(computer, data))
        return result

    @asynccontextmanager
    async def lifespan(server):
        try:
            yield {}
        finally:
            await asyncio.gather(*(backend.close() for backend in backends.values()))

    return Server('Tunnel', version='0.1.0', icons=icons(), on_list_tools=listing, on_call_tool=calling, lifespan=lifespan,
                  instructions='One Tunnel, multiple computers. Call list_computers to discover names. '
                  'Translate the user\'s named computer into the required computer argument on every call. '
                  'Ask when the computer is ambiguous. Never select a global default or fall back. '
                  'Load get_workflow for the selected computer before file or command work. '
                  'Paths, revisions, recovery copies, session and operation IDs belong to that computer. '
                  'Configuration is local operator owned; no remote endpoint or command configuration tools.')


async def serve(path):
    router = await create_router(load_computers(path), [path.resolve()])
    async with stdio_server() as streams:
        await router.run(*streams, router.create_initialization_options())


def main():
    parser = argparse.ArgumentParser(description='Multi-computer Tunnel router over stdio')
    parser.add_argument('--config', type=Path, required=True, help='Private, operator-owned computer command map')
    args = parser.parse_args()
    asyncio.run(serve(args.config))


if __name__ == '__main__':
    main()
