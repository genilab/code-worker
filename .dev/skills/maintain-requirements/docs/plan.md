# Skill Plan — maintain-requirements

## Summary

Maintain one authoritative, GraphK-format requirements record for each target module.

## Description

This internal skill converts confirmed module behavior into independently
testable requirement rows and preserves their evidence links and recorded
status without making implementation or validation claims.

## Script Requirements

- It must create or revise exactly one `{module}_reqs.md` record for the selected module.
- It must use Req_id, Description, Verification, Test Unit, and Status columns for every requirement row.
- It must require a stable module prefix, independently testable behavior, verification question, and evidence link or N/A before finalizing a row.
- It must keep new or changed requirements PENDING until actual evidence supports COMPLETED or FAILED.
- It must preserve module boundaries and report incomplete requirement details rather than guessing them.

## Delegation to Code

- No code is delegated because selecting and clarifying module behavior requires project-specific judgment.
- Delegate a repeated deterministic table or reference check to code only when it emerges and add executable test units with it.

## Code Requirements

N/A
