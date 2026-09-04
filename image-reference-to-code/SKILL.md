---
name: image-reference-to-code
description: Recreate or adapt a supplied UI screenshot/reference into production frontend code by extracting structure, tokens, components, responsive intent, and interaction states before implementation.
---
Use when the user supplies a UI image and wants code that closely matches or adapts it.

1. Inventory the reference: layout regions, grid, typography, colors, spacing, radii, borders, elevation, icons/assets, states, and apparent breakpoints.
2. Separate visual facts from guesses. State uncertain behavior that cannot be inferred from a static image.
3. Map repeated visual elements to reusable components and semantic tokens.
4. Reproduce hierarchy and proportions before micro-polish.
5. Adapt the reference to the target framework/design system rather than dumping absolute-positioned screenshot tracing into production.
6. Infer responsive behavior conservatively and verify at multiple widths.
7. Add missing focus/hover/loading/error/empty states consistent with the reference and product standard.
8. Preserve accessibility even when the screenshot lacks semantic information.
9. Compare rendered output side by side and iterate on the highest-impact mismatches first.
10. Do not copy protected branding/assets beyond what the user is authorized to use.
