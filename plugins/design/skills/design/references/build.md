# Plan and build

## Read the context

Identify the platform, scope of change, and any accepted visual target. Inspect
the repository's design guidance, tokens, components, representative screens,
and supplied references that apply to this task. Identify which choices are
required, which references provide inspiration, and which choices are open to
change. Preserve existing product decisions unless the brief calls for
replacing them; resolve meaningful conflicts before committing to a direction.

## Test an open product idea

When asked to evaluate an unsettled idea, or when a material product assumption
is genuinely unresolved, identify the intended user, their problem, existing
alternatives, the proposed change, and what evidence would challenge it. Ask
focused questions only where answers change the decision; label assumptions and
continue with work that does not depend on them. Do not turn a clear build
request into an unsolicited interview or present speculation as research.

## Plan the direction

For new work or a redesign, write a compact plan before building:

- **Palette:** four to six named colors with their values.
- **Type:** the faces and the role each plays.
- **Layout:** the composition and alignment, as a sentence or an ASCII
  wireframe.
- **Principle:** what makes this design specific to its subject.

Review the plan against the brief before writing code. Revise any part that
would come out the same for a similar brief or repeats one of the skill's
generic defaults, and note what changed. Share the plan and any assumption that
could change the design in a short note, then build from the revised plan
without waiting for approval; the user can correct the direction as you work.

## Build or refine

For a focused refinement, keep the settled direction and change only what the
task requires.

Implement the main experience using real content and the relevant craft
references. Default to local HTML for standalone web prototypes. Use a native
preview when the decision depends on platform controls, gestures, or text
scaling. Use the existing stack and design system for product changes. Include
the controls and states needed to complete the requested task.

Inspect the rendered result and exercise its main path, covering the states in
the skill's proof list. For original work, look for material problems in
hierarchy, task flow, states, and accessibility before delivering; a separate
audit report is not required. For an accepted visual target, use [design
QA](design-qa.md). For a focused refinement, inspect the exact changed workflow
at a representative viewport and exercise the affected interaction.

Before treating an exploratory prototype as production-ready, carry the chosen
variant and its settings into the real component. Exercise its actual content,
interaction, accessibility, supported devices, and performance as relevant to
the change; report missing evidence instead of treating the prototype as proof.
Use the target platform's checks rather than assuming web-specific mechanics.

Correct material issues within the requested scope, then inspect the affected
result again. Then use [finish review](../../../references/finish-review.md)
for the final independent comparison and verified corrections, including when
the builder's own check is clean. Keep the handoff proportional to the change;
do not reopen settled design decisions or audit unrelated screens. Report open
findings and evidence gaps at any stop; stopping does not establish readiness.
