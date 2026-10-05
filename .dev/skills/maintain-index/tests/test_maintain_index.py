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
            self.assertIn("## Internal Skills", skills_index)
            self.assertIn("## External Skills", skills_index)
            self.assertIn("| **Skill** | **Action** | **Definition** | **Class** | **Plan** | **QA** | **Status** |", skills_index)
            self.assertIn("| [`example`](example/SKILL.md) | Run example. | Example. | prompt + code | [plan](example/docs/plan.md) | missing | PENDING |", skills_index)
            (skill / "docs/qa.md").write_text("| Validation | Status | Actual result |\n| --- | --- | --- |\n| Overall status | PASSED | Done |\n")
            self.assertIn("| [qa](example/docs/qa.md) | PASSED |", MODULE.render_skills(root))


if __name__ == "__main__":
    unittest.main()
