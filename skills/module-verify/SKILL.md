---
name: module-verify
description: Verify one module and record factual QA evidence.
metadata:
  source: project
  action: Verify {module}.
---

# Verify Module

## Scope

Use this skill when a module's requirements, source, tests, or design change.
It produces a QA record linked to requirement, automated, integration,
edge-case, and manual evidence.
Primary agent role: test-engineer.

## Workflow

1. Read requirements, implementation, tests, design, and existing QA.
2. Run applicable checks and retain actual outcomes.
3. Update module QA and requirement traceability without concealing failures.

## Implementation

Run `python3 src/code_worker.py verify --help`. An explicit command after
`--check` runs without a shell in the selected delivery project. Its exit code
and captured output are written to `assets/docs/qa/`; a nonzero result remains
`FAILED`.

## Constraints

- Do not repair source code or rewrite requirements in this skill.
- Do not preserve a prior pass after relevant change.
