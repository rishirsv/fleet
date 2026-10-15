# Dots

Focused workflows for planning, building, reviewing, and shipping software in
Codex and Claude Code. Install through the repository's
[installation guide](https://github.com/rishirsv/fleet/blob/main/INSTALL.md).

## Working with Dots

Select [Dots](skills/dots/SKILL.md) and describe the outcome, any constraints,
and what would show it works. You do not need to choose a playbook or list
skills. Dots selects the workflow and loads supporting guidance as needed.

Use `$dots` in Codex. The entrypoint is explicitly selected; individual focused
skills can still apply according to their own invocation settings.

| Intent | Example prompt |
| --- | --- |
| Investigate | `$dots why does logout leave the cached profile visible? Explain the cause; don't change code.` |
| Plan | `$dots plan CSV export for the reports page. Preserve filters. Stop before implementation.` |
| Build | `$dots add CSV export. The exported rows must match the active filters, including an empty result.` |
| Fix | `$dots retries create duplicate notifications. Reproduce it, fix the cause, and show the before-and-after result.` |
| Refactor | `$dots rename UserCtx to SessionContext. Keep behavior unchanged and account for every reference.` |
| Review | `$dots review this branch for regressions. Report findings without editing files.` |

Follow up with "do it" or "continue" when the outcome is already settled.
To change direction, state the new task or boundary:

```text
New task: explain how the export queue retries failed jobs. Don't fix anything.
```

Dots selects the workflow again when the task changes. A question during a
build does not authorize new implementation, and a plan-only request stops at
the plan. Re-select Dots in a new chat; it does not install an always-on rule.

Use a focused skill when you already know the operation, such as
`$change-review medium review-only`. Select `$agent-workflow` when you want
the delegated plan-to-PR flow. Ordinary implementation does not publish a PR
unless you request it.

## Choose a focused skill

| Task | Skill |
| --- | --- |
| Explain code or investigate a decision | [How](skills/how/SKILL.md), [Why](skills/why/SKILL.md) |
| Design a boundary or resolve an uncertain choice | [Architect](skills/architect/SKILL.md), [Prototype](skills/prototype/SKILL.md) |
| Review architecture or a completed change | [Architecture Review](skills/architecture-review/SKILL.md), [Change Review](skills/change-review/SKILL.md) |
| Investigate what a change could break elsewhere | [Blast Radius](skills/blast-radius/SKILL.md) |
| Write repository docs or build an HTML report | [Repo Docs](skills/repo-docs/SKILL.md), [HTML](skills/html/SKILL.md) |
| Publish or monitor a pull request | [Publish PR](skills/publish-pr/SKILL.md), [Babysit PR](skills/babysit-pr/SKILL.md) |

See [Dots](skills/dots/SKILL.md) for the complete routing map. Each skill
defines its own inputs, permissions, and checks.

## Optional tools

[Tunnel](scripts/dots-tunnel/README.md) is a separate connection for locally
authorized file access and optional command execution from ChatGPT. The Dots
plugin contains its source and workflow, but does not bundle the app connection.
