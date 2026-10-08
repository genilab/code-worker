# Available Skills

This is the authoritative catalog of Agent Skills available in this project.
QA status is derived from actual format, documentation, and functionality validation.

## Internal Skills

| **Skill** | **Definition** | **Class** | **Plan** | **QA** | **Status** |
| --- | --- | --- | --- | --- | --- |
| [`create-skill`](create-skill/SKILL.md) | Create or revise a managed skill from its completed local plan. | prompt + code | [plan](create-skill/docs/plan.md) | [qa](create-skill/docs/qa.md) | PASSED |
| [`document-code`](document-code/SKILL.md) | Document and validate managed source and test code. | prompt + code | [plan](document-code/docs/plan.md) | [qa](document-code/docs/qa.md) | PASSED |
| [`maintain-index`](maintain-index/SKILL.md) | Regenerate concise, evidence-based project and skill indexes. | prompt + code | [plan](maintain-index/docs/plan.md) | [qa](maintain-index/docs/qa.md) | PASSED |
| [`maintain-readme`](maintain-readme/SKILL.md) | Maintain a verified user-facing README for a full-publication development project. | prompt | [plan](maintain-readme/docs/plan.md) | [qa](maintain-readme/docs/qa.md) | PASSED |
| [`maintain-requirements`](maintain-requirements/SKILL.md) | Maintain one authoritative, GraphK-format requirements record for each target module. | prompt | [plan](maintain-requirements/docs/plan.md) | [qa](maintain-requirements/docs/qa.md) | PASSED |
| [`validate-module`](validate-module/SKILL.md) | Validate one target module and write evidence-based module QA. | prompt | [plan](validate-module/docs/plan.md) | [qa](validate-module/docs/qa.md) | PASSED |
| [`validate-skill`](validate-skill/SKILL.md) | Validate managed skills and refresh their QA evidence and catalog. | prompt + code | [plan](validate-skill/docs/plan.md) | [qa](validate-skill/docs/qa.md) | PASSED |

## External Skills

| **Skill** | **Action** | **Definition** | **Class** | **Plan** | **QA** | **Status** |
| --------- | ------------------------ | --------- | -------- | ------ | ---------- | ---------- |
| [`connect-github`](connect-github/SKILL.md) | Connect a project repository to GitHub. | Connect one standalone project repository to its intended GitHub repository. | prompt + code | [plan](connect-github/docs/plan.md) | [qa](connect-github/docs/qa.md) | PASSED |
| [`project-planning`](project-planning/SKILL.md) | Plan a CodeWorker project. | Plan a project from its intended result before implementation starts. | prompt + code | [plan](project-planning/docs/plan.md) | [qa](project-planning/docs/qa.md) | PASSED |
| [`publish-version`](publish-version/SKILL.md) | Publish a semantic version to GitHub. | Publish the next semantic GitHub release from an already connected project repository. | prompt + code | [plan](publish-version/docs/plan.md) | [qa](publish-version/docs/qa.md) | PASSED |
