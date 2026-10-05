#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## .dev/skills/create-skill/code/create_skill.py - Creates unified skill plans, test-unit starters, and QA records.
##

"""
AI instruction:
- Scaffolds the unified plan-and-requirements record required before a skill receives implementation.
- Delegates deterministic work to code and creates a pending test-unit starter.
- Leaves QA results pending until validation runs actual checks.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
RESOURCE_NAMES = {"code", "scripts", "references", "assets", "tests"}


def skill_document(
    name: str,
    description: str,
    source: str,
    skill_type: str,
    role: str,
    activation: str,
    workflow_skills: list[str],
    action: str,
    workflow: str,
) -> str:
    action_metadata = f"action: {json.dumps(action)}\n" if role == "external" else ""
    dependencies = (
        "\n\n## Dependencies\n\n" + "\n".join(f"- `{skill}`" for skill in workflow_skills)
        if workflow_skills
        else ""
    )
    return f"""---
name: {name}
description: {json.dumps(description)}
source: {source}
{action_metadata}---

# {name.replace('-', ' ').title()}

## Scope

This is an {role} skill. Use it for this bounded operation: {description}
It is responsible only for **{action}**. {activation}

## Workflow

1. Read the completed `docs/plan.md` before creating or revising this skill. Use it to identify the request inputs, expected outcome, decisions, and boundaries.
2. Confirm the request is in scope; ask for clarification when a required input, decision, or boundary is missing.
3. {workflow}
4. Produce the outcome defined by the completed plan. Cover every Script Requirement and implement only the deterministic work delegated to code.
5. Maintain the plan, QA evidence, code, and test units together; validate the completed package before recording it as passed.

## Constraints

- Keep this skill narrowly scoped to **{action}**.
- Keep `SKILL.md` minimal: YAML discovery metadata, one title, Scope, Workflow, Constraints, and Dependencies only when this workflow invokes another managed skill.
- Describe the trigger, responsibility, inputs, outcome, clarification conditions, and non-goals in those sections; do not create duplicate descriptive sections.
- Keep planning and QA records in `docs/`; keep deterministic implementation in `code/` and its executable test units in `tests/` only when the plan delegates work to code.
- Do not leave unresolved placeholders or create duplicate, catchall, or unsupported support artifacts.{dependencies}
"""


def plan_document(name: str, action: str, workflow: str, skill_type: str, role: str, activation: str, workflow_skills: list[str]) -> str:
    delegation = (
        "- Delegate the repeated, deterministic parts of this operation to code.\n"
        "- Explain which functions code must implement and verify with executable test units."
        if skill_type != "instruction"
        else "- No code is delegated now because this operation depends on project-specific judgment in `SKILL.md`.\n"
        "- Delegate a function to code only when repeatable, deterministic work emerges."
    )
    code_requirements = (
        "N/A"
        if skill_type == "instruction"
        else "- It must implement the deterministic functions identified in Delegation to Code and prove them with executable test units."
    )
    workflow_summary = ", ".join(f"`{skill}`" for skill in workflow_skills) or "None."
    return f"""# Skill Plan — {name}

## Summary

This {role} skill performs **{action}**.

## Description

This {role} skill exists to **{action}**. It follows this workflow:
**{workflow}**. Activation: {activation} Workflow skills: {workflow_summary}

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must perform **{action}** through **{workflow}** with clear inputs, outputs, controls, and incomplete conditions.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

{delegation}

## Code Requirements

{code_requirements}
"""


def qa_document(name: str) -> str:
    return f"""# QA — {name}

## Summary

- Overall status: PENDING
- Scope: `{name}` skill package.
- Standard alignment: PENDING — Not yet executed.
- Validation executed: Not yet executed.
- Result: PENDING
- Outstanding gaps: Run validate-skill after implementation.

## Validation Execution

- Pending validation.

## Requirement Traceability

- Pending — PENDING — Complete the plan, instruction script, code, and test units before validation.

## Executed Test Units

- Pending validation.

"""


def test_unit_document(name: str) -> str:
    class_name = "".join(part.title() for part in name.split("-")) + "CodeTest"
    return f'''#!/usr/bin/env python3
##
## code-worker - Foundational development operating system
## tests/test_{name.replace('-', '_')}.py - Pending test-unit starter for the {name} skill.
##

"""
AI instruction:
- Reserves executable evidence for the {name} code requirement.
- Keeps generated behavior explicitly pending until requirement-specific assertions replace it.
"""

import unittest


class {class_name}(unittest.TestCase):
    @unittest.skip("PENDING: implement requirement-specific test assertions")
    def test_code_requirement(self) -> None:
        self.fail("Replace this generated test unit.")


if __name__ == "__main__":
    unittest.main()
'''


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a managed code-worker Agent Skill.")
    parser.add_argument("name")
    parser.add_argument("--source", required=True, choices=("core", "project"), help="Origin of this flat skill package.")
    parser.add_argument("--description", required=True, help="Concise statement of what the skill does and when to use it.")
    parser.add_argument("--action", required=True)
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--type", default="instruction", choices=("instruction", "code-backed", "hybrid"))
    parser.add_argument("--role", required=True, choices=("internal", "external"))
    parser.add_argument("--activation", help="External user command or internal workflow trigger.")
    parser.add_argument("--workflow-skills", default="", help="Comma-separated skills this workflow may invoke.")
    parser.add_argument("--resources", default="", help="Comma-separated: code,scripts,references,assets,tests")
    parser.add_argument("--project", type=Path, default=Path("."))
    args = parser.parse_args()
    if not NAME.fullmatch(args.name) or not args.description.strip() or not args.action.strip() or not args.workflow.strip():
        parser.error("name, description, action, and workflow must be complete")
    resources = {item.strip() for item in args.resources.split(",") if item.strip()}
    if resources - RESOURCE_NAMES:
        parser.error("unsupported resources: " + ", ".join(sorted(resources - RESOURCE_NAMES)))
    if args.type != "instruction":
        resources.update({"code", "tests"})
    workflow_skills = [name.strip() for name in args.workflow_skills.split(",") if name.strip()]
    if any(not NAME.fullmatch(name) for name in workflow_skills):
        parser.error("workflow skill names must use lowercase hyphenated names")
    activation = args.activation.strip() if args.activation else (
        f"User activation command: `${args.name}`." if args.role == "external"
        else "Internal workflow only; no user activation command. Invoked by its calling workflow."
    )
    root = args.project.resolve()
    skills_directory = root / ".dev/skills"
    destination = skills_directory / args.name
    if destination.exists():
        parser.error("skill destination is unavailable")
    skills_directory.mkdir(parents=True, exist_ok=True)
    destination.mkdir()
    for resource in sorted(resources):
        (destination / resource).mkdir()
    (destination / "docs").mkdir()
    (destination / "SKILL.md").write_text(skill_document(args.name, args.description.strip(), args.source, args.type, args.role, activation, workflow_skills, args.action.strip(), args.workflow.strip()), encoding="utf-8")
    (destination / "docs/plan.md").write_text(plan_document(args.name, args.action.strip(), args.workflow.strip(), args.type, args.role, activation, workflow_skills), encoding="utf-8")
    (destination / "docs/qa.md").write_text(qa_document(args.name), encoding="utf-8")
    if args.type != "instruction":
        (destination / "tests" / f"test_{args.name.replace('-', '_')}.py").write_text(test_unit_document(args.name), encoding="utf-8")
    maintainer = root / ".dev/skills/maintain-index/code/maintain_index.py"
    completed = subprocess.run([sys.executable, str(maintainer), "--project", str(root)], check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
