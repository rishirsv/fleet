# Design review: Atlas Team billing (`screen.html`)

**Verdict: Block.** Eight `HIGH` findings. Two of them stop the screen's main jobs. Keyboard and touch users cannot reach "Remove" at all, and pointer users who do reach it get a dialog whose "Yes" removes nothing. Around those sit a red "Download receipt" that reads as destructive, a seat-management button whose label is clipped to a fragment, invoice names cut off with no way to read them, an error toast that offers no recovery, and two animations that run slow and from the wrong origin.

Used design-review, combined design audit (D1 to D5, U1 to U7), with motion review, critique, craft floor, accessibility, UX-copy, scores and severity. The task did not allow a browser, so every finding comes from reading the source plus computed contrast ratios. No rendered captures exist. Coverage gaps are listed at the end.

## Scores

These are based on source inspection only. Each needs a rendered pass to confirm.

| Area | Score | Why |
| --- | --- | --- |
| Layout and hierarchy | 4 | Three filled buttons compete in one toolbar, "Upgrade plan" sits under "Billing History", both sections use card-in-card surfaces, and the page never shows the current plan or seat count |
| Typography | 5 | System sans suits app UI, but the intro is 14px weight 300 at line-height 1.1 with no measure cap, and h2 (24px default) nearly matches h1 (26px) |
| Color | 3 | Danger red fills the safe "Download receipt" action, and two blue primaries sit beside it, all as hex literals with no tokens |
| Interaction and states | 2 | "Remove" cannot be reached by keyboard or touch, its "Yes" does nothing, Sort items do nothing, and the save error has no recovery |
| Motion | 3 | The sort menu grows from scale 0 at its own center over 600ms, and buttons animate `all` properties with ease-in and a 0.9 press |
| Copy | 4 | Errors and confirmations say "Oops! Something went wrong.", "Are you sure?" and "Yes"/"No"; file names stand in for invoice names; casing is mixed |

## Findings

Numbered in rank order. Escalation triggers come first.

### 1. HIGH: "Download receipt" uses the danger style

- **Location:** Billing History toolbar, `<button class="btn danger">Download receipt</button>` (line 46).
- **Evidence:** `.btn.danger { background: #e03131 }`. On this screen red is the only signal for destruction, and downloading a receipt destroys nothing.
- **Impact:** People hesitate before a safe action. The red also trains them to ignore red, which matters on a billing page where "Remove" and plan changes are real risks.
- **Correction:** Make it a secondary (ghost) button. Better, delete the toolbar button and give each invoice row its own download link (see 4), since a toolbar "receipt" names no target.
- **Verify:** Render the toolbar and confirm the danger color appears only on destructive controls.

### 2. HIGH: "Remove" appears only on hover, so keyboard and touch users cannot reach it

- **Location:** Team members rows, `.member .remove { visibility: hidden }` and `.member:hover .remove { visibility: visible }` (lines 28 and 29).
- **Evidence:** `visibility: hidden` takes the button out of the tab order, and there is no `:focus-within` or `(hover: none)` rule. On touch, the first tap can only fire a false hover.
- **Impact:** Keyboard, screen-reader and most touch users cannot remove a member. Pointer users cannot see that the action exists until they hover the right row.
- **Correction:** Show the button at all times (delete the two rules). If the visual weight bothers you, make it a quieter text button rather than hiding it. Give each one a distinct accessible name, for example `aria-label="Remove Jo Park"`.
- **Verify:** Tab through the members table and tap a row at 375px with touch emulation. "Remove" must be visible and reachable in both cases.

### 3. HIGH: The "Manage seats and roles" label is clipped with no ellipsis

- **Location:** Team members actions, `.btn.fixed { width: 96px; overflow: hidden; white-space: nowrap; }` (line 20, used on line 66).
- **Evidence:** A 96px box minus 32px of horizontal padding leaves about 64px for a 22-character label at 16px weight 600. That label needs roughly 170px, so most of it is cut off. This is estimated from the source and not yet rendered.
- **Impact:** The control for seats and roles, a core billing task, shows a fragment like "Manage s" with no ellipsis and no way to read the rest. It will get worse in longer locales.
- **Correction:** Delete `.fixed` so the button sizes to its label. If a width limit is truly needed, use `max-width` and let the label wrap.
- **Verify:** Render at 1440 and 320 and confirm the full label shows. Repeat with a pseudo-localized (about 40% longer) string.

### 4. HIGH: Invoice names are truncated with no way back, and rows cannot be opened

- **Location:** Billing History table, `.inv-name { max-width: 140px; text-overflow: ellipsis; white-space: nowrap }` (line 30).
- **Evidence:** "INV-2026-0412-design-team-annual-renewal-adjustment.pdf" and "INV-2026-0312-design-team-seat-change-prorated.pdf" share a long prefix. End truncation at 140px keeps the shared part and drops the part that says what each invoice is for. There is no `title`, link, or detail view.
- **Impact:** Users cannot tell an annual renewal from a prorated seat change without opening something, and nothing on the row opens.
- **Correction:** Show a readable name and the invoice number instead of the file name, for example "Annual renewal adjustment" with "INV-2026-0412" as secondary text, and let it wrap. Make the name, or a trailing "Download" link, open the PDF. If a file name must show, truncate in the middle.
- **Verify:** Render at 375 and 1440. Both rows must be distinguishable and each must open its own invoice.

### 5. HIGH: The save error offers no recovery, and the toast is unreliable and silent

- **Location:** `#save` handler and `show()` (lines 83 to 85), and `.toast` (line 31).
- **Evidence:**
  - Failure text is "Oops! Something went wrong." It does not say what failed or what to do.
  - Success text is "Saved successfully!"
  - The toast hides after a fixed 2.5s, and each call starts a new `setTimeout` without clearing the old one. Click Save twice within 2.5s and the first timer hides the second message early.
  - The toast has no `role="status"` or `aria-live`, so screen readers never announce it.
  - Save has no pending state.
  - The stub alternates success and failure on every click.
- **Impact:** After a failed save, users don't know whether their changes were kept or how to retry. Screen-reader users get no feedback at all. A message timed to 2.5s fails people who read slowly.
- **Correction:**
  - Failure: "Changes not saved. Check your connection and try again.", with a "Try again" action, kept on screen until dismissed.
  - Success: "Changes saved."
  - Clear the previous timer in `show()`, give the toast `role="status"`, and disable Save while the request runs.
- **Verify:** Trigger both outcomes, then double-click Save. Each message must stay its full time. Check that VoiceOver announces both.

### 6. HIGH: The remove confirmation names no one, does nothing, and lets focus escape

- **Location:** `#dlg` (lines 74 to 77) and its handlers (lines 87 and 88).
- **Evidence:**
  - One shared dialog reads "Are you sure?" with "Yes" (blue primary) and "No".
  - Both buttons just hide the dialog. No member is removed and no feedback appears.
  - The dialog has no `role="dialog"`, `aria-modal` or label.
  - Opening it does not move focus, Escape and backdrop clicks do nothing, and the page behind is not inert, so Tab continues into hidden content.
- **Impact:** A pointer user who clicks "Yes" believes the person was removed when nothing happened. The dialog doesn't say which person or what they lose, which matters most for "Aleksandra Wiśniewska-Kowalczyk", the only Admin listed. Keyboard users cannot work the dialog.
- **Correction:**
  - Use a native `<dialog>` opened with `showModal()`. That provides focus containment, Escape and inertness.
  - Title it "Remove Jo Park from Design?" with the body "They lose access to the team's projects. Their seat is credited on the next invoice." (match the actual billing rule).
  - Label the buttons "Remove member" (danger style) and "Cancel".
  - Wire the confirm button to remove the row and confirm the result, for example "Jo Park removed".
- **Verify:** Remove each member by keyboard only and by pointer. Check the title names the right person and focus returns to a sensible control afterwards.

### 7. HIGH: The sort menu grows from zero at its own center over 600ms

- **Location:** `.menu` (lines 23 and 24).
- **Evidence:** `transform: scale(0); transform-origin: center; transition: transform 600ms ease-in-out, opacity 600ms ease-in-out`. Twice the 300ms UI ceiling, from zero scale, anchored to the menu's own center rather than the "Sort by" trigger, with no reduced-motion rule.
- **Impact:** A dropdown people use often feels sluggish and appears to come from nowhere. Moving the pointer in during the first few hundred milliseconds finds tiny items.
- **Correction:** `transform: scale(0.95)` with opacity 0 when closed. Use `transform-origin: top left` (or the trigger position) and `transition: transform 180ms cubic-bezier(0.23, 1, 0.32, 1), opacity 180ms cubic-bezier(0.23, 1, 0.32, 1)`. Add `@media (prefers-reduced-motion: reduce)` with an opacity-only fade.
- **Verify:** Record open and close at normal speed and at 4x slowdown. Open and close rapidly to check it reverses from where it is.

### 8. HIGH: Button press animates every property with ease-in and a deep scale

- **Location:** `.btn { transition: all 300ms ease-in }` and `.btn:active { transform: scale(0.9) }` (lines 15 and 16), on every button including the menu items' siblings and dialog buttons.
- **Evidence:** Ease-in delays the moment of feedback. 300ms is twice the 100 to 160ms press range. `all` also animates color, shadow and the hover `visibility` toggle. A 0.9 press shrinks the button well past the 0.97 norm. There is no reduced-motion handling.
- **Impact:** Every click on the page feels late and spongy. This is the most frequent interaction on the screen.
- **Correction:** `transition: transform 140ms cubic-bezier(0.23, 1, 0.32, 1)` and `.btn:active { transform: scale(0.97) }`. Drop the scale under `prefers-reduced-motion: reduce`.
- **Verify:** Record a press at normal speed. The press must register on pointer-down, with no visible lag.

### 9. MEDIUM: The closed sort menu stays focusable, and sorting does nothing

- **Location:** `#sortBtn` and `#menu` (lines 47 to 49 and 80 and 81).
- **Evidence:**
  - When closed, the menu is only `scale(0); opacity: 0`, so "Newest", "Oldest" and "Amount" stay in the tab order as invisible buttons.
  - The trigger has no `aria-expanded` or `aria-haspopup`.
  - The menu closes only by clicking the trigger again, not by Escape, an outside click, or choosing an item.
  - Items have no handlers, and the trigger never shows the current sort.
  - "▾" is a Unicode glyph used as an icon, which screen readers may announce.
- **Impact:** Keyboard users tab onto three buttons they cannot see. Everyone picks a sort and sees nothing change, and the open menu covers the table until they find the trigger again.
- **Correction:** For three fixed options, a native `<select>` labelled "Sort" removes most of this code. If the custom menu stays:
  - Hide it with `visibility: hidden` when closed (transition `visibility` with the fade).
  - Toggle `aria-expanded`.
  - Close it on Escape, outside click and selection.
  - Apply the sort and show the choice, for example "Sort: Newest".
  - Replace "▾" with an icon from the product's set, marked `aria-hidden`.
- **Verify:** Tab past the closed menu. Choose each option and confirm the table order changes.

### 10. MEDIUM: Actions are misgrouped and the page lacks the billing facts it promises

- **Location:** Both cards (lines 41 to 70).
- **Evidence:**
  - The intro promises "plan, seats and invoices", yet the screen never states the current plan, seat count, price, renewal date or payment method.
  - "Upgrade plan" sits in "Billing History".
  - That toolbar fills three buttons, two blue and one red, with no single starting point.
  - "Save Changes" and "Discard changes" sit under a members table that has nothing to edit.
  - "Export invoices" and "Download receipt" overlap without explanation.
- **Impact:** An admin who arrives to check what they pay or to add a seat finds no answer, and the eye has nowhere to land first. The Save/Discard pair suggests there are unsaved edits that cannot exist.
- **Correction:**
  - Add a plan summary at the top: plan name, seats used of total, next invoice amount and date, with "Upgrade plan" as the page's single filled action.
  - Keep invoice actions with the invoice table and make "Export invoices" secondary.
  - Remove Save and Discard until the section has editable fields (for example a role select per member). Then keep one filled "Save changes".
- **Verify:** Render at 1440 and 375 and confirm one filled action per region and a plan summary in the first view.

### 11. MEDIUM: The intro paragraph is long, light, tightly leaded and uncapped in width

- **Location:** `.intro` (line 12) and its copy (line 39).
- **Evidence:** 14px at `font-weight: 300` (below the 400 minimum under 18px) and `line-height: 1.1` (wrapping text needs at least 1.4). There is no `max-width`, so at 1440 lines run far past 75 characters. The paragraph is four sentences of proration and contract policy. Contrast is fine at 9.4:1, so the problem is weight, leading and length, not color.
- **Impact:** The densest text on the page is the hardest to read and pushes the actual content down. Most of it explains rules that matter only at the moment of adding seats.
- **Correction:** Cut it to one line, or none. Move the proration rule next to seat management ("Added seats are prorated to your renewal date") and the account-manager note to a "Contact sales" link. If it stays: weight 400, line-height 1.5, `max-width: 65ch`.
- **Verify:** Render at 1440 and check line length and the first view.

### 12. MEDIUM: Missing table, button and landmark semantics

- **Location:** Both tables, Remove buttons, page structure.
- **Evidence:**
  - Header cells are `<th>` but have no `<thead>` or `scope`.
  - The members table has no header row at all.
  - Both Remove buttons share the accessible name "Remove".
  - Content is not inside `<main>`.
- **Impact:** Screen-reader users hear unlabeled columns in the members table and two identical "Remove" buttons with no indication of whom they affect.
- **Correction:** Add `<thead>` with `<th scope="col">` (Member, Role, and a visually hidden "Actions"), per-row accessible names (see 2), and wrap the page in `<main>`.
- **Verify:** VoiceOver table navigation in both tables.

### 13. MEDIUM: Both sections use card-in-card surfaces with mismatched radii and a heavy shadow

- **Location:** `.card` and `.card .inner` (lines 13 and 14).
- **Evidence:** A white 16px-radius card with 8px padding wraps a gray 16px-radius card. The craft floor bans nested cards. Concentric radii would need 24px outside. The outer surface uses a single `0 4px 16px rgba(0,0,0,.2)` shadow. The white card against the `#f4f5f7` page is only 1.09:1, so the heavy shadow does all the separating.
- **Impact:** Two frames per section add visual noise and make the corners look slightly off. This repeats across the whole page.
- **Correction:** Delete `.inner` and use one surface per section: white, 12 to 16px radius, about 20px padding, and a light layered shadow or a 1px ring. Move each section's `h2` to sit directly on that surface.
- **Verify:** Render at 2x and inspect corners and edges.

### 14. LOW: Heading scale, numeric alignment and casing slips

- **Location:** `h1`/`h2`, Amount column, labels.
- **Evidence:**
  - `h2` falls back to the browser default (about 24px bold) against a 26px `h1`, so the levels barely differ.
  - Amounts are left-aligned without `font-variant-numeric: tabular-nums`.
  - Currency and dates are hard-coded strings ("$4,320.00", "Apr 12", no year).
  - "Billing History" and "Save Changes" use title case beside "Team members" and "Discard changes".
- **Impact:** Weak heading contrast, harder amount comparison, and dates that become ambiguous across years.
- **Correction:** Set `h2` to about 18 to 20px weight 600. Right-align and tabular-align the Amount column. Format with `Intl.NumberFormat` and `Intl.DateTimeFormat` (for example "Apr 12, 2026"). Use sentence case: "Billing history", "Save changes".
- **Verify:** Render the tables at 1440.

### 15. MEDIUM, unverified: The toolbar and dialog likely overflow on small screens

- **Location:** `.page { padding: 32px 40px }`, `.actions { display: flex }` with no `flex-wrap`, `.dialog { width: 320px }`.
- **Evidence:** The Billing History toolbar holds four buttons of roughly 520px total with no wrap. At 320 the content box is 240px, so it should overflow sideways. The 320px dialog would also meet the screen edges. There are no media queries. This is reasoned from code only.
- **Impact:** If it renders as expected, the page scrolls sideways on phones and buttons get cut off.
- **Correction:** `flex-wrap: wrap` on `.actions`. Use smaller page padding under about 600px (16px). Use `width: min(320px, 100% - 32px)` on the dialog.
- **Verify:** Run the viewport sweep (320, 375, 768, 1024, 1440, 812x375) with `overflow.js`.

## What works

- Section names are plain and task-shaped ("Team billing", "Team members"), and the screen's purpose is clear from the title.
- Focus outlines are left at the browser default rather than removed, so once controls are reachable they show focus. Keep this when restyling buttons.
- Removal already has a confirmation step. Fix its copy and behavior rather than deleting it.
- Text contrast is strong: body text 15.7:1, intro 9.4:1, white on primary 5.67:1.
- `lang="en"` and the viewport meta are set, and the system font stack suits a product tool.

## Accessibility detail

**Color contrast** (computed from source values, WCAG 2.1 formula)

| Element | Foreground | Background | Ratio | Required | Result |
| --- | --- | --- | --- | --- | --- |
| Body and table text | #1c1e21 | #f7f8fa | 15.72:1 | 4.5:1 | Pass |
| Intro text | #3d4148 | #f4f5f7 | 9.4:1 | 4.5:1 | Pass (weight 300 still a typography issue) |
| Primary button label | #ffffff | #3b5bdb | 5.67:1 | 4.5:1 | Pass |
| Danger button label | #ffffff | #e03131 | 4.51:1 | 4.5:1 | Pass, with no margin |
| Toast text | #ffffff | #1c1e21 | 16.71:1 | 4.5:1 | Pass |
| Ghost button ring | #ced4da | #f7f8fa | 1.41:1 | 3:1 advisory | The label identifies the control, so 1.4.11 is not failed, but the edge barely shows |

**Keyboard** (from source; not exercised)

| Element | Tab order | Enter/Space | Escape |
| --- | --- | --- | --- |
| Toolbar buttons | Reachable | Native button | n/a |
| Sort menu items | Reachable even when closed and invisible | No handler | Does not close |
| Remove buttons | Not reachable (`visibility: hidden`) | n/a | n/a |
| Dialog | Focus not moved or contained | Closes only | Does nothing |

**Screen reader** (from source; not tested with assistive technology)

| Element | Likely announcement | Issue |
| --- | --- | --- |
| Sort trigger | "Sort by, down-pointing small triangle, button" | Glyph read aloud, no expanded state |
| Remove buttons | "Remove, button" twice | No member named |
| Dialog | Plain text, not announced as a dialog | No role or label |
| Toast | Silent | No live region |

Target size (2.5.5, AAA advisory): buttons are about 37px tall, below the 44px advisory. Not an AA failure.

## Copy alternatives

| Element | Current | Recommended |
| --- | --- | --- |
| Save error | "Oops! Something went wrong." | "Changes not saved. Check your connection and try again." |
| Save success | "Saved successfully!" | "Changes saved" |
| Remove dialog title | "Are you sure?" | "Remove Jo Park from Design?" |
| Remove dialog buttons | "Yes" / "No" | "Remove member" / "Cancel" |
| Section heading | "Billing History" | "Billing history" |
| Save button | "Save Changes" | "Save changes" |
| Invoice names | File names ending ".pdf" | "Annual renewal adjustment" with "INV-2026-0412" |

**Localization notes:** The fixed 96px button and the 140px invoice column will break first in German or French. Format currency and dates with `Intl`. The dialog title needs one message with a `{name}` placeholder, not concatenation. Wrap member names in `<bdi>` for mixed-direction safety.

## Coverage

- **Inspected:** The full source of `screen.html`, including CSS, markup and script, and contrast ratios computed from its color literals.
- **Not inspected:**
  - Any rendered capture. No browser was allowed, so every appearance claim (clipping widths, overflow, visual weight, alignment) is inferred from source.
  - The viewport sweep and alignment measurement.
  - Keyboard and screen-reader runs.
  - Motion frames and performance traces.
  - Dark theme (none defined) and reduced-motion behavior.
  - Loading, empty (no invoices, one member) and real error states, which this static screen does not implement.
- **Context:** No Atlas design system or tokens were supplied, so consistency is judged within this screen only.

**Verdict: Block.** Findings 1 to 8 are `HIGH` and must be fixed before shipping. This covers source-level review only. Rendered appearance, the viewport sweep, assistive-technology behavior and motion feel were not reviewed.
