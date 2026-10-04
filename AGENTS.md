# code-worker

`code-worker` is a GitHub template for evidence-driven codebase development.
Its development-control structure stays local; it does not generate a second
repository by default.

## Operating model

1. Start at [.dev/INDEX.md](.dev/INDEX.md), then read the relevant plan, requirements,
   skill, and QA.
2. Read `project_use` in `.dev/docs/project/plan.md`: an external project must maintain
   its root `README.md` through `maintain-readme`; an internal project does not
   require one. Run `maintain-readme` when an external project is created,
   when an internal project becomes external, or on a direct README request.
3. Use the applicable Agent Skill in `.dev/skills/`. Every created or revised
   Python file must follow the `document-code`
   [source-code standard](.dev/skills/document-code/docs/source_code_standard.md):
   factual header, retained license, `AI instruction:` context block, readable
   structure, public docstrings, and purposeful comments.
4. Define requirements before design or implementation, and keep the
   implementation traceable to them. Store one `{module}_reqs.md` file per
   target module under `.dev/requirements/`.
5. Store project-wide records under `.dev/docs/project/` and
   `.dev/qa/project/`. Store a module's documentation and QA under
   `.dev/docs/{package}/` and `.dev/qa/{package}/`, mirroring its source
   package path.
6. Keep every managed skill directly under `.dev/skills/{skill}/`; use its
   front-matter `source` field (`core` or `project`) to state its origin. Every
   external skill must also declare its bounded `action` in front matter so the
   skills index can route users to the correct operation.
7. Run the appropriate validation and record the actual outcome in the
   module's package-scoped QA record.
8. Regenerate `.dev/INDEX.md` through `maintain-index`; never use an index to
   manufacture a passing status.

The lifecycle is Plan → Requirements → Design → Implement → Validate → Deploy.
Core skills maintain this operating system; external skills are added only
when a target product needs a user-facing workflow.
