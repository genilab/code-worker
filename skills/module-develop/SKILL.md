---
name: module-develop
description: Develop one approved module through bounded work items.
metadata:
  source: project
  action: Develop {module}.
---

# Develop Module

## Scope

Use this skill only for a selected module with approved requirements, design,
and acceptance criteria. It delivers that module through bounded `src/`
changes, updated tests, and local check evidence.
Primary agent role: implementation-agent.

## Workflow

1. Read the selected requirement, design, test plan, and affected code.
2. Implement the smallest useful slice in `src/` and update `tests/`.
3. Run targeted local checks and hand evidence to `module-verify`.

## Implementation

Run `python3 src/code_worker.py develop --help` after source and test files
exist. The command records only files already under `src/` and `tests/`; it
does not write product code or certify QA.

## Constraints

- Do not broaden scope, approve design, or self-certify QA.
- Keep business rules outside presentation-only code.
