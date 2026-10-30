---
name: module-validate
description: Execute applicable verification and record factual module QA evidence.
metadata:
  source: project
  action: Verify a module.
---

# Validate Module

## Scope

Use this skill when a module's requirements, source, tests, or design change.
It produces a QA record linked to requirement, automated, integration,
edge-case, and manual evidence.
Primary agent role: test-engineer.

## Workflow

1. Read requirements, implementation, tests, design, and existing QA.
2. Run applicable checks and retain actual outcomes.
3. Update module QA and requirement traceability without concealing failures.

## Constraints

- Do not repair source code or rewrite requirements in this skill.
- Do not preserve a prior pass after relevant change.
