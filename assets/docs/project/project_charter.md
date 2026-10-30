# Project Charter — Code-worker

## Status

**DRAFT — awaiting human approval.**

## Purpose

Provide an orchestrated multi-agent operating system that helps developers
build software faster while retaining control, auditability, traceability, and
well-documented evidence.

## Objectives

- Guide projects from charter through approved release.
- Keep each requirement traceable through design, implementation,
  verification, and documentation.
- Separate implementation from testing, visual review, documentation, and
  release review.

## Users and use cases

Developers initialize an independent project from Code-worker, use its guided
workflow to plan and deliver a release, and choose whether their local control
records are tracked in their project repository.

## Constraints and exclusions

- Human approval is required for scope, design, high-impact tradeoffs, manual
  acceptance, external publication, and release.
- Code-worker does not receive commits or releases from delivery projects.
- Each delivery project selects its repository visibility and artifact-tracking
  policy during `Project init`; Code-worker itself is not a delivery target.

## Success criteria

The pilot project can demonstrate complete purpose-to-documentation
traceability and a human-approved release-review result.
