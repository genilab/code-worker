<h1 align="center">CodeWorker</h1>
<h3 align="center">A normalized, evidence-driven way for AI agents to create and maintain stable codebases.</h3>

## What is CodeWorker?

CodeWorker is a development-control system for AI-assisted codebase work. It
provides the working structure and repeatable workflows that turn an idea into
a controlled software-development lifecycle: project plan, explicit module
requirements, solution architecture, implementation, executable tests,
verification, QA evidence, documentation, releases, and derived indexes.

Rather than deciding how to construct that control system for every project,
you start from a prepared baseline and focus on defining the product you need.
CodeWorker then keeps the artifacts connected: each requirement can lead to
implementation, test evidence, verification, and recorded QA.

## Why do we have CodeWorker?

AI coding tools can generate useful code quickly, but code generation alone
does not make the engineering process visible or controllable. Without explicit
plans, requirements, architecture, QA, documentation, and release evidence,
it is difficult to understand scope, verify outcomes, manage change, or control
the cost of maintenance.

CodeWorker makes those control points explicit. It applies software-development
lifecycle discipline to AI-assisted work so that people define what must be
built, inspect the evidence, and make informed decisions while agents handle
the repeatable workflow.

## How it works

CodeWorker maintains a local development-control system in `.dev/`:

1. **Initialize** — clarify the project, its users, objectives, boundaries,
   constraints, architecture concerns, roadmap, and initial modules.
2. **Plan and specify** — maintain the project plan, solution architecture,
   release plan, roadmap, and independently testable module requirements.
3. **Implement** — build only the approved, traceable behavior.
4. **Verify and assure quality** — run executable tests, inspect documentation,
   and record actual QA evidence for each module.
5. **Document and release** — maintain user-facing documentation, publish
   controlled versions, and preserve GitHub release notes as the changelog.

Indexes are generated from those maintained records. They are the entry point
for navigating the current project state, not a substitute for evidence.

## Getting started

Create and enter the target project directory, then clone the CodeWorker
template:

```bash
git clone https://github.com/kochf1/code-worker.git project-x
cd project-x
```

With the local CodeWorker control package available to your coding agent, run:

```text
Initialize project
```

The kickoff workflow creates the local `.dev/` control records, guides the
project-definition conversation, creates initial module requirement records,
and generates `.dev/INDEX.md`. Start every later workflow from that index.

`.dev/` is intentionally local to development and excluded from this GitHub
template. The GitHub repository contains the reusable codebase baseline;
CodeWorker's local control system contains the project's working plans,
requirements, validation evidence, and skills.

## Example

GraphK uses CodeWorker to establish its project plan, architecture, module
requirements, QA evidence, and implementation workflows before extending its
graph-execution codebase.
