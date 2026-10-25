# Skill evidence

From this skill directory, use the read-only helper to select a fixed evidence set:

```sh
python3 scripts/self_improve.py --platform codex skill-usage --skill pstack:publish-pr --days 30 --limit 100
```

Choose the platform explicitly. The skill filter applies after scanning the
selected sessions; title-only searches miss invocations without a prompt mention.
Mentions, structured invocations and correlated friction signals are different.
Injected skill text is not independent evidence of use. Silent selection and
unrecorded calls may be absent; label that coverage limit.

Read every selected representative, including successful invocations. Establish
whether the skill ran, what it changed and the actual outcome. Distinguish a
skill causing a problem from merely appearing in the same task. Repeated clean
runs can support keeping a method. Do not equate low measured use with no value.

When editing or shortening a skill, compare its current source with the last
known capable version and any named source material. Inventory modes, inputs,
methods, evidence requirements, exceptions, outputs and reference entry points.
Distinguish duplicate prose from instructions that produce different behavior;
word count does not measure capability. References still on disk but no longer
linked may be effectively lost.

For each removed mechanism, show where its behavior survives or why it was
intentionally retired. Check representative requests for each mode and a case
that would expose the loss. Use behavioral evaluations when available; a source
comparison or format validator alone does not establish model performance.
Preserve the capability comparison and observed evaluation results outside the
shipped skill unless they are needed for its operation.

The helper is discovery support, not authoritative billing or context telemetry.
Inspect inherited copies, modern event schemas and opaque content before relying
on counts. Preserve stable identifiers, fixed bounds and source coverage in the report.
