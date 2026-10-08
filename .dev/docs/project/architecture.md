# Solution Architecture

**Status:** Draft — preserve the established invariants and complete the marked
design decisions as the project plan becomes concrete.

## Architectural purpose

`code-worker` separates a target product from the development-control system
that governs it.

The front matter in `.dev/docs/project/plan.md` declares `project_use` as
`internal` or `external`. Its Title, Tagline, Core Proposition, and Key Ideas
sections provide the authoritative user-facing project identity and message.
External projects must
maintain their root `README.md` for users; internal projects do not require one.
An external-project creation, conversion to external use, or direct README
request invokes `maintain-readme`.

{{QUESTION: What architectural qualities matter most—such as simplicity, portability, automation, extensibility, or auditability—and why?}}

```text
src/ + tests/                 target product and its executable tests
.dev/requirements/            authoritative requirements
.dev/skills/{skill}/          flat managed skills; front matter declares source
.dev/qa/{package}/            module QAs; `qa/project/` holds project-wide QA
.dev/INDEX.md                 evidence-derived navigation and status
```

## Components and responsibilities

| Component | Responsibility | Design decision / open question |
| --- | --- | --- |
| `src/` and `tests/` | The target product and its executable tests. | {{QUESTION: What product-module conventions should apply when target code exists?}} |
| `.dev/skills/{skill}/` | One flat package per managed skill; `source: core` identifies template-control work and `source: project` identifies target-project work. | {{QUESTION: Which core capabilities should be added after the foundational three?}} |
| `.dev/requirements/` | One authoritative `{module}_reqs.md` document per module, maintained by [maintain-requirements](../../skills/maintain-requirements/SKILL.md). | {{QUESTION: What module-prefix and ownership conventions should be adopted?}} |
| `.dev/qa/{package}/` | One `{module}_qa.md` file per module with actual validation results, maintained by [validate-module](../../skills/validate-module/SKILL.md). | {{QUESTION: What evidence-retention policy is required?}} |

Skills are Agent Skills. Each has a `SKILL.md`; code that implements a skill
belong in that skill's `code/` directory, and skill-specific tests belong in
its `tests/` directory. A skill's `scripts/` directory, when needed, is
reserved for GenAI scripts rather than executable code. Every skill owns its plan, including script and code requirements, in
`docs/plan.md`, and actual validation evidence in `docs/qa.md`.
Target-product requirements remain under
`.dev/requirements/`.

Every managed process uses the same design chain:

```text
action → workflow → skill
```

An **action** names the bounded outcome. A **workflow** defines how that
outcome is performed. A **skill** is the executable prompt and optional code
implementation that owns the workflow, its requirements, tests, validation,
and catalog entry.

## Skill routing

Every skill activates its own workflow and declares the skills that workflow
may invoke. The declaration is an explicit workflow map, not permission to
run an unrelated skill.

| Role | Activation | Use |
| --- | --- | --- |
| External | A user activation command, such as `$plan-project`. | A user-facing entry point that starts a workflow. |
| Internal | No user activation command; invoked by a calling workflow. | Reusable support functionality such as documentation, validation, or index maintenance. |

The skills index separates internal and external skills. Each skill definition
retains its activation and associated workflow skills, making routing
inspectable before a workflow runs.

## Source Code Documentation

All source code—skill code and test units as well as target code and
tests—uses the GraphK-adapted standard maintained within the `document-code`
skill. That skill creates or revises the documentation, and project validation
checks it before code test evidence is accepted.

## Information flow

```text
project plan → requirements → solution design → implementation → tests
     ↑                                                        ↓
roadmap ← release plan ← QA evidence ← validation ←─┘
```

{{QUESTION: Which information flows, integrations, or automation boundaries need to be added to this model?}}

## Invariants

- Target-project code belongs in `src/`; its executable tests belong in `tests/`.
- Every meaningful implementation maps to explicit requirements and a recorded
  QA.
- `.dev/INDEX.md` is derived navigation, not an evidence store.
- `.dev/skills/INDEX.md` derives each skill definition from the corresponding
  skill plan's `Overview`, with discovery metadata as a fallback.

## Open design decisions

{{QUESTION: Which unresolved architectural decision must be made before the next release can be designed?}}
