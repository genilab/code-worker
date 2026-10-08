---
name: connect-github
description: Associate an existing standalone project repository with its intended GitHub repository before publication.
source: project
action: "Connect a project repository to GitHub."
---

# Connect GitHub

## Scope

This is an external skill. Use it when an existing project needs an `origin`
remote for a specified GitHub `owner/repository` before a release can be
published. It is responsible only for verifying the association and, when the
user requests application, configuring that remote. Its inputs are the project
path, target repository, local Git state, and GitHub authentication; its outcome
is a verified association or a clear refusal. User activation command:
`Connect GitHub {owner/repository}`.

## Workflow

1. Confirm the target project is exactly its own Git repository root, declares `project_type: development` and `publication_policy: full` in its plan, the GitHub slug is complete, and the user has requested connection; ask for clarification when any is ambiguous.
2. Run the code preflight to inspect the project root, existing `origin`, GitHub repository visibility, and authenticated write permission.
3. Report the proposed remote change without changing Git configuration when the existing origin differs or the check fails.
4. Apply the remote change only with the explicit replacement option, then rerun preflight and report the verified repository slug.

## Constraints

- The workflow must reject an application project, a non-full publication policy, a directory nested inside another repository, a non-GitHub remote, an unavailable GitHub repository, or insufficient write permission.
- It must not initialize a repository, push commits, alter branches, or replace an existing `origin` without the user's explicit request. Non-goals include version publishing and release-note generation.
- Use `https://github.com/{owner}/{repository}.git` as the configured origin and retain actual command failures in the outcome.

## Dependencies

- `document-code`
- `maintain-index`
