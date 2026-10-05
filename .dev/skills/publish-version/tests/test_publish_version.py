#!/usr/bin/env python3
##
## code-worker - Foundational development operating system.
## .dev/skills/publish-version/tests/test_publish_version.py - Test units for semantic GitHub publication behavior.
##

"""
AI instruction:
- Verifies semantic version calculation and safe publication-command construction for the publish-version skill.
- Does not contact GitHub, create tags, or mutate any Git repository.
"""

import importlib.util
import sys
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parents[1] / "code" / "publish_version.py"
SPEC = importlib.util.spec_from_file_location("publish_version", CODE)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PublishVersionTest(unittest.TestCase):
    """Verify deterministic release behavior without external side effects."""

    def test_finds_highest_stable_tag(self) -> None:
        """Ignore non-semantic tags while selecting the highest stable version."""
        self.assertEqual(MODULE.latest_version(["v1.0.0", "v1.10.0", "draft", "v2.0.0-beta"]).tag(), "v1.10.0")

    def test_calculates_each_semantic_bump(self) -> None:
        """Reset lower components according to semantic-version bump rules."""
        current = MODULE.Version(1, 2, 3)
        self.assertEqual(MODULE.next_version(current, "major").tag(), "v2.0.0")
        self.assertEqual(MODULE.next_version(current, "minor").tag(), "v1.3.0")
        self.assertEqual(MODULE.next_version(current, "patch").tag(), "v1.2.4")

    def test_rejects_an_invalid_bump(self) -> None:
        """Reject release levels outside the supported user activation syntax."""
        with self.assertRaises(MODULE.PublicationError):
            MODULE.next_version(MODULE.Version(1, 0, 0), "preview")

    def test_builds_safe_release_commands(self) -> None:
        """Keep tag and GitHub release operations as separated argument lists."""
        commands = MODULE.publication_commands(Path("/project"), "v1.2.3", "acme/project")
        self.assertEqual(commands[0], ["git", "tag", "-a", "v1.2.3", "-m", "Release v1.2.3"])
        self.assertIn("--verify-tag", commands[2])
        self.assertIn("--generate-notes", commands[2])
        self.assertNotIn("shell", " ".join(commands[2]).lower())


if __name__ == "__main__":
    unittest.main()
