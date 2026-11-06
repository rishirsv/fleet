# Motion review

Use for product interaction motion. Measure every animation against
[Motion](../../design/references/motion.md) and cite its values; never
approximate them. Choose the mode before inspecting:

| Request | Result | Edits |
|---|---|---|
| Review a transition or change | Findings table and verdict | None |
| Audit motion across a product | Ranked findings, then plans for the ones picked | Plans only |
| Find opportunities | Proposed motion and rejected candidates | None |
| Remove motion that feels slow or excessive | Removed, kept, and cleanup | Subtraction only |

Do not claim product-wide coverage from a sampled route. If a design doc or
comment explains a deliberate motion choice, note it and leave it.

## Default to flagging

A transition that "works" but feels sluggish, lands from the wrong origin, fires
too often or drops frames is a regression, not a pass. Approval is earned, not
assumed. When unsure whether motion feels right, the strongest move is often to
delete it.

## The gate

Walk every animation through this, in order, and record the deciding branch:

1. **Keyboard-triggered** (shortcut, command palette, focus jump, arrow keys): delete.
2. **Seen 100+ times a day** (core navigation, tab switches, list rows, in-app route changes): delete.
3. **On data the user reads or acts on** (charts, tables, numbers): delete, unless it shows a real change in value on user action.
4. **No nameable purpose** (feedback, spatial consistency, state, preventing a jarring change, explanation): keep only if it is a rare, first-time moment; otherwise delete.
5. **Seen tens of times a day** (hover, frequent toggles, list expansion): reduce to the near-imperceptible version.
6. **Over budget** (UI animation over 300ms, or a slide or scale where a fade carries the same meaning): reduce.
7. Otherwise keep.

Marketing pages get more latitude: explanation and one hero entrance can stay.
Scroll reveals on every section still fail.

## Inspect

For retained motion inspect entry, exit, origin, timing, continuity,
interruption, repeated activation, gestures and reduced motion. Check the eight
categories:

1. **Purpose and frequency**, as the gate above.
2. **Easing and duration.** Ease-in anywhere, bare ease or linear on entrances, UI durations over 300ms, a delay on every tooltip in a toolbar after the first.
3. **Physicality and origin.** Scale from zero, pure fades with no initial transform, trigger-anchored surfaces growing from their own center (modals are exempt), pressables with no press feedback.
4. **Interruptibility.** Fixed timelines on toasts, toggles and rapidly triggered UI; gestures tweened with fixed durations; drags dismissed on distance rather than velocity (about `0.11` points per millisecond); hard stops at boundaries instead of rising resistance.
5. **Performance.** Every property animated, layout properties animated, a parent value that recalculates every child, heavy animated blur.
6. **Preferences.** No reduced-motion handling, hover motion on touch, reduced-motion treatments that remove all feedback.
7. **Cohesion and tokens.** One bouncy component in a crisp app, near-identical curves that should be one token, group entrances with no stagger, cross-fades that double-expose.
8. **Missed opportunities.** State changes that teleport, spatially connected UI with no motion explaining where it came from. Report at most a handful.

Observe a running interaction when possible. Record or slow it and scrub
intermediate frames; relate each finding to the element, trigger, phase and
value. Exercise rapid reversal and repetition at normal speed too: a slowed
recording cannot establish responsiveness. A screenshot shows an endpoint, not
continuity. Source can establish implementation defects but cannot prove how
movement feels. Record device, viewport, input method, motion preference and
coverage gaps, and do not transfer web compositor rules to native UI.

## Fix order

Prefer earlier moves:

1. Delete the animation.
2. Reduce it: shorter duration, smaller transform, fewer properties.
3. Fix the easing: ease-in to ease-out, or a strong custom curve.
4. Fix origin and physicality: anchor to the trigger; replace scale from zero with `0.95` plus opacity.
5. Make it interruptible: state-driven transitions, springs for gestures.
6. Move it to the compositor: position, scale and opacity.
7. Asymmetric timing: slow the deliberate phase, snap the response.
8. Polish: blur-masked cross-fades, stagger for groups, springs for elements that should feel alive.
9. Preferences and cohesion: reduced motion, hover gating, the product's personality.

## Performance

Measure smoothness with a trace, never a feeling. Every frame lands within one
refresh interval (8.3ms at 120Hz, which most phones run), no frame runs past
50ms while something moves, and every interaction paints its response within
200ms. Test on a mid-range device or with the CPU throttled 4×, record the
interaction three times, read each slow frame's cause, then trace the fix with
the same steps and throttle and report both side by side.

On Apple platforms, profile with Instruments. On the web, throttle through the
browser's emulation and run [observe.js](frames/observe.js) through the
browser's evaluate call: `window.__frames.start()`, perform the interaction
three times, then `window.__frames.stop()`.

## Removal

Only subtract: delete an animation, reduce it, or remove code it orphaned.
Never add motion or retune easing on animations that stay; list badly built
survivors for a focused review. Propose, never perform, removing a motion
dependency. Reducing means a smaller version of the same motion: hover with
scale or lift becomes color or opacity under 150ms; a frequent slide or scale
entrance becomes a 150ms fade; anything over 300ms drops to 200–250ms; a stagger
caps at 30ms per item; an infinite loop on a persistent element runs once. If
reducing leaves motion too small to carry its purpose, delete it.

Before deleting, check what depends on it:

- **Hidden start states.** An element resting invisible, offset or scaled until its animation runs stays that way forever unless the start state goes too.
- **Code that waits.** Completion callbacks and delays sized to a duration must go with it.
- **Exit animations.** Work that ran after an exit moves to the point the view closes.
- **Layout animations hiding a jump.** If removal exposes a layout shift, keep the animation and report the shift.
- **Focus and tests** timed after motion must move or wait immediately.

Then delete orphaned definitions, wrappers, imports and tokens, and search for
every removed name to confirm nothing references it.

## Report

- **Focused review:** one table, then a [severity](../../../references/severity.md) verdict and coverage gaps. A feel-breaking regression, animation on a keyboard or 100+/day action, or a layout-property animation with an easy compositor fix is `HIGH` and blocks.

  | Before | After | Why |
  | --- | --- | --- |
  | Popover growing from its own center | Origin at the trigger | Popovers grow from their trigger |

- **Product audit:** re-read the cited code for every finding and drop anything by design, mis-attributed or exempt. Present one table ordered by impact over effort (`#`, severity, category, location, finding, fix). Write a plan under `plans/` only for the findings the user picks, or the top three to five when they ask without picking. Each plan is self-contained: problem with `path:line` and current code, exact target values, the repo convention to imitate, one edit per step, boundaries, and a feel check to watch at normal and slowed speed. "The motion here is already right" is a valid result.
- **Opportunities:** trigger, purpose, treatment and expected benefit, plus plausible candidates the gate rejected and why.
- **Removal:** a table of removed and reduced animations (location, was, verdict, deciding branch), ordered by frequency; two to five animations deliberately kept with the purpose that saved them; the cleanup; and what still needs a check on a real device.

Based on Emil Kowalski's public review-animations, improve-animations,
find-animation-opportunities, animation-performance and remove-animations
(emilkowalski/skills, commit c8a7962), and Raphael Salaja's public frames
(raphaelsalaja/skills, commit 31031e9), adapted for web and native product
interfaces; [observe.js](frames/observe.js) is copied unchanged. See the
[Kowalski](../../../references/emil-kowalski-LICENSE.txt) and
[Salaja](../../../references/raphael-salaja-LICENSE.txt) licenses.
