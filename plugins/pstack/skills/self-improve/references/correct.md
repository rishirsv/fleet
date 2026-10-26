# Correct

The operator keeps correcting agents in this repo for the same mistakes. Change the repo so the next agent can't make them.

Assume every contributor is an agent that sees only the files it opened, copies the nearest example, and takes the shortest path that compiles. Design the repo so a change that looks right from one file is right for the whole repo.

## Find the mistake classes

First, read recent commits, reverts, review comments, agent instruction files, and comments that explain workarounds. Group the mistakes into classes. A class counts once it has happened twice.

## Fix each class at the highest level that works

1. **Eliminate it with architecture.** Give each piece of state one owner and each task one supported way. Hide internals so the wrong import fails. Replace hand-synced lists with one source of truth. Delete old ways and dead code an agent would copy.
2. **Enforce it with types so the bad state can't be written.** If bad code still compiles, add a lint or CI check whose error names the file, type, or function to use instead. If the pattern is already common, fail only when a change adds more.
3. **Test the behavior.** Fix or delete any test that still passes when the behavior it checks breaks, or that fails when only the internals change.
4. **Write docs or agent rules last, only for judgment calls.** Nothing fails when an agent skips them.

## Fix and prove

Apply supported fixes within the user's requested scope, following [self-improve](../SKILL.md). Prove each new check fails on a real past mistake. Run the same command locally and in CI when CI integration is part of the change. Use existing checks before adding new ones. Do not mandate new checks for low-impact changes that merely mirror the implementation.

Keep each class's correction focused. Do not automatically commit, add a rule table to agent instructions, or create an exception process. Use [instructions](instructions.md) when the supported correction belongs in agent guidance.

**Reply:** each class with its evidence, the level you picked, and why a higher level didn't work.
