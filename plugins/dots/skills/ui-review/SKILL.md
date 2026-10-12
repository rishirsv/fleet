---
name: ui-review
description: "Audits an existing interface or UI change for visual quality, usability, accessibility, and regressions, and stress tests components with edge-case content. Use when asked to review, audit, or stress test a UI."
---

# UI review

Judge an existing interface, a UI change, or a component from rendered evidence,
and report findings tied to what you observed. An audit reports findings; when
the user also asks for fixes, load `$ui-design`, correct within the requested
scope, and inspect the corrected route, viewport, and interaction again.

## Choose the review

| Request | Read |
|---|---|
| Judge visual quality, UX, accessibility, or readiness | [Design audit](references/design-audit.md) |
| Find UI regressions in a diff, branch, commit, or pull request | [Change audit](references/change-audit.md), with the design audit's criteria and result |
| Stress test or harden a component | [Component stress](references/component-stress.md) |

Checking a build against an accepted design belongs to `$ui-design`'s design QA.
For the craft guidance behind a finding or its fix (layout, typography, color,
interaction, motion, icons), load `$ui-design` and read the matching reference.

## Gather evidence

Follow [visual proof](../../references/visual-proof.md). Source inspection can
establish implementation defects. Claims about appearance need the rendered
interface; claims about behavior need the exercised interaction. A readiness or
polish claim needs rendered evidence from the affected workflow at a
representative viewport, including the changed interaction or state.

Record which routes, states, themes, and devices you inspected and which you
could not. Report a coverage gap instead of generalizing from a sample, and keep
independently useful findings when some evidence is missing.

## Report

Lead with the overall assessment and the highest-impact changes. Each finding
gives its location or journey step, evidence, user impact, proposed correction,
and the verification it needs. Prioritize by consequence; structural and
behavioral problems often matter more than cosmetic ones. Quote copy and name
elements: "Four equally prominent actions obscure where to start" gives a
correction a target, where "improve hierarchy" does not. Distinguish observed
effects from hypotheses about users, and name strengths a correction could
damage. Include relevant captures and summarize uncovered scope.
