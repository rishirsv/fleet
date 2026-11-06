# Motion review

Use for product interaction motion. Showcase choreography belongs to
`$design-to-motion`; use the shared motion guidance when evaluating its website
behavior. Choose the mode before inspecting:

| Request | Work | Result |
|---|---|---|
| Review a transition or change | Inspect the scoped motion and its states | Findings and verdict |
| Improve motion across a product | Follow the [motion audit](motion-audit.md): recon, eight categories, vetted findings | Audit and self-contained plans |
| Find opportunities | Look for candidate changes and test each against the gate | Opportunities and rejected candidates |
| Remove motion that feels slow or excessive | Put every animation through the [removal gate](remove-motion.md), then subtract | Removals, kept motion and cleanup |

A review or opportunity search is read-only unless the user also requests
changes; removal edits code, but only to subtract. Do not claim product-wide coverage from a sampled route.

## Default to flagging

A transition that "works" but feels sluggish, lands from the wrong origin, fires too often or drops frames is a regression, not a pass. Approval is earned, not assumed. Measure every animation against [Motion](../../design/references/motion.md): the frequency gate, a named purpose, the easing and duration tables, the 300ms ceiling, origin at the trigger and never from zero scale, interruptibility, compositor-friendly properties, reduced motion and hover gating, asymmetric timing on deliberate actions, and cohesion with the product's personality. A violation is a finding. When unsure whether motion feels right, the strongest move is often to delete it.

## Gate and inspect

For each candidate, ask in order: **Should this animate at all? What is the
purpose?** Consider frequency, task, attention, and platform conventions. If
motion would slow or obscure the task, propose an immediate state change or
static feedback. For retained motion inspect entry, exit, origin, timing,
continuity, interruption, repeated activation, gestures, and reduced motion as
applicable. Reuse established tokens and components; avoid contradictory motion
systems.

Observe a running interaction when possible. Record or slow it and scrub through
intermediate frames to identify where a problem occurs; relate each finding to
the element, trigger, phase and relevant value. Exercise rapid reversal and
repetition at normal speed too: a slowed recording cannot establish
responsiveness. A screenshot shows an endpoint, not continuity. Source code
can establish implementation defects but cannot prove how movement feels.
Record device, viewport, input method, motion preference and coverage gaps.
Distinguish measured bottlenecks from guesses and do not transfer web
compositor rules to native UI.

## Fix order

When proposing fixes, prefer earlier moves over later ones:

1. **Delete the animation** (high-frequency, no purpose, keyboard-triggered).
2. **Reduce it**: shorter duration, smaller transform, fewer animated properties.
3. **Fix the easing**: ease-in to ease-out, or a strong custom curve.
4. **Fix the origin and physicality**: anchor to the trigger; replace a scale from zero with `0.95` plus opacity.
5. **Make it interruptible**: a fixed timeline to a state-driven transition, or a spring for gesture-driven motion.
6. **Move it to the compositor**: layout properties to position, scale and opacity.
7. **Asymmetric timing**: slow the deliberate phase, snap the response.
8. **Polish**: blur to mask a cross-fade, stagger for groups, an entry transition, a spring for elements that should feel alive.
9. **Preferences and cohesion**: reduced motion and hover gating; tune to the component's personality.

## Performance budgets

Measure smoothness with a trace, never a feeling. Every frame lands within one refresh interval: 16.7ms at 60Hz and 8.3ms at 120Hz, which most phones now run, so design against the smaller number. No animation frame runs past 50ms while something moves, and every interaction paints its response within 200ms. "Feels smooth" with no numbers is a finding.

1. **Name the interaction**: the screen, the steps and the moment that matters. Test on a mid-range device, or with the CPU throttled 4× to stand in for one; a fast laptop hides almost every problem.
2. **Record it** three times, then read each slow frame's cause: input delay, processing or presentation.
3. **Find the cause.** A layout property animated across a large subtree reflows every frame; move it to position, scale and opacity. Reading layout after writing a style forces layout mid-frame; read every value first, then write. A state update on every frame re-renders the tree; drive the value outside the render cycle. A large surface repainted each frame costs more than the motion is worth; shrink the painted area or fade a static copy.
4. **Trace the fix** with the same steps and the same throttle, and report both recordings side by side.

On Apple platforms, profile with Instruments and the Build iOS Apps performance skills. On the web, throttle through the browser's emulation and run [observe.js](frames/observe.js) through the browser's evaluate call: `window.__frames.start()`, perform the interaction three times, then `window.__frames.stop()`.

## Report

- **Focused review:** one table, one row per issue, never a list of Before:
  and After: lines, then a [severity](../../../references/severity.md) verdict
  and coverage gaps. These are `HIGH` and block: a feel-breaking regression
  (sluggish easing, an entrance from zero scale, ease-in on UI), animation on a
  keyboard or 100+/day action, or a layout-property animation with an easy
  compositor fix.

  | Before | After | Why |
  | --- | --- | --- |
  | Every property animated over 300ms | Transform over 200ms, ease-out | Name the properties; animating everything moves unintended properties off the compositor |
  | Popover growing from its own center | Origin at the trigger | Popovers grow from their trigger (modals are exempt) |
- **Product audit:** see [motion audit](motion-audit.md).
- **Opportunities:** list the proposed trigger, purpose, motion treatment and
  expected benefit. Also list plausible candidates rejected by the gate and
  why they should stay still. Do not invent durations where feel or platform
  behavior requires testing.

Based on Emil Kowalski's public review-animations, improve-animations,
find-animation-opportunities and animation-performance (emilkowalski/skills,
commit c8a7962), and Raphael Salaja's public frames (raphaelsalaja/skills,
commit 31031e9), adapted for web and native product interfaces;
[observe.js](frames/observe.js) is copied unchanged. See the
[Kowalski](../../../references/emil-kowalski-LICENSE.txt) and
[Salaja](../../../references/raphael-salaja-LICENSE.txt) licenses.
