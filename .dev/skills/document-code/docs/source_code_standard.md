# Source Code Documentation and Structure Standard

Apply this standard to every created or revised Python source or test module.
It preserves behavior; it does not replace requirements, design decisions, or
executable evidence.

## File prologue

Start an executable entry point with its shebang. Then use this exact header
shape, with a factual project identity and root-relative module path:

```py
#!/usr/bin/env python3
##
## {Project name} - {factual project purpose}.
## {root-relative/path.py} - {brief factual responsibility}.
##
```

Keep any existing license and attribution immediately after the header. Do not
remove, shorten, or replace them without explicit authorization.

## AI instruction and module overview

Before imports, provide one module docstring beginning with `AI instruction:`.
It is maintainers' and coding agents' factual context, not a conversational
prompt. Use at least two bullets to state the module's responsibility,
principal public interface or test subject, and boundaries that must be
preserved. Include explicit exclusions where they prevent a likely ownership
mistake.

```py
"""
AI instruction:
- Provides {responsibility} through {principal interface}.
- Preserves {invariant or boundary}; it does not {out-of-scope behavior}.
"""
```

## Structure and comments

- Order imports as standard library, third-party, then project-local imports,
  with blank lines between groups.
- Keep one statement per line; do not compress conditionals, lifecycle
  transitions, or public methods into semicolon-separated one-liners.
- Give public classes and functions concise factual docstrings. Use comments
  to explain invariants, ownership, ordering, or non-obvious decisions—not to
  narrate obvious syntax.
- Use clear sections only where they improve navigation (for example,
  initialization, public interface, or private helpers). Keep names, types,
  error paths, and control flow readable without relying on the AI instruction.
- Preserve interfaces and behavior while documenting or reformatting. Pair a
  behavior-affecting change with requirements and executable tests instead of
  hiding it in a documentation pass.
