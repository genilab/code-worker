# QA — validate-skill

## Summary

- Overall status: PASSED
- Scope: `validate-skill` instruction script, plan, code, test units, and local QA evidence.
- Standard alignment: PASSED — Actual checks passed.
- Validation executed: standard alignment, format, documentation, requirement coverage, code documentation, and executable test checks.
- Result: Actual checks passed. Actual checks passed. Actual checks passed.
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
- Result: PASSED — Actual checks passed.

## Requirement Traceability

### Script Requirements

- It must validate each selected skill's authoritative minimal format, local plan, QA structure, source documentation, and test evidence. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must validate the required trigger, responsibility, input, outcome, clarification, and non-goal statements for newly managed skills. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must write QA results from current checks and report PENDING or FAILED evidence without inventing a pass. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must accept `{skill}` or `all` and refresh the skills catalog after validation. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must reject a managed skill that does not use the authoritative minimal format. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.

### Code Requirements

- It must resolve one flat skill selector or discover every registered skill. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must invoke the shared validator and report each selected skill's format, documentation, and executable-test results. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must refresh `.dev/skills/INDEX.md` after every validation run. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must prove selector handling and index refresh with executable test units. — PASSED — Verified by the current code-documentation and executable-test checks.

## Executed Test Units

- `tests/test_validate_skills.py`: PASSED — Actual checks passed.
