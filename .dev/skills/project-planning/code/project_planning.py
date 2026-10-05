#!/usr/bin/env python3
##
## CodeWorker - Evidence-driven development control for AI-assisted codebases.
## .dev/skills/project-planning/code/project_planning.py - Bootstraps a planned target project's local CodeWorker control records.
##

"""
AI instruction:
- Creates a local .dev control package from a declared CodeWorker source and confirmed outcome-first project inputs.
- Preserves target source and Git state, refusing existing control directories or incomplete initialization data.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


class InitializationError(RuntimeError):
    """Raised when a target cannot safely receive the local control package."""


@dataclass(frozen=True)
class ProjectInput:
    """Describe the minimum confirmed facts required for project initialization."""

    name: str
    objective: str
    project_use: str
    modules: tuple[str, ...]
    tagline: str


def default_source() -> Path:
    """Return the CodeWorker project root that owns this skill implementation."""
    return Path(__file__).resolve().parents[4]


def validate(project: ProjectInput, target: Path, source: Path) -> None:
    """Reject unsafe targets and incomplete project facts before creating files."""
    if not project.name.strip() or not project.objective.strip():
        raise InitializationError("project name and objective are required")
    if project.project_use not in {"internal", "external"}:
        raise InitializationError("project use must be internal or external")
    if not project.modules or any(not module.strip() for module in project.modules):
        raise InitializationError("at least one non-empty module is required")
    if not target.is_dir():
        raise InitializationError(f"target directory does not exist: {target}")
    if target.resolve() == source.resolve():
        raise InitializationError("the CodeWorker source cannot initialize itself")
    existing = target / ".dev"
    if existing.exists() and not (existing / "skills" / "maintain-index" / "code" / "maintain_index.py").is_file():
        raise InitializationError(f"target has an unrelated control directory: {existing}")
    if not (source / ".dev" / "skills" / "maintain-index" / "code" / "maintain_index.py").is_file():
        raise InitializationError(f"control source is incomplete: {source}")


def requirements(module: str) -> str:
    """Render one unresolved module record without inventing a requirement."""
    prefix = module.upper().replace("-", "_")
    return f"# Requirements — {module}\n\n{{{{QUESTION: What independently testable behavior must {module} provide? Use {prefix}-1 for the first confirmed row.}}}}\n\n| Req_id | Description | Verification | Test Unit | Status |\n| --- | --- | --- | --- | --- |\n"


def project_records(project: ProjectInput) -> dict[str, str]:
    """Render the initial project records from confirmed facts and visible questions."""
    modules = ", ".join(project.modules)
    return {
        "project_identity.md": f"# Project Identity\n\n| Field | Value |\n| --- | --- |\n| Name | {project.name} |\n| Purpose | {project.objective} |\n| Verification state | PENDING |\n",
        "plan.md": f"---\nproject_name: {project.name}\nproject_use: {project.project_use}\ntagline: \"{project.tagline}\"\n---\n\n# Project Plan\n\n## Overview\n\n{project.objective}\n\n## Overall Requirements\n\n- It must define and maintain explicit planning, architecture, release, roadmap, module requirements, QA, and indexes before implementation.\n- It must maintain independently owned modules: {modules}.\n- It must preserve unresolved product decisions as questions until confirmed.\n",
        "architecture.md": f"# Solution Architecture\n\n## Overview\n\n{{{{QUESTION: What components, boundaries, integrations, and data flows realize {project.objective}?}}}}\n\n## Initial Modules\n\n{modules}\n",
        "release.md": "# Next Release\n\n## Overview\n\n{{QUESTION: What smallest verified outcome belongs in the first release?}}\n\n## Overall Requirements\n\n- It must define evidence-backed scope before implementation.\n",
        "roadmap.md": "# Roadmap\n\n## Upcoming Versions\n\n{{QUESTION: What outcome belongs in each planned version after the initial release?}}\n",
        "qa.md": "# Project QA\n\n## Summary\n\n- Overall status: PENDING\n- Scope: Project initialization records only.\n- Outstanding gaps: Define module behavior, implementation, and executable evidence.\n",
    }


def ignore_target_control_directory(target: Path) -> None:
    """Ensure the target keeps its generated .dev control records out of Git."""
    ignore = target / ".gitignore"
    lines = ignore.read_text(encoding="utf-8").splitlines() if ignore.is_file() else []
    if ".dev/" not in lines:
        ignore.write_text("\n".join([*lines, ".dev/"]).lstrip("\n") + "\n", encoding="utf-8")


def untrack_target_control_directory(target: Path) -> None:
    """Remove a copied master .dev package from a target Git index without deleting its files."""
    repository = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=target, capture_output=True, text=True, check=False)
    if repository.returncode:
        return
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", ".dev"], cwd=target, capture_output=True, text=True, check=False)
    if not tracked.returncode:
        removed = subprocess.run(["git", "rm", "-r", "--cached", "--ignore-unmatch", ".dev"], cwd=target, capture_output=True, text=True, check=False)
        if removed.returncode:
            raise InitializationError(removed.stderr.strip() or "could not untrack target .dev")


def initialize(project: ProjectInput, target: Path, source: Path) -> Path:
    """Copy the local control package, render project records, and refresh navigation."""
    validate(project, target, source)
    ignore_target_control_directory(target)
    control = target / ".dev"
    if control.exists():
        untrack_target_control_directory(target)
    else:
        shutil.copytree(source / ".dev", control)
    records = project_records(project)
    project_docs = control / "docs" / "project"
    project_docs.mkdir(parents=True, exist_ok=True)
    (control / "qa" / "project").mkdir(parents=True, exist_ok=True)
    (control / "requirements").mkdir(parents=True, exist_ok=True)
    for name, content in records.items():
        destination = control / "qa" / "project" / "README.md" if name == "qa.md" else project_docs / name
        destination.write_text(content, encoding="utf-8")
    requirements_dir = control / "requirements"
    for module in project.modules:
        (requirements_dir / f"{module}_reqs.md").write_text(requirements(module), encoding="utf-8")
    maintainer = control / "skills" / "maintain-index" / "code" / "maintain_index.py"
    completed = subprocess.run(["python3", str(maintainer), "--project", str(target)], capture_output=True, text=True, check=False)
    if completed.returncode:
        raise InitializationError(completed.stderr.strip() or "could not generate target indexes")
    return control / "INDEX.md"


def main() -> int:
    """Create a local control baseline only when explicit apply is requested."""
    parser = argparse.ArgumentParser(description="Bootstrap a planned target with CodeWorker local development control.")
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--result", dest="objective", required=True, help="The observable completed project result.")
    parser.add_argument("--project-use", choices=("internal", "external"), required=True)
    parser.add_argument("--module", action="append", default=[])
    parser.add_argument("--tagline", default="")
    parser.add_argument("--control-source", type=Path, default=default_source())
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    project = ProjectInput(args.name, args.objective, args.project_use, tuple(args.module), args.tagline or args.objective)
    try:
        validate(project, args.target, args.control_source)
        if not args.apply:
            print(f"READY {args.target.resolve()} modules={','.join(project.modules)}")
            return 0
        print(f"INITIALIZED {initialize(project, args.target, args.control_source)}")
        return 0
    except InitializationError as error:
        print(f"REFUSED: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
