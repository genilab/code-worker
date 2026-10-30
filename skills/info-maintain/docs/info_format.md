# Code-worker INFO Format

This is the authoritative format for the Code-worker root and skills
INFO documents. `info-maintain`, `skill-create`, and `skill-validate` must
apply it whenever they create, revise, or check either document.

## Master INFO

The root file is named `INFO.md` and contains exactly these sections, in this
order:

```md
# Code-worker Info

## Description

{One paragraph describing Code-worker as a knowledge-base maintainer and
how its topic-based knowledge base works.}

## Entry Points

| Entry Point | Location |
| --- | --- |
| Skills | [skills/INFO.md](skills/INFO.md) |
| Knowledge | [knowledge/INFO.md](knowledge/INFO.md) |

## Public Interfaces

- `{action}` {what the action does and how its workflow works}.
  ([workflow-name](skills/workflow-name/SKILL.md))
```

Do not add project metadata, status tables, plans, QA, release details, a
README substitute, or any other sections to the master INFO document.

## Skills INFO

The local file is named `skills/INFO.md`. It contains exactly the title below
and one table, with no description before the table and no content after it:

```md
# SKILLS Info

| Skill | Action | Status | Plan | QA |
| --- | --- | --- | --- | --- |
| [skill-name](skill-name/SKILL.md) | Bounded action. | PENDING | [Plan](skill-name/docs/plan.md) | [QA](skill-name/docs/qa.md) |
```

List every managed local skill once, alphabetically by its folder name. The
Status value is evidence-based (`VERIFIED`, `PENDING`, `FAILED`, or another
documented current state); it is never inferred from a missing or stale QA
record. The Action value comes from the corresponding package's
`metadata.action` value; it does not define or activate a public user action.
