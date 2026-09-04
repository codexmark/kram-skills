---
name: theme-factory
description: Build or compare complete semantic theme systems for applications, documents, or branded interfaces without reducing them to a handful of raw colors.
---
Use when the user asks for light/dark themes, brand themes, theme variants, or a reusable token palette.

1. Start from semantic roles, not hex values: background, surface, raised, text levels, borders, actions, focus, success, warning, danger, info.
2. Define typography, spacing, radius, elevation, motion, and chart colors only when the theme scope requires them.
3. Keep light/dark themes semantically equivalent; do not redesign component behavior between themes.
4. Check text, interactive-state, focus, and status contrast before approving a palette.
5. Avoid pure black/white everywhere when subtler surfaces improve comfort, unless the user explicitly wants AMOLED/high-contrast treatment.
6. Keep brand color separate from semantic success/warning/danger unless the brand meaning legitimately overlaps.
7. Provide a compact token table and implementation-ready variable names.
8. Show sample component mappings so the theme is testable in context.
9. When offering alternatives, vary the system coherently rather than swapping accent colors only.

A theme is a semantic contract, not a moodboard.
