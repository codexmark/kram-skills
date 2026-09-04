# UI/UX skill curation

The UI/UX skills in this repository are **original Kram playbooks**, not verbatim copies of the projects below. They synthesize recurring, compatible ideas into a smaller set of orthogonal capabilities that match Kram's existing `<name>/SKILL.md` model.

## Why curate instead of vendoring everything

The upstream collections overlap heavily. Installing them all as independent authorities can produce conflicting advice: one skill optimizes novelty, another consistency; one prefers spacious marketing layouts, another dense enterprise work; one persists its own design memory while the project already has a design system.

Kram therefore keeps the useful capabilities but makes project authority explicit:

`legal/safety/security -> domain correctness -> project frontend standard -> design system -> usability -> visual polish -> novelty`

## Curated skills

| Kram skill | Role | Primary influences |
| --- | --- | --- |
| `ui-redesign-existing-product` | Transform an existing product without creating a parallel visual language | Taste `redesign-existing-projects`; controlled enterprise UX ideas |
| `ui-visual-audit` | Hierarchy, spacing, typography, color, depth, density, anti-slop | Wondel `refactoring-ui`; Impeccable polish/distill/quieter philosophy |
| `ux-heuristic-audit` | Severity-ranked usability and cognitive-friction audit | Wondel `ux-heuristics`; Nielsen-style heuristic review |
| `web-ui-quality-gate` | Accessibility, keyboard, responsive, forms, states, browser quality | Vercel `web-design-guidelines`; existing Kram frontend engineering rules |
| `design-system-governance` | Keep one source of truth across teams and sessions | Interface Design persistence concept; Kram's existing design-system-first rule |
| `frontend-redesign-pipeline` | Sequence the other capabilities without mixing their responsibilities | Kram synthesis |

## Source collections reviewed

- Taste Skill — https://github.com/Leonxlnx/taste-skill
- Impeccable — https://github.com/pbakaus/impeccable
- Wondel Skills (`refactoring-ui`, `ux-heuristics`) — https://github.com/wondelai/skills
- Vercel Agent Skills (`web-design-guidelines`) — https://github.com/vercel-labs/agent-skills
- Interface Design — https://github.com/Dammyjay93/interface-design
- Bencium marketplace / controlled UX — https://github.com/bencium/bencium-marketplace
- UI/UX Pro Max — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

## Deliberately not promoted to Kram core authority

Highly expressive or novelty-oriented design skills can be useful for landing pages, portfolios, experimental sites, and ideation, but they are intentionally not encoded as defaults for product/backoffice work. Kram's curated set prioritizes transfer of learning, accessibility, task efficiency, design-system coherence, and renderer-visible quality.

## Relationship to `frontend-ui-engineering`

`frontend-ui-engineering` remains the small default skill for ordinary UI implementation. Use `frontend-redesign-pipeline` when the request affects multiple routes, the app shell, information architecture, or the design language as a whole.
