# Drafts

Writing workflows for developing ideas, drafting, and revising prose while
preserving the writer's voice. Install through the repository's
[installation guide](https://github.com/rishirsv/fleet/blob/main/INSTALL.md).

## Get started

Select **Drafts**, provide an idea, notes, or a draft, and describe the result
you want. [Scribe](skills/scribe/SKILL.md) routes the plugin call. You can also
invoke it directly in Codex:

```text
Use $scribe to revise this essay for a reader who is new to the subject.
Keep my argument and examples; flag gaps before inventing new material.
```

Scribe chooses the smallest useful writing workflow and loads the selected
skill's instructions. It is the only automatically discoverable Drafts skill in
Codex; the other 13 skills remain available by explicit call or through Scribe.
Claude retains its native skill discovery behavior.

You can begin with existing material. A writing home is useful for keeping your
own `VOICE.md`, `STYLE.md`, examples, and drafts together; the plugin does not
supply your personal voice.

## Choose an editorial pass

| Task | Skill |
| --- | --- |
| Find an idea or draw out your thinking | [Brainstorm](skills/brainstorm/SKILL.md), [Interview](skills/interview/SKILL.md) |
| Organize material or write a draft | [Outline](skills/outline/SKILL.md), [Draft](skills/draft/SKILL.md) |
| Review the argument and structure | [Dev Edit](skills/dev-edit/SKILL.md) |
| Improve sentences or check the voice | [Line Edit](skills/line-edit/SKILL.md), [Voice Check](skills/voice-check/SKILL.md) |
| Get a reader's response or a readiness verdict | [Reader](skills/reader/SKILL.md), [Final Pass](skills/final-pass/SKILL.md) |

See [Scribe](skills/scribe/SKILL.md) for the full workflow. For a new writing
home, explicitly choose [Setup Project](skills/setup-project/SKILL.md) and a
destination outside the plugin source.
