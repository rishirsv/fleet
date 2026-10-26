---
name: figure-it-out
description: "Design an auditable playbook for substantial work whose execution path is uncertain. Scales rigor to the task, runs a hypothesis loop, and logs decisions. Use when explicitly asked for /figure-it-out or to figure out a substantial task whose execution path is uncertain."
---

# Figure it out

When explicitly invoked for substantial work whose execution path is uncertain, design a playbook. Size, duration or the absence of a narrower playbook alone does not trigger this skill. The deliverable before any code is the workflow itself: a sequence of phases that scales rigor to the task, runs the scientific method, and leaves a decision trail a human can audit after stepping away.

## Start

Read the [pstack router](../pstack/SKILL.md) for the available skills and delegation rules. Open a todolist with the phases below as todos.

## Phase A: Frame

Ground first, then commit. Don't start the run until you can state:

- The definition of done as a falsifiable predicate.
- Scope, quantified: rough units and effort, plus the blockers grounding surfaced.
- The rigor level, proportional to the uncertainty and consequences. One-way doors and high blast radius get more. Reversible low-stakes steps get less. Rigor is gates and artifacts, not "try harder".

Present the framing and tradeoffs before committing to a long run. Reversible work proceeds, but a multi-hour run earns one checkpoint.

## Phase B: Design the workflow

Decompose into atomic, independently-landable units. Sequence riskiest-unknown-first. Identify how each unit will be checked before implementing it. Use existing checks when they establish the required behavior.

- When existing checks cannot establish the outcome and the stakes justify it, build the missing verification before the work, with the baseline captured from the pre-change state, so the check reads as "old value vs new value". For a prototype, direct observation is the check; use the [Prototype playbook](../../playbooks/prototype.md).
- For one-way-door design decisions, run the [architect](../architect/SKILL.md) skill. Skip it for mechanical work whose shape is already concrete. A second design exploration over a settled design is over-engineering.
- Decide what fans out. Parallelize only across seams, and give each writing worker its own worktree or disjoint output path. Don't over-fan. Use [swarm](../swarm/SKILL.md) when independent parallel work is useful; the [pstack Subagents section](../pstack/SKILL.md#subagents) owns model and tool selection.
- Write the designed phase list down. That list is what the human reviews.

Then execute the design. Add its steps to the todolist as concrete items between the Phase C and Phase D entries. Run each under the Phase C loop discipline, and weave the Phase D log through them, a row as each step lands, rather than saving the whole trail for the end.

## Phase C: Run the loop

Each unit is an experiment. State the hypothesis, make the smallest change, measure against the predicate on the real artifact, keep it if it advanced, revert it if it didn't. Check each dependent unit before building on it instead of batching checks at the end. Use the smallest check that establishes the relevant outcome.

- Verify by inspecting the artifact, never a self-report. When something passes too easily, suspect the observation method before the system.
- Use [change-review](../change-review/SKILL.md) when consequential code changes need independent review. Do not add a judge to every delegated step. If a worker games the gate, reset and harden the contract. If the gate itself is wrong, fix the gate in its own change rather than routing around it.
- A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass. Don't hide a negative.

## Phase D: Keep the audit trail

Record decisions, evidence, rejected approaches and unresolved questions as the work proceeds. Keep a short in-chat trail for ordinary runs. Save a decision-trail file when the run is long or consequential enough that the user needs to audit it later; commit it only when requested or required by the repository. Reuse an existing task record rather than creating a parallel log.

## Phase E: Verify and hand back

Check the whole against the Phase A predicate on the real product, not just the harness. A recurring correction may warrant [self-improve](../self-improve/SKILL.md), but do not automatically add a gate, lint rule, check or script. Keep durable workflow changes within the requested scope.

**Reply:** the playbook you designed, the rigor level and why, the decision trail or its path, what's verified against the predicate, and what's still open.
