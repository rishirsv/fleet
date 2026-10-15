# Change audit

Find UI regressions in a diff, branch, commit, or pull request. Review the
requested change and the surfaces it affects, judge them with the [design
audit](design-audit.md) criteria, and report through its result.

## Contents

- [Resolve scope](#resolve-scope)
- [Inspect the affected interface](#inspect-the-affected-interface)
- [Read the removed lines](#read-the-removed-lines)
- [Classify every finding](#classify-every-finding)
- [Hold the change to its stated intent](#hold-the-change-to-its-stated-intent)

## Resolve scope

Use the target the user supplied. Compare a branch or pull request with the
merge base of its actual base branch, and a commit with its parent; ask which
parent to use for an ambiguous merge commit. With no target, review the current
branch's commits plus working changes, and describe committed and uncommitted
changes separately. If there are no changes, say so and ask for a target.

Inspect both paths of renamed files, and changed images, fonts, or visual
snapshots that affect the interface. Preserve the user's checkout; inspect other
revisions through fetched refs or an isolated worktree.

## Inspect the affected interface

Find the screens and components that use each changed file and review the
interface there. For shared tokens or primitives, follow their uses to
representative screens that cover different states, themes, and layouts. List
uses you did not inspect.

## Read the removed lines

A removed line identifies something to investigate. Inspect both sides of every
relevant hunk, and report a regression only after confirming the change did not
replace the removed behavior.

| Removed from the `-` side | What to check |
| --- | --- |
| `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-live`, `role=` | The control or region lost its accessible name, description, or announcement |
| `alt=`, `<label`, `for=`, `scope=` | An image, field, or table cell lost its programmatic association |
| `<button>`, `<a>`, `<nav>`, `<main>`, `<ul>` replaced by `div` or `span` | Keyboard and assistive-technology behavior was traded for styling |
| `:focus-visible`, `:focus`, `outline`, `tabindex` | Keyboard users lost the focus indicator, or the element left the tab order |
| `prefers-reduced-motion` | Motion now ignores the user's system preference |
| `prefers-contrast` | Contrast now ignores the user's system preference |
| Logical properties swapped for `left` / `right` | Direction-aware layout was dropped |
| `lang=`, `dir=` | Language metadata or text direction was dropped |
| `text-wrap`, `line-clamp`, `overflow-wrap`, `tabular-nums`, `font-feature-settings` | Text rendering, wrapping, or numeral alignment changed |
| A color token swapped for a literal or a lighter token | The rendered contrast pair may now fail; measure it |
| A user-facing string deleted or shortened | A label, error, or empty state lost the information it carried |

These replacements can preserve the removed behavior; verify the replacement
works before dismissing the removal:

- `aria-label` replaced by `aria-labelledby` pointing at visible text.
- An explicit `role` dropped because the element became its native equivalent,
  such as a `div` with `role="button"` becoming a `<button>`.
- `outline` replaced by a `box-shadow` focus ring that stays visible, including
  in forced colors.
- `tabindex="0"` dropped from an element that is now natively focusable.
- A color literal replaced by a token that measures the same rendered pair.
- A physical property replaced by its logical counterpart, which is a fix.
- A string moved into the translation catalog.

## Classify every finding

Give every finding one status by its cause:

- `Introduced`: the change created it.
- `Regression`: the change weakened something previously correct.
- `Pre-existing`: present in the touched surface but not caused by this change.

Compare with the base revision when needed to confirm the cause. An untouched
line can regress because its shared token or ancestor changed; nearby locations
and Git blame alone do not prove the cause. Keep pre-existing issues separate
unless they block the requested result.

## Hold the change to its stated intent

Read the pull request title and body, the linked issue, and the commit messages,
and check whether the interface delivers what they claim. Check the applicable
states of a new variant or theme, translation entries for new strings, and
sibling surfaces that must expose the same action. Report missing states only
where the component or task requires them.

Return the resolved scope, affected surfaces, classified findings, and
uninspected coverage.
