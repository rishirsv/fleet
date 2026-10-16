# Shared agent guidance

Read the current repository's instructions before changing files. Follow its
conventions, commands, and release process; repository-specific instructions
take precedence over this shared guidance.

Complete the requested work, including relevant validation. Make reasonable
implementation choices and ask only when missing information blocks progress.
Preserve unrelated working-tree changes and machine-specific settings.

Keep changes focused. Prefer existing tools and dependencies. Read changed
files directly and run checks appropriate to the behavior changed. Report what
changed, what passed, and any remaining limitation.

Use concise, purpose-based branch names such as `fix/<description>` or
`feature/<description>` unless the repository specifies another convention.
Commit, push, publish, or install Git hooks only when the user requests it or
the current repository explicitly defines that action as part of the request.

Keep secrets and personal machine details outside repositories. Edit maintained
source instead of generated output or installed caches. Explain configuration
choices in plain language and keep only settings the user selected.

On macOS, prefer available browser tools for interactive browser work. Before
launching Chrome, Chrome for Testing, or a browser test runner directly, check
Launch Services and WindowServer access in the same execution context. If either
is sandbox-denied, stop that launch path and use an available browser tool or an
execution context already permitted by the task. Do not repeat a failing launch
or disable safety settings; Chrome's `--no-sandbox` cannot remove the parent
shell's restrictions. Use isolated browser profiles and close only processes
owned by the current task.

When diagnosing Simulator errors, distinguish simulator services from host
services using the crash report's process path and device coalition. Preserve
other tasks' devices and target an exact device UUID; never use global simulator
shutdown, erase, or process-name kills as cleanup. Back up affected state before
a repair, and treat shutdown timeout reports separately from startup crashes.
