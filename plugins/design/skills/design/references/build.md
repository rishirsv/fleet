# Build with what exists

For changes to an existing product. New directions are planned in the design skill itself.

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

## Reuse before building

Build the ask and nothing beside it. Add no sections, badges, counts, captions,
footers, icons inside buttons or sounds the user did not request, and no toast
or dialog for an action whose result is already on screen. Use the native
element before a custom one and a fixed value before a setting nobody will
change. A cut the user has not approved is a proposal, not an edit.

Build in this order: the project's own components, icons and tokens first, then
a maintained library or a platform feature, then custom code. Search the shared
components before writing UI and name what you found; a new component, style or
icon that duplicates one the project has is a finding. Use a component's
variants rather than restyling it locally, and keep one style per kind of thing:
one menu, one table, one dialog shell. When a fix applies to every instance,
make it inside the shared component, then find every sibling that patched the
same problem locally, remove those patches and list the files. Read a
component's documentation and use its current API before relying on it; check
that a library is maintained before installing it, and port the pattern when it
isn't.

When the user says remove, delete the code with its styles, variables, routes
and menu entries rather than deferring it.

## Build or refine

For a focused refinement, keep the settled direction and change only what the
task requires.

Implement the main experience using real content and the relevant craft
references. Default to local HTML for standalone web prototypes. Use a native
preview when the decision depends on platform controls, gestures, or text
scaling. Use the existing stack and design system for product changes. Include
the controls and states needed to complete the requested task.

Inspect the rendered result when you can and exercise its main path and the
states it reaches. For original work, look for material problems in hierarchy,
task flow, and states before delivering; a separate audit report is not required. For an accepted visual target, use [design
QA](design-qa.md). For a focused refinement, inspect the exact changed workflow
at a representative viewport and exercise the affected interaction.

Before treating an exploratory prototype as production-ready, carry the chosen
variant and its settings into the real component. Exercise its actual content,
interaction, supported devices, and performance as relevant to
the change; report missing evidence instead of treating the prototype as proof.
Use the target platform's checks rather than assuming web-specific mechanics.

Correct material issues within the requested scope, then inspect the affected
result again. When you can start a fresh reviewer, use
[finish review](../../../references/finish-review.md) for the final independent
comparison and verified corrections. Keep the handoff proportional to the change;
do not reopen settled design decisions or audit unrelated screens. Report open
findings and evidence gaps at any stop; stopping does not establish readiness.

Build-with-what-exists rules adapted from Raphael Salaja's public restraint and reuse (raphaelsalaja/skills, commit 31031e9). See [license](../../../references/raphael-salaja-LICENSE.txt).
