---
name: scroll-driven-experience
description: Design scroll-linked storytelling, pinned scenes, scrubbed media, reveal sequences, and long-form interactive pages with accessibility, performance, and self-verification gates.
---
Use when scroll is intentionally part of the narrative or interaction model.

1. Decide whether scroll is navigation, timeline, reveal mechanism, or camera control; do not mix modes casually.
2. Build a content argument that still makes sense without animation.
3. Use one coherent page grammar and a small set of signature behaviors rather than animating every section differently.
4. Keep text readable at every scroll position; avoid states where content exists only at a precise pixel.
5. Provide reduced-motion and non-script fallbacks where practical.
6. Prevent scroll-jacking that breaks expected browser/device behavior.
7. Reserve dimensions for media and verify decoding/loading before the user reaches the scene.
8. Measure for dead scroll, unreachable states, stuck pins, contrast failures over moving media, and mobile layout breakage.
9. Test with keyboard/page navigation, touch, trackpad, and lower-power hardware.
10. For long cinematic pages, generate a contact-sheet or equivalent checkpoint review across the full scroll timeline.

Scroll is a progression mechanism, not an excuse to hide ordinary content behind spectacle.
