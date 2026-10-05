# Skill Plan — publish-version

## Summary

Publish the next semantic GitHub release from an already connected project repository.

## Description

This external skill calculates a requested major, minor, or patch release from
the current semantic Git tags, creates and pushes an annotated tag, then
publishes GitHub-generated release notes as the authoritative changelog.

## Script Requirements

- It must accept `major`, `minor`, or `patch` as the version bump and default to `patch`.
- It must treat `vMAJOR.MINOR.PATCH` Git tags and GitHub Releases as the sole version and changelog records.
- It must verify a standalone Git root, matching GitHub origin, clean working tree, GitHub authentication, and write permission before publication.
- It must refuse to publish when no commits exist since the preceding semantic tag, the target tag already exists, or a prerequisite check fails.
- It must create and push one annotated semantic tag and publish one GitHub Release with generated notes.
- It must return the actual GitHub Release URL and retain failures without claiming publication.
- It must not create a local version file or changelog, stage source changes, force-push, or delete existing release records.

## Delegation to Code

- Code must parse and compare semantic tags, calculate the requested next tag, and create safe Git and GitHub CLI command argument lists.
- Code must validate the selected project root, GitHub origin, clean state, GitHub authentication, write permission, existing tags, and commit range before mutation.
- Code must support a dry-run preflight and an explicit publish mode that tags, pushes, creates generated GitHub release notes, and obtains the release URL.

## Code Requirements

- It must calculate major, minor, and patch bumps from valid semantic Git tags.
- It must reject invalid bump levels, nested roots, non-GitHub origins, dirty trees, existing tags, and no-change release ranges.
- It must construct annotated-tag, tag-push, GitHub Release creation, and release-URL retrieval commands without shell interpolation.
- It must have executable test units for semantic version behavior, GitHub remote parsing, and publication command construction.
