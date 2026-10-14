# Surface recipes

Web treatments for radii, alignment, depth, image edges, gradients, and texture.
Use them when they fit the accepted visual system; on native platforms, use
system components and materials.

## Contents

- [Concentric border radius](#concentric-border-radius)
- [Optical alignment](#optical-alignment)
- [Shadows for depth](#shadows-for-depth)
- [Image outlines](#image-outlines)
- [Gradient interpolation](#gradient-interpolation)
- [Grain](#grain)

## Concentric border radius

For close nested surfaces with a uniform inset and circular corners, derive the
inner radius from the distance between their outer edges:

```
innerRadius = max(0, outerRadius - inset)
inset = parentBorderWidth + parentPadding
```

Include any additional gap in the inset. With no parent border or gap, this is
`outerRadius = innerRadius + padding` until the inner radius reaches zero.
Around `24px` of padding the layers may read as independent surfaces; judge
that relationship by eye.

```css
/* Good: concentric radii */
.card {
  border-radius: 20px; /* 12 + 8 */
  padding: 8px;
}
.card-inner {
  border-radius: 12px;
}

/* Bad: same radius on both */
.card { border-radius: 12px; padding: 8px; }
.card-inner { border-radius: 12px; }
```

The corner gap and the straight-edge gap should form a continuous band. If the
inset exceeds the outer radius, the inner corner becomes square. Asymmetric
insets and other corner shapes need individual judgment. Keep an established
component token where the layers are independent or the padding is deliberately
asymmetric.

## Optical alignment

If a geometrically centered glyph looks off-center, adjust it to balance its
visible shape. Squint, or temporarily blur the glyph in the inspector, to see
where its weight sits; compare original and adjusted at display size, then
remove the diagnostic blur. Move the glyph only, keeping the control's hit area
and neighboring alignment fixed.

For a button with text and icon, symmetric padding can look unbalanced. Start
with icon-side padding 2px less than text-side padding:

```css
.button-with-icon {
  padding-inline-start: 16px;
  padding-inline-end: 14px; /* trailing icon side = text side - 2px */
}
```

A right-pointing play triangle's geometric center sits left of its visual
center; a small rightward shift is a starting point. Check the path and viewBox
first, because the icon may already include the correction, and set direction
and amount per glyph.

```css
/* Candidate: compare with the unshifted glyph */
.play-button svg {
  transform: translateX(2px);
}
```

For other asymmetric icons (stars, arrows, carets), fix the SVG viewBox or path
so the component needs no extra spacing. As a fallback, nudge the wrapper:
`<span className="translate-x-px"><StarIcon /></span>`.

## Shadows for depth

When buttons, cards, and containers use a border to show elevation, replace it
with a subtle `box-shadow`. Shadows use transparency, so they adapt to images
and varied backgrounds where a fixed border color fails. Apply this only to
borders that represent elevation; dividers (`border-b`, `border-t`, side
borders) and other separators stay borders.

In light mode, use three layers: a 1px ring, subtle lift, and ambient depth.

```css
:root {
  --shadow-border:
    0px 0px 0px 1px oklch(0 0 0 / 0.06),
    0px 1px 2px -1px oklch(0 0 0 / 0.06),
    0px 2px 4px 0px oklch(0 0 0 / 0.04);
  --shadow-border-hover:
    0px 0px 0px 1px oklch(0 0 0 / 0.08),
    0px 1px 2px -1px oklch(0 0 0 / 0.08),
    0px 2px 4px 0px oklch(0 0 0 / 0.06);
}
```

In dark mode, layered depth shadows disappear, so use one white ring under the
project's dark-mode selector:

```css
--shadow-border: 0 0 0 1px oklch(1 0 0 / 0.08);
--shadow-border-hover: 0 0 0 1px oklch(1 0 0 / 0.13);
```

For a card whose lift benefits from a transition, transition `box-shadow`
between the two tokens over about 150ms.

| Use shadows | Use borders |
| --- | --- |
| Cards, containers with depth | Dividers between list items |
| Buttons with bordered styles | Table cell boundaries |
| Elevated elements (dropdowns, modals) | Form input outlines (for accessibility) |
| Elements on varied backgrounds | Hairline separators in dense UI |
| Hover states for lift | Focus indicators that must survive forced colors |

Box shadows can disappear in forced colors; keep an outline or border fallback
where a control boundary must stay visible.

## Image outlines

Add a `1px` low-opacity outline to content imagery that needs separation,
especially where other elements use borders or shadows. Leave decorative images
and logos alone unless their treatment calls for it.

Use pure black at 10% in light mode, `oklch(0 0 0 / 0.1)`, and pure white at 10%
in dark mode, `oklch(1 0 0 / 0.1)`. A pure neutral keeps the edge from picking
up a tint; palette near-blacks such as slate-900 or `#111827`, and accent or
ink colors, combine with the surface and discolor the image edge.

```css
img {
  outline: 1px solid oklch(0 0 0 / 0.1);
  outline-offset: -1px; /* draw the ring just inside the image edge */
}

/* dark mode */
img {
  outline-color: oklch(1 0 0 / 0.1);
}
```

`outline` adds no width or height, and the negative offset follows the corner
radius. Compare pale, dark, and mixed-edge images with the outline on and off in
each theme; the edge should clarify the image's shape without reading as a
frame.

## Gradient interpolation

Choose the interpolation space for the midpoint you want and keep a plain
fallback declaration: sRGB and `in oklab` pass near gray between opposite hues,
while `in oklch shorter hue` keeps chroma by traveling around the hue wheel.
Large, low-contrast gradients band on 8-bit displays; increase the contrast
between stops, reduce the area, or add grain.

## Grain

Use grain when visible gradient bands need softening or texture creates the
chosen material. Compare with the untreated surface first and keep the plain
surface when grain only adds visual activity.

A live SVG turbulence filter suits small surfaces and tuning. Large filtered
areas, especially during scrolling or animation, need measurement on the target
device. For large static treatments, use a small repeating tile, and keep the
noise parameters static unless the brief calls for motion. Save this as a
project asset; `stitchTiles` makes opposite edges meet:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128">
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.7"
      numOctaves="2" stitchTiles="stitch" />
    <feColorMatrix type="saturate" values="0" />
  </filter>
  <rect width="100%" height="100%" filter="url(#grain)" />
</svg>
```

Export a raster tile instead when profiling shows the SVG still costs too much;
browsers do not all rasterize an SVG tile once.

```css
.textured-surface {
  position: relative;
  isolation: isolate;
  background: var(--surface-background);
}

.textured-surface::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background: url("./grain.svg") repeat;
  background-size: 128px 128px;
  opacity: 0.06;
  mix-blend-mode: soft-light;
  pointer-events: none;
}
```

Isolation keeps blending local. The negative layer sits above the surface's
background and below its content, so grain neither covers text nor intercepts
input. Contain the texture this way instead of clipping the component, which
can cut off focus rings and popovers. Toggle the layer in the real surface and
theme: check that bands soften, tile edges stay invisible, and text keeps its
contrast. Tune scale and opacity in context, and compare scrolling and repaint
cost with the layer disabled.

References: [SVG
turbulence](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feTurbulence),
[blend
isolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation).
