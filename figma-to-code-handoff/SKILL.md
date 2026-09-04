---
name: figma-to-code-handoff
description: Translate supplied Figma designs/specs into production UI while preserving the target codebase's architecture, semantics, responsiveness, accessibility, and design-system conventions.
---
Use when the user provides Figma frames/specs/tokens or asks for faithful design-to-code implementation.

1. Treat the design as visual/interaction intent, not permission to bypass the application's architecture.
2. Map Figma styles to existing semantic tokens/components before creating new ones.
3. Separate exact visual requirements from incidental frame artifacts such as fixed demo widths, placeholder copy, or prototype-only layers.
4. Reconstruct responsive behavior from constraints, grids, component variants, and product context; do not hardcode one screenshot size.
5. Preserve semantic HTML/native controls and accessibility even when the design file is visually flattened.
6. Identify missing states: hover, focus, active, disabled, loading, empty, error, validation, and reduced motion.
7. Match typography, spacing, alignment, radius, borders, assets, and iconography with reusable implementation primitives.
8. Document any intentional deviation caused by accessibility, platform limitations, or existing product standards.
9. Verify with rendered comparison at representative breakpoints.

Pixel fidelity matters, but maintainable semantic fidelity matters more than reproducing accidental design-file implementation details.
