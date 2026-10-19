# Set up Fleet

Clone this repository on each computer. Install the apps you use and sign in.
Sync requires Git, Python 3.10+, and Zsh; Codex/plugin sync also needs uv, and
Claude plugin sync needs Node. VS Code extension installation needs `code` on
PATH. On macOS, install Karabiner-Elements and grant its requested permissions
for Caps Lock → Hyper. Logi Options retains its separate setup.

## Check this computer

```sh
python3 scripts/doctor.py
python3 scripts/doctor.py --configs
```

Doctor checks required CLI tools, per-profile plugin-source choices, Fleet hooks,
and macOS app/font installation. `--configs` also checks saved configuration
drift; `--profile PATH` selects a Codex profile. It reports problems without
applying changes. App sign-ins and macOS permissions
still need verification in their apps.

## Preview and apply

```sh
scripts/sync-configs.sh --dry-run
scripts/sync-configs.sh --apply
scripts/install-hooks.sh
```

Preview is the default. Apply backs up changed files. JSON/TOML sync preserves
unlisted settings and unrelated shortcuts, but rewrites JSONC as plain JSON.
Ghostty and `.zshrc` are replaced with backups; move private exports and any
needed local shell setup into `~/.zshrc.local` before applying. Open a new shell
and reload affected apps afterward.

Choose one or several targets when needed:

| Target | Managed configuration |
| --- | --- |
| `--agents` | Shared guidance in Codex `AGENTS.md` and Claude `CLAUDE.md` |
| `--codex` | Settings, shortcuts, and selected IAB preferences in each selected Codex profile |
| `--claude` | Settings and supported shortcuts |
| `--vscode` | Minimal editor settings, shortcuts, Codex and Claude extensions |
| `--karabiner` | Selected-profile Caps Lock mapping, macOS only |
| `--ghostty` | Terminal settings and Paper Mono |
| `--zsh` | Interactive shell, completion, history, and helpers |

Without targets, sync covers all of them. Codex defaults to `CODEX_HOME` or
`~/.codex`, plus `~/.codex-personal` when present. `--profile PATH` selects one
Codex profile; it does not narrow other targets. Claude uses `CLAUDE_CONFIG_DIR`
or `~/.claude`; VS Code supports `VSCODE_USER_DIR`. Paper Mono Regular installs
on macOS when syncing Codex, VS Code, or Ghostty. IAB sync merges the selected
preferences from `configs/codex/browser.toml`, preserving profile-specific site
rules and other browser settings. Font size is 16 throughout;
apps use different sizing units, so visual adjustment may still be needed.

Shared guidance uses a managed block and preserves existing global instructions.
Repository instructions take precedence. Fleet's publishing rules and hooks
stay in Fleet; using the shared guidance in another repo never installs hooks
there. Edit `configs/agents/AGENTS.md` to change the shared guidance.

Apply can succeed for one target before another fails. Check the output and
retry the failed target; backups are beside changed files. `--status` reports
drift without writing. Sync does not execute on another computer.

## Plugins

Choose the source for the account in the current Codex profile:

```sh
# Personal account with existing cloud Dots/Drafts installations
scripts/sync-plugins.sh --codex --source cloud
# Work account using local plugins
scripts/sync-plugins.sh --codex --source local
# Claude marketplace plugins
scripts/sync-plugins.sh --claude
```

The source choice is saved per profile and preserved by later syncs. Cloud mode
requires the account's existing installations. Sync validates a fresh Codex
loader and rejects duplicates; restart existing desktop sessions when needed.
Claude uses the `rishirsv/dots` marketplace; `/reload-plugins` refreshes sessions.
Sync compares installed files with the refreshed marketplace and reinstalls stale
copies even when their version is unchanged, preserving data and disabled state.
Plugin sync refuses dirty plugin/tooling source; `--allow-dirty` is for development.

`scripts/sync-plugins.sh --all` refreshes both hosts. Local sync does not publish
cloud releases; follow [cloud releases](docs/maintainers/cloud-releases.md).
Config sync installs the selected VS Code extensions; Codex/Claude plugin
installation remains a separate step.

Retained mouse/keyboard setup is in [Logi Options](configs/logi-options-plus/shortcuts.md).

## Shortcuts and shell

Hyper means Command+Control+Option+Shift. Hold Caps Lock for Hyper; tap it for
Escape. Equivalent Karabiner rules are retained; conflicting Caps Lock mappings
stop that target for manual integration. Unrelated rules remain.

| Hyper key | Codex | Claude Code | VS Code |
| --- | --- | --- | --- |
| T | Terminal | — | Terminal |
| R | Cycle reasoning | — | — |
| M | Model picker | Model picker | — |
| F | Fast mode | Fast mode | — |
| Y | Worktree mode | — | — |
| B | Sidebar | — | Sidebar |
| O | Project picker | — | Open folder |

Ghostty forwards Claude's supported bindings using extended terminal sequences.
Use Claude's model picker for effort controls. Claude inherits terminal fonts
and its automatic theme follows the terminal background. Codex and Claude
settings enable the selected unrestricted permissions; VS Code enables tool
auto-approval. Codex defaults to GPT-6.1 Sol with medium reasoning; individual
chats can override these defaults.

Claude Code uses fullscreen rendering with mouse support so conversation scrolling
stays inside Claude instead of relying on terminal redraw history. The managed
settings override stale shell variables that disabled the alternate screen or mouse.
Mouse-wheel scrolling uses a three-line multiplier.

Shell helpers: `cx` (Codex), `cxp` (personal Codex), `cl` (Claude), `gs` (status),
`gd` (diff), `gds` (staged diff), `gr` (repo root), and `fleet` (config preview).
Set `FLEET_HOME` in `.zshrc.local` if Fleet is outside `~/Code/fleet`.

Interactive shells set the soft open-file limit to 4096. Restart an existing
Codex app-server daemon with that limit after syncing its configuration:

```sh
ulimit -S -n 4096 && codex app-server daemon restart
```

## Remote development and T3

Use the execution host's project in Codex and T3 so worktrees, dependencies,
builds and Simulators stay on that host. Codex Remote Control supports desktop
and phone clients. T3 can connect through an existing SSH alias without enabling
T3 Connect. Keep machine names, paths and host preferences in local settings;
sync preserves guidance outside the managed shared block in `~/.codex/AGENTS.md`.

T3's Codex provider should use that host's Codex home. In each T3 environment's
settings, set the default model to GPT-6.1 Sol and reasoning to Medium. T3's
Full access mode corresponds to Codex's `never` approvals and
`danger-full-access` sandbox. Preserve intentional project and chat overrides.
T3 settings are applied through its Settings UI; Fleet does not overwrite its
live settings file. These defaults match at setup time, not through live sync.

Repository `t3.json` can select worktrees and offer the same setup/build/test
commands as `.codex/environments/environment.toml`; import its scripts once
from the T3 project's Actions menu. T3 does not import Codex's
environment actions. Keep dependency and Simulator setup in the repository's
shared command, rather than implementing it separately for each app. For remote
documents, return a private preview URL; a host's absolute path or `localhost`
URL cannot be opened as a local file on another device.

## Fleet hooks

Install hooks separately in each Fleet checkout with `scripts/install-hooks.sh`.
Every completed commit pushes its branch, applies configs, refreshes all plugins,
and syncs configured computers. Push failure leaves the commit intact and stops
sync. Rebase intermediate commits are skipped. Merge/rebase pull hooks apply
configs and refresh plugins locally. Existing hooks must be integrated first.

Run `scripts/sync-fleet.py` for a full pull and sync, including an already-current
pull. Git has no hook for a pull that changes nothing; use this command when you
need guaranteed refresh. It does not create commits: agents commit scoped work
before invoking it. Failed targets are reported for retry, without undoing work.

Configure peers separately on each computer; private machine details stay in
`.git/config`:

```sh
git config --local --add fleet.syncPeer 'HOST:/absolute/path/to/fleet'
```

Use an existing SSH alias with key authentication. Peers pull their current
upstream with fast-forward only and must reach the initiating revision. Sync
never switches their branch, resets changes, or propagates recursively. Install
hooks on every peer, and keep the same release branch checked out for unattended
propagation. Offline or divergent peers remain pending until a later retry.
Git does not copy hook installation, app sign-ins, or macOS permissions.

Scripts expose sync, doctor, hook installation, and validation. `config-sync.py`
contains the shared file merge helper; `plugin-sync/` contains plugin internals.
The retained Logi repair helper is under `scripts/logi-options/`. Root tests
cover package validation only. Sync is checked through doctor, dry-run, and
status commands; skill tests stay with their plugin source.

## Space switching on macOS

Run `scripts/sync-configs.sh --spaces --apply` (included in normal Fleet sync).
Fleet assigns macOS Move left/right a space directly to Hyper+Left/Right and
removes Tinycast's Previous/Next Space hotkeys so they cannot intercept those
keys. Tinycast still supplies Caps Lock → Hyper, with Include Shift enabled;
keep one Caps Lock remapper active (Tinycast or Karabiner).
Restart Tinycast after applying; log out/in if macOS retains old shortcuts.
`--spaces --status` checks saved settings; `--spaces --dry-run` previews drift.
Existing preferences are backed up under `~/Library/Application Support/Fleet/backups/`.

Fleet also applies `configs/logi-options-plus/spaces.json` to every local
MX Master 4 gesture profile, matching model slots rather than private profile
IDs. It selects Custom gestures and assigns left/right to explicit Hyper arrows,
using the same macOS shortcut as the keyboard. Click/up/down, other buttons,
account state and device identities stay local. Options+ is stopped for the
merge, its SQLite database is backed up beside the original, and the agent is
restarted. Other mouse models are reported as skipped rather than guessed.
The standalone helper is `python3 scripts/logi-options/sync-spaces.py apply`.

Tinycast's Settings → Backup → Export Backup saves its native backup separately;
keep that archive outside Git because it may include personal application data.
Verify physical Hyper+Left/Right and gesture-button+left/right after restore.

## Reverse-Engineer application analysis

Reverse-Engineer is a local MCP plugin available alongside Dots, Drafts and Design. Fleet sync
installs `rea@dots` for both local- and cloud-selected Codex profiles and Claude
Code. It preserves the selected Dots/Drafts source. Start a fresh chat and use
`$reverse-engineer-anything` with the application or artifact to inspect.

The first launch needs npm/network access to cache REA 6.7.0 and Node 24.11.0.
Native analysis engines are configured separately on each computer. This runtime
is local; it does not provide tools to ChatGPT web/mobile. The supplied source
snapshot and provenance are stored under `projects/rea/`; the installable package
is `plugins/rea/`. See its README for runtime and validation details.
