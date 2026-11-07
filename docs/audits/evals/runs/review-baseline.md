# Atlas Team billing screen: design and front-end review

Source reviewed: `screen.html` (static read of markup, CSS and script; not rendered in a browser).

## Verdict

The screen is not ready to ship. Four problems block real use: the "Manage seats and roles" button is clipped to unreadable text, keyboard and touch users can never reach "Remove", the remove confirmation does not say who is being removed or what it costs, and "Save Changes" fakes a result for a form that has nothing to save. Beyond those, the action hierarchy is noisy (three filled buttons, one of them red for a harmless download), the invoice table hides the information that tells invoices apart, and the motion is slow and starts from the wrong place.

## Blocking issues

### 1. "Manage seats and roles" is clipped

`.btn.fixed { width: 96px; overflow: hidden; white-space: nowrap; }` (line 20) forces a 22-character label into 96px minus 32px of padding, about 64px of text. At 14-16px semibold the visible text is roughly "Manage s", cut with no ellipsis. Users cannot read what the button does.

Fix: remove `.fixed`. Let the button size to its label. If a uniform width is wanted, use `min-width`, never a fixed `width` with `overflow: hidden`.

### 2. "Remove" is unreachable for keyboard and touch users

`.member .remove { visibility: hidden; }` with `.member:hover .remove { visibility: visible; }` (lines 28-29). `visibility: hidden` also removes the button from the tab order, so a keyboard user can never focus it, and there is no hover on touch screens. The column also has no header, so screen reader users get an unlabeled button with no row context ("Remove", "Remove").

Fix: show the button at rest, in a quieter style if needed. If it must be hover-revealed on pointer devices, use `opacity` plus `.member:hover .remove, .member:focus-within .remove { opacity: 1 }`, and keep it always visible under `@media (hover: none)`. Give each button an accessible name, e.g. `aria-label="Remove Jo Park"`.

### 3. The remove confirmation gives no context and uses the wrong styling

The dialog (lines 74-77) says only "Are you sure?" with "Yes" / "No".

- It does not name the member or the consequence. On a billing screen the consequence is the point: does the seat free up, is a prorated credit issued, does the person lose access immediately?
- The confirm button is `primary` blue. A destructive confirm should use the danger style.
- "Yes" / "No" make the user reread the question. Labels should state the action.
- Both buttons only close the dialog (line 88). The removal never happens and nothing records which row was clicked.

Suggested content: title "Remove Jo Park?", body "Jo loses access to the Design team now. The seat is credited, prorated, on your next invoice.", buttons "Remove member" (danger) and "Cancel".

Implementation gaps: no `role="dialog"`/`aria-modal="true"`/`aria-labelledby`, no focus moved into the dialog, no focus trap, no Escape to close, no backdrop click, and focus is not returned to the triggering button. Using the native `<dialog>` element with `showModal()` covers most of this.

### 4. "Save Changes" is fake and the error is unhelpful

- Nothing on the page is editable. There are no inputs, so "Save Changes" and "Discard changes" have nothing to act on. They are always enabled and imply unsaved state that does not exist. Either remove them or tie them to a real dirty state (disabled until something changes).
- The handler alternates between success and failure on each click (`fail = !fail`, line 85). That's placeholder logic shipped as behavior.
- "Oops! Something went wrong." gives no cause and no next step. Say what failed and what to do: "Couldn't save seat changes. Check your connection and try again." with a Retry action.
- Success and error toasts look identical (same dark background, no icon).
- The error disappears after 2.5s. Errors should persist until dismissed or shown inline near the action.
- The toast has no `role="status"` / `aria-live`, so screen readers never announce it.
- `setTimeout` is never cleared. Click twice within 2.5s and the first timer hides the second message early.

## Information architecture and content

- **The plan itself is missing.** The intro promises "Manage your plan, seats and invoices", but the screen shows no current plan, price, seat count (used/total), renewal date or payment method. Those are the first things someone on a billing page looks for. Add a plan summary card at the top and put "Upgrade plan" there.
- **"Upgrade plan" sits under "Billing History"**, a section about past invoices. It belongs to the plan summary.
- **The intro is about 85 words of policy** (proration, annual terms, custom contracts) in one paragraph. Cut to one line, for example "Manage your plan, seats and invoices for the Design team." Move the proration rule next to the seat controls, where it affects a decision, and the custom-contract note to a short footer link ("Need a custom contract? Contact your account manager").
- **Casing is inconsistent.** "Billing History" and "Save Changes" use Title Case; "Team members" and "Discard changes" use sentence case. Pick sentence case throughout.
- **"Download receipt" is ambiguous.** It sits beside "Export invoices" with no indication of which receipt. Receipts belong per row in the invoice table.
- **"Sort by ▾" does not show the current sort**, and choosing an option does nothing (no handlers, no selected state). Use "Sort: Newest" and mark the active option. With two invoices, consider dropping sort until the list is long enough to need it.

## Action hierarchy

- The billing actions row has three filled buttons: two `primary` and one `danger`. That leaves no clear primary action. Use at most one primary per section.
- `danger` red on "Download receipt" is wrong. Downloading is not destructive. Reserve red for removal and cancellation, or users learn to ignore it.
- In the team row the order is ghost, primary, ghost. The primary sits between two secondaries, and "Manage seats and roles" (the main task of the section) looks least important. If save/discard stay, group them as "Discard" then "Save", at the trailing edge.

## Invoice table

- **Truncation hides the distinguishing part.** `.inv-name { max-width: 140px; text-overflow: ellipsis }` shows roughly "INV-2026-0412-des…". Both rows begin with the same prefix and differ only at the end ("annual-renewal-adjustment" vs "seat-change-prorated"), which is exactly what gets cut. There's no `title` or other way to see the full name. Show a human description ("Annual renewal adjustment", "Seat change, prorated") with the invoice number as secondary text, and drop the `.pdf` filename.
- **Rows are not actionable.** You cannot open or download a specific invoice. Make the invoice name a link and add a per-row download.
- **Dates lack a year.** "Apr 12" and "Mar 12" become ambiguous once history spans more than a year. Use "Apr 12, 2026".
- **Amounts are left-aligned.** Right-align the Amount column and use `font-variant-numeric: tabular-nums` so values line up by digit.
- **No status.** Billing history usually needs Paid / Due / Failed.
- **Semantics:** no `<thead>`, no `scope="col"` on headers, no caption or `aria-labelledby` pointing to the section heading. The members table has no header row at all.

## Visual design

- **Nested radii are not concentric.** The outer card has `border-radius: 16px; padding: 8px` and the inner panel also has `16px`. The inner radius should be outer minus padding, so 8px, or the corners look pinched. Better: drop the double surface. A white card containing a near-white (#f7f8fa) panel on a gray (#f4f5f7) page creates three nearly identical grays and adds no grouping.
- **Card shadow is heavy.** `0 4px 16px rgba(0,0,0,.2)` on a light page reads as floating modals. Something like `0 1px 2px rgba(0,0,0,.06), 0 1px 3px rgba(0,0,0,.08)` or a 1px border fits a settings page.
- **Intro text is hard to read.** `font-weight: 300` at 14px is thin on most screens, and `line-height: 1.1` is far too tight for a multi-line paragraph (use about 1.5). It also has no `max-width`, so on wide screens lines run well past a comfortable measure (cap near 65ch).
- **Ghost button borders are too faint.** #ced4da on #f7f8fa is about 1.4:1, below the 3:1 non-text contrast guideline for control boundaries. Darken the border (around #868e96) or give ghost buttons a fill.
- **No hover or focus styles.** Buttons have no hover state. Menu items have no hover or focus highlight, so keyboard users cannot see which item is active. Add `:hover` and `:focus-visible` styles.
- **h2 uses browser default margins**, which vary and leave uneven spacing inside the panel. Set explicit heading sizes and spacing.

## Motion

- **Sort menu opens from the wrong origin, too slowly.** It scales from `scale(0)` around `transform-origin: center` over 600ms `ease-in-out`. A dropdown should grow from its trigger (`transform-origin: top left`), start near full size (`scale(.96)`), and take about 150-200ms with an ease-out curve. At 600ms the menu lags the click noticeably.
- **Hidden menu still takes focus.** With `opacity: 0` and `scale(0)`, its three buttons remain in the tab order and in the accessibility tree. Keyboard users tab into invisible items. Add `visibility: hidden` (transitioned) or `inert` when closed.
- **Menu behavior is incomplete:** no `aria-haspopup`/`aria-expanded` on the trigger, no Escape, no outside-click close, does not close after choosing an option, no arrow-key navigation. The `▾` character will be read aloud by some screen readers; mark it `aria-hidden` or use a CSS/SVG chevron.
- **Button press is exaggerated and laggy.** `:active { transform: scale(0.9) }` is a large shrink for a text button (0.97 is typical), and `transition: all 300ms ease-in` delays the feedback, since ease-in starts slow. Transition only the properties that change (`transform, background-color, box-shadow`) over about 100-150ms ease-out. `all` also animates layout-affecting properties if they ever change.
- **No `prefers-reduced-motion` handling.** Disable the scale effects under `@media (prefers-reduced-motion: reduce)`.

## Responsive behavior

- `.actions` is a non-wrapping flex row. The billing row (four buttons, about 500px) overflows on a 375px phone once you subtract 80px of page padding and 56px of card padding. Add `flex-wrap: wrap`, and reduce `.page` padding on small screens.
- The menu is positioned with a hard-coded `top: 44px`. Use `top: calc(100% + 4px)` so it follows the trigger's actual height. It also has no `z-index`, so later positioned content can cover it.
- Long names like "Aleksandra Wiśniewska-Kowalczyk" wrap acceptably in the table, but on narrow screens the three-column members table and four-column invoice layout need a stacked or scrollable treatment.

## Structure and code

- No `<main>` landmark; wrap `.page` in `<main>`.
- Toast and dialog are toggled via inline `style.display`. Prefer classes or the `hidden` attribute, and native `<dialog>` for the modal.
- `document.getElementById('yes').onclick = document.getElementById('no').onclick = ...` wires confirm and cancel to the same no-op, which hides the missing removal logic. Keep separate handlers and pass the member being removed.

## Priority order

1. Remove the fixed width on "Manage seats and roles".
2. Make "Remove" reachable and labeled; rebuild the confirmation with name, consequence, danger styling and proper dialog behavior.
3. Remove or wire up Save/Discard; replace the alternating fake result with real error handling and an announced, persistent error.
4. Add a plan summary (plan, seats, renewal, payment method) and move "Upgrade plan" into it.
5. Fix the action hierarchy: one primary per section, no red on downloads, per-row invoice downloads.
6. Fix invoice truncation, dates, amount alignment and table semantics.
7. Tighten motion (menu origin, duration, focusability; press feedback; reduced motion).
8. Visual cleanup: single card surface, lighter shadow, readable intro, stronger ghost borders, hover/focus states, wrapping action rows.
