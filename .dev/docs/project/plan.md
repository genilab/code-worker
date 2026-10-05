---
project_name: code-worker
project_use: external
tagline: "An evidence-driven development template for codebase projects."
---

# Project Plan

## Overview

`code-worker` is an external, reusable template for projects that work with a
codebase. It keeps the target product separate from the local development
control system in `.dev/`, where plans, requirements, quality evidence, and
managed skills make work traceable. Its first target application is GraphK.

## Overall Requirements

- It must provide a reusable development-control structure for codebase projects without embedding target-product implementation in the template.
- It must plan a target from its intended result before implementation through the external `project-planning` workflow.
- It must keep target-product code in `src/` and target executable tests in `tests/` when a target product is present.
- It must maintain project architecture, release, roadmap, module requirements, and module QA as separate local records.
- It must create each `{module}_reqs.md` record through the internal [maintain-requirements](../../skills/maintain-requirements/SKILL.md) workflow and one `{module}_qa.md` quality record in its package folder for each target module.
- It must create every `{module}_qa.md` record through the internal [validate-module](../../skills/validate-module/SKILL.md) workflow.
- It must create, maintain, validate, and index managed skills using the authoritative minimal skill format.
- It must derive `.dev/INDEX.md` and `.dev/skills/INDEX.md` from maintained evidence rather than treating either index as evidence.
- It must maintain a user-facing root README from verified evidence because this project is declared external.
- It must publish its `.dev/` master control package with the GitHub template while the project-planning workflow keeps each target project's `.dev/` local and ignored.
- It must preserve traceability from planned requirement through implementation, executable test, validation, and recorded QA.
