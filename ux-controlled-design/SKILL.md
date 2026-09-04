---
name: ux-controlled-design
description: Design within strict enterprise, government, regulated, safety-critical, or high-accountability constraints where predictability and auditability outrank novelty.
---
Use for operational systems, government backoffices, finance, healthcare administration, infrastructure, compliance, or any workflow where mistakes have real consequences.

Priorities:
1. task correctness and error prevention;
2. visibility of system state;
3. predictable navigation and action placement;
4. clear permissions and consequences;
5. auditability and traceable feedback;
6. accessibility and keyboard operation;
7. visual coherence;
8. novelty last.

Rules:
- prefer domain vocabulary over technical implementation terms;
- expose status, ownership, deadlines, dependencies, and irreversible effects clearly;
- use confirmations only for consequential actions, with explicit verbs and consequences;
- preserve context after navigation, errors, retries, and back/forward actions;
- avoid hidden gestures, novelty navigation, ambiguous icon-only actions, or decorative motion;
- dense information is acceptable when hierarchy and scanning remain strong;
- render deep/admin routes at the same quality level as headline product routes.

When in doubt, choose the interaction a trained operator can predict before clicking.
