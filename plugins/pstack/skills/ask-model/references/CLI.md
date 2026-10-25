# CLI sessions

Run from the actual task repository. Check the installed CLI help and active
model catalog for supported models, effort, flags and output shapes. Preserve
an explicitly requested model; do not launch a paid probe just to discover it.
Use the configured effort when none is requested; do not invent a different
model choice. Machine-specific profiles belong in local configuration, not this
portable skill.

Review and consultation default to ephemeral, read-only runs. Persist only when
a follow-up is expected; implementation should be resumable. Give a multiline
prompt through a temporary file outside the repository. Positional prompts in
background Codex runs need stdin redirected from `/dev/null`, otherwise the CLI
may wait for additional input. New untrusted directories can also wait for a
trust prompt; resolve that through supported local setup before retrying.

Codex launch shape (replace placeholders with the selected values):

```sh
codex exec -C /absolute/repository -m MODEL \
  -c 'model_reasoning_effort="EFFORT"' -c 'approval_policy="never"' \
  --sandbox read-only --ephemeral --json - < /absolute/prompt.txt
```

For authorized implementation use the appropriate write sandbox and omit
`--ephemeral`. Use broader bypass flags only when authorized and disclose the
actual access. Custom-agent prose is not an OS sandbox.

Claude launch shape for read-only work:

```sh
claude -p --model MODEL --effort EFFORT --tools 'Read,Glob,Grep' \
  --no-session-persistence --output-format json < /absolute/prompt.txt
```

That tool list restricts capabilities, not OS access. Choose the authorized
write/tool configuration for implementation and persist the session. Do not
silently use a permission-bypass flag as the normal implementation setup.

For Codex JSONL, capture the `thread_id` from `thread.started` and the final
`agent_message`; for Claude JSON, capture `session_id` and `result`. Check the
installed version’s actual event shape rather than deriving an ID from filenames.

Record the exact returned session ID, repository, model, effort, permissions,
profile and configuration home. An ephemeral run cannot be resumed. Resume by
that ID, never `--last`, preserving its launch settings. Codex resume does not
accept `-C`, so change to the repository first. Inspect output and the actual
diff/checks; a successful process exit alone does not prove implementation.

For a persisted implementation, resume from the repository using the same
profile, configuration home, model, effort and access. With launch values
substituted, the CLI shapes are:

```sh
codex exec resume -m MODEL -c 'model_reasoning_effort="EFFORT"' \
  -c 'approval_policy="never"' -c 'sandbox_mode="workspace-write"' \
  --json SESSION_ID - < /absolute/correction.txt
claude -p --resume SESSION_ID --model MODEL --effort EFFORT \
  --output-format json < /absolute/correction.txt
```

Repeat any launch-specific tool/permission restrictions on the Claude command;
the example does not grant write access. Put a selected Codex `-p PROFILE`
before `exec` on launch and resume, and before `archive SESSION_ID` at cleanup.

If a run never emits a session-start event, inspect stdin, trust and stderr,
then stop the task-owned process before a corrected retry. After accepting a
persisted Codex advisor's final output, archive it through the supported flow,
using the same profile and configuration home.
