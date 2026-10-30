# Plan

## Summary

Create or reconcile one confirmed agent-worker project structure through a
single safe workflow.

## Description

This skill replaces the separate structure-creation and structure-maintenance
workflows. It first establishes whether the target structure is absent or
already present, then creates missing approved elements or reconciles existing
navigation without overwriting material.

## Script Requirements

- It must confirm project identity, role, required structure, and external
  README need before changing a target.
- It must establish the target's graph-based multi-agent orchestration
  contract: an orchestrator, necessary agent roles, skill ownership and
  handoffs, and escalation boundaries, using `multiagent_project_model.md`.
- It must create required folders, `AGENTS.md` with the multi-agent
  orchestration contract, and main and local `INFO.md`
  documents when the target structure is absent.
- It must create `assets/images/` for approved infographics and
  `assets/reports/` for generated reports; other asset subfolders require a
  clearly named asset type.
- It must declare an `asset-agent` for the standard assets area, including
  ownership, skill routing, and the handoff to publication when a public asset
  reference is requested.
- It must reconcile missing required elements and stale navigation when the
  target structure exists.
- It must preserve unexpected or conflicting material and report it rather
  than deleting or overwriting it.
- It must distinguish permanent project structure from temporary migration
  material.
- It must ask whether the project adopts the shared GitHub/version-control
  package and, when selected, transfer its skill package, catalog row, and
  AGENTS and INFO action declarations without transferring another project's
  remote, history, tags, releases, or project-specific rules.
- It must record the owner-selected repository visibility and README profile
  in the target AGENTS file before README maintenance can occur.

## Delegation to Code

No code is delegated. Structure decisions require project-specific inspection
and human confirmation when a conflict exists.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
