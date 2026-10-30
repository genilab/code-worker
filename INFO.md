# Code-worker Info

## Description

Code-worker is a reusable graph-orchestrated template for evidence-driven,
agent-oriented software delivery. It guides approved work from a project
charter through requirements, design, implementation, verification,
documentation, and human-approved release.

## Entry Points

| Entry Point | Location |
| --- | --- |
| Skills | [skills/INFO.md](skills/INFO.md) |
| Documentation | [assets/docs/INFO.md](assets/docs/INFO.md) |
| Assets | [assets/INFO.md](assets/INFO.md) |

## Public Interfaces

The local command runner is [src/code_worker.py](src/code_worker.py). Run
`python3 src/code_worker.py --help` to see executable forms of these actions.

- `Project init` guides the developer through charter, release scope, roadmap,
  baseline structure, and approvals. ([project-init](skills/project-init/SKILL.md))
- `Define Modules` defines the approved modules, dependencies, risks, owners,
  and delivery gates. ([module-define](skills/module-define/SKILL.md))
- `Define requirements {module}` creates measurable requirements and
  acceptance criteria for one module. ([requirements-define](skills/requirements-define/SKILL.md))
- `Develop {module}` delivers one approved module incrementally through its
  bounded work items. ([module-develop](skills/module-develop/SKILL.md))
- `Verify {module}` records automated, integration, edge-case, and applicable
  manual verification evidence. ([module-verify](skills/module-verify/SKILL.md))
- `Maintain documentation [ALL | {module}]` refreshes factual documentation,
  assets, and INFO navigation from current evidence. ([documentation-maintain](skills/documentation-maintain/SKILL.md))
- `Review release` checks readiness evidence and requests a human decision; it
  does not publish. ([release-review](skills/release-review/SKILL.md))
- `Show info [ALL | {topic}]` opens the selected existing INFO document
  without changing the project. ([info-show](skills/info-show/SKILL.md))
