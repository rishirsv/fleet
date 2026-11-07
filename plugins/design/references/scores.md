# Design scores

Design audits and change audits rate six areas out of 10. A score says how good
the design is in that area. It is separate from [severity](severity.md), which
rates individual problems: a screen with one `HIGH` finding can still score 8
for typography, and a screen with no findings can score 6 for being correct but
undistinguished.

## How to score

Judge each area against its anchors and the reference that owns its rules. Pick
the nearest anchor, move up or down by one when the evidence sits between two,
and give the reason in one line that names what you saw. Use whole numbers.

Rate only what you inspected. An area you could not see or that the work does
not include, such as motion on a static screen, is `Not rated`, with the
reason. Do not average the six into an overall score.

In a change audit, score the affected surfaces as they stand after the change,
and mark an area the change made worse.

## Anchors

**Layout and hierarchy** ([Layout](../skills/design/references/layout.md), [design skill](../skills/design/SKILL.md))

- 10: one clear starting point, grouping carried by space, shared edges, and the structure holds at every size in the sweep.
- 7: clear structure with a few uneven gaps, a competing element, or one size where it strains.
- 4: no obvious starting point, grouping that misleads, or a layout that breaks at a supported size.
- 1: content or controls unreachable or unreadable.

**Typography** ([Typography](../skills/design/references/typography.md))

- 10: a small, consistent scale; hierarchy reads at a glance; comfortable measure and line height; the right weights, digits and punctuation; holds up with long strings and larger text sizes.
- 7: a sound scale with stray sizes or weights, an uncapped measure, or a few wrapping problems.
- 4: no consistent scale, hierarchy that misleads, or text that is hard to read.
- 1: text that cannot be read at a supported size.

**Color** ([Color](../skills/design/references/color.md))

- 10: ramps behind role tokens, one meaning per color, one filled primary action, and both themes designed rather than inverted.
- 7: a coherent palette with a few literals, borrowed tokens, or one theme less finished.
- 4: colors with competing meanings, several filled actions fighting, or a theme that looks broken.
- 1: color that misleads, such as danger on a safe action throughout.

**Interaction and states** ([Interaction](../skills/design/references/interaction.md))

- 10: every reachable state is designed (hover, pressed, focus, disabled, loading, empty, error), feedback is immediate, and every error says how to recover.
- 7: the main path is solid, with a missing or generic secondary state.
- 4: missing loading, empty or error states, or controls that don't read as controls.
- 1: the core task cannot be completed.

**Motion** ([Motion](../skills/design/references/motion.md))

- 10: every animation passes the frequency and purpose gate, with the right curves and durations, interruptible, with a reduced-motion treatment; or the design is deliberately still where it should be.
- 7: purposeful motion with a slow duration, a weak curve, or one animation that should not exist.
- 4: decoration on frequent actions, sluggish timing, or motion that blocks input.
- 1: motion that hides state or makes the interface hard to use.

**Copy** ([UX copy](ux-copy.md))

- 10: plain words, one vocabulary throughout, verb-first labels, and errors and empty states that say what to do next.
- 7: clear copy with a few inconsistent terms, vague labels, or casing slips.
- 4: jargon, mismatched terms for the same thing, or errors that don't help.
- 1: copy that misleads about what an action does.

## Format

Open the report with the table, before the findings:

| Area | Score | Why |
| --- | --- | --- |
| Layout and hierarchy | 7 | Clear start, but the filter bar competes with the page title at 375 |
| Motion | Not rated | Static screen |
