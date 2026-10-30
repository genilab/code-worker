# Skill Plan — readme-maintain

## Summary

Maintain a verified user-facing README for a full-publication development project.

## Description

`readme-maintain` is an internal skill used when a project's `AGENTS.md`
declares a public-release or private-repository README profile, or on a direct
README request. It uses verified project evidence and reports missing facts
rather than inventing content.

For Code-worker, the public-release README is intentionally limited to a
purpose paragraph, stable GitHub Releases link, and verified Topics table.

## Script Requirements

- It must read repository visibility and README profile from `AGENTS.md`
  before deciding whether README maintenance applies.
- It must select the public-release or private-repository template without
  exposing information beyond the declared visibility.
- It must generate public-release README content in this order: title,
  one-line description, Infographics, Badges, What does, differentiators,
  Getting started, and What can you do next.
- It must reserve infographics for an approved generation process and use only
  verified badges, clone commands, differentiators, and next operations.
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
