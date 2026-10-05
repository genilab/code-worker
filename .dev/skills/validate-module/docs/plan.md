# Skill Plan — validate-module

## Summary

Validate one target module and write evidence-based module QA.

## Description

This internal skill reads a module requirements table, source documentation,
and executable test evidence, then records only the current results in the
module QA record.

## Script Requirements

- It must validate the selected module against every row in its `{module}_reqs.md` table.
- It must run applicable source-documentation and executable-test checks and retain their actual results.
- It must update requirement status only when evidence supports PENDING, COMPLETED, or FAILED.
- It must create `{module}_qa.md` with Summary, Validation Execution, Requirement Traceability, and Executed Test Units sections.
- It must show one evidence-based traceability result for every requirement row and keep unresolved failures visible.
- It must report missing targets, checks, tests, or evidence rather than guessing them.

## Delegation to Code

- No code is delegated because selecting module checks and interpreting project evidence requires project-specific judgment.
- Delegate repeated deterministic test discovery, execution, or QA rendering to code only when it emerges and add executable test units with it.

## Code Requirements

N/A
