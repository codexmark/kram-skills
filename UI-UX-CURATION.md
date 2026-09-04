# UI/UX skill curation

The UI/UX skills in this repository are **original Kram playbooks**, not verbatim copies of the projects below.

Kram uses a two-layer model:

1. **Recommended core** — a small set of orthogonal capabilities used by default for product, enterprise, admin and backoffice work.
2. **Extended library** — broader creative, research, branding, motion, spatial, native-mobile, platform-specific and experimental capabilities that remain fully available when the task calls for them.

The goal is not to minimize what Kram can do. The goal is to keep defaults predictable while preserving a wide design toolbox.

## Authority model

Multiple design skills may legitimately disagree. Project authority therefore remains explicit:

`legal/safety/security -> domain correctness -> project frontend standard -> design system -> usability -> requested creative direction -> visual polish -> novelty`

A specialized skill may be more expressive than the core, but it still does not silently override a product's own design system or domain constraints.

## Recommended core

| Kram skill | Role | Primary influences |
| --- | --- | --- |
| `ui-redesign-existing-product` | Transform an existing product without creating a parallel visual language | Taste redesign ideas; controlled enterprise UX |
| `ui-visual-audit` | Hierarchy, spacing, typography, color, depth, density, anti-slop | Refactoring UI principles; Impeccable polish/distill/quieter philosophy |
| `ux-heuristic-audit` | Severity-ranked usability and cognitive-friction audit | Nielsen/Krug-style heuristic review |
| `web-ui-quality-gate` | Accessibility, keyboard, responsive, forms, states, browser quality | Vercel web-interface guidance; Kram frontend engineering rules |
| `design-system-governance` | Keep one source of truth across teams and sessions | Design-memory/persistence patterns; Kram's design-system-first rule |
| `frontend-redesign-pipeline` | Sequence the other capabilities without mixing responsibilities | Kram synthesis |

## Extended library

The extended layer intentionally includes more opinionated and more general skills: art-direction exploration, style families, design reference study, parameterized taste, anti-slop review, controlled/innovative UX, research, design sprint, retention, React/React Native/iOS, Figma/Stitch handoff, theme/brand work, motion, scroll experiences, procedural 3D, App Store assets, visual artifact design and skill authoring.

See [EXTENDED-UI-UX.md](EXTENDED-UI-UX.md) for the complete catalog.

## Source collections reviewed

The Kram playbooks synthesize ideas from the broader public ecosystem while remaining original to this repository. Important sources include:

- Anthropic Claude Code / frontend-design — https://github.com/anthropics/claude-code
- Anthropic Skills — https://github.com/anthropics/skills
- UI/UX Pro Max — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Taste Skill — https://github.com/Leonxlnx/taste-skill
- Impeccable — https://github.com/pbakaus/impeccable
- Hallmark — https://github.com/nutlope/hallmark
- Scroll World — https://github.com/oso95/scroll-world
- Scroll Craft — https://github.com/nateherkai/scroll-craft
- img2threejs — https://github.com/img2threejs/img2threejs
- Interface Design — https://github.com/Dammyjay93/interface-design
- Frontend Design Pro Demo — https://github.com/claudekit/frontend-design-pro-demo
- Designer Skills — https://github.com/Owl-Listener/designer-skills
- Awesome Claude Design — https://github.com/rohitg00/awesome-claude-design
- Bencium marketplace — https://github.com/bencium/bencium-marketplace
- Vercel Agent Skills — https://github.com/vercel-labs/agent-skills
- Wondel Skills — https://github.com/wondelai/skills
- Apple/iOS skills — https://github.com/rshankras/claude-code-apple-skills
- Emil Kowalski design skill — https://github.com/emilkowalski/skill
- App Store screenshots — https://github.com/ParthJadhav/app-store-screenshots
- gstack — https://github.com/garrytan/gstack

## Why not vendor every upstream file verbatim

External collections evolve at different speeds, overlap heavily, may use provider-specific command/plugin layouts, and do not all share the same licensing/provenance model. Kram therefore keeps original provider-agnostic playbooks for the common capabilities and preserves upstream links for richer examples or source-specific integrations.

## Relationship to `frontend-ui-engineering`

`frontend-ui-engineering` remains the small default skill for ordinary UI implementation. Use `frontend-redesign-pipeline` when the request affects multiple routes, the app shell, information architecture, or the design language as a whole. Use an extended skill when the user explicitly needs its specialized design mode.
