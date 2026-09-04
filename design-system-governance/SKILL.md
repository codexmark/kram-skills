---
name: design-system-governance
description: Keep frontend decisions coherent across teams and sessions by enforcing one source of truth for tokens, primitives, components, patterns, templates, and product-specific visual rules.
---
Use this when a product is accumulating duplicate components, one-off styling, visual drift, or conflicting design instructions.

## Source-of-truth chain

Establish and preserve this order:

`tokens -> primitives -> components -> patterns -> page templates -> features -> product`

Features may consume the chain; they must not quietly fork it.

## Rules

1. **One authority.** Identify the project's canonical frontend/design standard before editing UI.
2. **Semantic tokens first.** Repeated color, spacing, radius, typography, motion, elevation, and z-index values belong in tokens rather than feature CSS.
3. **Generic components stay generic.** Shared components receive state/intent; they do not know domain roles, entity types, or business rules.
4. **Generalize recurring needs.** When a feature needs a new visual pattern, determine whether it belongs in the design system before making it local.
5. **No shadow systems.** Do not create parallel `new`, `v2`, `modern`, or feature-specific copies of buttons, tables, cards, dialogs, fields, or page headers unless there is a deliberate migration plan.
6. **Preserve decisions across sessions.** A design-memory file may summarize approved decisions, but it must point back to the authoritative standard and never override it.
7. **Deprecate deliberately.** Mark old components, provide migration guidance, verify consumers, then remove.
8. **Treat admin/deep routes as first-class.** Generic implementation is allowed; generic-looking output is not.
9. **Document exceptions.** If a route legitimately diverges, record why, what rule is being overridden, and whether the divergence is temporary.
10. **Guard the system.** Prefer lint/spec/visual regression gates that prevent new arbitrary tokens or duplicated primitives.

## Review checklist

Before approving a UI change, ask:
- did this reuse the existing design system?
- did it introduce a new token or component that already exists under another name?
- is the pattern reusable or genuinely feature-specific?
- will light/dark and responsive behavior remain coherent?
- does this change make another route look obsolete?
- is there now more than one source of truth?

If the answer to the last question is yes, stop and consolidate before continuing.
