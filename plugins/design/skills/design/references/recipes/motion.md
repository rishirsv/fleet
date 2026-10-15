# Motion recipes

Web treatments to use within the project's established motion system. Use the
project's existing Motion package (`motion/react` or `framer-motion`, never
both import paths) for the Motion examples. Every treatment needs a
reduced-motion path that shows the final state immediately, and native controls
keep platform motion.

## Contents

- [Small state transition](#small-state-transition)
- [Storyboard a sequence](#storyboard-a-sequence)
- [Scripted motion lifecycle](#scripted-motion-lifecycle)
- [Scale on press](#scale-on-press)
- [Skip animation on first render](#skip-animation-on-first-render)
- [Popover transform origin](#popover-transform-origin)
- [Tooltip group timing](#tooltip-group-timing)
- [CSS entry with @starting-style](#css-entry-with-starting-style)
- [Staged entrance](#staged-entrance)
- [Exit animation](#exit-animation)
- [Icon swap](#icon-swap)
- [Inspect motion](#inspect-motion)

## Small state transition

```css
.disclosure-icon {
  transition: transform 180ms cubic-bezier(0.2, 0, 0, 1);
}

.disclosure-button[aria-expanded="true"] .disclosure-icon {
  transform: rotate(180deg);
}
```

Drive `aria-expanded` and panel visibility from the same state. The icon
transition reverses naturally on a second toggle. Keep panel semantics, focus,
and content available immediately, independent of the icon's transition.

## Storyboard a sequence

For a sequence with meaningful stages, keep a short description near its timing
configuration:

```text
Trigger: user opens the result preview.
1. Preview surface appears from its trigger.
2. Result becomes visible as the surface settles.
3. Supporting details enter together; primary actions are already usable.
Interruption: closing cancels pending entrances and returns toward the trigger.
Reduced motion: show the complete preview immediately.
```

Name values by role, such as `surfaceEnter`, `detailsDelay`, and
`travelDistance`. Use one component or controller to manage sequencing and
cancellation, and derive appearance from current state instead of independent
flags.

## Scripted motion lifecycle

When CSS cannot express the sequence, an animation can complete after the user
has requested a different state. Check that the completing animation still
belongs to the active transition before it hides content or removes an element.
`transitionend` may not fire when a transition is removed, so give cleanup
another path too.

## Scale on press

A subtle scale-down on press gives buttons tactile feedback. Use `scale(0.96)`
and keep it at or above `0.95`. CSS transitions let a release mid-press return
smoothly. Apply it only to buttons that benefit, and reuse an existing variant
to turn it off.

```css
.button {
  transition-property: scale;
  transition-duration: 150ms;
  transition-timing-function: ease-out;
}

.button:active:not(:disabled) {
  scale: 0.96;
}
```

```tsx
// Motion
<motion.button whileTap={{ scale: 0.96 }}>Click me</motion.button>
```

## Skip animation on first render

Use `initial={false}` on `AnimatePresence` when a stateful component should show
its default state on page load and animate only on later state changes: icon
swaps, toggles, tabs, and segmented controls. The [icon swap](#icon-swap) shows
it in use.

Keep the default where the component relies on `initial` for a first-time
entrance, such as a staggered page hero or a loading state; `initial={false}`
would skip the whole entrance. Check the component on a full page refresh.

## Popover transform origin

Scale a popover from its trigger with the component library's transform-origin
API. Keep `transform-origin: center` for centered modals, which are anchored to
the viewport.

```css
/* Base UI; other libraries expose a different variable */
.popover {
  transform-origin: var(--transform-origin);
}
```

## Tooltip group timing

Tooltips delay before appearing to prevent accidental activation. Once one is
open, adjacent tooltips open instantly with no animation. Use the library's
tooltip-group API, keep content available to keyboard users, and keep
essential meaning out of tooltips.

```css
.tooltip {
  transition: transform 125ms ease-out, opacity 125ms ease-out;
  transform-origin: var(--transform-origin);
}

.tooltip[data-starting-style],
.tooltip[data-ending-style] {
  opacity: 0;
  transform: scale(0.97);
}

/* Skip animation on subsequent tooltips */
.tooltip[data-instant] {
  transition-duration: 0ms;
}
```

## CSS entry with @starting-style

Animate entry without JavaScript when the supported browsers allow it. Manage
exit and focus separately.

```css
.toast {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 400ms ease, transform 400ms ease;

  @starting-style {
    opacity: 0;
    transform: translateY(100%);
  }
}
```

Where support is missing, set a `data-mounted` attribute after the first render
and transition from the unmounted styles.

## Staged entrance

Use for infrequent entrances where sequence communicates hierarchy: the first
load of a page hero, a success state, an empty state.

Split the content into logical groups (title, description, actions) and stagger
them about 100ms apart. Titles can stagger individual words about 80ms apart.
Combine `opacity`, `blur`, and `translateY`.

```tsx
const item = {
  hidden: { opacity: 0, y: 12, filter: "blur(4px)" },
  visible: { opacity: 1, y: 0, filter: "blur(0px)" },
};

function PageHeader() {
  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={{ visible: { transition: { staggerChildren: 0.1 } } }}
    >
      <motion.h1 variants={item}>Welcome</motion.h1>
      <motion.p variants={item}>A description of the page.</motion.p>
      <motion.div variants={item}>
        <Button>Get started</Button>
      </motion.div>
    </motion.div>
  );
}
```

## Exit animation

```tsx
// Default: a small fixed offset indicates direction
<motion.div
  exit={{ opacity: 0, y: -12, filter: "blur(4px)", transition: { duration: 0.15, ease: "easeOut" } }}
>
  {content}
</motion.div>

// When spatial context matters (a card returning to a list, a drawer closing)
<motion.div exit={{ opacity: 0, x: "-100%", transition: { duration: 0.2, ease: "easeOut" } }}>
  {content}
</motion.div>
```

When the exit adds no context, remove the element immediately.

## Icon swap

Use when animation helps communicate an icon state change. Check `package.json`
and nearby imports: with Motion installed, use the Motion version; otherwise use
the CSS version and add no dependency. The `0.25` scale, `4px` blur, and zero
bounce suit glyphs; tune larger surfaces separately.

The example shows a toggle: keep its label stable and expose state with
`aria-pressed`. For a changing action such as Play/Pause, name the next action
and omit `aria-pressed`; for disclosure, use `aria-expanded`. Connect the button
event to the component or service that owns the state.

```tsx
// Motion
import { AnimatePresence, motion } from "motion/react";

function IconButton({ isActive, ActiveIcon, InactiveIcon, label }) {
  const Icon = isActive ? ActiveIcon : InactiveIcon;
  return (
    <button type="button" aria-label={label} aria-pressed={isActive}
      className="relative inline-flex items-center justify-center">
      <AnimatePresence initial={false} mode="popLayout">
        <motion.span
          className="inline-flex"
          aria-hidden="true"
          key={isActive ? "active" : "inactive"}
          initial={{ opacity: 0, scale: 0.25, filter: "blur(4px)" }}
          animate={{ opacity: 1, scale: 1, filter: "blur(0px)" }}
          exit={{ opacity: 0, scale: 0.25, filter: "blur(4px)" }}
          transition={{ type: "spring", duration: 0.3, bounce: 0 }}
        >
          <Icon />
        </motion.span>
      </AnimatePresence>
    </button>
  );
}
```

For the CSS version, keep both glyphs mounted and cross-fade them so enter and
exit both animate: leave the inactive glyph in flow to set the layout size,
overlay the active glyph with absolute positioning, and transition `opacity`,
`scale`, and `filter` on both with the same values.

## Inspect motion

When continuity is unclear, play the animation at 2–5x its duration or slow it
in the browser's animation inspector, and step frame by frame where the tool
allows. Check that:

- Colors transition smoothly without two distinct states overlapping.
- Easing accelerates and decelerates as intended.
- The element scales from the correct transform origin.
- Opacity, transform, and color stay in sync.

Then judge responsiveness at normal speed. Test touch interactions such as
drawers and swipes on a physical device: load the local dev server by IP
address and use Safari remote devtools. Report the gap when no device is
available.
