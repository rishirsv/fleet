### Test consolidation

Use for requested suite consolidation, test placement, or cleanup after a task
creates diagnostic tests, fixtures, snapshots, scripts, or inline instrumentation.
Call these temporary artifacts probes. Existing coverage may be sufficient.
Reuse the task's test-admission decision. This playbook does not require new tests
or another review.

1. Establish what belongs to this task. Inspect the existing status and diff
   before creating probes. Retain that baseline in the working context. If prior
   ownership is uncertain, preserve the artifact and report the uncertainty.
2. Name the invariant and choose the lowest layer that can prove it. Use unit
   coverage for a rule owned within one module, integration coverage for component
   interactions such as persistence or retries, and end-to-end coverage when
   lower layers cannot establish the user-visible contract. Multiple layers need
   distinct failure modes. Keep early live observations independent of this
   placement decision. They need not become permanent automated tests.
3. Find the existing suite at that owner. Reuse sufficient coverage without edits.
   Otherwise, extend an existing behavior test or add a case in that suite.
   Create a file only when the existing files cannot express the case clearly.
   A standalone regression suite needs a deterministic, durable contract that no
   existing suite can cover cleanly. Convenience alone does not justify one.
4. Give each task-created probe a disposition. Promote the smallest deterministic
   version that catches a meaningful regression and adds unique coverage at its
   owner. Merge unique assertions into an existing behavior test and remove the
   redundant probe. Drop diagnostic-only or redundant artifacts, including inline
   instrumentation. Do not keep implementation-coupled, speculative, flaky, or
   costly probes merely because they helped the investigation.
5. For each deletion of durable coverage, name a surviving check that protects
   its contract or the requirement explicitly retired by this task. Assess deletions together.
   Tests removed in the same group cannot protect each other. Preserve distinct
   privacy, persistence, concurrency, retry, lifecycle, and external-boundary
   coverage. Similar names and passing totals do not establish redundancy.
   Removal of pre-existing tests requires suite consolidation or requirement
   retirement within the task's scope. Routine probe cleanup covers only this
   task's artifacts and must preserve unrelated edits. A diagnostic probe that
   never protected an accepted contract needs no replacement test.
6. Finish cleanup before final verification. Run the affected target and required
   repository checks. Reuse completed checks when the final code they covered is
   unchanged. For a new regression test, reuse failing-then-passing evidence or
   obtain it when cheap and safe. Do not build extra infrastructure for that proof.

During review-only work, inspect placement and proposed deletions and report
probe dispositions. Do not edit files or run implementation verification steps.

**Reply:** the invariant, owning layer and suite, retained or merged coverage,
probe cleanup, checks actually run, and unresolved coverage. During implementation,
include these decisions in the existing task report without a separate checklist.

Adapted from Instructa's [consolidate-test-suites skill](https://github.com/instructa/agent-skills/blob/main/skills/engineering/consolidate-test-suites/SKILL.md).
