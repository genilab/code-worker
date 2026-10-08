#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/maintain-index/tests/test_maintain_index.py - Executable test unit for the maintain-index skill.
##

"""
AI instruction:
- Verifies deterministic behavior for the maintain-index skill.
- Uses isolated fixtures where controlled project state is needed.
- Produces executable evidence for Code validation.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path


CODE_FILE = Path(__file__).resolve().parents[1] / "code" / "maintain_index.py"
SPEC = importlib.util.spec_from_file_location("maintain_index", CODE_FILE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MaintainIndexTest(unittest.TestCase):
    def test_registry_uses_evidence_or_pending(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / ".dev/skills/example"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: example\ndescription: Example.\nsource: project\naction: Run example.\n---\n\n# Example\n\n## Scope\n\nThis is an external skill. User activation command: `$example`.\n\n## Workflow\n\n1. Handle the example.\n\n## Constraints\n\n- Keep the example bounded.\n")
            (skill / "code").mkdir()
            (skill / "code/run.py").write_text("")
            (skill / "tests").mkdir()
            (skill / "tests/test_example.py").write_text("")
            (skill / "docs").mkdir()
            (skill / "docs/plan.md").write_text("# Requirements\n")
            project_index = MODULE.render(root)
            skills_index = MODULE.render_skills(root)
            self.assertIn("[Skills index](skills/INDEX.md)", project_index)
            self.assertIn("[QA](qa/project/README.md)", project_index)
            self.assertIn("| Project use | PENDING |", project_index)
            self.assertIn("| Project type | PENDING |", project_index)
            self.assertIn("| Publication policy | PENDING |", project_index)
            self.assertIn("| Tagline | PENDING |", project_index)
            self.assertIn("## Key ideas\n\n- PENDING", project_index)
            self.assertIn("## Internal Skills", skills_index)
            self.assertIn("## External Skills", skills_index)
            self.assertIn("| **Skill** | **Action** | **Definition** | **Class** | **Plan** | **QA** | **Status** |", skills_index)
            self.assertIn("| [`example`](example/SKILL.md) | Run example. | Example. | prompt + code | [plan](example/docs/plan.md) | missing | PENDING |", skills_index)
            (skill / "docs/qa.md").write_text("| Validation | Status | Actual result |\n| --- | --- | --- |\n| Overall status | PASSED | Done |\n")
            self.assertIn("| [qa](example/docs/qa.md) | PASSED |", MODULE.render_skills(root))

    def test_project_index_uses_canonical_plan_identity(self) -> None:
        """Render public project identity from Title, Tagline, and Core Proposition."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = root / ".dev/docs/project/plan.md"
            plan.parent.mkdir(parents=True)
            plan.write_text(
                "---\nproject_name: demo\nproject_use: external\nproject_type: application\npublication_policy: private\n---\n\n# Project Plan\n\n## Title\n\nDemo\n\n## Tagline\n\nBuild with confidence.\n\n## Core Proposition\n\nA traceable development workflow.\n\n## Key Ideas\n\n- Keep project evidence visible.\n",
                encoding="utf-8",
            )
            project_index = MODULE.render(root)
            self.assertIn("| Project | Demo |", project_index)
            self.assertIn("| Tagline | Build with confidence. |", project_index)
            self.assertIn("| Core proposition | A traceable development workflow. |", project_index)
            self.assertIn("| Project type | application |", project_index)
            self.assertIn("| Publication policy | private |", project_index)
            self.assertIn("- Keep project evidence visible.", project_index)


if __name__ == "__main__":
    unittest.main()
