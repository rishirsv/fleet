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

```html
<!-- Good: stroke tuned to the label weight -->
<button class="flex items-center gap-2 font-semibold">
  <PlusIcon stroke-width="2" class="size-4" />
  New project
</button>
```

Keep icon weights consistent within each interface region, and use one library
per toolbar. Where the library has no stroke variants, keep its native stroke
and use size or color for emphasis. Size inline icons relative to the text's cap
height, typically `1em`–`1.25em`, so the pair scales together.

## One SVG, recolored per state

When states differ only in color, use one SVG drawn with `currentColor` and let
CSS state drive the color:

```html
<svg fill="none" stroke="currentColor" stroke-width="2">…</svg>
```

```css
.icon-button { color: oklch(0.552 0.016 285.938); }
.icon-button:hover { color: oklch(0.21 0.006 285.885); }
.icon-button[aria-pressed="true"] { color: oklch(0.623 0.188 259.815); }
.icon-button:disabled { opacity: 0.4; }
```

```html
<!-- Tailwind -->
<button class="text-zinc-500 hover:text-zinc-900 aria-pressed:text-blue-600 disabled:opacity-40">
  <BookmarkIcon />
</button>
```

Replace hardcoded fills inside a monochrome glyph, such as `fill="#666"`, with
`currentColor`; preserve intentional multicolor artwork.

## Outline default, fill active

Where an icon set offers outline and filled variants, use them as a state pair:

| Variant | Use for |
| --- | --- |
| Outline | Default state: toolbars, list rows, inline with text |
| Fill | Selected or active state: the active tab, a toggled bookmark, a liked heart |

```tsx
// Good: variant communicates state
<TabIcon variant={isActive ? "solid" : "outline"} />

// Bad: filled icons everywhere, so the active tab has no state signal
<TabIcon variant="solid" />
```

Animate a variant change only when motion adds information; otherwise swap
statically.

## Design at render size

An icon that is clear at 48px can lose detail at 16px: thin interior lines,
tight counters, and fine texture blur or alias.

- Test every icon at the smallest size it will render, often `16px`.
- Use simplified glyphs for small contexts in place of scaled-down detailed
  artwork.
- Use the set's native grid sizes (`16`, `20`, `24`). A 16px icon drawn on a
  24px grid with fractional scaling can blur.
- Prefer SVG for ordinary web interface glyphs. Keep intentional raster artwork
  and native symbol assets in their source formats.

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

```html
<!-- Tailwind -->
<ChevronRightIcon class="icon-directional rtl:-scale-x-100" />
```

Analyze composite icons part by part; a badge or slash overlay may keep its
position when the base glyph flips. Give icon-only buttons accessible names.
