# Color

Inspect existing brand colors, semantic roles, surface hierarchy, and themes.
Preserve their meaning unless changing the system is part of the request.
Choose colors by role and intended atmosphere, and choose accent strength,
neutrals, and saturation to fit the brief.

Never estimate a color you could compute. Notation, a tinted neutral and a gradient's interpolation space are project choices, not findings. A broken role mapping and an out-of-gamut step are findings. Perceived lightness throughout means OKLCH `L`, from `0` to `1`. Icon color belongs to [Icons](icons.md).

## Match the project's color system

Reuse the project's tokens and notation, whether CSS variables, an asset catalog or design-tool variables. One notation throughout beats a second one scattered through it.

For a new system, work in OKLCH, because its numbers behave the way the ramp rules below describe, then output in the platform's format: CSS `oklch()` or hex on the web, sRGB or Display P3 values in an asset catalog. A color library produces the same ramp in any notation.

## A system is ramps, not colors

One neutral ramp, one accent ramp and only the status ramps the product actually renders. A `warning` ramp nothing imports is maintenance for zero pixels. A second accent hue earns its place only when two things must be distinguishable at a glance. Otherwise use more steps of the one accent ramp.

## Every step has a job

A ramp is not a gradient to pick from by eye. Each step exists because a role needs it: window background, hovered or pressed component, border, solid fill, body text. Do not generate a step no role consumes. Both the Tailwind `50`–`950` and Radix `1`–`12` conventions map to those roles.

## Name primitives by hue, semantics by role

Primitives name a value (`blue-600`) and are never applied in a component. Semantic tokens name a job (`text-secondary`), point at a primitive and are the only tier components reference. That seam is what lets a theme repoint colors without touching components.

## Use a token only in its role

Never borrow a token because its value is right today. A separator used as a text color works until borders get lighter, and then the text goes with them. If a role has no token, add the token.

## Hold the hue across the ramp

A ramp holds one hue end to end, peaks in vividness mid-ramp and steps more finely at the light end. Build it with a color library, never by eye.

## One color, one meaning

Use a color for one purpose across the whole interface, treating anything within `15°` of OKLCH hue as the same color. Never let color be the only carrier of meaning. Pair it with an icon or a label.

## Fill exactly one action per view

When filled color encodes primary emphasis, one primary action gets it and peers stay neutral. Put the color on the background, not the label. A filled button reads as primary across the room; accent-colored text on a neutral button reads as a link.

Keep an established hierarchy that already signals emphasis another way. Several colored backgrounds are fine when they encode distinct states or categories rather than competing as peers.

## Foregrounds on color and imagery

Choose foregrounds relative to their surface. A generic gray or reduced-opacity
white can look muddy or disabled on a colored background and can vary over
imagery. Select a foreground for the actual background with the intended
prominence.

For text over imagery, test the full range of expected crops and user-provided
content. Reposition the text or focal crop when possible; otherwise control the
local background with a scrim, gradient, or image treatment.

## Pick a gradient's interpolation space

The space is a look, not a correctness setting. Where the platform lets you choose, default to a perceptual space (OKLab), and reach for OKLCH when a two-hue gradient goes gray in the middle; on the web, `in oklab` and `in oklch`.

## Themes

Check text, controls, focus, selection, and status contrast in their actual
contexts and themes. Paint the window or document background from the same
theme state as the content so overscroll and short screens match, and let
scrollbars and native controls follow the theme (on the web, `color-scheme` on
the root and one `theme-color` per scheme). When a theme switch animates the whole
page, suppress transitions for the swap.

## Web patterns

| Pattern | Fix |
| --- | --- |
| A hex, `rgb(` or `oklch(` literal in a component file where a token exists | Reuse or add the role token, in the project's notation |
| One `oklch(` value in a codebase otherwise written in hex | Write it in the established notation unless a migration is in scope |
| `var(--blue-600)` or `bg-blue-600` in a component file | Point a semantic token at the primitive and use that |
| A semantic name containing a hue or a component, as in `--color-blue-button` or `--color-sidebar-gray` | Rename it for its role: `--color-accent-solid`, `--color-bg-surface` |
| `--color-primary` and `--color-text-primary` both defined | Rename the brand token `accent` |
| A `border` or `separator` token inside `color:`, or a `text` token inside `background:` | Add a token for the missing role |
| `hsl(` ramp values that differ only in lightness | Rebuild with a constant perceived hue, in the project's notation |
| `50`–`200` stepping as far apart in OKLCH `L` as mid-ramp steps do | Tighten the light end to about `0.04`–`0.05` per step |
| One chroma or saturation number copied across every hue's ramp | Use the same proportion of each hue's own maximum |
| A status hue within `15°` of the accent hue | Move it at least `15°` away, or give the destructive action a distinct treatment |
| Dark tokens equal to the light ramp in reverse step order | Lower the accent's chroma, widen the dark end and remeasure every pair |
| Color tokens set under both `prefers-color-scheme` and a `.dark` class | Pick one switching mechanism and use it throughout |
| `oklch()` chroma beyond sRGB with no sRGB value declared before it | Declare the sRGB value first, then the vivid one inside `@media (color-gamut: p3)` |
