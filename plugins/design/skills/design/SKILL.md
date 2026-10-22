---
name: design
description: "Designs, builds, refines, and recreates web or native product interfaces. Use for UI design, visual exploration, UX copy or microcopy, button and error-message wording, and developer handoff specifications from a design."
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

## Ground the design

Identify the subject, audience, and primary job before choosing a style. When
the brief leaves them open, propose a concrete interpretation and continue; ask
only when different answers would materially change the design. Draw
distinctive choices from the subject's materials, vocabulary, imagery, and
activities instead of demographic clichés: a children's toy and an analyst's
dashboard need different density, hierarchy, and expression. When a page opens
with a hero, lead with the most characteristic thing in the subject's world,
such as a headline, an image, a live demo, or an interaction. Build with real
content, or plausible content for the actual task; generic copy makes a design
read as a template as surely as generic styling does.

## Avoid generic defaults

Generated interfaces converge on a few looks whatever the subject:

- A warm cream background, high-contrast serif display, and terracotta accent.
- A near-black background with one acid-green or vermilion accent.
- A broadsheet of hairline rules, square corners, and dense columns.
- The SaaS card kit: identical rounded cards with one radius and one soft gray
  shadow, decorative gradient washes, and a hero of one big number, a small
  label, and supporting stats.
- Template chrome: a tracked uppercase eyebrow over each heading, one accented
  word per headline, `01 / 02 / 03` markers on content that is not a sequence,
  metadata joined with middle dots, arrows appended to link text, a fade-up
  entrance on every section, and a hover lift on every card.

Any of these can suit a brief, but none is a choice when it would appear for
any subject. Where the brief specifies a look, follow it exactly, even when it
asks for one of these. Where the brief leaves a choice open, spend that freedom
on something drawn from the subject. Use borders, numbering, labels, and
dividers only when they encode something about the content. Start a section
with its heading, put category or context in the body or footer, and keep
functional navigation such as breadcrumbs separate from the heading.

Before editing UI, read the [craft floor](../../references/craft-floor.md).
Its aesthetic bans are required checks, not optional suggestions; this list of
generic defaults does not waive them. Apply them to the requested change,
preserving explicit user choices and unrelated existing UI.

## Hierarchy and restraint

Spend boldness in one place: let one element carry the memorable idea, keep the
rest quiet, and cut decoration that does not serve the brief. Establish
hierarchy before decoration, and reduce competing elements before enlarging the
main one. Use a small, consistent set of type, color, spacing, radius, and depth
values, with exceptions only for a distinct role or a visible problem. Preserve
the meaning and behavior of conventional controls. Meet a baseline of
responsive layout, visible keyboard focus, reduced motion, and readable
contrast without presenting it as a feature.

## Choose the workflow

Read only the references the current decision needs.

| Outcome | Read |
|---|---|
| Build a new interface or substantially redesign one | [Plan and build](references/build.md) |
| Refine a settled interface | [Build or refine](references/build.md#build-or-refine); reuse established context |
| Explore directions or compare variants | [Ideation](references/ideation.md) |
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
