---
name: publish-pr
description: "Commits and pushes finished changes, then opens or updates a GitHub pull request ready for review. Use when the user asks to publish completed work as a PR; not for merging, review feedback, or monitoring checks."
---

# Publish PR

Commit and push the intended work, then update its existing GitHub PR or open
one ready for review. Preserve unrelated changes and follow repository and
user choices about branches, commits, templates and draft status.

Confirm the repository, account, branch, intended diff and current PR base.
Resolve conflicts before publishing; rebase only when policy or relevant base
changes require it. Reuse completed checks and visual evidence. Rerun only
checks invalidated by subsequent code, dependency, build or history changes.

Commit and push the scoped changes. Reuse the branch's PR. Confirm its head
contains the pushed commit and attach the created or updated PR to the current
chat when the host provides that operation. Do not merge or start recurring
monitoring unless requested.

Write a terse result-based title and a short description for a reviewer who
has not seen the chat. Lead with the concrete problem and resulting behavior.
Include decisive validation and material risks, unverified behavior and recovery
limits. Follow the repository template; omit file inventories, agent narration
and generic checklists.

Use existing screenshots or videos when they help. Check `gh pr create --help`
or `gh pr edit --help` for `--attach`; use a body file for multiline text and
attach each referenced file. If unavailable, use an authorized attachment tool
or report missing media. Never publish a local filesystem path as evidence.
Read back the saved body and verify media and hosted links.

Report the PR URL, pushed head, check status and remaining limitations.
