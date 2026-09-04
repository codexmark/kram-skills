---
name: frontend-ui-engineering
description: Build UI mobile-first with real states, honest accessibility, and the project's own design system; escalate broad redesigns to the curated redesign pipeline.
---
When building or changing UI:

1. Every view has explicit applicable states: loading, populated, empty, no-results, error, and submission/processing feedback. Missing states will design themselves in production.
2. Use the project's existing components, tokens, and page patterns before inventing any — visual drift starts with one bespoke button.
3. Mobile-first means the task must survive narrow widths and 200% zoom, not merely that CSS technically wraps.
4. Accessibility is structural: semantic elements first, ARIA only where native semantics cannot reach; every interactive element needs an accessible name and visible keyboard focus.
5. State lives as high as shared, as low as possible otherwise. Navigable state such as important filters, sort, pagination, or tabs belongs in the URL when the product benefits from back/forward, refresh, or deep links.
6. Verify in the actual browser/renderer. A component that only passed unit tests has not been visually verified.
7. Keep shared visual components free of business rules; features resolve permissions and domain state, then pass intent/state to the component.
8. Do not ship visually inferior admin/scaffold fallbacks. Generic internal implementation is acceptable; generic-looking rendered UX is not.

For a change spanning multiple routes, the app shell, information architecture, or the design language itself, use `frontend-redesign-pipeline` rather than treating it as a sequence of isolated component edits.
