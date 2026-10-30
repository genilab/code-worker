# Maintain GitHub Plan

## Summary

Perform one explicit GitHub status, connection, versioned commit, or pull
action for a confirmed project without automatic synchronization.

## Description

This unified workflow replaces separate connection, status, up-sync, and
down-sync skills. Its action parameter keeps the user in control of every
state-changing step while providing one simple GitHub action. Every commit
generates a factual message and creates a semantic GitHub release.

For Code-worker commits, it first reconciles the knowledge catalog and
README Topics table, then applies the declared README profile before generating
the commit preview.

## Script Requirements

- It must accept `status`, `connect {owner/repository}`, `commit`, `commit
  version`, `commit minor version`, `commit major version`, and `pull`.
- It must confirm the exact project root before every operation.
- It must keep status read-only.
- It must initialize local Git only at the confirmed root and create a GitHub
  repository only with an explicit visibility choice.
- It must generate a concise factual commit message from the changed files.
- It must create a semantic GitHub release after a successful commit and push.
- It must default `commit` to a patch bump, use minor for `commit version` and
  `commit minor version`, and use major for `commit major version`.
- It must use GitHub releases and semantic tags as the sole version authority,
  with `v0.0.1` as the initial release when no prior release exists.
- It must pull only by safe fast-forward from a clean, non-divergent branch.
- It must refuse automatic synchronization and any destructive or
  history-rewriting operation.

## Delegation to Code

No code is delegated in this first Code-worker migration. The unified
workflow must be validated before deterministic command automation is
introduced.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
