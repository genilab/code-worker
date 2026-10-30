---
name: requirements-define
description: Define testable requirements and acceptance criteria for one module.
metadata:
  source: project
  action: Define requirements {module}.
---

# Define Requirements

## Scope

Use this skill when a selected module needs requirements or acceptance criteria.
It produces a requirements matrix with traceability columns.
Primary agent role: requirements-analyst.

## Workflow

1. Read the accepted charter and delivery plan.
2. Define independently testable behavior, acceptance, exclusions, and evidence needs.
3. Preserve uncertainty for human decision and hand accepted requirements to architecture.

## Implementation

Run `python3 src/code_worker.py define-requirements --help`. The command
requires an existing module and stores one requirement ID, description, and
acceptance criterion in its module record and requirements document.

## Constraints

- Do not invent behavior or write implementation in this skill.
- New or changed requirements remain pending until actual evidence exists.
