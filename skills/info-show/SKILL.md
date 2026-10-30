---
name: info-show
description: Open the Code-worker main or one confirmed local INFO document in the workspace editor.
metadata:
  source: core
  action: Show info [ALL | {topic}].
---

# Show Info

## Scope

Use this skill when the user says `Show info ALL` or `Show info {topic}`.
It opens the requested existing `INFO.md` in the workspace editor without
changing the workspace.
Primary agent role: information-agent.

## Workflow

1. For `Show info ALL`, open the root `INFO.md` in the workspace editor.
2. For `Show info {topic}`, resolve the named confirmed area and open its
   local `INFO.md` in the workspace editor.
3. State when the requested area has no INFO document or is ambiguous; do not
   create, infer, or modify information while showing it.

## Implementation

Run `python3 src/code_worker.py show-info --help`. The command prints the
confirmed root or topical `INFO.md` and leaves the project unchanged.

## Constraints

- This is read-only.
- Do not substitute README content for an INFO document.
- Do not treat temporary migration records as durable Code-worker info.
