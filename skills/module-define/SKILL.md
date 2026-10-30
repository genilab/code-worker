---
name: module-define
description: Define approved delivery modules, their dependencies, and gates.
metadata:
  source: project
  action: Define Modules.
---

# Define Modules

## Scope

Use this skill after project initialization to define modules, dependencies,
acceptance criteria, risks, owners, design work, test work, and gate state. It
produces the current delivery plan.
Primary agent role: orchestrator.

## Workflow

1. Read the approved charter and existing records.
2. Define small modules with inputs, outputs, dependencies, risks, tests, and owner roles.
3. Route unresolved scope or ordering decisions to the human reviewer.
4. Update the task board and traceability links.

## Implementation

Run `python3 src/code_worker.py define-modules --help`. The command registers
one named module with goal, dependencies, risks, and owner, then renders the
current delivery plan under `assets/docs/plan/`.

## Constraints

- Do not add requirements that are absent from the charter.
- Do not advance a module past an unmet gate.
