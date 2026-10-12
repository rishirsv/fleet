# Ground and build

## Ground the design

Establish the subject, audience, primary job, and intended outcome. Identify the
platform, scope of change, and any accepted visual target. Start with the brief
and conversation.

If the subject or purpose is missing, propose a concrete interpretation: what we
are designing, who it serves, what they need to accomplish, and why this
proposal fits. State reasonable assumptions and continue when context supports
them. Ask a focused question when different answers would materially change the
design; continue without asking for approval when the brief is clear.

Inspect the repository's design guidance, tokens, components, representative
screens, and supplied references that apply to this task. Identify which choices
are required, which references provide inspiration, and which choices are open
to change. Preserve existing product decisions unless the brief calls for
replacing them; resolve meaningful conflicts before committing to a direction.

Choose design details from the subject's language, materials, imagery,
activities, and emotional context. A toy experience for girls aged 8–11 and a
financial analysis dashboard need different hierarchy, density, expression, and
interaction. Translate audience and task into concrete choices instead of
relying on demographic clichés.

Use content specific to the subject and audience. When real content is
unavailable, use plausible examples that represent the actual task. Summarize
the brief and proposed direction in a short note, including assumptions that
could change the design. Continue the work so the user can correct your
interpretation without having to approve it.

## Build or refine

For new work, describe the proposed composition, type roles, palette, imagery,
and interaction from the brief. For a focused refinement, keep the settled
direction and change only what the task requires.

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
