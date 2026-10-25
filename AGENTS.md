# Fleet

Source for pstack and Drafts plugins and selected portable configuration.
For setup and sync behavior, see [INSTALL.md](INSTALL.md).

## Ownership

- Plugin source: `plugins/<plugin-name>/`. Marketplaces:
  `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`.
- Selected settings: `configs/<tool>/`; retain only user-selected settings.
  Keep Logi Options under `configs/logi-options-plus/`.
- Shared, repository-neutral guidance: `configs/agents/AGENTS.md`. Keep Fleet
  release rules here; never propagate them into other repositories.
- Helpers: `scripts/`. Plugin policies and TOML merge: `scripts/plugin-sync/`.
  Unreleased skills that must not ship belong in `wip/`.
- Edit maintained source, not installed caches. Name new branches by purpose:
  `fix/`, `feature/`, `refactor/`, `docs/`, or `chore/`, followed by lowercase
  kebab-case; omit an extra `codex/` prefix.

## Plugin boundaries

Use local pstack/Drafts on both Fleet Macs, including personal-account desktop
profiles. Disable their cloud copies only in each desktop profile's local
loader; keep the account-wide cloud installations available on the web.
`scripts/sync-plugins.sh --codex --source local` records the desktop choice in
`pstack-plugin-source`, which later config and plugin syncs preserve. Verify
the local source and zero duplicates on each computer. Use cloud as a desktop
source only when explicitly requested. Never uninstall account-wide cloud
plugins to fix desktop duplicates.

Keep pstack a standalone skills plugin with no `.app.json` or `apps` binding.

Follow [the cloud release procedure](docs/releases.md).
Prefer Plugin Creator source/archive updates. Update the existing backend ID
with its current `expected_release_id`; preserve identity, scope, and audience.
Never create a replacement pstack plugin during an ordinary update. Archive
updates cannot delete files: report retired files that remain. Verify expected
cloud skills/content and a fresh desktop loader with one source and zero
duplicates. Report cloud publication and desktop verification separately;
failed verification remains pending. Local sync does not publish cloud.

## Work and propagation

- `sync` means pull Fleet with fast-forward only, commit only task-scoped changes
  when present, always push those commits, then apply configs and sync all plugins
  on this computer and every configured peer. Preserve unrelated changes. Use
  `scripts/sync-fleet.py`; it also syncs when the pull is already up to date.
- Every Fleet commit must be pushed. Install `scripts/install-hooks.sh` in each
  Fleet checkout: post-commit pushes the current branch and runs local/peer sync;
  post-merge and completed post-rebase pulls apply configs and sync plugins.
  Hooks skip intermediate rebase commits. Never install them in other repos.
- Keep SSH aliases and checkout paths outside tracked files. Configure each
  checkout with repeatable local `fleet.syncPeer` values (`HOST:/absolute/path`).
  Peer sync pulls its existing branch without switching or resetting it, verifies
  the requested revision, and suppresses recursive propagation. Report unreachable,
  divergent, or failed peers as pending; never claim all computers synced then.
- `sync` and `commit` authorize config apply and plugin refresh across configured
  computers. For other config work, preview with `scripts/sync-configs.sh --dry-run`
  and apply only when requested. Local sync does not publish cloud releases.
- Bump the owning `plugin.json` only when release content is final and ready
  to commit.
- Use the active environment's default skill creator for creation/validation.

## Validation

Review changed files and run relevant deterministic checks. Skill changes also
require the active environment's default skill validation.

`scripts/verify.py --plugins` checks registered plugins and optional source
packages. Use Python 3.10+.
Run `scripts/verify.py --full` (also requires `uv`) only when explicitly requested,
for marketplace/plugin packaging, shared integration or release infrastructure,
or changes to the gate itself.
