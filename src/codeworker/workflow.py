"""Safe, local implementations of the Code-worker public actions."""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


class WorkflowError(ValueError):
    """Raised when a lifecycle action cannot safely continue."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    if not slug:
        raise WorkflowError("A non-empty name is required.")
    return slug


def _read_json(path: Path, default: object) -> object:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise WorkflowError(f"Invalid JSON record: {path}") from error


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _require_initialized(project: Path) -> Path:
    manifest = project / "assets/docs/project/project_manifest.json"
    if not manifest.exists():
        raise WorkflowError("Project is not initialized. Run Project init first.")
    return manifest


def _project_root(path: Path | str) -> Path:
    return Path(path).expanduser().resolve()


def _origin_for(project: Path) -> str | None:
    if not (project / ".git").exists():
        return None
    result = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        cwd=project,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout.strip() or None


def _is_master_repository(project: Path) -> bool:
    master = Path(__file__).resolve().parents[2]
    if project == master:
        return True
    origin = _origin_for(project)
    return bool(origin and "genilab/code-worker" in origin.lower())


@dataclass
class Module:
    name: str
    goal: str
    dependencies: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    owner: str = "implementation-agent"
    requirements: list[dict[str, str]] = field(default_factory=list)
    implementation: list[str] = field(default_factory=list)
    tests: list[str] = field(default_factory=list)
    verification: dict[str, object] | None = None


def initialize_project(
    project_path: Path | str,
    *,
    name: str,
    release: str,
    roadmap: str,
    visibility: str,
    artifact_policy: str,
) -> list[str]:
    """Create missing project controls without overwriting an existing project."""
    project = _project_root(project_path)
    if visibility not in {"public", "private"}:
        raise WorkflowError("Visibility must be public or private.")
    if artifact_policy not in {"local", "tracked"}:
        raise WorkflowError("Artifact policy must be local or tracked.")
    if _is_master_repository(project):
        raise WorkflowError("Project init refuses the Code-worker master repository or its origin.")

    project.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    for relative in (
        "src",
        "tests",
        "skills",
        "assets/images",
        "assets/reports",
        "assets/docs/project",
        "assets/docs/plan",
        "assets/docs/requirements",
        "assets/docs/design/diagrams",
        "assets/docs/qa",
        "assets/docs/test",
        "assets/docs/release",
    ):
        directory = project / relative
        was_missing = not directory.exists()
        directory.mkdir(parents=True, exist_ok=True)
        if was_missing:
            created.append(relative + "/")

    manifest = {
        "artifact_policy": artifact_policy,
        "initialized_at": _utc_now(),
        "name": name,
        "release": release,
        "roadmap": roadmap,
        "visibility": visibility,
    }
    manifest_path = project / "assets/docs/project/project_manifest.json"
    if manifest_path.exists():
        existing = _read_json(manifest_path, {})
        comparable_existing = {key: value for key, value in existing.items() if key != "initialized_at"}
        comparable_manifest = {key: value for key, value in manifest.items() if key != "initialized_at"}
        if comparable_existing != comparable_manifest:
            raise WorkflowError("Project is already initialized with different controls; review it manually.")
    else:
        _write_json(manifest_path, manifest)
        created.append("assets/docs/project/project_manifest.json")

    records = {
        "INFO.md": "# Project Info\n\nUse the records in this directory for project identity and lifecycle state.\n",
        "assets/docs/INFO.md": "# Documentation Info\n\nLifecycle records live beneath this directory.\n",
        "assets/docs/project/project_charter.md": (
            f"# Project Charter — {name}\n\n## Status\n\nDRAFT — requires human approval.\n"
        ),
        "assets/docs/plan/roadmap.md": (
            f"# Roadmap — {name}\n\n## Current release\n\n{release}\n\n## Future releases\n\n{roadmap}\n"
        ),
        "assets/docs/plan/delivery_plan.md": "# Delivery Plan\n\n| Module | Goal | Status |\n| --- | --- | --- |\n",
        "assets/docs/requirements/INFO.md": "# Requirements Info\n\nOne file per module holds testable requirements.\n",
        "assets/docs/qa/INFO.md": "# QA Info\n\nVerification reports contain actual check outcomes.\n",
        "assets/docs/release/INFO.md": "# Release Info\n\nRelease review never publishes a release.\n",
        "skills/INFO.md": "# Local Skills Info\n\nProject-local skills are documented here.\n",
    }
    for relative, content in records.items():
        if _write_if_missing(project / relative, content):
            created.append(relative)
    return created


def _modules_path(project: Path) -> Path:
    return project / "assets/docs/plan/modules.json"


def _load_modules(project: Path) -> list[Module]:
    values = _read_json(_modules_path(project), [])
    if not isinstance(values, list):
        raise WorkflowError("Module register must contain a list.")
    return [Module(**value) for value in values]


def _save_modules(project: Path, modules: Iterable[Module]) -> None:
    _write_json(_modules_path(project), [asdict(module) for module in modules])
    lines = ["# Delivery Plan", "", "| Module | Goal | Dependencies | Risks | Owner | Gate status |", "| --- | --- | --- | --- | --- | --- |"]
    for module in modules:
        status = "VERIFIED" if module.verification and module.verification.get("status") == "PASSED" else "PENDING"
        lines.append(
            f"| {module.name} | {module.goal} | {', '.join(module.dependencies) or 'None'} | "
            f"{', '.join(module.risks) or 'None'} | {module.owner} | {status} |"
        )
    (project / "assets/docs/plan/delivery_plan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def define_module(
    project_path: Path | str,
    *,
    name: str,
    goal: str,
    dependencies: Iterable[str] = (),
    risks: Iterable[str] = (),
    owner: str = "implementation-agent",
) -> Module:
    project = _project_root(project_path)
    _require_initialized(project)
    module_name = _slug(name)
    modules = _load_modules(project)
    if any(module.name == module_name for module in modules):
        raise WorkflowError(f"Module already exists: {module_name}")
    module = Module(module_name, goal.strip(), list(dependencies), list(risks), owner.strip())
    if not module.goal:
        raise WorkflowError("Module goal is required.")
    modules.append(module)
    _save_modules(project, modules)
    return module


def _selected_module(project: Path, name: str) -> tuple[list[Module], Module]:
    modules = _load_modules(project)
    module_name = _slug(name)
    for module in modules:
        if module.name == module_name:
            return modules, module
    raise WorkflowError(f"Unknown module: {module_name}. Run Define Modules first.")


def define_requirement(
    project_path: Path | str,
    *,
    module_name: str,
    requirement_id: str,
    description: str,
    acceptance: str,
) -> dict[str, str]:
    project = _project_root(project_path)
    _require_initialized(project)
    modules, module = _selected_module(project, module_name)
    requirement_id = requirement_id.strip()
    if not requirement_id or not description.strip() or not acceptance.strip():
        raise WorkflowError("Requirement id, description, and acceptance criteria are required.")
    if any(item["id"] == requirement_id for item in module.requirements):
        raise WorkflowError(f"Requirement already exists: {requirement_id}")
    requirement = {"id": requirement_id, "description": description.strip(), "acceptance": acceptance.strip()}
    module.requirements.append(requirement)
    _save_modules(project, modules)
    lines = [f"# Requirements — {module.name}", "", "| ID | Description | Acceptance criteria | Status |", "| --- | --- | --- | --- |"]
    lines.extend(f"| {item['id']} | {item['description']} | {item['acceptance']} | PENDING |" for item in module.requirements)
    (project / f"assets/docs/requirements/{module.name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return requirement


def _relative_project_file(project: Path, value: str, permitted_root: str) -> str:
    candidate = (project / value).resolve()
    root = (project / permitted_root).resolve()
    if not candidate.is_file() or root not in candidate.parents:
        raise WorkflowError(f"Evidence must be an existing file under {permitted_root}/: {value}")
    return str(candidate.relative_to(project))


def record_development(
    project_path: Path | str,
    *,
    module_name: str,
    implementation: Iterable[str],
    tests: Iterable[str],
) -> Module:
    project = _project_root(project_path)
    _require_initialized(project)
    modules, module = _selected_module(project, module_name)
    if not module.requirements:
        raise WorkflowError("Define requirements before recording development.")
    implementations = [_relative_project_file(project, value, "src") for value in implementation]
    test_files = [_relative_project_file(project, value, "tests") for value in tests]
    if not implementations or not test_files:
        raise WorkflowError("At least one source file and one test file are required.")
    module.implementation = implementations
    module.tests = test_files
    _save_modules(project, modules)
    return module


def verify_module(
    project_path: Path | str,
    *,
    module_name: str,
    check: list[str] | None = None,
) -> dict[str, object]:
    project = _project_root(project_path)
    _require_initialized(project)
    modules, module = _selected_module(project, module_name)
    if not module.requirements or not module.implementation or not module.tests:
        raise WorkflowError("Requirements, source evidence, and test evidence are required before verification.")
    if not check:
        raise WorkflowError("Verification requires an explicit test command after --check.")
    result = subprocess.run(check, cwd=project, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    outcome = {
        "checked_at": _utc_now(),
        "command": check,
        "exit_code": result.returncode,
        "output": result.stdout[-12000:],
        "status": "PASSED" if result.returncode == 0 else "FAILED",
    }
    module.verification = outcome
    _save_modules(project, modules)
    report = [f"# QA — {module.name}", "", "## Summary", "", f"- Overall status: {outcome['status']}", f"- Check: `{' '.join(check)}`", f"- Exit code: {result.returncode}", "", "## Output", "", "```text", result.stdout[-12000:].rstrip(), "```", "", "## Requirement traceability", ""]
    report.extend(f"- `{item['id']}`: {outcome['status']} — command outcome above." for item in module.requirements)
    (project / f"assets/docs/qa/{module.name}.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return outcome


def _markdown_link_issues(project: Path) -> list[str]:
    issues: list[str] = []
    pattern = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
    for path in project.rglob("*.md"):
        if ".git" in path.parts or "temp" in path.parts:
            continue
        for raw in pattern.findall(path.read_text(encoding="utf-8")):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "codex:")):
                continue
            destination = target.split("#", 1)[0]
            if destination and not (path.parent / destination).exists():
                issues.append(f"{path.relative_to(project)} -> {target}")
    return issues


def maintain_documentation(project_path: Path | str, *, scope: str = "ALL") -> dict[str, object]:
    project = _project_root(project_path)
    _require_initialized(project)
    scope = scope.strip() or "ALL"
    modules = _load_modules(project)
    if scope != "ALL" and not any(module.name == _slug(scope) for module in modules):
        raise WorkflowError(f"Unknown documentation scope: {scope}")
    issues = _markdown_link_issues(project)
    report = {
        "checked_at": _utc_now(),
        "scope": scope,
        "markdown_link_issues": issues,
        "status": "PASSED" if not issues else "FAILED",
    }
    _write_json(project / "assets/reports/documentation/documentation_audit.json", report)
    return report


def review_release(project_path: Path | str, *, release: str, human_approved: bool = False) -> dict[str, object]:
    project = _project_root(project_path)
    _require_initialized(project)
    modules = _load_modules(project)
    ready_modules = bool(modules) and all(
        module.requirements and module.implementation and module.tests and module.verification and module.verification.get("status") == "PASSED"
        for module in modules
    )
    docs = maintain_documentation(project)
    status = "READY_FOR_HUMAN_APPROVAL" if ready_modules and docs["status"] == "PASSED" and not human_approved else "APPROVED" if ready_modules and docs["status"] == "PASSED" else "BLOCKED"
    report = {
        "reviewed_at": _utc_now(),
        "release": release,
        "human_approved": human_approved,
        "modules_ready": ready_modules,
        "documentation_status": docs["status"],
        "status": status,
        "publication": "NOT PERFORMED",
    }
    _write_json(project / "assets/docs/release/release_review.json", report)
    return report


def show_info(project_path: Path | str, *, topic: str = "ALL") -> tuple[Path, str]:
    project = _project_root(project_path)
    targets = {
        "ALL": project / "INFO.md",
        "assets": project / "assets/INFO.md",
        "docs": project / "assets/docs/INFO.md",
        "skills": project / "skills/INFO.md",
        "project": project / "assets/docs/project/INFO.md",
        "plan": project / "assets/docs/plan/INFO.md",
        "requirements": project / "assets/docs/requirements/INFO.md",
        "qa": project / "assets/docs/qa/INFO.md",
        "release": project / "assets/docs/release/INFO.md",
    }
    target = targets.get(topic.strip().lower() if topic.strip().lower() != "all" else "ALL")
    if target is None or not target.is_file():
        raise WorkflowError(f"No confirmed INFO document for topic: {topic}")
    return target, target.read_text(encoding="utf-8")
