---
name: frontend-ui-engineering
description: Build UI mobile-first with real states (loading/empty/error), honest a11y, and the design system's own tokens.
---
When building or changing UI:

1. Every view has four states: loading, empty, error, populated. Design all four or the missing ones will design themselves in production.
2. Use the project's existing components/tokens before inventing any — visual drift starts with one bespoke button.
3. Mobile-first: layout must survive 320px width and 200% zoom. Test keyboard navigation — tab order is architecture, not polish.
4. A11y is structural: semantic elements first, ARIA only where semantics cannot reach; every interactive element needs an accessible name.
5. State lives as high as shared, as low as possible otherwise.
6. Verify in the actual browser/renderer — a component that only passed unit tests has not been seen by anyone.
