#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/maintain-index/code/maintain_index.py - Index-maintenance code for the maintain-index skill.
##

"""
AI instruction:
- Implements deterministic behavior for the maintain-index skill.
- Exposes its command-line or reusable workflow interface.
- Keeps status and evidence dependent on actual executed checks.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


TYPE = re.compile(r"^\*\*Skill type:\*\*\s*(instruction|code-backed|hybrid)\s*$", re.MULTILINE | re.IGNORECASE)
ROLE = re.compile(r"^\*\*Skill role:\*\*\s*(internal|external)\s*$", re.MULTILINE | re.IGNORECASE)
SOURCE = re.compile(r"^source:\s*(core|project)\s*$", re.MULTILINE | re.IGNORECASE)
ACTION = re.compile(r"^action:\s*(?P<value>.+)$", re.MULTILINE)
SCOPE = re.compile(r"^## Scope\s*$\n(?P<value>.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
SCOPE_ROLE = re.compile(r"\b(?:an?\s+)?(internal|external)\s+skill\b", re.IGNORECASE)
STATUS = re.compile(
    r"^(?:\|\s*Overall status\s*\|\s*([^|]+)\||-\s*Overall status:\s*([A-Z]+)\s*$)",
    re.MULTILINE | re.IGNORECASE,
)
SHORT_DESCRIPTION = re.compile(r"^## Short Description\s*$\n(?P<value>.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
DESCRIPTION = re.compile(r"^description:\s*(?P<value>.+)$", re.MULTILINE)
SUMMARY = re.compile(r"^## Summary\s*$\n(?P<value>.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
PROJECT_USE = re.compile(r"\A---\n.*?^project_use:\s*(internal|external)\s*$.*?\n---", re.MULTILINE | re.DOTALL | re.IGNORECASE)
PROJECT_TYPE = re.compile(r"\A---\n.*?^project_type:\s*(development|application)\s*$.*?\n---", re.MULTILINE | re.DOTALL | re.IGNORECASE)
PUBLICATION_POLICY = re.compile(r"\A---\n.*?^publication_policy:\s*(full|limited|private)\s*$.*?\n---", re.MULTILINE | re.DOTALL | re.IGNORECASE)
PROJECT_VERSION = re.compile(r'^version\s*=\s*["\'](?P<value>[^"\']+)["\']\s*$', re.MULTILINE)
PLAN_SECTION = re.compile(r"^## (?P<heading>Title|Tagline|Core Proposition|Key Ideas)\s*$\n(?P<value>.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)


def validation_status(path: Path) -> str:
    if not path.is_file():
        return "PENDING"
    match = STATUS.search(path.read_text(encoding="utf-8"))
    return (match.group(1) or match.group(2)).strip().upper() if match else "PENDING"


def relative(base: Path, path: Path) -> str:
    return os.path.relpath(path, base).replace(os.sep, "/")


def identity(root: Path) -> tuple[str, str, str, str]:
    """Return project identity from the canonical project-plan documentation."""
    record = root / ".dev/docs/project/project_identity.md"
    text = record.read_text(encoding="utf-8") if record.is_file() else ""
    values = {}
    for field, value in re.findall(r"^\|\s*(Name|Title|Tagline|Core Proposition|Purpose|Verification state)\s*\|\s*([^|]+)\|", text, re.MULTILINE):
        values[field] = value.strip()
    plan = root / ".dev/docs/project/plan.md"
    plan_values = {
        match.group("heading"): " ".join(match.group("value").split())
        for match in PLAN_SECTION.finditer(plan.read_text(encoding="utf-8"))
    } if plan.is_file() else {}
    name = plan_values.get("Title", values.get("Title", values.get("Name", "code-worker")))
    tagline = plan_values.get("Tagline", values.get("Tagline", "PENDING"))
    proposition = plan_values.get("Core Proposition", values.get("Core Proposition", values.get("Purpose", "PENDING")))
    state = values.get("Verification state", "PENDING")
    return (name, tagline, proposition, f"Initialized target — {state}")


def project_use(root: Path) -> str:
    """Return the project-use declaration from the project plan front matter."""
    plan = root / ".dev/docs/project/plan.md"
    if not plan.is_file():
        return "PENDING"
    declared = PROJECT_USE.search(plan.read_text(encoding="utf-8"))
    return declared.group(1).lower() if declared else "PENDING"


def project_configuration(root: Path) -> tuple[str, str]:
    """Return project type and publication policy from the canonical plan."""
    plan = root / ".dev/docs/project/plan.md"
    if not plan.is_file():
        return ("PENDING", "PENDING")
    content = plan.read_text(encoding="utf-8")
    project_type = PROJECT_TYPE.search(content)
    publication_policy = PUBLICATION_POLICY.search(content)
    return (
        project_type.group(1).lower() if project_type else "PENDING",
        publication_policy.group(1).lower() if publication_policy else "PENDING",
    )


def key_ideas(root: Path) -> list[str]:
    """Return the canonical plan's non-empty Key Ideas as concise bullet text."""
    plan = root / ".dev/docs/project/plan.md"
    if not plan.is_file():
        return []
    sections = {match.group("heading"): match.group("value") for match in PLAN_SECTION.finditer(plan.read_text(encoding="utf-8"))}
    return [line.removeprefix("- ").strip() for line in sections.get("Key Ideas", "").splitlines() if line.startswith("- ") and line[2:].strip()]


def project_version(root: Path) -> str:
    """Return declared package version when a project provides pyproject metadata."""
    metadata = root / "pyproject.toml"
    if not metadata.is_file():
        return "0.0.0-dev"
    declared = PROJECT_VERSION.search(metadata.read_text(encoding="utf-8"))
    return declared.group("value") if declared else "0.0.0-dev"


def next_work(root: Path) -> str:
    """Return the next-work guidance supported by the active planning records."""
    plan = root / ".dev/docs/project/plan.md"
    if plan.is_file() and "{{QUESTION:" in plan.read_text(encoding="utf-8"):
        return "Complete the marked questions in the project plan, solution architecture, next release plan, and roadmap."
    return "Use the active release plan to define, implement, validate, and record the next evidence-backed outcome."


def skill_type(skill: Path, text: str) -> str:
    """Return the catalog class from actual packaged code, with legacy fallback."""
    if (skill / "code").is_dir() and any((skill / "code").glob("*.py")):
        return "prompt + code"
    declared = TYPE.search(text)
    return {"instruction": "prompt", "code-backed": "code", "hybrid": "prompt + code"}.get(
        declared.group(1).lower() if declared else "instruction", "prompt"
    )


def skill_role(text: str) -> str:
    """Return a skill's declared routing role for the catalog."""
    scope = SCOPE.search(text)
    if scope:
        declared_scope = SCOPE_ROLE.search(scope.group("value"))
        if declared_scope:
            return declared_scope.group(1).lower()
    declared = ROLE.search(text)
    return declared.group(1).lower() if declared else "missing"


def skill_source(text: str) -> str:
    """Return the skill's declared template origin from discovery metadata."""
    declared = SOURCE.search(text)
    return declared.group(1).lower() if declared else "missing"


def skill_action(text: str, source: str) -> str:
    """Return an external skill's declared action, or a neutral core marker."""
    if source == "core":
        return "—"
    declared = ACTION.search(text)
    return declared.group("value").strip().strip('"') if declared else "missing"


def skill_definition(plan: Path, text: str) -> str:
    """Return the concise catalog definition from a plan Summary."""
    summary = SUMMARY.search(plan.read_text(encoding="utf-8")) if plan.is_file() else None
    if summary:
        return " ".join(summary.group("value").split())
    description = SHORT_DESCRIPTION.search(text) or DESCRIPTION.search(text)
    return " ".join(description.group("value").strip('"').split()) if description else "Missing definition"


def skill_rows(root: Path, source: str) -> list[str]:
    """Render catalog rows for one declared skill source."""
    rows = []
    index_parent = root / ".dev" / "skills"
    folder = root / ".dev" / "skills"
    for skill in sorted(path for path in folder.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()):
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        kind = skill_type(skill, text)
        declared_source = skill_source(text)
        if declared_source != source:
            continue
        plan = skill / "docs/plan.md"
        qa = skill / "docs/qa.md"
        qa_status = validation_status(qa)
        summary = skill_definition(plan, text)
        plan_link = f"[plan]({relative(index_parent, plan)})" if plan.is_file() else "missing"
        definition_link = f"[`{skill.name}`]({relative(index_parent, skill / 'SKILL.md')})"
        qa_link = f"[qa]({relative(index_parent, qa)})" if qa.is_file() else "missing"
        if source == "project":
            action = skill_action(text, declared_source)
            rows.append(f"| {definition_link} | {action} | {summary} | {kind} | {plan_link} | {qa_link} | {qa_status} |")
        else:
            rows.append(f"| {definition_link} | {summary} | {kind} | {plan_link} | {qa_link} | {qa_status} |")
    return rows


def render(root: Path) -> str:
    name, tagline, proposition, lifecycle = identity(root)
    use = project_use(root)
    project_type, publication_policy = project_configuration(root)
    version = project_version(root)
    ideas = [f"- {idea}" for idea in key_ideas(root)] or ["- PENDING"]
    return "\n".join([
        f"# {name} Index",
        "",
        "## Project identity",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| Project | {name} |",
        f"| Tagline | {tagline} |",
        f"| Core proposition | {proposition} |",
        "| Template | Codebase projects |",
        f"| Current version | {version} |",
        f"| Project use | {use} |",
        f"| Project type | {project_type} |",
        f"| Publication policy | {publication_policy} |",
        f"| Lifecycle state | {lifecycle} |",
        "",
        "## Key ideas",
        "",
        *ideas,
        "",
        "## Project state",
        "",
        "- [Plan](docs/project/plan.md)",
        "- [Release](docs/project/release.md)",
        "- [Roadmap](docs/project/roadmap.md)",
        "- [Architecture](docs/project/architecture.md)",
        "- [Requirements](requirements/)",
        "- [QA](qa/project/README.md)",
        "",
        "## Available skills",
        "",
        "[Skills index](skills/INDEX.md)",
        "",
        "## Next work",
        "",
        next_work(root),
        "",
    ])


def render_skills(root: Path) -> str:
    return "\n".join([
        "# Available Skills",
        "",
        "This is the authoritative catalog of Agent Skills available in this project.",
        "QA status is derived from actual format, documentation, and functionality validation.",
        "",
        "## Internal Skills",
        "",
        "| **Skill** | **Definition** | **Class** | **Plan** | **QA** | **Status** |",
        "| --- | --- | --- | --- | --- | --- |",
        *skill_rows(root, "core"),
        "",
        "## External Skills",
        "",
        "| **Skill** | **Action** | **Definition** | **Class** | **Plan** | **QA** | **Status** |",
        "| --------- | ------------------------ | --------- | -------- | ------ | ---------- | ---------- |",
        *skill_rows(root, "project"),
        "",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate code-worker project and skills indexes.")
    parser.add_argument("--project", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.project.resolve()
    skills = root / ".dev/skills"
    if not skills.is_dir():
        parser.error(f"missing skill directory: {skills}")
    project_index = root / ".dev" / "INDEX.md"
    skills_index = root / ".dev" / "skills" / "INDEX.md"
    project_index.write_text(render(root), encoding="utf-8")
    skills_index.write_text(render_skills(root), encoding="utf-8")
    print(project_index)
    print(skills_index)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
