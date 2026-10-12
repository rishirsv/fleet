# Set up Fleet

Clone this repository on each computer. Install the apps you use and sign in.
Sync requires Git, Python 3.10+, and Zsh; Codex/plugin sync also needs uv, and
Claude plugin sync needs Node. VS Code extension installation needs `code` on
PATH. On macOS, install Karabiner-Elements and grant its requested permissions
for Caps Lock → Hyper. Tunnel and Logi Options retain their separate setup.

## Check this computer

```sh
python3 scripts/doctor.py
python3 scripts/doctor.py --configs
```

Doctor checks required CLI tools, per-profile plugin-source choices, Fleet hooks,
and macOS app/font installation. `--configs` also checks saved configuration
drift; `--profile PATH` selects a Codex profile. It reports problems without
applying changes. App sign-ins, Tunnel authorization, and macOS permissions
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

## Plugins and Tunnel

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

Follow [Tunnel setup](plugins/dots/scripts/dots-tunnel/README.md#local-setup)
for its separate connection and folder authorization. Retained mouse/keyboard
setup is in [Logi Options](configs/logi-options-plus/shortcuts.md).

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
auto-approval. Model and effort remain app defaults.

Claude Code uses fullscreen rendering with mouse support so conversation scrolling
stays inside Claude instead of relying on terminal redraw history. The managed
settings override stale shell variables that disabled the alternate screen or mouse.
Mouse-wheel scrolling uses a three-line multiplier.

Shell helpers: `cx` (Codex), `cxp` (personal Codex), `cl` (Claude), `gs` (status),
`gd` (diff), `gds` (staged diff), `gr` (repo root), and `fleet` (config preview).
Set `FLEET_HOME` in `.zshrc.local` if Fleet is outside `~/Code/fleet`.

## Fleet hooks

Install hooks separately in each Fleet checkout. They push after a commit,
then apply local configs and sync plugins on main. Failed push prevents apply
without undoing the commit. Rebase intermediate commits skip publishing;
completed rebase/merge pulls apply configs and sync plugins. Plugin sync fetches
the account catalog before checking the fresh skill loader, so cloud duplicates
cannot be hidden by a local-only CLI inventory. Dirty plugin source stops sync
with an explicit error; it is never installed as a release by a hook.
A pull with no changes may not invoke hooks: sync manually if needed.
Existing hook configuration must be integrated before installation.

Pull Fleet on another computer to receive changes. Git does not copy hook
installation, app sign-ins, private shell settings, or macOS permissions.

Scripts expose sync, doctor, hook installation, and validation. `config-sync.py`
contains the shared file merge helper; `plugin-sync/` contains plugin internals.
The retained Logi repair helper is under `scripts/logi-options/`. Root tests
cover package validation only. Sync is checked through doctor, dry-run, and
status commands; skill and Tunnel runtime tests stay with their plugin source.
