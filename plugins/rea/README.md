# Reverse-Engineer

Local application analysis through REA's stdio MCP server and upstream
`reverse-engineer-anything` usage skill. Enable **Reverse-Engineer** from Fleet's `dots`
marketplace in Codex or Claude Code, then start a fresh chat.

Fleet sync installs the local plugin on each configured computer, including
cloud-selected Codex profiles. Dots/Drafts source choices remain independent.
This local runtime cannot run in ChatGPT web or mobile.

The launcher requires `npx` on PATH and downloads pinned `node@24.11.0` and
`rea-agents@6.7.0` into npm's cache on first use. It does not replace system Node
or run `rea setup`. Native analysis requires a separately configured engine;
static JavaScript analysis works without Hopper, Ghidra or IDA. Existing engine
installations and client registrations remain machine-local.

Source provenance is in `projects/rea/` at the Fleet repository root. The usage
skill and its references come from the supplied MIT-licensed source snapshot;
Fleet adds runtime guidance, pins CLI examples and supplies plugin/UI metadata.
The Fleet-owned icon depicts separated software layers, with matching composer
and listing assets. The stable package ID remains `rea@dots`; its display name is **Reverse-Engineer**.
Do not publish this stdio package as a hosted service or claim cloud tool access.

Validate with `python3 scripts/verify.py --full` from Fleet. Runtime checks should
initialize MCP, list tools, and inspect a harmless JavaScript fixture without
executing it. A fresh chat is required to expose newly installed tools to an agent.
