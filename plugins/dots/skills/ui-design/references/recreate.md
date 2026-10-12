# Recreate a reference

Recreate a selected image, screenshot, mockup, or live URL as a faithful,
responsive, interactive interface. Default to browser-openable local HTML with
CSS and JavaScript. Use an existing app's stack when the task is to integrate
there.

## Contents

- [Inputs](#inputs)
- [Resolve an image or mockup](#resolve-an-image-or-mockup)
- [Capture a live reference](#capture-a-live-reference)
- [Inspect a visual effect](#inspect-a-visual-effect)
- [Read the target](#read-the-target)
- [Prepare assets, type, and icons](#prepare-assets-type-and-icons)
- [Build the local interface](#build-the-local-interface)
- [Preview and deliver](#preview-and-deliver)

## Inputs

- **Target:** the exact selected image, screenshot, mockup, generated result,
  or URL and the routes to reproduce. A written brief alone does not establish
  visual fidelity.
- **Context:** relevant project code, brand assets, fonts, tokens, components,
  content, and behavior requirements already supplied or available locally.
- **Scope:** static mock, interactive prototype, or production integration;
  reference viewport and supported sizes. Infer the platform from the task and
  project; the screenshot's aspect ratio does not decide it.

Use this workflow when the reference is the target to reproduce. For inspiration
or redesign requests, preserve only the aspects the user selected.

## Resolve an image or mockup

Resolve the selected target before building. For numbered options, use the
user-visible image order. Prefer an exact attachment or image identifier over
an ordinal. If the selection is ambiguous, ask which image to reproduce.

Inspect the original at full resolution and retain detail crops where
typography, icons, or assets need closer comparison. A still image establishes
appearance; use the brief and product context for behavior it cannot show.

## Capture a live reference

Open the source in the in-app browser or the user's chosen browser. Confirm the
intended route and state before treating it as evidence; an unexpected login,
redirect, error, or loading screen is not the target. Try another available
browser when it could resolve an access problem. If access remains blocked,
identify the missing source and continue only from usable supplied evidence.

Capture each requested page from top to bottom with overlapping viewport views.
Let lazy content load and note sticky regions, scroll effects, animation, and
newly revealed controls. Return to the top to check changes caused by
scrolling. Repeat at relevant desktop and mobile sizes, using the user's device
dimensions when supplied. Record the route, viewport, and state for each
capture.

Use DOM and computed-style inspection alongside screenshots to recover copy,
link destinations, component structure, layout dimensions, spacing, colors,
fonts, assets, and responsive rules. Prefer observed values to guessed CSS.

Exercise the controls within the requested experience: navigation, inputs,
menus, drawers, dialogs, tabs, carousels, hover and focus states, and sticky
behavior. Isolate each interaction from a known starting state and record its
trigger, visible result, dismissal or recovery, and relevant DOM changes. For
actions that would change live data or submit a transaction, use a safe preview
or record the behavior as untested.

Save accessible source assets locally: images, logos, icons, fonts, video, SVGs,
sprites, masks, cursors, and backgrounds the experience needs. Preserve
filenames or source mappings useful for verification. Serve assets locally in
the delivered prototype instead of hotlinking them.

## Inspect a visual effect

Use when a live reference's blur, gradient, masking, or motion needs explanation
before recreation. Inspect the named region and the adjacent layers it depends
on with the browser's permitted inspection APIs.

An effect can depend on several layers. A hero gradient is commonly four things
at once:

- An element oversized past its container and pushed partly outside it, so no
  edge is ever visible.
- A multi-stop gradient at low alpha, often four stops around 20% opacity.
- A large `filter: blur()`, which blends the discrete stops.
- Sometimes a layer above with `backdrop-filter`, which blurs the content behind
  it.

Report the layers in paint order. For each, name the declaration that produces
its effect, include blur and element size when they determine the result, and
explain what the values do. For example, `opacity: 0 → 0.85 at 20% → 1` over
`1500ms` reaches 85% opacity in the first 300ms and takes the remaining 1200ms
for the last 15%: the layer appears quickly, then settles slowly. A linear
`0 → 1` over the same duration looks different.

Inspection methods:

- Read computed styles on the element and its `::before` and `::after`:
  background images, filters, backdrop filters, masks, blend modes, opacity,
  transforms, and shadows. Check whether a pseudo-element generates a box.
  Ignore identity values such as `blur(0px)`, but inspect the active state
  before dismissing an animated property.
- Use `elementsFromPoint` to find candidates in a region. It reflects hit
  testing: decoration with `pointer-events: none`, pseudo-elements, and shadow
  contents need separate inspection. Resolve stacking contexts, DOM order, and
  overlays; coordinates and `z-index` alone do not establish paint order.
- Use `getAnimations()` for CSS transitions, CSS animations, and Web Animations
  while the effect is active. Trigger the real interaction first; an empty
  result at rest does not disprove animation, and frame-driven scripts may not
  appear.
- If the result remains unexplained, inspect SVG filters, images, video,
  canvas, and clipped content. Finding nothing in CSS does not prove a shader.
  Avoid calling `canvas.getContext()` to detect a renderer; it can create or
  lock a context.

Label values read from computed styles as measured, values calculated from them
as derived, and guesses about authoring technique as inferred. Compiled styles
do not reveal which source helper the author used. From a screenshot alone,
propose how the effect could be built; pixel samples depend on capture scale,
antialiasing, and color processing.

## Read the target

Inspect the whole composition, then zoom into text, controls, and assets. Map
the sections, content order, grid, major proportions, alignment, margins,
padding, spacing rhythm, density, and visible states. Separate page content from
browser chrome, device frames, and the surrounding presentation canvas.

Use source values when available; otherwise estimate relationships and record
uncertainties that affect fidelity. For live sources, use the captured
responsive behavior. Match the reference viewport first, then adapt the
composition to the supported sizes. For a phone prototype, use the reference or
requested device dimensions and keep primary actions reachable without
accidental horizontal scrolling or clipping.

## Prepare assets, type, and icons

Inventory every visible asset and its location: hero and background images,
article art, thumbnails, illustrations, textures, logos, product imagery, and
avatars. Record the needed dimensions, crop, focal point, and transparency.

Reuse supplied originals and project assets first. Generate missing custom
imagery when needed, using reference crops and a shared art direction, palette,
and rendering style. Inspect each result at its display size. Prioritize assets
in the initial viewport and replace temporary placeholders before QA. Disclose
any approximation of an asset that cannot be recovered.

Keep lettering inside posters, packaging, signs, or illustrations in the image
when it belongs to the artwork. Implement editable interface copy as real text
and interactive UI as real elements. Use distinctive imagery where it carries
the design. Choose image, vector, or CSS techniques for fidelity and
editability; ordinary borders and gradients need no generated assets.

Use supplied fonts when available; otherwise find an available, appropriately
licensed match. Compare letterforms, weight, width, optical size, line metrics,
and wrapping. Choose an icon library by shape, stroke, fill, and optical weight.
Preserve supplied brand marks.

When asset production can proceed independently, delegate bounded asset tasks
while building the page. Give each task its reference crop, dimensions, focal
point, style, output path, and consuming element. Assign asset creation and page
edits to different files to avoid conflicts; standard library icons need no
asset subtask.

## Build the local interface

Use one HTML file with embedded CSS and JavaScript when practical, with local
asset files as needed. Add a framework or build tooling only when the existing
project or requested behavior needs it. Reuse shared styles and components so
each correction applies to all equivalent elements.

Build from captured evidence and preserve the target's copy, imagery, hierarchy,
and visual direction. In an existing app, connect controls to its state and
navigation instead of creating parallel behavior to mimic the screenshot.

Unless the user requests a static mock, make the core experience work:

- Navigation, links, tabs, menus, and primary calls to action.
- Visible inputs, filters, toggles, selections, and forms.
- Relevant hover, focus, selected, open and closed, loading, empty, error, and
  success states.
- The main task or journey from entry through its outcome.

Use local sample data and in-memory state for prototypes. Identify simulated
outcomes; add authentication, persistence, external integrations, or production
services only when the task requires them. Add screens only when the requested
journey needs them. In the delivery note, identify peripheral controls that
show appearance only.

## Preview and deliver

Open the result following [visual proof](../../../references/visual-proof.md).
Exercise primary interactions and investigate console errors affecting the
experience. For URL references, replay the captured interactions and compare
desktop and mobile behavior with the corresponding source states.

Run [design QA](design-qa.md) against the selected target at matching viewports
and states. A running server or successful build does not establish visual
fidelity.

Return the clickable HTML file or local preview URL, the QA result, and material
remaining differences or unverified behavior. If the iteration limit leaves QA
blocked, deliver the reviewable prototype with that status. Keep the preview
server running while the user needs it. Local delivery is sufficient;
publishing is a separate request.
