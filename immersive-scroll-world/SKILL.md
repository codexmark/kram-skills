---
name: immersive-scroll-world
description: Plan cinematic scene-to-scene scroll experiences that may combine generated imagery/video, camera-flight continuity, mobile-specific rendering, and explicit cost/performance approval.
---
Use only when the user explicitly wants an immersive branded world or continuous cinematic scroll experience.

1. Confirm the experience warrants generated media and potentially paid asset pipelines; do not default to them.
2. Define ordered scenes, transition logic, visual continuity, narrative purpose, desktop/mobile aspect strategies, and fallback experience before asset generation.
3. Treat the last frame of one scene and the first frame of the next as a continuity contract.
4. Estimate external generation cost and required tooling before triggering paid or expensive generation; obtain explicit user approval when real spend is involved.
5. Build a non-cinematic fallback that preserves core content and navigation.
6. Keep loading, buffering, decoding, reduced-motion, and mobile bandwidth constraints visible in the design.
7. Avoid scroll-jacking that traps users or makes content inaccessible.
8. Verify every seam, scroll segment, playback state, and orientation with actual rendered output.
9. If generated assets fail continuity, regenerate the seam rather than hiding the cut with UI clutter.
10. Keep the implementation modular so the branded media layer can fail without breaking the page's core information.

This is a specialized, high-cost experience skill, never a normal landing-page default.
