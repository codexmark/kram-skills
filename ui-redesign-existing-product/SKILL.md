---
name: ui-redesign-existing-product
description: Redesign an existing product UI without inventing a parallel design language; preserve domain behavior while improving hierarchy, density, navigation, and visual coherence.
---
Use this when an existing application works but looks inconsistent, scaffold-like, dated, noisy, or visually fragmented.

## Authority first

Before proposing visual changes, establish the project's design authority in this order:

1. legal, safety, security, and domain requirements;
2. existing product/frontend standards;
3. the current design system and semantic tokens;
4. approved product-specific visual direction;
5. existing reusable components and page patterns;
6. this skill.

Never let a redesign create a second design system beside the first one. If the product already has tokens, primitives, components, patterns, and templates, evolve them rather than bypassing them.

## Redesign workflow

1. **Inventory before styling.** Map shell, navigation, routes, page templates, shared components, states, and obvious visual forks.
2. **Find experience seams.** Identify where the application feels like different products: scaffold CRUDs, one-off forms, legacy buttons, duplicated tables, debug-looking detail screens, or inconsistent navigation.
3. **Set product dials.** State three values before redesigning: design variance, motion intensity, and visual density. Enterprise/regulated backoffices usually want low variance, low motion, and medium-high density.
4. **Fix macro hierarchy first.** App shell, navigation, page header, primary action, content order, page width, and grouping come before color polish.
5. **Fix information architecture.** Navigation reflects user tasks and domain language, not database tables, controllers, or internal resource names.
6. **Use page templates.** Lists, details, forms, dashboards, settings, and admin hubs must share recognizable composition.
7. **Remove fallback quality tiers.** Deep admin routes may be generic internally, but the rendered experience must be as polished and coherent as primary operational routes.
8. **Preserve behavior.** Do not alter API contracts, permissions, business rules, or workflows just to simplify a mockup.
9. **Validate responsive transformations.** Mobile is a reprioritization of information, not a squeezed desktop.
10. **Verify in the renderer.** Screenshots or browser inspection are part of the redesign; source code alone is insufficient evidence.

## Enterprise defaults

Prefer:
- calm surfaces and restrained color;
- strong information hierarchy;
- one dominant primary action per page;
- compact but readable tables;
- semantic status badges;
- borders over decorative shadows;
- dedicated pages for complex entities;
- human vocabulary over technical identifiers;
- explicit loading, empty, no-results, error, and success states.

Avoid:
- generic dashboard-template aesthetics;
- excessive glassmorphism, gradients, neon, or large shadows;
- pills for every control;
- cards around every block;
- huge navigation trees;
- debug identifiers with the same visual weight as user-facing data;
- visually inferior scaffold/admin fallbacks.

## Definition of done

Open representative routes from every major product area. If one route looks like another product, a raw CRUD, a debug tool, or an unfinished fallback, the redesign is not done.
