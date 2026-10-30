# Code-worker Reboot — Implementation Status

## Repository state

- Code-worker has its own Git root and the `genilab/code-worker` `origin`.
- The reboot baseline was committed and pushed to `main`; no tag or GitHub
  Release was created.

## Implemented locally

- Replaced the obsolete `.dev/` operating contract with the INFO-based,
  graph-orchestrated [AGENTS.md](../../../AGENTS.md).
- Moved all ten legacy skill packages intact to
  `temp/migration/legacy-code-worker/skills/` and recorded their disposition.
- Created active `skills/`, `assets/docs/`, and asset navigation.
- Consolidated the active catalogue to the eight public-action packages:
  project initialization, module definition, requirements definition, module
  development, module verification, documentation maintenance, release review,
  and information display.
- Added templates for charter, delivery plan, roadmap, requirements matrix,
  test plan, module QA, and release checklist.
- The eight active public actions are implemented by
  `src/code_worker.py` and `src/codeworker/workflow.py`; they persist only
  factual local control records and never publish a release.
- The full local integration suite currently passes. Feature expansion and
  pilot-project validation remain future work.

## Remaining validation

- Run the implemented lifecycle against a real delivery-project pilot.
- Complete a human-approved release review before creating a release, tag, or
  external publication.
