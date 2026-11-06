---
name: landing-page-design
description: "Plan, write, and build conversion landing pages and campaigns. Use for offer, audience, page structure, conversion copy, proof, or SEO, not app UI."
---

# Landing Page Design

A landing page is not a homepage. A homepage serves multiple intents. A landing page wins one intent:

**one offer → one audience → one primary action.**

This skill has two halves. **Part A** ([strategy and structure](references/strategy.md)) decides what the page says and how it is structured. **Part B** applies Design’s shared craft guidance to that strategy.

## Scope

Use for conversion-focused landing pages and marketing campaigns. Use `$design`
for general interface work and `$design-review` for an audit without edits.
For an existing landing page, preserve its established identity and change only
what the requested outcome needs.

Read the [context contract](../../references/context-contract.md), relevant
product sources, and the [craft floor](../../references/craft-floor.md) before
choosing a direction. Explicit user choices and an accepted reference or
incumbent design system take precedence as described in the craft floor.

Use the [page strategy](references/strategy.md) to decide the content. Use
Design’s shared craft references for visual choices; this skill does not impose a separate font,
color, spacing, or motion system.

---

# PART B — Visual system

Build within the product’s identity. For a new page, choose a distinctive
visual direction from its subject, using Design’s
[direction](../design/references/direction.md), and carry it through
consistently. Use a small set of role-based values rather than importing a
fixed aesthetic.

| Decision | Read |
|---|---|
| Page composition, spacing, grouping, responsive layout | [Layout](../design/references/layout.md) |
| Font families, weights, sizes, line height, wrapping | [Typography](../design/references/typography.md) |
| Palette, surfaces, contrast, gradients | [Color](../design/references/color.md) |
| Buttons, navigation, forms, feedback, labels | [Interaction](../design/references/interaction.md) |
| Icon family, weight, size, states | [Icons](../design/references/icons.md) |
| Timing, choreography, interruption, reduced motion | [Motion](../design/references/motion.md) |

Do not require gradient headings, glass navigation, a fixed hero width, a
font whitelist, Tailwind scale snapping, or a tagline reveal. Keep content
visible before motion; avoid identical fade-up entrances on every section.
Use `$design-to-motion` when the requested outcome includes an animated product
visual or showcase. Routine navigation and control feedback follow the shared
motion guidance above.

## Content and states

Write real draft copy in the product’s voice. Use supplied proof for commercial
claims; label synthetic demonstration content honestly. Keep headings and
buttons in sentence case, and make system messages calm and specific.

Implement relevant hover, active, focus, loading, empty, and error states using
the product’s interaction patterns. Keep visible keyboard focus, accessible
contrast, reduced motion, semantic HTML, and meaningful image alternatives.
No dead links or placeholder actions presented as functional.

## Finish and verify

Check the affected layout at narrow and wide widths, real and extreme copy,
keyboard navigation, forms, and reduced motion. Include metadata, favicon,
social previews, legal links, and error routes where the page’s delivery scope
requires them; use existing destinations and content rather than inventing
legal terms or expanding a page edit into unrelated site work.

Follow [visual proof](../../references/evidence.md) for rendered claims and
[finish review](../../references/finish-review.md) before delivering implemented
UI. Explain the result with [reporting guidance](../../references/reporting.md).

---

# Output format

Before building a new page, briefly state the proposed outline, hero copy,
primary action, available proof, and visual direction. Include benefit copy,
process steps, FAQ, and an indexing recommendation when relevant to the offer.
Do not require a separate approval gate when the brief is sufficiently clear.

Then build section by section per [A6](references/strategy.md#a6-build-order). Report the visible result, verification,
and any unresolved content or behavior.

---

# Quick checklist

- [ ] One offer, one audience, one primary action
- [ ] Copy matches the traffic source and uses supported claims
- [ ] Proof and available risk-reducing terms sit near the relevant decision
- [ ] Sections suit the offer rather than a mandatory page template
- [ ] Typography, colors, spacing, icons, and motion follow the product’s system
- [ ] Craft floor, accessible states, and responsive layout checked
- [ ] Relevant links, forms, metadata, and delivery requirements work
- [ ] Rendered evidence and finish review completed for implemented UI
