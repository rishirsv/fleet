# $design UX copy

Read [Workflow guidance](workflows-guide.md) for evidence, output formats, tool availability, and authorization before applying this workflow.

> If you see unfamiliar placeholders or need to check which tools are connected, see [tools.md](tools.md).

Write or review UX copy for any interface context.

## Usage

```
$design UX copy <target and instructions>
```

## What I Need From You

- **Context**: What screen, flow, or feature?
- **User state**: What is the user trying to do? How are they feeling?
- **Tone**: Formal, friendly, playful, reassuring?
- **Constraints**: Character limits, platform guidelines?

## Principles

1. **Clear**: Say exactly what you mean. No jargon, no ambiguity.
2. **Concise**: Use the fewest words that convey the full meaning.
3. **Consistent**: Same terms for the same things everywhere.
4. **Useful**: Every word should help the user accomplish their goal.
5. **Human**: Write like a helpful person, not a robot.

A deliberate brand voice is not a defect. Raise a departure from plain language only when it creates inconsistency, ambiguity, translation risk or a tone the stakes don't support. Rewording that merely suits your taste is not a finding.

## Inventory the existing strings first

Before writing or reviewing, find where the copy lives and read the copy around the change:

1. Find the string catalog or locale files and the call that reads them: a String Catalog or `.strings` file on Apple platforms; `t(`, `i18n.`, `<FormattedMessage` or `$t(` with `locales/**/*.json`, `messages/*.json` or `*.po` on the web. Copy may also come from a CMS or the API.
2. List the noun used for each object and the verb used for each action, as in "project" or "workspace" and "Delete" or "Remove".
3. Note any voice or content style guide.

New copy uses the terms on that list. A synonym is a finding only where the same thing is named two ways.

## One voice, one vocabulary

The product has one voice and its existing copy establishes it. A local edit does not get to invent a new one. If it's "Archive" in the menu, it isn't "Move to storage" in the toast. Name things by what the user manages, not by how the system is built: "Notifications", not "Webhook config".

A multi-step flow uses one vocabulary throughout: "Get started" to enter, either "Continue" or "Next" to advance, "Done" to finish. Tone flexes with the stakes:

| Context | Tone |
| --- | --- |
| Success, onboarding, empty states | Warm, can be light |
| Routine actions, settings | Neutral, minimal |
| Errors, destructive confirmations | Calm, plain, zero playfulness |
| Data loss, security | Serious, explicit |

## Address the reader directly

In instructional copy, write "you", not "the user". In errors, "we" reads as deflection, so prefer "Unable to load content. Check your connection and try again." An established first-person voice can stay in low-stakes copy where it still reads clearly.

Use possessives sparingly: "Favorites" beats "Your favorites". Never mix perspectives in one flow, such as "My account" beside "Your settings".

## Plain words, fewest words

Choose words a tired reader gets on the first pass, and delete every word that does no work. No idioms, no colloquialisms and no humor that won't translate.

- Use as few words as still say what happens: "Start download" on a download screen is just "Start".
- Show a number on its own when the context already names the noun: "12", not "12 items", in a column headed Items.
- Show a thing's display name, never its id or an internal acronym: "Instagram", not `instagram_graph`; "Product page", not "PDP".
- Skip unnecessary gender: "Subscribers can post recipes", not "each subscriber can post his or her recipes".
- Match the input device: "tap" on touch, "click" with a pointer, "select" when both are possible.

## Build strings whole

Never assemble a sentence from fragments around a variable (`"You have " + n + " new messages"`), because word order changes per language. Write one message with placeholders, and use the locale's plural rules rather than `n === 1 ? "" : "s"`; many languages have more than two plural forms. Never hand-build a number, date, currency or list; format them with the user's locale.

On Apple platforms, String Catalogs carry the plural variants and the system formatters handle numbers, dates and lists. On the web, write one ICU message per sentence and format with `Intl`:

```text
inbox.count = {count, plural,
  =0 {No new messages}
  one {# new message}
  other {# new messages}
}
invite.sent = {name} invited you to {project}
```

| Value | Call | `en-US` output |
| --- | --- | --- |
| Currency | `new Intl.NumberFormat(locale, { style: "currency", currency: "EUR" })` | `€4,320.00` |
| Unit | `new Intl.NumberFormat(locale, { style: "unit", unit: "megabyte" })` | `12 MB` |
| Date | `new Intl.DateTimeFormat(locale, { dateStyle: "medium" })` | `Jun 30, 2026` |
| Relative time | `new Intl.RelativeTimeFormat(locale, { numeric: "auto" }).format(-1, "day")` | `yesterday` |
| List | `new Intl.ListFormat(locale, { type: "conjunction" })` | `Ana, Ben, and Cy` |

## Verb-first buttons

A button label starts with a verb naming the action and, where useful, what it acts on: "Send", "Save draft", "Delete project", "Start free trial". Never "OK!", "Submit" or "Let's go!". Match the outcome to the label. An icon-only button's accessible name follows the same rule: "Delete project", never "Trash icon".

## Links describe their destination

Link text makes sense out of context: "Read the billing docs", never "Click here". A bare "Learn more" breaks down as soon as two appear on one page; suffix each one: "Learn more about exports".

## Sentence case everywhere

Buttons, menu items, tabs, headings, titles and setting names use sentence case: capitalize the first word and proper nouns only. "Save Changes" beside "Discard changes" reads as sloppiness.

## Settings describe the ON state

Label a toggle for what happens when it is on. "Send read receipts" lets users infer the off state; "Don't send read receipts" turns the toggle into a double negative.

Link straight to a referenced setting rather than describing the path to it: a "Notification settings" link, not "Go to Settings > Notifications > Email".

## One line of description or none

A setting or option gets one line of description at most. Move any further detail into a tooltip, help text or a detail view.

## Status matches the moment

| State | Pattern | Example |
| --- | --- | --- |
| In progress | Verb in `-ing` plus the object | "Saving changes…", "Loading invoices…" |
| Done | Object plus past-tense verb, no "successfully" | "Changes saved", "Invite sent to sam@example.com" |
| Failed | What didn't happen, then the next step | "Changes not saved. Check your connection and try again." |
| Unavailable | Why, and what unlocks it, beside the control | "Add a payment method to publish" |
| Partial | Counts for both outcomes | "9 of 12 files uploaded. Retry 3 failed files" |

Keep the in-progress and done strings parallel, so "Saving changes…" resolves to "Changes saved". "Searched" while the search still runs is wrong; it is "Searching", then "Searched". Set expectations in loading copy and reduce anxiety.

## Errors say how to fix, next to where it broke

An error is an instruction, and it belongs beside the field that failed. Structure: what happened, why when it helps, and how to fix it.

| Bad | Good |
| --- | --- |
| That password is too short | Choose a password with at least 8 characters |
| Invalid date | Enter a date as DD/MM/YYYY |
| Oops! Something went wrong. | Unable to save. Check your connection and try again. |
| Card declined | Payment declined. Your card was declined by your bank. Try a different card or contact your bank. |

No blame, no "oops" and no exclamation marks. Phrase hints positively, as in "Use at least 8 characters" rather than "Don't use fewer than 8". Show a known requirement as helper text before input, not only in the error. When the same error keeps firing, redesign the interaction so it cannot happen.

## Undo beats confirmation

Prefer undo when the action can be reversed and people perform it often, such as archiving, moving or deleting into a trash. Act at once and offer undo in the result: "Project archived. Undo".

Confirm before acting when the action cannot be reversed, affects other people or destroys many items at once. The confirmation repeats the consequence, so the dialog is answerable without reading the body:

- The title names the action and the object, "Delete 'Q3 report'?", never "Are you sure?".
- The body says what is lost and what cannot be recovered, with counts where they apply.
- The action button is verb plus object, `Delete project`; the dismiss button follows the platform's convention, such as `Cancel` on Apple platforms and most web apps. Never `Yes` and `No`.
- For an account, a workspace or a repository, ask the person to type the object's name.

| Situation | Copy |
| --- | --- |
| Reversible, frequent action | Toast: "Project archived" with an `Undo` action |
| Irreversible, one item | Title: "Delete 'Q3 report'?" Body: "This permanently deletes the report and its 4 comments." Buttons: `Delete report` and the platform's dismiss label |
| Irreversible, many items | Title: "Delete 12 files?" Body: "You can't undo this." Buttons: `Delete 12 files` and the platform's dismiss label |
| Affects other people | Body names who: "The 8 members of Design lose access." |
| Account, workspace or repository | Field label: "Type 'acme-web' to confirm". The button stays disabled until it matches |

## Empty states point forward

An empty state says what this place is and how to fill it, and offers one clear next action: "No projects yet. Projects keep your tasks and files together." with a "Create a project" button, not "No results."

A filtered empty state names the query and offers an exit: "No results for 'quarterly'. Clear filters". Never park persistent information in an empty state. It disappears the moment content exists.

## Placeholders, tooltips and onboarding

A placeholder shows a realistic example in the format the field accepts, `name@example.com` or `DD/MM/YYYY`, never an instruction. Tooltips are concise and helpful, never obvious. Onboarding uses progressive disclosure, one concept at a time.

## Naming features

For a feature or destination name, start from the audience and the benefit they
seek, try candidates in real navigation and spoken sentences, and prefer a
familiar neutral term when ambiguity would undermine trust. An invented name
works only when its meaning is discoverable in context.

## Before you finish

| Detection pattern | Fix |
| --- | --- |
| `Click here`, a link reading `here` or two identical `Learn more` links | Name the destination |
| `Oops`, `Something went wrong` or `!` in an error string | Say what failed and the next step |
| A sentence built from fragments around a variable, or a hand-made plural | One message with a plural argument |
| `OK`, `Yes` or `No` on a dialog button | Verb plus object, and the platform's dismiss label |
| `Are you sure` | Name the action and the object |
| `successfully` | Cut it: "Changes saved" |
| `Please` in a routine instruction | Cut it |
| A toggle label starting `Don't`, `Disable` or `Hide` | Describe the ON state |
| An accessible name such as "Trash", "Close icon" or "X" | Name the action: "Delete project", "Close dialog" |
| A date or number formatted without the user's locale | The platform's locale-aware formatter |
| `Save Changes` beside `Discard changes` | Sentence case |
| An id, enum value or internal acronym in visible copy | The display name |

## Output

```markdown
## UX Copy: [Context]

### Recommended Copy
**[Element]**: [Copy]

### Alternatives
| Option | Copy | Tone | Best For |
|--------|------|------|----------|
| A | [Copy] | [Tone] | [When to use] |
| B | [Copy] | [Tone] | [When to use] |
| C | [Copy] | [Tone] | [When to use] |

### Rationale
[Why this copy works — user context, clarity, action-orientation]

### Localization Notes
[Anything translators should know — idioms to avoid, character expansion, cultural context]
```

## If Connectors Available

If **~~knowledge base** is connected:
- Pull your brand voice guidelines and content style guide
- Check for existing copy patterns and terminology standards

If **~~design tool** is connected:
- View the screen context in Figma to understand the full user flow
- Check character limits and layout constraints from the design

## Tips

1. **Be specific about context** — "Error message when payment fails" is better than "error message."
2. **Share your brand voice** — "We're professional but warm" helps me match your tone.
3. **Consider the user's emotional state** — Error messages need empathy. Success messages can celebrate.
