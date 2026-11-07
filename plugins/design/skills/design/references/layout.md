# Layout and responsiveness

Compose around the user's task and information relationships. Preserve
established grids and spacing conventions unless changing them is part of the
brief.

## Establish hierarchy and density

Identify the primary action, reading order, and information needed together.
Group related content through proximity, alignment, and type before adding
containers. Use cards for independently meaningful objects; group other
sections with space and alignment. A card never sits inside another card: put
the heading outside and let one surface hold the content. Match density to use: repeated expert work
may need more simultaneous information than onboarding or a focused decision.

Group with space first, background shapes second, and separator lines last,
only where space alone can't carry the structure. The gap between groups is at
least 2× the gap within one, so `8pt` inside a group means `16pt` or more between
groups. Give every interactive element a background shape, a border, an
underline or a consistent placement zone such as a toolbar; a control styled
like the static text beside it does not read as a control. The most important
content sits near the top and the leading edge; within a row, identifying
content leads and metadata and actions trail, and visual order matches source
order.

Choose a grid that serves the content. Give repeated rows consistent columns for
icons, labels, values, and actions, including rows with missing optional
content. Tune optical alignment after structural alignment. Use spacing tokens
for repeated relationships. Use a few strong alignment axes within each region;
several unrelated left, center, and right edges make scanning harder. Choose
one major and one minor spacing unit for vertical rhythm, and align everything
to those units by default.

Organize the first view around the user's immediate task. Remove labels that
merely restate visible context and state each fact, status, or result in one
region. Show source information, original inputs, and internal rule or revision
details when they help someone verify, compare, or correct the result. Keep
risk, coverage, and approval information visible when it changes the user's
decision or next action.

Judge repeated rows as a collection at the real viewport. Account for every
recurring control, label, divider, and line of copy: a small excess repeated
across the visible list can dominate the screen. When a row has optional
supporting content, put one clearly named disclosure control in the row and
expand the content in place, keeping the closed row free of an extra subrow. A
disclosure still adds a control and a decision, so include it only when the
hidden content is useful in that view.

## Adapt the composition

Decide what reflows, stacks, condenses, moves into disclosure, or remains
scrollable as space changes. Preserve task priority and logical reading order
as the structure changes. Keep controls reachable when browser or system chrome, a
virtual keyboard, safe areas, or sticky regions reduce the available space.

Breakpoints come from the content, not device presets. Keep the expanded
layout until it stops fitting, then collapse; adapt components to their
container rather than the screen, and test the smallest and largest supported
sizes first. Translated strings grow, and short ones grow proportionally more,
so a one-word button label is the riskiest thing on the screen: size text
containers with a maximum width and a minimum height, never a fixed width or
height, let rows wrap, and test with pseudo-localization and one long-string
locale such as German. Never park a critical action where resizing or scrolling
clips it.

Every piece of off-screen or collapsed content needs a visible cue: the
project's established cue, the next item peeking `16`–`32pt` past the scroll
edge, or a disclosure control. Write direction-dependent layout as leading and
trailing, never left and right, so it mirrors; reserve physical sides for
physical geometry such as safe areas.

Without an established density system, start with `12pt` between adjacent
bordered or filled controls and `24pt` between the visible glyphs of borderless
text and icon controls, counting each one's own padding; compact layouts may use
less as long as hit areas never overlap. In content layouts, keep full-width
buttons inside the layout margins, starting near `16pt` on phones.

Scale properties at different rates. Large display type, media, and generous
padding often need to contract faster than body text, controls, and touch
targets. Keep elements near the size their content needs while space is
available; resize flexible regions first and reduce other elements only when
the available space requires it.

Dense tables and canvases may need intentional scrolling or alternate views.
Keep essential context and controls available, and distinguish that behavior
from accidental page overflow.

## Alignment

Lines, gaps, centers and radii are measured on the rendered result, never
estimated from the code. A miss of 1–4pt is a finding, because it reads as a
mistake while a `16pt` indent reads as intent. Visual weight has no number; judge
it from a capture at 1× and name what the eye lands on first.

- **Shared edges.** Text, icons and controls that start a column share one edge. Use one spacing step per level of nesting, where `16pt` is a useful default.
- **Even gaps.** Repeated siblings sit at one gap, and every padding, gap and margin is a step on the project's scale.
- **Icons with labels.** An icon beside a label centers on the label's cap height, not its line box. Text in a control centers on cap height and baseline ([Typography](typography.md)).
- **Optical nudges.** Where geometric centering looks off, nudge by eye and name the value: give a button `2pt` less padding on its icon side, shift a play triangle toward its point, and fix asymmetric glyphs in the artwork itself.
- **Concentric radii.** Where nested surfaces share a visible, even inset, the outer radius is the inner radius plus the padding plus any border. Past `24pt` of padding, or with deliberately uneven padding, treat the layers as separate surfaces and keep each one's radius token.
- **Visual weight.** Circles and triangles need roughly 10% more size than a square to read as equal. Compare icon strokes with the text's stem weight, and filled icons beside outline icons.

On the web, run [measure.js](../../../references/alignment/measure.js) through the browser's evaluate call with `window.__alignmentOptions = { scale }` set from the spacing tokens, at a device scale factor of 2; treat each result as a candidate until a 2× crop confirms it.

## Surfaces and scroll edges

Use the project's tokens wherever one exists for a value below.

- **Scroll edges fade.** A scrolling region fades at its ends rather than cutting content at the edge.
- **Shadows are never cut off.** Give a scrolling region enough padding that its children's shadows fit inside it.
- **Code and tables scroll, never wrap.** Code blocks and data tables scroll sideways.
- **Overlays keep their scroll.** Scrolling past the end of a dialog, sheet, menu or side panel never scrolls the content behind it.
- **Sticky chrome keeps its edge.** A sticky header or footer takes a 1pt separator, or a fade, against the content scrolling under it, and anchored targets land below it rather than under it.
- **Content clears the system chrome.** Fixed headers, tab bars, toasts and sheets stay inside the safe areas, above the home indicator and clear of browser toolbars.
- **Floating surfaces take a ring, not a border.** A popover, menu or floating card pairs its shadow with a translucent 1pt ring rather than an opaque border.
- **Shadows are layered and fall one way.** Use the project's elevation token. Without one, layer three shadows with blur growing and opacity falling, all offset downward, rather than one heavy shadow. To raise a surface on hover, fade in the raised shadow rather than animating the shadow itself.
- **Content images take a faint outline.** Photos and screenshots take a 1pt outline inset by 1pt, black at 10% in light mode and white at 10% in dark, so a light image doesn't melt into its card. Skip logos and transparent artwork.

On the web: fade scroll edges with a `mask-image` gradient; contain overlays with `overscroll-behavior: contain`; offset anchors with `scroll-padding-block-start` set to the sticky header's height; use `viewport-fit=cover` with `env(safe-area-inset-*)`, and `100dvh` for app shells (`min-height: 100svh` for a first screen); draw rings inside the `box-shadow` stack over `border: 1px solid transparent`; and draw the image outline with `outline` and `outline-offset: -1px`.

On the web, a grid track or flex child holding long text needs `minmax(0, 1fr)` or `min-width: 0`; use `width: 100%`, not `100vw`, which includes the scrollbar; adapt reusable components with `@container`, not `@media`; give a container-query element a definite width; write logical properties (`margin-inline-start`, `inset-inline-start`, `float: inline-start`) and add `[dir="rtl"]` overrides for `translateX` and `background-position`, which have no logical form.

## Irregular collections

When items have different proportions, choose deliberately between cropping,
regular tracks, and a masonry-style layout. Preserve meaningful source order and
check that keyboard traversal agrees with visual grouping. Treat new layout
features as progressive enhancements and inspect the fallback on the supported
browsers or OS versions.
