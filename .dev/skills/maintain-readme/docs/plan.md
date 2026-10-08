# Skill Plan — maintain-readme

## Summary

Maintain a verified user-facing README for a full-publication development project.

## Description

`maintain-readme` is an internal skill used when a full-publication development project needs an
accurate user-facing root README, when a project becomes external, or on a
direct README request. It uses verified project evidence and reports missing
facts rather than inventing content.

## Script Requirements

- It must read `project_type`, `publication_policy`, and `project_use` before deciding whether README maintenance applies.
- It must maintain the root README automatically for a development project with full publication and leave an application project unchanged unless directly requested.
- It must collect composition evidence from the project plan, architecture, release and roadmap records, module requirements, QA, existing README, and available assets, preserving accurate existing content.
- It must use the plan's Title, Tagline, Core Proposition, and Key Ideas; verified architecture and requirements; QA-backed claims; and real assets to compose the infographic, banners, What is, Why, optional Key Ideas, Getting Started, and Examples layout.
- It must ask the embedded audience, setup, example, public-capability, visual-asset, and support/contribution/license questions when the maintained records do not supply a required user-facing fact.
- It must create or refresh the README when a full-publication development project is created or receives a direct request, and it must never infer that an application is safe to publish.
- It must report unavailable required facts or assets instead of fabricating content.

## Delegation to Code

- No code is delegated because README maintenance depends on project-specific evidence, audience, and editorial judgment.
- Delegate a repeated deterministic fact-extraction or structure-check function to code only when it emerges and add executable test units with it.

## Code Requirements

N/A
