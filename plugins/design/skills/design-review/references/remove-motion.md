# Remove motion

Put every existing animation on trial, then delete or reduce the ones that can't defend themselves. Edits code, but only to subtract. It is the counterpart to the opportunities mode in [motion review](motion-review.md). It does not add motion, and it does not fix easing, origin, or interruptibility on animations that stay (that's a focused motion review).

## Operating Posture

The premise: sometimes the best animation is no animation. Agents add motion by default — fade-in on scroll, hover-scale on cards, animated command palettes — and each one is defensible alone while together they make the product feel slow.

So the burden of proof is reversed. An animation stays only if it passes the gate. "It's already there" and "it looks nice" are not defenses.

Deleting everything is also wrong. Motion that bridges a jarring change — a toast that would otherwise teleport in, a panel that needs to show where it came from — earns its place. Removing it trades a slow interface for a disorienting one.

## Hard Rules

1. **Only subtract.** Every edit deletes an animation, reduces it, or removes code it left orphaned. Never add motion, change an easing curve, or retune a spring. If an animation should stay but is badly built, list it for a focused motion review and leave it untouched.
2. **Check what depends on the animation before deleting it** (see "Removal Hazards"). A removal that leaves an element invisible or breaks unmount timing is a regression, not a cleanup.
3. **Ask before removing a dependency.** Uninstalling a motion library touches the lockfile and other people's work; propose it, don't do it.
4. **Respect documented decisions.** If a comment or design doc explains why a specific animation exists, keep it and note it.

## The Gate

Walk every animation through this tree. Record the branch that decided it — it goes in the report.

```
Is it triggered by the keyboard (shortcut, command palette, focus jump, arrow-key navigation)?
└── Yes → DELETE. Raycast has no open/close animation; that is the optimal experience.

Is it seen 100+ times a day (core navigation, tab switches, list rows, route changes inside the app)?
└── Yes → DELETE. At that frequency any duration reads as delay.

Is it on functional data the user is reading or acting on (charts, tables, numbers, dashboards)?
└── Yes → DELETE, unless it shows a real change in value (e.g. a number ticking from old to new on user action).
          Re-animating on every refresh or mount is decoration.

Can you name its purpose — feedback, spatial consistency, state indication, preventing a jarring change, explanation?
├── No → Is it a rare, first-time moment (onboarding, empty state, success)?
│        ├── Yes → KEEP. This is the delight budget.
│        └── No → DELETE.
└── Yes → Is it seen tens of times a day (hover, frequent toggles, list expansion)?
          ├── Yes → REDUCE to the near-imperceptible version (see "Reducing").
          └── No → Is it over budget (UI animation > 300ms, or a slide/scale where a fade would carry the same meaning)?
                   ├── Yes → REDUCE.
                   └── No → KEEP.
```

Marketing pages get more latitude than product UI: explanation and a single hero entrance can stay. Repeated scroll reveals on every section still fail — the visitor sees them once per section, on every visit, and they hold content back from people who scroll fast.

## Reducing

Reduce means a smaller version of the same motion, never a different animation:

| Today | Reduced to |
| --- | --- |
| Hover with scale, lift, or shadow growth | Color/opacity change only, ≤150ms, `ease` |
| Slide or scale entrance on a frequent surface | Opacity only, 150ms, `ease-out` |
| UI animation over 300ms | 200–250ms, same curve |
| Stagger over 80ms per item, or over 300ms total | Cap at 30ms per item, or drop the stagger and fade the group as one |
| Infinite loop (pulse, shimmer, glow) on a persistent element | Run once, or remove the loop and keep the static end state |

If reducing would leave motion so small it stops carrying its purpose, delete it instead.

## Where to Hunt

Sweep for these — each is a known class of motion that rarely survives the gate:

**Keyboard and high-frequency**
- Command palette, menu, or dialog opened by a shortcut with an enter/exit animation
- Tab switches, segmented controls, and sidebar navigation that slide or crossfade
- Route or page transitions inside the app (not on marketing pages)
- Hover transforms on rows and list items users sweep the cursor across

**Decoration**
- Fade-in-on-scroll on every section or row (on the web: `whileInView`, IntersectionObserver reveal classes, AOS, `animate-fade-in` utilities)
- Hover `scale` or lift on cards that aren't the primary action
- Infinite loops: pulsing badges, gradient orbs, glowing borders, spinning icons that aren't loading indicators
- Staggered entrances on lists the user loads many times a day

**Functional data**
- Charts that redraw from zero every time they appear or refresh
- Numbers that count up when the screen opens rather than on a change
- Table rows that animate in when data loads

**Over-engineering**
- Spinners on operations that resolve in under 300ms — the flash reads as a glitch
- Skeleton shimmer on content that loads in under 300ms
- Transitions on every property (`transition: all` on the web) — delete it and list only the properties that actually need to transition, or none

Search for the animation, transition, repeat and stagger calls the project uses. On the web, grep for `transition`, `animation`, `@keyframes`, `motion.`, `animate={`, `whileInView`, `whileHover`, `AnimatePresence`, `layout`, `stagger`, `infinite`, `animate-`, `IntersectionObserver`, `transition: all`.

## Removal Hazards

Check each of these before deleting. They are why removal is not a find-and-replace:

- **Hidden start states.** An element that rests invisible, offset or scaled down until its animation runs. Delete the animation without deleting the start state and the element stays invisible forever. Always remove the start state with the animation. On the web: keyframes with `animation-fill-mode: forwards` from `opacity: 0`, Motion's `initial={{ opacity: 0 }}`, or a reveal class that starts at `opacity: 0` until an observer fires.
- **Code that waits for the animation.** Completion callbacks and delays sized to a duration. Delete the wait along with the animation, or the UI keeps pausing for motion that no longer exists. On the web: `onAnimationEnd`, `transitionend` listeners, `onExitComplete`, and `setTimeout` calls.
- **Exit animations that delay removal.** A view stays on screen until its exit finishes, and work runs after it. Once the exit is gone the view leaves immediately — move whatever ran after the exit to the point where the view is closed. On the web: `AnimatePresence` and `onExitComplete`.
- **Layout animations hiding a jump.** An animated layout change can be masking a layout shift (on the web, Motion's `layout` prop or a FLIP animation). Remove it and the jump appears. If it does, keep the animation and list the shift as a finding — fixing layout is out of scope.
- **Focus timed after motion.** Focus moved in an animation callback must move immediately once the animation is gone.
- **Tests and selectors.** Tests that wait for animation classes or durations need the same removal.

## Cleanup

After the removals, delete what they orphaned:

- Animation definitions and utilities no longer referenced anywhere
- Animation wrappers and modifiers where no motion remains
- Motion library imports in files that no longer animate
- Animation entries in configuration or token files with zero references

On the web that means `@keyframes`, `motion.div` → `div` where no motion props remain, empty `AnimatePresence` wrappers, unused variants objects and Tailwind config entries.

If the motion library is no longer imported anywhere, say so and propose removing the dependency (Hard Rule 3).

## Workflow

1. **Recon.** Identify the stack, motion libraries, where motion lives (styles, tokens, configuration, component code), and the product's personality — a crisp dashboard keeps less than a playful consumer app. Build a frequency map of the animated surfaces.
2. **Sweep** the hunt list. Done when every hunt class has either yielded candidates with `file:line` evidence or been explicitly cleared.
3. **Gate** every candidate through the tree. Record the deciding branch.
4. **Check hazards** for each Delete and Reduce.
5. **Edit.** Apply the deletions and reductions, then the cleanup.
6. **Verify.** Search for every removed animation, class, and variant name to confirm nothing still references it.
7. **Report** in the format below.

## Required Output Format

### Part 1 — Removed and reduced

One row per change, ordered by how often the user hits it:

| # | Location | Was | Verdict | Deciding branch |
| --- | --- | --- | --- | --- |
| 1 | `CommandMenu.tsx:24` | 200ms scale + fade on open/close | Deleted | Keyboard-triggered |
| 2 | `ProjectCard.tsx:31` | `hover:scale-105` with shadow growth | Reduced → border color, 150ms `ease` | Tens/day hover |
| 3 | `sections/*.tsx` | `whileInView` fade-up on 9 sections | Deleted, `initial` opacity removed | No purpose |

### Part 2 — Kept (REQUIRED)

List 2–5 animations you considered and deliberately kept, each with the purpose that saved it:

- `Toast.tsx:41` — enter from bottom edge. **Kept: prevents a jarring change; occasional frequency.**
- `Onboarding.tsx:88` — success confetti. **Kept: rare, first-time moment.**

Also list animations that stay but are badly built, for a focused motion review (e.g. "`Dropdown.tsx:12` — `ease-in` on enter, kept but should be `ease-out`").

This section is what separates this skill from deleting every transition in the codebase.

### Part 3 — Cleanup and verdict

List orphaned code removed and any dependency you propose dropping. Then one short paragraph: how over-animated the interface was, what it feels like now, and anything that needs a human to check on a real device (hover feel, perceived speed).

Adapted from Emil Kowalski's public remove-animations (emilkowalski/skills, commit c8a7962).
See [license](../../../references/emil-kowalski-LICENSE.txt).
