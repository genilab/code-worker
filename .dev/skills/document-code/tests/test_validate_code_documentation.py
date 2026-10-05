#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/document-code/tests/test_validate_code_documentation.py - Tests source code documentation validation with positive and negative fixtures.
##

"""
AI instruction:
- Exercises valid and invalid Code documentation fixtures.
- Confirms that the documentation validator checks both header and overview.
- Keeps test evidence independent of a managed project checkout.
"""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


CODE_FILE = Path(__file__).resolve().parents[1] / "code" / "validate_code_documentation.py"
SPEC = importlib.util.spec_from_file_location("validate_code_documentation", CODE_FILE)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class PythonDocumentationTest(unittest.TestCase):
    """Verify the Code-worker adaptation of the GraphK documentation pattern."""

    def test_accepts_a_standard_header_and_bullet_overview(self) -> None:
        """Accept a syntactically valid source module with the required documentation."""
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "example.py"
            source.write_text(
                "##\n## Example - Example project\n## example.py - Example module\n##\n"
                "\"\"\"\nAI instruction:\n- Provides an example.\n- Keeps its behavior bounded.\n\"\"\"\n\n"
                "def run(value: str) -> str:\n    return value\n",
                encoding="utf-8",
            )
            self.assertEqual(MODULE.source_issues(source), [])

    def test_reports_missing_header_and_overview(self) -> None:
        """Expose a source file that has no Code-worker documentation."""
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "example.py"
            source.write_text("import pathlib\n", encoding="utf-8")
            issues = MODULE.source_issues(source)
            self.assertTrue(any("header" in issue for issue in issues))
            self.assertTrue(any("Module Overview" in issue for issue in issues))

    def test_reports_a_missing_ai_instruction(self) -> None:
        """Require factual AI-maintenance context within the module overview."""
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "example.py"
            source.write_text(
                "##\n## Example - Example project\n## example.py - Example module\n##\n"
                "\"\"\"\n- Provides an example.\n- Keeps its behavior bounded.\n\"\"\"\n\n"
                "def run(value: str) -> str:\n    return value\n",
                encoding="utf-8",
            )
            self.assertTrue(any("AI instruction" in issue for issue in MODULE.source_issues(source)))


if __name__ == "__main__":
    unittest.main()
