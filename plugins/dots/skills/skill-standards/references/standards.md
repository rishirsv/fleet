# Skill standards

Use this standard to create, update, or review Dots skills. The environment's
default `skill-creator` and `plugin-creator` own schemas, initial files,
packaging, installation, and validation commands. This reference adds what
those tools do not cover: clear instructions and preserved behavior.

Contents:

- [How to apply this standard](#how-to-apply-this-standard)
- [Discovery](#discovery)
- [Structure and loading](#structure-and-loading)
- [Instructions that change behavior](#instructions-that-change-behavior)
- [Authority and stops](#authority-and-stops)
- [Revise an existing skill](#revise-an-existing-skill)
- [Completion and evidence](#completion-and-evidence)

## How to apply this standard

Apply the sections the job needs to the skill being authored or reviewed,
including every reference and prompt its future runs load. Encode task-specific
decisions in that skill; this reference is not a template, checklist, or
scoring system.

Most guidance here is judgment: follow it by default and adapt it when the
job, evidence, or target environment calls for a different shape. Items marked
**Requirement** hold unless host validity, repository instructions, or an
explicit user decision overrides them.

Apply the shared writing style to every description, instruction, reference,
and embedded prompt while drafting, not only at the end. Exact meaning and
required formats take priority over stylistic preferences.

## Discovery

The skill body loads only after selection, so it cannot correct a vague or
overlapping description. **Requirement:** state the complete selection
criteria in metadata.

- **Write short, narrow descriptions.** Use the form "<Does X>. Use when …"
  in the third person, in about 250 characters or fewer. Name the job and its
  trigger in words people naturally use. Hosts may truncate long descriptions
  before selection, and broad trigger lists load the skill for unrelated work.
- **Give each trigger one strong phrase.** Collapse synonyms instead of
  listing every way to ask for the same thing.
- **Add an exclusion only when it prevents a wrong choice** between this skill
  and a related one.
- **Treat description edits as behavior changes.** Recheck a request that
  should select the skill, a similar request that should not, a request for a
  related skill, and the invocation mode.
- **Follow the host invocation policy.** Let the default skill creator govern
  invocation settings and preserve existing user choices.

For a pull-request publishing skill:

- **Before:** "Publish a pull request. Use for code changes, Git, or GitHub work."
- **After:** "Publishes finished changes as a pull request. Use when the user
  asks to open or update a PR for review."

The narrower trigger keeps the publishing workflow out of ordinary code edits
and Git questions.

## Structure and loading

- **Keep the root `SKILL.md` a router.** It holds the purpose, essential
  constraints, the choice of workflow, and a pointer to each supporting file
  with the condition for reading it. A simple skill can stay in one file.
- **Point to references where they apply.** "Read the review reference for a
  source audit" lets a description edit skip the review method. A mandatory
  "read these files before every task" loads unrelated modes and manuals.
- **Keep references one level deep.** Link every reference directly from
  `SKILL.md`. A reference should not send the reader on to another reference;
  link shared files, such as `plugins/dots/references/*.md`, from `SKILL.md`
  with their loading condition. Agents follow nested links unreliably and may
  read only part of a chained file.
- **Start references over 100 lines with a short Contents list** so the agent
  can find the section it needs from a partial read.
- **Make each resource reachable.** Remove empty folders, placeholder files,
  broken links, unused scripts, and assets that no workflow uses.
- **Use real component names.** Document only skills, agents, tools, apps, and
  connectors the target package provides.
- **Describe composition accurately.** Loading another skill adds its
  instructions to the current agent, so say read, load, or apply. Reserve
  handoff, pass, and give for a real change of owner or context, such as a
  subagent, another task, or an external system.
- **Keep one owner for each instruction.** Link to the owner instead of
  copying a second version that can drift.
- **Keep development records outside the shipped skill.** Plans, research
  notes, rejected drafts, source collections, run history, and private
  examples belong with the maintainer's working files.
- **Keep secrets and local state out of skills.** Use the host's supported
  authentication, configuration, or state mechanism.
- **Enforce checkable rules with checks.** When a script, schema, or validator
  can enforce a rule, prefer it to prose and keep the prose for why and when.
  Put lookups, scoring arithmetic, and fixed formatting in data files or
  scripts, and leave the agent the judgment.

## Instructions that change behavior

The writing style covers general prose. These points are specific to
instructions an agent will execute.

- **Keep a sentence when it changes an action,** clarifies a decision or
  limit, or gives understanding the agent lacks. The target model is capable;
  add only the context it does not already have.
- **Leave room for judgment.** Specify the outcome, relevant context, and
  decision criteria. Prescribe an exact sequence only when order protects a
  concrete dependency, permission boundary, or fragile operation. Detailed
  itineraries for work the model already handles can make strong models worse.
- **Open with the work.** Name what the agent inspects, creates, changes, or
  decides. A promise about quality, confidence, or impact does not produce
  that property; state the mechanism that does, or remove the sentence.
- **Make the work concrete before making it shorter.** Write the actions,
  artifacts, roles, and decisions plainly, then remove repetition without
  substituting umbrella nouns or compressed policy language.
- **Use familiar terms only when they carry stable behavior.** A word such as
  `audit` can replace repeated explanation when it reliably activates the same
  method. Broad nouns such as evidence, confidence, or quality do not name a
  method.
- **Pair each prohibition with the behavior to use instead,** and keep
  prohibitions for real guardrails.
- **Write at normal volume.** Reserve capitals, `CRITICAL`, or stacked `must`
  for an instruction that an observed failure shows is underweighted, and put
  the reason beside it. Current models overreact to emphatic language, and
  when several lines are critical the markers stop carrying information. Write
  a real requirement as a requirement: `try to`, `if possible`, and `ideally`
  read as permission to skip it.
- **Attach the reason to the rule** when it helps the agent choose between
  plausible actions or understand a non-obvious constraint. The model
  generalizes from the reason. A bare list makes every rule look equally
  important, and its format may be copied into the output. Leave out reasons
  that only advertise the value of following the instruction.
- **Give one default.** Name the default path and when to depart from it
  instead of offering equal alternatives.
- **State each requirement directly.** Replace "you will be graded on" with
  the requirements the grader checks.
- **Specify output needs by audience.** When tone, length, or format affects
  usefulness, describe the reader and the required result. Prefer "answer only
  what the reader asked" to word counts, and keep an exact limit only when the
  deliverable or a consumer sets one.
- **Keep examples from becoming templates.** The target copies an example's
  length, tone, and structure. When an example teaches judgment, show
  contrasting cases and label them illustrative. Use a single exact example
  only when it pins a required format.
- **Make delegation conditional.** When parallel work benefits the recurring
  job, state which independent work can go to subagents, how much, and who
  integrates it. Keep simple work local and respect the host's agents and
  authorization.

## Authority and stops

- **Let user instructions override the skill.** Write requirements so the
  user's explicit request wins. When a stop or limit protects something, name
  what it protects, so an agent that must diverge from the request can name
  the skill file, quote the instruction, and explain how it applies.
- **Keep authorization concrete.** Continue work the request and session
  already authorize. Ask only for missing decisions that materially affect the
  result or for actions outside that scope, and prepare independent work
  first. Avoid "stop for review after the first implementation" and approval
  gates for reversible work.
- **State what happens when the task cannot proceed normally.** Say whether
  the agent asks, makes an assumption, preserves partial work, reports that it
  found nothing, or stops.
- **Leave routine verification to the agent.** Agents run relevant tests and
  checks unprompted, and instructions to verify cause repeated testing. Name a
  check only when the agent could not infer it: a specific script, a
  known-fail case, or a required receipt. Keep explicit permission for
  known-safe workflows the agent might otherwise hesitate to run.

## Revise an existing skill

Ask what the agent would do differently because a sentence exists. Delete it
in full only when it changes nothing and its removal loses no useful
explanation, emphasis, voice, or navigation. **Requirement:** compare the
revision with the original and keep its selection criteria, permissions,
required actions, exceptions, examples, output fields, and completion
conditions. If the original meaning is unclear, resolve it from source or
report the uncertainty; a paraphrase must not create new policy.

- **Shorten structurally first.** Remove obsolete branches, duplicated
  procedures, unnecessary templates, and unconditional ceremony before
  rewriting good local prose. Leave clear prose and wording the user asked to
  keep alone.
- **Keep context only the author has.** Audience, environment facts, tool and
  script contracts, the quality bar, hard judgment calls, and the reasons
  behind constraints are not pruning targets. Prune restatements of what the
  agent already does.
- **Account for the target model.** A workaround for an older model may now
  constrain useful judgment. Preserve operational invariants and treat
  uncertain behavioral benefits as hypotheses. Use a focused trial only when it
  would change the decision and the active workflow permits it.
- **Write current rules.** Remove incident IDs, PR numbers, past-tense
  narratives, and relative phrasing such as "now", "no longer", or "also
  counts"; the agent never saw the earlier version. Keep a pinned version,
  path, or flag only when the job depends on it, and check it against the
  current environment.
- **Combine rules that address the same cause.** When several conditions each
  answer one past incident, state their shared principle or add the missing
  context, then check that the revised rule still handles each case.
- **Use the environment as the source of truth.** Point to cheap authoritative
  sources such as configuration, schemas, directory structure, and `--help`.
  Keep the reason, convention, or failure pattern the environment cannot show.
- **Account for every removal.** Before finishing, list each removed mode,
  branch, decision rule, example, output field, and accepted passage, and
  search the package and repository for references to it, including tests,
  evaluations, docs, other skills, and scripts, then update or remove each one.
- **Judge by behavior.** **Requirement:** a shorter skill counts as better
  only when it preserves or improves capability, judgment, and writing
  quality. Line count alone is not evidence.

## Completion and evidence

- **Define done up front.** Specify the deliverable so the agent can tell done
  from not done, and make the condition cover all important work. "Every
  changed caller is accounted for" drives more useful work than "review the
  callers." For broad work, name the set that must be covered, such as every
  selected file, finding, caller, or required field.
- **Match proof to risk.** Open-ended work needs an outcome and decision
  criteria. Fragile work may need exact checks, scripts, or known-fail cases.
  For scripts or workflows whose failure handling is part of the contract,
  exercise both valid and failing inputs.
- **Requirement: report the result honestly.** Creating a file or calling a
  tool does not prove completion. Syntax, file existence, and schema checks
  prove structure only. A failed check must change the next action or the
  reported status. State remaining uncertainty instead of turning missing
  evidence into a success claim.
- **Use behavior as evidence.** Asking a model whether it needs an instruction
  does not show what the instruction does. Use a behavioral trial when a
  removal's effect is contested; if it regresses, restore the minimal form
  rather than the verbose original.
- **Trace important rules** to an explicit user requirement, repository
  contract, accepted output, observed failure, or credible domain source. Treat
  a generated example or one unexplained failure as a hypothesis, and keep a
  narrow correction narrow until repeated evidence supports a broader rule.
