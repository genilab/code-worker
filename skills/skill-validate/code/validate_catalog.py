#!/usr/bin/env python3
"""Validate the current Code-worker skill catalog and its INFO links."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml


ALLOWED = {"name", "description", "license", "allowed-tools", "metadata"}
ROLE = re.compile(r"^Primary agent role: ([a-z][a-z0-9-]*)\.$", re.M)


def check(project: Path) -> list[str]:
    """Return catalog-schema errors; an empty list means the catalog is valid."""
    skills_root = project / "skills"
    packages = sorted(path for path in skills_root.iterdir() if path.is_dir())
    errors, actions = [], {}
    for package in packages:
        skill, plan, qa = package / "SKILL.md", package / "docs/plan.md", package / "docs/qa.md"
        if not all(path.is_file() for path in (skill, plan, qa)):
            errors.append(f"{package.name}: missing SKILL.md, plan, or QA")
            continue
        source = skill.read_text()
        front = re.match(r"^---\n(.*?)\n---", source, re.S)
        data = yaml.safe_load(front.group(1)) if front else {}
        if not isinstance(data, dict) or set(data) - ALLOWED:
            errors.append(f"{package.name}: unsupported front matter")
            continue
        meta = data.get("metadata")
        if data.get("name") != package.name or not isinstance(meta, dict) or not meta.get("action"):
            errors.append(f"{package.name}: invalid name or metadata.action")
            continue
        if len(ROLE.findall(source)) != 1:
            errors.append(f"{package.name}: requires exactly one primary agent role")
            continue
        actions[package.name] = meta["action"]
    catalog = (skills_root / "INFO.md").read_text() if (skills_root / "INFO.md").is_file() else ""
    rows = dict(re.findall(r"^\| \[([^]]+)\]\([^)]*\) \| (.*?) \| [^|]+ \|", catalog, re.M))
    if list(rows) != list(actions): errors.append("Skills Info does not list packages alphabetically")
    for name, action in actions.items():
        if rows.get(name) != action: errors.append(f"{name}: catalog action mismatch")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path("."))
    args = parser.parse_args()
    errors = check(args.project)
    if errors:
        raise SystemExit("\n".join(errors))
    print("Code-worker catalog is valid.")
