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

Implemented UI ends with a fresh, scoped finish reviewer and evidence-backed
verification of material corrections. Shared aesthetic bans guide both building
and review. The handoff reuses captures and task notes; no extra engine, hook,
config, or product document is required. Hosts without delegation disclose a
local self-check instead of claiming independent review.

The seven complete [domain workflows](references/workflows-guide.md) are loaded for
their respective jobs. Their mapping and capability boundaries live in
[Workflow guidance](references/workflows-guide.md). The bundled design-system
runtime and full format documentation live in `design-system/`,
including local file preparation and compatible-host publishing instructions.

The package has no required app or MCP connections. Browser, native-preview,
Figma and research integrations are optional capabilities of the active host.
No pstack install is required. Optional HTML and verification authoring packages
live in Fleet’s `wip/` directory. Personal/product state stays outside this plugin.

Local package version: 0.1.3. Marketplace appearance is prepared; this does not
mean the plugin is publicly listed or approved. Cloud publication, retirement of old Dots UI
skills and fresh desktop verification are separate release steps.
