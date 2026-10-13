# Plan and build

## Read the context

Identify the platform, scope of change, and any accepted visual target. Inspect
the repository's design guidance, tokens, components, representative screens,
and supplied references that apply to this task. Identify which choices are
required, which references provide inspiration, and which choices are open to
change. Preserve existing product decisions unless the brief calls for
replacing them; resolve meaningful conflicts before committing to a direction.

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

Default to one correction cycle (inspect, fix, inspect again) or the user's
requested iteration limit. Report material remaining issues at the limit;
reaching the limit does not establish readiness.
