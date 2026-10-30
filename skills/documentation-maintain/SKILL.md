---
name: documentation-maintain
description: Maintain factual documentation and INFO navigation for all or one module.
metadata:
  source: project
  action: Maintain documentation [ALL | {module}].
---

# Maintain Documentation

## Scope

Use this skill when all project documentation or one module's documentation
needs reconciliation. It receives existing records and produces factual
documentation, asset references, and INFO navigation only.
Primary agent role: documentation-agent.

## Workflow

1. Resolve `ALL` or the selected module, then read its records and current QA evidence.
2. Refresh the relevant documentation, asset references, and INFO document using only existing targets.
3. Report missing evidence as pending or absent.

## Implementation

Run `python3 src/code_worker.py maintain-documentation --help`. The command
checks local Markdown links for the selected scope and writes a factual audit
to `assets/reports/documentation/`; it does not invent lifecycle evidence.

## Constraints

- This is not a Git synchronization.
- Do not create requirements, QA passes, or implementation claims.
