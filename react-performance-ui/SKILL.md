---
name: react-performance-ui
description: Review and improve React UI performance by controlling render work, data flow, loading boundaries, bundle cost, and expensive interaction paths.
---
Use for React/Next.js performance work, not as a generic frontend rule for Angular/Vue/Svelte projects.

1. Measure or identify the slow interaction before optimizing; avoid cargo-cult memoization.
2. Keep state local when possible and avoid broad context/state updates that invalidate large trees.
3. Stabilize expensive derived work only when profiling or code structure justifies it.
4. Split heavyweight, infrequent UI such as editors, maps, charting, admin tools, and large dialogs when appropriate.
5. Avoid request waterfalls; start independent work concurrently and place loading boundaries intentionally.
6. Virtualize genuinely large lists while preserving keyboard/accessibility semantics.
7. Prevent layout shift by reserving dimensions for async media/content.
8. Keep event handlers responsive; move expensive non-urgent work off the immediate interaction path where framework primitives permit.
9. Check hydration/server-client boundaries in frameworks that use them.
10. Verify with production-like builds and representative data.

Prefer observable performance wins over cleverness.
