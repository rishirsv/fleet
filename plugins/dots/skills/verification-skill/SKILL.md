---
name: verification-skill
description: "Creates or refreshes a project-local verify skill (verify-appname) that launches the real app, drives it the way a user does, and captures proof. Use only when the user selects `$verification-skill`, or asks for a repeatable way to prove app behavior."
---

# Verification skill

Give a repository one maintained way to prove behavior in the running product:
launch it, check it is healthy, drive a feature the way a user does, capture
evidence, and clean up. The output is a project skill named `verify-<app>`
that a future agent reads cold, mid-task, without having seen the app.

Choose the route:

- **Create** when the repository has no verification skill.
- **Refresh** when one exists and the app has changed, a drive failed, or the
  user asks to audit it.

Put the generated skill where this repository already keeps project skills.
If it has none, use the project skill directory the active agent loads (for
Claude Code, `.claude/skills/`) and say so.

## Create

1. **Learn the app from the repository.** Find what a user touches (web UI,
   CLI or TUI, desktop or mobile app, API), how it starts locally (the
   documented dev command, ports, environment, seed data, sign-in), how an
   agent can drive it (existing Playwright or simulator harnesses first, then
   browser automation, a PTY or tmux session, or plain HTTP), what evidence it
   can produce, and whether two instances can run side by side. Ask the user
   only what the repository cannot answer. If the app does not build or start,
   fix or report that first; a skill written against a broken base teaches the
   wrong steps.
2. **Write `verify-<app>/SKILL.md`.** Give it frontmatter whose description
   names the app, its surface, and when to use it. Fill these sections with
   real commands and selectors from this repository, never placeholders:
   - **Launch:** the exact start command, the signal that it is ready, and
     teardown. For a short-lived CLI, build once and run each drive in its own
     isolated session.
   - **Doctor:** one read-only check that the instance is worth driving:
     process up, expected build, port owned by this run, sign-in valid. Run it
     first and again after anything surprising.
   - **Drive:** the harness recipe with stable handles (accessible names, data
     attributes, prompt strings, routes) over coordinates.
   - **Evidence:** what to capture and where it is saved. Follow
     [Visual proof](../../references/visual-proof.md) for rendered output.
     Prove the user path rather than internal setters or test-only routes,
     capture the action and the resulting state, and check side effects such
     as files, rows, or messages. Confirm what a dry-run mode really skips.
   - **Cleanup:** stop only what this run started, never by process name, and
     keep the evidence.
   - **Helpers:** make any shipped script executable and show its invocation.
3. **Seed the feature map.** Create `features/README.md` and one file for each
   of the top three to five user-facing features, in the shape of
   [the feature map example](references/feature-map.md).
4. **Prove it once.** Follow the new skill end to end: launch, doctor, drive
   one mapped feature, capture evidence, clean up, and confirm the evidence
   still exists. Fix what fails and clean up after every failed attempt. An
   unexecuted verification skill is a draft.

## Refresh

1. **Check the map.** Compare the feature map with the current routes,
   commands, and screens. Add missing user-facing features only with a source
   path, remove dead entries, and fix wrong descriptions.
2. **Drive what changed.** Run doctor, then drive every feature touched by
   recent changes or reported failures. Drive the whole map when the user asks
   for a full audit. Re-run doctor after any failed drive before continuing.
3. **Sort each failure.** A wrong description is map drift; fix it. Working
   behavior the harness cannot drive is a harness gap; fix it and drive it
   again. Behavior that is actually broken is a product bug; report it and
   leave product code and the map's description of intended behavior alone.
4. **Report the outcome.** Say whether the skill is current, was corrected, or
   is blocked, which features were driven, and which could not be reached and
   why (missing sign-in, platform, or external state).

Edit only the verification skill's own files during a refresh.

## Finish

Report the skill's location, the feature exercised and its evidence path, and
any startup or harness limits a future agent should know.
