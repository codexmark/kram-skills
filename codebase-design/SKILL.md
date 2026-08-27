---
name: codebase-design
description: Place new code where a reader would look for it, matching the codebase's existing architecture.
---
Before adding a new file, package, or layer:

1. Find where similar things already live — the codebase's own answer beats any general principle.
2. A fact/behavior belongs where the reader would look for it, not where it was convenient to write.
3. Respect the existing dependency direction. If your change needs an import that feels backwards, the placement is wrong, not the import rules.
4. New abstractions must pay rent: two real usages minimum, today — not "we might need it".
5. When the existing architecture genuinely blocks the change, say so and propose the smallest structural fix as its own step.
