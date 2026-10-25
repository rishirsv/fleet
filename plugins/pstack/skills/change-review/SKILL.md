---
name: change-review
description: "Reviews a diff, branch, commit, or pull request for defects and maintainability, with configurable independent reviewers. Repairs supported findings unless the user requests review-only."
---

# Change Review

Review the requested change for real bugs and useful cleanup, then repair
supported findings. A broad audit of existing code uses Architecture Review.
This skill owns the review lenses, evidence bar, findings format and repair
workflow; reviewer roles supply independent execution.

## Invocation

The skill identifier is `change-review`; its display name is **Change Review**.
Accept the level, mode and target in any order:

- `$change-review low` — one fresh reviewer, then repair supported findings.
- `$change-review medium review-only #123` — two reviewers, findings only.
- `$change-review 3 main` — three reviewers against the named base branch.

Treat “Change Review low” as the same request. With no level, use `low`. With
no target, review the current branch and its uncommitted changes. `review-only`
returns findings without edits. An explicitly delegated review is always
read-only: do not modify files, create commits, push branches, post review
comments, or delegate the review to another agent. A delegated reviewer uses
the fixed target, skips coordinator instructions and Phase 2, and returns
findings using Phase 3.

## Phase 0 — Gather the diff

Read the applicable `AGENTS.md` instructions, including ancestor and changed
directory guidance. Recover intended behavior from the request, PR description,
requirements, commits and source.

- **Pull request:** resolve its actual base and head; compare what would merge.
- **Base branch:** resolve the comparison ref to the base branch's configured
  upstream when that upstream exists and is ahead of the local branch;
  otherwise use the local branch. Run `git merge-base HEAD <comparison-ref>`
  and inspect the diff from that merge base. If the local base cannot be
  resolved, try its configured upstream or remote-tracking ref before reporting
  that the target is unavailable. Do not assume the feature branch's own
  tracking ref is its merge base.
- **Commit:** inspect the specified commit against its parent; for a merge,
  establish which parent defines the requested comparison.
- **Working tree:** include staged, unstaged and untracked changes. A tracked
  diff alone does not include new untracked files; enumerate and read them too.

Record the exact revisions and changed paths. Recover omitted or truncated
patches from those revisions. Keep the target fixed; if it changes unexpectedly,
refresh the affected scope before relying on the review. With no reviewable
diff, report that and stop before launching reviewers.

## Phase 1 — Review

### Assign reviewers — coordinator only

Levels set reviewer counts, not model reasoning effort. `low` launches exactly
one fresh reviewer covering every lens. Larger requested levels permit parallel
assignments; a positive number overrides the presets. Do not increase the count
automatically or add agents for discovery, finding verification or consensus.

| Level | Reviewers | Distinct assignments |
|---|---:|---|
| low | 1 | Whole change, all lenses |
| medium | 2 | Split paths with all lenses, or correctness/security/tests and reuse/simplification/efficiency/altitude |
| high | 3 | Correctness/security; reuse/simplification/altitude; efficiency/tests |
| xhigh | 4 | High plus downstream effects outside the diff |
| max | 5 | Xhigh plus a different model through Ask Model when available; otherwise another distinct risk |

On Codex, explicitly pass `fork_turns: "none"` on every reviewer spawn. Use a
read-only adversary role. An agent that implemented any part of the change must
not serve as its independent reviewer. Give each reviewer the fixed target,
intended behavior, applicable instructions, changed paths and assigned lenses.
Let it inspect source directly without the implementer's conclusions. Supply
this skill as the review contract; do not duplicate its rules in role prompts.

For multiple reviewers, dispatch independent assignments together and cover all
lenses across them. Give every changed path a primary owner when partitioning
by paths; reviewers may trace callers outside their scope for context. Avoid
giving everyone the same undivided assignment. At high or above, include an
omissions sweep in existing assignments when moved logic, default changes or
lifecycle changes make gaps likely.

For a named external reviewer, use Ask Model when supported or prepare the
requested handoff and wait for its result. Do not silently substitute a model.
If independent review is unavailable, review locally and state
`Independent review unavailable.`

### Inspect the assigned change

Apply the assigned lenses across the complete diff; continue after finding
the first issue. Check relevant tests and call sites to confirm findings. Read
existing validation; do not run builds or test suites during review. A focused
read-only probe may establish a disputed fact.

For PRs, finish independent inspection before reading existing review discussion,
then inspect current checks and unresolved threads. Apply the following lenses
within the assigned scope.

### Correctness

Review the diff as a careful senior engineer would: read every hunk, open the
surrounding files for context as needed (Read, Grep, git log/blame/show), and
hunt for correctness issues — wrong or inverted conditions, off-by-one,
null/undefined dereference, missing `await`, dropped error handling, removed
guards or validations, broken callers of changed functions, races. Prefer real
failure modes over style; every finding needs a concrete scenario in which the
code misbehaves.

Trace state transitions, cancellation, empty inputs, repeated execution and
interruption midway through a write. For deleted logic, identify its invariant
and surviving owner. For wrappers and caches, verify forwarding reaches the
intended instance without recursion. For shared writers, inspect atomicity or
serialization and whether independent outputs can remove unnecessary sharing.

For downstream risk, name the fact safety depends on. Look beyond symbol
searches at persisted data, wire formats, configuration, generated code,
scheduled jobs and other consumers. An empty text search alone does not prove
absence. Preserve real external and user-data compatibility while removing
obsolete internal paths.

### Security

Trace untrusted input through authorization, parsing, storage and external
writes. Check trust boundaries, secret exposure, destructive effects and failure
or retry behavior. Demonstrate a reachable security problem introduced by the
change; a generic warning is not a finding.

### Reuse

Flag new code that re-implements something the codebase
already has — Grep shared/utility modules and files adjacent to the change,
and name the existing helper to call instead.

### Simplification

Flag unnecessary complexity the diff adds: redundant or derivable state,
copy-paste with slight variation, deep nesting, dead code left behind. Name
the simpler form that does the same job.

Before removing a boundary, determine whether necessary complexity would spread
into callers. Keep translation at real external boundaries. Do not confuse
local repetition with competing policy owners or flag formatter-enforced details.

### Efficiency

Flag wasted work the diff introduces: redundant computation or repeated I/O,
independent operations run sequentially, blocking work added to startup or
hot paths. Name the cheaper alternative.

For long-lived closures or captured environments, demonstrate which values
remain reachable and why their lifetime creates material retention. Recommend
capturing only needed fields when that fixes the problem; a closure alone is
not evidence of a leak. Check scaling, unbounded work, pagination and resource
cleanup. Support performance claims with measurements or a concrete cost model.
Every retry needs a reason, refreshed state or backoff and a stopping bound.
One failed batch item should not prevent independent items from completing.

### Altitude

Check that each change fixes the root cause at the right depth rather than
patching a symptom with a fragile bandaid. Special cases layered on shared
infrastructure are a sign the fix isn't deep enough — prefer the simpler, more
general change to the underlying mechanism over adding special cases, and name
that change.

A cast, default, fallback or retry needs a reachable legitimate state; otherwise
it may hide the producer's contract failure. Keep parsing and normalization with
the responsible boundary. Root-cause placement does not authorize redesigning
unrelated code.

### Tests

Treat tests as claims about observable behavior. Derive expected results
independently of the implementation. A useful test rejects a plausible broken
behavior and survives an internal refactor with identical observable results.
Flag vacuous assertions, production logic inside doubles, broad snapshots
unrelated to the contract and duplicate coverage that adds no failure signal.

For an absence assertion, check a companion case where the effect occurs so
the test demonstrates it can observe it. Prefer the existing suite at the
invariant's owner; another layer needs a distinct failure mode. Before deleting
tests, identify surviving coverage for privacy, persistence, concurrency, retry,
lifecycle and external-system contracts. Existing passing results establish
only the behavior exercised. Exact UI claims need rendered evidence.

### Keep only supported findings

Flag an issue only when all of these are true:

- It affects correctness, security, performance, or maintainability in a meaningful way.
- It is discrete and actionable.
- It was introduced by the reviewed change.
- The affected scenario or call path can be demonstrated from the code.
- The author would probably fix it if they knew about it.

For a bug, show the trigger and incorrect behavior. For cleanup, show the
concrete cost — what is duplicated, wasted or harder to maintain — and the
behavior-preserving replacement. Cite the applicable requirement when claiming
a specification violation. Do not flag speculative concerns, pre-existing
problems, intentional behavior changes, or style nits that do not obscure the
code. Return every qualifying finding without a quota or ceiling.

If an omissions sweep was assigned, reread the diff and enclosing functions
for defects absent from the current findings, especially moved guards, changed
defaults and asymmetric setup/teardown. Confirm new candidates against the same
evidence bar and return one combined result; an empty sweep is valid.

## Phase 2 — Apply the fixes — coordinator only

Wait for all assigned reviewers, then deduplicate findings about the same
mechanism while preserving their evidence. Resolve material uncertainty with
the smallest targeted check or a focused follow-up to the same reviewer; do
not repeat the whole investigation or send findings to verification agents.

For `review-only`, proceed to Phase 3. Otherwise, fix every supported issue
within the original task scope, one at a time. Run affected checks and inspect
the final diff. Do not stop at proposed repairs when implementation is already
authorized. A cleanup must preserve intended behavior; a bug fix must restore it.

Skip false positives and repairs requiring new authority, unrelated work or an
unsettled behavior change. Complete the other repairs and report consequential
skips or unresolved findings with their reason. Ordinary repairs do not restart
the review; another review needs a user request or materially changed scope.
Posting comments, publishing a PR or starting ongoing monitoring requires the
corresponding request; Publish PR and Babysit PR own those workflows.

## Phase 3 — Write the result

Present findings first, ordered by severity. Use one entry per issue in this form:

`[P1] Imperative finding title — path/to/file.rs:line`

Follow the title with one short paragraph explaining the affected scenario and
why the behavior is wrong, or the concrete maintenance cost and smaller
replacement. Keep the cited range as small as possible and make sure it overlaps
the reviewed diff. When repairs were requested, mark findings as repaired or
unresolved and state the reason for any unresolved finding.

Use these priorities:

- `P0`: universal release blocker or critical failure.
- `P1`: urgent defect that should be fixed next.
- `P2`: ordinary defect that should be fixed.
- `P3`: low-impact issue that is still worth fixing.

If there are no qualifying findings, say `No findings.` Do not invent a finding
to fill the result. After the findings, add a brief overall assessment and mention
any material test gaps or residual risks. For applied repairs, summarize the
checks and their observed results. Use native structured findings when available,
but keep the findings visible in the final reply. Omit investigation chronology,
rejected candidates and praise.
