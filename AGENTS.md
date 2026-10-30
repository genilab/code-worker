# Code-worker

Code-worker is the reusable, graph-orchestrated template for controlled,
evidence-driven agent-oriented software delivery. It helps a developer take a
project from a human-approved purpose through requirements, design,
implementation, verification, documentation, and an explicitly approved
release.

## Navigation

- Start at [INFO.md](INFO.md).
- Read an invoked local skill completely before using or changing it.
- Use [skills/INFO.md](skills/INFO.md) as the local skill catalogue.
- Use local `INFO.md` files under `assets/docs/` to navigate confirmed project
  records; `INFO.md`, not `INDEX.md`, is the default navigation convention.
- Keep migration evidence and retired packages only under `temp/`.

## Operating model

Every delivery project must preserve this traceability path:

```text
purpose -> requirement -> design -> implementation -> verification -> documentation
```

The developer retains approval authority for scope, design, meaningful
tradeoffs, manual or visual acceptance, external publication, and release.
Agents may organize, propose, implement bounded work, and return factual
evidence; they do not invent approval.

Code-worker is the source template, not the repository for a delivery
project's code or releases. A developer creates an independent destination
repository from the Code-worker template, clones that repository into a chosen
folder, and runs `Project init` there. A delivery project must not
retain Code-worker as its destination `origin`, and it never commits or pushes
work back to Code-worker.

`Project init` confirms the project identity, charter, destination repository,
visibility, current-release scope, roadmap, modules, and control-artifact
policy before implementation. The developer explicitly chooses whether that
project's `assets/docs/` and `skills/` folders are `local` or `tracked` in the
destination repository. In `local` mode, their files remain on the developer's
machine and are removed from Git tracking without deletion; in `tracked` mode,
they are versioned only with that delivery project.

Each initialized delivery project uses this baseline:

```text
{project-folder}/
├── AGENTS.md
├── INFO.md
├── README.md
├── src/                         # application source code
├── tests/                       # executable test units
├── skills/                      # project-local bounded skills
│   └── INFO.md
├── assets/                      # project-produced, non-source assets
│   ├── images/
│   ├── reports/
│   └── {other-asset-type}/
├── assets/docs/                 # all maintained project documentation
│   ├── INFO.md
│   ├── plan/
│   ├── requirements/
│   ├── design/diagrams/
│   ├── qa/
│   ├── test/
│   └── {package}/
└── temp/                        # migration or generated working material
```

The root `INFO.md` is the project-wide navigation entry point. `skills/INFO.md`
is the evidence-based skill catalogue. Each maintained documentation area and
package has a local `INFO.md`; no active `INDEX.md` system is created.

## Multi-agent orchestration

Code-worker is a graph-based multi-agent project. The orchestrator interprets
a confirmed public action, routes it to one capability role and bounded skill,
reviews returned evidence, then completes the action, routes a handoff, or
requests a human decision. It does not authorize ambiguous, external,
destructive, or release actions on its own.

| Agent role | Responsibility | Typical evidence | Handoffs |
| --- | --- | --- | --- |
| `orchestrator` | Maintains project state, dependencies, task board, decision log, and traceability. | Updated plan and route outcome. | Requirements, architecture, delivery, verification, documentation, or human reviewer. |
| `requirements-analyst` | Turns an accepted charter into measurable requirements and acceptance criteria. | Requirements matrix. | Architect. |
| `architect` | Defines user flow, modules, data/API boundaries, UML, validation rules, and tradeoffs. | Design package. | Human reviewer, then implementation agent. |
| `implementation-agent` | Builds one approved smallest useful slice. | Source changes and local checks. | Test engineer. |
| `test-engineer` | Plans and performs automated, integration, regression, and edge-case testing. | Test results and module QA. | Visual reviewer or documentation agent. |
| `ui-visual-reviewer` | Checks a real UI, CLI, or API journey. | Manual-test observations and supporting screenshots when useful. | Human reviewer or documentation agent. |
| `documentation-agent` | Maintains verified documentation and project asset records. | Updated documentation and classified assets. | Release reviewer. |
| `release-reviewer` | Checks completion gates and prepares the delivery summary. | Traceability report and release checklist. | Human reviewer. |
| `human-reviewer` | Accepts scope, design, important tradeoffs, manual acceptance, and release. | Explicit decision or requested revision. | Orchestrator. |

The deliberation path is always:

```text
public action -> orchestrator -> agent role -> skill workflow -> evidence
      ^                                                        |
      +------ complete, hand off, or request approval --------+
```

These roles are capability nodes, not a claim that persistent external agents
are already running.

## Public actions and workflows

Use this public sequence:

1. `Project init` guides the developer through the charter, current-release
   scope, roadmap, baseline folders, and required approvals. It does not
   publish or implement product behavior.
2. `Define Modules` creates the delivery plan: modules, dependencies, risks,
   owners, design work, tests, and gates.
3. `Define requirements {module}` establishes measurable behavior and
   acceptance criteria for one selected module.
4. `Develop {module}` delivers that module in small approved work items,
   including source and tests. It does not self-certify QA.
5. `Verify {module}` records actual automated, integration, edge-case, and
   applicable manual verification evidence.
6. `Maintain documentation [ALL | {module}]` refreshes factual lifecycle
   records, supporting assets, and INFO navigation. It is not a Git operation
   and does not manufacture evidence.
7. `Review release` checks traceability, design alignment, verification,
   documentation, limitations, and repository hygiene for human acceptance.
8. `Show info [ALL | {topic}]` opens root or selected existing INFO navigation
   without changing the project.

Charter creation, design-package work, test planning, manual review, asset
management, reflection, and GitHub operations are supporting skill workflows
within this sequence, not separate public actions. GitHub work remains an
explicit post-approval operation for the confirmed destination repository.

Every public action routes through the orchestrator. A missing, failed, or
unapproved gate returns work to the responsible role rather than allowing the
next module or release to proceed.

## Asset management

- Store every project-produced non-source asset under `assets/`; do not place
  generated images, reports, or other assets in `src/`, `tests/`, or outside
  the appropriate `assets/` subfolder.
- `assets/images/` contains approved images and infographics. Store every
  infographic there before referencing it from project documentation.
- `assets/reports/` contains generated or approved project reports. Create a
  purpose-named subfolder only when the project needs another distinct asset
  type.
- Before an asset becomes active, confirm its purpose, type, source or
  provenance, and relationship to a verified project record. Use a factual
  caption or reference when documentation needs it; do not treat an image or
  report as proof of an unsupported product or QA claim.
- `Maintain documentation [ALL | {module}]`, owned by the documentation role,
  performs this classification and storage workflow. It escalates unclear,
  unverified, externally sourced, or publication-sensitive assets.
- Asset storage does not itself publish an asset, modify a release, or mark a
  requirement as verified.

## Development and release boundaries

- Define requirements before design or implementation. Each module has
  acceptance criteria, dependency and risk information, and required test
  coverage before implementation begins.
- Develop one requirement at a time: confirm acceptance and edge cases -> make
  the smallest `src/` change -> add or update `tests/` -> run relevant checks
  -> record QA in `assets/docs/qa/` -> update affected documentation and INFO files.
- The current release contains only the requirements approved for current
  implementation. Put deferred work in the roadmap under its intended future
  release.
- Documentation claims must be backed by maintained records, actual QA, or
  verified implementation. Preserve known limitations and unsupported behavior
  explicitly.
- No commit, push, tag, release, remote change, or external publication occurs
  unless the user explicitly requests that exact operation for the confirmed
  destination repository.

## Reboot transition

The eight active actions are implemented and covered by the local integration
suite. Legacy skills and workflows remain under `temp/migration/` as local
migration evidence, not active guidance. A delivery-project pilot is still
required before a release decision; historical passed records do not transfer
automatically.
