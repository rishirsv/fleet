---
name: design-review
description: "Reviews interfaces, flows, mockups, Figma frames, screenshots, or design descriptions for usability, visual quality, accessibility and copy. Use for design critique, UI change review, UX-copy review, or component stress testing."
---

# Design review

Judge the target at its actual stage: an implemented interface, UI change,
component, mockup, Figma frame, screenshot or design description. Report findings
tied to that evidence. Description-only critique can assess proposed hierarchy,
flow and copy, but labels visual conclusions as hypotheses rather than rendered
observations. Do not require a running implementation to critique an early idea. An audit reports findings; when
the user also asks for fixes, load `$design`, correct within the requested
scope, and inspect the corrected route, viewport, and interaction again.

Read the [context contract](../../references/context-contract.md) for product
sources. Do not edit in a review-only request.

## Choose the review

| Request | Read |
|---|---|
| Judge visual quality, UX, accessibility, or readiness | [Design audit](references/design-audit.md) |
| Find UI regressions in a diff, branch, commit, or pull request | [Change audit](references/change-audit.md), with the design audit's criteria and result |
| Stress test or harden a component | [Component stress](references/component-stress.md) |

Checking a build against an accepted design belongs to `$design`'s design QA.
For the craft guidance behind a finding or its fix (layout, typography, color,
interaction, motion, icons), load `$design` and read the matching reference.

For critique, read the full [critique guide](../../references/critique.md).
For accessibility, read the full [accessibility guide](../../references/accessibility.md).
For copy review, read the full [UX-copy guide](../../references/ux-copy.md).
Apply the [workflow guidance](../../references/workflows-guide.md) to these workflows.
Assess only what the available evidence supports; do not claim WCAG conformance
from visual inspection alone. A flow audit records numbered steps with evidence,
friction and impact, not just a gallery of screenshots.

## Gather evidence

Follow [visual proof](../../references/evidence.md). Source inspection can
establish implementation defects. Claims about appearance need the rendered
interface; claims about behavior need the exercised interaction. An implementation-readiness or
polish claim needs rendered evidence from the affected workflow at a
representative viewport, including the changed interaction or state.

Record which routes, states, themes, and devices you inspected and which you
could not. Report a coverage gap instead of generalizing from a sample, and keep
independently useful findings when some evidence is missing.

## Report

Write findings with [Writing style](../../references/reporting.md).

For a selected workflow, use its Output structure by default,
marking unsupported fields unknown. Otherwise lead with the overall assessment
and highest-impact changes. Each finding
gives its location or journey step, evidence, user impact, proposed correction,
and the verification it needs. Prioritize by consequence; structural and
behavioral problems often matter more than cosmetic ones. Quote copy and name
elements: "Four equally prominent actions obscure where to start" gives a
correction a target, where "improve hierarchy" does not. Distinguish observed
effects from hypotheses about users, and name strengths a correction could
damage. Include relevant captures and summarize uncovered scope.
