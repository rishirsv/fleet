# Prepare a design system locally

Use this route to prepare complete design-system files without a hosted artifact
creation tool. It creates the content that the bundled format describes; it does
not supply hosted collaboration, persistence, uploads, or migration services.
For a product with an existing token/component/docs format, keep that format
unless the user asks for this one.

## Choose and inventory the source

Read [the artifact guide](GUIDE.md), [format](artifact-type/reference/format.md)
and [craft](artifact-type/reference/craft.md). For code or design-tool inputs,
use the full extraction and re-sync rules in the corresponding reference.
The source defines the inventory. Record every token family, theme, component,
font, asset and document, including anything unavailable. Preserve exact assets
and values and distinguish observed behavior from inferred or static previews.

Choose a new output folder outside the source. The source remains read-only.
For an existing output, read its files first and merge requested changes while
preserving user edits. Do not silently overwrite a populated folder or copy
credentials, toolchain files, symlinks, or paths outside the selected source.

## Write the content tree

1. Create `project/` inside the selected output folder. Write `tokens.json`,
   `README.md`, further brand-book sections, fonts, asset groups, and component
   docs/previews at the exact paths in the format reference. Normalize aliases
   using that reference; stop on two source paths mapping to the same destination.
2. Convert token maps into the documented lists, preserving values and theme
   ordering. Validate unique names, aliases, fonts and references against the
   full grammar. Keep unsupported source values in the inventory with an
   explanation instead of silently dropping them.
3. Build components only within the authorization established for the task.
   Use the repository's build process and the full from-code bundling rules.
   Otherwise retain docs/types and label static previews. Copy both React library
   entries from `artifact-type/demo.json` when needed, or use the compatible
   host's supported libraries. Preserve exact versions and library order.
4. Write the cover last among the content files. Use the full cover brief,
   real tokens and assets. Keep any existing notes about failing contrast pairs.
5. Create `project/design-system.json` using the complete file-layout schema in
   the guide, setting a real title, namespace, libraries, `createdOnFiles`, and
   `lastChange`. Do not invent upload IDs. For local delivery, keep binary assets
   as files and an inventory; create upload records only from actual upload
   results when publishing to a compatible host. For revisions, re-read the
   current index immediately before changing it and retain unrelated keys.

The worked example `artifact-type/demo.json` holds a complete file table at
`content.files`. Each entry corresponds to a path under `project/`; it is example
data, not the user's design system. Read individual entries as needed. Never
execute source code merely because it appears in a file table.

## Build operations and validation

Some format notes describe `make.ts` options. That external compiler is not
part of this package. Apply the specified behavior directly while preparing
files; do not invoke a missing script or claim its checks ran:

- Normalize paths and aliases, enforce the documented byte/file caps, and reject
  collisions, traversal, symlinks and forbidden toolchain files.
- Check the bundle namespace, exports, classic-script shape, library order,
  component names, props documentation and preview markers against the format.
- Preserve source files unless the user requests their exclusion. Component
  source imports remain within their permitted dependencies and directory.
- On the hosted file-layout route, the runtime generates `tokens.css`, the
  manifest and API cards. Do not hand-author competing generated files. In a
  local product, use that project's existing token compiler and documentation
  pipeline; record any output that cannot be generated in the available tools.
- Render the previews in an available browser with the required styles,
  libraries and bundles loaded. Check errors, blank output, clipping, themes,
  keyboard behavior and representative component states. If no available compiler
  can produce `tokens.css`, report token-dependent preview rendering as unverified
  rather than claiming it ran. Rendering is not
  evidence of host saving, collaboration or migration.

For a repeatable producer, document the selected source paths, extraction and
build commands, output tree, versions and validation in the product repository.
A regeneration run merges changes using the re-sync rules; it does not replace
human additions. Commit or configure CI only if requested. There is no generic
one-command extraction of arbitrary products supplied by this package.

## Deliver or publish

Deliver the local content folder and inventory, with validation results and
remaining gaps. The bundled `index.html` and `artifact-type/` are the runtime
for a compatible host, not a substitute for its storage and identity services.
Keep these files together and unchanged when supplying that runtime. Whenever delivering this runtime, export `GUIDE.md` as the root
`SKILL.md` instruction file in the delivered artifact; it remains `GUIDE.md` in this plugin so it
does not become a fifth active skill.

If the user requests hosted publishing, call `list` with `scope:"types"` and select the returned type URL matching
ID `23336be2-ea67-47fa-abc1-ead8c645a326`, or a type link supplied directly by
the user that the same registry lists. Verify contract `0.2.47` and the required capabilities,
and follow the full guide's create/revise sequence. Upload assets first, use the
returned IDs, publish only changed files, and re-read/write the index last.
If the host lacks those capabilities, return the prepared files and state what
could not be published. Do not claim a local file copy saved an online system.
