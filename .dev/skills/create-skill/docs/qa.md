# QA — create-skill

## Summary

- Overall status: PASSED
- Scope: `create-skill` instruction script, plan, code, test units, and local QA evidence.
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

- It must create a named flat skill with `source: core` or `source: project` discovery metadata and only the support folders the operation needs. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must create a self-contained `docs/plan.md`, `docs/qa.md`, test starter when code is delegated, and an updated skills index. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must require a bounded action and workflow before creating a skill. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must require the completed target plan before creating or revising the target `SKILL.md`, code, or test units. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must create the target `SKILL.md` to cover every target Script Requirement. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must create every target `SKILL.md` in the authoritative ideal minimal Codex skill format: valid name and description metadata, one title, focused Scope, Workflow, Constraints, and Dependencies only when another managed skill is invoked. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must make each target `SKILL.md` minimally well-described by stating its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within the allowed sections. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must reject invalid names, groups, existing destinations, unsupported resources, and catchall or incomplete requests. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must apply the source-code standard whenever the target skill has code or test units, including the factual `AI instruction:` context block and readable code structure. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must preserve the role, activation, and associated workflow skills declared for the target skill. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must record actual validation evidence and refresh the skills index without manufacturing a passing status. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.

### Code Requirements

- It must validate creation inputs and reject invalid names, groups, unsupported resources, and unavailable destinations. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must create the approved target skill folders, starter plan, QA record, instruction-script starter, and test starter when code is delegated. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must render the simplified plan format with Summary, Description, Script Requirements, Delegation to Code, and Code Requirements. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must render the ideal minimal Codex skill format and reject unfinished placeholders or duplicated legacy instruction sections. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must refresh `.dev/skills/INDEX.md` after scaffolding. — PASSED — Verified by the current code-documentation and executable-test checks.
- It must validate managed skills for the current plan format, requirement coverage, code documentation, and executable test results. — PASSED — Verified by the current code-documentation and executable-test checks.

## Executed Test Units

- `tests/test_create_skill.py`: PASSED — Actual checks passed.
- `tests/test_validate_skill.py`: PASSED — Actual checks passed.
