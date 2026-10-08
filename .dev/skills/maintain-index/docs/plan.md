# Skill Plan — maintain-index

## Summary

Regenerate concise, evidence-based project and skill indexes.

## Description

`maintain-index` is an internal skill used after project records, managed
skills, or QA evidence change. It derives concise local navigation and a
skills catalog from those records without modifying the evidence that supplies
them.

## Script Requirements

- It must derive project navigation and the skills catalog from maintained records.
- It must display recorded validation status or PENDING without inventing a pass.
- It must show each skill, definition from its plan Summary, actual class, plan link, QA link, and separate PASSED, FAILED, or PENDING status.
- It must separate internal and external skills in the catalog.
- It must show the project's declared internal or external use.
- It must derive the project's Title, Tagline, Core Proposition, and Key Ideas from the project plan and show them in the project index.

## Delegation to Code

- Delegate record discovery, metadata extraction, status derivation, and Markdown index rendering to code.
- Code must generate `.dev/INDEX.md` and `.dev/skills/INDEX.md` from project-plan documentation and front matter, `SKILL.md` records, and actual QA evidence.

## Code Requirements

- It must generate both local indexes from current maintained records.
- It must read a skill definition from its discovery description and classify the skill from its packaged implementation.
- It must classify skills by role and render the required catalog fields for each section.
- It must read `project_use` from project-plan front matter and show it in the project index.
- It must read Title, Tagline, Core Proposition, and Key Ideas from the project plan and show them in the project index.
- It must prove that missing evidence remains PENDING and no passing status is manufactured.
