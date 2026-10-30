---
name: project-init
description: Guide and validate initialization of one independent delivery-project control baseline.
metadata:
  source: project
  action: Project init.
---

# Project Init

## Scope

Use this skill after the developer chooses an independent destination project
folder. It guides the developer through the charter, current release, roadmap,
baseline `src/`, `tests/`, `skills/`, `assets/`, `assets/docs/`, and INFO
records.
Primary agent role: orchestrator.

## Workflow

1. Confirm project identity, charter, destination repository, release scope, roadmap, and `local` or `tracked` assets/docs/skills policy.
2. Refuse the Code-worker master or an origin that points back to it.
3. Create the approved baseline and validate each supplied decision before progressing.
4. Require charter and design approvals before development begins.

## Implementation

Run `python3 src/code_worker.py project-init --help`. The command creates only
missing baseline records, refuses the Code-worker master or its origin, and
requires explicit identity, release, roadmap, visibility, and artifact-policy
values. It does not alter Git tracking, commit, or publish.

## Constraints

- Do not implement product behavior, publish, or commit during initialization.
- Do not infer repository visibility or artifact-tracking policy.
