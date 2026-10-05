# Skill Plan — create-skill

## Summary

Create or revise a managed skill from its completed local plan.

## Description

`create-skill` is an internal workflow that creates or revises a managed Agent
Skill. It begins with the completed target skill plan, creates the target
instruction script and only the supporting artifacts required by that plan,
then validates the result and refreshes the skills index. It may invoke
`document-code`, `validate-skill`, and `maintain-index`.

## Script Requirements

- It must create a named flat skill with `source: core` or `source: project` discovery metadata and only the support folders the operation needs.
- It must create a self-contained `docs/plan.md`, `docs/qa.md`, test starter when code is delegated, and an updated skills index.
- It must require a bounded action and workflow before creating a skill.
- It must require the completed target plan before creating or revising the target `SKILL.md`, code, or test units.
- It must create the target `SKILL.md` to cover every target Script Requirement.
- It must create every target `SKILL.md` in the authoritative ideal minimal Codex skill format: valid name and description metadata, one title, focused Scope, Workflow, Constraints, and Dependencies only when another managed skill is invoked.
- It must make each target `SKILL.md` minimally well-described by stating its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within the allowed sections.
- It must reject invalid names, groups, existing destinations, unsupported resources, and catchall or incomplete requests.
- It must apply the source-code standard whenever the target skill has code or test units, including the factual `AI instruction:` context block and readable code structure.
- It must preserve the role, activation, and associated workflow skills declared for the target skill.
- It must record actual validation evidence and refresh the skills index without manufacturing a passing status.

## Delegation to Code

- Delegate package scaffolding, input validation, folder creation, starter-record generation, and index refresh to code.
- Implement code that creates the approved package structure from the creation inputs.
- Delegate completed-skill validation to `validate-skill` after the target instruction script, delegated code, and test units have been created from the target plan.

## Code Requirements

- It must validate creation inputs and reject invalid names, groups, unsupported resources, and unavailable destinations.
- It must create the approved target skill folders, starter plan, QA record, instruction-script starter, and test starter when code is delegated.
- It must render the simplified plan format with Summary, Description, Script Requirements, Delegation to Code, and Code Requirements.
- It must render the ideal minimal Codex skill format and reject unfinished placeholders or duplicated legacy instruction sections.
- It must refresh `.dev/skills/INDEX.md` after scaffolding.
- It must validate managed skills for the current plan format, requirement coverage, code documentation, and executable test results.
