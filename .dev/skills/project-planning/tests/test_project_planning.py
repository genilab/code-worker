#!/usr/bin/env python3
##
## CodeWorker - Evidence-driven development control for AI-assisted codebases.
## .dev/skills/project-planning/tests/test_project_planning.py - Test units for local outcome-first project planning.
##

"""
AI instruction:
- Verifies planning input validation and generated record content in isolated temporary directories.
- Does not modify a real project, Git configuration, or GitHub repository.
"""

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parents[1] / "code" / "project_planning.py"
SPEC = importlib.util.spec_from_file_location("project_planning", CODE)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ProjectPlanningTest(unittest.TestCase):
    """Validate deterministic project-control scaffolding without external side effects."""

    def test_rejects_missing_modules(self) -> None:
        """Require at least one independently owned module before initialization."""
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            with self.assertRaises(MODULE.InitializationError):
                MODULE.validate(MODULE.ProjectInput("demo", "Demo", "Build a demo", "external", "application", "private", (), "A demo", "A verified demo.", ("Keep work visible.",)), target, Path("/source"))

    def test_rejects_an_unrelated_control_directory(self) -> None:
        """Protect a target's existing non-CodeWorker control records from replacement."""
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            (target / ".dev").mkdir()
            project = MODULE.ProjectInput("demo", "Demo", "Build a demo", "external", "application", "private", ("core",), "A demo", "A verified demo.", ("Keep work visible.",))
            with self.assertRaises(MODULE.InitializationError):
                MODULE.validate(project, target, Path("/source"))

    def test_renders_question_backed_module_record(self) -> None:
        """Keep unknown module behavior explicit instead of fabricating requirements."""
        record = MODULE.requirements("runtime-core")
        self.assertIn("{{QUESTION: What independently testable behavior", record)
        self.assertIn("RUNTIME_CORE", record)
        self.assertIn("| Req_id | Description | Verification | Test Unit | Status |", record)

    def test_renders_project_identity_and_plan(self) -> None:
        """Use confirmed project inputs in the initial control records."""
        project = MODULE.ProjectInput(
            "Demo",
            "Demo application",
            "Build a demo",
            "external",
            "application",
            "private",
            ("core",),
            "A demo",
            "A controlled way to build a demo.",
            ("Keep work visible.",),
        )
        records = MODULE.project_records(project)
        self.assertIn("| Name | Demo |", records["project_identity.md"])
        self.assertIn("| Title | Demo application |", records["project_identity.md"])
        self.assertIn("| Project type | application |", records["project_identity.md"])
        self.assertIn("publication_policy: private", records["plan.md"])
        self.assertIn("## Title\n\nDemo application", records["plan.md"])
        self.assertIn("## Tagline\n\nA demo", records["plan.md"])
        self.assertIn("## Core Proposition\n\nA controlled way to build a demo.", records["plan.md"])
        self.assertIn("## Key Ideas\n\n- Keep work visible.", records["plan.md"])
        self.assertIn("Build a demo", records["plan.md"])
        self.assertIn("core", records["architecture.md"])

    def test_initializes_a_new_target_control_directory(self) -> None:
        """Copy a declared control source and render target records without source changes."""
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "source"
            target = workspace / "target"
            target.mkdir()
            maintainer = source / ".dev/skills/maintain-index/code"
            maintainer.mkdir(parents=True)
            (maintainer / "maintain_index.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
            project = MODULE.ProjectInput("demo", "Demo", "Build a demo", "external", "application", "private", ("core",), "A demo", "A verified demo.", ("Keep work visible.",))
            index = MODULE.initialize(project, target, source)
            self.assertEqual(index, target / ".dev/INDEX.md")
            self.assertIn(".dev/", (target / ".gitignore").read_text(encoding="utf-8"))
            self.assertIn("Build a demo", (target / ".dev/docs/project/plan.md").read_text(encoding="utf-8"))
            self.assertIn("CORE-1", (target / ".dev/requirements/core_reqs.md").read_text(encoding="utf-8"))

    def test_rejects_missing_project_identity_content(self) -> None:
        """Require public documentation identity before initialization can proceed."""
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "source"
            target = workspace / "target"
            target.mkdir()
            maintainer = source / ".dev/skills/maintain-index/code"
            maintainer.mkdir(parents=True)
            (maintainer / "maintain_index.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
            project = MODULE.ProjectInput("demo", "", "Build a demo", "external", "application", "private", ("core",), "A demo", "A verified demo.", ("Keep work visible.",))
            with self.assertRaisesRegex(MODULE.InitializationError, "title, tagline, and core proposition"):
                MODULE.validate(project, target, source)

    def test_rejects_missing_key_ideas(self) -> None:
        """Require at least one memorable project idea before initialization."""
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "source"
            target = workspace / "target"
            target.mkdir()
            maintainer = source / ".dev/skills/maintain-index/code"
            maintainer.mkdir(parents=True)
            (maintainer / "maintain_index.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
            project = MODULE.ProjectInput("demo", "Demo", "Build a demo", "external", "application", "private", ("core",), "A demo", "A verified demo.", ())
            with self.assertRaisesRegex(MODULE.InitializationError, "key idea"):
                MODULE.validate(project, target, source)

    def test_rejects_a_development_project(self) -> None:
        """Keep reusable development masters out of the application bootstrap path."""
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            project = MODULE.ProjectInput("master", "Master", "Build targets", "external", "development", "full", ("core",), "A master", "A reusable master.", ("Create applications.",))
            with self.assertRaisesRegex(MODULE.InitializationError, "application projects only"):
                MODULE.validate(project, target, Path("/source"))


if __name__ == "__main__":
    unittest.main()
