---
name: maintain-readme
description: Create or refresh an accurate root README when an external project or an explicit request requires user-facing documentation.
source: core
---

# Maintain Readme

## Scope

This is an internal skill. Use it when an external project is created, becomes
external, changes verified user-facing evidence, or receives a direct README
request. It is responsible only for the root README. Its inputs are the project
plan, relevant module records, verified implementation evidence, and available
assets, and it produces an accurate user-facing README or a clear gap report. It
has no user activation command; a calling workflow invokes it.

## Workflow

1. Read `.dev/docs/project/plan.md` and confirm `project_use`, project name, tagline, verified capabilities, setup evidence, and assets; ask for clarification when a required user-facing fact is missing.
2. For `project_use: internal`, report that README maintenance does not apply unless the request explicitly asks for one. Otherwise, maintain the root `README.md`.
3. Use the default layout: centered title and tagline, `assets/images/info.png` when it exists, verified banners, What is, Why, Getting Started, and Examples.
4. Add configuration, integrations, status, support, contribution, or license content only when verified evidence makes it useful; produce the updated README and report unresolved gaps.

## Constraints

- Do not invent setup steps, capabilities, integrations, support channels, banners, or release claims.
- Preserve accurate existing material and use only real assets. If the infographic is required but unavailable, report the gap rather than adding a broken reference.
- Non-goals include maintaining an internal project's README without a direct request and changing implementation, plans, or release evidence.
