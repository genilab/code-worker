#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/document-code/code/validate_code_documentation.py - Validates the required source-code header and module overview.
##

"""
AI instruction:
- Validates documentation shape without changing source behavior.
- Checks named code files or every managed code file in a Code-worker project.
- Requires a factual AI-instruction, bullet-based module overview before imports.
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path


def managed_files(root: Path) -> list[Path]:
    """Return source code owned by skills or the target codebase."""
    files: list[Path] = []
    for relative in (Path(".dev/skills"), Path("src"), Path("tests")):
        folder = root / relative
        if folder.is_dir():
            files.extend(path for path in folder.rglob("*.py") if "__pycache__" not in path.parts)
    return sorted(files)


def source_issues(path: Path) -> list[str]:
    """Return documentation-format gaps for one source-code file."""
    try:
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text, filename=str(path))
    except (OSError, SyntaxError) as error:
        return [f"cannot parse source code: {error}"]
    lines = text.splitlines()
    offset = 1 if lines and lines[0].startswith("#!") else 0
    required = ("##", "## ", "## ", "##")
    issues: list[str] = []
    if len(lines) < offset + len(required):
        issues.append("missing standard source header")
    else:
        header = lines[offset : offset + len(required)]
        if header[0] != "##" or header[3] != "##":
            issues.append("missing standard source header boundaries")
        if not header[1].startswith("## ") or " - " not in header[1]:
            issues.append("missing project identity header line")
        if not header[2].startswith("## ") or " - " not in header[2]:
            issues.append("missing module identity header line")
    if not tree.body or not isinstance(tree.body[0], ast.Expr) or not isinstance(tree.body[0].value, ast.Constant) or not isinstance(tree.body[0].value.value, str):
        issues.append("missing Module Overview immediately before imports")
        return issues
    overview = ast.get_docstring(tree, clean=False) or ""
    if not overview.lstrip().startswith("AI instruction:"):
        issues.append("Module Overview must begin with an AI instruction")
    bullets = [line for line in overview.splitlines() if line.strip().startswith("- ")]
    if len(bullets) < 2:
        issues.append("Module Overview needs at least two factual bullet items")
    return issues


def validate(root: Path, selected: list[Path]) -> dict[Path, list[str]]:
    """Validate selected files, or discover every managed code file."""
    files = [path.resolve() for path in selected] if selected else managed_files(root)
    return {path: source_issues(path) for path in files}


def main() -> int:
    """Run the source-documentation validator and print any gaps."""
    parser = argparse.ArgumentParser(description="Validate Code-worker source-code documentation.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--project", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.project.resolve()
    results = validate(root, args.files)
    failed = False
    for path, issues in results.items():
        if issues:
            failed = True
            print(f"FAILED {path}")
            print("\n".join(f"- {issue}" for issue in issues))
    if failed:
        return 1
    print(f"CODE DOCUMENTATION PASSED ({len(results)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
