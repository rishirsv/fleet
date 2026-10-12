# Feature development

Contents:

- [Choose the route](#choose-the-route)
- [Performance hypotheses](#performance-hypotheses)
- [Follow the common workflow](#follow-the-common-workflow)
- [Stop at a planning handoff when requested](#stop-at-a-planning-handoff-when-requested)
- [Completion](#completion)

Use this playbook when the user explicitly selects Dots, `$index`, or Dots
Feature Development for features, bug fixes, refactors, measured performance
work, configuration changes that affect behavior, or their plans. Handle
ordinary requests directly with any applicable focused skills.

Keep one compact working record in the active task with the outcome, non-goals,
settled decisions, responsible code, chosen direction, current route, and proof
status.

For work spanning sessions or several implementation passes, save the working
record in the repository's established plan location when one exists. Otherwise,
keep the record in the active task and include it in the handoff. Keep one current
next action, completed and remaining work, blockers, and verification evidence.
Update it when discoveries change the plan and before a handoff. Replace stale
instructions rather than appending another status summary.

## Choose the route

- **Feature:** add or change behavior. Define the data or state and the
  component responsible for it before distributing logic across callers.
- **Bug fix:** reproduce the reported symptom where it occurs before
  changing code. Form competing hypotheses, run checks that distinguish them,
  and confirm the cause supported by those checks. The original reproduction must pass
  after the fix. When two fixes have failed and both rested on the same
  assumption, test that assumption directly before trying a third.
- **Refactor:** record the behavior that must remain stable, name the target
  ownership or structure, migrate every caller, and remove the replaced path in
  the same change under [Hard-cut policy](hard-cut-policy.md) unless the
  repository requires a staged rollout.
- **Performance:** freeze a representative input and baseline, locate the
  measured cause with a trace or profile, and compare the same measurement
  after each candidate change. Keep measured improvements that preserve the required behavior. Remove
  experiments that do not improve the target or violate those requirements.

If no route fits, use the common workflow below and state what evidence will
show that the requested task succeeded.

Before you report or act on a benchmark, speedup, or regression you measured,
apply [Performance measurement](performance-measurement.md).

## Performance hypotheses

Prefer the cheapest change that meets the target, and stop once one does. The
usual order from cheapest is: stop work whose result nothing uses; avoid
repeating work; do less of it; defer it; move it off the path the user waits
on; run it concurrently; and make the remaining work cheaper. Skip an option
when the measured cause rules it out.

## Follow the common workflow

The steps describe the contract between phases; adapt their depth to the task.

1. **Understand.** Identify the intended result, what must stay true, and what
   would prove completion. Before choosing a design, confirm the facts that
   determine ownership, interfaces, constraints, sequencing, or proof; leave
   ordinary local discovery to implementation. Use read-only investigators only
   when separate investigations would make the work faster or cover more
   relevant evidence.
2. **Settle decisions.** Answer repository-owned questions from source. Use a
   focused probe when observation can resolve a consequential uncertainty;
   apply `$prototype` when an isolated experiment is needed. Make reasonable
   assumptions for routine choices within the requested scope. Ask the user
   for product choices, preferences, authority, or information that would
   materially change the result, and continue work independent of the answer.
3. **Choose the design.** Select the smallest coherent approach that fits the
   existing system. Apply `$architect` when a consequential new or changed
   boundary needs its caller experience, public contract, data or state shape,
   responsible module, or place to test behavior settled before implementation.
   Use Architect for the design phases only, then return here for implementation,
   proof, review, and completion.
   Apply `$ui-design` when visible product UI needs design guidance, then return
   here.
4. **Implement.** Build the complete authorized change in checkable units. A
   unit with a clear scope, defined behavior, source locations, and an
   executable check may go to a cheaper worker; the coordinator retains design
   decisions, integration, review, and final proof. Return to step 3 when
   repeated implementation problems show that the selected module boundary or
   data shape is wrong.
   For a repetitive edit across many sites, make the first one by hand, then
   script the rest and confirm the script reproduces the manual edit.
   Record consequential decisions made during implementation that the request
   or plan left open. Include the reason, tradeoff, and whether the decision is
   provisional. Reopen a settled decision only when new evidence changes it.
5. **Prove it.** Exercise the real product path when one exists. A build or
   unit test does not by itself prove an integration or visible behavior; verify visible output with
   [Visual proof](visual-proof.md). Bugs use the original reproduction;
   refactors compare behavior with the recorded baseline; performance work
   repeats the same measurement on the fixed input.
   Place new or moved tests with [Test consolidation](test-consolidation.md).
   When adding or repairing a regression test, confirm that it fails for the
   intended reason on the broken behavior and passes after the fix. If written
   after the fix, demonstrate the failure using an isolated copy or reversible
   change that preserves unrelated work. Report any missing failing control.
6. **Review and finish.** Inspect the final diff against the requested outcome.
   Before finishing, reconcile every requirement and consequential recorded
   decision with the final implementation. Each must be implemented and
   supported by appropriate evidence, explicitly require no code, or remain
   identified as an unresolved gap.
   Apply `$change-review` when the user requests a review, repository
   policy requires it, or consequential behavior needs independent challenge;
   it owns review scope, reviewer handoff, findings, repair, and review-only
   requests. Add `$ui-review` when that review covers visible UI.
   Report the result, evidence, and important remaining gaps. List the
   decisions you made that the request did not cover, least confident first,
   each with how to reverse it. Apply
   [Evidence in claims](writing-style.md#evidence-in-claims)
   when writing the completion report.

## Stop at a planning handoff when requested

When the user asks only for a plan, stop after step 3. Do not edit product
source. Return a brief that another capable agent can use without guessing the
outcome, responsible code, order of work, or verification. Include:

- the selected outcome and explicit exclusions;
- confirmed current behavior and responsible code;
- the chosen approach and the decisions it depends on;
- units of work that each deliver verifiable behavior, when dependencies or
  separate agent contexts require the work to be divided;
- the source locations each unit should inspect;
- the behavior or scenario that proves each unit; and
- rollback instructions, conditions for a safe release, unresolved blockers,
  and weak assumptions when they affect implementation.

If the user requests an HTML plan, finish the planning decisions here, then
apply `$html` to the verified material and reading order. Start the HTML plan
with a visual explanation of its sequence, dependencies, or decisions. Keep
the full steps and verification details after that explanation. Do not make a durable artifact for a localized change
whose handoff fits clearly in chat.

## Completion

The playbook is complete when the requested behavior works through its real
path, proof supports the result, the final diff has been inspected and any
required review is complete, and
every material gap is stated honestly.

For planning-only work, it is complete when the execution handoff is grounded
in current source, every decision needed for implementation is settled or listed as a blocker,
and the verification checks the requested behavior rather than an unrelated
passing result.
