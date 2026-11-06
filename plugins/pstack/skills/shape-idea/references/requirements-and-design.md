# Requirements and design

## Intake and brief

Look up the facts in the product, code, docs, research, or data that are
available and relevant. Ask the owner for choices, preferences, and missing
facts that would change the output. Group independent questions in a round.
Defer questions that depend on an answer from that round. Follow the user's
format. By default, give each question a number, a short title, and a separate
recommended answer so the owner can accept the round or correct individual
items. Narrow vague answers with a concrete choice. Record delegated choices
as assumptions.

The brief covers the product and reason to rethink it, primary users, other
stakeholders, executive audience, sources and access gaps, and constraints
such as time, team, technical limits, and exclusions. Propose four to six
expert roles suited to the product, including roles likely to disagree.
Record what confirmation settles and carry open evidence gaps forward.

## Compare and challenge the designs

Write each option as an executive-readable thesis plus the change to the same
hero journeys and its tradeoff. For an interaction choice, use
[Exhibits](exhibits.md) to show the same task in comparable variants, ideally
behind one switcher. Verify the exhibit on the relevant surface. If a fact
could change the decision, test it with the smallest runnable prototype or
probe. Say what the artifact showed and which claims remain open.

Have each expert role challenge the options with specific cases. Show where
roles disagree, what changed as a result, and which claims need real evidence.
When simulating stakeholder interviews, cover each group's goals, friction,
conditions for adoption or support, and conflicts with other groups. Summarize
the hypothesis changes and write a short guide to test them with real people.

State the vision as a north star, three to five design principles, changes
for each group, exclusions, and success measures. For each grading round,
show the grades, largest gaps, and resulting revisions. Present the final
vision in full. Grade the quality of the proposal against the rubric and
label criteria whose outcomes still need validation.

## Spec handoff

Use approved `intent.md` as the source for the problem, desired outcome, and
accepted decisions. If approval is missing, surface the unresolved choice and
obtain it before drafting a spec for handoff. Use the repository's product,
design, engineering, and policy guidance that applies. If a requirement
conflicts with a constraint, state the impact and who needs to decide. Carry
unresolved questions into the spec with what each blocks.

Save the spec alongside the intent or at the user's requested location. In
Product rethink, cover three to five hero flows from trigger to outcome, with
differences from today. Give each user story a flow, a priority, and checkable
acceptance criteria. Include dependencies, consequential edge states, and
how to verify the outcome on the relevant surface. Scale the spec to the scope
when used on its own. Flag evidence still needed and preserve the distinction
between an approved direction and a measured result.

For the Product rethink handoff, summarize the problem, vision, hero flows,
success measures, top risks, and next decision in one page. Include a short
implementation prompt that points to both files and names the verification
expected from the build. Present the spec for owner review.

[Claude Academy requirements and design lesson](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design)
describes the approved-intent-to-spec handoff. The
[Cursor pstack design guide](https://github.com/cursor/plugins/blob/main/pstack/docs/guide/04-design.md)
describes comparing prototypes and testing open questions before committing to a design.
