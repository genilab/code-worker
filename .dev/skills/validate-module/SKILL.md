---
name: validate-module
description: Validate a target module and record evidence-based QA when its requirements, code, or tests change.
source: core
---

# Validate Module

## Scope

This is an internal skill. Use it when a target module needs current validation
evidence after its requirements, implementation, documentation, or tests
change. It is responsible only for validating the selected module and recording
its QA. Its inputs are `{module}_reqs.md`, relevant source and tests,
documentation-check output, and test output; it produces
`.dev/qa/{package}/{module}_qa.md`. It has no user activation command; a calling
workflow invokes it.

## Workflow

1. Read the module requirements table, source, tests, existing QA, and package location.
2. Confirm the target module, applicable checks, test units, and evidence locations are known; ask for clarification when they are missing or ambiguous.
3. Run applicable source-documentation and executable-test checks, retaining their actual output.
4. Update requirement status only when the resulting evidence supports PENDING, COMPLETED, or FAILED.
5. Create or regenerate the module QA record from current evidence, leave unresolved failures visible, and invoke `maintain-index` when navigation inputs change.

## Constraints

- Use this exact module-QA structure:

  ```md
  # QA — {module}

  ## Summary
  - Overall status: PASSED | FAILED | PENDING
  - Scope: `{module}` requirements, implementation, tests, and QA evidence.
  - Validation executed: {actual checks run}
  - Result: {concise evidence-based outcome}
  - Outstanding gaps: None. | {actual gaps}

  ## Validation Execution
  ### Requirement Alignment
  - Result: PASSED | FAILED | PENDING — {actual evidence}
  ### Implementation and Documentation
  - Result: PASSED | FAILED | PENDING | N/A — {actual evidence}
  ### Functionality
  - Result: PASSED | FAILED | PENDING | N/A — {actual evidence}

  ## Requirement Traceability
  - `{REQ-ID}` — {description from `{module}_reqs.md`} — PASSED | FAILED | PENDING — {concise evidence-based explanation}

  ## Executed Test Units
  - `{test-unit}`: PASSED | FAILED | PENDING | N/A — {actual result}
  ```

- Record one traceability bullet for every requirements-table row. Use N/A only when a check does not apply.
- Do not invent test output, preserve a previous pass after source or requirement changes, repair implementation, or silently alter requirements. Non-goals include requirements design and release decisions.

## Dependencies

- `document-code`
- `maintain-index`
