---
name: release-review
description: Evaluate release readiness from evidence without publishing a release.
metadata:
  source: project
  action: Review release.
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

## Implementation

Run `python3 src/code_worker.py review-release --help`. The command evaluates
module verification and documentation evidence, writes a review record, and
never commits, pushes, tags, or publishes.

## Constraints

- Do not commit, push, tag, or publish.
- Code existence alone is not release evidence.
