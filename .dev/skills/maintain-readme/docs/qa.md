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

- It must read `project_type`, `publication_policy`, and `project_use` before deciding whether README maintenance applies. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must maintain the root README automatically for a development project with full publication and leave an application project unchanged unless directly requested. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must collect composition evidence from the project plan, architecture, release and roadmap records, module requirements, QA, existing README, and available assets, preserving accurate existing content. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must use the plan's Title, Tagline, Core Proposition, and Key Ideas; verified architecture and requirements; QA-backed claims; and real assets to compose the infographic, banners, What is, Why, optional Key Ideas, Getting Started, and Examples layout. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must ask the embedded audience, setup, example, public-capability, visual-asset, and support/contribution/license questions when the maintained records do not supply a required user-facing fact. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must create or refresh the README when a full-publication development project is created or receives a direct request, and it must never infer that an application is safe to publish. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.
- It must report unavailable required facts or assets instead of fabricating content. — PASSED — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.

### Code Requirements

- N/A — N/A — No code requirement is declared.

## Executed Test Units

- N/A — no executable test unit is required.
