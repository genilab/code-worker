---
name: maintain-index
description: Rebuild local project and skills indexes when maintained records or QA evidence change.
source: core
---

# Maintain Index

## Scope

This is an internal skill. Use it after project records, managed skills, or QA
evidence change. It is responsible only for deriving local navigation and the
skills catalog from authoritative records. Its inputs are current project plans,
skill definitions, and QA records, and it produces refreshed `.dev/INDEX.md` and
`.dev/skills/INDEX.md`. It has no user activation command; a calling workflow
invokes it.

## Workflow

1. Read the relevant maintained records and confirm they identify project use, skill source, definition, class, plan, and QA status; ask for clarification when a source is missing or ambiguous.
2. Run `code/maintain_index.py --project .` to derive both indexes from those records.
3. Check that internal and external skills are separated and each catalog row shows the skill, concise plan Summary, class, plan link, QA link, and separate actual status. External rows also show their action.
4. Produce the refreshed indexes and report source gaps as PENDING rather than inferring a result.

## Constraints

- Do not edit a requirement, plan, skill definition, or QA record to make an index look complete.
- Do not manufacture a passing status; the index reports recorded evidence only.
- Non-goals include creating skills, changing project behavior, and deciding missing source facts.
