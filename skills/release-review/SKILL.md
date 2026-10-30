---
name: release-review
description: Evaluate release readiness from evidence without publishing a release.
metadata:
  source: project
  action: Review release readiness.
---

# Review Release

## Scope

Use this skill when the current release may be complete. It produces a
traceability report, completed or failed checklist, and delivery summary.
Primary agent role: release-reviewer.

## Workflow

1. Read release scope, traceability, design, test, manual-review, docs, and hygiene evidence.
2. Mark each gate from actual evidence and retain unresolved gaps.
3. Request human release approval or return work to the responsible role.

## Constraints

- Do not commit, push, tag, or publish.
- Code existence alone is not release evidence.
