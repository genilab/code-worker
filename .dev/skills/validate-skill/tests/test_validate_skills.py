#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/validate-skill/tests/test_validate_skills.py - Executable test unit for the validate-skill skill.
##

"""
AI instruction:
- Verifies deterministic behavior for the validate-skill skill.
- Uses isolated fixtures where controlled project state is needed.
- Produces executable evidence for Code validation.
"""

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


CODE_FILE = Path(__file__).resolve().parents[1] / "code" / "validate_skills.py"
SPEC = importlib.util.spec_from_file_location("validate_skills", CODE_FILE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidateSkillsTest(unittest.TestCase):
    def make_project(self, root: Path) -> Path:
        (root / ".dev/skills").mkdir(parents=True)
        source_core = CODE_FILE.parents[2]
        shutil.copytree(source_core / "create-skill", root / ".dev/skills/create-skill")
        shutil.copytree(source_core / "maintain-index", root / ".dev/skills/maintain-index")
        skill = root / ".dev/skills/sample"
        (skill / "docs").mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            "---\nname: sample\ndescription: Handle a bounded sample request when the sample command is invoked.\nsource: project\naction: Handle a bounded sample request.\n---\n\n# Sample\n\n"
            "## Scope\n\nThis is an external skill. Use it when the sample command is invoked. It is responsible only for handling the sample action. It receives a sample input and produces a sample output. User activation command: `$sample`.\n\n"
            "## Workflow\n\n1. Confirm the sample input is complete; ask for clarification when it is missing.\n2. Handle the sample action and produce the sample output.\n\n"
            "## Constraints\n\n- Do not perform work outside the sample action.\n"
        )
        (skill / "docs/plan.md").write_text(
            "# Skill Plan — sample\n\n## Summary\n\nHandle a bounded sample request.\n\n## Description\n\nSample operation.\n\n## Script Requirements\n\n- It must handle a bounded sample request.\n\n"
            "## Delegation to Code\n\n- No code is delegated.\n\n## Code Requirements\n\nN/A\n"
        )
        return skill

    def test_validates_one_skill_and_refreshes_the_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_project(root)
            results = MODULE.validate(root, "sample")
            self.assertEqual(results, {"sample": []})
            self.assertIn("sample", (root / ".dev/skills/INDEX.md").read_text())

    def test_rejects_a_legacy_qualified_or_missing_selector(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_project(root)
            with self.assertRaises(ValueError):
                MODULE.selected_skills(root, "core/sample")


if __name__ == "__main__":
    unittest.main()
