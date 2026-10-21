---
name: formal-verification-skill
description: "Creates or refreshes a project-local formal check for one consequential invariant. Use for a reusable formal-verification workflow, not app smoke tests or general code review."
---

# Formal verification skill

Create or refresh a maintained check for one property that is expensive to get
wrong and poorly covered by ordinary tests. Read the responsible code before
choosing the property or tool. If a normal test answers the question more
cheaply, recommend that test instead of creating a formal artifact.

Use [Verification skill](../verification-skill/SKILL.md) for driving the real
app. A formal result supplements runtime evidence; it does not prove that the
application starts, renders correctly, or follows the modeled transitions.

Create when no check covers the property. Refresh when a check exists and its
covered code, assumptions, or tools have changed. Keep artifacts in the
repository's established verification and project-skill locations. Name the
generated skill `verify-<app>-<property>` so its scope is visible.

Work within the requested artifact scope. Do not repair product code, install
toolchains, change CI, or publish artifacts unless the request authorizes it.
When a required tool is unavailable, report the prerequisite and leave an
unexecuted artifact labeled draft.

Before any run, including an existing check during refresh, set a time and
memory budget and record how the command or tool configuration enforces it.
An exhausted budget is inconclusive; do not raise it automatically.

## Create

1. **State the property.** Define the allowed inputs, initial state, expected
   invariant or progress condition, and the consequence of violating it.
   Derive the expected behavior from the requirement, not from the current
   implementation. Identify the source paths and all writers that can affect it.
2. **Choose the method.** Use a state model for interleavings or protocol
   behavior, a code-level verifier for a property of the implementation, or
   a proof when the claim must hold beyond finite bounds. Choose by the
   question and available toolchain, not by a preferred language or template.
   Record assumptions, excluded behavior, finite bounds, and any fairness
   conditions. Distinguish bounded exploration from an unbounded proof.
3. **Connect the check to code.** Map model state and transitions to source
   symbols and operations. Preserve actual atomicity, shared writers, failure,
   retry, and cancellation boundaries relevant to the property. List where
   the model abstracts away implementation detail and what supports each
   abstraction. A passing model with an unverified mapping remains a model
   result, not an implementation guarantee.
4. **Run and challenge it.** Run the check and retain its result. Check that
   valid inputs and important transitions are reachable, so contradictory
   assumptions cannot make the property pass vacuously. Use a plausible
   property-violating mutation of the covered code as a negative control in
   an isolated copy or worktree. The verification workflow must detect it,
   either through a code-level failure or a detected mismatch with the model.
   Changing only the model does not establish sensitivity to production code.
   Restore the mutation, rerun, and verify cleanup. If a safe negative control
   cannot run, report that gap rather than claiming it passed. Do not weaken
   the property, assumptions, or state space to hide a counterexample.
5. **Make it repeatable.** Write the project skill with the exact tool version,
   configuration, one rerun command, expected success/failure results, evidence
   location, code mapping, and maintenance triggers. Include model or harness
   files only when the method needs them. Record the source revision last
   checked; for uncommitted code, record the relevant diff or content hashes
   rather than treating HEAD as its identity. Run the documented command from
   the documented starting directory before calling the artifact usable.

## Refresh

Compare the recorded source baseline with current covered code, callers, and
writers, including newly introduced ones. A path list alone cannot establish
that coverage is unchanged. Recheck tool versions, assumptions, atomicity,
bounds, and source mappings that the changes affect.

Run the existing check before editing and retain that result. If an intended
requirement changed, cite the requirement or accepted change and record the old
and new property. A passing result alone is never a reason to change a property.
Translate each counterexample into steps in the actual code; an impossible
step is a modeling defect, not a product-bug finding.

Classify the result:

- **Current:** the mapping still holds and the documented check passes.
- **Corrected:** the model, mapping, or harness had drifted; correct only the
  verification-owned files and rerun the affected checks and negative control.
- **Product bug:** a counterexample corresponds to allowed production behavior.
  Preserve the failure and intended property; report the trace and source path.
  Artifact maintenance alone does not authorize a product fix.
- **Blocked:** the tool, source mapping, required state, or execution is missing,
  or the solver returns unknown or times out. State what remains unestablished.

Update the recorded baseline only after checking the mapping and rerunning the
documented command successfully. Preserve unresolved findings. Changes to
covered operations, shared writers, contracts, tool versions, or assumptions
trigger a refresh; unrelated UI changes do not require a solver run.

## Report

Report the property, artifact location, source baseline, command and tool
version, result, negative-control result, bounds, assumptions, and exclusions.
Separate facts established about the model from facts established about the
implementation. An unchecked mapping, unknown result, or draft is not a pass.
Keep real-app and regression evidence under their existing owners.

Write with [Writing style](../../references/writing-style.md).
