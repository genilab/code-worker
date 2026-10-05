---
name: maintain-requirements
description: Create or update a module requirements record when confirmed module behavior changes.
source: core
---

# Maintain Requirements

## Scope

This is an internal skill. Use it when a target module needs new, changed, or
clarified expected behavior. It is responsible only for the module's
requirements record. Its inputs are the project plan, module scope, confirmed
behavior, and existing evidence; it produces an authoritative
`{module}_reqs.md` table. It has no user activation command; a calling workflow
invokes it.

## Workflow

1. Read the project plan, module boundaries, existing requirements, and relevant implementation evidence.
2. Confirm the module prefix, independently testable behavior, verification question, and test-unit evidence are known; ask for clarification when any is missing.
3. Create or revise the single `{module}_reqs.md` record without merging unrelated module behavior.
4. Keep every row in the required table format and mark new or changed requirements PENDING until actual evidence supports a different status.
5. Produce the updated requirement record and invoke `maintain-index` when its navigation inputs change.

## Constraints

- Use this exact GraphK-style table for every target module:

  ```md
  # Requirements — {module}

  | Req_id | Description | Verification | Test Unit | Status |
  | --- | --- | --- | --- | --- |
  | {PREFIX}-1 | {one independently testable behavior} | {verification question} | {linked test record or N/A} | PENDING |
  ```

- Use a stable module prefix and sequential numeric suffix. Keep one independently testable behavior per row.
- Status is PENDING, COMPLETED, or FAILED and changes only from actual recorded test evidence. A test-unit link must point to real evidence or be N/A when no test can yet apply.
- Do not write implementation guesses, claim validation has occurred, change source behavior, or rewrite module QA. Non-goals include test execution and release decisions.

## Dependencies

- `maintain-index`
