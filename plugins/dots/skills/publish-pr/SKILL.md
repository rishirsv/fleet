---
name: publish-pr
description: "Commits and pushes finished changes, then opens or updates a GitHub pull request ready for review. Use when the user asks to publish completed work as a PR; not for merging, review feedback, or monitoring checks."
---

# Publish PR

Commit and push the intended changes, then open or update their GitHub pull
request ready for review. Preserve unrelated work.

For commit messages, the pull-request title, and its description, apply
[Writing style](../../references/writing-style.md)
as an editing standard.

1. Confirm the GitHub repository and active account. If necessary, run
   `gh auth switch` and confirm access again.

2. Exclude unrelated changes. If the work is not on a branch, follow the
   repository's naming convention or name the branch after the result. Ask only
   when the change scope or branch starting point is unclear.

3. Fetch the remote and check the branch against the PR's current base. Resolve
   conflicts before publishing. Rebase when repository policy requires it or
   when base changes affect this work.

4. Reuse the completed task's checks and visual evidence; publication alone
   does not require a new verification pass. After rebasing or splitting the
   work, inspect changes to code, dependencies, and build configuration, and
   rerun only checks whose evidence no longer covers the delivered PR.

5. Commit and push, then update the branch's existing pull request to describe
   the latest changes, or open one if none exists. Make it ready for review;
   never create or leave a draft.

6. Confirm that the pull request contains the pushed commit. Report its URL,
   automated checks, and anything that remains unverified. Do not merge it.

## Commit messages and titles

Keep commit subjects and PR titles terse and specific. Follow the repository's
type-prefix convention and add a scope only when useful. Name the result in
plain language. Omit a commit body unless a material reason or caveat is unclear
from the subject; keep any body brief.

## Description

Write the opening for the product owner deciding whether to merge, who may
know the product but not its code or the investigation. In one or two sentences,
name the action that triggers the problem, what the person previously saw, and
what happens after the change. Use the product's button and screen names. For
a refactor or tooling change, explain its practical purpose and whether product
behavior changes. Preserve required template fields without copying older PR
wording or treating historical prose as the standard.

Keep the rest brief and explain the final change from scratch. Replace
implementation vocabulary with the behavior it causes; keep technical detail
only when it helps assess a decision. Keep decisive checks and material risks,
limitations, and unverified behavior visible. Put full logs and detailed
technical evidence in a linked report or collapsed section.

Name the relevant check and its observed result, including what behavior it
verifies. Use before-and-after evidence when the completed task produced it.
Claim that a check failed
before the change only when that failure was observed.

Only when material, assess who or what the change can affect and whether
reverting the code restores the previous behavior. Describe material
consequences and any recovery work a revert would leave, such as restoring data
or coordinating consumer changes.

Use short paragraphs or bullets. Omit investigation chronology, repeated
evidence, background, file inventories, commit history, generic checklists,
and agent narration. For a performance change, give the primary measurement
with its unit as before → after.

Before publishing, read only the title and opening. A reader should understand
the problem and result without reading code, following an audit link, or knowing
another PR. If they cannot, rewrite them around a concrete action and outcome.

## Visual evidence

Upload visual evidence only when the completed task already produced a
screenshot or short video; `$publish-pr` does not capture or recapture it.

Check `gh pr create --help` or `gh pr edit --help` for `--attach`. When it is
supported, write the description to a Markdown file, reference each image or
video where it belongs by its local path, and attach that path. Put a video
reference in its own paragraph so it renders as a player. Repeat `--attach` for
multiple files. `gh` uploads each file and replaces a matching local Markdown
link with its GitHub-hosted URL. Without a matching reference, it appends the
file; set appended-image alt text with a quoted `file#alt text` value. Use the
same flags with `gh pr create` for a new pull request:

```bash
gh pr edit 123 --body-file pr-body.md --attach ./settings.png
gh pr edit 123 --attach './settings.png#Account status in Settings'
```

If `--attach` is unavailable, use another already-authorized attachment
interface when one exists; otherwise keep the evidence local and report that
the pull request lacks it. Never put a local path in the published body.

After publishing, confirm that the saved body contains
`github.com/user-attachments` links instead of local paths and that each image
or video renders.
