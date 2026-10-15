# Release cloud plugins

This procedure is for maintainers publishing an existing account or workspace
plugin. Public users install local plugins through [INSTALL.md](../../INSTALL.md).

Dots is a standalone skills plugin. Tunnel is a separate app with its own
connection and release process. Dots packages contain no `.app.json` binding or
`apps` declaration. Keep Git as the source for local and cloud releases.
A profile selects cloud only when its signed-in account has those plugins.
Otherwise it selects local. Source selection controls the local loader, not
cloud publication or account sign-in.
Keep cloud Dots enabled for the personal account on both web and desktop.
A missing icon does not indicate that the wrong source is enabled. Switching
desktop to local would hide the cloud branding defect without repairing web.
Use the profile's local enablement policy for duplicate loaders; account-wide
uninstall is not a desktop-only switch.
Cloud publication is manual. Commits, pulls, hooks, and local sync commands
must not publish an account release.

Resolve the target plugin's exact backend ID from its installation metadata or
authorized plugin discovery. Maintainers may keep their deployment IDs in
`~/.config/dots/cloud-plugins.json`, outside Git. Verify each ID against the
signed-in account; do not reuse another maintainer's private plugin.

Use Plugin Creator's supported tools without ChatGPT web login:

1. Read `get_plugin_files` with the resolved ID. Follow inventory pagination and
   inspect the manifest, scope, and current release. Preserve the existing scope
   and the existing audience. A display name or `name@marketplace` key is not
   a backend ID.
2. Finish the source changes and bump the owning plugin's three manifests
   together. Run `python3 scripts/verify.py --full` for the release. Commit only the release
   changes, then package `plugins/<name>/` from that commit, including hidden
   compatibility manifests, as one `<name>/` directory in a ZIP outside the
   source directory. Include skills, scripts, references, agents, and assets; exclude secrets, caches, and
   untracked development files. Do not package another task's uncommitted edits.
3. Call `update_plugin` with the exact backend ID, the archive's absolute local
   path as `archive`, and the observed release as `expected_release_id`.
   If the release changed, reread and reconcile before retrying. Do not create
   a replacement plugin. The update overlays files; explicitly pass retired
   file paths through `delete_paths` when supported. Otherwise identify retired
   files still present rather than claiming ZIP omission removed them.
4. Read back the returned release. Compare the complete expected skill inventory,
   changed content, and metadata with the source. Open the cloud listing and
   desktop plugin card to confirm the logo and composer icon render. Packaged
   image files alone do not prove that the listing uses them; report branding
   verification as pending if either surface shows a fallback icon.
   If an archive update leaves the cloud image URLs empty, upload the same
   committed ZIP through the existing plugin's **Upload new version** action.
   Refresh the web page and the desktop plugin inventory before checking again.
   Include explicit light and dark icon paths, even when both use the same artwork.
   Fetch `plugin/list` with `created-by-me-remote` before reading skills; a fresh
   CLI server otherwise omits account plugins and can falsely pass the duplicate
   check. Require hosted logo and composer image URLs and visually compare the
   web listing, sidebar, and composer against the source artwork after refresh.
   A nonempty image URL alone does not establish correct rendered branding.
   Compare the owner catalog with the installed sidebar, listing, and composer.
   If they disagree, inspect the responses used by those pages through the
   supported browser tools. Compare the exact plugin and release IDs and the
   four logo/composer URL fields. The detail or owner response can return hosted
   images while the installed response returns null for the same release.
   Reinstalling Dots and Drafts did not repair that mismatch in an observed
   release. Preserve screenshots and a summary of the mismatching fields outside
   Git, and report host verification as blocked. Do not repeat identical ZIP
   uploads or add an app binding to work around the mismatch.
   Do not report a release complete while a surface still shows a fallback.
   Installing or publishing skills does not start Tunnel or authorize folders.
5. Refresh the desktop plugin inventory and verify a fresh loader uses the
   selected source without duplicates. The current `verify-skills.py`
   checks availability and known duplicates, not complete release contents.
   Report cloud publication separately from desktop verification. Restart only
   after active chats finish if desktop retains stale skills.

## Diagnose missing cloud icons

On 2026-10-15, uploading the committed Dots 0.2.256 ZIP through **Upload new
version** created a new release ID without changing the version. The detail
response returned all four hosted image URLs, but the installed response for
the same release returned null. The web UI continued to use its folder fallback.
This isolates a cloud response inconsistency; it does not prove that the
packaged artwork is missing or that local and cloud skills conflict.

Inspect responses captured from the actual page through supported browser tools:

- Detail: `/backend-api/ps/plugins/<plugin-id>`.
- Installed: `/backend-api/ps/plugins/installed`.
- Compare `release.id`, `release.version`, and `release.interface` fields
  `composer_icon_url`, `composer_icon_dark_url`, `logo_url`, and `logo_url_dark`.

Keep evidence outside Git and redact signed image query strings. After one web
upload and refresh, if the responses still disagree, report the branding repair
as blocked on the host service. Repeated uploads, reinstalling the same plugin,
and changing profile source do not resolve the observed inconsistency. Preserve
the existing plugin identity and report skill delivery separately from branding.

## Preserve Tunnel during skill releases

Preserve the existing Tunnel app and its connected account, runtime credentials,
and authorized folders. Its app-backed canonical plugin cannot be edited with
Plugin Creator. Use the app's owning release process for Tunnel updates; never
package Dots skills into it. Keep the tools-only Tunnel plugin enabled
independently of the Dots/Drafts skill-source policies.

If a supported publisher or read-back is unavailable, report that step as
pending. Archive creation, local cache refresh, and local skill availability
alone do not prove cloud publication. Do not edit installed caches or switch
another profile's source to complete a release.

