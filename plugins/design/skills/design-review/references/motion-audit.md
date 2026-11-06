# Motion audit

Find the motion work with the highest leverage across a product, such as the ease-in that makes every dropdown feel sluggish, the fixed timelines that make toasts jump, or the keyboard action that should never have animated, and turn each into a plan so precise that someone with no context can execute it without taste of their own.

## Rules

1. **Read-only.** Don't modify source code, install, build with side effects or commit. The only files you write are plans, under `plans/` (or `animation-plans/` if `plans/` already exists for something else).
2. **Plans are self-contained.** Never write "use the easing discussed above"; inline the exact curve, duration, file path and code excerpt.
3. **Don't re-litigate settled decisions.** If a design doc or comment documents a deliberate motion trade-off, note it and leave it.

## 1. Recon

Map the motion surface before judging it:

- **Stack**: UI framework, motion libraries and component libraries.
- **Where motion lives**: tokens for curves and durations, animation definitions, animation props and modifiers, gesture handlers.
- **Conventions**: existing curve tokens, duration scales and spring settings. Plans extend these, never invent parallel ones.
- **Personality**: a playful consumer app or a crisp dashboard? Cohesion findings depend on it.
- **Frequency map**: which animated elements are hit 100+ times a day, occasionally, or rarely. This drives severity.

## 2. Audit eight categories

Values come from [Motion](../../design/references/motion.md); cite them, never approximate.

1. **Purpose and frequency.** Animations on keyboard-initiated actions, command palettes with open and close transitions, decorative motion on list items or hover states hit constantly. The strongest fix is often to delete it.
2. **Easing and duration.** Ease-in anywhere, bare ease or linear on entrances, durations over 300ms on UI, and a tooltip delay plus animation on every tooltip in a toolbar (after the first, they should be instant).
3. **Physicality and origin.** Scale from zero, pure-fade entrances with no initial transform, trigger-anchored surfaces growing from their own center (modals are exempt), and pressable elements with no press feedback.
4. **Interruptibility.** Fixed timelines on toasts, toggles and rapidly triggered UI; gesture handlers that tween with fixed durations; drags dismissed on distance alone rather than velocity (about `0.11` points per millisecond); hard stops at drag boundaries instead of rising resistance; symmetric timing on press-and-release.
5. **Performance.** Every property animated, layout properties animated, animation driven through a parent value that recalculates every child, scripted loops doing what declarative animation could, and heavy animated blur (keep it under 20pt).
6. **Preferences.** Movement with no reduced-motion handling, hover motion on touch, and reduced-motion treatments that remove all feedback.
7. **Cohesion and tokens.** One bouncy component in a crisp app, near-identical curves and durations that should be one token, group entrances with no stagger, and cross-fades that visibly double-expose (mask them with a brief `2pt` blur).
8. **Missed opportunities.** State changes that teleport, spatially connected UI with no motion explaining where it came from, and rare high-emotion moments with none of their delight budget. Report at most a handful, grounded in seams you observed.

## 3. Vet and rank

Re-read the cited code for every finding. Reject anything by design, mis-attributed, duplicated or exempt; a long duration on a marketing page can be fine. Never present a finding you haven't confirmed at its location.

Present vetted findings as one numbered table, ordered by leverage (impact ÷ effort), with [severity](../../../references/severity.md):

| # | Severity | Category | Location | Finding | Fix summary |
| --- | --- | --- | --- | --- | --- |

For motion, `HIGH` breaks the feel (wrong easing on UI, animation on keyboard or high-frequency actions, dropped frames, scale from zero); `MEDIUM` is noticeably off (wrong origin, non-interruptible dynamic UI, missing reduced-motion handling); `LOW` is polish (stagger, blur-masked cross-fades, token consolidation). List missed opportunities separately, since they add rather than correct.

## 4. Write plans

One plan per finding the user picks, or the top three to five by leverage when they ask for plans without picking. Two findings that share every file and the same fix pattern may merge into one plan. Number plans `NNN-short-slug.md`, stamp each with the current commit, and keep a `README.md` beside them with the order, dependencies and status of each plan.

```markdown
# NNN — <Short imperative title>

- **Status**: TODO
- **Commit**: <short commit hash when this plan was written>
- **Severity**: HIGH | MEDIUM | LOW
- **Category**: <audit category>
- **Estimated scope**: <n files, rough size>

## Problem

What is wrong, where, and why it matters to how the product feels. Cite every
location as `path/to/file:123` and include the current code verbatim.

## Target

The exact end state. Every value spelled out: curves, durations, spring
settings, preference handling. Never "use a nicer easing".

## Repo conventions to follow

How this codebase already does it, with one exemplar the executor should
imitate (token names, file placement, prop patterns).

## Steps

1. <One concrete edit per step: file, what changes, resulting code.>

## Boundaries

- Do NOT touch <files or components out of scope>.
- Do NOT change structure, only motion properties, unless a step says otherwise.
- Do NOT add new dependencies.
- If a step doesn't match the code you find, STOP and report instead of improvising.

## Verification

- **Feel check**: run the UI, trigger <interaction>, and confirm:
  - <observable check, e.g. "the dropdown grows from its trigger">
  - <e.g. "spamming the toggle never restarts the animation from zero">
  - At 10% playback speed, confirm <detail>.
  - With reduced motion on, movement is gone but opacity feedback remains.
- **Done when**: <eye-checkable completion criteria>.
```

The feel check is not optional. Motion can be mechanically correct and still feel wrong; give whoever executes or reviews the plan concrete things to watch for in slow motion.

A short list of high-confidence, high-leverage plans beats a long padded one; "the motion here is already right" is a valid result. When feel can't be judged from code alone, such as a cross-fade or a spring's bounce, say so and put a feel check in the plan instead of guessing.

Adapted from Emil Kowalski's public improve-animations (emilkowalski/skills, commit c8a7962). See [license](../../../references/emil-kowalski-LICENSE.txt).
