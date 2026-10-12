# Enforcement order

Read the repo's own check command first: its `package.json` or build-tool
`lint`/`check` scripts, its CI workflow, and its pre-commit hooks. If a check exists but is unwired or
broken, report that as the finding and repair it before adding another.
Distinguish a missing or broken check from an agent failing to run an available
one. A repo with no pre-commit hook and no CI job running its
lint/typecheck/test command is itself a finding; report the missing protection
without claiming it caused a failure the evidence does not establish.

1. **Eliminate it with architecture.** Remove the design flaw that invites the
   mistake, such as split ownership, two ways to do one task, importable
   internals, or a hand-synced list; Design red flags gives each fix.
   Delete dead code an agent would copy.
2. **Enforce it with types so the bad state can't be written.** If bad code
   still compiles, add a lint or CI check whose error names the file, type, or
   function to use instead. If the pattern is already common, fail only when a
   change adds more.
3. **Test the behavior.** Fix or delete any test that would still pass if every
   function it calls returned nothing.
4. **Write docs or agent rules last, only for judgment calls.** Nothing fails
   when an agent skips them.

Prove each new check fails on a real past mistake, and run the same command
locally and in CI.
