#!/usr/bin/env python3
##
## code-worker - Foundational development operating system.
## .dev/skills/connect-github/tests/test_connect_github.py - Test units for GitHub connection preflight behavior.
##

"""
AI instruction:
- Verifies URL parsing and no-write remote-change decisions for the connect-github skill.
- Uses temporary paths and mocks external commands; it does not contact GitHub or alter a real remote.
"""

import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


CODE = Path(__file__).resolve().parents[1] / "code" / "connect_github.py"
SPEC = importlib.util.spec_from_file_location("connect_github", CODE)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ConnectGithubTest(unittest.TestCase):
    """Validate deterministic connection choices without real GitHub operations."""

    def test_parses_supported_github_remote_urls(self) -> None:
        """Recognize HTTPS and SSH GitHub origins as the same repository slug."""
        self.assertEqual(MODULE.github_slug("https://github.com/acme/project.git"), "acme/project")
        self.assertEqual(MODULE.github_slug("git@github.com:acme/project.git"), "acme/project")
        self.assertIsNone(MODULE.github_slug("https://example.com/acme/project.git"))

    def test_rejects_nested_project_root(self) -> None:
        """Prevent an inner directory from configuring its parent's Git repository."""
        with patch.object(MODULE, "run", return_value="/workspace"):
            with self.assertRaises(MODULE.ConnectionError):
                MODULE.repository_root(Path("/workspace/inner"))

    def test_requires_explicit_replacement_for_different_origin(self) -> None:
        """Leave an existing different remote unchanged unless replacement is explicit."""
        with patch.object(MODULE, "repository_root", return_value=Path("/project")), patch.object(MODULE, "require_full_development_publication"), patch.object(MODULE, "verify_github_access"), patch.object(MODULE, "origin", return_value="https://github.com/acme/old.git"):
            with self.assertRaises(MODULE.ConnectionError):
                MODULE.build_plan(Path("/project"), "acme/new")

    def test_builds_add_plan_for_missing_origin(self) -> None:
        """Plan the canonical HTTPS origin when the project has none."""
        with patch.object(MODULE, "repository_root", return_value=Path("/project")), patch.object(MODULE, "require_full_development_publication"), patch.object(MODULE, "verify_github_access"), patch.object(MODULE, "origin", return_value=None):
            plan = MODULE.build_plan(Path("/project"), "acme/new")
        self.assertEqual(plan.action, "add")
        self.assertEqual(plan.remote_url, "https://github.com/acme/new.git")

    def test_rejects_application_project_policy(self) -> None:
        """Keep target applications from receiving a publishable GitHub remote."""
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            plan = root / ".dev/docs/project/plan.md"
            plan.parent.mkdir(parents=True)
            plan.write_text("---\nproject_type: application\npublication_policy: private\n---\n", encoding="utf-8")
            with self.assertRaisesRegex(MODULE.ConnectionError, "reserved for development projects"):
                MODULE.require_full_development_publication(root)


if __name__ == "__main__":
    unittest.main()
