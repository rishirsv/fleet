# Validation

Check the claims, examples, and interfaces the documentation change describes.
This is documentation QA, so apply only the checks the change touches.

## Truth

- Confirm behavior against source, config, CLI help, tests, schemas, or
  authoritative docs when a claim depends on them.
- Match examples, commands, paths, flags, environment variables, and output
  names to the current repository.
- Label inference, proposals, and partial evidence beside the affected claim,
  and call a claim verified only when a current check or recently supplied
  result supports it.

## The document

- Meet the selected recipe's or design checklist's expectations and the
  repository's conventions.
- Check heading order, links, code fences, tables, inline code, and terms
  where the change touches them.
- Keep link text meaningful without surrounding prose.
- Keep essential text available as text; give informative images alt text and
  carry meaning by more than color, shape, size, or position.
- Distinguish required actions, optional actions, expected outcomes, and
  possible outcomes.
- Keep protected sections' heading, markers, body, formatting, and position
  unchanged unless the user requested that section, and place generated
  content outside them.

## Agent-readable bundles

- Parse required frontmatter and require a non-empty `type`; preserve unknown
  existing fields unless the user asks to remove them.
- Match index entries to added, removed, and renamed concept files.
- Keep descriptions useful as one-sentence search or index snippets.
- Link related concepts in the repository's preferred path style.
- Give external claims inline source links or a `# Citations` section when
  source authority matters.
