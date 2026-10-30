# Authoritative Minimal Skill Format

This is the required format for every managed skill created or revised by
`skill-create`. It is deliberately minimal, but it must still describe enough
for an agent to select and execute the skill correctly.

## Naming

Every skill name uses lowercase `{target}-{action}` form. The package folder
and `name` front-matter value must match exactly: for example, `skill-create`,
`topic-create`, `info-show`, and `github-maintain`.

## Required Structure

```md
---
name: lowercase-hyphenated-name
description: Concise statement of what the skill does and when to use it.
metadata:
  source: core-or-project
  action: Bounded action performed by this external skill.
---

# Skill Title

## Scope

This is an internal or external skill. Use it when {trigger}. It is responsible
only for {bounded responsibility}. It receives {inputs} and produces {outcome}.
State its activation condition here.
Primary agent role: {lowercase-hyphenated-role}.

## Workflow

1. Read the completed `docs/plan.md`.
2. Confirm the request is in scope; ask for clarification when a required input,
   decision, or boundary is missing.
3. Perform the bounded operation.
4. Produce the expected outcome.
5. Maintain the required QA evidence.

## Constraints

- State the non-goals and operation boundary.
- State the code and test boundary.
- Do not add duplicate descriptive sections.

## Dependencies

- `another-managed-skill`
```

`## Dependencies` is optional and appears only when the workflow invokes another
managed skill. `metadata.action` is required for every local skill and supplies
the Skills Info Action value; it does not create an automatic user invocation.
`metadata.source` records the skill origin. Public user actions belong in
`AGENTS.md` and root `INFO.md`. No unsupported top-level front-matter fields
are allowed in a newly created or revised minimal skill.

## Required Meaning

The allowed sections must collectively state:

- The trigger or use condition.
- The bounded responsibility.
- The inputs.
- The expected outcome.
- The clarification or escalation condition.
- The non-goals.

The plan and QA evidence remain in `docs/`; deterministic implementation remains
in `code/`; executable test units remain in `tests/`. They are not copied into
`SKILL.md`.

`Primary agent role: {role}.` is required once in `## Scope`, as a complete
sentence on its own line. The role must be a capability node declared in the
owning `AGENTS.md` Agent graph. It identifies skill ownership and routing; it
does not represent an unsupported top-level front-matter field or prove that a
persistent external agent is deployed.
