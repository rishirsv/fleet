# Icons

Choose icon weight, states, size, and direction to fit the interface. Platform
conventions and supplied brand artwork govern meaning. Apply stroke and fill
rules only to icon families that offer those variants.

## Contents

- [Match icon stroke to text weight](#match-icon-stroke-to-text-weight)
- [One SVG, recolored per state](#one-svg-recolored-per-state)
- [Outline default, fill active](#outline-default-fill-active)
- [Design at render size](#design-at-render-size)
- [Icons in RTL](#icons-in-rtl)

## Match icon stroke to text weight

A very thin icon beside semibold text can appear incomplete. A heavy icon beside
regular text can draw too much attention.

| Adjacent text | Icon stroke width (24px grid) |
| --- | --- |
| Regular (400), 14–16px | `1.5px` |
| Medium or semibold (500–600) | `2px` |
| Bold (700), or emphasized standalone | `2.5px` |

Keep icon weights consistent within each interface region, and use one library
per toolbar. Where the library has no stroke variants, keep its native stroke
and use size or color for emphasis. Size inline icons relative to the text's cap
height, typically `1em`–`1.25em`, so the pair scales together.

## One SVG, recolored per state

When states differ only in color, draw one SVG with `currentColor` and let the
control's state set the color. Replace hardcoded fills inside a monochrome
glyph, such as `fill="#666"`, with `currentColor`; preserve intentional
multicolor artwork.

## Outline default, fill active

Where an icon set offers outline and filled variants, use them as a state pair:

| Variant | Use for |
| --- | --- |
| Outline | Default state: toolbars, list rows, inline with text |
| Fill | Selected or active state: the active tab, a toggled bookmark, a liked heart |

Filled icons everywhere leave the active state with no signal. Animate a
variant change only when motion adds information; otherwise swap statically.

## Design at render size

Check each icon at the smallest size it renders, often `16px`, where thin
interior lines and tight counters blur. Use simplified glyphs in small contexts
and the set's native grid sizes (`16`, `20`, `24`); fractional scaling from
another grid blurs the glyph.

## Icons in RTL

Under `dir="rtl"`, flip icons whose meaning follows reading direction and leave
the rest alone:

| Flip | Keep |
| --- | --- |
| Back and forward arrows, navigation chevrons | Logos and brand marks |
| Text-block glyphs (alignment, lists, indent) | Checkmarks |
| Speaker and volume waves | Physical objects: clocks, cups, pencils |
| "Send" style directional glyphs | Media playback (play and rewind stay LTR by convention) |

```css
[dir="rtl"] .icon-directional {
  scale: -1 1;
}
```

Analyze composite icons part by part; a badge or slash overlay may keep its
position when the base glyph flips. Give icon-only buttons accessible names.
