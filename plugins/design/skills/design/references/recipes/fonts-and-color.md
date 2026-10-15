# Font and color recipes

Web CSS for fonts, contrast, color tokens, the document canvas, and theme
switches. Use the project's styling system and tune example values to the
actual font, content, and supported browsers.

## Contents

- [Web fonts](#web-fonts)
- [Measure contrast](#measure-contrast)
- [Color tokens](#color-tokens)
- [Document canvas](#document-canvas)
- [Theme switch without transitions](#theme-switch-without-transitions)

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

## Measure contrast

Measure a foreground (text, icon, or UI element) against the background it
actually renders on, usually the nearest ancestor that paints one. A card's
text measured against the page background gives the wrong answer.

Use the project's required standard, and report APCA, if used, as a separate
design measure. Record the foreground, actual background, state and theme,
method, result, and threshold. Resolve alpha and overlapping layers first. Use
a tool that supports the color space; arbitrary conversions and antialiased
glyph-edge samples misstate contrast. A screenshot gives rendered evidence,
without the authored values.

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

Components use semantic tokens named by role (`--color-text-secondary`), which
reference primitives named by value (`--blue-500`), so a dark, white-label, or
increased-contrast theme changes only which primitives the semantic tokens
reference. Apply each semantic token only in the role it names: a separator
token used for text, or a text token used as a background, breaks when a future
theme gives it a value that suits only its own role.

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
