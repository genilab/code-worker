---
name: readme-maintain
description: Create or refresh an accurate root README when an external project or an explicit request requires user-facing documentation.
metadata:
  source: core
  action: Maintain external GitHub documentation when required.
---

# Maintain Readme

## Scope

This is an internal skill. Use it when the project's `AGENTS.md` declares a
README profile or the user directly requests a README. It selects either the
public-release or private-repository template and maintains only the root
document. Its inputs are the declared visibility/profile, approved project
identity, verified implementation evidence, existing README, and available
assets. It produces an accurate README or a clear gap report. It has no user
activation command; a calling workflow invokes it.
Primary agent role: publication-agent.

## Workflow

1. Read the Repository publication declaration in `AGENTS.md`. Escalate a
   missing visibility or README profile rather than inferring one.
2. For `public-release`, use the
   [public-release template](docs/public_release_template.md) and
   [public README process](docs/public_readme_process.md); for `private`,
   use the [private-repository template](docs/private_repo_template.md).
3. Use approved identity, verified capabilities, validation evidence, real
   assets, and accurate existing README material. Do not expose private
   operating details or planned capabilities as present facts.
4. For a public release, retain the template's ordered title, one-line
   description, Infographics, Badges, What does, Getting started, and What
   can you do next sections. For Code-worker, use the verified knowledge
   base purpose and public actions. Embed or link an infographic only when an
   approved file exists in `assets/images/` and the `asset-agent` has handed it
   off for public documentation.
5. Ask for clarification about any material gap before creating the affected
   section. Do not infer public claims, access rules, or release details.
6. Produce the updated README and a concise gap report for any unanswered
   question or unavailable required asset.

## Constraints

- Do not invent setup steps, capabilities, integrations, support channels, banners, or release claims.
- Preserve accurate existing material and use only real assets. If the infographic is required but unavailable, report the gap rather than adding a broken reference.
- Non-goals include using README as an internal info, exposing private
 information, and changing implementation, plans, or release evidence.
