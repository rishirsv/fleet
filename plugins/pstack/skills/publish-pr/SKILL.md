---
name: publish-pr
description: "Commits and pushes finished changes, then opens or updates a GitHub pull request ready for review. Use when the user asks to publish completed work as a PR; not for merging, review feedback, or monitoring checks."
---

# Publish PR

Commit and push the intended work, then update its existing GitHub PR or open
one ready for review. Preserve unrelated changes and follow repository and
user choices about branches, commits, templates and draft status.

Confirm the repository, account, branch, intended diff and current PR base.
Fetch the remote and compare against the PR’s current base. Resolve conflicts
before publishing; rebase only when policy or relevant base changes require it.
Reuse completed checks and visual evidence. Rerun only
checks invalidated by subsequent code, dependency, build or history changes.

Commit and push the scoped changes. Reuse the branch's PR. Confirm its head
contains the pushed commit and attach the created or updated PR to the current
chat when the host provides that operation. Do not merge or start recurring
monitoring unless requested.

Write a terse result-based title and a short description for a reviewer who
has not seen the chat. Describe the final diff when creating or updating a PR.
Follow the repository template. When none exists, use `## Summary`,
`## Evidence` and `## Merge Danger`, in that order. Fit the same information
into an existing template without adding duplicate sections.

- **Summary.** Lead with the concrete problem and resulting behavior. A reader
  should understand both from the title and opening alone. Add the smallest
  useful diagram, pseudocode or shaped diff when it clarifies behavior or
  ownership. Keep small changes in short prose. Omit file inventories and
  agent narration.
- **Evidence.** Show observed before/after behavior or results where available.
  Claim a failing-before result only when it was observed. Otherwise name the
  executed checks, their results and what remains unverified. Keep skipped
  and unrun checks distinct from passes. Give performance measurements with
  units and comparable conditions. Omit generic checklists.
- **Merge Danger.** State whether the change is a one-way or two-way door and
  explain how to roll it back or recover. Name material data or external
  changes that reverting code would leave behind. Describe the blast radius
  through the affected users, data, consumers or workflows and what could
  break. Do not substitute a risk label for concrete consequences and limits.

Use existing screenshots or videos when they help. Check `gh pr create --help`
or `gh pr edit --help` for `--attach`; use a body file for multiline text and
attach each referenced file. If unavailable, use an authorized attachment tool
or report missing media. Never publish a local filesystem path as evidence.
Read back the saved body and verify media and hosted links.

Report the PR URL, pushed head, check status and remaining limitations.

Output format adapted from [AI Hero's PR skill](https://www.aihero.dev/skills-pr).
