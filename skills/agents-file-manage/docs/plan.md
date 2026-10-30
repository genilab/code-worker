# Plan

## Summary

Create or maintain one project `AGENTS.md` through a single evidence-based
workflow.

## Description

This skill replaces separate creation and maintenance workflows. It establishes
whether `AGENTS.md` is absent or present, then creates an initial operating
contract or makes the smallest revision justified by confirmed project
decisions.

## Script Requirements

- It must confirm project identity, role, resource locations, and boundaries
  before creating or revising `AGENTS.md`.
- It must establish or preserve the graph-based multi-agent contract: a
  bounded orchestrator, agent-role graph, skill ownership and handoffs, and
  escalation rules, following `multiagent_project_model.md`.
- It must create a complete operating contract when the file is absent.
- It must preserve existing guidance and make only confirmed changes when the
  file is present.
- It must identify stale links, conflicting guidance, and decisions requiring
  escalation.
- It must distinguish operating guidance from durable knowledge and INFO
  navigation.
- It must not represent a capability role as a persistent external agent
  without an explicit deployment decision.
- It must record asset ownership and preservation boundaries when `assets/` is
  part of the managed project structure.

## Delegation to Code

No code is delegated. Evaluating project operating rules and ownership
boundaries requires project-specific review.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
