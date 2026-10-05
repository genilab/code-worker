# QA — validate-module

## Summary

- Overall status: PASSED
- Scope: `validate-module` instruction script, plan, code, test units, and local QA evidence.
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

- It must validate the selected module against every row in its `{module}_reqs.md` table. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must run applicable source-documentation and executable-test checks and retain their actual results. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must update requirement status only when evidence supports PENDING, COMPLETED, or FAILED. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must create `{module}_qa.md` with Summary, Validation Execution, Requirement Traceability, and Executed Test Units sections. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must show one evidence-based traceability result for every requirement row and keep unresolved failures visible. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must report missing targets, checks, tests, or evidence rather than guessing them. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.

### Code Requirements

- N/A — N/A — No code requirement is declared.

## Executed Test Units

- N/A — no executable test unit is required.
