---
name: taste-parameterized-design
description: Tune frontend output explicitly with three design dials: structural variance, motion intensity, and visual density.
---
Use when the user wants precise control over how conservative, animated, or information-dense a design should be.

Before proposing UI, state three values from 1-10:

- `DESIGN_VARIANCE`: 1 = conventional/aligned; 10 = highly asymmetric/experimental.
- `MOTION_INTENSITY`: 1 = basic state transitions; 10 = motion-led experience.
- `VISUAL_DENSITY`: 1 = spacious/editorial; 10 = compact/data-dense.

Then apply them consistently:

1. Variance changes composition and hierarchy, not accessibility or basic usability.
2. Motion changes transition richness, not task latency or input predictability.
3. Density changes spacing, control size, table composition, and disclosure strategy without dropping required information.
4. Enterprise/admin defaults are usually roughly `3 / 2 / 7`; marketing/editorial work may legitimately move elsewhere.
5. Do not change the values mid-build without recording why.
6. Respect the project's tokens and component system; the dials tune the system rather than bypassing it.
7. Verify desktop/mobile and reduced-motion behavior after implementation.
