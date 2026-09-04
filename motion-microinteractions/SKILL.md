---
name: motion-microinteractions
description: Add purposeful interface motion, transitions, gestures, and micro-interactions that improve feedback, hierarchy, spatial understanding, and perceived quality.
---
Use when the user asks for animation polish, motion design, hover/press behavior, transitions, or interaction refinement.

1. Every animation needs a job: feedback, continuity, hierarchy, causality, orientation, or brand character.
2. Start from state changes and interaction timing before decorative choreography.
3. Keep routine microinteractions short; longer motion is reserved for meaningful spatial transitions or storytelling.
4. Use easing that matches physical intent; avoid bounce/spring everywhere.
5. Animate compositor-friendly properties when possible and avoid jank on scroll/input paths.
6. Do not delay task completion or hide important state behind animation.
7. Respect `prefers-reduced-motion` or equivalent platform settings with a meaningful reduced alternative.
8. Verify hover, focus, active, keyboard, touch, interruption, rapid repeated input, and reverse transitions.
9. Motion must degrade gracefully on lower-power devices.
10. If removing the animation does not change understanding or brand value, question whether it belongs.
