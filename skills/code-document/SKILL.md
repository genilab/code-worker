---
name: code-document
description: Document and validate managed source code when code or test files need the code-worker documentation standard.
metadata:
  source: core
  action: Apply the shared documentation standard to skill code and tests.
---

# Document Code

## Scope

This is an internal skill. Use it when a managed source or test file is created,
changed, or checked for documentation quality. It is responsible only for
applying the code-worker documentation standard without changing behavior. Its
inputs are the source file and its owning project, module, or skill record, and
it produces documented source plus validation findings. It has no user activation
command; a calling workflow invokes it.
Primary agent role: skill-agent.

## Workflow

1. Read the completed `docs/plan.md`, the owning record, the source file, and the [source-code standard](docs/source_code_standard.md) to identify responsibility, interfaces, and boundaries.
2. Confirm the required project identity, root-relative path, source description, and AI-instruction boundaries are available; ask for clarification when they are missing or ambiguous.
3. Add or revise the standard header, retained license and attribution, and factual `AI instruction:` module overview before imports. Keep imports, public docstrings, comments, and control flow in the documented structure. Preserve interfaces and behavior.
4. Run `code/validate_code_documentation.py` for the selected source or project and produce the actual result for the calling workflow.

## Constraints

- Do not alter implementation behavior, public interfaces, licenses, or attribution unless separately requested.
- The documentation must be source-specific and factual: header identity, root-relative path, responsibility, principal interface or test subject, and meaningful boundaries.
- `AI instruction:` is maintainers' and coding agents' bounded context, not an end-user prompt. It must not invent requirements, request a behavior change, or override the owning records.
- Do not compress multi-step behavior into one-line statements or use comments to conceal an implementation change. Non-goals include design changes and requirement changes.
