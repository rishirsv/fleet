---
name: change-review
description: "Reviews a diff, branch, or pull request for defects and maintainability, with configurable independent reviewers. Repairs supported findings unless the user requests review-only."
---

# Change review

Review the requested diff, branch or PR for introduced defects and actionable
maintainability problems. Repair supported findings unless review-only was
requested. Broad structural audits use Architecture Review.

A delegated reviewer skips coordination and follows **Review the assigned change**
without spawning agents or making repairs.

## Pin the target

Resolve the actual PR base/head or the branch's configured comparison upstream.
Use the merge base and account for staged, unstaged and untracked changes in a
working-tree review. Read every changed path and recover omitted patches from
the exact revisions. With no reviewable diff, stop without spawning a reviewer.
Recover intended behavior from the request, requirements and source; keep the
comparison fixed. Refresh it if the reviewed content changes unexpectedly.

## Independent review

`low` is the default and launches exactly one fresh reviewer. A positive number
overrides the presets. Presets set reviewer counts, not model reasoning effort:

| Level | Reviewers | Distinct assignments |
|---|---:|---|
| low | 1 | Whole change |
| medium | 2 | Split paths, or correctness and design |
| high | 3 | Correctness; design/simplicity; tests/security/performance |
| xhigh | 4 | High plus downstream effects outside the diff |
| max | 5 | Xhigh plus a different model through Ask Model when available |

On Codex, explicitly pass `fork_turns: "none"` on every reviewer spawn. Never
omit it or inherit the implementing conversation. Give the reviewer the fixed
target, intended behavior, applicable ancestor and changed-directory instructions,
changed paths and assigned focus. Let it inspect source directly, without the
implementer's conclusions. Use a read-only adversary role; an implementer cannot
independently review its own work. For an explicitly named external reviewer,
prepare that handoff and wait for its result rather than silently substituting.
If fresh review is unavailable, review locally and label independence unavailable.

Partition multiple reviewers' assignments rather than giving everyone the same
diff. Allocate the requested budget to consequential risks; do not add discovery,
verification, per-finding or consensus agents. Wait for all assigned findings,
merge duplicates, and resolve material uncertainty with a targeted check or the
same reviewer. Do not repeat their investigations. At high or above, request a
final omissions sweep within existing assignments when moved logic or lifecycle
changes make gaps likely; it adds no agents.

## Review the assigned change

A delegated reviewer does not edit, publish, commit or spawn another reviewer.
Inspect the whole assigned diff, relevant callers and tests. Read existing
validation; do not run builds or test suites during review. Use
[review-checks.md](references/review-checks.md) for evidence and downstream checks.
For PRs, finish independent inspection before reading existing review discussion,
then inspect current checks and unresolved threads. External posting requires
the user's authorization.

## Findings and repairs

Keep only discrete, consequential issues introduced by this change, supported
by a reachable scenario, source and applicable requirement. Reject speculative,
pre-existing, intentional or unsupported stylistic objections. A no-findings
result is valid. Verify candidate findings before returning all of them.

Report findings first, ordered by severity, with a concise title, exact changed
location, trigger, consequence and smallest repair. Use P0 for universal release
blockers, P1 urgent, P2 ordinary, P3 low-impact; style findings require a cited
local convention. Explain remaining validation gaps after the findings.

The coordinating implementer repairs supported in-scope issues one at a time
and runs affected checks before finishing. Review-only returns findings without
edits. Report out-of-scope or unauthorized repairs unresolved and complete the
rest. Inspect the final diff; ordinary repairs do not restart the review. Start
another review only when requested or the repairs materially change its scope.
For repaired findings, state the fix and checks; do not stop at proposed repairs
when implementation is already authorized.
