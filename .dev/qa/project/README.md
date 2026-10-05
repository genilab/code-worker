# Project QA

This folder holds project-wide quality records. Store each target module's QA
record under `.dev/qa/{package}/{module}_qa.md`; do not place module QA files
directly in `.dev/qa/`. The internal `validate-module` skill owns the module QA
format and creates or updates those records from actual evidence.
