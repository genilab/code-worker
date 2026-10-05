#!/usr/bin/env python3
##
## code-worker - Foundational development operating system.
## .dev/skills/connect-github/code/connect_github.py - Preflights and safely configures a project's GitHub origin remote.
##

"""
AI instruction:
- Provides GitHub repository association checks and explicit origin configuration through a command-line interface.
- Preserves repository boundaries and never initializes, pushes, or silently replaces a remote.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


SLUG = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
REMOTE_PATTERNS = (
    re.compile(r"^https://github\.com/(?P<slug>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?$"),
    re.compile(r"^git@github\.com:(?P<slug>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?$"),
    re.compile(r"^ssh://git@github\.com/(?P<slug>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?$"),
)
WRITE_PERMISSIONS = {"ADMIN", "MAINTAIN", "WRITE"}


class ConnectionError(RuntimeError):
    """Raised when a project cannot safely be associated with GitHub."""


@dataclass(frozen=True)
class ConnectionPlan:
    """Represent one checked GitHub association and its required remote change."""

    root: Path
    slug: str
    remote_url: str
    action: str


def run(command: list[str], cwd: Path) -> str:
    """Run one argument-list command and return its stripped standard output."""
    completed = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    if completed.returncode:
        message = completed.stderr.strip() or completed.stdout.strip() or "command failed"
        raise ConnectionError(f"{' '.join(command)}: {message}")
    return completed.stdout.strip()


def repository_root(project: Path) -> Path:
    """Return the Git root only when the selected project is that exact root."""
    resolved = project.resolve()
    root = Path(run(["git", "rev-parse", "--show-toplevel"], resolved)).resolve()
    if root != resolved:
        raise ConnectionError(f"{resolved} is nested inside Git repository {root}; select a standalone project root")
    return root


def validate_slug(slug: str) -> str:
    """Validate and normalize a GitHub owner/repository identifier."""
    normalized = slug.strip()
    if not SLUG.fullmatch(normalized):
        raise ConnectionError("GitHub repository must use owner/repository format")
    return normalized


def github_slug(remote_url: str) -> str | None:
    """Return an owner/repository slug for supported GitHub remotes."""
    for pattern in REMOTE_PATTERNS:
        match = pattern.fullmatch(remote_url.strip())
        if match:
            return match.group("slug")
    return None


def origin(root: Path) -> str | None:
    """Return the current origin URL, or None when it is not configured."""
    completed = subprocess.run(["git", "remote", "get-url", "origin"], cwd=root, capture_output=True, text=True, check=False)
    return completed.stdout.strip() if completed.returncode == 0 else None


def verify_github_access(root: Path, slug: str) -> None:
    """Require an authenticated GitHub CLI session with repository write permission."""
    run(["gh", "auth", "status", "--hostname", "github.com"], root)
    permission = run(["gh", "repo", "view", slug, "--json", "viewerPermission", "--jq", ".viewerPermission"], root).upper()
    if permission not in WRITE_PERMISSIONS:
        raise ConnectionError(f"GitHub permission for {slug} is {permission or 'unknown'}, not write-capable")


def build_plan(project: Path, slug: str, replace_origin: bool = False) -> ConnectionPlan:
    """Preflight one association without changing the project's Git configuration."""
    root = repository_root(project)
    target = validate_slug(slug)
    verify_github_access(root, target)
    remote_url = f"https://github.com/{target}.git"
    existing = origin(root)
    if existing is None:
        action = "add"
    elif github_slug(existing) == target:
        action = "unchanged"
    elif not replace_origin:
        raise ConnectionError(f"origin is {existing}; rerun with --replace-origin to replace it with {remote_url}")
    else:
        action = "replace"
    return ConnectionPlan(root=root, slug=target, remote_url=remote_url, action=action)


def apply(plan: ConnectionPlan) -> None:
    """Apply only the already-reviewed add or replacement operation."""
    if plan.action == "add":
        run(["git", "remote", "add", "origin", plan.remote_url], plan.root)
    elif plan.action == "replace":
        run(["git", "remote", "set-url", "origin", plan.remote_url], plan.root)


def main() -> int:
    """Print a connection preflight or apply its explicit remote change."""
    parser = argparse.ArgumentParser(description="Preflight or connect a standalone project to a GitHub repository.")
    parser.add_argument("slug", help="GitHub owner/repository")
    parser.add_argument("--project", type=Path, default=Path("."))
    parser.add_argument("--replace-origin", action="store_true", help="Allow replacing an existing different origin.")
    parser.add_argument("--apply", action="store_true", help="Apply the reviewed remote change.")
    args = parser.parse_args()
    try:
        plan = build_plan(args.project, args.slug, args.replace_origin)
        if args.apply:
            apply(plan)
        print(f"{plan.action.upper()} {plan.slug} {plan.remote_url}")
        return 0
    except ConnectionError as error:
        print(f"REFUSED: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
