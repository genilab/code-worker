# Skill Plan — maintain-readme

## Summary

Maintain a verified user-facing README for an external project.

## Description

`maintain-readme` is an internal skill used when an external project needs an
accurate user-facing root README, when a project becomes external, or on a
direct README request. It uses verified project evidence and reports missing
facts rather than inventing content.

## Script Requirements

- It must read `project_use` before deciding whether README maintenance applies.
- It must maintain the root README for an external project and leave an internal project unchanged unless directly requested.
- It must use only verified project evidence and preserve accurate existing README content.
- It must use the defined title, tagline, infographic, verified banners, What is, Why, Getting Started, and Examples layout.
- It must create or refresh the README when an external project is created, becomes external, or receives a direct request.
- It must report unavailable required facts or assets instead of fabricating content.

## Delegation to Code

- No code is delegated because README maintenance depends on project-specific evidence, audience, and editorial judgment.
- Delegate a repeated deterministic fact-extraction or structure-check function to code only when it emerges and add executable test units with it.

## Code Requirements

N/A
