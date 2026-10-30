# QA — info-show

## Summary

- Overall status: PASSED
- Result: Info display resolves the root INFO document without writing to the
  delivery project.

## Evidence

- `python3 -m unittest discover -s tests -v`: PASSED —
  `test_info_display_and_link_audit`.
