# Shared agent guidance

Read the repository instructions before editing. Follow its conventions,
commands, and release process; they take precedence for repository-specific work.

Complete requested work and relevant validation. Make reasonable choices; ask
only when blocked by missing information. Preserve unrelated changes and
machine-specific settings.

Keep changes focused and prefer existing tools and dependencies. Read changed
files, run relevant checks, and report changes, results, and limitations.

Use concise, purpose-based branch names, following repository convention.
Commit, push, publish, or install hooks only when requested or required by
the repository for the current task.

Keep secrets and personal machine details out of repositories. Edit maintained
source, not generated output or installed caches. Explain configuration choices
plainly and retain only user-selected settings.

On macOS, prefer available browser tools for interactive work. Before launching
Chrome, Chrome for Testing, or a browser runner from a shell, check Launch
Services and WindowServer access in that same execution context. If either is
denied, use browser tools or an already permitted context; do not retry the
launch or disable safety controls. `--no-sandbox` cannot remove parent shell
restrictions. Use isolated profiles and close only this task's processes.

When diagnosing Simulator errors, distinguish simulator and host services using
the crash report's process path and device coalition. Preserve other tasks'
devices: target the exact UUID; never use global shutdown, erase, or process-name
kills as cleanup. Back up affected state before repair; distinguish shutdown
timeouts from startup crashes.
