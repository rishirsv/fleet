# PART C — Recording and export

## C1. Deterministic capture

Use a browser capability that supports a controlled clock and frame capture. If using a shell-launched browser or Playwright runner, follow the active host’s browser preflight requirements. If deterministic capture is unavailable, report that limitation rather than claiming the checks passed. Never screen record in real time. Step a fake clock and screenshot every frame. Three details decide whether the loop is smooth and the seam is clean; all three are in the snippet.

```js
await page.clock.install({ time: 0 });
await page.goto(url + '?capture', { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.clock.pauseAt(10000);
const loopTime = [];
for (let i = 0; i < frames; i++) {
  // 1. whole milliseconds that average exactly 1000/60 (17, 17, 16, ...); runFor(1000 / 60) drifts
  const dt = Math.round((i + 1) * 1000 / 60) - Math.round(i * 1000 / 60);
  await page.clock.runFor(dt);
  loopTime.push(await page.evaluate(([i, PRE, dt]) => {
    if (i === PRE) window.__start();          // 2. start inside the same evaluate as the seek
    if (i >= PRE) window.__tick(dt / 1000);   // 3. the page clock advances here, never through rAF
    const now = performance.now();
    for (const a of document.getAnimations()) {  // CSS transitions follow the fake clock
      a.__m ??= window.__mark;                    // each one keeps the mark it was created under
      a.pause(); a.currentTime = Math.max(0, now - a.__m);
    }
    return i >= PRE ? window.__lt : 0;
  }, [i, PRE, dt]));
  await page.screenshot({ path: `${out}/${String(i).padStart(5, '0')}.png` });
}
```

On the page side, in `?capture`:

- `__start()` adds the `in` class. Every change of the stage's state classes (`in`, `out`, the reset) sets `window.__mark = performance.now()`, so each transition is seeked from the moment it was created. Transition delays (`--d`) are counted inside `currentTime`.
- `__tick(dt)` advances the loop time, runs the cycle phases (B5), draws every story and accent, and sets `window.__lt`.
- Loops that never end (shimmer, marquee) are driven by the JS clock, not by infinite CSS keyframes, which the seek would restart.

`PRE` is a few frames (about 15) recorded before the start, so the page has settled. Save `loopTime` beside the frames.

- Viewport is the frame size. `deviceScaleFactor = min(1920 / W, 1200 / H)` so the long side hits the X limit. Screenshots round to whole pixels and can come out one pixel odd (1745×1200 for a 1440×990 frame); the MP4 crop to even dimensions takes care of it, so expect 1744×1200.
- **The export window** starts at frame `PRE − 1` (loop time 0, the empty state) and spans exactly `cycle × 60` frames. Record at least 10 frames past it for the seam check.

## C2. Formats

| File | Spec |
|---|---|
| `<name>-x.mp4` | H.264, `yuv420p`, 60fps, CRF 14–15, preset slow, `+faststart`, max 1920×1200, even dimensions |
| `<name>-loop.gif` | 960px wide, 15–20fps, about 2 to 3MB, for the website |
| `<name>-800x500.gif` | Always delivered. When the frame has wide empty borders (most card and bento frames), crop to the content with about 40px of margin at exactly 1.6:1. When the content fills the frame, fit it and pad with the page background colour. On a photo background, always crop, so no flat band sits beside the photo. 20fps, 12fps if heavy |

```bash
ffmpeg -start_number $A -framerate 60 -i frames/%05d.png -frames:v $N \
  -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -preset slow -crf 15 \
  -pix_fmt yuv420p -movflags +faststart name-x.mp4

ffmpeg -start_number $A -framerate 60 -i frames/%05d.png -filter_complex \
  "trim=end_frame=$N,fps=20,scale=960:-2:flags=lanczos,split[a][b];\
   [a]palettegen=max_colors=192:stats_mode=diff[p];\
   [b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" -loop 0 name-loop.gif
```

For the 800×500 GIF, add `scale=800:500:force_original_aspect_ratio=decrease,pad=800:500:(ow-iw)/2:(oh-ih)/2:color=<page bg>` before `split`.

- Keep bayer dithering whenever a photo is in frame; without it photos band.
- If a GIF is too heavy, lower the frame rate or colours before lowering the size.
