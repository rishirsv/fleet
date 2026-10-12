# Text, color, and layout recipes

Web CSS for fonts, text layout, contrast, color tokens, themes, and
direction-aware or container-responsive layout. Use the project's styling system
and tune example values to the actual font, content, and supported browsers.

## Contents

- [Web fonts](#web-fonts)
- [Text layout](#text-layout)
- [Measure contrast](#measure-contrast)
- [Color tokens](#color-tokens)
- [Document canvas](#document-canvas)
- [Theme switch without transitions](#theme-switch-without-transitions)
- [Direction-aware layout](#direction-aware-layout)
- [Container queries](#container-queries)

## Web fonts

Replace the path and weight range with the font's own. Declare italic
separately when used. For a static font, declare one face per weight.

```css
@font-face {
  font-family: "Product Sans";
  src: url("./assets/product-sans.woff2") format("woff2");
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
}

body {
  font-family: "Product Sans", system-ui, sans-serif;
}
```

`swap` keeps fallback text visible but can change wrapping when the font
arrives. If that shift is disruptive, measure the fallback and set
`size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override` on
a fallback face; the values are specific to the font pair. Preload only fonts
needed immediately.

```css
.article {
  font-optical-sizing: auto;
}

.balance,
.timer {
  font-variant-numeric: lining-nums tabular-nums;
}

.small-caps {
  font-variant-caps: all-small-caps;
}
```

Check that the font supplies each feature. Tabular digits keep widths stable
for changing values and aligned columns; decimal alignment still needs layout.
Reserve `font-variation-settings` for axes without a standard property.

## Text layout

```css
.prose {
  max-inline-size: 65ch;
  font-size: 1rem;
  line-height: 1.6;
}

.display {
  font-size: clamp(2rem, 1.25rem + 3vw, 4.5rem);
  line-height: 1.1;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.description {
  text-wrap: pretty;
}

.user-content {
  overflow-wrap: anywhere;
}
```

Test fluid sizing under zoom as well as viewport changes. `balance` and `pretty`
are enhancements; normal wrapping must stay usable without them. Apply
aggressive word breaking only to content that needs it. Set
`min-inline-size: 0` on a flex or grid item whose intrinsic minimum blocks the
intended shrinkage.

```css
.single-line {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.preview {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}

.preview.is-expanded {
  display: block;
}
```

The single-line container needs a constrained width. Pair truncated meaningful
content with a keyboard- and touch-accessible detail or expansion control, and
keep its expanded state and label synchronized. Keep essential instructions and
interactive descendants outside clipped content.

```css
.text-link {
  text-decoration-line: underline;
  text-decoration-thickness: from-font;
  text-underline-offset: 0.15em;
  text-decoration-skip-ink: auto;
}
```

Check underline position with the active font and fallback. Isolate a value of
unknown direction inside directed content; isolation protects adjacent
punctuation and order but neither translates nor mirrors the layout:

```html
<p lang="en">Created by <bdi dir="auto">اسم المستخدم</bdi></p>
```

## Measure contrast

Measure a foreground (text, icon, or UI element) against the background it
actually renders on, usually the nearest ancestor that paints one. A card's
text measured against the page background gives the wrong answer.

Use the project's required standard. For WCAG 2.x AA, normal text generally
needs 4.5:1 and large text 3:1 (18pt, or 14pt bold). Required non-text
components and graphical information generally need 3:1 against adjacent
colors; check the criteria's exceptions. Report APCA, if used, as a separate
design measure.

Record the foreground, actual background, state and theme, method, result, and
threshold. Resolve alpha and overlapping layers first. Use a tool that supports
the color space; arbitrary conversions and antialiased glyph-edge samples
misstate contrast. A screenshot gives rendered evidence, without the authored
values.

Check:

- **Every pair in every appearance.** Light and dark palettes are not mirror
  images.
- **Translucent surfaces.** Text on a `backdrop-filter` header or overlay shifts
  with what scrolls behind. Test against the lightest and darkest content, or
  make the surface opaque enough.
- **Computed colors.** Measure the rendered result of `color-mix()`, relative
  color syntax, and opacity modifiers.
- **Text over images and gradients.** Measure the lowest-contrast region, or add
  a scrim for a controlled background.

To fix a failing pair, change the foreground's perceived lightness and keep its
hue and saturation, so the fix stays out of the palette. If no foreground
reaches the target while preserving the design, change the background or add a
controlled surface. Pushing lightness can leave the gamut; reduce chroma and
measure the mapped result. Change the governing token or local role, check its
other uses, and measure again.

## Color tokens

Use when creating or extending a theme system. Keep the project's naming
convention; a local color fix needs no token migration.

Primitive tokens name values by hue and step (`--blue-500`, `--neutral-200`) and
never change meaning between themes. Semantic tokens name roles
(`--color-text-secondary`, `--color-border-subtle`) and reference primitives.
Components use semantic tokens only.

```css
:root {
  /* Tier 1: primitives, named by appearance. Never used directly. */
  --blue-500: #3b82f6;
  --neutral-200: #e5e7eb;
  --neutral-700: #374151;

  /* Tier 2: semantics, named by role. Components use these. */
  --color-accent-solid: var(--blue-500);
  --color-border: var(--neutral-200);
  --color-text-secondary: var(--neutral-700);
}
```

Dark mode, a white-label theme, or an increased-contrast variant then changes
only which primitives the semantic tokens reference. If components used
`--blue-500` directly, every use would need inspection to decide which mean "the
accent". Add a component tier (`--color-button-danger-bg`) only where a
component intentionally diverges; repeated exceptions suggest a missing semantic
role.

Apply each semantic token only in the role it names. A text token reused as a
background can break when a future theme gives it a value that works only for
text.

```css
/* Bad: separator token used as text color */
.caption { color: var(--color-border); }

/* Bad: text token used as background */
.tag { background: var(--color-text-secondary); }
```

## Document canvas

A wrapper paints only its own box; the document canvas can show beyond it on
short pages and during overscroll. Give `html` an explicit background from the
same theme state as the app. A transparent root can inherit the body's
background, so a missing root declaration alone does not prove a visible
defect.

```css
/* Use the product's actual tokens and theme selector. */
:root {
  --page-background: #f6f3ec;
  color-scheme: light;
}

:root[data-theme="dark"] {
  --page-background: #191b20;
  color-scheme: dark;
}

html,
body {
  background-color: var(--page-background);
}
```

Put the theme selector where it can update the root token; a class on an app
descendant cannot change an ancestor's background. Apply the initial theme
before first paint so the canvas does not flash. If the page uses
`meta[name="theme-color"]`, update it on theme change with a literal color
(custom properties do not work there); `color-scheme` separately informs native
control rendering. Compare the app edge in each theme, including overscroll.
Keep normal bounce and scroll chaining; suppressing overscroll hides the
symptom without fixing the background.

Reference: [CSS canvas
backgrounds](https://www.w3.org/TR/css-backgrounds-3/#special-backgrounds).

## Theme switch without transitions

A theme switch changes `color`, `background-color`, `border-color`, and
`box-shadow` on nearly every element, so every transition on those properties
runs at once and the page fades slowly. Reuse the framework's option when it
exists (`next-themes` has `disableTransitionOnChange`). Otherwise, inject a
stylesheet that disables transitions, force a reflow, and remove the stylesheet
after the next paint:

```tsx
"use client";

import { useEffect } from "react";

export function DisableThemeTransitions() {
  useEffect(() => {
    const mql = window.matchMedia("(prefers-color-scheme: dark)");
    const styles = new Set<HTMLStyleElement>();
    const frames = new Set<number>();
    const afterFrame = (callback: () => void) => {
      const id = requestAnimationFrame(() => {
        frames.delete(id);
        callback();
      });
      frames.add(id);
    };

    const handleChange = () => {
      const style = document.createElement("style");
      style.append(document.createTextNode("*,*::before,*::after{transition:none !important}"));
      document.head.append(style);
      styles.add(style);

      const _flushReflow = document.body.offsetHeight;

      afterFrame(() => {
        afterFrame(() => {
          style.remove();
          styles.delete(style);
        });
      });
    };

    mql.addEventListener("change", handleChange);
    return () => {
      mql.removeEventListener("change", handleChange);
      frames.forEach((id) => cancelAnimationFrame(id));
      styles.forEach((style) => style.remove());
    };
  }, []);

  return null;
}
```

Reading `document.body.offsetHeight` forces a synchronous style flush, so the
new theme resolves while the override is present and no transition starts. The
nested `requestAnimationFrame` removes the override after that paint. Tracking
frames and styles lets unmount clean up during rapid switches. This handles the
OS-level change; wrap an in-app toggle the same way: apply the override, change
the theme, flush, remove.

## Direction-aware layout

For horizontal positions that follow writing direction, use logical properties
so the layout mirrors under `dir="rtl"`:

| Physical | Logical |
| --- | --- |
| `margin-left` | `margin-inline-start` |
| `padding-right` | `padding-inline-end` |
| `left: 0` | `inset-inline-start: 0` |
| `text-align: left` | `text-align: start` |
| `border-right` | `border-inline-end` |

```html
<!-- Good: Tailwind logical utilities -->
<div class="ms-4 pe-6 text-start">…</div>

<!-- Bad: breaks in RTL -->
<div class="ml-4 pr-6 text-left">…</div>
```

Keep physical properties for physical screen sides, such as a device notch or
a gesture direction. Flex and grid follow writing direction, but explicit
placement can override it; check reading order in RTL. Digits inside numbers
keep their order.

## Container queries

Use container queries for components whose layout depends on their column. A
card adapts to the column it is in. Set the threshold where its content stops
fitting; `400px` is an example.

```css
/* Good: component adapts to its container */
.card-list { container-type: inline-size; }
.card { display: grid; grid-template-columns: auto minmax(0, 1fr); }
@container (max-width: 400px) {
  .card { grid-template-columns: 1fr; }
}

/* Viewport queries alone miss a card inside a narrow sidebar */
@media (max-width: 768px) {
  .card { grid-template-columns: 1fr; }
}
```

Test the smallest and largest supported sizes first, then the sizes between.
