#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/create-skill/code/validate_skill.py - Validates skill format, documentation, functionality, and QA evidence.
##

"""
AI instruction:
- Validates one managed skill against its plan, requirements, source code, and tests.
- Separates format, documentation, and functionality outcomes for QAing.
- Writes evidence only from checks executed during the validation run.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

FRONT_MATTER = re.compile(r"\A---\n(?P<fields>.*?)\n---", re.DOTALL)
SECTION = re.compile(r"^### (?P<name>Script Requirements|Code Requirements)\s*$\n(?P<value>.*?)(?=^###\s|^##\s|\Z)", re.MULTILINE | re.DOTALL)
LEGACY_HEADINGS = ("Short Description", "Action", "Workflow", "Requirements Alignment", "Skill Maintenance")
MINIMAL_HEADINGS = ("Scope", "Workflow", "Constraints")
LEGACY_ROLE = re.compile(r"^\*\*Skill role:\*\*\s*(internal|external)\s*$", re.MULTILINE | re.IGNORECASE)
MINIMAL_ROLE = re.compile(r"\b(?:an?\s+)?(internal|external)\s+skill\b", re.IGNORECASE)
MARKDOWN_SECTION = re.compile(r"^## (?P<name>Activation|Workflow Skills|Scope|Workflow|Constraints|Dependencies)\s*$\n(?P<value>.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
WORKFLOW_SKILL = re.compile(r"^- `(?P<name>[a-z0-9]+(?:-[a-z0-9]+)*)`\s*$", re.MULTILINE)
SCRIPT_REQUIREMENT = re.compile(r"^\s*-\s+\*\*(SR-[A-Z0-9-]+-\d+)\*\*\s*$", re.MULTILINE)
CODE_REQUIREMENT = re.compile(r"^\s*-\s+\*\*(CD-[A-Z0-9-]+-\d+)\*\*\s*$", re.MULTILINE)
SIMPLE_REQUIREMENT = re.compile(r"^\s*-\s+It must\b", re.MULTILINE | re.IGNORECASE)
STATUS = re.compile(
    r"^(?:\|\s*Overall status\s*\|\s*([^|]+)\||-\s*Overall status:\s*([A-Z]+)\s*$)",
    re.MULTILINE | re.IGNORECASE,
)
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def section(text: str, name: str) -> str | None:
    """Return one requirements section without interpreting its content."""
    for match in SECTION.finditer(text):
        if match.group("name") == name:
            return match.group("value")
    return None


def markdown_section(text: str, name: str) -> str | None:
    """Return one non-requirements Markdown section without interpreting it."""
    for match in MARKDOWN_SECTION.finditer(text):
        if match.group("name") == name:
            return match.group("value").strip()
    return None


def h1_titles(text: str) -> list[str]:
    """Return Markdown H1 titles while ignoring examples inside fenced code blocks."""
    titles: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.fullmatch(r"# (?!#)\S.*", line):
            titles.append(line)
    return titles


def plan_section(text: str, name: str) -> str | None:
    """Return one top-level plan section without interpreting its content."""
    match = re.search(
        rf"^## {re.escape(name)}\s*$\n(?P<value>.*?)(?=^##\s|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group("value").strip() if match else None


def project_root(skill: Path) -> Path | None:
    """Locate the project root that owns a managed skill."""
    return next((parent for parent in (skill, *skill.parents) if (parent / ".dev/skills").is_dir()), None)


def known_skills(root: Path) -> set[str]:
    """Return managed skill names available from one project root."""
    return {
        skill.name
        for skill in (root / ".dev/skills").glob("*")
        if (skill / "SKILL.md").is_file()
    }


def qa_status(skill: Path) -> str | None:
    """Return the recorded overall QA status for a skill."""
    report = skill / "docs/qa.md"
    if not report.is_file():
        return None
    match = STATUS.search(report.read_text(encoding="utf-8"))
    return (match.group(1) or match.group(2)).strip().upper() if match else None


def simple_requirements(text: str) -> list[str]:
    """Return current-format requirement bullets without their Markdown marker."""
    return [match.group(1).strip() for match in re.finditer(r"^\s*-\s+(It must\b.*)$", text, re.MULTILINE | re.IGNORECASE)]


def code_documentation_issues(skill: Path, files: list[Path]) -> list[str]:
    """Run the managed source-code documentation validator when available."""
    root = next((parent for parent in (skill, *skill.parents) if (parent / ".dev/skills/document-code/code/validate_code_documentation.py").is_file()), None)
    if root is None:
        return []
    path = root / ".dev/skills/document-code/code/validate_code_documentation.py"
    spec = importlib.util.spec_from_file_location("code_worker_code_documentation", path)
    if spec is None or spec.loader is None:
        return ["FAILED: cannot load the source-code documentation validator"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [f"PENDING: {source.name}: {issue}" for source in files for issue in module.source_issues(source)]


def validation_results(skill: Path, run_code_tests: bool = True) -> dict[str, list[str]]:
    """Collect independent format, documentation, and functionality outcomes."""
    results = {"standard": [], "format": [], "documentation": [], "functionality": []}
    definition = skill / "SKILL.md"
    plan = skill / "docs/plan.md"
    if not definition.is_file():
        results["standard"].append("PENDING: SKILL.md is missing")
        results["format"].append("PENDING: SKILL.md is missing")
        return results
    text = definition.read_text(encoding="utf-8")
    front = FRONT_MATTER.match(text)
    if not front:
        results["standard"].append("PENDING: SKILL.md lacks Codex YAML front matter")
        results["format"].append("PENDING: SKILL.md lacks YAML front matter")
    else:
        if f"name: {skill.name}" not in front.group("fields"):
            results["standard"].append("PENDING: Codex skill name does not match its folder")
            results["format"].append("PENDING: SKILL.md name does not match its folder")
        if not re.search(r"^description:\s*\S", front.group("fields"), re.MULTILINE):
            results["standard"].append("PENDING: Codex skill lacks a discovery description")
            results["format"].append("PENDING: SKILL.md lacks discovery metadata")
        if not re.search(r"^source:\s*(core|project)\s*$", front.group("fields"), re.MULTILINE):
            results["standard"].append("PENDING: Codex skill must declare source as core or project")
            results["format"].append("PENDING: SKILL.md lacks valid source metadata")
    titles = h1_titles(text)
    if len(titles) != 1:
        results["standard"].append("PENDING: Codex skill must contain one concise H1 title")
    if not SKILL_NAME.fullmatch(skill.name):
        results["standard"].append("PENDING: Codex skill folder name must be lowercase hyphenated")
    if "{{" in text or "TODO" in text:
        results["standard"].append("PENDING: Codex skill instruction contains an unfinished placeholder")
    minimal = bool(markdown_section(text, "Scope"))
    required_headings = MINIMAL_HEADINGS if minimal else LEGACY_HEADINGS
    for heading in required_headings:
        if not re.search(rf"^## {re.escape(heading)}\s*$\n(?=\S)", text, re.MULTILINE):
            results["format"].append(f"PENDING: SKILL.md lacks a non-empty {heading} section")
    if minimal:
        scope = markdown_section(text, "Scope") or ""
        workflow = markdown_section(text, "Workflow") or ""
        constraints = markdown_section(text, "Constraints") or ""
        role = MINIMAL_ROLE.search(scope)
        activation = scope
        workflow_skills = markdown_section(text, "Dependencies")
        allowed_headings = {"Scope", "Workflow", "Constraints", "Dependencies"}
        for heading in re.findall(r"^## (?P<name>.+?)\s*$", text, re.MULTILINE):
            if heading not in allowed_headings:
                results["format"].append(f"PENDING: minimal Codex skill has an unsupported {heading} section")
        for heading in ("Short Description", "Action", "Requirements Alignment", "Skill Maintenance"):
            if re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE):
                results["format"].append(f"PENDING: minimal Codex skill must not duplicate the legacy {heading} section")
        descriptive_checks = (
            ("Scope", scope, r"\buse\b", "trigger or use condition"),
            ("Scope", scope, r"\bresponsib", "bounded responsibility"),
            ("Scope or Workflow", f"{scope}\n{workflow}", r"\binput", "input"),
            ("Scope or Workflow", f"{scope}\n{workflow}", r"\b(produc|outcome|result)", "expected outcome"),
            ("Workflow", workflow, r"\bclarif", "clarification condition"),
            ("Constraints", constraints, r"\b(non-goal|must not|do not)\b", "non-goal"),
        )
        for section_name, value, pattern, requirement in descriptive_checks:
            if not re.search(pattern, value, re.IGNORECASE):
                results["format"].append(f"PENDING: minimal Codex skill {section_name} lacks a {requirement}")
    else:
        role = LEGACY_ROLE.search(text)
        activation = markdown_section(text, "Activation")
        workflow_skills = markdown_section(text, "Workflow Skills")
        if project_root(skill):
            results["format"].append("PENDING: newly managed skills must use the authoritative minimal Codex skill format")
    if not role:
        results["format"].append("PENDING: SKILL.md lacks an internal or external skill role")
    elif role.group(1).lower() == "external" and (not front or not re.search(r"^action:\s*\S", front.group("fields"), re.MULTILINE)):
        results["standard"].append("PENDING: external skill must declare an action")
        results["format"].append("PENDING: SKILL.md lacks external action metadata")
    if not activation:
        results["format"].append("PENDING: SKILL.md lacks an activation declaration")
    elif role and role.group(1).lower() == "external" and "user activation command:" not in activation.lower():
        results["format"].append("PENDING: external skill lacks a user activation command")
    elif role and role.group(1).lower() == "internal" and not re.search(r"no\s+user\s+activation\s+command", activation, re.IGNORECASE):
        results["format"].append("PENDING: internal skill must declare no user activation command")
    if minimal and not workflow_skills:
        pass
    elif not workflow_skills:
        results["format"].append("PENDING: SKILL.md lacks a workflow-skills declaration")
    elif workflow_skills != "- None.":
        root = project_root(skill)
        if root:
            for name in WORKFLOW_SKILL.findall(workflow_skills):
                if name not in known_skills(root):
                    results["format"].append(f"PENDING: workflow skill `{name}` is not managed by this project")
    plan_text = plan.read_text(encoding="utf-8") if plan.is_file() else ""
    current_plan = bool(plan_section(plan_text, "Summary"))
    if not plan.is_file():
        results["documentation"].append("PENDING: docs/plan.md is missing")
        script_text = code_text = ""
    elif current_plan:
        for heading in ("Summary", "Description", "Script Requirements", "Delegation to Code", "Code Requirements"):
            if not plan_section(plan_text, heading):
                results["documentation"].append(f"PENDING: docs/plan.md lacks {heading}")
        if plan_section(plan_text, "Completion Conditions"):
            results["documentation"].append("PENDING: current plan format must not include Completion Conditions")
        script_text = plan_section(plan_text, "Script Requirements") or ""
        code_text = plan_section(plan_text, "Code Requirements") or ""
        delegation = plan_section(plan_text, "Delegation to Code") or ""
        if re.search(r"^\|.*\|\s*$", delegation, re.MULTILINE):
            results["documentation"].append("PENDING: Delegation to Code must use bullets or prose, not a table")
        if not SIMPLE_REQUIREMENT.findall(script_text):
            results["documentation"].append("PENDING: Script Requirements must contain bullets beginning with 'It must'")
        if re.search(r"^\|", script_text, re.MULTILINE) or re.search(r"^\|", code_text, re.MULTILINE):
            results["documentation"].append("PENDING: current plan requirements must not use tables")
    else:
        for heading in ("Overall Requirements", "Delegation to Code", "Requirements", "Completion Conditions"):
            if not plan_section(plan_text, heading):
                results["documentation"].append(f"PENDING: docs/plan.md lacks {heading}")
        overall = plan_section(plan_text, "Overall Requirements")
        if overall:
            for label in ("Role:", "Activation:", "Workflow skills:"):
                if label not in overall:
                    results["documentation"].append(f"PENDING: Overall Requirements lacks {label} workflow instruction")
        if plan_section(plan_text, "Workflow Composition"):
            results["documentation"].append("PENDING: workflow composition belongs in Overall Requirements, not a separate section")
        delegation = plan_section(plan_text, "Delegation to Code") or ""
        if re.search(r"^\|.*\|\s*$", delegation, re.MULTILINE):
            results["documentation"].append("PENDING: Delegation to Code must use bullets or prose, not a table")
        script_text = section(plan_text, "Script Requirements") or ""
        code_text = section(plan_text, "Code Requirements") or ""
        if not script_text:
            results["documentation"].append("PENDING: plan lacks Script Requirements")
        if not code_text:
            results["documentation"].append("PENDING: plan lacks Code Requirements")
        script_ids = SCRIPT_REQUIREMENT.findall(script_text)
        if not script_ids:
            results["documentation"].append("PENDING: plan's Script Requirements lack SR identifiers")
        if re.search(r"^\|", script_text, re.MULTILINE):
            results["documentation"].append("PENDING: Script Requirements must use structured bullets, not a table")
        if re.search(r"^\|", code_text, re.MULTILINE):
            results["documentation"].append("PENDING: Code Requirements must use structured bullets, not a table")
        for identifier in script_ids:
            if identifier not in text:
                results["documentation"].append(f"PENDING: SKILL.md does not align with {identifier}")
    if skill.name == "create-skill":
        format_record = skill / "docs/skill_format.md"
        if not format_record.is_file():
            results["documentation"].append("PENDING: authoritative minimal skill-format record is missing")
        else:
            format_text = format_record.read_text(encoding="utf-8")
            for heading in ("Required Structure", "Required Meaning"):
                if not re.search(rf"^## {heading}\s*$", format_text, re.MULTILINE):
                    results["documentation"].append(f"PENDING: authoritative skill-format record lacks {heading}")
    code = sorted((skill / "code").glob("*.py")) if (skill / "code").is_dir() else []
    tests = sorted((skill / "tests").glob("test_*.py")) if (skill / "tests").is_dir() else []
    results["documentation"].extend(code_documentation_issues(skill, code + tests))
    code_ids = CODE_REQUIREMENT.findall(code_text)
    simple_code_requirements = SIMPLE_REQUIREMENT.findall(code_text)
    if code:
        if current_plan and not simple_code_requirements:
            results["functionality"].append("PENDING: Code Requirements must contain bullets beginning with 'It must'")
        elif not current_plan and not code_ids:
            results["functionality"].append("PENDING: code files lack CD requirement identifiers")
        if not tests:
            results["functionality"].append("PENDING: code files lack executable test units")
        elif run_code_tests:
            for test in tests:
                completed = subprocess.run([sys.executable, str(test)], capture_output=True, text=True, check=False)
                output = completed.stdout + completed.stderr
                if completed.returncode:
                    results["functionality"].append(f"FAILED: {test.name} failed")
                elif "skipped=" in output.lower() or "PENDING" in output:
                    results["functionality"].append(f"PENDING: {test.name} remains a generated pending test unit")
    elif current_plan and code_text.strip() != "N/A":
        results["functionality"].append("PENDING: Code Requirements must be N/A when no code exists")
    elif code_ids:
        results["functionality"].append("PENDING: Code Requirements exist without source code")
    elif code_text.strip() != "N/A" and "No code portion is currently required." not in code_text:
        results["documentation"].append("PENDING: Code Requirements must explain the absent code portion")
    return results


def validate_skill(skill: Path, run_code_tests: bool = True) -> list[str]:
    """Return every unmet validation condition for callers needing a flat list."""
    return [issue for issues in validation_results(skill, run_code_tests).values() for issue in issues]


def category_status(issues: list[str], applicable: bool = True) -> str:
    """Reduce one QA category to a report status."""
    if not applicable:
        return "N/A"
    if any(issue.startswith("FAILED:") for issue in issues):
        return "FAILED"
    return "PENDING" if issues else "PASSED"


def write_qa(skill: Path, results: dict[str, list[str]]) -> Path:
    """Write actual QA evidence produced by the current validation run."""
    code_files = list((skill / "code").glob("*.py")) if (skill / "code").is_dir() else []
    requirement_text = (skill / "docs/plan.md").read_text(encoding="utf-8")
    current_plan = bool(plan_section(requirement_text, "Summary"))
    code_text = plan_section(requirement_text, "Code Requirements") if current_plan else section(requirement_text, "Code Requirements")
    planned_code = bool(CODE_REQUIREMENT.findall(code_text or "")) or (current_plan and (code_text or "").strip() != "N/A")
    code_ids = CODE_REQUIREMENT.findall(code_text or "")
    functionality_applies = bool(code_files) or planned_code
    statuses = {
        category: category_status(results[category], applicable)
        for category, applicable in (("standard", True), ("format", True), ("documentation", True), ("functionality", functionality_applies))
    }
    def detail(category: str, applicable: bool = True) -> str:
        if not applicable:
            return "N/A — no code portion is required."
        return "; ".join(results[category]) if results[category] else "Actual checks passed."

    script_text = plan_section(requirement_text, "Script Requirements") if current_plan else section(requirement_text, "Script Requirements")
    script_requirements = simple_requirements(script_text or "")
    code_requirements = simple_requirements(code_text or "")
    if not script_requirements:
        script_requirements = [f"Requirement record: {identifier}" for identifier in SCRIPT_REQUIREMENT.findall(script_text or "")]
    if not code_requirements and code_ids:
        code_requirements = [f"Requirement record: {identifier}" for identifier in code_ids]
    test_units = sorted((skill / "tests").glob("test_*.py")) if (skill / "tests").is_dir() else []
    overall = "FAILED" if "FAILED" in statuses.values() else "PENDING" if "PENDING" in statuses.values() else "PASSED"
    gaps = [issue for category in results.values() for issue in category]
    lines = [
        f"# QA — {skill.name}",
        "",
        "## Summary",
        "",
        f"- Overall status: {overall}",
        f"- Scope: `{skill.name}` instruction script, plan, code, test units, and local QA evidence.",
        f"- Standard alignment: {statuses['standard']} — {detail('standard')}",
        "- Validation executed: standard alignment, format, documentation, requirement coverage, code documentation, and executable test checks.",
        f"- Result: {detail('format')} {detail('documentation')} {detail('functionality', functionality_applies)}",
        "- Outstanding gaps: None." if not gaps else "- Outstanding gaps: " + "; ".join(gaps),
        "",
        "## Validation Execution",
        "",
        "### Standard Alignment",
        "",
        "- Executed: Codex skill-structure validation on `SKILL.md`.",
        "- Checks: lowercase hyphenated folder name, matching YAML name, discovery description, one H1 title, and absence of unfinished instruction placeholders.",
        f"- Result: {statuses['standard']} — {detail('standard')}",
        "",
        "### Format",
        "",
        "- Executed: managed skill-format validation on `SKILL.md` and `docs/plan.md`.",
        "- Checks: discovery metadata; minimal Scope, Workflow, and Constraints structure; trigger, responsibility, input, outcome, clarification, and non-goal statements; role, activation, dependencies, and required plan structure.",
        f"- Result: {statuses['format']} — {detail('format')}",
        "",
        "### Documentation",
        "",
        "- Executed: plan, instruction, and source-documentation validation.",
        "- Checks: plan-to-instruction coverage and required code-documentation structure.",
        f"- Result: {statuses['documentation']} — {detail('documentation')}",
        "",
        "### Functionality",
        "",
        "- Executed: each available executable test unit.",
        "- Checks: code behavior and generated-skill workflow behavior.",
        f"- Result: {statuses['functionality']} — {detail('functionality', functionality_applies)}",
        "",
        "## Requirement Traceability",
        "",
        "### Script Requirements",
        "",
    ]
    for requirement in script_requirements:
        requirement_status = "FAILED" if "FAILED" in (statuses["format"], statuses["documentation"]) else "PENDING" if "PENDING" in (statuses["format"], statuses["documentation"]) else "PASSED"
        lines.append(f"- {requirement} — {requirement_status} — Verified by the current format and documentation checks of `SKILL.md` and the managed skill package.")
    lines.extend(["", "### Code Requirements", ""])
    if not code_requirements:
        lines.append("- N/A — N/A — No code requirement is declared.")
    else:
        for requirement in code_requirements:
            lines.append(f"- {requirement} — {statuses['functionality']} — Verified by the current code-documentation and executable-test checks.")
    lines.extend(["", "## Executed Test Units", ""])
    if test_units:
        for test in test_units:
            lines.append(f"- `{test.relative_to(skill)}`: {statuses['functionality']} — {detail('functionality', functionality_applies)}")
    else:
        lines.append("- N/A — no executable test unit is required.")
    report = skill / "docs/qa.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a managed Agent Skill and write its QA.")
    parser.add_argument("skill", type=Path)
    parser.add_argument("--no-code-tests", action="store_true")
    args = parser.parse_args()
    results = validation_results(args.skill.resolve(), run_code_tests=not args.no_code_tests)
    write_qa(args.skill.resolve(), results)
    issues = [issue for items in results.values() for issue in items]
    if issues:
        print("SKILL VALIDATION FAILED")
        print("\n".join(f"- {issue}" for issue in issues))
        return 1
    print("SKILL VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
