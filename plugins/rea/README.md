# Reverse-Engineer

Fleet owns the skills, launcher, locked build recipe and complete REA source
snapshot. The launcher builds that snapshot rather than downloading the published
`rea-agents` package. Source provenance and its SHA-256 are in
[runtime/origin.json](runtime/origin.json); the original MIT-licensed archive is
[runtime/rea-6.7.0-source.zip](runtime/rea-6.7.0-source.zip).

## Set up a new computer

Install these prerequisites separately:

- **Python 3.10+**, available as `python3`.
- **Node.js with npm**. Node 24 LTS is recommended; the source snapshot's `.nvmrc`
  selects 24.18.0. Supported versions are 22 >=22.19, 24 >=24.11, or 26+.
  Node 23 and 25 are unsupported. SQLite inspection needs Node 24 >=24.15 or 26+.
- **Codex CLI** or **Claude Code**, signed in, if you want plugin registration.
- Network access to npm for the first dependency installation. Locked dependencies
  are downloaded; REA's own source comes from this repository.

After cloning Fleet, run this from its root for Codex:

```sh
python3 scripts/setup-rea.py --client codex
```

Use `--client claude` for Claude Code or `--client both` for both clients.
The command verifies the archive, extracts it, installs locked npm dependencies,
builds the CLI/MCP runtime and runs a static MCP smoke test. It then registers
Fleet's local marketplace and installs only `rea@dots`. Start a new chat when ready.
The host may copy the plugin. Setup primes that newly installed copy with the
verified build before you start a chat, avoiding a cold compile during MCP startup.
If manually installed without this command, the launcher can build from its bundled
source on first launch; progress stays on stderr and MCP stdout stays clean.

**An existing REA installation is protected.** With `--client`, setup checks the
selected clients first and refuses to replace either `rea@dots` or `rea@rea-local`.
This also applies on repeat runs after installation. For an already configured
computer, prepare or check the repo runtime without changing installed plugins:

```sh
python3 scripts/setup-rea.py
```

This default mode does not register a marketplace, update client settings, refresh
installed caches, restart servers, apply Fleet configs, or propagate to peers.
Migration of an existing installation is a separate later action. Fleet-wide sync
still refreshes installed plugins when explicitly requested; do not run it while
preserving an older installation for active projects.

If your supported Node is not first on PATH, set `FLEET_REA_NODE` to its executable
for setup and launch. The setting is machine-local; do not put its path in Git.
GUI-launched clients need the supported Node/Python on their own PATH as well.

## What travels with Fleet

| Location | Ownership |
| --- | --- |
| `skills/` | Maintained main skill, three companion skills, references, UI metadata and exercise source |
| `runtime/` | Exact upstream source archive, original lockfile inside it, provenance and checksum |
| `scripts/` | Fleet build, launch and MCP smoke-test code |
| `node_modules/.fleet-rea/` | Ignored extracted source, dependencies, compiled generations and private npm download cache |
| `mcp.json`, `.mcp.json` | Portable and Claude-compatible local launch configuration |

The extracted source includes upstream `src/`, bridges, build scripts, documentation,
tests, license notices and its original `package-lock.json`. Build generations are
keyed by source digest, Fleet builder revision, Node ABI, OS and CPU architecture.
Successful generations are reused; failed staging builds are removed. Rebuilding
publishes a new generation without deleting older generations. Checkout paths are
not written into launch configuration. Run setup again after moving between
operating systems or architectures; ignored build output is regenerated after a
fresh clone. No global REA installation or existing `~/.npm` cache is required.

The setup is source-contained and reproducible, not an offline bundle of all npm
packages and external tools. First setup needs dependency downloads; a prepared
compatible build runs without fetching REA or its npm dependencies again.

For local CLI use from Fleet:

```sh
python3 plugins/rea/scripts/rea.py --version
python3 plugins/rea/scripts/rea.py --help
python3 plugins/rea/scripts/rea.py mcp
```

The launcher also works by absolute path from another project's working directory.
It locates its own package; it does not depend on your current directory.
This is a local stdio runtime for desktop/CLI clients, not a hosted ChatGPT web or
mobile service. Package identity remains `rea@dots`, display name **Reverse-Engineer**.

## Install analysis engines only when needed

Setup does not install or configure external analysis engines, browsers, SDKs or
licenses. JavaScript/Electron static analysis and ordinary managed inspection use
the repo build's npm dependencies. Other targets require additional tools:

| Investigation | Separately installed dependency |
| --- | --- |
| Native disassembly/decompilation | A supported Ghidra + Java installation, licensed Hopper, or an existing supported IDA/MCP setup |
| Android code | Full JDK and supported JADX/headless bridge; configure `REA_JADX_MCP_JAR` |
| Apple runtime/device/simulator work | Appropriate Xcode/Command Line Tools, LLDB and matching device/simulator access |
| Live browser/Electron observation | A supported installed browser/runtime and its explicit debugging endpoint; browsers are not downloaded by setup |
| Recorded packets | Wireshark tools (`tshark`, sometimes `capinfos`) and the host isolation tools required by the chosen operation |
| Firmware, signals, WASM, offline ELF/core analysis | The selected Binwalk/Unblob, sigrok, WABT, pwntools or debugger tools and their supported host platform |

Keep engine paths, licenses and device-specific settings outside Git. Consult the
[main usage skill](skills/reverse-engineer-anything/SKILL.md) and its focused
references for operation-specific versions, environment variables and host limits.
This setup is exercised on macOS; Linux uses the same Python/npm recipe. Native
Windows setup and optional provider integrations have not been validated here.

## Choose an investigation workflow

- [Reverse-Engineer](skills/reverse-engineer-anything/SKILL.md) owns REA tool routing,
  provider/session mechanics and evidence handling.
- [Recon Artifact](skills/recon-artifact/SKILL.md) finds feature entry points from an
  app, package, URL or capture, including an Apple/iOS investigation playbook.
- [Reconstruct Behavior](skills/reconstruct-behavior/SKILL.md) follows a feature through
  computation, state and side effects to an explanation, specification or requested build.
- [Verify Reconstruction](skills/verify-reconstruction/SKILL.md) compares functions,
  files, stateful flows or GUI/network behavior and checks its comparison harness.

Investigations keep resumable state and matching evidence. The
[research notes](skills/recon-artifact/references/source-notes.md) record the
companion skills' design inputs. The known-target C exercise is for calibration.
Fleet's skills remain independent of the upstream generated skill inside a build;
setup never overwrites the maintained `skills/` directory.

## Validate or update the package

`python3 scripts/setup-rea.py` builds and verifies only the repository runtime.
`python3 scripts/verify.py --full` runs Fleet's integration gate with isolated
Codex installation checks. Neither is an instruction to sync existing computers.

For a source refresh, replace the bundled archive and update its provenance and
checksum after inspecting the new upstream instructions and lockfile. Verify the
source build and relevant providers; the source snapshot is not assumed to be
byte-identical to an npm release. Change Fleet skills in `skills/`, not in generated
build output or installed caches. Keep the plugin manifests' versions synchronized
when preparing a release; local setup never bumps or publishes a release.
