# QA — maintain-readme

## Summary

- Overall status: PASSED
- Scope: `maintain-readme` instruction script, plan, code, test units, and local QA evidence.
- Standard alignment: PASSED — Actual checks passed.
- Validation executed: standard alignment, format, documentation, requirement coverage, code documentation, and executable test checks.
- Result: Actual checks passed. Actual checks passed. N/A — no code portion is required.
- Outstanding gaps: None.

## Validation Execution

### Standard Alignment

- Executed: Codex skill-structure validation on `SKILL.md`.
- Checks: lowercase hyphenated folder name, matching YAML name, discovery description, one H1 title, and absence of unfinished instruction placeholders.
- Result: PASSED — Actual checks passed.

### Format

- Executed: managed skill-format validation on `SKILL.md` and `docs/plan.md`.
- Checks: discovery metadata; minimal Scope, Workflow, and Constraints structure; trigger, responsibility, input, outcome, clarification, and non-goal statements; role, activation, dependencies, and required plan structure.
- Result: PASSED — Actual checks passed.

### Documentation

- Executed: plan, instruction, and source-documentation validation.
- Checks: plan-to-instruction coverage and required code-documentation structure.
- Result: PASSED — Actual checks passed.

### Functionality

- Executed: each available executable test unit.
- Checks: code behavior and generated-skill workflow behavior.
- Result: N/A — N/A — no code portion is required.

## Requirement Traceability

### Script Requirements

- It must read `project_use` before deciding whether README maintenance applies. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must maintain the root README for an external project and leave an internal project unchanged unless directly requested. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must use only verified project evidence and preserve accurate existing README content. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must use the defined title, tagline, infographic, verified banners, What is, Why, Getting Started, and Examples layout. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must create or refresh the README when an external project is created, becomes external, or receives a direct request. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must report unavailable required facts or assets instead of fabricating content. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.

### Code Requirements

- N/A — N/A — No code requirement is declared.

## Executed Test Units

- N/A — no executable test unit is required.
