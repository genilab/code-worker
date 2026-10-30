---
name: github-maintain
description: Perform one explicitly requested GitHub connection, status, versioned commit, or pull operation for a confirmed project.
metadata:
  source: core
  action: Connect, inspect, versioned commit, or pull one project on explicit request.
---

# Maintain GitHub

## Scope

Use this skill when the user says `GitHub {action}` for one confirmed project.
Supported actions are `status`, `connect {owner/repository}`, `commit`,
`commit version`, `commit minor version`, `commit major version`, and `pull`.
Every commit action generates a concise message from the changed files and
creates a GitHub-controlled semantic version release. It never synchronizes
automatically. Apply the portable
[version-control standard](docs/version_control.md).
Primary agent role: publication-agent.

## Workflow

1. Read `docs/plan.md`, the target project's `AGENTS.md`, and its main
   `INFO.md`. Confirm the exact project root and requested GitHub action.
2. For `status`, inspect and report the local Git root, origin, branch,
   upstream, working-tree state, and available ahead/behind information without
   changing state.
3. For `connect {owner/repository}`, inspect local Git and GitHub access. On
   the explicit request, initialize Git only at the confirmed project root,
   create the named GitHub repository only when it is absent and the user has
   explicitly selected public or private visibility, then configure a
   non-conflicting `origin`. Do not commit, push, or pull.
4. For a Code-worker commit action, first invoke
   `knowledge-base-maintain` to reconcile `knowledge/INFO.md` and the minimal
   README Topics table from verified topics, then invoke `readme-maintain`
   using the declared README profile. Then confirm the branch and upstream,
   inspect the changed files, and generate a concise factual commit message.
   Preview the proposed changed files, message, and next version before
   mutation. Commit and push the confirmed project changes, create and push an
   annotated semantic tag, then create a GitHub Release with generated notes.
5. Determine the requested version bump under the version-control standard.
   Use the latest GitHub semantic release/tag as the version authority; an
   explicitly requested initial version may override the default `v0.0.1`.
   Do not create a local VERSION file or changelog.
6. For `pull`, fetch remote information and report divergence. On the explicit
   request, fast-forward only when the working tree is clean and no merge or
   rebase is required.
7. Report factual resulting state, including any commit, version, release URL,
   or revision identifier,
   or escalate when the requested operation is unsafe or ambiguous.

## Constraints

- Never perform an action not explicitly named by the user.
- Never create a GitHub repository without an explicit public/private choice.
- Never replace an existing origin, amend, force-push, merge, rebase, reset,
  discard changes, or change branches.
- GitHub tags and releases are the authoritative version records; never create
  a local VERSION file or changelog.
- A commit action stages only the changed non-ignored files in the confirmed
  project root after previewing them; escalate an ambiguous or unsafe scope.
- Never synchronize automatically after local changes, connection, or on a
  schedule.
- Escalate missing authentication, insufficient permission, an ambiguous root,
  a different existing origin, unapproved files, a dirty tree, divergence, or
  any required merge or rebase.
