---
name: skill-create
description: Create or revise a managed local skill from its completed plan when a reusable workflow is needed.
metadata:
  source: core
  action: Create or revise a managed skill.
---

# Create Skill

## Scope

Use this internal skill when Code-worker needs a new or revised reusable,
bounded workflow. It accepts a defined skill intent and completed target plan,
then is responsible for producing a managed skill package with only the
artifacts that operation needs. It has no user activation command; a calling
workflow invokes it.
Primary agent role: skill-agent.

## Workflow

1. Define or complete the target `docs/plan.md` before authoring its instruction script, code, or test units. It must contain Summary, Description, Script Requirements, Delegation to Code, and Code Requirements; it is the source of truth.
2. Confirm the requested action is bounded and its primary executing agent
   role, activation, inputs, expected outcome, dependencies, handoffs, and
   code delegation are known. Every local skill must declare its catalog
   action in supported front-matter metadata and its primary agent role in its
   Scope. Ask for clarification when any of these is missing.
3. Read the owning `AGENTS.md` and relevant `INFO.md` files before authoring.
   Confirm that the action belongs in the shared base rather than in a
   project-specific workspace.
4. Create only the target package folders required by the plan, its pending QA
   record, and one `skills/INFO.md` entry that follows the five-column format
   in [the info-format standard](../info-maintain/docs/info_format.md). The
   copied scaffold script is migration material until it is reconciled to the
   `skills/` layout.
5. Create or revise the target `SKILL.md` in the minimal format. State when to use it, its primary agent role, what it receives, what it produces, its decision or escalation conditions, handoffs, and its boundaries. Cover every Script Requirement; implement and test only the deterministic work stated in Delegation to Code and Code Requirements.
6. Apply `code-document` and its [source-code standard](../code-document/docs/source_code_standard.md) to every target code and test file: factual header, retained license, `AI instruction:` context block, readable structure, public docstrings, and purposeful comments. Then use `skill-validate` to regenerate `docs/qa.md` from actual checks and `info-maintain` to refresh the catalog in its approved format.

## Constraints

- Reject unbounded, duplicate, incomplete, or unsupported skill requests.
- Keep generated skills narrow. Their plan and QA evidence belong in `docs/`; deterministic implementation belongs in `code/`; executable test units belong in `tests/`; optional prompt resources belong in `scripts/`.
- Use the authoritative [minimal skill format](docs/skill_format.md) for every
  newly created or revised managed skill. Do not add duplicate headings;
  include the operation's trigger, responsibility, inputs, outcome,
  clarification conditions, and non-goals in the allowed sections. Every local
  skill must include its bounded `metadata.action` value and exactly one
  primary agent role that is declared by the owning `AGENTS.md` graph.
- Do not claim that a role is a persistent external agent unless its deployment
  and authority have been explicitly confirmed.
- Do not record a passing QA status after a change until actual validation runs again.

## Dependencies

- `code-document`
- `skill-validate`
- `info-maintain`
