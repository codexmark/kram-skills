---
name: ux-heuristic-audit
description: Audit an interface for cognitive friction, predictability, error prevention, recoverability, and task efficiency using severity-ranked usability heuristics.
---
Use this to review whether a UI is understandable and operable, not merely attractive.

## Heuristics

Audit against these ten questions:

1. **System status:** does the user always know what is happening?
2. **Real-world match:** does language reflect the user's domain instead of implementation jargon?
3. **Control and freedom:** can the user cancel, go back, undo, or recover when appropriate?
4. **Consistency:** do equivalent actions, statuses, and components behave the same way everywhere?
5. **Error prevention:** does the UI prevent predictable mistakes before they become backend failures?
6. **Recognition over recall:** is necessary context visible instead of requiring memory?
7. **Efficiency:** are frequent tasks fast without making uncommon tasks confusing?
8. **Minimalism:** is every visible element helping a decision, task, or orientation?
9. **Error recovery:** do errors explain what happened and what the user can do next?
10. **Help in context:** when the domain is complex, is guidance available at the point of need?

## Severity

Classify every finding:

- `S0` cosmetic only;
- `S1` small friction;
- `S2` meaningful usability problem;
- `S3` serious task risk or repeated operational cost;
- `S4` blocks a task, creates dangerous ambiguity, or can lead to material operational/legal error.

S3/S4 findings outrank visual polish.

## Operational-system checks

For enterprise, government, regulated, or backoffice systems, additionally verify:

- current status is explicit on every lifecycle entity;
- destructive/irreversible actions communicate consequence;
- routine reversible actions are not burdened with needless confirmation;
- filters/search/sort survive navigation when users are working a queue;
- permissions do not create misleading affordances;
- empty, no-results, loading, and error states are distinct;
- technical identifiers do not displace the human identity of a record;
- audit/history is human-readable;
- the user can tell what needs attention now.

## Output

Return findings ordered by severity, then a short remediation plan grouped into:

1. navigation/orientation;
2. task flow;
3. errors/recovery;
4. consistency;
5. efficiency.

Do not suggest visual novelty unless it directly improves one of those categories.
