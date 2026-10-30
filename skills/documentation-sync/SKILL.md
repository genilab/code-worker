---
name: documentation-sync
description: Refresh selected INFO navigation from maintained documents and current evidence.
metadata:
  source: project
  action: Sync documentation navigation.
---

# Sync Documentation

## Scope

Use this skill when a selected documentation area needs its local INFO
navigation reconciled. It receives existing records and produces factual links
only.
Primary agent role: documentation-agent.

## Workflow

1. Read the selected records and current QA evidence.
2. Refresh the relevant INFO document using only existing targets.
3. Report missing evidence as pending or absent.

## Constraints

- This is not a Git synchronization.
- Do not create requirements, QA passes, or implementation claims.
