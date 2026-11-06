# Icons

Choose icon weight, states, size, and direction to fit the interface. Platform
conventions and supplied brand artwork govern meaning. Apply stroke and fill
rules only to icon families that offer those variants.

## Contents

- [Match icon stroke to text weight](#match-icon-stroke-to-text-weight)
- [One glyph, tinted per state](#one-glyph-tinted-per-state)
- [Outline default, fill active](#outline-default-fill-active)
- [Design at render size](#design-at-render-size)
- [Icons in RTL](#icons-in-rtl)

## Match icon stroke to text weight

A very thin icon beside semibold text can appear incomplete. A heavy icon beside
regular text can draw too much attention.

| Adjacent text | Icon stroke width (24pt grid) |
| --- | --- |
| Regular (400), 14–16pt | `1.5pt` |
| Medium or semibold (500–600) | `2pt` |
| Bold (700), or emphasized standalone | `2.5pt` |

Keep icon weights consistent within each interface region, and use one library
per toolbar. Symbol sets that follow the adjacent text's weight and size, such
as SF Symbols, handle this for you. Where the library has no stroke variants,
keep its native stroke and use size or color for emphasis. Size inline icons
relative to the text, typically 1–1.25× its size, so the pair scales together.

## One glyph, tinted per state

When states differ only in color, use one monochrome glyph tinted by the
control's state, not a separate asset per state. Replace hardcoded fills inside
a monochrome glyph with the inherited tint; preserve intentional multicolor
artwork. On the web that is an SVG with `currentColor` instead of
`fill="#666"`; on Apple platforms, a template image or symbol.

## Outline default, fill active

Where an icon set offers outline and filled variants, use them as a state pair:

| Variant | Use for |
| --- | --- |
| Outline | Default state: toolbars, list rows, inline with text |
| Fill | Selected or active state: the active tab, a toggled bookmark, a liked heart |

Filled icons everywhere leave the active state with no signal. Animate a
variant change only when motion adds information; otherwise swap statically.

## Design at render size

Check each icon at the smallest size it renders, often `16pt`, where thin
interior lines and tight counters blur. Use simplified glyphs in small contexts
and the set's native grid sizes (`16`, `20`, `24`); fractional scaling from
another grid blurs the glyph.

## Icons in RTL

In a right-to-left interface, flip icons whose meaning follows reading direction
and leave the rest alone:

| Flip | Keep |
| --- | --- |
| Back and forward arrows, navigation chevrons | Logos and brand marks |
| Text-block glyphs (alignment, lists, indent) | Checkmarks |
| Speaker and volume waves | Physical objects: clocks, cups, pencils |
| "Send" style directional glyphs | Media playback (play and rewind stay LTR by convention) |

Use the platform's automatic mirroring where it exists (SF Symbols mirror their
directional glyphs) and mark custom directional assets to mirror. On the web,
flip them under `[dir="rtl"]` with `scale: -1 1`.

Analyze composite icons part by part; a badge or slash overlay may keep its
position when the base glyph flips. Give icon-only buttons accessible names.

Adapted from Jakub Krehel's public better-ui (jakubkrehel/skills, commit 60bf140).
See [license](../../../references/jakub-krehel-LICENSE.txt).
