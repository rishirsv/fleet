---
name: design
description: "Design, build, refine, or recreate web and native product UI. Use for new screens, redesigns, visual directions, product ideas, UX copy, motion terms, or handoff specs."
---

# Design

Design with a point of view. Make deliberate choices about palette, typography,
composition, and interaction that belong to this brief and would not carry over
unchanged to a similar one. Take aesthetic risks when they express the subject
or improve the experience. When refining an established product, work within
its identity. When creating or redesigning one, commit to a single visual
direction and carry it through every screen and state.

To audit an existing interface, review a UI change, or stress test a component,
load `$design-review`.

Read the [context contract](../../references/context-contract.md) and relevant
product sources before choosing a direction. Saved context is optional.

## Order of work

For anything bigger than a one-line fix:

1. **Before building:** [direction](references/direction.md) when visual
   choices are open, [recreate a reference](references/recreate.md) if
   references matter; offer [ideation](references/ideation.md) when the
   direction is open.
2. **While building:** the [craft floor](../../references/craft-floor.md) and
   [craft references](#choose-the-craft), `$prototype` for faux UI and
   marketing visuals, and [Motion](references/motion.md) for new motion.
3. **Before saying done:** [prove the result](#prove-the-result) in the running
   app, including its layout checks for layout changes, `$design-review`'s
   [component stress](../design-review/references/component-stress.md) for
   data-heavy screens, and [finish review](../../references/finish-review.md)
   on the changed UI. Offer `$design-review`'s accessibility or
   [motion review](../design-review/references/motion-review.md) when the
   change touches keyboard access, focus or heavy motion.
4. **After:** offer to save a correction with `$design-context` if it came up
   twice.

Keep it proportional. A copy tweak needs the
[UX-copy guide](../../references/ux-copy.md), not the whole pipeline.

Before editing UI, read the [craft floor](../../references/craft-floor.md).
Its aesthetic bans are required checks, not optional suggestions; the generic
defaults in [direction](references/direction.md) do not waive them. Apply them
to the requested change, preserving explicit user choices and unrelated
existing UI.

## Choose the workflow

Read only the references the current decision needs.

| Outcome | Read |
|---|---|
| Build a new interface or substantially redesign one | [Direction](references/direction.md), then [Plan and build](references/build.md) |
| Challenge an open product idea before building | [Test an open product idea](references/build.md#test-an-open-product-idea) |
| Build or refine a conversion-focused landing page | `$landing-page-design` for offer, audience, structure, and copy; retain this skill's shared craft guidance |
| Create a scripted product walkthrough or staged UI illustration | `$prototype` for the scene; retain this skill’s product and craft guidance |
| Animate an accepted static design or product visual, or export a showcase | `$design-to-motion` for fidelity, choreography, and capture |
| Refine a settled interface | [Build or refine](references/build.md#build-or-refine); reuse established context |
| Explore directions or compare variants | [Direction](references/direction.md) and [Ideation](references/ideation.md) |
| Name a motion effect or explain a motion term | [Animation vocabulary](references/animation-vocabulary.md) |
| Recreate an accepted image, mockup, or live page | [Recreate a reference](references/recreate.md) |
| Check or correct a build against an accepted design | [Design QA](references/design-qa.md) |

For UX copy, read the full [UX-copy guide](../../references/ux-copy.md)
and [workflow guidance](../../references/workflows-guide.md). For an engineering
handoff specification, read the full [handoff guide](../../references/handoff.md).
Measure from available sources, specify relevant states and accessible behavior,
and label inferred values. Creating a handoff does not authorize publishing it.

## Choose the craft

| Decision | Guidance |
|---|---|
| Hierarchy, density, repeated rows, responsive layout | [Layout](references/layout.md) |
| Fonts, text roles, wrapping, truncation | [Typography](references/typography.md) |
| Palette, contrast, themes, gradients | [Color](references/color.md) |
| Controls, forms, feedback, search, labels | [Interaction](references/interaction.md) |
| Timing, choreography, gesture motion | [Motion](references/motion.md) |
| Icon weight, states, size, direction | [Icons](references/icons.md) |
| Native Apple controls, app icons, lazy SwiftUI lists | [Platforms](references/platforms.md) |

## Prove the result

Follow [visual proof](../../references/evidence.md) for any claim about how
the interface renders or behaves. Inspect the states the change affects:

- Layout: narrow and wide containers, widths just above and below each
  breakpoint, real and extreme content, text scaling, and sticky regions over
  focused content. Check that the hierarchy survives as well as the fit.
- Typography: long strings, localized expansion, fallback fonts, supported
  text sizes, and reflow when fonts load.
- Interaction: the main path, errors, retries, cancellation, dismissal, and
  back navigation.
- Motion: entry, exit, rapid repetition, reversal, interruption, and reduced
  motion. A static capture proves the endpoint only; use a recording or
  intermediate frames when continuity is in question.

Before delivering implemented UI, run [finish review](../../references/finish-review.md):
a fresh reviewer judges the changed scope and verifies material corrections.
Use it as the final comparison in design QA, not an additional audit cycle.
Planning, unselected concept variants, prose-only deliverables, and review-only
requests do not trigger this handoff.

## Explain the result

Write design explanations with [Writing style](../../references/reporting.md).
Lead with the visible result, design decision, or blocker; name elements and
quote copy. Interface copy follows
[Interaction](references/interaction.md#labels-and-messages).
