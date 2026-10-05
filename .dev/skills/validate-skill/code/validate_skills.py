#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/validate-skill/code/validate_skills.py - Validation code for the validate-skill skill.
##

"""
AI instruction:
- Implements deterministic behavior for the validate-skill skill.
- Exposes its command-line or reusable workflow interface.
- Keeps status and evidence dependent on actual executed checks.
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def discovered_skills(root: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    folder = root / ".dev" / "skills"
    if not folder.is_dir():
        return result
    for skill in sorted(path for path in folder.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()):
        result[skill.name] = skill
    return result


def selected_skills(root: Path, selector: str) -> dict[str, Path]:
    skills = discovered_skills(root)
    if selector == "all":
        return skills
    if selector not in skills:
        raise ValueError("selector must be `all` or a managed flat skill name such as `create-skill`")
    return {selector: skills[selector]}


def refresh_index(root: Path) -> None:
    maintainer = root / ".dev" / "skills" / "maintain-index" / "code" / "maintain_index.py"
    completed = subprocess.run([sys.executable, str(maintainer), "--project", str(root)], check=False)
    if completed.returncode:
        raise RuntimeError("could not refresh the skills index")


def validate(root: Path, selector: str) -> dict[str, list[str]]:
    validator_path = root / ".dev" / "skills" / "create-skill" / "code" / "validate_skill.py"
    if not validator_path.is_file():
        raise ValueError("create-skill shared validator is missing")
    validator = load_module(validator_path, "code_worker_shared_skill_validator")
    results = {}
    for name, skill in selected_skills(root, selector).items():
        outcome = validator.validation_results(skill, run_code_tests=True)
        validator.write_qa(skill, outcome)
        results[name] = [issue for issues in outcome.values() for issue in issues]
    refresh_index(root)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate one managed skill or all skills and refresh the catalog.")
    parser.add_argument("selector", help="`all` or a managed flat skill name such as `create-skill`")
    parser.add_argument("--project", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        results = validate(args.project.resolve(), args.selector)
    except (ValueError, RuntimeError) as error:
        parser.error(str(error))
    failed = False
    for name, issues in results.items():
        if issues:
            failed = True
            print(f"FAILED {name}")
            print("\n".join(f"- {issue}" for issue in issues))
        else:
            print(f"PASSED {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
