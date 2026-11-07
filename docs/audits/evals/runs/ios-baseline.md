# Atlas iOS: Account screen

Settings > Account. Copy and layout spec for implementation.

## Summary

One scrolling inset-grouped list with four sections, top to bottom:

1. Profile (photo, name, email)
2. Notifications
3. Connected Apps
4. Delete Account

Profile edits are saved with an explicit **Save** button. Toggles and disconnects take effect immediately, as in iOS Settings. Every string the user sees is listed in this document; anything not listed should not appear.

## Assumptions to confirm

These shape behavior. Flag any that are wrong before building.

- **Mentions** is a push notification. **Weekly digest** and **Product updates** are emails.
- Changing email requires confirming the new address. The old address stays active until then.
- Apps are connected from Atlas on the web. iOS only lists and disconnects them.
- Deleting an account keeps the projects and tasks the user created in their workspaces. A user who is the only owner of a workspace must transfer or delete that workspace first, on the web.
- Account deletion is immediate and has no grace period.

## Navigation bar

| Element | Spec |
|---|---|
| Title | `Account`, inline (standard-size) title, since the screen is pushed from Settings |
| Back | System back button, labeled `Settings` |
| Right item | `Save`, bold. Hidden until name or email differs from the saved value. Replaced by a spinner while saving |

While saving, name and email fields are not editable and Back is disabled. Toggles and other sections stay usable.

**Leaving with unsaved edits.** Back (or the edge-swipe) shows an action sheet:

- Title: `Discard changes to your profile?`
- `Discard Changes` (destructive)
- `Keep Editing` (cancel)

## Layout

- List style: inset grouped. System grouped background and cell colors, so light and dark mode come free.
- Horizontal margins: system readable-content margins (16pt on iPhone, wider on iPad).
- Rows: 44pt minimum height, growing with Dynamic Type. No fixed heights anywhere.
- Section headers: system style (small caps-style footnote, secondary color).
- Spacing between sections: system default. Do not add custom spacers.
- Supports Dynamic Type through Accessibility XXXL. At accessibility sizes, label and value stack vertically instead of truncating.

## 1. Profile

No section header. The photo sits above the first group, centered, outside any cell.

### Photo

- 88pt circle, centered horizontally, 24pt from the top of the scroll content and 16pt above the name/email group.
- Below it, 8pt gap, a text button: `Edit` (tint color, subheadline weight).
- No photo: initials on a solid color circle. Initials are the first letter of the first and last word of the name, uppercase (`Maya Okafor` becomes `MO`; a single-word name gives one letter). Color is derived from the user ID so it is stable across devices. Use the same avatar component as elsewhere in Atlas.

Tapping the photo or `Edit` opens an action sheet:

- `Take Photo`
- `Choose Photo`
- `Remove Photo` (destructive, only shown when a photo is set)
- `Cancel`

After a photo is chosen, show the system square crop with a circular mask. Upload begins as soon as the crop is confirmed; it does not wait for **Save**. During upload, the new image shows at 50% opacity with a small spinner centered on it. On success it goes to full opacity. On failure see [Save failures](#save-failures).

`Remove Photo` applies immediately with no confirmation (easy to redo).

Permissions: if camera or photo access is denied, show an alert:

- Title: `Atlas doesn't have access to your camera` (or `to your photos`)
- Message: `You can allow access in iOS Settings.`
- Buttons: `Open Settings`, `Cancel`

### Name and email group

Two rows. Each row is a label on the left and an editable text field filling the rest of the row. Field text is left-aligned after the label column so long values have room.

| Row | Label | Field | Keyboard |
|---|---|---|---|
| 1 | `Name` | Current full name | Default, words autocapitalized, return key `Done` |
| 2 | `Email` | Current email | Email address, no autocapitalization or autocorrect, return key `Done` |

Validation runs on **Save**, not while typing:

| Case | Inline error |
|---|---|
| Name empty or only spaces | `Enter your name.` |
| Name over 100 characters | `Use 100 characters or fewer.` |
| Email not a valid address | `Enter a valid email address.` |
| Email already used (from server) | `That email is already used by another Atlas account.` |

Inline errors appear as the group's footer, in the system red, one line per error. The field with the first error gets focus. Errors clear when that field is edited.

**Pending email change.** After saving a new email, the Email row keeps showing the current, confirmed address. The group footer reads, in secondary color:

`Check maya@newmail.com to confirm your new email.` followed by a tint-colored `Resend` link on the same line.

Tapping `Resend` replaces it with `Sent` for 3 seconds. The footer disappears once the server reports the change confirmed (refresh on screen appear).

**Successful save.** `Save` disappears, the keyboard dismisses, and a success haptic plays. No toast or banner.

## 2. Notifications

Section header: `Notifications`

Three rows, each a label with a trailing switch:

| Row | Label |
|---|---|
| 1 | `Mentions` |
| 2 | `Weekly digest` |
| 3 | `Product updates` |

No subtitles or footer.

Switches send their change immediately. The switch moves at once (optimistic). If the request fails, the switch animates back and this alert appears:

- Title: `Couldn't update notifications`
- Message: `Check your connection and try again.`
- Button: `OK`

**iOS notifications turned off for Atlas.** If system notification permission is denied, the Mentions switch is replaced by tint-colored text `Turn On`. Tapping it opens Atlas's page in iOS Settings. If permission was never requested, the switch shows normally and turning it on triggers the system permission prompt; if the user declines, the switch returns to off.

## 3. Connected Apps

Section header: `Connected Apps`

### Empty (most users)

One non-tappable row, text in secondary color: `No connected apps`

No illustration, button, or explanation.

### With apps

One row per app, sorted by name:

- Leading: app icon, 29pt, 6.5pt corner radius (matches iOS Settings icon size).
- Title: app name, for example `Slack`.
- Subtitle, secondary color: `Connected Mar 4, 2026` (medium date style, user's locale).
- No disclosure chevron.

Disconnect by swiping the row left (destructive action `Disconnect`) or long-pressing it (context menu with `Disconnect`, destructive). Either shows an alert:

- Title: `Disconnect Slack?`
- Message: `Slack will lose access to your Atlas data. You can reconnect it from Atlas on the web.`
- Buttons: `Disconnect` (destructive), `Cancel`

On success, the row animates out. If it was the last app, the empty row appears. On failure, the row stays and this alert appears:

- Title: `Couldn't disconnect Slack`
- Message: `Check your connection and try again.`
- Buttons: `Try Again`, `Cancel`

VoiceOver: expose `Disconnect` as a custom action on each row, since swipe actions are hard to discover.

## 4. Delete Account

No section header. One row, centered text in system red: `Delete Account`

Tapping it shows an alert:

- Title: `Delete your account?`
- Message: `This permanently deletes your profile and removes you from all workspaces. Projects and tasks you created stay in their workspaces. This can't be undone.`
- Buttons: `Delete Account` (destructive), `Cancel` (preferred, so Return selects it)

After `Delete Account`, require Face ID, Touch ID or the device passcode (reason string: `Confirm it's you to delete your account.`). If authentication is cancelled, nothing happens.

While deleting, show a full-screen blocking spinner over the app with no text. On success, sign out and return to the Atlas welcome screen. No goodbye screen.

**Sole workspace owner.** If the server refuses because the user is the only owner of one or more workspaces, show:

- Title: `Transfer your workspaces first`
- Message: `You're the only owner of Design Team and Ops. Make someone else an owner or delete these workspaces on atlas.app, then try again.` (list all affected workspace names; with more than three, show the first three and `and 2 more`)
- Button: `OK`

**Other failure:**

- Title: `Couldn't delete your account`
- Message: `Check your connection and try again.`
- Buttons: `Try Again`, `Cancel`

## Save failures

Covers name, email and photo. Validation errors are covered under [Name and email group](#name-and-email-group). This section covers network and server failures.

**Name or email save fails:**

- The spinner turns back into `Save`. Fields become editable again with the user's edits intact. Nothing reverts.
- An alert appears:
  - Title: `Couldn't save your profile`
  - Message: `Check your connection and try again.` (offline or timeout) or `Something went wrong on our end. Try again in a moment.` (5xx)
  - Buttons: `Try Again` (repeats the save), `Cancel` (closes the alert, edits stay)
- An error haptic plays when the alert appears.

**Photo upload fails:**

- The photo reverts to the previous photo (or initials).
- An alert appears:
  - Title: `Couldn't update your photo`
  - Message: same connection or server message as above
  - Buttons: `Try Again` (re-uploads the same cropped image), `Cancel`
- An image over the server's size limit after cropping uses the message `This photo is too large. Choose a smaller one.` with only an `OK` button.

**Session expired** (401 on any save): no alert on this screen. Route to the app's standard sign-in flow and keep unsaved name and email edits in memory so they are still there if the user returns.

## Loading

The screen renders immediately from the locally cached account. It refreshes in the background on every appear; changed values update in place without animation. If there is no cache (rare), show the list with system placeholder redaction on the photo, name, email and app rows until data arrives. If that first load fails, replace the list with a centered `Couldn't load your account` and a `Try Again` button below it.

## Accessibility

- Photo: one element, label `Profile photo`, hint `Double-tap to change.` Initials avatar reads as `Profile photo, MO`.
- Name and email fields: the row label is the field's accessibility label.
- Inline errors are announced when they appear and are attached to their field.
- Pending email footer: `Resend` is a separate button element.
- All destructive actions use system destructive styling, never color alone.
- Minimum tap target 44 by 44pt, including `Edit`, `Resend` and `Turn On`.

## Copy reference

Every string on this screen, for localization.

| Key | English |
|---|---|
| nav.title | Account |
| nav.save | Save |
| discard.title | Discard changes to your profile? |
| discard.confirm | Discard Changes |
| discard.cancel | Keep Editing |
| photo.edit | Edit |
| photo.take | Take Photo |
| photo.choose | Choose Photo |
| photo.remove | Remove Photo |
| photo.a11y.label | Profile photo |
| photo.a11y.hint | Double-tap to change. |
| access.camera.title | Atlas doesn't have access to your camera |
| access.photos.title | Atlas doesn't have access to your photos |
| access.message | You can allow access in iOS Settings. |
| access.open | Open Settings |
| profile.name | Name |
| profile.email | Email |
| error.name.empty | Enter your name. |
| error.name.long | Use 100 characters or fewer. |
| error.email.invalid | Enter a valid email address. |
| error.email.taken | That email is already used by another Atlas account. |
| email.pending | Check %@ to confirm your new email. |
| email.resend | Resend |
| email.sent | Sent |
| notif.header | Notifications |
| notif.mentions | Mentions |
| notif.digest | Weekly digest |
| notif.updates | Product updates |
| notif.turnOn | Turn On |
| notif.error.title | Couldn't update notifications |
| apps.header | Connected Apps |
| apps.empty | No connected apps |
| apps.connected | Connected %@ |
| apps.disconnect | Disconnect |
| apps.disconnect.title | Disconnect %@? |
| apps.disconnect.message | %@ will lose access to your Atlas data. You can reconnect it from Atlas on the web. |
| apps.error.title | Couldn't disconnect %@ |
| delete.row | Delete Account |
| delete.title | Delete your account? |
| delete.message | This permanently deletes your profile and removes you from all workspaces. Projects and tasks you created stay in their workspaces. This can't be undone. |
| delete.auth | Confirm it's you to delete your account. |
| delete.owner.title | Transfer your workspaces first |
| delete.owner.message | You're the only owner of %@. Make someone else an owner or delete these workspaces on atlas.app, then try again. |
| delete.owner.more | and %d more |
| delete.error.title | Couldn't delete your account |
| save.error.title | Couldn't save your profile |
| photo.error.title | Couldn't update your photo |
| photo.error.tooLarge | This photo is too large. Choose a smaller one. |
| load.error | Couldn't load your account |
| error.network | Check your connection and try again. |
| error.server | Something went wrong on our end. Try again in a moment. |
| common.tryAgain | Try Again |
| common.cancel | Cancel |
| common.ok | OK |
