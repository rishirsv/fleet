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
