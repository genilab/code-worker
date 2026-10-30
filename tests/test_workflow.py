from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from subprocess import run

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from codeworker.workflow import (  # noqa: E402
    WorkflowError,
    define_module,
    define_requirement,
    initialize_project,
    maintain_documentation,
    record_development,
    review_release,
    show_info,
    verify_module,
)


class WorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.workspace = tempfile.TemporaryDirectory()
        self.project = Path(self.workspace.name) / "delivery-project"
        initialize_project(
            self.project,
            name="Delivery Project",
            release="0.1.0",
            roadmap="Next: reporting",
            visibility="private",
            artifact_policy="tracked",
        )

    def tearDown(self) -> None:
        self.workspace.cleanup()

    def test_initialization_creates_required_baseline(self) -> None:
        for relative in ("src", "tests", "skills", "assets/images", "assets/reports", "assets/docs/project/project_manifest.json"):
            self.assertTrue((self.project / relative).exists(), relative)
        self.assertEqual(
            [],
            initialize_project(
                self.project,
                name="Delivery Project",
                release="0.1.0",
                roadmap="Next: reporting",
                visibility="private",
                artifact_policy="tracked",
            ),
        )

    def test_full_lifecycle_records_actual_test_result(self) -> None:
        define_module(self.project, name="Catalog", goal="Expose product catalog")
        define_requirement(
            self.project,
            module_name="Catalog",
            requirement_id="CAT-1",
            description="The catalog returns a product list.",
            acceptance="A caller receives one or more product records.",
        )
        (self.project / "src/catalog.py").write_text("PRODUCTS = ['widget']\n", encoding="utf-8")
        (self.project / "tests/test_catalog.py").write_text("assert True\n", encoding="utf-8")
        record_development(self.project, module_name="Catalog", implementation=["src/catalog.py"], tests=["tests/test_catalog.py"])
        verification = verify_module(self.project, module_name="Catalog", check=[sys.executable, "-c", "print('ok')"])
        self.assertEqual("PASSED", verification["status"])
        self.assertTrue((self.project / "assets/docs/qa/catalog.md").is_file())
        self.assertEqual("PASSED", maintain_documentation(self.project)["status"])
        self.assertEqual("READY_FOR_HUMAN_APPROVAL", review_release(self.project, release="0.1.0")["status"])
        self.assertEqual("APPROVED", review_release(self.project, release="0.1.0", human_approved=True)["status"])

    def test_development_requires_requirements_and_evidence(self) -> None:
        define_module(self.project, name="Catalog", goal="Expose product catalog")
        with self.assertRaises(WorkflowError):
            record_development(self.project, module_name="Catalog", implementation=["src/missing.py"], tests=["tests/missing.py"])

    def test_verification_preserves_failure(self) -> None:
        define_module(self.project, name="Catalog", goal="Expose product catalog")
        define_requirement(self.project, module_name="Catalog", requirement_id="CAT-1", description="Catalog responds.", acceptance="Response exists.")
        (self.project / "src/catalog.py").write_text("pass\n", encoding="utf-8")
        (self.project / "tests/test_catalog.py").write_text("pass\n", encoding="utf-8")
        record_development(self.project, module_name="Catalog", implementation=["src/catalog.py"], tests=["tests/test_catalog.py"])
        result = verify_module(self.project, module_name="Catalog", check=[sys.executable, "-c", "raise SystemExit(4)"])
        self.assertEqual("FAILED", result["status"])
        self.assertIn("Overall status: FAILED", (self.project / "assets/docs/qa/catalog.md").read_text(encoding="utf-8"))

    def test_info_display_and_link_audit(self) -> None:
        path, content = show_info(self.project, topic="ALL")
        self.assertEqual((self.project / "INFO.md").resolve(), path)
        self.assertIn("Project Info", content)
        (self.project / "assets/docs/broken.md").write_text("[missing](nope.md)\n", encoding="utf-8")
        report = maintain_documentation(self.project)
        self.assertEqual("FAILED", report["status"])
        self.assertEqual(["assets/docs/broken.md -> nope.md"], report["markdown_link_issues"])

    def test_cli_dispatches_project_init(self) -> None:
        project = Path(self.workspace.name) / "cli-project"
        command = [
            sys.executable,
            str(Path(__file__).resolve().parents[1] / "src/code_worker.py"),
            "project-init",
            "--project",
            str(project),
            "--name",
            "CLI Project",
            "--release",
            "0.1.0",
            "--roadmap",
            "Next: reporting",
            "--visibility",
            "private",
            "--artifact-policy",
            "tracked",
        ]
        result = run(command, text=True, capture_output=True, check=False)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue((project / "assets/docs/project/project_manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()
