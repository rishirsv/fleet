# Interaction and states

Define what the interface does through the user's task, available actions, and
observable outcomes. Motion describes transitions; this reference defines the
behavior and state those transitions communicate.

## Contents

- [Map the task](#map-the-task)
- [Make controls understandable](#make-controls-understandable)
- [Design forms and recovery](#design-forms-and-recovery)
- [Own each state](#own-each-state)
- [Exercise the experience](#exercise-the-experience)
- [Agency and permission timing](#agency-and-permission-timing)
- [Search](#search)

## Map the task

Identify the entry point, main path, completion, and relevant recovery paths.
Reuse the product's navigation and the components or services that manage its
state. Keep similar actions consistent, make the next step predictable, and
preserve location or progress when returning. Use familiar platform controls
unless another treatment improves the actual task.

## Make controls understandable

Match control type to the choice: navigation changes location, buttons perform
actions, selections change values. Give controls persistent, meaningful labels.
By default, give each region where the user makes a choice one visually
dominant action, and put secondary actions behind a menu once there are more
than three. Style secondary and destructive actions according to their
role. State the action and its object when context alone would not make the
outcome clear. Carry essential meaning in visible text or shape so it works
without hover, color, or an unexplained icon.

Before building a custom web select, check whether a semantic select with
progressive styling meets the required behavior.

## Design forms and recovery

Default to a single-column form so labels, fields, and errors follow one
scanning path; use multiple columns only for short, strongly related values when
the reading order remains unmistakable. Let field width suggest the expected
amount of input without constraining valid values.

- **Fields ask for the right keyboard.** Every field declares its content type, keyboard and autofill hint, so an email field brings up the email keyboard and offers saved addresses.
- **Fields accept what people paste.** Take input the way people type or paste it, such as spaces in a card number or brackets in a phone number; strip the formatting in code and show the value cleanly. Never block paste, and trim the trailing space some keyboards add.
- **Enter submits.** Enter submits a form with one field, or from the form's last field. In a multi-line field, Enter adds a line and ⌘ or Ctrl with Enter submits.
- **Forms validate on submit.** Submit stays enabled until the request starts. On submit, show each error beside its field and move to the first one.
- **Busy buttons keep their label.** While its request runs, a button keeps its label, shows an indicator and disables itself.
- **Hotkeys stay out of inputs.** Shortcuts don't fire while a text field or editable element has focus.

Match confirmation or undo to the consequence of an action; routine changes
need neither. Explain the consequences before the user performs the action.

## Own each state

Assign idle, pending, success, empty, error, selected, and disabled states to
the control or region that owns the outcome; not every element needs every
state. Give timely feedback and prevent unintended duplicate actions while work
is pending. Preserve useful content during refresh where possible. When web
feedback changes without navigation, decide whether focus, a field description,
or a live region should communicate it.

An action responds within 400ms or shows feedback straight away, as an
optimistic value, a skeleton or a progress bar. Hold a spinner or skeleton back
150–300ms, then keep it up at least 300–500ms once shown, so it never flashes
for one frame. A skeleton matches the layout it stands in for.

Distinguish first use, no results, and unavailable data: each needs a different
next action. Explain disabled actions when their cause is not apparent. For
optimistic updates, define what happens if the operation fails and how the user
can recover; mark an unconfirmed outcome as pending when correctness matters.

Show warnings where the relevant condition occurs. State the consequence and a
useful next step; present non-blocking context as quieter supporting detail.
Let the current controls communicate routine workflow state; add narration only
when it changes what the user can do or explains how to recover.

## Navigation and overlays

- **Navigation uses the platform's links.** Moving to another place uses a real link or navigation element, so opening in a new tab or window, Back, and sharing a link all work.
- **State survives a reload.** Filters, tabs, pagination and open panels persist, so refresh, sharing and Back keep them: the URL on the web, state restoration and deep links natively.
- **One dialog at a time.** Never open a dialog on top of a dialog. Use a menu, a popover or a new screen.
- **Taps feel native.** Every tappable element has its own pressed state, and a tap fires without waiting to rule out a double tap. On the web, set `-webkit-tap-highlight-color: transparent` once on the root and `touch-action: manipulation` on buttons and links.

## Exercise the experience

For reversible state changes, exercise both directions and check dependent
status, counts, and action eligibility. For example, reopening a required
checklist item must revoke readiness if readiness requires every item to be
complete. Check rapid repeated input and supported input methods.

After a rerender, keep focus on the equivalent control. If that control is
unavailable, move focus to a useful enabled destination; focusing a disabled or
removed trigger leaves keyboard users without a usable position. Verify that
labels, visible state, focus, and underlying behavior agree.

## Agency and permission timing

Let people explore without unnecessary setup. Request personal data at the point
its purpose is apparent; explain why it is needed and ask only for that purpose.
Where a feature could cause concrete harm, address that failure in the
interaction itself.

## Search

Decide what can be searched and where results belong before placing the field.
Use a global entry for app-wide discovery and a field beside a collection for
local filtering. Keep the scope apparent in placement and wording. Distinguish
an exploratory search landing page from immediate text entry.

Provide useful recent queries with removal controls. Keep predictive suggestions
visually distinct from entered text. Give results more prominence than
suggestions. Offer relevant, visible filters; tokens may supplement them. When
there are no results, show the query and a way to change or clear it. Exercise
entry, clearing, cancellation, scope changes, suggestions, filters, results,
and no results.
