---
name: babysit-pr
description: "Monitors a GitHub pull request and fixes failing checks or review feedback within its original goal until it is ready. Use when the user asks to watch or babysit a pull request; not for a one-time status report."
---

# Babysit PR

Monitor the requested pull request and fix failures or review feedback within
its original goal until the latest commit is ready. A one-time status request
does not start monitoring.

Resolve the repository, account, PR, branch and head commit. Prefer connected
GitHub tools; confirm authentication before using `gh`. Record current checks,
merge state and unresolved discussion IDs. A flat comment list cannot establish
which discussions remain open.

Use native completion events or the supported scheduler; reuse an existing
monitor. State the actual cadence, honoring a requested one. Keep the monitor
read-only and quiet unless state becomes actionable, ready, merged or closed.
Read full logs or comments only when relevant state changes. Do not add an
agent to relay unchanged status or keep the main agent in an indefinite poll.
If persistent scheduling is unavailable, use a bounded native wait or report
that monitoring could not be established. Claim it is active only after success.

Discard old check results when the head changes. Investigate the actual failed
run and verify feedback against current code before making an in-scope repair.
Do not repair unrelated problems or speculate about inaccessible external logs.
After a repair, run affected checks, commit and push as this requested workflow
authorizes, and resume monitoring the new head. Update the base only when
required by repository policy or a real conflict.

Follow repository and user authorization for external replies, resolving
threads or requesting automated review; request a new review only when allowed.
Do not merge without a request.

Finish when required checks and reviews pass on the latest commit, no actionable
discussion or conflict remains, or the PR is merged, closed, or requires the
user's decision. Cancel the monitor on completion. Report the PR, current state,
repairs and material gaps.
