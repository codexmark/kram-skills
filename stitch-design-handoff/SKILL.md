---
name: stitch-design-handoff
description: Prepare or consume portable design specifications for Google Stitch-style workflows while preserving semantic tokens, responsive intent, and production-code architecture.
---
Use when a design is moving between a generative design tool and implementation through a portable design/spec document.

1. Treat the handoff artifact as a contract: product context, design principles, tokens, typography, layout grid, components, states, responsive rules, motion, and anti-patterns.
2. Keep token names semantic rather than tool-specific.
3. Distinguish required visual behavior from illustrative mockup content.
4. Include interactive states and accessibility expectations that a static design tool may omit.
5. On import, map the spec onto the target project's existing design system before adding new primitives.
6. Record deviations caused by framework/platform constraints.
7. Keep the handoff human-readable and portable; avoid embedding assumptions that require one specific model/provider.
8. Verify the generated/implemented result against the same design contract after each transfer.

The goal is lossless design intent across tools, not loyalty to one generator's internal format.
