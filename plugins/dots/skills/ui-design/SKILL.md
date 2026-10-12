---
name: ui-design
description: "Designs, builds, and refines web or native app interfaces, including recreating an accepted image, mockup, or URL and checking the build against it. Use when making or changing how a product interface looks or behaves."
---

# UI design

Make deliberate choices about palette, typography, composition, and interaction
that fit the brief. Challenge clichés and familiar templates. Take aesthetic
risks when they help express the idea or improve the experience. When refining
an established product, work within its existing identity. When creating or
redesigning a product, choose a consistent visual direction.

Establish visual hierarchy before adding decoration. Reduce the prominence of
competing elements before enlarging or emphasizing the main element. Use a
small, consistent set of type, color, spacing, radius, and depth values. Add
exceptions when an element has a distinct role or a visible problem. Preserve
the meaning and behavior of conventional controls. Start sections with the
heading itself; put category or context labels in the body or footer, and keep
functional navigation separate from headings.

To audit an existing interface, review a UI change, or stress test a component,
load `$ui-review`.

## Choose the workflow

Read only the references the current decision needs. Read a recipe file only
when implementing or checking the treatment it describes; each has a contents
list at the top.

| Outcome | Read |
|---|---|
| Build a new interface or substantially redesign one | [Ground and build](references/build.md) |
| Refine a settled interface | [Build or refine](references/build.md#build-or-refine); reuse established context |
| Explore directions or compare variants | [Ideation](references/ideation.md) |
| Recreate an accepted image, mockup, or live page | [Recreate a reference](references/recreate.md) |
| Check or correct a build against an accepted design | [Design QA](references/design-qa.md) |

Design QA belongs to this skill: it compares a build with its accepted target
and corrects the build. Judging whether a design itself is good belongs to
`$ui-review`.

## Choose the craft

| Decision | Guidance | Code recipes |
|---|---|---|
| Hierarchy, density, repeated rows, responsive layout | [Layout](references/layout.md) | [Logical properties and container queries](references/recipes/text-color-layout.md#direction-aware-layout) |
| Fonts, text roles, wrapping, truncation | [Typography](references/typography.md) | [Web fonts and text CSS](references/recipes/text-color-layout.md#web-fonts) |
| Palette, contrast, themes, gradients | [Color](references/color.md) | [Contrast, tokens, canvas](references/recipes/text-color-layout.md#measure-contrast); [gradients and grain](references/recipes/surfaces.md#gradient-interpolation) |
| Controls, forms, feedback, search, labels | [Interaction](references/interaction.md) | [Accessible interaction](references/recipes/accessibility.md) |
| Timing, choreography, gesture motion | [Motion](references/motion.md) | [Motion recipes](references/recipes/motion.md) |
| Radii, optical alignment, depth, image edges, texture | Treatments below | [Surface recipes](references/recipes/surfaces.md) |
| Icon weight, states, size, direction | [Icons](references/icons.md) | [Icon swap](references/recipes/motion.md#icon-swap) |
| Native Apple controls, app icons, lazy SwiftUI lists, spatial scenes | [Platforms](references/platforms.md) | |

Use surface treatments only when they fit the accepted visual system. Preserve
structural, selection, and focus boundaries, and use system components and
materials on native platforms.

## Prove the result

Follow [visual proof](../../references/visual-proof.md) for any claim about how
the interface renders or behaves. Inspect the states the change affects:

- Layout: narrow and wide containers, widths just above and below each
  breakpoint, real and extreme content, text scaling, and sticky regions over
  focused content. Check that the hierarchy survives as well as the fit.
- Typography: long strings, localized expansion, fallback fonts, supported
  text sizes, and reflow when fonts load.
- Interaction: the main path, errors, retries, cancellation, dismissal, back
  navigation, and both directions of reversible changes.
- Motion: entry, exit, rapid repetition, reversal, interruption, and reduced
  motion. A static capture proves the endpoint only; use a recording or
  intermediate frames when continuity is in question.

## Explain the result

Lead with the visible result, design decision, or blocker. Support judgments
with specific observations. Name the element, quote the copy, or describe which
elements compete for attention. Explain how the observation affects the user's
task and what change would improve it. "Four equally prominent actions obscure
where to start; give the primary task more weight" is more useful than "improve
hierarchy." Distinguish observed behavior from assumptions about users'
feelings. Name strengths a correction could damage, and show relevant previews
or evidence when available.
