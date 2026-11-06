# Handoff spec: Account (Settings > Account), Atlas for iOS

## Overview

Account is where a person checks who they are signed in as, edits their profile, chooses which emails and notifications Atlas sends, reviews apps connected to their account, and deletes the account. Most visits are short and routine: change a photo, turn off the weekly digest. Deletion is rare and must be hard to do by accident.

The screen is a native inset grouped list pushed from Settings. It uses system controls, system text styles and system colors throughout, so it inherits Dynamic Type, dark mode, and VoiceOver behavior for free. Atlas character lives in the tint color and the profile photo, not in custom controls.

Two save models, kept apart on purpose:

- **Profile** (name, email, photo) is edited in an `Edit profile` sheet with `Cancel` and `Save`. Text edits need an explicit commit, and the sheet gives the save failure one obvious place to appear.
- **Notification toggles** apply the moment they flip, like every iOS settings toggle. No Save button on the Account screen itself.

### Sources and assumptions

No Atlas design system, string catalog, or existing screens were available. Values marked **(inferred)** follow iOS conventions and should be replaced by Atlas tokens where they exist. Product behavior I could not confirm is listed in [Open questions](#open-questions); the spec picks a default for each so the build is not blocked.

Vocabulary used everywhere on this screen: **account**, **profile**, **photo**, **name**, **email**, **connected apps**, **Save**, **Cancel**, **Disconnect**, **Delete account**. Input verb is "tap".

## Layout

```
┌───────────────────────────────────────┐
│ ‹ Settings        Account             │  inline nav title
├───────────────────────────────────────┤
│ ┌───────────────────────────────────┐ │
│ │ (photo)  Ana Ruiz               › │ │  Profile row
│ │  56pt    ana@example.com          │ │
│ └───────────────────────────────────┘ │
│                                       │
│ NOTIFICATIONS                         │
│ ┌───────────────────────────────────┐ │
│ │ Mentions                     [ ●] │ │
│ │ When someone mentions you in a…   │ │
│ │───────────────────────────────────│ │
│ │ Weekly digest                [ ●] │ │
│ │ A summary of your projects each…  │ │
│ │───────────────────────────────────│ │
│ │ Product updates              [○ ] │ │
│ │ New features and changes in Atlas │ │
│ └───────────────────────────────────┘ │
│                                       │
│ CONNECTED APPS                        │
│ ┌───────────────────────────────────┐ │
│ │ No connected apps                 │ │  empty (most users)
│ └───────────────────────────────────┘ │
│ Apps you connect from Atlas on the    │  footer, empty only
│ web appear here.                      │
│                                       │
│ ┌───────────────────────────────────┐ │
│ │ Delete account                    │ │  red text, own section
│ └───────────────────────────────────┘ │
└───────────────────────────────────────┘
```

Section order follows frequency and risk: identity first, routine settings next, the rare list after, the destructive action last and alone.

| Region | Spec |
|---|---|
| Container | `List` with `.insetGrouped` style. System grouped background. Content respects readable width on iPad. |
| Nav bar | Inline title `Account`. Back button shows the previous title (`Settings`). No trailing items. |
| Profile section | One row, no section header. Leading photo 56pt circle **(inferred)**, 16pt gap to text, text stack: name above email, 2pt between. Trailing disclosure chevron. Row vertical padding 12pt **(inferred)**. |
| Notifications section | Header `Notifications`. Three toggle rows, each with title and one-line subtitle, standard separators. |
| Connected apps section | Header `Connected apps`. Empty: one non-interactive row plus a footer. Populated: one row per app. |
| Delete section | No header. One button row, `Delete account`, system red, leading-aligned like other rows. |
| Spacing between sections | System list section spacing. Do not add custom spacers. |

## Design tokens used

All are iOS system values until Atlas tokens are supplied.

| Token | Value | Usage |
|---|---|---|
| `AccentColor` (Atlas tint) | Atlas brand tint, unknown | Toggles on-state, `Change photo`, initials avatar fill (at 15% opacity behind tint-colored initials) |
| `.label` | System | Row titles, name |
| `.secondaryLabel` | System | Email, toggle subtitles, empty-state row text, dates |
| `.systemRed` | System | `Delete account`, `Disconnect` actions, inline error text |
| `.systemGroupedBackground` / `.secondarySystemGroupedBackground` | System | Screen and cell backgrounds |
| `.headline` | 17pt semibold, Dynamic Type | Name in profile row |
| `.body` | 17pt regular, Dynamic Type | Row titles, toggle titles, field text |
| `.subheadline` | 15pt regular, Dynamic Type | Email in profile row, toggle subtitles, connected app date |
| `.footnote` | 13pt regular, Dynamic Type | Section footers, inline errors |
| `.title` | 28pt, Dynamic Type | Initials inside the 96pt edit-sheet avatar |
| Row min height | 44pt | Every tappable row and button |

## Components

| Component | Variant | Content | Notes |
|---|---|---|---|
| Profile row | `NavigationLink`-style button | Photo or initials, name, email | Opens `Edit profile` sheet. Name wraps to 2 lines. Email wraps to 2 lines, then truncates in the middle so the domain stays visible. |
| Avatar | Photo / initials | Circle crop of photo, or initials on tinted circle | Initials from `PersonNameComponentsFormatter` with `.abbreviated` style so they are correct per locale. Photos get a 1pt inner outline: black 10% in light, white 10% in dark. |
| Notification toggle row | `Toggle` with title and subtitle | See copy deck | Subtitle is one line at default size; wraps freely at larger sizes. Never truncate it. |
| Connected app row | Button row | App icon 29pt rounded square, app name, `Connected {date}` | No chevron (it does not navigate). Tap opens the disconnect confirmation. Also supports a trailing swipe action `Disconnect`. |
| Empty connected apps row | Static row | `No connected apps` in `.secondaryLabel` | Not tappable, no pressed state. |
| Delete account row | Button, destructive role | `Delete account` | Pushes the `Delete account` screen. |
| Edit profile sheet | `.sheet`, large detent, `NavigationStack` inside | Avatar, `Change photo`, Name field, Email field | `Cancel` leading, `Save` trailing (bold, the one primary action). Swipe-to-dismiss is blocked while there are unsaved changes (`interactiveDismissDisabled`); a dismiss attempt then shows the discard dialog. |
| Delete account screen | Pushed view, grouped form | Consequences, typed confirmation field, destructive button | See [Delete account](#delete-account). |

## Copy deck

Keys are suggestions for the String Catalog. `{…}` are placeholders filled by the code; never concatenate around them. Pluralized strings need plural variants in the catalog.

### Account screen

| Key | Copy |
|---|---|
| `account.title` | Account |
| `account.profile.a11yHint` | Edits your name, email and photo. |
| `account.notifications.header` | Notifications |
| `account.notifications.mentions.title` | Mentions |
| `account.notifications.mentions.subtitle` | When someone mentions you in a task or comment |
| `account.notifications.digest.title` | Weekly digest |
| `account.notifications.digest.subtitle` | A summary of your projects each Monday |
| `account.notifications.updates.title` | Product updates |
| `account.notifications.updates.subtitle` | New features and changes in Atlas |
| `account.notifications.error` | {setting} not changed. Check your connection and try again. |
| `account.notifications.pushOff` | Notifications for Atlas are off in iOS Settings. |
| `account.notifications.pushOff.link` | Turn on notifications |
| `account.apps.header` | Connected apps |
| `account.apps.empty` | No connected apps |
| `account.apps.empty.footer` | Apps you connect from Atlas on the web appear here. |
| `account.apps.connectedOn` | Connected {date} |
| `account.apps.loadError` | Connected apps didn’t load. |
| `account.apps.retry` | Try again |
| `account.apps.disconnect.swipe` | Disconnect |
| `account.apps.disconnect.title` | Disconnect {app}? |
| `account.apps.disconnect.body` | {app} stops receiving updates from Atlas. You can connect it again from Atlas on the web. |
| `account.apps.disconnect.confirm` | Disconnect {app} |
| `account.apps.disconnect.error` | {app} not disconnected. Check your connection and try again. |
| `account.delete.row` | Delete account |

Toggle labels are nouns under the `Notifications` header, which reads as the ON state: "Mentions, on" means mention notifications are sent. No label starts with "Don't" or "Disable".

### Edit profile sheet

| Key | Copy |
|---|---|
| `profile.edit.title` | Edit profile |
| `profile.edit.cancel` | Cancel |
| `profile.edit.save` | Save |
| `profile.photo.change` | Change photo |
| `profile.photo.menu.choose` | Choose photo |
| `profile.photo.menu.take` | Take photo |
| `profile.photo.menu.remove` | Remove photo |
| `profile.name.label` | Name |
| `profile.name.placeholder` | Ana Ruiz |
| `profile.email.label` | Email |
| `profile.email.placeholder` | name@example.com |
| `profile.email.footer.pending` | We sent a link to {newEmail}. Your email changes when you open it. |
| `profile.saving.a11y` | Saving profile… |
| `profile.saved.a11y` | Profile saved |
| `profile.error.name.empty` | Enter your name. |
| `profile.error.name.long` | Use {max} characters or fewer. |
| `profile.error.email.format` | Enter an email like name@example.com. |
| `profile.error.email.taken` | Another Atlas account uses this email. Enter a different email. |
| `profile.error.offline` | Profile not saved. Check your connection and try again. |
| `profile.error.server` | Profile not saved. Atlas couldn’t be reached. Try again in a few minutes. |
| `profile.error.photo` | Photo not saved. Try again or choose a different photo. |
| `profile.error.partial` | Name and email saved. Photo not saved. Tap Save to try again. |
| `profile.discard.title` | Discard changes? |
| `profile.discard.confirm` | Discard changes |
| `profile.discard.keep` | Keep editing |

`profile.email.footer.pending` is the one "we" string. It reports an action Atlas took, not a failure, so first person reads clearly. Drop it for "A link was sent to {newEmail}…" if Atlas copy never uses "we".

### Delete account

| Key | Copy |
|---|---|
| `delete.title` | Delete account |
| `delete.body` | This permanently deletes your Atlas account, your profile and your notification settings. You can’t undo this. |
| `delete.body.content` | Tasks and comments you created stay in their projects and show your name as Deleted user. |
| `delete.blocked.owner` | You own {count} workspaces. Transfer or delete them on the web before you delete your account. (plural variants: one / other) |
| `delete.confirm.label` | Type {email} to confirm |
| `delete.confirm.placeholder` | {email} |
| `delete.button` | Delete account |
| `delete.deleting.a11y` | Deleting account… |
| `delete.error` | Account not deleted. Check your connection and try again. |
| `delete.done` | Account deleted |

### Alternatives for the strings most likely to be debated

| Element | Option | Copy | Tone | Best for |
|---|---|---|---|---|
| Profile save failure | A (recommended) | Profile not saved. Check your connection and try again. | Calm, plain | Offline or timeout, the most common cause |
| | B | Unable to save your profile. Try again. | Neutral | When the cause is genuinely unknown |
| | C | Changes not saved. Your edits are still here. Try again. | Reassuring | If research shows people fear losing typed edits |
| Connected apps empty | A (recommended) | No connected apps / Apps you connect from Atlas on the web appear here. | Neutral, points forward | Connecting is web-only (assumed) |
| | B | No connected apps / `Connect an app` button | Action-led | If iOS gains a connect flow |
| | C | No connected apps (no footer) | Minimal | If connecting is rare enough that guidance is noise |
| Delete body | A (recommended) | This permanently deletes your Atlas account, your profile and your notification settings. You can’t undo this. | Serious, explicit | Default |
| | B | Your account and profile are deleted right away. You can’t undo this. | Shorter | If a grace period never exists and space is tight |
| | C | Your account is scheduled for deletion in 30 days. Sign in before then to keep it. | Serious, with recovery | Only if the backend has a grace period |

## States and interactions

### Account screen

| Element | State | Behavior |
|---|---|---|
| Screen | First load | Show cached profile and toggle values immediately. Refresh in the background; update values in place without a spinner. |
| Profile row | Pressed | System cell highlight. Tap opens `Edit profile` sheet. |
| Profile row | Email change pending | Email line shows the current (old) email. No extra line on this screen; the pending note lives in the sheet. |
| Toggle | Tap | Flip immediately (optimistic), light selection haptic from the system toggle, send the change. Further taps on the same toggle are allowed; send only the latest value. |
| Toggle | Save failed | Flip back to the previous value, show `account.notifications.error` as the section footer in `.systemRed` with `{setting}` set to the toggle title, post a VoiceOver announcement of the same text. Footer clears on the next successful change. |
| Mentions toggle | iOS notifications denied | Only if mentions are delivered as push (see Open questions). Toggle stays usable (controls email too, or stored for later). Section footer: `account.notifications.pushOff` followed by an inline link `Turn on notifications` that opens `UIApplication.openNotificationSettingsURLString`. Recheck permission when the app returns to foreground. |
| Connected apps | Loading | If the list is not back within 300ms, show one redacted placeholder row (`.redacted(reason: .placeholder)`) for at least 300ms. |
| Connected apps | Empty | `No connected apps` row plus `account.apps.empty.footer`. |
| Connected apps | Populated | Rows sorted by app name. Footer hidden. Date uses `.formatted(date: .abbreviated, time: .omitted)`. |
| Connected apps | Load failed | Row text `account.apps.loadError` in `.secondaryLabel` and a second row, `Try again`, in tint color. Rest of the screen works normally. |
| Connected app row | Tap or swipe `Disconnect` | Confirmation dialog (action sheet): title `Disconnect {app}?`, message body, `Disconnect {app}` (destructive), `Cancel`. |
| Connected app row | Disconnecting | Row stays in place with a trailing `ProgressView`; row disabled. |
| Connected app row | Disconnected | Row animates out with the system list removal. If it was the last row, the empty state appears. |
| Connected app row | Disconnect failed | Row returns to normal. Section footer shows `account.apps.disconnect.error` in `.systemRed`, announced to VoiceOver. |
| Delete account row | Tap | Push `Delete account` screen. |

### Edit profile sheet

| Element | State | Behavior |
|---|---|---|
| Sheet | Open | Fields prefilled. `Save` disabled until something differs from the saved profile (nothing to save is self-evident, so no explanation). Focus is not moved into a field automatically. |
| Avatar | Default | 96pt circle **(inferred)**, centered, `Change photo` text button 8pt below. |
| `Change photo` | Tap | Menu: `Choose photo` (PHPicker, single image), `Take photo` (camera; hide the item if no camera), `Remove photo` (destructive role, only when a photo exists). |
| Avatar | New photo picked | Preview immediately with a centered square crop. Photo is staged, not uploaded, until `Save`. Downscale before upload (long edge 1024px, JPEG) **(inferred)** so file-size limits rarely apply. |
| Avatar | Photo removed | Shows initials. Staged until `Save`. |
| Name field | Default | `.textContentType(.name)`, autocapitalize words, autocorrect off. Trim leading and trailing spaces on save. |
| Email field | Default | `.textContentType(.emailAddress)`, `.keyboardType(.emailAddress)`, no autocapitalization, no autocorrect. Trim spaces. Return on Name moves to Email; Return on Email triggers Save when enabled. |
| `Save` | Tap | Validate locally first (empty name, email format). If invalid: show each error as that field's section footer in `.systemRed`, move focus to the first invalid field, no request sent. |
| `Save` | Saving | Label stays `Save`, a `ProgressView` replaces it in place at the same width, button and fields disabled, `Cancel` disabled. If the request finishes under 150ms, never show the indicator. |
| `Save` | Success | Dismiss the sheet. Account screen row updates. VoiceOver announces `Profile saved`. No toast. |
| `Save` | Success with email change | Sheet stays open for this one case, email field shows the old email, footer under it shows `profile.email.footer.pending`. `Save` returns to disabled. `Cancel` becomes the way out (label stays `Cancel`; there is nothing left to discard). |
| `Save` | Field error from server (email taken, name too long) | Same treatment as local validation: footer under the field, focus moves to it, other edits kept. |
| `Save` | Failed, offline or server | See [Profile save failure](#profile-save-failure). |
| `Cancel` or swipe down | No changes | Dismiss. |
| `Cancel` or swipe down | Unsaved changes | Confirmation dialog anchored to `Cancel`: title `Discard changes?`, `Discard changes` (destructive), `Keep editing` (cancel role). |

### Profile save failure

This is the state the engineer most needs pinned down. When `Save` fails for a reason that is not tied to one field:

1. The sheet stays open. Every edit the person made (name, email, staged photo) stays exactly as typed.
2. A message appears at the top of the form as the header of the first section, in `.footnote`, `.systemRed`, with a leading `exclamationmark.circle.fill` SF Symbol in the same color, aligned to the text's cap height:
   - No connection or timeout: `Profile not saved. Check your connection and try again.`
   - 5xx or unreachable server: `Profile not saved. Atlas couldn’t be reached. Try again in a few minutes.`
3. `Save` becomes enabled again with its normal label, so retrying is one tap.
4. Play the `.error` notification haptic once.
5. VoiceOver: post an announcement with the message text. Do not move focus away from `Save`.
6. The message clears when the person edits any field or taps `Save` again.

Photo failures:

- Photo upload fails and nothing else changed: message under the avatar, `Photo not saved. Try again or choose a different photo.` Staged photo stays in the preview.
- Name or email saved but the photo failed (if the API saves them separately): show `Name and email saved. Photo not saved. Tap Save to try again.` under the avatar. `Save` stays enabled because the photo is still unsaved. The Account screen row already shows the new name.

Never use a blocking alert for these failures. The inline message keeps the edits visible and the retry next to them.

### Delete account

Layout of the pushed screen, top to bottom, as a grouped form:

1. Section with `delete.body` and, beneath it, `delete.body.content`, both `.body`, `.label`. No icon, no illustration.
2. Blocked case only, replacing everything below: `delete.blocked.owner` as a plain paragraph, and no field or button. Workspaces must be handled on the web first (assumed).
3. Section with header `Type {email} to confirm`, one text field, placeholder `{email}`, email keyboard, autocorrect and autocapitalization off. Paste allowed.
4. Section with one button row, `Delete account`, destructive role, full-width row.

| Element | State | Behavior |
|---|---|---|
| `Delete account` button | Field doesn’t match | Disabled. Match is case-insensitive after trimming spaces. Why it’s disabled is stated in the header right above the field. |
| `Delete account` button | Field matches | Enabled. |
| `Delete account` button | Tap | No second dialog; the typed email is the confirmation. Send the request. |
| `Delete account` button | Deleting | Label stays, `ProgressView` beside it, field and button disabled, back button hidden so the request cannot be abandoned midway. |
| Screen | Delete failed | Message as section footer under the button in `.systemRed`: `delete.error`. Field keeps its value, button enabled. VoiceOver announcement. `.error` haptic. |
| Screen | Deleted | Sign out locally, clear cached data, replace the app’s root with the sign-in screen, and show `Account deleted` there as a brief confirmation (VoiceOver announces it). |
| Screen | Re-authentication required (if the server demands it) | Present the app’s existing sign-in confirmation, then resume the delete. Do not build a new auth UI for this screen. |

App Store Review Guideline 5.1.1(v) requires account deletion to be available in the app, so this flow cannot only link out to the web. The blocked case above still satisfies it as long as deletion becomes possible once workspaces are dealt with; confirm with whoever owns App Review.

## Responsive behavior

| Size class | Changes |
|---|---|
| Compact width (iPhone) | Layout as drawn. |
| Regular width (iPad, Settings in split view detail) | Same list; system readable-width margins. Edit profile presents as a form sheet. Confirmation dialogs become popovers anchored to the tapped row or `Cancel`. |
| Accessibility text sizes (AX1 and up) | Profile row stacks: avatar above the text, both leading-aligned. Toggle rows: title and subtitle wrap fully, toggle stays trailing, vertically centered on the title's first line. Connected app date moves under the name (it already is). Nothing truncates except email past 2 lines. |
| Landscape iPhone | No change beyond system safe-area insets. |

## Edge cases

- **Long names**: wrap to 2 lines in the profile row, then end-truncate. Full name always visible in the edit field. Test with a 64-character name and a German-length UI.
- **Long emails**: 2 lines, then middle truncation (`ana.ruiz-…@example.com`), so the domain stays readable.
- **Name limit**: `{max}` comes from the API. 64 characters is the inferred default until confirmed.
- **No photo**: initials. One-word name gives one initial. A name with no letters (emoji only) falls back to the SF Symbol `person.crop.circle.fill` in tint color.
- **Many connected apps**: list grows naturally; no cap and no "show more". Long app names wrap.
- **Email change pending, then changed again**: the newest pending address replaces the old one in the footer.
- **Offline on open**: cached values show. Toggles and Save attempt the request and fail with the copy above. Connected apps shows its load-failed row if nothing is cached.
- **Pseudo-localization**: run with the double-length pseudolanguage. The riskiest strings are `Save`, `Cancel` and `Disconnect` because short labels grow most.
- **Right-to-left**: all layout leading/trailing. The chevron and swipe actions mirror via the system. Email and app names are isolated as left-to-right values.

## Animation / motion

System motion only. No custom transitions on this screen.

| Element | Trigger | Animation | Duration | Easing |
|---|---|---|---|---|
| Toggle | Flip or revert on failure | System toggle | System | System |
| Inline error footer | Appears or clears | Default list update (`withAnimation`), height change plus fade | System default | System default |
| Connected app row | Disconnected | System row deletion | System | System |
| Edit profile sheet | Open, close | System sheet | System | System |
| Avatar preview | New photo staged | Crossfade old to new | 200ms **(inferred)** | ease-out |

With Reduce Motion on, replace the avatar crossfade with an instant swap; system animations adapt on their own.

## Accessibility notes

- **VoiceOver order on Account**: back button, title, profile row, Notifications header, three toggles in order, Connected apps header, app rows or empty row, footer, `Delete account`.
- **Profile row**: one element. Label "{name}, {email}", trait button, hint `Edits your name, email and photo.` The avatar image is hidden from VoiceOver.
- **Toggles**: label is the title, the subtitle is read as part of the label after a pause (combine children), value is On or Off (system).
- **Connected app row**: label "{app}, Connected {date}", trait button, hint "Disconnects {app}." Swipe action is also exposed as a custom action named `Disconnect`.
- **Edit profile**: avatar announced as "Profile photo" (or "No profile photo, initials {initials}"); `Change photo` is a button. Fields use their visible labels as accessibility labels. An error footer is attached as the field's accessibility hint so it is read when the field gains focus.
- **Announcements**: every failure and success listed in the state tables posts its exact visible text, nothing different.
- **Delete account**: the field's label is the full "Type {email} to confirm" string. The disabled button reads "Delete account, dimmed", and the field above it explains why.
- **Hit areas**: every tappable row 44pt minimum height; `Change photo` gets a 44pt hit area even though its text is smaller.
- **Contrast**: system colors meet contrast in light, dark and Increase Contrast. Check the Atlas tint on the initials avatar (tint text on 15% tint fill) against 4.5:1; darken the initials if it fails.
- **Full Keyboard Access (iPad, hardware keyboard)**: Tab moves through rows in the VoiceOver order above; Space toggles; Return in the last edit field triggers `Save`; Escape triggers `Cancel` in the sheet (with the discard dialog if needed).

## Localization notes

- Every sentence is one string with placeholders. `{setting}`, `{app}`, `{email}`, `{newEmail}`, `{date}`, `{count}`, `{max}` are filled in code; translators must see them as variables.
- `delete.blocked.owner` needs plural variants. Some languages have more than two forms; use the String Catalog's plural support, not a hand-made "s".
- `Connected {date}`: the date comes from the locale formatter. Some languages put the date first; the placeholder allows that.
- `Deleted user` in `delete.body.content` must match exactly whatever label Atlas shows on deleted users' content elsewhere.
- "Mentions" means @-mentions of a person. Give translators that context so it isn't rendered as "references" or "citations".
- "Digest" means a summary email. Tell translators; it has no food meaning here.
- No idioms, humor or exclamation marks anywhere on this screen.

## Open questions

Each has a default the spec already uses. Confirm before release.

| # | Question | Default used in this spec |
|---|---|---|
| 1 | How are the three notifications delivered: push, email, or both? | Channel-neutral copy. The iOS-permission footer applies only if mentions use push. |
| 2 | Which day does the weekly digest send, and is it per time zone? | "each Monday". Drop the day from the subtitle if it varies. |
| 3 | Server defaults for each toggle for new users? | Unknown; the screen shows whatever the server returns. |
| 4 | Does changing email require verification? | Yes, link sent to the new address; email changes on open. |
| 5 | Can apps be connected from iOS? | No. Connecting is web-only, so the empty state points to the web. |
| 6 | Do profile fields and photo save in one request or two? | Two possible, so the partial-failure string exists. |
| 7 | Name length limit and photo size limit? | 64 characters; client downscales photos so size limits rarely apply. |
| 8 | What happens to a deleted user's tasks, comments and owned workspaces? | Content stays and shows Deleted user; owning a workspace blocks deletion until transferred on the web. |
| 9 | Is there a deletion grace period? | No, deletion is immediate. Use alternative C for the body if there is one. |
| 10 | Does Atlas sell App Store subscriptions? | Assumed no. If yes, add a line that deleting the account does not cancel an App Store subscription, with a link to manage subscriptions. |
| 11 | Does deletion require recent sign-in? | Reuse the existing sign-in confirmation if the server asks. |
