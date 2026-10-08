# Skill Plan — connect-github

## Summary

Connect one standalone project repository to its intended GitHub repository.

## Description

This external skill verifies that a selected project is its own Git repository,
confirms a GitHub repository and write access, and adds or explicitly replaces
the project's `origin` remote without publishing source changes.

## Script Requirements

- It must accept one GitHub `owner/repository` target and a project path.
- It must allow GitHub association only when the plan declares `project_type: development` and `publication_policy: full`.
- It must refuse to connect a directory that is not exactly a Git repository root.
- It must verify the target GitHub repository and authenticated write permission before changing `origin`.
- It must report an existing, different `origin` and require explicit replacement before changing it.
- It must use the canonical HTTPS GitHub remote and report the verified association after application.
- It must not initialize repositories, push content, create tags, or publish releases.

## Delegation to Code

- Code must determine the Git repository root, read and enforce the plan's project type and publication policy, parse supported GitHub remote URLs, validate a repository slug, inspect the existing `origin`, and invoke GitHub CLI preflight checks.
- Code must construct safe argument-list calls for adding or replacing `origin`, with a dry-run default and an explicit apply option.
- Code must return factual outcomes that the instruction workflow can present without inferring successful GitHub access.

## Code Requirements

- It must expose a command-line preflight for a project path and GitHub `owner/repository` target.
- It must reject nested project paths, invalid slugs, non-GitHub remotes, and an existing different origin without explicit replacement.
- It must refuse application projects and projects without `publication_policy: full`.
- It must add or replace `origin` only when explicitly requested and must emit the verified repository slug.
- It must have executable test units for URL parsing, root validation, and remote-change decisions.
