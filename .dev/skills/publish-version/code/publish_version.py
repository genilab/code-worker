#!/usr/bin/env python3
##
## code-worker - Foundational development operating system.
## .dev/skills/publish-version/code/publish_version.py - Preflights and publishes semantic GitHub releases through annotated Git tags.
##

"""
AI instruction:
- Provides deterministic semantic-tag calculation and safe Git/GitHub CLI publication commands for the publish-version skill.
- Preserves repository boundaries, never stages source changes, and publishes only after all preflight checks pass.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


SEMVER = re.compile(r"^v(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)$")
REMOTE_PATTERNS = (
    re.compile(r"^https://github\.com/(?P<slug>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?$"),
    re.compile(r"^git@github\.com:(?P<slug>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?$"),
)
WRITE_PERMISSIONS = {"ADMIN", "MAINTAIN", "WRITE"}
PROJECT_TYPE = re.compile(r"^project_type:\s*(?P<value>\S+)\s*$", re.MULTILINE | re.IGNORECASE)
PUBLICATION_POLICY = re.compile(r"^publication_policy:\s*(?P<value>\S+)\s*$", re.MULTILINE | re.IGNORECASE)


class PublicationError(RuntimeError):
    """Raised when a release prerequisite or publication command fails."""


@dataclass(frozen=True, order=True)
class Version:
    """Represent one stable semantic version without prerelease support."""

    major: int
    minor: int
    patch: int

    def tag(self) -> str:
        """Return the canonical Git tag representation."""
        return f"v{self.major}.{self.minor}.{self.patch}"


def run(command: list[str], cwd: Path) -> str:
    """Run one safe argument-list command and return its stripped output."""
    completed = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    if completed.returncode:
        message = completed.stderr.strip() or completed.stdout.strip() or "command failed"
        raise PublicationError(f"{' '.join(command)}: {message}")
    return completed.stdout.strip()


def git_root(project: Path) -> Path:
    """Return the Git root only if it is the explicitly selected project root."""
    resolved = project.resolve()
    root = Path(run(["git", "rev-parse", "--show-toplevel"], resolved)).resolve()
    if root != resolved:
        raise PublicationError(f"{resolved} is nested inside Git repository {root}; select a standalone project root")
    return root


def require_full_development_publication(root: Path) -> None:
    """Allow release publication only for a declared full-publication development master."""
    plan = root / ".dev" / "docs" / "project" / "plan.md"
    if not plan.is_file():
        raise PublicationError("project plan must declare development/full publication before release publication")
    content = plan.read_text(encoding="utf-8")
    project_type = PROJECT_TYPE.search(content)
    policy = PUBLICATION_POLICY.search(content)
    if not project_type or project_type.group("value").lower() != "development":
        raise PublicationError("release publication is reserved for development projects; application projects remain local by default")
    if not policy or policy.group("value").lower() != "full":
        raise PublicationError("release publication requires publication_policy: full")


def github_slug(remote_url: str) -> str | None:
    """Extract a GitHub owner/repository slug from a supported origin URL."""
    for pattern in REMOTE_PATTERNS:
        match = pattern.fullmatch(remote_url.strip())
        if match:
            return match.group("slug")
    return None


def parse_tag(tag: str) -> Version | None:
    """Parse one stable vMAJOR.MINOR.PATCH tag, ignoring all other tags."""
    match = SEMVER.fullmatch(tag.strip())
    if not match:
        return None
    return Version(**{name: int(value) for name, value in match.groupdict().items()})


def latest_version(tags: list[str]) -> Version | None:
    """Return the highest stable semantic version from a collection of Git tags."""
    versions = [parsed for tag in tags if (parsed := parse_tag(tag)) is not None]
    return max(versions) if versions else None


def next_version(current: Version | None, level: str) -> Version:
    """Calculate the next major, minor, or patch version from the current tag."""
    if level not in {"major", "minor", "patch"}:
        raise PublicationError("bump must be major, minor, or patch")
    if current is None:
        return Version(1, 0, 0)
    if level == "major":
        return Version(current.major + 1, 0, 0)
    if level == "minor":
        return Version(current.major, current.minor + 1, 0)
    return Version(current.major, current.minor, current.patch + 1)


def origin_slug(root: Path) -> str:
    """Require an origin remote that names one public GitHub repository."""
    slug = github_slug(run(["git", "remote", "get-url", "origin"], root))
    if slug is None:
        raise PublicationError("origin must be a supported github.com remote; run connect-github first")
    return slug


def verify_github_access(root: Path, slug: str) -> None:
    """Require a GitHub CLI session with write permission on the exact origin repository."""
    run(["gh", "auth", "status", "--hostname", "github.com"], root)
    permission = run(["gh", "repo", "view", slug, "--json", "viewerPermission", "--jq", ".viewerPermission"], root).upper()
    if permission not in WRITE_PERMISSIONS:
        raise PublicationError(f"GitHub permission for {slug} is {permission or 'unknown'}, not write-capable")


def publication_commands(root: Path, tag: str, slug: str) -> list[list[str]]:
    """Return the mutation commands in their required, no-shell-interpolation order."""
    return [
        ["git", "tag", "-a", tag, "-m", f"Release {tag}"],
        ["git", "push", "origin", tag],
        ["gh", "release", "create", tag, "--repo", slug, "--title", tag, "--generate-notes", "--verify-tag", "--fail-on-no-commits"],
    ]


def preflight(project: Path, level: str) -> tuple[Path, str, Version | None, str]:
    """Validate release conditions and return the exact next tag without mutation."""
    root = git_root(project)
    require_full_development_publication(root)
    slug = origin_slug(root)
    if run(["git", "status", "--porcelain"], root):
        raise PublicationError("working tree is not clean")
    verify_github_access(root, slug)
    run(["git", "fetch", "--tags", "origin"], root)
    current = latest_version(run(["git", "tag", "--list"], root).splitlines())
    target = next_version(current, level).tag()
    if target in run(["git", "tag", "--list", target], root).splitlines():
        raise PublicationError(f"target tag {target} already exists")
    if current and run(["git", "rev-list", "--count", f"{current.tag()}..HEAD"], root) == "0":
        raise PublicationError(f"no commits exist since {current.tag()}")
    return root, slug, current, target


def publish(project: Path, level: str) -> str:
    """Create, push, and publish one preflighted tag, returning the GitHub Release URL."""
    root, slug, _, tag = preflight(project, level)
    for command in publication_commands(root, tag, slug):
        run(command, root)
    return run(["gh", "release", "view", tag, "--repo", slug, "--json", "url", "--jq", ".url"], root)


def main() -> int:
    """Run a dry-run preflight by default or publish with explicit --publish."""
    parser = argparse.ArgumentParser(description="Preflight or publish the next semantic GitHub release.")
    parser.add_argument("bump", nargs="?", default="patch", choices=("major", "minor", "patch"))
    parser.add_argument("--project", type=Path, default=Path("."))
    parser.add_argument("--publish", action="store_true", help="Create and push the tag and GitHub Release after preflight.")
    args = parser.parse_args()
    try:
        if args.publish:
            print(f"PUBLISHED {publish(args.project, args.bump)}")
        else:
            _, slug, current, target = preflight(args.project, args.bump)
            previous = current.tag() if current else "none"
            print(f"READY {slug} {previous} -> {target}")
        return 0
    except PublicationError as error:
        print(f"REFUSED: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
