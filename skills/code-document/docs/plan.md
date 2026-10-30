# Skill Plan — code-document

## Summary

Document and validate managed source and test code.

## Description

`code-document` is an internal skill used when managed source or test files
need the code-worker documentation standard. It reads the source and its owning
record, documents the source without changing its behavior, validates the
result, and reports actual gaps.

## Script Requirements

- It must apply the source-code standard: factual header, preserved license and attribution, `AI instruction:` module overview, readable import order, public docstrings, and purposeful comments to managed source and test files.
- It must preserve behavior, public interfaces, licenses, and attribution while documenting code.
- It must derive project identity and source description from maintained records rather than inventing them.
- It must validate the required documentation structure before reporting a result.

## Delegation to Code

- Delegate source discovery and documentation-shape checks to code.
- Code must validate a selected source file or all managed source for the required header and module overview.

## Code Requirements

- It must validate a named source file for the standard header and factual AI-instruction module-overview shape.
- It must discover managed source in skill `code/` and `tests/` folders, `src/`, and `tests/` when no source file is selected.
- It must prove valid and invalid documentation cases with executable test units.
