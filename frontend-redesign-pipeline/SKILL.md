---
name: frontend-redesign-pipeline
description: Orchestrate a safe redesign of an existing frontend by sequencing discovery, UX audit, visual audit, implementation, polish, and final web quality gates.
---
Use this when the user wants a broad redesign rather than an isolated component fix.

## Required sequence

Do not run every UI skill at once. Use this pipeline:

1. **Investigate first.** Map routes, shell, shared components, tokens, page templates, states, and product-specific design rules. Read the project's frontend/design authority before proposing changes.
2. **Governance check.** Apply `design-system-governance`. Determine what must be reused, what may evolve, and where visual forks already exist.
3. **Redesign proposal.** Apply `ui-redesign-existing-product`. Produce the macro composition and information-architecture changes before touching polish.
4. **Usability audit.** Apply `ux-heuristic-audit` to the proposal. S3/S4 task risks override aesthetic preferences.
5. **Visual audit.** Apply `ui-visual-audit`. Consolidate hierarchy, spacing, type, color, depth, and density into one solution.
6. **Implement system-first.** Change tokens/primitives/components/patterns/templates before one-off route styling.
7. **Polish pass.** Remove visual noise, redundant containers, excessive radius/shadows, decorative color, and other AI-template artifacts.
8. **Final web gate.** Apply `web-ui-quality-gate` for accessibility, keyboard, responsive behavior, forms, states, URL/context behavior, and browser-visible quality.
9. **Regression sweep.** Open representative routes from every product area. A redesign is incomplete if deep/admin routes remain visually inferior.
10. **Report evidence.** Summarize routes reviewed, system-level changes, remaining exceptions, renderer/browser verification, and tests run.

## Decision priority

When recommendations conflict, use:

`legal/safety/security > domain correctness > project frontend standard > design system > usability > visual polish > novelty`

## Stop conditions

Stop and consolidate if:
- a second design system starts emerging;
- new components duplicate existing primitives;
- the proposal alters business behavior merely to fit a mockup;
- a high-severity usability issue is being hidden by visual polish;
- screenshots/browser evidence contradicts source-level assumptions.

The goal is not maximum novelty. The goal is one coherent product whose visual quality survives every route and state.
