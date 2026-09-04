---
name: image-to-threejs
description: Reconstruct a visual reference as procedural Three.js code by decomposing form, material, lighting, camera, and detail, then iterating against rendered comparisons.
---
Use when the user wants a 3D object or scene recreated from a reference image primarily as code rather than imported mesh assets.

1. Inventory the subject: primary volumes, silhouette, proportions, materials, repeated details, decals/text, lighting, and camera perspective.
2. Decide what can be represented with primitives, generated geometry, curves, instancing, shaders, or procedural textures.
3. Build large forms first; do not spend tokens on tiny detail before silhouette/proportion match.
4. Match camera and lighting before judging geometry accuracy.
5. Keep geometry and material parameters named and editable rather than embedding unexplained magic numbers.
6. Render comparison checkpoints after each major pass.
7. Optimize repeated parts with instancing/parametric generation when appropriate.
8. Avoid downloading opaque third-party models unless the user explicitly allows asset use; state when the reconstruction is an approximation.
9. Keep runtime performance appropriate for the target browser/device.
10. Stop adding detail when it no longer changes the target viewing distance meaningfully.

Prefer inspectable procedural structure over a visually similar but unmaintainable pile of geometry.
