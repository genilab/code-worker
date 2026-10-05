---
name: project-planning
description: Plan a CodeWorker-controlled project from its intended result, user experience, boundaries, requirements, and proposed delivery structure.
source: project
action: "Plan a CodeWorker project."
---

# Project Planning

## Scope

This is an external skill. Use it to start a new project or plan an existing
codebase before implementation. It is responsible for leading the human
developer through a brainstorming conversation that translates the desired
result into explicit control records and a proposed delivery structure. Its
inputs are the intended result, how people or systems will use it, expected
outputs, boundaries, constraints, and optional package preferences; its outcome
is an approved local project plan and navigable `.dev/` baseline. User activation command: `Plan project`; alternative: `Initialize project`.

## Workflow

1. Start a brainstorming conversation with the human developer. Ask for the final result first: what the completed project must do, how people or systems use it, what they see or receive, and how success is recognized. Ask for clarification whenever outcomes, users, boundaries, or constraints remain ambiguous.
2. Progress with the developer from result to requirements: required actions, inputs, outputs, quality expectations, exclusions, and acceptance evidence. Preserve unknowns as questions rather than inventing them.
3. Continue from requirements to independently owned modules, then to the units of work and test evidence each module needs. The developer confirms what must be implemented; the agent keeps the resulting requirements explicit and traceable.
4. Propose—not impose—the package structure, module boundaries, solution architecture direction, initial release, and subsequent roadmap. Incorporate any structure the developer already has in mind, then obtain confirmation before bootstrap.
5. Run the planning code with confirmed identity, result, project use, and modules. It creates the local control baseline, initial records, requirement stubs, and derived index.
6. Only after planning is confirmed, begin operational work through the implementation and module-QA workflows. For an external project, invoke `maintain-readme` from verified planning facts; direct work from `.dev/INDEX.md`.

## Constraints

- Project planning must establish the result and requirements before product implementation. It must not write product source code, mark QA passed, publish a release, or silently configure GitHub.
- Keep CodeWorker's master `.dev/` package versioned with CodeWorker. The bootstrap must add `.dev/` to each target project's ignore rules so target control records remain local. Indexes are derived navigation, not evidence.
- The planning code must refuse an unrelated target `.dev/` directory or use its own project as a target. When a target was cloned from CodeWorker, it must retain the master `.dev/` files locally while removing them from that target's Git index. Non-goals include implementation, release publication, and retrospective QA.
- The human developer owns product decisions; the agent must ask, organize, challenge ambiguity, and propose options, but must not infer unconfirmed requirements or begin operational work before confirmation.

## Dependencies

- `maintain-requirements`
- `maintain-index`
- `maintain-readme`
- `validate-module`
