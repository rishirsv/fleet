# Quick checklist

**Fidelity**
- [ ] Reference frame rendered from the source
- [ ] Every moving element exported as its own layer, text included
- [ ] Figma z order kept, strokes above children, group shadow on the union
- [ ] Background is the original image, positioned by its transform, verified by PSNR
- [ ] Every variant keeps the background, frosted panels blur the photo behind them
- [ ] Still frame matches the reference (no structural differences)

**Context and layout**
- [ ] Context decided: showcase, or website with each section mapped (text only sections untouched)
- [ ] Website mockups: stories after the loading intro added only on request, otherwise offered
- [ ] Layout identified: app frame with joined surfaces, or separate cards
- [ ] App frame: joined surfaces present, opaque, and still in the empty state, Figma stacking kept where they meet
- [ ] Separate cards: cards rise in themselves, empty state is the background alone
- [ ] Each container clips its own contents with its exact radii
- [ ] Overflow check passes for the layout type

**Motion**
- [ ] Exports and page load start on the empty state
- [ ] Rise plus blur to sharp intro, staggered in reading order
- [ ] Bars fill like progress bars, no added loading lines or shapes that are not in the design
- [ ] Every visual acts out a story after load, starting and ending on the exact design; text only cards rest
- [ ] Stories stay visible in the 800×500 GIF
- [ ] Stories are obvious, offset between cards, and only counters or typing change text
- [ ] Covered layers arrive last and leave first
- [ ] No zoom or pan unless asked, background never moves
- [ ] Dissolves back to the empty state, background untouched
- [ ] Seam, empty beat, and rest checks pass

**Export**
- [ ] Deterministic frame capture: whole millisecond steps averaging 1000/60, start and tick inside the seek, no real time recording
- [ ] `<name>-x.mp4`, `<name>-loop.gif`, `<name>-800x500.gif` delivered
- [ ] Token never printed or committed
