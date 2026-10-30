import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE = Path(__file__).parents[1] / "code/render_skills_info.py"
SPEC = importlib.util.spec_from_file_location("renderer", MODULE)
RENDERER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RENDERER)


class RenderSkillsInfoTest(unittest.TestCase):
    def test_renders_metadata_action_and_pending_status(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / "skills/alpha-check"
            (skill / "docs").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: alpha-check\ndescription: Check alpha.\nmetadata:\n  source: core\n  action: Check alpha.\n---\n\n# Alpha\n")
            (skill / "docs/plan.md").write_text("# Plan\n")
            (skill / "docs/qa.md").write_text("Status: PENDING\n")
            rendered = RENDERER.render(root)
            self.assertIn("| [alpha-check](alpha-check/SKILL.md) | Check alpha. | PENDING |", rendered)
            self.assertNotIn("## ", rendered)
