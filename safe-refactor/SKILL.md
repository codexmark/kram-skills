---
name: safe-refactor
description: Refactor only under a green test baseline, in small verified steps, preserving behavior.
---
Before refactoring:

1. Establish the baseline: run the existing tests; if the area has none, write characterization tests FIRST that pin current behavior.
2. Refactor in small steps — one rename, one extraction, one move at a time — re-running the tests after each.
3. Never mix refactoring with behavior changes in one step (or one commit). If you find a bug mid-refactor, note it, finish the refactor, fix the bug separately.
4. If tests go red and the fix is not obvious in one step, revert to the last green state rather than digging.

The definition of refactoring is behavior preservation. No green baseline, no refactor.
