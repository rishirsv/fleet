# PART A — Fidelity

## A1. Intake

Gather these before building. Infer what the request and source settle; ask, in one batch, only for what would change the result.

- **Context.** Showcase or website (see "Two contexts"). Decide this first.
- **Source.** A Figma link with a node id is best. A flat image works, but its layers cannot be separated perfectly (see A2).
- **Layout.** Decide it yourself from the tree (A5): an **app frame** (a dashboard or app screen built from joined surfaces, such as a sidebar and a body) or **separate cards** (a bento grid, a card set, widgets). The two load differently.
- **Background.** Is there a photo or texture behind the UI? Assume it must stay exactly as designed.
- **Visuals.** Which parts are visuals that should act out a story after load (B4)? Assume every chart, list, stack, calendar, flow, prompt, photo, media control, and status indicator.
- **Deliverables.** Showcase: default to all three, MP4 for X, website GIF, 800×500 GIF. Website: the animated sections in the site's code, with exports only when asked.
- **Camera.** Assume no zoom and no pan (B7).

If the user cannot answer, make a reasonable assumption, state it in one line, and continue. Deliver the live page with the exports, so the direction can still be corrected.

## A2. Source of truth

**Figma.** Prefer an available, authorized design-tool connector that can read
node structure and render or export the required layers. Discover its actual
capabilities; do not assume a particular tool name or require a personal access
token when the connector supplies the needed data. See
[Design connectors](../../../references/tools.md).

The REST endpoints below describe the required data, not a mandatory transport.
Use direct REST only when the connector cannot supply the required structure or
exports and authorized credentials are available. If access is missing, use
supplied design exports or ask for the missing access; do not imply that a
connector provides a token or silently approximate unavailable layers.

- Read the token from a secure store (an environment variable or the OS keychain). Never print it, echo it, paste it into chat, or commit it.
- `GET /v1/files/:key/nodes?ids=:node&geometry=paths` gives the tree, bounds, fills, effects, and radii.
- `GET /v1/images/:key?ids=:node&format=png&scale=2` renders the **reference frame**. The finished still must match this image (A7).
- Note the frame's absolute origin. Every layer position is `absolute bounds − origin`.
- The image URLs the API returns point at a CDN that sometimes resets connections. Retry every download, and check each PNG's size before using it.

**Flat image only.** The image is the reference. Rebuild what you can isolate, and tell the user plainly which parts cannot be separated before you animate them. Never fake fidelity by animating a screenshot as one block.

## A3. Layer export

Export every element that will move as its own PNG at **3x** using the connected tool’s export capability. When using REST `/v1/images`, batch 20 to 25 ids per call. Preserve the same bounds, layer order, and fidelity checks with either route.

| Case | Placement |
|---|---|
| PNG size equals `absoluteRenderBounds` (text layers always do) | Place at the render bounds |
| PNG larger than the render bounds (a parent clipped it), effects that overhang evenly | `x = bbox.x − (pngW − bbox.w) / 2`. Use `renderBounds.y` when the top was not clipped, otherwise derive it from the effect radius and offset |
| Overhang that is not even (a line with an arrowhead, a stroke with one square cap) | Take the bounds of `strokeGeometry` or `fillGeometry` from the `geometry=paths` response instead of the formula |
| Rotated vectors with a large layer blur (soft colour blobs) | Export with `use_absolute_bounds=true` and place at the bounding box. Run a PSNR offset search against the reference only if that region scores below about 45 dB. Blobs can be stored at 1x; the loss is invisible |
| Zero height or zero width stroked vectors | `use_absolute_bounds=true` returns null for them. Export without it |
| Mask group with blurred content | Anchor on the edge that was not clipped (usually the bottom of the mask plus its stroke) |
| Arcs, donuts, partial ellipses | Export with `use_absolute_bounds=true` |
| Patterns or overlays far larger than their surface | Export with `use_absolute_bounds=true`, then crop to the surface rectangle |
| Instance children (ids like `I12:34;56:78`) | They often return null. Export the parent instance |
| Lines that should draw on, dashed or not | Figma outlines strokes into filled shapes, so there is no centerline to animate. Write the centerline yourself and use it as a mask over the exported PNG (example below) |
| A photo baked inside a larger exported layer | Export the photo node on its own as well. Cover the baked photo with a skeleton, and put the separate photo layer on top for the `photo` resolve. At rest it must equal the reference |

Rules that keep the frame exact:

- **Text stays an exported layer in a showcase.** Never retype it in HTML there: fonts, kerning, and line metrics will not match. On a website, text is live HTML (see "Two contexts").
- **Keep Figma's z order.** Static layers can sit between animated ones in the same order the tree has them.
- **Frame strokes usually draw above children.** Render a card's stroke as a separate overlay above its clipped content, then confirm against the reference: a glow inside the card can tint the stroke in Figma's render.
- **Containers whose children move on their own.** The API always exports a frame together with its children, so exporting a card or panel bakes in everything inside it. When its children must load or act separately, rebuild the container in CSS from the node data: fills, corner radii, inside strokes (including `individualStrokeWeights`), and effects. Then export each child separately.
- **Shadow mapping.** A Figma drop shadow with blur `R` is a CSS `box-shadow` with blur `R` on a single element, or `filter: drop-shadow()` with blur about `R / 2` on a group. Both give the same Gaussian. Verify against the reference.
- **A group shadow is the shadow of the union.** When a drop shadow sits on a group of joined surfaces (an app frame), put all surface shapes in one static container with `filter: drop-shadow()`. Per element `box-shadow` would darken neighbours where surfaces overlap. Separate cards each carry their own shadow inside their `card` unit, so the shadow moves with the card.
- **Skip hidden layers** (`visible: false`) and stray layers buried under opaque shapes.

**Drawing a line on.** Read the corner points and arc radii from the outline in `strokeGeometry`: the centerline sits halfway across the stroke width, and a rounded corner's centerline radius is the outline's inner radius plus half the stroke. Most UI connectors are straight runs and arcs, so the path is short:

```html
<svg class="ly" viewBox="0 0 1440 990" style="left:0;top:0;width:1440px;height:990px">
  <mask id="draw1">
    <path d="M193 832 V700 A45 45 0 0 1 238 655 H380" fill="none" stroke="#fff" stroke-width="8"
          pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
  </mask>
  <image href="data:image/png;base64,..." x="192" y="653" width="190" height="181" mask="url(#draw1)"/>
</svg>
```

Animate `stroke-dashoffset` from 1 to 0 on the JS clock. `pathLength="1"` means no length measuring, and the wide mask stroke covers the line's antialiasing. For pulses that travel along it, read positions with `getPointAtLength` on the same path.

## A4. Background (sacred)

When the design sits on a photo or texture, the background is part of the design, not decoration. Often the whole canvas outside the app frame is background.

- **It never changes.** Not in the intro, not in the loop, not in the dissolve, not in any zoom. It never moves, blurs, scales, fades, or recolours.
- **Every version keeps it.** A "loading only" or "no zoom" variant is still the same design on the same background. Never drop the photo to make a variant simpler.
- **Export the original image, not a render.** Use the connector’s original-image capability when available; the REST equivalent is `GET /v1/files/:key/images`, which returns the raw image fills. Apply the fill's scale mode and `imageTransform` as CSS: for a stretch fill with a transform, `background-size` is the frame size divided by the transform scale, and `background-position` is the negative offset.
- **Verify it.** Compare the background region of your still against the reference. Aim above 45 dB PSNR. A crop or offset error shows up instantly.
- **Frosted panels must see the photo.** A surface with `backdrop-filter: blur()` is its own element, a sibling above the background, never inside an ancestor that has `filter` or `opacity` below 1. Headless Chrome only renders it with `transform: translateZ(0)` and a `z-index` on that element.
- **If you cannot reproduce it, say so before building.** No image access, a generated texture, a missing fill: tell the user and ask. Never swap in a flat colour silently.
- Store photos as high quality JPEG or WebP, not PNG.

## A5. Layout: app frame or separate cards

Decide which of the two layouts the design is. It changes what the empty state contains and what moves.

**App frame (joined surfaces).** A dashboard or app screen whose frame is built from two or more surfaces joined into one unit: a sidebar and a body, often overlapping by a few pixels. Only this layout gets static surfaces.

- **The surfaces exist in the empty state.** The sidebar and body are in place, fully opaque, and still from the first frame. They never fade, slide, scale, or blur in. Only the elements inside them load.
- **Keep Figma's stacking where they meet.** The body sits above the sidebar's content clip, so sidebar content can never draw over the body, and the body never slides over the sidebar.
- Cards inside the body are content: they load like any other element.

**Separate cards (bento, card sets, widgets).** Cards that stand apart from each other with gaps between them. These are **not** joined surfaces.

- **The cards themselves load in.** Each card rises in with blur (the `card` kind in B2), staggered in reading order, and its contents follow inside it.
- The empty state is the background alone.

**Both layouts:**

- **Each container clips its own contents** to its exact shape, including per corner radii. Nothing may overflow onto a neighbour or the background.
- **Image shaped surfaces.** When a container's silhouette is a photo (a cover header, a full bleed card image), give it a placeholder in the image's average colour. The photo then loads into it.
- **Nested content is content.** Trays, toolbars, and inner panels load like any other element.

Clip pattern, which keeps stage coordinates valid inside the clip. For separate cards, the card's unit wraps its clip, so the card and its contents move together:

```html
<div class="clip" style="left:113px;top:138px;width:305px;height:907px;border-radius:16px 0 0 16px">
  <div class="cin" style="left:-113px;top:-138px"><!-- units in stage coordinates --></div>
</div>
```

```css
.clip { position: absolute; overflow: hidden; isolation: isolate; }
.cin  { position: absolute; width: var(--stage-w); height: var(--stage-h); }
```

## A6. Page architecture (showcase)

On a website, build inside the site's code instead, following the website rules in "Two contexts". The clock, units, and modes below still apply per section.


- One self contained HTML file: a fixed size stage at the frame's exact size, scaled to fit the viewport. Images inline as base64, deduplicated when the same image repeats. Wait for decode on `<img>` elements only; CSS gradients are not images.
- **Modes:** `?still` renders the exact Figma frame with no motion (also used for reduced motion). `?loop` repeats the cycle like the exports. `?capture` turns off `requestAnimationFrame` and exposes `window.__start()`, `window.__tick(dt)`, and the loop time `window.__lt`, so the recorder drives the clock (C1).
- **Units.** Every animated element is wrapped in a full stage layer `.u` carrying its delay `--d`. The intro is CSS transitions keyed on `.stage.in`. Because a unit covers the whole stage, any percentage in `clip-path` or `transform-origin` on it refers to the stage, not the element. Use pixel values computed from the element's rectangle.
- **Static layers stay composited.** Give clips and stroke overlays `transform: translateZ(0)`, so their antialiasing does not change when nearby transitions start. Otherwise a 1px edge flickers at every cycle start.
- **One JS clock** (`requestAnimationFrame`) drives everything time based: masks, sweeps, stories, accents. Drive it from loop time, never from wall clock, so capture is deterministic. In `?capture` the clock advances only through `__tick`.
- Default page behaviour: wait for image decode, play the intro once (when the frame scrolls into view, if it sits on a longer page), then keep the stories running.

## A7. Verify the still

Render `?still` at 2x and compare it with the reference before any motion work.

- PSNR for the whole frame and for each container, after a light blur (`gblur sigma≈1.2`) so sub pixel antialiasing does not dominate. Aim above 35 dB overall and above 30 dB per container. Text heavy containers sit near 30 dB because 3x layers are resampled to 2x; if one is lower, retest it at `sigma≈2.5`, where text edges stop counting and only structure remains.
- Look at a blurred, amplified difference image. It reveals structural errors: a glow placed too high, wrong stacking, a missing stroke, a shifted shadow.
- **Do not chase sub pixel offsets.** Measuring at 2x cannot resolve errors under half a pixel, and "corrections" overshoot. Fix structure, not antialiasing.
