# Shared GitHub Version-Control Standard

This standard is the portable GitHub/version-control package for an
agent-worker project. A project adopts it only when its owner selects GitHub
versioning during structure setup.

## Public Actions

- `GitHub status` inspects state without changing it.
- `GitHub connect {owner/repository}` initializes only the confirmed project
  root and configures a non-conflicting existing or newly approved remote.
- `GitHub commit` creates the default patch release.
- `GitHub commit version` or `GitHub commit minor version` creates a minor
  release.
- `GitHub commit major version` creates a major release.
- `GitHub pull` fetches and fast-forwards only a clean, non-divergent branch.

## Version Rules

GitHub semantic tags and releases are the sole version authority. Tags use
`vMAJOR.MINOR.PATCH`. The default initial release is `v0.0.1`; an explicitly
requested initial version is permitted. Each commit action previews the changed
files, generated factual message, and next version before mutation. It then
commits, pushes, creates an annotated tag, pushes the tag, and creates a GitHub
release with generated notes.

## Safety Rules

Synchronization is manual. Never force-push, amend, reset, rebase, merge,
discard changes, replace an origin, or change branches. Stop for a dirty tree,
divergence, missing authentication, a different origin, a required merge, or
an ambiguous project root.

## Transfer to Another Project

When GitHub versioning is selected during project setup, copy the complete
`github-maintain` package, including this reference, into the target's local
`skills/` folder. Add its row to `skills/INFO.md`, add the `GitHub {action}`
block to the target `AGENTS.md`, and describe the action in the target root
`INFO.md`. The target keeps its own remote, GitHub history, tags, releases, and
project-specific pre-commit reconciliation rules.
