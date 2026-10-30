#!/usr/bin/env python3
"""Command-line entry point for Code-worker's eight public actions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from codeworker.workflow import (
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


def _emit(value: object) -> None:
    print(json.dumps(value, indent=2, sort_keys=True, default=str))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Execute Code-worker lifecycle actions locally.")
    subcommands = parser.add_subparsers(dest="action", required=True)

    init = subcommands.add_parser("project-init", help="Project init")
    init.add_argument("--project", required=True, type=Path)
    init.add_argument("--name", required=True)
    init.add_argument("--release", required=True)
    init.add_argument("--roadmap", required=True)
    init.add_argument("--visibility", required=True, choices=("public", "private"))
    init.add_argument("--artifact-policy", required=True, choices=("local", "tracked"))

    modules = subcommands.add_parser("define-modules", help="Define Modules")
    modules.add_argument("--project", required=True, type=Path)
    modules.add_argument("--module", required=True)
    modules.add_argument("--goal", required=True)
    modules.add_argument("--dependency", action="append", default=[])
    modules.add_argument("--risk", action="append", default=[])
    modules.add_argument("--owner", default="implementation-agent")

    requirements = subcommands.add_parser("define-requirements", help="Define requirements {module}")
    requirements.add_argument("--project", required=True, type=Path)
    requirements.add_argument("--module", required=True)
    requirements.add_argument("--id", required=True)
    requirements.add_argument("--description", required=True)
    requirements.add_argument("--acceptance", required=True)

    develop = subcommands.add_parser("develop", help="Develop {module}")
    develop.add_argument("--project", required=True, type=Path)
    develop.add_argument("--module", required=True)
    develop.add_argument("--implementation", required=True, action="append")
    develop.add_argument("--test", required=True, action="append")

    verify = subcommands.add_parser("verify", help="Verify {module}")
    verify.add_argument("--project", required=True, type=Path)
    verify.add_argument("--module", required=True)
    verify.add_argument("--check", required=True, nargs=argparse.REMAINDER, help="Test command and arguments")

    docs = subcommands.add_parser("maintain-documentation", help="Maintain documentation [ALL | {module}]")
    docs.add_argument("--project", required=True, type=Path)
    docs.add_argument("--scope", default="ALL")

    review = subcommands.add_parser("review-release", help="Review release")
    review.add_argument("--project", required=True, type=Path)
    review.add_argument("--release", required=True)
    review.add_argument("--human-approved", action="store_true")

    show = subcommands.add_parser("show-info", help="Show info [ALL | {topic}]")
    show.add_argument("--project", required=True, type=Path)
    show.add_argument("--topic", default="ALL")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.action == "project-init":
            _emit({"created": initialize_project(args.project, name=args.name, release=args.release, roadmap=args.roadmap, visibility=args.visibility, artifact_policy=args.artifact_policy)})
        elif args.action == "define-modules":
            _emit(define_module(args.project, name=args.module, goal=args.goal, dependencies=args.dependency, risks=args.risk, owner=args.owner).__dict__)
        elif args.action == "define-requirements":
            _emit(define_requirement(args.project, module_name=args.module, requirement_id=args.id, description=args.description, acceptance=args.acceptance))
        elif args.action == "develop":
            _emit(record_development(args.project, module_name=args.module, implementation=args.implementation, tests=args.test).__dict__)
        elif args.action == "verify":
            _emit(verify_module(args.project, module_name=args.module, check=args.check))
        elif args.action == "maintain-documentation":
            _emit(maintain_documentation(args.project, scope=args.scope))
        elif args.action == "review-release":
            _emit(review_release(args.project, release=args.release, human_approved=args.human_approved))
        else:
            target, content = show_info(args.project, topic=args.topic)
            print(f"# {target}\n\n{content}", end="")
    except WorkflowError as error:
        print(f"Code-worker action blocked: {error}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
