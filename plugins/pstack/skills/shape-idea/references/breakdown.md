# Breakdown

When the user wants the settled tree split into tickets or specifications,
derive them from the Idea Snapshot without reopening settled decisions.

Cut **vertical slices**: each delivers one narrow behavior end to end through
every layer it touches, and can be demonstrated or checked on its own. Put any
preparatory refactor first. For one mechanical change that spans the codebase,
such as a rename, sequence it as expand, migrate in batches, then remove the
old form, so each step stays green.

For each slice, give:

```md
**<NN> · <title>**

- **Delivers:** <the behavior that works when this is done, in user terms>
- **Blocked by:** <slice numbers, or "None">
- **Acceptance checks:** <observable conditions that prove it works>
- **Decisions carried:** <snapshot decisions and guardrails this slice relies on>
```

Leave out file paths and code, which go stale; include a prototype snippet only
when it states a decision more precisely than prose. Present the list and
adjust granularity or blocking edges from the user's reply. Publish to an issue
tracker or files only when the user asks.
