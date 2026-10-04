<h1 align="center">code-worker</h1>
<h3 align="center">An evidence-driven development template for codebase projects.</h3>

## What is code-worker?

code-worker is a GitHub template for projects that work with a codebase. It
provides a consistent `src/` and `tests/` starting point, alongside a local
development-control workflow for planning, requirements, QA, and skills.

## Why do we have code-worker?

It gives codebase projects a repeatable baseline instead of rebuilding their
working structure and evidence practices from scratch. GraphK is the first
project using this template.

## Getting Started

1. Create a new repository from the code-worker template and clone it.
2. Place product source code in `src/` and executable tests in `tests/`.
3. Keep local development-control records in `.dev/`; they are excluded from
   the GitHub template.
4. Define each module's requirements as `.dev/requirements/{module}_reqs.md`
   and record its QA as `.dev/qa/{package}/{module}_qa.md`, mirroring the
   source package path.

## Examples

- **GraphK:** apply code-worker as the local development-control baseline while
  developing the GraphK codebase.
