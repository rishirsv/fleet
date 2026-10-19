// An execution-free JavaScript fixture through the actual MCP transport.
import { createRequire } from 'node:module';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { tmpdir } from 'node:os';
import { pathToFileURL } from 'node:url';

const root = resolve(process.argv[2]);
const require = createRequire(join(root, 'package.json'));
const { Client } = await import(pathToFileURL(require.resolve('@modelcontextprotocol/client')).href);
const { StdioClientTransport } = await import(pathToFileURL(require.resolve('@modelcontextprotocol/client/stdio')).href);
const fixture = await mkdtemp(join(tmpdir(), 'fleet-rea-smoke-'));
const client = new Client({ name: 'fleet-rea-setup', version: '1.0.0' });
try {
  await writeFile(join(fixture, 'package.json'), JSON.stringify({ name: 'fleet-smoke', main: 'index.js' }));
  await writeFile(join(fixture, 'index.js'), 'export const fixtureValue = 42;\n');
  await client.connect(new StdioClientTransport({ command: process.execPath, args: [join(root, 'scripts/rea.mjs'), 'mcp'], stderr: 'inherit' }));
  const { tools } = await client.listTools();
  if (!tools.some(tool => tool.name === 'analyze_javascript_application')) throw new Error('JavaScript analysis tool missing from MCP');
  const result = await client.callTool({ name: 'analyze_javascript_application', arguments: { input_path: fixture, detail: 'summary' } });
  if (result.isError || typeof result.structuredContent?.evidence_id !== 'string') throw new Error(`MCP fixture inspection failed: ${JSON.stringify(result).slice(0, 1000)}`);
  process.stderr.write(`Fleet REA MCP verified: ${tools.length} tools; static fixture inspected.\n`);
} finally {
  await client.close();
  await rm(fixture, { recursive: true, force: true });
}
