# Authoritative Minimal Skill Format

This is the required format for every managed skill created or revised by
`create-skill`. It is deliberately minimal, but it must still describe enough
for an agent to select and execute the skill correctly.

## Required Structure

```md
---
name: lowercase-hyphenated-name
description: Concise statement of what the skill does and when to use it.
source: core-or-project
action: Bounded action performed by this external skill.
---

# Skill Title

## Scope

This is an internal or external skill. Use it when {trigger}. It is responsible
only for {bounded responsibility}. It receives {inputs} and produces {outcome}.
State its activation condition here.

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
managed skill. `action` is required for external skills and omitted for internal
skills. No other top-level sections are allowed in a newly created or revised
minimal skill.

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
