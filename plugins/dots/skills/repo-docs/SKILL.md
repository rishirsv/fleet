---
name: repo-docs
description: "Writes, revises, or reviews repository documentation, including READMEs, design docs, runbooks, ADRs, and changelogs. Use for durable repository knowledge; not project instructions, code comments, or chat explanations."
---

# Repo Docs

Write the smallest durable document that lets its reader act or understand
correctly, and stop when the document has done its job.

## References

Repository and user-named style guides come before these defaults.

- Apply [Writing style](../../references/writing-style.md) when drafting,
  editing, or reviewing documentation, including small prose edits and the
  written report.
- After choosing the document type, read its recipe in
  [document-types.md](references/document-types.md).
- For a design doc, architecture proposal, or durable build plan, read
  [design-docs.md](references/design-docs.md).
- For a flow doc or a design-doc diagram, choose the form with
  [Visual explanations](../../references/visual-explanations.md).

## Workflow

1. Define the reader, job, document type, controlling sources, destination, and
   requested mode: edit, draft, or review. Infer clear answers from the request
   and repository. Choose whether the reader needs guided practice, a task
   procedure, lookup facts, or an explanation. Keep these purposes distinct;
   a README may use separate sections and links. Do not split files or expand
   a small edit into a documentation reorganization without a need in scope.
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
6. Check changed claims, examples, paths, and links against their sources.
   Run relevant documentation checks available in the repository. Exercise
   examples when safe and useful; report untested commands without running
   external mutations merely to validate prose. Fix documentation errors,
   and report product defects rather than expanding into product repairs.
7. Report the changed files, document types, checks performed, material checks
   skipped, and open gaps.

For review-only requests, lead with material findings and cite their locations
and evidence. State the reviewed scope and say plainly when no material issue
was found.

## Write for use

Address the reader as "you" where useful. Give task headings an action verb
and concept headings a specific subject. Keep heading levels sequential.
Use numbered steps for ordered actions and parallel bullets otherwise.
Name link destinations; format code identifiers as code and UI labels in bold.
Follow the repository's indentation conventions in examples.

Keep conditions with their actions and put prerequisites before the steps
that need them. Present the usual path before exceptions. Avoid promises of
unreleased behavior and claims that a procedure is easy. Preserve uncertainty
where the evidence requires it. Read for natural rhythm as well as precision;
do not mechanically shorten a clear sentence to meet a word count.

## Frontmatter

Add frontmatter only when the repository convention or the selected
agent-readable format requires it, and preserve existing fields.

## Boundaries

`AGENTS.md` and project instruction files are instructions for agents working in
the repository. Update them only when the user asks for instruction changes.
