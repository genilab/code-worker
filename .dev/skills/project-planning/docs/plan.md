# Skill Plan — project-planning

## Summary

Plan a project from its intended result before implementation starts.

## Description

This external skill leads a human-developer brainstorming conversation from the
final result through requirements, modules, and units of work. It then proposes
a package structure, architecture direction, release plan, and roadmap for
confirmation before creating local control records or starting operations.

## Script Requirements

- It must begin by defining the final result, how a human or system uses it, expected outputs, and observable success.
- It must lead a human-developer conversation from final result to explicit actions, inputs, outputs, boundaries, constraints, quality expectations, and independently owned modules.
- It must progress from modules to the units of work and test evidence each module needs before operational work begins.
- It must propose package structure, module boundaries, architecture direction, initial release, and roadmap while incorporating user-provided preferences.
- It must obtain confirmation before creating the local control baseline and preserve unresolved decisions as questions.
- It must create or maintain project plan, architecture, release, roadmap, and one `{module}_reqs.md` record for every confirmed module.
- It must regenerate indexes and direct the user to `.dev/INDEX.md` for implementation and later QA workflows.
- It must not implement product code, record passing QA, publish a release, or silently configure GitHub.

## Delegation to Code

- Code must copy a declared local CodeWorker control package, render confirmed project records, create module requirement stubs, and regenerate the target index.
- Outcome discovery, requirement interpretation, and delivery-structure proposals remain in the instruction workflow because they require user-specific judgment.

## Code Requirements

- It must reject a missing control source, an unrelated target `.dev/`, an empty result, or no modules.
- It must create target project identity, plan, architecture, release, roadmap, project QA, and one requirement stub for every declared module.
- It must preserve target source code and Git configuration while adding `.dev/` to the target ignore rules and untracking a copied CodeWorker master `.dev/` package without deleting its local files.
- It must have executable test units for input validation and generated control records.
