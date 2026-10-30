# Skill Plan — info-maintain

## Summary

Maintain the approved Code-worker root and skills INFO formats from
current project records and skill evidence.

## Description

`info-maintain` is an internal skill used after project records, managed
skills, or QA evidence change. It maintains the root `INFO.md` and the local
`skills/INFO.md` from authoritative records without modifying the evidence
that supplies them. The durable formats are defined in `info_format.md`.

## Script Requirements

- It must derive root navigation and the skills catalog from maintained records.
- It must preserve only Description, Entry Points, and Public Interfaces in
  the root INFO document.
- It must render `skills/INFO.md` as only `# SKILLS Info` and one table with
  Skill, Action, Status, Plan, and QA columns.
- It must display recorded validation status or PENDING without inventing a pass.
- It must link each listed skill, plan, and QA record using existing paths.

## Delegation to Code

- Future replacement code may automate record discovery, metadata extraction,
  status derivation, and Markdown rendering only after it implements the
  approved formats and has passing current validation.

## Code Requirements

- It must generate the root and skills INFO documents from current maintained records.
- It must render no retired sections or columns.
- It must read each skill's action and current QA status from its package.
- It must prove that missing evidence remains PENDING and no passing status is manufactured.
