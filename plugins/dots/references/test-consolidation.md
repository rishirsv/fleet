# Test consolidation

Contents:

- [Decide whether the test should exist](#decide-whether-the-test-should-exist)
- [Placement rules](#placement-rules)
- [Regression signal](#regression-signal)
- [Decision order](#decision-order)
- [Owning layer rules](#owning-layer-rules)
- [Exception for standalone regression tests](#exception-for-standalone-regression-tests)
- [Duplicate cleanup](#duplicate-cleanup)

Keep tests that detect regressions. Prove each lasting rule once at the layer
responsible for that rule, using a check that can verify it.

Definitions:

- Invariant: the rule that must stay true.
- Owning layer: the lowest layer that truly owns and can prove that rule.
- Canonical suite: the normal existing suite for that owning layer.

Default: reuse an existing canonical suite. Create a standalone regression test
only when the exception below allows it.

## Decide whether the test should exist

Before choosing test APIs or placement:

1. Name the durable invariant and its owning layer.
2. Name the plausible regression and resulting user or system harm.
3. Search for an existing test, type, static check, or other proof that already
   owns it.
4. Prefer static analysis, rendered evidence, or manual platform verification
   when those prove the invariant more truthfully than an automated test.
5. Reject coverage that requires broad fakes or repeats the same invariant at
   another layer.
6. Before deleting a suite that checks several kinds of behavior, list its
   privacy, data-integrity, persistence, concurrency, retry, lifecycle, and
   external-system contracts, and give each a surviving owner.

## Placement rules

- Choose one primary owning layer for the invariant: unit, integration, or
  end-to-end.
- Cover an invariant in a second layer only when that layer catches a different
  failure mode, and name that failure mode.
- Assert implementation details only when that implementation unit itself owns
  the invariant; otherwise a refactor breaks the test without a regression.
- Speed or convenience alone does not justify a standalone regression test.
- If the invariant and owning layer cannot be named, stop and report that
  placement is not justified.

## Regression signal

Review whether changed tests detect plausible regressions. Test count does not
establish this. Reconsider:

- a test double that computes the production outcome; a double may configure,
  record, delay, fail, or cancel;
- assertions about exact copy, layout, styling, motion, haptics, timing, or
  source structure unless an external, privacy, accessibility, persistence, or
  compatibility contract requires that exact value;
- assertions about repository or collaborator calls or forwarding when the durable result can be asserted;
- an expected value computed by calling the code under test, or a fixture or
  constant compared with itself;
- an assertion that only checks the call did not throw or returned something
  defined or truthy;
- a broad snapshot when one field carries the contract, so unrelated changes
  fail it and reviewers approve updates unread;
- a regression test whose failing run was never observed, or failed for a
  different reason than the defect it targets;
- a new test file created only to mirror a new production symbol; and
- test-only launch flags, hooks, or fixtures without a current owner and removal condition.

## Decision order

Choose the first option that fits, because each later option adds a file or
suite that future maintainers must find:

1. Add to an existing test in an existing file in the owning layer.
2. Add a new test to an existing canonical file in the owning layer.
3. Create a new file inside the existing canonical suite in the owning layer.
4. Create a standalone regression-style test only if the exception rule passes.

## Owning layer rules

Choose unit when:

- one module owns the rule, and
- the bug reproduces without I/O, transport, persistence, retries, IPC, orchestration, or lifecycle coupling.

Choose integration when:

- the rule lives at a boundary between components, or
- the bug depends on serialization, persistence, ordering, replay, retries, IPC, process lifecycle, or multi-component coordination.

Choose end-to-end only when:

- the user-visible contract cannot be trusted from lower-layer tests alone.

Tie-breakers:

- If torn between unit and integration, choose integration.
- Choose a higher layer for the contract it owns. Uncertainty about the cause,
  or easier reproduction there, does not justify end-to-end or another higher
  layer.

## Exception for standalone regression tests

A standalone regression-style test is allowed only if all are true:

- no existing canonical suite can express the case cleanly
- the reproduction is deterministic
- the case protects a lasting contract or a failure that must remain covered
- adding it to the canonical suite would make that suite less clear

If any condition is false, fold the coverage into the canonical suite.

## Duplicate cleanup

After placing coverage:

1. Search for tests that assert the same invariant.
2. Keep the strongest test in the layer responsible for the rule.
3. Merge any unique assertions into that location.
4. Delete or simplify weaker duplicates.
5. Rename tests by behavior and owner, not by ticket number or bug history.
