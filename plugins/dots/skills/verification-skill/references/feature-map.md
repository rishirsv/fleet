# Feature map example

The feature map lives in `verify-<app>/features/`. `README.md` is the index and
each feature has its own file. This example describes a notes app driven by a
helper named `verify-notes`.

## Index (`features/README.md`)

The index holds what every recipe shares:

- **Baseline:** launch at `http://127.0.0.1:4173` with a disposable data
  directory per run (`NOTES_DATA_DIR=/tmp/notes-verify-$RUN_ID`), seed notes
  titled `Quarterly plan` and `Grocery list`, and require
  `verify-notes doctor` to report the expected URL, data directory, and build.
- **Driving conventions:** start each recipe from the baseline, prefer roles
  and accessible names over CSS selectors, run commands exactly as written,
  and restore seeded data after a change. Drive only instances this run
  started.
- **Proof:** capture the action and the resulting state. UI proof is an
  accessibility snapshot and a screenshot that shows the app; CLI proof is the
  command, output, and exit code; a change is proven by a second read of the
  stored value. Label every artifact with the feature ID and entry point.
- **Unreachable paths:** report the command attempted and the missing
  precondition. Never report an entry point as verified through another path.
- **Features:** one line per feature file, with a link.

## Feature file (`features/search.md`)

Start with an H1 title and one paragraph describing what the user sees, then
use exactly these four sections in order.

```markdown
# Search notes

Search finds notes by title or body text, opens a match, and tells an empty
result apart from an unavailable search.

## Sub-features

- `search-open` opens search from each entry point.
- `search-match` returns title and body matches without changing data.
- `search-empty` shows a complete empty state for a query with no matches.
- `search-cli` returns the same matches from the terminal.

## How to get to it (user POV)

- Choose `Search` in the toolbar.
- Press `/` while focus is outside an editable field.
- Run `notes search <query>`.

## Driving it with verify-notes

Preconditions: the baseline instance passes doctor and holds the seed notes.

- **Toolbar entry.** Run `verify-notes browser click --role button --name "Search"`.
  A dialog named `Search notes` opens with focus in its search box.
- **Title match.** Run `verify-notes browser fill --role searchbox --name "Search notes" --value "quarterly"`.
  Results contain `Quarterly plan` and not `Grocery list`.
- **Empty state.** Fill `volcano`. A status named `No matching notes` appears.
- **CLI match.** Run `verify-notes cli -- notes search "quarterly" --format json`.
  Exit code 0; output holds one object titled `Quarterly plan`.
- **Proof.** Save `artifacts/search/results.aria.txt` and `results.png`
  showing the app, the query, and the match.

## Gotchas

- `/` types a slash when the editor has focus.
- Results update after a short delay; wait for the list or empty status
  rather than a fixed sleep.
- The CLI prints human-readable text by default; use `--format json` for
  stable checks.
```

Keep implementation details out of the map. Name user paths, stable handles,
required state, exact commands, and observable results.
