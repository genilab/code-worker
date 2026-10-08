---
name: publish-version
description: Publish the next semantic GitHub release for a connected project when a major, minor, or patch version is requested.
source: project
action: "Publish a semantic version to GitHub."
---

# Publish Version

## Scope

This is an external skill. Use it to publish the next GitHub release for a
connected, standalone project repository. It is responsible only for semantic
version calculation, an annotated Git tag, and a GitHub Release with generated
notes. Its inputs are the project path, requested major/minor/patch level, Git
history, and GitHub credentials; its outcome is a release URL or a factual
failure. User activation command: `Commit this version [major|minor|patch]`;
the default is `patch`.

## Workflow

1. Confirm the requested bump level, target project, standalone Git-root status, `project_type: development`, `publication_policy: full`, connected GitHub origin, clean working tree, and authenticated write permission; ask for clarification when any is missing or ambiguous.
2. Run preflight in dry-run mode to fetch tags, calculate the next semantic tag, and confirm there are changes since the prior tag.
3. On this explicit user activation, run the publish operation: create and push an annotated tag, then create the GitHub Release using generated notes.
4. Retrieve the published release URL and record only actual command outcomes in QA or release evidence.

## Constraints

- Tags in `vMAJOR.MINOR.PATCH` format are the sole version source; do not create or maintain a local `VERSION` file or `CHANGELOG.md`.
- The workflow must refuse an application project, a project without full publication, a nested or unconnected project, dirty working tree, invalid version history, missing GitHub CLI authentication, insufficient permission, an existing target tag, or no new commits.
- It must not stage or commit arbitrary working-tree changes, force-push, delete tags or releases, or publish a different repository. Non-goals include source modification and non-GitHub deployment.
- Use an annotated local tag, push that exact tag, and require GitHub to verify the remote tag before publishing generated release notes.

## Dependencies

- `connect-github`
- `document-code`
- `maintain-index`
