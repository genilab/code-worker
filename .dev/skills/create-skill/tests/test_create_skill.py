#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/create-skill/tests/test_create_skill.py - Executable test unit for the create-skill skill.
##

"""
AI instruction:
- Verifies deterministic behavior for the create-skill skill.
- Uses isolated fixtures where controlled project state is needed.
- Produces executable evidence for Code validation.
"""

import subprocess
import sys
import tempfile
import unittest
import shutil
from pathlib import Path


CODE_FILE = Path(__file__).resolve().parents[1] / "code" / "create_skill.py"


class CreateSkillTest(unittest.TestCase):
    def make_project(self, root: Path) -> None:
        (root / ".dev" / "skills").mkdir(parents=True)
        source_maintainer = CODE_FILE.parents[2] / "maintain-index"
        destination_maintainer = root / ".dev/skills/maintain-index"
        shutil.copytree(source_maintainer, destination_maintainer)

    def test_creates_a_linked_hybrid_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_project(root)
            result = subprocess.run(
                [sys.executable, str(CODE_FILE), "sample-skill", "--source", "core",
                 "--description", "Handle a bounded sample workflow.", "--type", "hybrid", "--role", "external",
                 "--action", "Handle a sample action.", "--workflow", "Receive input, perform the action, and report the result.",
                 "--project", str(root)], text=True, capture_output=True, check=False
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            skill = root / ".dev/skills/sample-skill"
            document = (skill / "SKILL.md").read_text()
            self.assertIn("name: sample-skill", document)
            self.assertIn("source: core", document)
            self.assertIn("## Scope", document)
            self.assertIn("This is an external skill.", document)
            self.assertIn("## Workflow", document)
            self.assertIn("Receive input, perform the action, and report the result.", document)
            self.assertIn("## Constraints", document)
            self.assertIn("User activation command: `$sample-skill`.", document)
            self.assertIn("## Summary", (skill / "docs/plan.md").read_text())
            self.assertIn("## Description", (skill / "docs/plan.md").read_text())
            self.assertIn("## Script Requirements", (skill / "docs/plan.md").read_text())
            self.assertIn("## Delegation to Code", (skill / "docs/plan.md").read_text())
            self.assertIn("## Code Requirements", (skill / "docs/plan.md").read_text())
            self.assertNotIn("## Completion Conditions", (skill / "docs/plan.md").read_text())
            self.assertIn("Complete this plan before authoring the final `SKILL.md`", (skill / "docs/plan.md").read_text())
            self.assertIn("- It must perform", (skill / "docs/plan.md").read_text())
            self.assertIn("- Delegate the repeated, deterministic parts", (skill / "docs/plan.md").read_text())
            self.assertNotIn("## Short Description", document)
            self.assertNotIn("## Artifact Boundary", document)
            self.assertNotIn("## Skill Maintenance", document)
            self.assertTrue((skill / "code").is_dir())
            self.assertTrue((skill / "tests").is_dir())
            self.assertTrue((skill / "docs/plan.md").is_file())
            self.assertFalse((skill / "docs/requirements.md").exists())
            self.assertIn("## Script Requirements", (skill / "docs/plan.md").read_text())
            self.assertNotIn("SR-SAMPLE-SKILL-001", (skill / "docs/plan.md").read_text())
            self.assertTrue((skill / "docs/qa.md").is_file())
            self.assertTrue((skill / "tests/test_sample_skill.py").is_file())
            self.assertIn("Cover every Script Requirement", (skill / "SKILL.md").read_text())
            self.assertIn("sample-skill", (root / ".dev/skills/INDEX.md").read_text())

    def test_rejects_invalid_name(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_project(root)
            result = subprocess.run(
                [sys.executable, str(CODE_FILE), "Bad_Name", "--source", "core",
                 "--description", "x", "--action", "x", "--workflow", "x", "--project", str(root)], text=True, capture_output=True
            )
            self.assertNotEqual(result.returncode, 0)

    def test_creates_an_external_skill_with_project_source(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_project(root)
            result = subprocess.run(
                [sys.executable, str(CODE_FILE), "sample-external", "--source", "project",
                 "--description", "Handle a bounded external workflow.", "--role", "external",
                 "--action", "Handle an external action.", "--workflow", "Receive input and report the result.",
                 "--project", str(root)], text=True, capture_output=True, check=False
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            skill = root / ".dev/skills/sample-external"
            self.assertTrue((skill / "SKILL.md").is_file())
            self.assertIn("source: project", (skill / "SKILL.md").read_text())
            self.assertFalse((skill / "code").exists())
            self.assertFalse((skill / "tests").exists())


if __name__ == "__main__":
    unittest.main()
