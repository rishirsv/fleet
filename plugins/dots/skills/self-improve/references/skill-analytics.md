# Skill evidence

From this skill directory, use the read-only helper to select a fixed evidence set:

```sh
python3 scripts/self_improve.py --platform codex skill-usage --skill dots:publish-pr --days 30 --limit 100
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

The helper is discovery support, not authoritative billing or context telemetry.
Inspect inherited copies, modern event schemas and opaque content before relying
on counts. Preserve stable identifiers, fixed bounds and source coverage in the report.
