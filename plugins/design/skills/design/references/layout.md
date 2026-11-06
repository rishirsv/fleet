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

Scale properties at different rates. Large display type, media, and generous
padding often need to contract faster than body text, controls, and touch
targets. Keep elements near the size their content needs while space is
available; resize flexible regions first and reduce other elements only when
the available space requires it.

Dense tables and canvases may need intentional scrolling or alternate views.
Keep essential context and controls available, and distinguish that behavior
from accidental page overflow.

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

## Irregular collections

When items have different proportions, choose deliberately between cropping,
regular tracks, and a masonry-style layout. Preserve meaningful source order and
check that keyboard traversal agrees with visual grouping. Treat new layout
features as progressive enhancements and inspect the fallback on the supported
browsers or OS versions.

Surface, form, loading, navigation and sound defaults adapted from Raphael Salaja's public defaults (raphaelsalaja/skills, commit 31031e9). See [license](../../../references/raphael-salaja-LICENSE.txt).
