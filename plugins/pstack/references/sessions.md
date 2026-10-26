# Sessions

## Read the prior trail

Use supported read-only interfaces first: list candidate chats, then read the
smallest useful matching set. Archived work may need a separate listing. Do not
resume, fork, message, rename or archive a task merely to inspect its history.
A historical completion claim does not establish a PR or branch's live status.

State sources, host, cutoff, selected window and exclusions. Codex and Claude
local stores do not cover all consumer web chats. Analyze platforms separately
before comparison. Preserve successful and contradictory outcomes. Transcripts
can contain private source and credentials; return findings, not raw dumps.

When supported interfaces omit necessary detail, use this plugin's read-only
helper from `skills/self-improve/`:

```sh
python3 scripts/self_improve.py --platform codex triage --days 30 --limit 100
python3 scripts/self_improve.py --platform codex show THREAD_ID
python3 scripts/self_improve.py --platform claude files SESSION_ID
python3 scripts/self_improve.py --platform codex stats --days 7
```

Counts narrow the read set; inspect the underlying evidence. Never present
cumulative usage or total transcript length as current context occupancy.

Codex's local fallback is normally `$CODEX_HOME/state_5.sqlite` with transcripts
at each row's `rollout_path`. Check schema before querying: these are host
implementation details, not a public API. Use read-only access; if WAL locking
prevents a read, copy the DB together with WAL/SHM into private temporary storage.
Never rewrite history. Parent/child copies may have recaptured timestamps; stable
call IDs and declared lineage are stronger deduplication evidence.

Claude's local fallback is normally `$CLAUDE_CONFIG_DIR/projects/` with parent
JSONL, nested `subagents/` and referenced `tool-results/`. `history.jsonl` only
discovers prompts. Export/session APIs are preferable when available. Retention
and disabled persistence create gaps. Tolerate unknown events, report malformed
JSONL with file and line, and distinguish unavailable, empty and opaque content.
Generated summaries and old reports support selection; reading them is not a
fresh transcript audit.

## Resume prior work

**You own the resume point. Read the prior trail, don't redo it.**

1. Locate the prior trail. Use the retrieval guidance above. Stay within the requested workspace, topic and time window. Read the metadata overview and last messages first, then scan back for the decision points. Parse a long transcript in a subagent when delegation is available and authorized; otherwise read bounded relevant regions in the main thread. Keep the decision evidence and resume point.
2. Reconstruct operational state. The branch and worktree, what already landed (`git log`, `git diff` against the base), the open todos, the decisions made. The prior trail is authoritative input. Resist the bias to re-derive it.
3. Diff done vs pending. Compare what shipped against what was planned, name the resume point, do not re-run the prior repro or redo completed work. A "let me verify from scratch" pass means you're treating the trail as untrustworthy when it's authoritative.
4. Route the remaining work to the matching skill or playbook and pick the verdict: continue the execution, ship a finished recommendation, ratify or override a prior conclusion, or postmortem a failed run. The pickup playbook ends here. The routed playbook owns the rest.
5. Verify the inherited claims against the original goal on the real artifact. Check claims needed for the next action, such as the current branch, PR status or existing changes; do not repeat completed checks without a new change, failure or concrete unresolved risk. A passing prior self-report is not the proof.

**Reply:** where the prior agent stopped, what you inherited vs redid (ideally nothing redone), the resume point, and the outcome.
