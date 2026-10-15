---
name: design-context
description: "Save, recall, update, or forget product design context; audit, document, extend, build or sync a design system from a repository or design file. Use for tokens, components, brand guidance and product design preferences."
---

# Design context

Keep product facts and reusable decisions close to their authoritative sources.
Follow the [context contract](../../references/context-contract.md). This skill
owns saved context; it does not make a new source of truth for token values or
silently replace a component library.

## Context operations

Read the product's established design docs first, or the home named by the user.
For an explicit save with no established home, use `docs/design/context.md` in
the current product repository for shared product facts. Put personal/private
material in a user-selected external location; ask for that location only when
needed. No repository and no selected home: ask where to save, and prepare the
content meanwhile. Never use the installed plugin directory as state.

A useful entry contains the product and scope, fact or preference, source link
or file, date added/last verified, and intended use. Distinguish user preference,
measured value, research evidence and assumption. Link token and component
sources instead of copying a second authoritative inventory. Capture conflicts
rather than silently overwriting product decisions.

For recall, read relevant entries and report their sources and freshness. For
update, read the latest file, change the named entries and preserve unrelated
content. For forget, remove only the requested entries and their exclusively
owned saved assets; do not delete authoritative source files. Report what changed.
Save screenshots only when requested and keep them next to the context file
with descriptive names. Do not persist credentials or identifiable participant
data. Missing context, stale links and `not provided` are not facts.

## Design-system work

Read the full [design-system guide](../../references/design-system.md)
and [workflow guidance](../../references/workflows-guide.md).

- Audit the actual tokens, component inventory and representative callers.
  Identify duplicate semantics, missing states, inaccessible combinations and
  hardcoded values with evidence. A deliberate exception is not automatically a defect.
- Document actual variants, states, API, usage and accessibility behavior. Mark
  missing behavior; do not turn a desired spec into a claim about implementation.
- Extend from an observed product need. Reuse existing patterns and change the
  owning token/component source. Show affected themes and states using the
  [evidence contract](../../references/evidence.md); a context document alone
  does not implement a component.

To build or sync the bundled design-system format, read the full
[artifact guide](../../design-system/GUIDE.md) and
[local setup](../../design-system/local-setup.md). Use the source-specific
extraction and re-sync references they identify. Select local delivery or hosted
publishing from the requested outcome and available capabilities.
Write results with [reporting guidance](../../references/reporting.md).
