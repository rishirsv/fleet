# Feature development

Contents:

- [Choose the route](#choose-the-route)
- [Follow the common workflow](#follow-the-common-workflow)
- [Stop at a planning handoff when requested](#stop-at-a-planning-handoff-when-requested)
- [Completion](#completion)

Use this playbook when the user explicitly selects Dots, `$dots`, or Dots
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
- **Bug fix:** read [Bug fix](../playbooks/bug-fix.md).
- **Refactor:** read [Refactoring](../playbooks/refactoring.md).
- **Performance:** read [Performance](../playbooks/performance.md).

Load only the selected playbook. It owns the route's technical sequence; apply
the common workflow's scope, design, proof, and completion rules within that
sequence, not as a second pass. For a plan-only request, use the playbook to
define the work and proof, then stop at the planning handoff below.

An investigation of what a named change could break beyond its diff belongs
to [Blast radius](../skills/blast-radius/SKILL.md). This does not authorize a fix.

If no route fits and the task needs dependent experiments or changes, read
[Task-specific workflow](../playbooks/task-specific-workflow.md). Otherwise use
the common workflow below directly.

Before you report or act on a benchmark, speedup, or regression you measured,
apply [Performance measurement](performance-measurement.md).

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
   Apply the installed `$design` skill when visible product UI needs design guidance, then return
   here.
4. **Implement.** Build the complete authorized change in checkable units. A
   unit with a clear scope, defined behavior, source locations, and an
   executable check may go to a cheaper worker; the coordinator retains design
   decisions, integration, review, and final proof. Return to step 3 when
   repeated implementation problems show that the selected module boundary or
   data shape is wrong.
   For dependent migrations or sweeps, read
   [Sequence verifiable units](sequence-verifiable-units.md) unless already loaded.
   For a repetitive edit across many sites:

   - Prefer an existing rename operation or codemod. If a custom tool is needed,
     do the first unit by hand to learn the recipe, then build the tool. Prove
     it by rerunning it on that unit and diffing against your hand-done version.
     Make the tool safe to rerun.
   - A deterministic tool beats fan-out. If the tool can process every unit
     in one pass, run it yourself. Don't fan out delegates to hand-apply what
     a script can do.

   Record consequential decisions made during implementation that the request
   or plan left open. Include the reason, tradeoff, and whether the decision is
   provisional. Reopen a settled decision only when new evidence changes it.
5. **Prove it.** Exercise the real product path when one exists. A build or
   unit test does not by itself prove an integration or visible behavior; verify visible output with
   [Visual proof](visual-proof.md). Bugs use the original reproduction;
   refactors compare behavior with the recorded baseline; performance work
   repeats the same measurement on the fixed input. When the repository has a
   `verify-<app>` skill, drive the change with it and fix its feature map if
   the change made the map wrong.
   Place new or moved tests and establish their regression signal with
   [Test consolidation](test-consolidation.md).
6. **Review and finish.** Inspect the final diff against the requested outcome.
   Before finishing, reconcile every requirement and consequential recorded
   decision with the final implementation. Each must be implemented and
   supported by appropriate evidence, explicitly require no code, or remain
   identified as an unresolved gap.
   Apply `$change-review` when the user requests a review, repository
   policy requires it, or consequential behavior needs independent challenge;
   it owns review scope, reviewer handoff, findings, repair, and review-only
   requests. Add the installed `$design-review` skill when that review covers visible UI.
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

If the Design plugin is unavailable, complete UI work directly using the product's
existing design system and this plugin's visual-proof guidance. Do not require
a second plugin to finish an engineering task.
