---
name: complete-ui-output
description: Finish UI implementation tasks completely: no placeholder sections, skipped states, partial responsive behavior, or hand-waved design-system work unless explicitly scoped out.
---
Use when the user asks for a complete frontend result or when a design task is prone to stopping at a polished mockup while leaving real states unfinished.

1. Enumerate the promised scope before implementation.
2. Complete every in-scope state: populated, loading, empty, no-results, error, disabled/read-only, submission/progress, success, and destructive confirmation where applicable.
3. Complete responsive behavior for the product's supported widths rather than only the supplied screenshot size.
4. Finish light/dark or platform variants when they are part of the existing product contract.
5. Do not leave `TODO`, placeholder copy, fake data, stub actions, or unexplained visual gaps in finished scope.
6. Reuse or finish shared components instead of patching one page locally.
7. Verify keyboard/focus/accessibility behavior for new interaction surfaces.
8. Run available tests/build/lint and inspect the actual renderer when possible.
9. Report anything intentionally left out, with a concrete reason.

"Complete" means the user can use the delivered scope, not merely see its happy-path appearance.
