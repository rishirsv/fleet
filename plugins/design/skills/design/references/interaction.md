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
- [Labels and messages](#labels-and-messages)

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
dominant action. Style secondary and destructive actions according to their
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

Match confirmation or undo to the consequence of an action; routine changes
need neither. Explain the consequences before the user performs the action.

## Own each state

Assign idle, pending, success, empty, error, selected, and disabled states to
the control or region that owns the outcome; not every element needs every
state. Give timely feedback and prevent unintended duplicate actions while work
is pending. Preserve useful content during refresh where possible. When web
feedback changes without navigation, decide whether focus, a field description,
or a live region should communicate it.

Distinguish first use, no results, and unavailable data: each needs a different
next action. Explain disabled actions when their cause is not apparent. For
optimistic updates, define what happens if the operation fails and how the user
can recover; mark an unconfirmed outcome as pending when correctness matters.

Show warnings where the relevant condition occurs. State the consequence and a
useful next step; present non-blocking context as quieter supporting detail.
Let the current controls communicate routine workflow state; add narration only
when it changes what the user can do or explains how to recover.

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

## Labels and messages

Read the copy nearby first and follow the product's voice, terminology, and
localization conventions. Keep one term per concept: if the menu says
"Archive", the toast says "Archive" too. Name things by what the user manages,
not by how the system is built: "Notifications", not "Webhook config". A
deliberate brand voice is a choice; flag a departure from plain language only
when it creates inconsistency, ambiguity, translation risk, or a tone the
stakes don't support. Check every label against the action it invokes and
every error for a stated recovery. Keep persistent information outside empty
states.

For a feature or destination name, start from the audience and the benefit they
seek, try candidates in real navigation and spoken sentences, and prefer a
familiar neutral term when ambiguity would undermine trust. An invented name
works only when its meaning is discoverable in context.
