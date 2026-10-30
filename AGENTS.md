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
- Use local `INFO.md` files under `docs/` to navigate confirmed project
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
folder, and runs `Project init {folder}` there. A delivery project must not
retain Code-worker as its destination `origin`, and it never commits or pushes
work back to Code-worker.

`Project init` confirms the project identity, charter, destination repository,
visibility, current-release scope, roadmap, modules, and control-artifact
policy before implementation. The developer explicitly chooses whether that
project's `docs/` and `skills/` folders are `local` or `tracked` in the
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
├── docs/                        # all maintained project documentation
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

- `Project init {folder}` guides and validates a new delivery project from its
  charter through current-release scope, roadmap, modules, design baseline,
  and folder structure. It does not publish or implement product behavior.
- `Create or revise charter`, `Plan delivery`, `Define requirements {module}`,
  and `Design {module}` establish human-approved scope and design before a
  work item may be implemented.
- `Implement {work item}` builds one approved requirement slice. `Verify
  {module}` records actual automated evidence, and `Review experience
  {journey}` records manual or visual verification. Implementation does not
  self-certify.
- `Manage assets [scope]` will classify and store a project-produced asset,
  record its provenance and purpose, and update factual documentation
  references when appropriate.
- `Maintain documentation` and `Sync documentation [scope]` update verified
  records and their INFO navigation. Sync is not a Git operation and never
  manufactures QA evidence.
- `Review release` checks traceability, design alignment, automated and manual
  verification, documentation, limitations, and repository hygiene. `GitHub
  {action}` is an explicit follow-on action only after human approval.

Every public action routes through the orchestrator. A missing, failed, or
unapproved gate returns work to the responsible role rather than allowing the
next module or release to proceed.

## Asset management

- Store every project-produced non-source asset under `assets/`; do not place
  generated images, reports, or other assets in `src/`, `tests/`, or `docs/`.
- `assets/images/` contains approved images and infographics. Store every
  infographic there before referencing it from project documentation.
- `assets/reports/` contains generated or approved project reports. Create a
  purpose-named subfolder only when the project needs another distinct asset
  type.
- Before an asset becomes active, confirm its purpose, type, source or
  provenance, and relationship to a verified project record. Use a factual
  caption or reference when documentation needs it; do not treat an image or
  report as proof of an unsupported product or QA claim.
- The planned `asset-manage` skill, owned by the documentation role, performs
  this classification and storage workflow. It escalates unclear, unverified,
  externally sourced, or publication-sensitive assets.
- Asset storage does not itself publish an asset, modify a release, or mark a
  requirement as verified.

## Development and release boundaries

- Define requirements before design or implementation. Each module has
  acceptance criteria, dependency and risk information, and required test
  coverage before implementation begins.
- Develop one requirement at a time: confirm acceptance and edge cases -> make
  the smallest `src/` change -> add or update `tests/` -> run relevant checks
  -> record QA in `docs/qa/` -> update affected documentation and INFO files.
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

The current Code-worker contents are being reconciled to this model. Legacy
skills and workflows are retained under `temp/migration/` before replacement.
They are migration evidence, not active guidance. An imported or rewritten
skill starts `PENDING` and requires fresh validation; historic passed records
do not transfer automatically.
