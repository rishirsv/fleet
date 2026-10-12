# Accessible interaction recipes

Web patterns for focus, keyboard behavior, dialogs, hit areas, form feedback,
announcements, and drag input. Prefer native elements and the project's
established accessible components; use these when building or fixing custom
behavior. Native platforms use their own focus and gesture facilities.

## Contents

- [Focus styles](#focus-styles)
- [Composite keyboard behavior](#composite-keyboard-behavior)
- [Dialog focus](#dialog-focus)
- [Hit areas](#hit-areas)
- [Form feedback](#form-feedback)
- [Announce dynamic changes](#announce-dynamic-changes)
- [Drag input](#drag-input)

## Focus styles

Use `:focus-visible` for a custom focus indicator and let browser heuristics
decide when it shows, including on text fields focused with a pointer. When you
remove an outline with `outline: none` or `focus:outline-none`, provide a
visible replacement.

Prefer the browser's own indicator, which adapts to platform and forced colors;
adding only `outline-offset` keeps it. A custom `outline: 2px solid` with no
color renders `currentColor`, which can fail where the ring crosses other
colors.

```css
/* Best: keep the browser ring, give it breathing room */
:focus-visible {
  outline-offset: 2px;
}

/* Custom ring when the design requires one: use a verified token */
:focus-visible {
  outline: 2px solid var(--focus-ring);
  outline-offset: 2px;
}
```

```tsx
<button className="focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--focus-ring)]">
  Save
</button>
```

A custom indicator must meet the project's or WCAG's target for visible area and
change of contrast. Check the whole perimeter against every adjacent color it
crosses: component fills, page surfaces, images, gradients, and hover and
selected states.

In `forced-colors: active`, keep the default color adjustment or name a system
color such as `Highlight`. `forced-color-adjust: none` freezes the authored
color; use it only where you have checked the control stays perceivable. Use
`:focus-within` when a wrapper should show focus for an inner input, such as a
search box with an icon inside its border.

## Composite keyboard behavior

Custom widgets must implement the keyboard model of their role; an element with
`role="tab"` must provide the full tab model.

With roving tabindex, give the current item `tabindex="0"` and the rest
`tabindex="-1"`. Arrow keys move focus within the widget and transfer
`tabindex="0"`; Tab moves between widgets. Keep focus and selection separate
when activation is manual.

For tabs, connect each `role="tab"` to its `role="tabpanel"` with IDs,
`aria-controls`, and `aria-labelledby`. Activate automatically when panels
render instantly; when switching is expensive, activate with Enter or Space.
Match arrow handling to orientation and leave page-scroll keys available. Make
the panel focusable when it has no focusable content at its start.

Use the matching ARIA APG pattern for a menu, combobox, listbox, or toolbar;
their selection and focus models differ. Use native buttons with `aria-expanded`
for disclosure headers. Fix source order instead of using positive `tabindex`.

## Dialog focus

Prefer native `<dialog>` with `showModal()` or an established accessible dialog.
For a custom modal, make background content inert, give the dialog an accessible
name, and keep focus inside while it is open.

Choose initial focus for the task: a heading or introductory block with
`tabindex="-1"` for long content, the least destructive action for an
irreversible confirmation, or the relevant control for a short task. On close,
return focus to the trigger, or to a logical next location if the trigger is
gone. Escape dismisses only the topmost dismissible overlay. Exercise opening,
Tab and Shift+Tab at both ends, dismissal, and restoration.

## Hit areas

WCAG 2.5.8 Level AA requires a 24×24 CSS-pixel target or one of its exceptions:
spacing, equivalent control, inline, user agent, or essential. Check the
exceptions and the clickable extent before reporting a small visible glyph as a
failure. Use larger targets where space permits; 44 CSS pixels is a useful web
touch starting point, subject to the project's standard.

Under the spacing exception, an undersized target passes when a 24px circle
centered on its bounding box intersects no other target and no other undersized
target's circle. In the simple case, 20px targets need a 4px gap.

Anything that looks clickable must respond across its whole visual extent. A
checkbox and its label share one target. When the visible element is smaller,
extend the hit area with a pseudo-element on the wrapping `<label>` or
`<button>`; replaced elements such as `<input>` do not render `::before` or
`::after` reliably.

```css
.checkbox-label {
  position: relative;
  display: inline-grid;
  place-items: center;
  width: 20px;
  height: 20px;
}

.checkbox-label::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%; /* physical centering: direction-independent */
  transform: translate(-50%, -50%);
  width: 44px;
  height: 44px;
}
```

```tsx
<button type="button" aria-label="Confirm selection" className="relative size-5 after:absolute after:top-1/2 after:left-1/2 after:size-11 after:-translate-1/2">
  <CheckIcon aria-hidden="true" />
</button>
```

When the layout has room, enlarge the real box instead, so scrolling and
gestures use that geometry:

```css
.icon-button {
  min-width: 44px;
  min-height: 44px;
  display: inline-grid;
  place-items: center;
}
```

Where an extended area overlaps another control, shrink it to the largest size
that does not collide. If that loses the needed size, add layout spacing or give
the control a real larger box. Verify the edges activate the intended control,
including where ancestors clip overflow.

A decorative layer over interactive content (a scrim, glow, sheen, or
full-bleed `::after`) intercepts pointer events in its box, and enlarging the
control's hit area does not fix that. Give the layer `pointer-events: none`
(Tailwind `pointer-events-none`), add `aria-hidden="true"` on decorative DOM
elements, and keep pseudo-element content empty. A scrim that dismisses on
click is a control and keeps its pointer events.

```css
.card-glow {
  position: absolute;
  inset: 0;
  pointer-events: none;
}
```

## Form feedback

```html
<label for="email">Email</label>
<input
  id="email"
  type="email"
  autocomplete="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error">Enter a valid email address.</p>
```

- Set `aria-invalid="true"` on the failing field and remove it when the value
  is valid.
- `aria-describedby` makes screen readers announce the inline error with the
  field. Keep existing hint IDs in it when adding an error.
- Show errors inline beside their fields with an icon or text in addition to
  any red border.
- On failed submission, focus the first invalid field, or an error summary
  linked to the fields when the form needs an overview.

Use `autocomplete` with a meaningful `name` for recognized personal data:

| Field | `autocomplete` |
| --- | --- |
| Name | `name` (or `given-name` / `family-name`) |
| Email | `email` |
| Phone | `tel` |
| Address | `street-address`, `address-line1`, `postal-code`, `country` |
| Card | `cc-number`, `cc-exp`, `cc-csc`, `cc-name` |
| Login | `username`, `current-password` |
| Signup or reset | `new-password` |
| 2FA code | `one-time-code` |

Distinguish shipping and billing: `autocomplete="shipping street-address"`.

Correct `type` and `inputmode` select the right mobile keyboard:

| Input | Use |
| --- | --- |
| Email, URL, phone | `type="email"`, `type="url"`, `type="tel"` |
| OTP, PIN, card number | `type="text" inputmode="numeric"` (text semantics, no spinner) |
| Money, decimals | `type="text" inputmode="decimal"` |
| True numeric quantity | `type="number"` |

Set `spellcheck="false"` on emails, codes, and usernames. For password managers
and 2FA autofill, use a real `<form>`, real inputs, and correct `autocomplete`
values. Preserve passwords and other exact values; normalize whitespace only
where the field's meaning permits.

## Announce dynamic changes

For feedback that updates without navigation, use the first match:

1. **Focus moves to the updated content**, such as an opened modal or the first
   invalid field. Its accessible name and description carry the announcement;
   leave the live region out.
2. **The update belongs to a control**, such as a field error or character
   count. Reference it with `aria-describedby`. If it must be heard while focus
   is elsewhere, add a concise live update.
3. **The update is non-urgent and belongs to no control**, such as a toast,
   "Saved", a result count, or loading. Use `role="status"`.
4. **The update is urgent and belongs to no control**, such as impending
   session expiry. Use `role="alert"`.

| Mechanism | Politeness | Use for |
| --- | --- | --- |
| `role="status"` (= `aria-live="polite"` + `aria-atomic="true"`) | Waits for a pause | Toasts, "Saved", result counts, loading updates |
| `role="alert"` (= `aria-live="assertive"` + `aria-atomic="true"`) | Interrupts immediately | Errors and urgent problems only |

- Render a polite region empty from the start and change its text later;
  inserting a new region with its content is announced inconsistently.
- Inserted `role="alert"` content is usually announced, but behavior varies.
  Test the target browser and screen-reader pairs.
- Default to polite. Assertive interrupts whatever the user was reading.
- Keep messages short and self-contained; `aria-atomic="true"` rereads the whole
  region.
- Leave focus where the user is working when a toast appears. Give toasts a
  generous timeout or a dismiss button, and keep every action reachable outside
  an auto-dismissing toast.

```tsx
<div role="status" className="sr-only">
  {statusMessage}
</div>
```

For loading, set `aria-busy="true"` on the updating content and clear it when
done; keep any progress status region outside that subtree. Announce meaningful
outcomes ("Loaded, 12 results") and combine rapid search updates into one
announcement. Verify with the supported browser and screen reader; DOM
attributes alone do not show what was spoken.

## Drag input

Reuse the component's gesture system when it already provides these behaviors.

- Capture the initiating pointer on the element when dragging starts, so the
  drag continues outside its bounds.
- Track that pointer's identity and ignore additional touch points; switching
  fingers mid-drag otherwise makes the element jump.
- Handle pointer cancellation and lost capture as well as release. Clear
  transient drag state and commit no accidental action.
- Preserve page scrolling on unused axes.
- Provide a keyboard action or control for any essential drag action.

```js
function onPress() {
  if (isDragging) return;
  // Start drag...
}
```

Exercise leaving the bounds, a second finger, cancellation, and a new drag after
cancellation.
