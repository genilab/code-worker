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
| Documentation | [docs/INFO.md](docs/INFO.md) |
| Knowledge | [knowledge/INFO.md](knowledge/INFO.md) |
| Assets | [assets/INFO.md](assets/INFO.md) |
| Migration evidence | [temp/migration/legacy-code-worker/INVENTORY.md](temp/migration/legacy-code-worker/INVENTORY.md) |

## Public Interfaces

- `Project init {folder}` guides initialization of an independent delivery
  project after its destination repository and control-artifact policy are
  confirmed. ([project-init](skills/project-init/SKILL.md))
- `Manage assets [scope]` classifies and stores project-produced assets with
  factual provenance and documentation references. ([asset-manage](skills/asset-manage/SKILL.md))
- `Sync documentation [scope]` refreshes local INFO navigation from maintained
  records and current evidence. ([documentation-sync](skills/documentation-sync/SKILL.md))
- `Review release` checks delivery evidence and prepares a release decision;
  it does not publish. ([release-review](skills/release-review/SKILL.md))
