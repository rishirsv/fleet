# Dots HTML visual style

Token values live in `assets/design-tokens.yaml`; `scripts/generate-theme.mjs`
compiles them into `assets/theme.css`. This file explains how to use them.

## Contents

- [Overview](#overview)
- [Tones](#tones)
- [Colors](#colors)
- [Typography](#typography)
- [Layout](#layout)
- [Surfaces and code](#surfaces-and-code)
- [Components](#components)
- [Page rules](#page-rules)

## Overview

Use a restrained technical style for the default tone. Use one flat page
background: warm white in light mode and near black in dark mode. Use
grotesque type with tight negative tracking. Show hierarchy through font
weight, size, spacing, and ink opacity. Use one desaturated blue for emphasis.
Align numbers, use thin rules, and keep motion brief and limited to one occurrence.

## Tones

The default tone (value `report`) is the cool, technical style described here.
It fits reviews, status, plans, incidents, and other work artifacts. A tone
changes token values only: every component, layout, and rule below still
applies, so a toned page keeps the same structure.

- `personal` suits letters, relationship or coaching reflections, personal
  reviews, and other private material written to one person. It uses warm
  paper and ink colors, serif display headings with lighter tracking, and a
  softer card radius. Its accent remains the only emphasis color, and
  `danger-*` stays semantic.

Set the tone with `tone` on `page()`, `--tone` for the assembler, or `tone` in
a page-set manifest. Tones live under `x-tones` in the token file. Each lists
only the tokens it changes: `colors` and `dark` override the matching base
roles (the alpha ladder is recomputed from the tone's foreground),
`display-font`, `display-tracking`, and `card-radius` set headings and card
shape, and `text-muted-step` raises muted text to a stronger alpha step when
the tone's light palette would otherwise fall below 4.5:1. Add a tone there
when a recurring kind of content needs it; restyling one page with inline
colors breaks theme switching.

## Colors

Take grays from the alpha ladder (`--a4` … `--a70`): `--a12` for subtle
borders, `--a20` for strong rules, and `--text-muted` (or `--a70` for stronger
contrast) for secondary text. Use lower alpha steps only for borders, fills,
and non-text marks.

`accent` is for links, active states, the recommendation and recommended
option, and the one emphasized data point.
`accent-deep` is its high-contrast partner for small emphasized text.
`warning-*` and `danger-*` mark genuine warnings and failures only. Code
surfaces stay dark in both modes (`code-surface`/`code-ink`). The `x-dark`
block redefines the same roles for dark mode.

## Typography

Use the system grotesque stack; no webfonts. Use mono only for code and
aligned figures, and the body font for labels. Digits that line up vertically
set `font-variant-numeric: tabular-nums`.

## Layout

Pages use one of three maximum widths on the same flat background:

- `article` (900px) for explanations with text and figures, status,
  incidents, and plans.
- `wide` (1040px) for comparisons, reviews, file maps, and other pages that
  need evidence side by side.
- `canvas` (1440px) for visual references and atlases. Keep prose inside a
  nested article-width reading column and use the extra width for visuals.

Separate sections with 48px of space and, at most, a hairline rule. The table
of contents is a sticky margin rail beside the reading column at wide
viewports, with a scroll-spy active state; on narrow viewports it collapses to
a native disclosure. Linear processes reflow into a vertical sequence;
branching diagrams and wide tables stay bounded inside their own containers.

The page shell supplies the spacing between its header and the first content
block; do not set structural spacing on the header's last child. For parallel
grids, declare the item count and leave no empty columns.

## Surfaces and code

Hierarchy comes from spacing, type, ink contrast, and hairline rules first.
Objects the reader compares or acts on (stat tiles, option cards,
disclosures, code panels, form choices) sit on the `surface` color with a
hairline border and the soft `shadow-sm`; only the recommended or selected
object steps up to `shadow-md`. Running prose, tables, and timelines stay on
the page background. A component may use a faint semantic tint when meaning
requires it. Keep one surface per exhibit: inside a review point, use flat
disclosures and spacing instead of bordered cards inside bordered cards.

Wrap code and diffs within their panels, including long identifiers, so
readers never scroll sideways. Wrapping must preserve the original text when
copied. Give copy controls a small icon with an accessible name and visible
focus.

`rounded.card` (10px) is for cards and code panels; `rounded.inline` (5px) for
inline code and focus rings; `rounded.pill` for status chips. Keep the radius
uniform within a component. Borders are 1px hairlines from the alpha ladder.

## Components

Components consume the design tokens and add no local palettes or shape
systems. Their finished structure lives in the component registry; this file
defines the visual rules shared across it.

Use semantic HTML and native controls. Preserve native tab order and the shared
focus-visible outline; do not add `tabindex` or rebuild a button, link, input,
select, or textarea from a generic element. Informative images and figures need
an accessible name or equivalent adjacent content. Hide decorative SVGs from
assistive technology and omit raster decoration.

Charts use the `x-chart` roles for structure, marks, labels, values, and the
single emphasized point. Those roles follow light and dark modes and keep
chart emphasis independent from links and callouts.

Use `x-motion` only for a one-time load stagger on header elements (a short
rise with a slight blur that settles within about a second), one-time reveals
for figures entering the viewport (bars grow once, SVG paths draw once),
disclosures opening, the theme cross-fade, and hover, focus, press, and TOC
active states. The shared ease decelerates quickly, so motion feels responsive
without overshoot. Add no ambient
or looping motion. Enable motion only under
`prefers-reduced-motion: no-preference`. With JavaScript off, the page renders
completely and stays static.

## Page rules

- Keep one flat page background edge to edge. Do not place a lighter or
  darker content card inside a differently colored body.
- Mark callouts with a full hairline border and, if needed, a faint tint. Put
  no left-side accent stripe on callouts, quotes, recommendations, or the TOC;
  the active TOC item uses weight and color alone.
- Use chips only for a status value inside a structured component, such as a
  milestone state, a finding's severity, or the recommended option. Inside
  callouts and headers, start with a bold lead word ("**Note.**") instead of
  a label chip.
- Start with the title and follow the heading rules in
  [Dots writing style](../../../references/writing-style.md). Keep document
  metadata in the footer, review IDs in exported feedback, and functional
  breadcrumb navigation below the introduction.
- Use numbered markers, dividers, and labels only for real structure. If the
  content is not a sequence, do not number it.
