#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/create-skill/tests/test_validate_skill.py - Executable test unit for the create-skill skill.
##

"""
AI instruction:
- Verifies deterministic behavior for the create-skill skill.
- Uses isolated fixtures where controlled project state is needed.
- Produces executable evidence for Code validation.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path


CODE_FILE = Path(__file__).resolve().parents[1] / "code" / "validate_skill.py"
SPEC = importlib.util.spec_from_file_location("validate_skill", CODE_FILE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidateSkillTest(unittest.TestCase):
    def test_ignores_h1_examples_inside_fenced_code(self) -> None:
        text = "# Sample\n\n```text\n# Example heading\n```\n"
        self.assertEqual(MODULE.h1_titles(text), ["# Sample"])

    def test_checks_prompt_alignment_and_code_test_cases(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp) / "sample"
            (skill / "code").mkdir(parents=True)
            (skill / "tests").mkdir()
            (skill / "docs").mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: sample\ndescription: Sample.\nsource: project\naction: Perform the sample action.\n---\n\n# Sample\n\n"
                "**Skill type:** hybrid\n\n**Skill role:** external\n\n## Short Description\n\nSample behavior.\n\n"
                "## Action\n\nPerform the sample action.\n\n## Workflow\n\nReceive input and report output.\n\n"
                "## Activation\n\nUser activation command: `$sample`.\n\n## Workflow Skills\n\n- None.\n\n"
                "## Requirements Alignment\n\n- `SR-SAMPLE-001`: Covered.\n"
                "\n## Skill Maintenance\n\nKeep the local records aligned.\n"
            )
            (skill / "docs/plan.md").write_text(
                "## Overall Requirements\n\n- Role: external\n- Activation: User activation command: `$sample`.\n- Workflow skills: None.\n\n## Delegation to Code\n\ntext\n\n"
                "## Requirements\n\n### Script Requirements\n\n- **SR-SAMPLE-001**\n  - Requirement: Covered\n\n"
                "### Code Requirements\n\n- **CD-SAMPLE-001**\n  - Deterministic behavior: Tested\n\n## Completion Conditions\n\ntext\n"
            )
            (skill / "code/run.py").write_text("pass\n")
            (skill / "tests/test_sample.py").write_text("print('ok')\n")
            self.assertEqual(MODULE.validate_skill(skill), [])
            (skill / "SKILL.md").write_text((skill / "SKILL.md").read_text().replace("SR-SAMPLE-001", "SR-OTHER-001"))
            self.assertTrue(any("SR-SAMPLE-001" in issue for issue in MODULE.validate_skill(skill)))
            (skill / "SKILL.md").write_text((skill / "SKILL.md").read_text().replace("## Action", "## Missing Action"))
            self.assertTrue(any("Action section" in issue for issue in MODULE.validate_skill(skill)))
            (skill / "SKILL.md").write_text((skill / "SKILL.md").read_text().replace("action: Perform the sample action.\n", ""))
            self.assertTrue(any("external action metadata" in issue for issue in MODULE.validate_skill(skill)))

    def test_rejects_a_tabular_code_delegation_section(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp) / "sample"
            (skill / "docs").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: sample\ndescription: Sample.\nsource: core\n---\n\n# Sample\n\n"
                "**Skill type:** instruction\n\n**Skill role:** internal\n\n## Short Description\n\nSample behavior.\n\n"
                "## Action\n\nPerform the sample action.\n\n## Workflow\n\nReceive input and report output.\n\n"
                "## Activation\n\nInternal workflow only; no user activation command.\n\n## Workflow Skills\n\n- None.\n\n"
                "## Requirements Alignment\n\n- `SR-SAMPLE-001`: Covered.\n\n## Skill Maintenance\n\nKeep records aligned.\n"
            )
            (skill / "docs/plan.md").write_text(
                "## Overall Requirements\n\n- Role: internal\n- Activation: Internal workflow only; no user activation command.\n- Workflow skills: None.\n\n## Delegation to Code\n\n"
                "| Work | Owner |\n| --- | --- |\n| Task | Code |\n\n"
                "## Requirements\n\n### Script Requirements\n\n| ID | Requirement |\n| --- | --- |\n"
                "| SR-SAMPLE-001 | Covered |\n\n### Code Requirements\n\nNo code portion is currently required.\n\n"
                "## Completion Conditions\n\ntext\n"
            )
            issues = MODULE.validate_skill(skill)
            self.assertTrue(any("Delegation to Code" in issue for issue in issues))
            self.assertTrue(any("Script Requirements must use structured bullets" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
