---
name: design-memory
description: Persist approved design decisions across sessions without creating a second source of truth beside the project's real design system.
---
Use for long-running products where visual drift appears because multiple agents or sessions repeatedly re-decide the same UI rules.

1. Locate the authoritative frontend/design standard first.
2. Maintain a compact design-memory document only for approved decisions that are not already encoded in tokens/components/docs.
3. Record decisions as: context, decision, rationale, affected patterns, date/version, and source of authority.
4. Link back to canonical tokens/components instead of duplicating their full definitions.
5. Never let the memory file override legal, domain, accessibility, brand, or design-system rules.
6. When a decision becomes stable enough, migrate it into the actual design system or frontend standard and remove the duplicate note.
7. Mark superseded decisions explicitly; stale design memory is worse than no memory.
8. Before new UI work, review relevant decisions and state any intentional deviation.

Suggested memory header:
`This file summarizes approved decisions. It is not the design-system source of truth.`
