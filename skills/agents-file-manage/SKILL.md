---
name: agents-file-manage
description: Create or maintain one project AGENTS.md from confirmed operating decisions.
metadata:
  source: core
  action: Create or maintain one standard `AGENTS.md`.
---

# Manage AGENTS File

## Scope

Use this skill when a project needs its initial `AGENTS.md` or when confirmed
changes affect its identity, navigation, permanent structure, operating rules,
shared resources, or boundaries. It produces a new or minimally revised
operating contract for one project.
Primary agent role: structure-agent.

## Workflow

1. Read `docs/plan.md`, relevant INFO documents, and the existing `AGENTS.md`
   if present. Confirm project identity, role, resource locations, local
   boundaries, its orchestrator, necessary agent roles, skill ownership,
   handoffs, asset ownership when `assets/` exists, and the decisions
   supporting any requested change.
2. If `AGENTS.md` is absent, create it with project identity, navigation,
   permanent-structure rules, the `Multi-agent orchestration` contract from
   [the graph-based model](../project-structure-manage/docs/multiagent_project_model.md),
   operating boundaries, and escalation conditions.
3. If `AGENTS.md` exists, make the smallest coherent revision supported by
   confirmed project decisions. Identify stale links or conflicts for review.
4. State what is shared, what is local, and what requires escalation.

## Constraints

- Do not invent product behavior, publication claims, external workflows, or
  unconfirmed operating rules.
- Do not use `AGENTS.md` as a replacement for INFO documents or knowledge
  records.
- Treat agent roles as capability nodes unless a user has explicitly approved
  an external-agent deployment and its authority.
- When the project has `assets/`, declare its asset-agent, the approved asset
  subfolders, preservation rule, and the asset-to-publication handoff.
- Do not move durable information into `AGENTS.md` or overwrite conflicting
  guidance without explicit authorization.
- Escalate missing project identity, ambiguous shared-resource ownership, or a
  material change to project role.
