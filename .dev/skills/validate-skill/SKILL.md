---
name: validate-skill
description: Validate one managed skill or the complete local catalog when current QA evidence is required.
source: core
---

# Validate Skill

## Scope

This is an internal skill. Use it when a managed skill needs current format,
documentation, code-test, and QA evidence. It is responsible only for checking
the selected named skill or full catalog against its local records. Its
inputs are a selector (`{skill}` or `all`) and current
skill packages, and it produces refreshed `docs/qa.md` records and a skills index.
It has no user activation command; a calling workflow invokes it.

## Workflow

1. Read the selected plan and confirm the selector names a managed flat skill and the required local records exist; ask for clarification when the intended target or missing evidence is ambiguous.
2. Run `code/validate_skills.py {skill} --project .` or `code/validate_skills.py all --project .`.
3. Check the authoritative [minimal skill format](../create-skill/docs/skill_format.md), plan requirements, source documentation, and executable test units where code is delegated.
4. Produce QA from the current checks, refresh the skills index, and report PENDING or FAILED results with actual evidence.

## Constraints

- Do not invent validation status, preserve a previous pass after changes, or change source artifacts to make validation pass.
- Every managed skill must use the authoritative minimal format.
- Non-goals include creating a skill, repairing its behavior, or deciding an unresolved requirement without user direction.

## Dependencies

- `document-code`
- `maintain-index`
