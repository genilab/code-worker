---
name: maintain-readme
description: Create or refresh an accurate root README when an external project or an explicit request requires user-facing documentation.
source: core
---

# Maintain Readme

## Scope

This is an internal skill. Use it when a development project is created,
changes verified user-facing evidence, or receives a direct README
request. It is responsible only for the root README. Its inputs are the project
plan, architecture, release and roadmap records, module requirements and QA,
verified implementation evidence, existing README, and available assets. It
produces an accurate user-facing README or a clear gap report. It has no user
activation command; a calling workflow invokes it.

## Workflow

1. Read `.dev/docs/project/plan.md` and confirm `project_type`, `publication_policy`, and `project_use`. Maintain a root README automatically only for `project_type: development` with `publication_policy: full`. For an application project, require a direct README request and ensure its claims are suitable for its stated publication policy; otherwise report that automatic README maintenance does not apply.
2. Use the maintained project records as follows: the plan supplies Title, Tagline, Core Proposition, Key Ideas, intended result, and boundaries; architecture supplies the solution explanation and a verified infographic candidate; release and roadmap supply verified current scope and explicitly approved future context; module requirements supply supported capabilities; module and project QA supply only claims backed by actual validation; assets supply real images and banners; the existing README supplies accurate material to preserve.
3. Compose the default layout from that evidence: centered Title and Tagline; `assets/images/info.png` when it exists; verified banners; What is; Why; Key Ideas when they help a reader understand the project; Getting Started; Examples; then only useful verified configuration, integration, status, support, contribution, or license content.
4. Ask for clarification with these questions for any material gap before creating the affected section: “Who is the intended reader and what outcome do they need?”; “What is the shortest verified setup path, including prerequisites, command, and expected result?”; “Which real example best demonstrates the result, including input and output?”; “Which capabilities, limitations, or integrations are safe to state publicly?”; “Is there an approved infographic or banner asset, and what does it depict?”; “Which support, contribution, license, or release information should be linked?” Do not infer an answer from a planned or unverified capability.
5. Produce the updated README and a concise gap report for any unanswered question or unavailable required asset.

## Constraints

- Do not invent setup steps, capabilities, integrations, support channels, banners, or release claims.
- Preserve accurate existing material and use only real assets. If the infographic is required but unavailable, report the gap rather than adding a broken reference.
- Non-goals include automatically maintaining an application's README, exposing user information from a private or limited application, and changing implementation, plans, or release evidence.
