# Design

From intent to interface. A standalone skills plugin for product design on
compatible agent hosts: build and refine web/native interfaces, review real workflows,
organize product context and design systems, and synthesize user research.

| Skill | Try it |
|---|---|
| design | `$design` refine this checkout; recreate this screenshot; write UX copy; prepare a developer handoff |
| design-review | `$design-review` audit this flow, accessibility or copy; report findings without edits |
| design-context | `$design-context` save our sources; audit, document or extend the component system |
| design-research | `$design-research` plan a study, synthesize these interviews, or investigate current UX pain |

Use existing product sources and available tools. No mandatory brief-approval or
image-generation gate for a sufficiently specified task. Visible claims need
rendered evidence. Corrections continue toward the requested outcome, bounded
by user limits and concrete blockers.

The seven complete [domain workflows](references/workflows-guide.md) are loaded for
their respective jobs. Their mapping and capability boundaries live in
[Workflow guidance](references/workflows-guide.md). The bundled design-system
runtime and full format documentation live in `design-system/`,
including local file preparation and compatible-host publishing instructions.

The package has no required app or MCP connections. Browser, native-preview,
Figma and research integrations are optional capabilities of the active host.
No Dots install is required. HTML documents and technical experiments remain
in Dots. Personal/product state stays outside this plugin.

Local package version: 0.1.1. Marketplace appearance is prepared; this does not
mean the plugin is publicly listed or approved. Cloud publication, retirement of old Dots UI
skills and fresh desktop verification are separate release steps.
