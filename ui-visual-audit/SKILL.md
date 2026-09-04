---
name: ui-visual-audit
description: Audit visual hierarchy, spacing, typography, color, depth, density, and anti-slop consistency in an existing interface before release.
---
Use this after a UI exists and needs a disciplined visual review.

## Audit order

1. **Hierarchy without color.** Mentally blur or grayscale the screen. The primary information and action must still dominate.
2. **Spacing relationships.** Related elements sit closer than unrelated groups. Repeated spacing follows the project's scale; arbitrary values are suspect.
3. **Typography.** Use a constrained size/weight scale. Secondary labels and metadata must not compete with values or page titles.
4. **Color discipline.** Color has semantic purpose. Do not use color to compensate for weak hierarchy. Verify contrast.
5. **Depth.** Shadows communicate actual elevation only. Normal panels prefer border/surface separation.
6. **Radius discipline.** Radius should be consistent and purposeful; pill shapes are reserved for badges/chips or controls that semantically need them.
7. **Density.** Enterprise interfaces may be dense, but density must come from good alignment and grouping, not smaller illegible text.
8. **Component consistency.** Buttons, inputs, badges, tables, headers, dialogs, and alerts must look and behave like one family.
9. **Data visualization.** Charts answer a question; colors are limited; axes, legends, tooltips, and comparisons remain readable.
10. **Anti-slop pass.** Remove decorative gradients, unnecessary icons, excessive cards, redundant labels, fake depth, repeated borders, and ornamental motion.

## Findings format

For each issue, report:

- severity: `minor | moderate | major`;
- location: route/component/file when known;
- observed problem;
- why it weakens hierarchy or consistency;
- smallest correction that restores the system.

End with:

- top 5 visual problems;
- design-system changes needed, if any;
- one sentence describing the intended visual character after fixes.

Do not redesign the product from scratch during an audit. Prefer system-level corrections that improve many screens at once.
