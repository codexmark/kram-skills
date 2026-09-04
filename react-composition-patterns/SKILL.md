---
name: react-composition-patterns
description: Design scalable React component APIs using composition, explicit state ownership, slots/children, and context only where it improves reuse and readability.
---
Use when React components are accumulating boolean-prop matrices, duplicated wrappers, prop drilling, or tightly coupled feature logic.

1. Prefer composition over adding many mutually interacting boolean props.
2. Keep shared components domain-agnostic; features resolve permissions/business state and pass intent/data down.
3. Use children/slots for structural variation, explicit props for semantic variation, and context for genuinely shared component-family state.
4. Build compound components only when they make the API clearer than a flat prop surface.
5. Separate controlled and uncontrolled behavior deliberately; do not mix ownership ambiguously.
6. Avoid components that fetch unrelated domain data merely because they render it.
7. Keep accessibility semantics inside reusable primitives where possible.
8. Expose escape hatches sparingly and document them.
9. Test public component behavior rather than implementation details.
10. Refactor APIs when consumers need to understand internal component structure to use them correctly.

Optimize for readable call sites and stable semantics, not abstraction count.
