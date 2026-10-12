---
name: repo-docs
description: "Writes, revises, or reviews durable documentation that lives in a repository. Use for READMEs, design docs, runbooks, ADRs, changelogs, or agent-readable knowledge; not for project instructions, code comments, or chat explanations."
---

# Repo Docs

Write the smallest durable document that lets its reader act or understand
correctly. Lead with the outcome, preserve the exact technical meaning, and stop
when the document has done its job.

## References

Repository and user-named style guides come before these defaults.

- Apply [Writing style](../../references/writing-style.md) to every new
  document or substantial section; durable docs are its main audience.
- After choosing the document type, read its recipe in
  [document-types.md](references/document-types.md).
- For a design doc, architecture proposal, or durable build plan, read
  [design-docs.md](references/design-docs.md).
- For a flow doc or a design-doc diagram, choose the form with
  [Visual explanations](../../references/visual-explanations.md).
- Before completion, apply the checks in
  [validation.md](references/validation.md) that the change touches.

## Workflow

1. Define the reader, job, document type, controlling sources, destination, and
   requested mode: edit, draft, or review. Infer clear answers from the request
   and repository.
2. Support the claims with the smallest set of authoritative sources needed.
   Expand only to resolve a concrete gap or conflict. Derive changelogs and
   release notes from history and merged changes since the last release.
3. Follow repository structure, metadata, and ownership conventions; otherwise
   use the closest recipe. Prefer updating or combining the documents
   responsible for the information over adding another index or status page.
4. Give each fact one home. Point to the code, schema, config, or `--help`
   that defines a list of files, options, commands, or fields instead of
   copying that inventory into prose, because copied inventories drift from
   the source. Link to another document rather than restating it.
5. Lead with what the reader can do, decide, or understand. Keep background
   proportional to that job. Preserve caveats and uncertainty; label proposals
   and unverified claims. Leave explicitly protected sections unchanged.
6. Report the changed files, document types, checks performed, material checks
   skipped, and open gaps.

For review-only requests, lead with material findings and cite their locations
and evidence. State the reviewed scope and say plainly when no material issue
was found.

## Frontmatter

Add frontmatter only when the repository convention or the selected
agent-readable format requires it, and preserve existing fields.

## Boundaries

`AGENTS.md` and project instruction files are instructions for agents working in
the repository. Update them only when the user asks for instruction changes.
