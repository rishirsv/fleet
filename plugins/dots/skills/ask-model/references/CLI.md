# CLI advisor runs

Run in the task's repository. Honor the user's model and effort; otherwise use
the configured model at medium effort. Pass a prompt that contains all necessary
task context as the final argument. For a long or multiline prompt, write it to
a temporary `.txt` file outside the repository and pass it on stdin.

Contents: [Models and effort](#models-and-effort) ·
[Session lifecycle](#session-lifecycle) · [Claude](#claude) · [Codex](#codex) ·
[Muse Spark profile](#muse-spark-profile) · [Prompt files](#prompt-files) ·
[Follow up](#follow-up)

## Models and effort

| Request | CLI model | Effort levels |
| --- | --- | --- |
| Fable | Claude: `fable` | `low`, `medium`, `high`, `xhigh`, `max` |
| Astra | Codex: `gpt-6-astra` | `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| Sol | Codex: `gpt-6.1-sol` | Same as Astra |
| Luna | Codex: `gpt-6-luna` | `low`, `medium`, `high`, `xhigh`, `max` |
| Muse Spark | Codex profile `muse`; model `meta/muse-spark-1.3-contributor` | `none`, `minimal`, `low`, `medium`, `high`, `xhigh` |

For other models or changed availability, read the catalog instead of
launching a probe run. `codex debug models` prints the configured Codex catalog
as JSON, with each model's `slug` and `supported_reasoning_levels`; the Muse
profile's catalog is `$CODEX_HOME/muse-models.json`. Claude accepts aliases and
full model IDs; check `claude --help` and `~/.claude/settings.json`. Do not
silently substitute a model or effort.

## Session lifecycle

Every persisted Codex run appears as a task in the Codex app, so decide whether
to save the session before launching:

- **Review and consultation:** run without persistence by default. Add
  `--ephemeral` after `exec` for Codex, or `--no-session-persistence` for
  Claude. An ephemeral run cannot be resumed. Persist it only when a follow-up
  in the same session is already expected.
- **Implementation:** persist the session so corrections can resume it.
- **Cleanup:** once the caller has accepted a persisted Codex run's final
  output, archive it with `codex archive <session-id>` using the launch's `-p`
  profile and `CODEX_HOME`. Claude sessions do not appear in the Codex app.

## Claude

```sh
cd /absolute/path/to/repo
claude -p --model fable --effort medium --dangerously-skip-permissions \
  --output-format json "<self-contained prompt>"
```

The bypass flag permits access beyond the workspace. For a read-only run,
replace it with `--tools 'Read,Glob,Grep' --no-session-persistence`; the tool
list restricts tools but is not an OS sandbox. The JSON result contains the
exact `session_id` and the final response in `result`. Record the ID for any
follow-up.

## Codex

```sh
codex exec -C /absolute/path/to/repo -m gpt-6-astra \
  -c 'model_reasoning_effort="medium"' -c 'approval_policy="never"' \
  --sandbox workspace-write --json "<self-contained prompt>" < /dev/null
```

Use `--sandbox read-only --ephemeral` for review and consultation. For
unrestricted execution, replace the sandbox and approval settings with
`--dangerously-bypass-approvals-and-sandbox` and disclose the broader access.
The `thread.started.thread_id` event contains the exact session ID; the final
response is the `agent_message` item.

`codex exec` also reads stdin when it is not a terminal, so a positional-prompt
launch from a background shell can block on "Reading additional input from
stdin". Redirect stdin from `/dev/null` as shown, or from the prompt file. A
headless run in a directory Codex has not trusted, such as a new worktree, can
wait on a trust prompt nobody sees; trust the path first under
`[projects."<path>"]` with `trust_level = "trusted"` in
`$CODEX_HOME/config.toml`. If a background run emits no `thread.started` event
within about three minutes, treat it as stalled: stop it, fix stdin or trust,
and relaunch.

## Muse Spark profile

`codex -p muse` layers `$CODEX_HOME/muse.config.toml` over the base config. The
profile selects `meta/muse-spark-1.3-contributor` at `xhigh`; its catalog
supports `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. The synced
profile provides valid settings that disable MCP transports, so no extra `-c mcp_servers.*` flags are needed.

```sh
codex -p muse exec --ephemeral -C /absolute/path/to/repo \
  -c 'model_reasoning_effort="xhigh"' -c 'approval_policy="never"' \
  --sandbox read-only --json "<self-contained prompt>" < /dev/null
```

For implementation, drop `--ephemeral` and change `--sandbox` to
`workspace-write`. Keep `-p muse` before `exec` on every launch, resume, and
archive.

## Prompt files

For a long prompt, keep the selected flags and redirect stdin. Claude uses
`< /tmp/advisor-prompt.txt`; Codex uses `- < /tmp/advisor-prompt.txt`.

## Follow up

Resume the original session when implementation is incomplete or a focused
correction is required. Resume by the explicit session ID, never `--last`, and
restate the original model, effort, access, profile, `CODEX_HOME`, and
repository. `codex exec resume` does not accept `-C`, so change to the same
repository first. A successful Codex resume emits the requested ID again in
`thread.started.thread_id`.

```sh
cd /absolute/path/to/repo

# Claude (Fable implementation launched above)
claude -p --resume <session-id> --model fable --effort medium \
  --dangerously-skip-permissions --output-format json \
  "<focused follow-up prompt>"

# Codex
codex exec resume -m gpt-6-astra \
  -c 'model_reasoning_effort="medium"' -c 'approval_policy="never"' \
  -c 'sandbox_mode="workspace-write"' --json <session-id> \
  "<focused follow-up prompt>" < /dev/null

# Muse Spark
codex -p muse exec resume \
  -c 'model_reasoning_effort="xhigh"' -c 'approval_policy="never"' \
  -c 'sandbox_mode="workspace-write"' --json <session-id> \
  "<focused follow-up prompt>" < /dev/null
```

A persisted read-only Claude run repeats its original `--tools` restriction
instead of the bypass flag. Archive a finished Muse run with
`codex -p muse archive <session-id>`.
