# Fleet

Source for Dots and Drafts plugins, Tunnel, and selected portable configuration.
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

Load one Dots/Drafts source per Codex profile: cloud for the personal account
shared by web and desktop; local for the work account without cloud plugins.
`scripts/sync-plugins.sh --codex --source cloud|local` records that profile's
choice in `dots-plugin-source`. Preserve other profiles' choices and enforce
this policy in config and plugin sync. Never uninstall account-wide cloud
plugins to fix desktop duplicates.

Keep Dots a standalone skills plugin and Tunnel a separate tools-only app.
Dots manifests must not bind Tunnel through `.app.json` or `apps`. Preserve
Tunnel's existing identity, service, connection, and authorized folders. Keep
Tunnel enabled independently of Dots/Drafts source selection; never return
Dots skills to its app-backed canonical plugin.

Follow [the cloud release procedure](docs/maintainers/cloud-releases.md).
Prefer Plugin Creator source/archive updates. Update the existing backend ID
with its current `expected_release_id`; preserve identity, scope, and audience.
Never create a replacement Dots plugin during an ordinary update. Archive
updates cannot delete files: report retired files that remain. Verify expected
cloud skills/content and a fresh desktop loader with one source and zero
duplicates. Report cloud publication and desktop verification separately;
failed verification remains pending. Local sync does not publish cloud.

## Work and propagation

- In this repository, `commit` or `sync` means commit only scoped files, push
  the current branch, then run relevant sync commands. Exclude unrelated changes.
- For plugin changes, use `scripts/sync-plugins.sh --all` after commits on
  `main` and plugin PR merges. Bump the owning `plugin.json` only when release
  content is final and ready to commit.
- Preview machine changes with `scripts/sync-configs.sh --dry-run`; apply only
  when requested with `--apply`. Installed Fleet hooks push and apply after
  commits, and apply after merge/rebase pulls. Install hooks per Fleet checkout,
  never automatically in another repository.
- Use the active environment's default skill creator for creation/validation.
  Dots quality guidance: `plugins/dots/skills/skill-standards/references/standards.md`.

## Validation

Review changed files and run relevant deterministic checks. Skill changes also
require the active environment's default skill validation.

`scripts/verify.py --plugins` checks both packages. Use Python 3.10+.
Run `scripts/verify.py --full` (also requires `uv`) only when explicitly requested,
for marketplace/plugin packaging, shared integration or release infrastructure,
or changes to the gate itself.
