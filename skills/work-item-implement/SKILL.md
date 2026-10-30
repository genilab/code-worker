---
name: work-item-implement
description: Implement one approved smallest useful requirement slice.
metadata:
  source: project
  action: Implement a work item.
---

# Implement Work Item

## Scope

Use this skill only for a selected requirement with approved design and known
acceptance criteria. It produces a bounded `src/` change, updated tests, and
local check evidence.
Primary agent role: implementation-agent.

## Workflow

1. Read the selected requirement, design, test plan, and affected code.
2. Implement the smallest useful slice in `src/` and update `tests/`.
3. Run targeted local checks and hand evidence to `module-validate`.

## Constraints

- Do not broaden scope, approve design, or self-certify QA.
- Keep business rules outside presentation-only code.
