---
name: verify-reconstruction
description: Test a recovered explanation, specification or implementation against the original app, binary or recorded behavior. Builds the appropriate comparison harness, checks the comparator itself, and fixes the earliest meaningful divergence.
---

# Prove the behavior that matters

Accept an original target plus a claim, spec or candidate implementation. Discover
existing fixtures/logs; do not require a prepared test plan. If the reference or
candidate is ambiguous, resolve it before comparing. Record exact build identities
and the requested behavior. Use [REA evidence workflows](../reverse-engineer-anything/references/evidence-workflows.md)
when the available typed `verify_reconstruction` tool fits the claim. Its pass is
bounded to declared comparable claims; ordinary harnesses remain useful.

## Choose the oracle and adapter

The expected behavior must come from outside the candidate: original execution,
retained observations, independently documented vectors, or held-out source for a
known target. Tests generated from the same mistaken spec are not independent.
When only static evidence exists, review semantics and report the untested runtime
claims rather than inventing expected output.

Read [comparison harnesses](references/comparison-harnesses.md) and choose the
observable surface that matches the request:

| Behavior | Compare |
| --- | --- |
| Pure function or recovered algorithm | Same inputs → return values, output buffers and relevant side effects |
| Parser, format or CLI | Input fixtures → accepted/rejected result, decoded fields, bytes, exit status and errors |
| Stateful feature | Same initial state + action sequence → intermediate results, persistent state and next launch |
| GUI feature | Same interaction and data → visible state, enabled actions, accessibility values and resulting effects |
| Network-backed flow | Captured or permitted observed requests/responses → client transformations, ordering and local state |
| Compatibility port | Original and rebuilt artifacts → scoped functional scenarios; byte identity only if explicitly required |

Do not silently replay saved traffic. Distinguish local behavior from a remote
contract that was observed only for certain samples. Keep simulator/device and
version differences in the comparison rather than normalizing them away.

## Test the tests before trusting a pass

Establish a known match and a deliberate mismatch: alter an expected value, omit
a required field, or use a visibly wrong candidate. The comparator must detect it.
Verify that the harness actually invoked both intended builds, consumed their
outputs, and compared nonempty cases. Missing output, crashes, timeouts and skipped
cases must not collapse into equality. Confirm any normalizer preserves the claim
under test. Fix a broken harness before changing the reconstruction to satisfy it.

## Probe the weakest claims

Start with a representative successful scenario, then select cases at the uncertain
boundaries: below/at/above thresholds, high-bit bytes, width/overflow, empty and
truncated inputs, retries, restart, reordered actions and errors. Choose useful cases
from the recovered behavior; do not blindly pass unsafe pointers into a native
function. Validate the ABI/calling convention before a direct native harness.

For stateful work, test sequences and persistence, not only isolated operations.
For nondeterministic work, control seed/clock/fixture state or state an explicit
invariant and tolerance. A tolerance needs a behavioral reason. Record intermediate
observations when equal final output could conceal a different state transition.

A runtime probe operates within the request's target and action scope. Preserve
originals and use task-owned fixtures. If access or execution is unavailable, keep
that case unverified and proceed with independent evidence that is available.
For training/calibration only, use the optional
[known-target exercise](references/known-target.md); do not substitute it for tests
of the actual requested target.

## Follow a mismatch to its cause

Save the failing input/sequence, reference result and candidate result. Minimize it
while preserving the failure. Find the earliest divergent value or state transition,
then inspect the corresponding code/evidence: argument lowering, branch predicate,
format conversion, initialization, persistence or asynchronous ordering. Revise the
spec when the hypothesis was wrong; revise the implementation when it violates a
supported rule. Preserve the failing case as a regression and rerun affected paths.

For consequential ambiguous reconstructions, an independent reviewer can challenge
the raw evidence, spec and logs when delegation is authorized. Give it the uncertain
question rather than the expected verdict. Escalation should resolve a concrete gap,
not require a named model or an expensive review of already settled behavior.

Retain commands, identities, input corpus/seeds, reset procedure, raw results,
comparator configuration and exit status in the investigation workspace. Only report
executed tests with actual results; a proposed case remains proposed. Stop expanding
the suite when the requested acceptance scenarios pass and material uncertainty is
resolved; further unrelated tests do not improve the scoped result.

Return verified, contradicted and unresolved behaviors with log references, the
comparison coverage and how to rerun. A finite suite demonstrates those scenarios,
not whole-program equivalence. If working code was requested, complete authorized
fixes and rerun comparisons rather than returning a mismatch report alone.
