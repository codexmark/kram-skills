---
name: code-simplification
description: Reduce code to the simplest form that passes the same tests — delete before you add.
---
When asked to simplify (or when your own draft feels heavy):

1. Delete first: dead code, unused parameters, speculative abstraction, comments that restate the code.
2. Inline single-use indirection: a helper called once, an interface with one implementation, a config for a value that never varies.
3. Flatten: early returns over nested conditionals; guard clauses over else-chains.
4. The tests define "same behavior" — run them after every removal.
5. Stop at simple, not at clever. Code golf is complexity wearing a costume.
