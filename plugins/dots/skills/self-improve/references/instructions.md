# Instruction files

## Choose the instruction file for the platform

| Runtime | Project instructions | Personal instructions | Generated memory |
|---|---|---|---|
| Codex | closest in-scope `AGENTS.md` or `AGENTS.override.md` | `~/.codex/AGENTS.md` | `~/.codex/memories/` |
| Claude Code | closest in-scope `CLAUDE.md` or `.claude/rules/*.md` | `~/.claude/CLAUDE.md` | `~/.claude/projects/<project>/memory/` |

Claude Code does not load `AGENTS.md` directly. When a repository uses shared
instructions, prefer a small `CLAUDE.md` containing `@AGENTS.md`, with only
genuinely Claude-specific guidance below it. Do not duplicate the shared rules.

## Choose the closest scope

Put a rule in the narrowest file that covers every place it should apply:

- personal defaults that hold across repositories belong in the personal file;
- repository-wide commands and conventions belong at the repository root;
- component-specific rules belong in the closest nested instruction file or
  path-scoped Claude rule;
- deterministic requirements belong in tests, linters, or validators instead
  of prose;
- long procedures belong in a skill or durable document, linked from the
  instruction file only when every session needs the pointer.

Before writing, verify how the active runtime discovers and merges instruction
files. Check existing imports and nested files so the proposal does not create
duplicate or contradictory guidance.

## Write observable rules

### Put guidance in the stage that uses it

Implementation and review need different guidance. Put decisions needed while
building in the implementation workflow. Put judgment criteria used to assess
a completed change in the review workflow.

Reserve `CODING_STANDARDS.md`, or the repository's existing review standards,
for genuine judgment calls (cross-file consistency, "matches the surrounding
style," anything no guardrail could ever substitute for). Mechanical violations
(a fixed syntactic pattern, a banned API, an import shape, a file-location rule)
belong in a deterministic check.

When instruction files grow large, remove instructions that change no behavior,
move review-only criteria to review standards, and replace duplicated
procedures with a pointer to their owner. Preserve guidance that affects a
decision even when it looks obvious in isolation.

### Handle corrections to existing rules

When the operator corrects a mistake, check whether the rule was already there.
If it was, determine whether it was unavailable, ambiguous, unenforced, or
bypassed. Fix that cause instead of adding another copy of the rule.

If the rule was already there and nothing enforces it, fix it at the highest
level that works within the authorized scope. Pair the rule with what enforces
it in the proposal or existing maintenance documentation; do not create a
mandatory rule table in the agent instruction file. Drop a rule once its
mistake can't happen, retaining any explanation still needed for judgment.

### Describe observable behavior

Describe behavior an agent can follow and a reviewer can verify:

- Weak: `Handle errors gracefully.`
- Strong: `On a failed write, preserve the user's input and show a recoverable
  error; do not clear the form.`

For a rule that needs more explanation, capture:

```text
Scope: when and where the rule applies
Rule: the observable decision
Why: the evidence-backed reason
Exceptions: when deviation is allowed
Source: approved thread, review, or decision
```

Short commands and settled conventions can remain one line. Delete or replace
stale text instead of appending another layer.

## Proposal checklist

A source-visible contradiction can support a narrow correction without
inventing a history of failures.

For every proposal:

1. Cite the governing files and any supporting thread clusters. Distinguish a
   source correction from a behavior claim that still needs transcript evidence.
2. Show the exact rule and target file.
3. Explain why a check, skill, doc, or memory note is not the more suitable
   place for the rule.
