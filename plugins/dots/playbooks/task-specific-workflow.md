# Task-specific workflow

Use when no focused engineering playbook fits and the task needs a sequence
of dependent experiments or changes. Ordinary local edits use the common
Feature Development workflow directly.

This reference supplies the technical sequence within
[Feature Development](../references/feature-development.md); its scope, design, review,
planning-only stop, and completion rules still apply. Keep the sequence in the
existing working record rather than creating another plan or decision log.

## Frame

Ground the workflow first. Don't start the run until you can state:

- The definition of done as a falsifiable predicate.
- Scope, quantified: rough units and effort, plus the blockers grounding surfaced.
- The rigor level, proportional to the consequences. One-way doors and high
  blast radius get more. Reversible low-stakes steps get less.

Record the framing and tradeoffs in the existing working record. Feature
Development owns clarification and approval boundaries.

## Design the workflow

Sequence riskiest-unknown-first. Scaffold and verification come before features
when subsequent units depend on them; reuse existing checks and infrastructure.
Capture the pre-change baseline before an intervention that needs comparison.
Build a verification harness only when existing tools cannot establish the
completion predicate.

Write the designed phase list in the same working record.
For dependent migrations or sweeps, read
[Sequence verifiable units](../references/sequence-verifiable-units.md).

## Run the loop

Each unit is an experiment. State the hypothesis, make the smallest change,
measure against the predicate on the real artifact, keep it if it advanced,
revert it if it didn't. Revert only the experiment's own changes and preserve
unrelated work. Stop when the agreed predicate is met; a failed experiment
calls for a revised hypothesis, not a broader assignment.

Verify by inspecting the artifact, never a self-report. When something passes
too easily, suspect the observation method before the system.

A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a
pass. Don't hide a negative. Reuse valid evidence; add an independent check only
when a material uncertainty could change the decision, within the selected
Change Review budget. Report an unresolved blocker when available evidence or
execution limits prevent a supported next step.

Return to Feature Development for completion, using the same evidence and
working record rather than repeating the checks.
