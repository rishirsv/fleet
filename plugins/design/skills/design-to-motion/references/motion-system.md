# PART B — Motion system

Every timing, distance, and curve below comes from the values in **Make it yours**. Never invent ad hoc values.

## B1. Start empty

The first frame of every page load and every export is the **empty state**. Empty becomes loaded. Never open on the finished frame.

- **App frame:** background plus the static joined surfaces, nothing else.
- **Separate cards:** the background alone.

## B2. Loading choreography

The appear animation is smooth, slow, and soft: elements **rise from below and resolve from blur to sharp**, staggered.

| Kind | Use for | From |
|---|---|---|
| `card` | Separate cards (bento, card sets) as a whole, with their shadow | `translateY(24px)`, `scale(0.985)`, `blur(6px)`, opacity 0 |
| `up` | Text, headers, values, rows | `translateY(10px)`, `blur(4px)`, opacity 0 |
| `down` | Top toolbars, top bars | `translateY(-8px)`, `blur(4px)` |
| `left` | Sidebar items, list rows, labels | `translateX(-10px)`, `blur(4px)` |
| `pop` | Icons, badges, avatars, buttons, dots | `scale(0.82–0.88)` from the element's own center, `blur(4px)` |
| `photo` | Images | skeleton shimmer first, then `blur(14px) saturate(0.6)` to sharp. For a photo baked into a bigger layer, see A3 |
| `wipe` | Bars, fills, highlights | A left to right `clip-path` reveal in pixels on the full stage unit (A6). The right inset starts at `stageW − x` (zero width, so no sliver shows) and ends at `stageW − (x + w)` (the element fully shown). Top and bottom insets stay at `y` and `stageH − (y + h)` |
| `line` / `grow` | Rules, ticks, timelines | `scaleX(0)` / `scaleY(0)` from their start edge |
| `donut` | Rings, gauges | conic mask sweeping clockwise from 12 o'clock |
| `tray` / `rise` | Sheets, trays, folders | slide up 40px from inside the container's bottom edge, clipped by it |
| `fade` | Layers that sit under another layer | opacity only |

- **Order.** Containers load in reading order, 80 to 90ms apart: for an app frame, the regions inside its static surfaces; for separate cards, the cards themselves, each starting about 0.15s before its own contents. Inside a container: header, then labels, then values, then visuals. Items in a group stagger 30 to 80ms.
- **Never `scale(0)` on an object.** Only lines and bars grow from zero, because they draw.
- **Covered layers arrive last and leave first.** Anything hidden under another layer in the final frame (calendar weeks under a meeting tray) appears after its cover lands and exits faster in the dissolve, so it never ghosts through.
- **Skeletons match the real shape** and sit 1px inside it, so no halo shows around the loaded image.
- Total intro: about 2 to 2.5 seconds for a full frame.

## B3. Bars fill like progress

- **Data bars, meters, and highlights fill like progress bars**: a left to right `clip-path` wipe with the in out curve, 0.7 to 1.1s.
- **Never add loading lines.** No progress line along a card's or surface's top edge, and no other bar or rule that is not in the design. Only shapes that exist in the design animate.

## B4. Story loops (the main act)

The intro is only the opening. The main act is every visual **acting out what it does**, on a loop: a lead list receives new leads, a chart is being read, a calendar finds an open slot, a prompt gets typed. When a user says "animate the visuals", this is what they mean. A frame that only loads in and then sits there with a few pulses is not finished.

**Write the story first.** For each visual, name its story in one sentence before building, for example "a new lead lands on top and the older ones settle back". Pick from this table, or invent one in the same spirit.

| Visual | Story |
|---|---|
| Stack of items (leads, notifications, files) | A new item lands on top with a blur, the others step back one slot, the last one leaves |
| Line or area chart | A scrubber glides across, dots ride the curves, the tooltip value counts. Or: the line redraws, a marker pops, the numbers count up with it |
| Bar chart, equalizer, grid of cells | Bars breathe like a live feed and settle back to the design heights. A dot and tooltip ride the active bar |
| Donut, gauge | Segments ease outward one at a time and back. Or: the ring sweeps again clockwise |
| Table, list | A cursor inspects rows one by one, the row highlights, and a preview loads for it. Or: a soft highlight steps down the rows |
| Calendar, scheduler | A highlight searches for an open slot, the event glides into it, then back |
| Flow, connectors, pipeline | Pulses travel along the connectors in the flow direction, and nodes or avatars light up as a pulse passes. Dashed lines march |
| AI, prompt, form | The prompt deletes and retypes, chips evaluate one by one, then the result appears with a blur |
| Counters, KPIs | Numbers count up together with the chart that drives them |
| Profile, long content | The content scrolls slowly inside its clip, then returns |
| Logo row | A continuous marquee that moves exactly one full set per loop, so it repeats seamlessly |
| Media player | The playback handle and progress advance while the play button pulses |

**Rules for stories**

- **Start and end on the exact design.** Each story leaves the Figma frame, acts, and comes back to it. At rest, the frame equals `?still`.
- **Use the design's own elements.** Cards, rows, bars, dots, chips, and tooltips from the design. Helpers the story needs (a cursor, duplicate stack items, extra pulses) must match the design's style, and are hidden in `?still`.
- **Changing text only when it is the point.** Counters, typing, and tooltip values. All other text stays still.
  - **Typing** reveals the exported text layer glyph by glyph, never as a smooth wipe. Find the glyph boundaries from the empty alpha columns of the text PNG, step the reveal one glyph every 45 to 70ms, and show a caret at the edge that blinks once a second while idle. Deleting runs the same steps backwards, a little faster.
  - **Counters** need live text in the design's font at the exact size and weight, landing on the design's exact text at rest.
- **Obvious, not busy.** Every card with a story shows a clear action every one to two seconds. A story is made of beats (a pulse leaves, a node lights, the arrow fires), and its beats provide that rhythm. If a viewer cannot tell the frame is animated within two seconds, the stories are too timid ("make more movement"). Calm screens, such as a document dashboard, may rest after load if the user prefers.
- **Text only cards get no story** in a showcase. They rise in with their card and rest. Not every card needs to move; every visual does.
- **Readable at the smallest export.** A story must still be visible in the 800×500 GIF. If a moving element is smaller than about 4px there (a pulse dot, a thin line), enlarge it within the design's style, add a halo, or pick a bigger story.
- **Offset the cards.** Cards never act in unison. Shift each card's story so attention travels around the frame in reading order.
- **One story per card, three to eight seconds long. A short story may repeat** within one cycle (twice in the 8.6s story phase is common), and a second run can vary a beat. Every run still ends at rest before the dissolve.
- Stories are built from eased keyframe tracks on the JS clock (A6), so capture stays deterministic:

```js
// [[time, value], ...] eased per segment; values may be numbers or arrays
function track(keys, t, ease = easeInOut) {
  if (t <= keys[0][0]) return keys[0][1];
  for (let i = 1; i < keys.length; i++) {
    const [t1, v1] = keys[i], [t0, v0] = keys[i - 1];
    if (t <= t1) {
      const k = ease(Math.min(1, (t - t0) / (t1 - t0 || 1)));
      return Array.isArray(v0) ? v0.map((v, j) => v + (v1[j] - v) * k) : v0 + (v1 - v0) * k;
    }
  }
  return keys[keys.length - 1][1];
}
// a slot that scrubs along a curve and returns to its design position
slot.style.transform = `translate(${track([[0, [0, 0]], [1.2, [46, -18]], [2.6, [46, -18]], [3.8, [0, 0]]], t).join('px,')}px)`;
```

**Accents** sit on top of stories, never instead of them:

| Accent | Use for | Values |
|---|---|---|
| Pulse ring | Status dots, live indicators, play buttons | 1.8–2.2s period, ring scale 1 → 2.6, opacity 0.55 → 0 |
| Heartbeat | Hearts, likes, sparkles | +20% over 0.35s, every 3s |
| Gentle bob | Floating objects (folders, devices, cards inside cards) | ±2.6px, 2.8s sine |
| Sheen sweep | Photos, bars, buttons | A band 38% of the element's width, peaking at 34% white, 1.5s pass every 3.4s. On light grey shapes it disappears; use a refill story instead |
| Skeleton glimmer | Placeholder lines inside the design | 2.4s shimmer |

- Stories and accents start when the intro has landed (about 2.4s). Stories begin from the exact design, so they need no fade. Accents and added helpers fade in over 0.6s.

## B5. The loop cycle (showcase)

On a website there is no cycle: the intro plays once on scroll and the stories run until the section leaves the viewport.


| Phase | Default timing |
|---|---|
| Build in | 0 → 2.4s |
| Stories | 2.4 → 11.0s |
| Dissolve | 11.0 → 11.6s (opacity 0.5s) |
| Empty beat | 11.6 → 12.0s |

- **The story phase holds at least one full story of every card.** Lengthen the cycle rather than cutting a story short. Time the stories so every card is back at rest when the dissolve starts.
- **The live page keeps telling stories forever** after its intro. Only `?loop` and the exports dissolve and restart.
- **Dissolve back to the empty state (B1).** For an app frame, only the contents dissolve and the joined surfaces stay. For separate cards, the cards dissolve too. The background never dissolves.
- **Reset everything.** A class that disables transitions for one frame resets the CSS, but every JS driven value (masks, tracks, helpers, typed text, pulses) must be set back to its empty state too, or it ghosts through the empty beat. The frame at the end of a cycle must equal the frame at its start.

## B6. Easing and duration

Never use default `ease` or `linear` for entrances.

| Token | Curve | Use |
|---|---|---|
| `--e` | `cubic-bezier(0.16, 1, 0.3, 1)` | Transforms on entrance (1.05s) |
| `--e2` | `cubic-bezier(0.33, 1, 0.68, 1)` | Opacity and blur (0.7–0.8s) |
| `--io` | `cubic-bezier(0.65, 0, 0.35, 1)` | Wipes, fills, sweeps, camera moves |
| linear | `linear` | Constant motion only (shimmer, playback) |

Showcase timing is slower than product UI timing on purpose. Product rules like "under 300ms" do not apply here; slow and smooth is the brief.

## B7. Camera

- **No zoom and no pan** by default. The user has to ask for it.
- When asked: only the app frame scales toward the items, the background never moves (A4), moves use `--io`, and the frame returns to its resting position before the dissolve.

## B8. Performance and accessibility

- Animate `transform`, `opacity`, `filter`, and `clip-path` only. Never `top`, `left`, `width`, or `height`.
- Keep animated blur at 14px or less. Static `backdrop-filter` is fine.
- `prefers-reduced-motion: reduce` renders the still frame.
- CSS transitions for the intro, the JS clock only for time based effects.

## B9. Motion checks

Run these on the recorded frames (C1) before encoding.

- **Overflow check.** Test with the containers' real shapes, rounded corners included, not rectangles: render a mask from the page itself (every container as a solid white shape with its exact radii on black, plus its shadow area if it has one), grow it by 2px to skip antialiasing, and compare only the black pixels. Any `?still` used for comparison here is rendered at the capture's device scale factor, not at the 2x of A7.
  - **App frame:** every pixel outside the joined surfaces must be identical to the empty first frame in every frame of the cycle (PSNR `inf`).
  - **Separate cards:** during the story phase, every pixel outside the cards (and their shadows, when they have any) must be identical to the `?still` frame, so no story, helper, or content escapes its card. The intro frames are excluded, because the cards' own rise moves pixels there; the contact sheet must show contents moving with their card, never ahead of it or outside it.
- **Seam check.** The first frame of the export window equals the frame one cycle later.
- **Empty beat check.** Every frame of the empty beat equals the frame before `__start`. The seam check cannot catch JS state that failed to reset, because both its frames are at loop time 0; this one can.
- **Rest check.** The last frame before the dissolve equals `?still` at the capture scale, proving every story came back to the design.
- **Contact sheet.** Tile frames at key moments (empty, mid intro, landed, several points through the stories, mid dissolve, end) and look for overflow, ghosting, pops, and stories too timid to notice.

## Make it yours

Every motion and export value lives here. Edit this section and the rest of the skill follows.

| Value | Default |
|---|---|
| Rise distance | 10px (`up`), 8px (`down`), 10px (`left`) |
| Entrance blur | 4px, photos 14px |
| Pop start scale | 0.82–0.88 |
| Transform duration | 1.05s with `--e` |
| Opacity and blur duration | 0.7–0.8s with `--e2` |
| Wipe duration | 0.7s, slow bars 1.1s, with `--io` |
| Card rise | 24px, `scale(0.985)`, `blur(6px)`, 0.9s transform with `--e`, 0.6s opacity |
| Container stagger | 80–90ms |
| Tray and folder rise | 40px |
| Typing | one glyph every 45–70ms, caret blink 1s |
| Item stagger | 30–80ms |
| Story start | 2.4s |
| Story length | 3–8s per card, offset between cards |
| Cycle | 12s (dissolve at 11.0s, reset at 11.6s), longer if a story needs it |
| MP4 | 60fps, CRF 15, max 1920×1200 |
| Website GIF | 960px wide, 20fps |
| Small GIF | 800×500, 20fps |
