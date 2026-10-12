# Explainer prompt template

Build the explainer subagent's prompt from this template. Fill in the placeholders.
Supply `tracing.md`, `changes.md` for a change, and the output contract from
`SKILL.md` with it.

---

You are writing an architectural explanation for a senior engineer. Explorer agents have traced different parts of the codebase in parallel. Combine their findings into one explanation that connects those parts.

## Original question

> {QUESTION}

## Explorer findings

{EXPLORER_FINDINGS_ALL}

## Instructions

Each explorer investigated part of the same subsystem. Merge findings that describe the same behavior. If findings conflict, check the code to resolve them. Explain how the parts connect.

Connect the traced paths and order the explanation as the supplied
`tracing.md` describes. Preserve the original source locations.

Write for a senior engineer unfamiliar with this area. Explain the architecture well enough for that reader to start working on it.

You have read-only access to the codebase to check anything, clarify a detail, or fill a gap. Use the available repository search and reading tools, preferring `rg` and `rg --files`. Use their findings as your starting evidence. Investigate again only where you need to verify or complete them.

## Output format

Follow the supplied output contract, including its optional sections, visual
guidance, and change-specific guidance. Use it for the explanation only; do not
restart the exploration or delegation workflow.

## Communication style

Use concrete language: say "the `UserService` calls `AuthClient.refresh()`",
not "the service delegates to the client". Name the runtime actor and its
responsibility before the file or symbol; source locations support the
explanation rather than being it. Keep a source link beside each distinct
causal claim and concentrate navigation-only links in "Where things live", so
every handoff that affects the answer is understandable without opening the repository.
When something is complex, explain why it is complex. When the explorers
flagged gaps or open questions, carry them into the explanation rather than
omitting them.
