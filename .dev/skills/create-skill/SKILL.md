---
name: create-skill
description: Create or revise a managed code-worker skill from its completed local plan when a reusable workflow is needed.
source: core
---

# Create Skill

## Scope

Use this internal skill when code-worker needs a new or revised reusable,
bounded workflow. It accepts a defined skill intent and completed target plan,
then is responsible for producing a managed skill package with only the
artifacts that operation needs. It has no user activation command; a calling
workflow invokes it.

## Workflow

1. Define or complete the target `docs/plan.md` before authoring its instruction script, code, or test units. It must contain Summary, Description, Script Requirements, Delegation to Code, and Code Requirements; it is the source of truth.
2. Confirm the requested action is bounded and the required role, activation, inputs, expected outcome, dependencies, and code delegation are known. An external skill must declare that action in front matter. Ask for clarification when any of these is missing.
3. Read the owning project plan before authoring. A skill for a development project must preserve the master-versus-target boundary; a skill for an application project must keep `.dev/` local and must not introduce publication behavior unless a separately approved, policy-aware workflow owns it.
4. Run `code/create_skill.py` to create only the target package folders required by the plan, its pending QA record, and an index entry.
5. Create or revise the target `SKILL.md` in the minimal format. State when to use it, what it receives, what it produces, its decision or escalation conditions, and its boundaries. Cover every Script Requirement; implement and test only the deterministic work stated in Delegation to Code and Code Requirements.
6. Apply `document-code` and its [source-code standard](../document-code/docs/source_code_standard.md) to every target code and test file: factual header, retained license, `AI instruction:` context block, readable structure, public docstrings, and purposeful comments. Then use `validate-skill` to regenerate `docs/qa.md` from actual checks and `maintain-index` to refresh the catalog.

## Constraints

- Reject unbounded, duplicate, incomplete, or unsupported skill requests.
- Keep generated skills narrow. Their plan and QA evidence belong in `docs/`; deterministic implementation belongs in `code/`; executable test units belong in `tests/`; optional prompt resources belong in `scripts/`.
- Use the authoritative [minimal skill format](docs/skill_format.md) for every newly created or revised managed skill. Do not add duplicate headings; include the operation's trigger, responsibility, inputs, outcome, clarification conditions, and non-goals in the allowed sections. Every external skill must include its bounded `action` in front matter.
- Do not record a passing QA status after a change until actual validation runs again.

## Dependencies

- `document-code`
- `validate-skill`
- `maintain-index`
