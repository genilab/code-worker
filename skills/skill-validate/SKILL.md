---
name: skill-validate
description: Validate one managed skill or the complete local catalog when current QA evidence is required.
metadata:
  source: core
  action: Validate a managed skill package.
---

# Validate Skill

## Scope

This is an internal skill. Use it when a managed skill needs current format,
documentation, code-test, and QA evidence. It is responsible only for checking
the selected named skill or full catalog against its local records. Its
inputs are a selector (`{skill}` or `all`) and current
skill packages, and it produces refreshed `docs/qa.md` records and a skills info.
It has no user activation command; a calling workflow invokes it.
Primary agent role: skill-agent.

## Workflow

1. Read the selected plan and confirm the selector names a managed flat skill and the required local records exist; ask for clarification when the intended target or missing evidence is ambiguous.
2. Run Codex's bundled `quick_validate.py` for the selected skill or catalog,
   then perform the documented Code-worker structural checks. Do not run
   deprecated validation code retained in migration storage.
3. Check the authoritative [minimal skill format](../skill-create/docs/skill_format.md),
   including exactly one primary agent-role declaration in each Scope, plan
   requirements, source documentation, and executable test units where code is
   delegated. Reconcile any legacy layout assumptions before relying on copied
   validation code.
4. Confirm that the root INFO document contains only Description, Entry Points,
   and Public Interfaces, and that `skills/INFO.md` contains only `# SKILLS
   Info` plus its `Skill`, `Action`, `Status`, `Plan`, and `QA` table.
5. Produce QA from the current checks, refresh the skills info, and report
   PENDING or FAILED results with actual evidence. Do not use deprecated
   automation to validate or overwrite the approved formats.

## Constraints

- Do not invent validation status, preserve a previous pass after changes, or change source artifacts to make validation pass.
- Every managed skill must use the authoritative minimal format.
- Non-goals include creating a skill, repairing its behavior, or deciding an unresolved requirement without user direction.

## Dependencies

- `code-document`
- `info-maintain`
