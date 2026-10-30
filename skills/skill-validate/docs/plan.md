# Skill Plan — skill-validate

## Summary

Validate managed skills and refresh their QA evidence and catalog.

## Description

`skill-validate` is an internal skill used when one managed skill or the full
catalog needs current QA evidence. It selects named targets, runs format,
documentation, and executable-test checks, writes QA only from actual results,
and refreshes the skills catalog.

## Script Requirements

- It must run Codex's bundled skill validator and validate each selected
  skill's authoritative minimal format, local plan, QA structure, source
  documentation, and test evidence.
- It must validate the required trigger, responsibility, input, outcome, clarification, and non-goal statements for newly managed skills.
- It must write QA results from current checks and report PENDING or FAILED evidence without inventing a pass.
- It must accept `{skill}` or `all` and refresh the skills catalog after validation.
- It must reject a managed skill that does not use the authoritative minimal
  format, including the required `metadata.action` value and exactly one
  primary agent-role declaration in its Scope.

## Delegation to Code

- Delegate target selection, catalog discovery, validation execution, QA writing, and catalog refresh to code.
- Code must resolve one named selector or all skills, invoke the shared validator, write actual QA outcomes, and refresh the skills info.

## Code Requirements

- It must resolve one flat skill selector or discover every registered skill.
- It must invoke the shared validator and report each selected skill's format, documentation, and executable-test results.
- It must detect a missing or duplicate primary agent-role declaration.
- It must refresh `skills/INFO.md` after every validation run.
- It must prove selector handling and info refresh with executable test units.
