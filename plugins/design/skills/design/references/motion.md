# Motion

Use motion to explain change, maintain spatial continuity, give feedback, or
express the interface's character. Preserve established motion conventions when
refining a product.

Two failure modes, and the first is worse:

1. **Animating something that shouldn't animate.** The gate below exists to produce zero lines of code sometimes. That's a success, not a dodge.
2. **Animating the right thing with the wrong ingredients** — an ease-in entrance, a scale from zero, a fixed timeline on a toast, a duration that makes a dropdown feel sluggish.

Make the call and state the reasoning in one line rather than presenting motion options as a menu. The values below are starting points: existing product and platform conventions and tokens take precedence, and a parallel motion system beside them is a defect.

Use [motion review](../../design-review/references/motion-review.md) for a
focused review, product-wide audit, search for opportunities, or removal. Use
[animation vocabulary](animation-vocabulary.md) to name an effect.

## Should this animate at all?

| Frequency | Decision |
| --- | --- |
| 100+ times/day (keyboard shortcuts, command palette toggle) | **No animation. Ever.** Stop here. |
| Tens of times/day (hover effects, list navigation) | Near-imperceptible only — fast and subtle, or nothing |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare / first-time (onboarding, success, celebration) | The delight budget lives here |

**Keyboard-initiated actions are a disqualifier, not a judgment call.** A launcher opened hundreds of times a day has no open/close animation, and that is correct. If the request fails this gate, say so and offer the non-motion alternative (an instant state change, a static affordance).

Default to immediate hover and selection feedback for repeatedly traversed rows,
menus, and tabs. Highlights follow the current pointer or focus position
without delay as the user moves across neighboring items.

## What is the purpose?

Name it in one of these words before continuing:

- **Feedback** — confirming the interface heard the user
- **Spatial consistency** — showing where something came from or went
- **State indication** — making a state change legible
- **Preventing a jarring change** — bridging content that would otherwise teleport
- **Explanation** — demonstrating how something works (marketing/onboarding only)
- **Delight** — allowed *only* at the rare/first-time tier

Can't name it? Don't build it. Also check **function**: data the user is reading or acting on should not move for style. Keep unsolicited movement to one orchestrated moment per view, preserve immediate access to content and controls, and add no artificial waiting to make an operation seem substantial.

## Pick the mechanism — cheapest that works

Walk down; stop at the first that fits:

1. A state-driven transition for hover, press, color and toggles.
2. An entry transition that runs when the element appears.
3. A predetermined animation that stays smooth while the app is busy, because it runs off the main thread.
4. Programmatic control of a single animation.
5. An animation or spring system for springs, layout animations, exit animations and gesture-driven values.

Use declarative, predetermined animation for fixed motion and programmatic springs for dynamic, interruptible motion. When the task needs a component rather than an animation — a toast, a drawer, a menu — use the platform's or the project's component instead of hand-rolling one.

## Pick the properties

- **Animate position, scale, rotation and opacity.** They skip layout and paint; animating width, height, margins or offsets re-runs layout every frame. Height is tolerated only for accordions, where nothing else expresses the change.
- **Never scale from zero.** Start from `0.9`–`0.97` scale with zero opacity. Nothing in the real world appears from nothing.
- **Anchor to the trigger.** Popovers, dropdowns, menus and tooltips grow out of the control that opened them. **Modals are exempt**; they're not anchored, so they stay centered.
- **Move by the element's own size**, not a fixed distance, when it slides fully in or out.
- **Transition only what changes.** Name the properties; never animate every property.

## Easing, duration — or a spring

| Situation | Easing |
| --- | --- |
| Entering or exiting | ease-out |
| Moving / morphing on screen | ease-in-out |
| Hover / color change | ease |
| Constant motion (marquee, progress) | linear |
| Default | ease-out |

**Never ease-in on UI.** It starts slow, delaying the exact moment the user is watching. Ease-out at 200ms *feels* faster than ease-in at 200ms. Built-in curves are too weak; use these cubic-bézier curves:

| Curve | Control points | Use |
| --- | --- | --- |
| Strong ease-out | `(0.23, 1, 0.32, 1)` | UI entrances and exits |
| Strong ease-in-out | `(0.77, 0, 0.175, 1)` | On-screen movement |
| Drawer | `(0.32, 0.72, 0, 1)` | iOS-like drawers and sheets |

| Element | Duration |
| --- | --- |
| Button press feedback | 100–160ms |
| Tooltips, small popovers | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Modals, drawers | 200–500ms |
| Marketing / explanatory | Can be longer |

**UI animations stay under 300ms.** A 180ms dropdown feels more responsive than a 400ms one. Within a range, choose by distance, element size, urgency and frequency of use.

**Reach for a spring instead** when the motion is drag with momentum, an element that should feel alive, a gesture the user can interrupt or reverse, or decorative pointer tracking. Tune settling time and overshoot deliberately; bounce can express character but should not make controls feel imprecise. Spring parameters differ by library and platform: confirm units and parameter meaning before transferring values; duration and bounce do not convert directly to stiffness and damping.

Think in two parameters. **Damping ratio** controls overshoot: `1.0` settles without bounce, lower overshoots. **Response** is how quickly the value reaches the target, in seconds; it is not a duration. Start most UI critically damped, and add bounce only when the gesture itself carried momentum (a flick, a throw, a drag release). Values Apple ships:

| Interaction | Damping | Response |
| --- | --- | --- |
| Move / reposition (e.g. PiP) | `1.0` | `0.4` |
| Rotation | `0.8` | `0.4` |
| Drawer / sheet | `0.8` | `0.3` |

## Common values

- **Press:** a pressed button scales to `0.97` over 100–160ms with ease-out, and a disabled one never scales. Give the button an opt-out where the motion would distract.
- **Stagger:** in a list, stagger items 30–80ms apart so everything doesn't enter at once, and bound the total so later items don't wait; on lists people see often, cap it at 30ms or fade the group as one. For a rare staged entrance (a first load, an onboarding step, an empty state), split the content into semantic chunks such as title, description and actions, and stagger them `100ms` apart, each entering with opacity, `4px` of blur and a `12px` rise over `300ms` with ease-out. Never stagger routine interactions.
- **Exits:** leave along the path you entered, shorter and smaller than the entrance: opacity, `4px` of blur and a fixed `12px` offset over `150ms` with ease-out, never the full container height. Slide fully out only where the destination carries meaning, such as a drawer closing. Remove the element instantly where motion adds no information.
- **Icon swaps:** where an icon swaps on an infrequent state change, such as play to pause or copy to copied, cross-fade both icons: scale `0.25` to `1`, opacity `0` to `1` and blur `4px` to `0`, over `300ms` with `(0.2, 0, 0, 1)` or an equivalent critically damped spring. A tab's icon swap and the actions a row reveals on hover respond instantly instead.
- **First appearance:** don't animate a component's default state in on first render; reserve that for intentional entrances.
- **Static cue:** every animated state change leaves a color, icon or label behind. Motion is never the only feedback.

## Choreograph the change

For a sequence with several stages, describe those stages before tuning
individual elements: what leads, what follows, which elements move together, and
what the final state is. Keep timing and spatial values named and easy to
adjust. Simple feedback needs no storyboard or stage controller.

Preserve identity through movement, resizing, and shared elements. Follow the
product's navigation model when forward and backward movement have different
meanings. Mirror the easing on reversible transitions so the outbound path
matches the return. Intermediate motion should point toward where things are
going. Coordinate by state or animation completion when one stage depends on
another; independent timers can drift or fire after the user leaves.

## Respond, interrupt, hand off

- **Respond on press, not on release.** Highlight a control the instant it's pressed. Audit debounces, artificial timers, transition waits and tap delays on the input path; anything not essential is a regression.
- **Never lock out input during a transition.** A user can grab a moving element mid-flight and reverse it.
- **Animate from the presented value**, the one on screen now, never the target. Rapid toggles, reversal and repeated activation converge on the latest requested state without snaps, queued animations, or delayed callbacks restoring an old state.
- **State-driven transitions, not fixed timelines, for anything triggered rapidly** — toasts, toggles, anything a user can fire twice in a second. Transitions retarget from the current value; fixed timelines restart from zero.
- **Springs for gestures**, because they carry velocity through an interruption. When a gesture reverses, blend velocity rather than hard-cutting it. Decompose 2D motion into independent X and Y springs.
- **Track 1:1 during direct manipulation.** Keep the grab offset, update continuously during the gesture rather than only at its end, and support cancellation. Require about `10pt` of movement before committing to a direction, and give tap targets about `10pt` of hysteresis so a press can be cancelled by dragging away and back.
- **Hand off velocity at release.** The spring starts at the finger's velocity; APIs that want relative velocity take `velocity / (target − current)`.
- **Project momentum.** Choose the destination from where the gesture is going, not where it was released: `projected = current + (velocity / 1000) × rate / (1 − rate)`, with a deceleration rate of about `0.998` (`0.99` for snappier), then snap to the nearest target.
- **Rubber-band at edges.** Resist progressively past a boundary instead of stopping hard: `offset = (overshoot × dimension × 0.55) / (dimension + 0.55 × |overshoot|)`.
- **Asymmetric timing where the user is deciding.** Slow on the deliberate phase (a hold-to-confirm press: 2s linear), snappy on the system's response (release: 200ms ease-out).

Separate product state from animated presentation. Define when an exiting
element stops accepting input, where focus moves, and when it can be removed.
Finish or cancel cleanup correctly even if motion is interrupted or disabled.
Keep scrolling and competing gestures usable, and provide alternatives for
essential gesture-only actions.

## Sound and haptics

1. **Causality** — it must be obvious what caused the feedback. Trigger it on the actual causal event (the toggle flipping, the item snapping home), and match its character to the action's physicality.
2. **Harmony** — the visual, the sound and the haptic fire on the **same frame**. Latency between them destroys the illusion.
3. **Utility** — add feedback only where it earns its place. Reserve haptics and sound for meaningful moments (success, error, commit, snap). Over-feedback trains users to ignore all of it.

Respect the separate sound and haptics settings. For the SwiftUI implementation of haptics and springs, use the Build iOS Apps plugin.

## Respect motion preferences

Reduced motion means **fewer and gentler** animations, not zero. Keep transitions that aid comprehension and replace translation, scale, zoom, parallax and repeated oscillation with an opacity cross-fade rather than removing the element instantly. Apply it to declarative and scripted animation alike, and respond to preference changes while the interface is open where supported. Hover effects run only on hover-capable pointers; touch fires false hovers on tap.

Keep progress and completion understandable without spatial motion. Avoid
flashing and provide control over prolonged automatic movement.

## Before you finish

| Never | Instead |
| --- | --- |
| Animating every property | Name the exact properties |
| Scale-from-zero entrance | `0.95` scale + zero opacity |
| Ease-in on a UI element | Ease-out or a strong custom curve |
| Built-in ease-out on a deliberate animation | `(0.23, 1, 0.32, 1)` |
| Animation on a keyboard shortcut or 100+/day action | No animation |
| UI duration over 300ms with no reason | 150–250ms |
| A trigger-anchored popover growing from its own center | Origin at the trigger (modals exempt) |
| A fixed timeline on toasts, toggles, rapidly-triggered elements | A state-driven transition |
| Animating width, height, margins or offsets | Position, scale and opacity |
| Hover motion on touch | Gate it to hover-capable pointers |
| No reduced-motion treatment | Gentler variant, not zero |
| Everything entering at once | 30–80ms stagger |

When the result depends on feel that code can't settle (a cross-fade, a spring's bounce, an entering list), say so and check it: play it at 2–5× duration, step it frame by frame, test gestures on a real device, and look again the next day.

## On the web

- Mechanism ladder: CSS transition, CSS `@starting-style`, CSS animation, the Web Animations API (`element.animate()`), then Motion for springs, layout, exit and gesture-driven values. CSS animations keep running smoothly under load; `requestAnimationFrame` animation drops frames while the page loads, scripts or paints.
- Properties: `transform` and `opacity` (plus `clip-path`); `transform-origin: var(--transform-origin)` at the trigger; percentage `translate()` moves by the element's own size. Never drive a child's transform from a CSS variable on the parent.
- Curves as tokens: `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)`, `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)`, `--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1)`.
- Gestures: Pointer Events with `setPointerCapture`, and a short position and time history for release velocity.
- Gate hover motion with `@media (hover: hover) and (pointer: fine)`, reduced motion with `@media (prefers-reduced-motion: reduce)`, and skip state animation on mount with `initial={false}` on `AnimatePresence`.
- Add `will-change` only after you see first-frame stutter, naming the animated property, never `all`.

Adapted from Emil Kowalski's public animate and apple-design skills (emilkowalski/skills, commit c8a7962) and Jakub Krehel's public better-ui (jakubkrehel/skills, commit 60bf140). See the [Kowalski](../../../references/emil-kowalski-LICENSE.txt) and [Krehel](../../../references/jakub-krehel-LICENSE.txt) licenses.
