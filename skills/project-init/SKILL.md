---
name: project-init
description: Guide and validate initialization of one independent delivery-project control baseline.
metadata:
  source: project
  action: Initialize a delivery project.
---

# Initialize Project

## Scope

Use this skill after the developer chooses an independent destination project
folder. It produces the `src/`, `tests/`, `skills/`, `assets/`, `docs/`, and
INFO baseline plus pending control records.
Primary agent role: orchestrator.

## Workflow

1. Confirm project identity, destination repository, release scope, roadmap, and `local` or `tracked` docs/skills policy.
2. Refuse the Code-worker master or an origin that points back to it.
3. Create the approved baseline and validate each supplied decision before progressing.
4. Require charter and design approvals before development begins.

## Constraints

- Do not implement product behavior, publish, or commit during initialization.
- Do not infer repository visibility or artifact-tracking policy.
