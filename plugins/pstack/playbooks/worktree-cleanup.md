### Worktree cleanup

1. Snapshot and audit. Record `df -h /`, then read paths from `git worktree list --porcelain`, never hand-typed. Inspect each candidate's size, age, branch, merge state against its actual PR base, tracked edits, untracked and ignored files, unpushed commits, PR state, and newest chat that touched it. Use [session history](../references/sessions.md#read-the-prior-trail) for chat evidence. A detached HEAD needs commit reachability checked explicitly.
2. The bucket is advice, not permission. The pinned and active chats are the real artifact. Get that set from the user or sidebar and cross-check every candidate. A missing chat record does not establish that a worktree is unused.
3. Verify usage before deleting. For every recent chat, or anything you doubt, read the relevant trail and identify which worktrees it touches. A pinned chat can spawn sibling worktrees through background subagents, and those are in use even when their names never hit the sidebar. Keep active, pinned, shared and primary worktrees.
4. Pause on irreversible loss. Show uncommitted work, untracked files, needed ignored files and commits without another recoverable reference before discarding them. Untracked does not mean throwaway. Clean and merged and not-in-use proceeds within a cleanup request. Uncertain ownership or unrecoverable work needs the user's decision.
5. Prune the confirmed set. For Codex-managed worktrees, use `list_artifacts` and `archive_worktree` with the exact returned identity. Preserve needed ignored files separately. The archive records a recoverable snapshot. For ordinary Git worktrees, use `git worktree remove <path>` without force. A refusal is new evidence to inspect, not permission to force removal or run `rm -rf`. Branch refs survive. Confirm with `df -h /` and re-list.

This is the one playbook that deletes user state with no code review to catch a slip, so the gates above are the review.

**Reply:** `df -h /` before and after with space reclaimed, the worktrees pruned, and a one-line reason for each held back (in-use by which chat, or uncommitted work).
