# kram-skills

Curated and extended skills for [Kram](https://github.com/codexmark/kram). Each directory holds one skill
(`<name>/SKILL.md`, frontmatter + playbook) installable with Kram's `skill_install` tool —
just ask Kram: *"install the skills from https://github.com/codexmark/kram-skills"*.

## Skills in this repo (original, MIT)

Discipline: `investigate-first` · `verify-and-stop` · `surgical-patch` · `safe-refactor` · `diagnosing-bugs`

Quality: `code-review-and-quality` · `code-simplification` · `codebase-design` · `domain-modeling`

Process: `planning-and-task-breakdown` · `security-and-hardening` · `frontend-ui-engineering`

### UI/UX — recommended core

`ui-redesign-existing-product` · `ui-visual-audit` · `ux-heuristic-audit` ·
`web-ui-quality-gate` · `design-system-governance` · `frontend-redesign-pipeline`

The core is the conservative default for product, enterprise, admin and backoffice work. It separates
redesign, visual audit, usability audit, browser quality, and design-system governance so several skills
do not accidentally compete as independent art directors.

### UI/UX — extended library

Art direction: `creative-frontend-direction` · `ui-style-explorer` · `taste-parameterized-design` ·
`anti-slop-interface-design` · `soft-ui-direction` · `minimalist-ui-direction` · `brutalist-ui-direction`

Continuity and references: `design-memory` · `design-reference-study` · `image-reference-to-code` ·
`complete-ui-output`

UX/research: `ux-controlled-design` · `ux-innovative-design` · `design-research-and-strategy` ·
`design-sprint` · `hooked-retention-ux` · `design-rating-scorecard`

Platform: `react-performance-ui` · `react-composition-patterns` · `react-native-ui-performance` ·
`ios-hig-design`

Design-to-code / brand: `figma-to-code-handoff` · `stitch-design-handoff` · `theme-factory` ·
`brand-guidelines` · `brand-kit-generation` · `visual-canvas-design` · `skill-authoring`

Motion / spatial / assets: `motion-microinteractions` · `scroll-driven-experience` ·
`immersive-scroll-world` · `image-to-threejs` · `app-store-screenshot-design`

Extended skills are available on purpose: Kram may be used for expressive sites, research, branding,
mobile/native work, motion, 3D, design exploration and experimentation as well as enterprise UI. They are
specialized rather than default; use the narrowest skill that matches the task.

See [UI-UX-CURATION.md](UI-UX-CURATION.md) for the authority model and
[EXTENDED-UI-UX.md](EXTENDED-UI-UX.md) for the extended catalog and source inspiration.

Voice: `ponytail` · `caveman`

## Vendored from external collections (MIT, see THIRD-PARTY-NOTICES.md)

Workflow ([obra/superpowers](https://github.com/obra/superpowers)):
`test-driven-development` · `systematic-debugging` · `verification-before-completion` ·
`brainstorming` · `writing-plans` · `executing-plans` · `requesting-code-review` ·
`receiving-code-review` · `using-git-worktrees` · `finishing-a-development-branch` · `using-superpowers`

Engineering practice ([github/awesome-copilot](https://github.com/github/awesome-copilot)):
`acquire-codebase-knowledge` · `ai-ready` · `bug-reproduction-brief` · `build-evidence-map` ·
`codeql` · `commit-message-storyteller` · `context-map` · `conventional-branch` ·
`conventional-commit` · `create-agentsmd` · `create-llms` · `create-readme` · `dependabot` ·
`documentation-writer` · `github-actions-hardening` · `quality-playbook` · `secret-scanning` · `security-review`

Domain ([vercel-labs/vgpu](https://github.com/vercel-labs/vgpu)): `vgpu`

Each vendored skill's `SOURCE` file records its origin — prefer updating from the
source repos when they evolve.

## Recommended external collections (install from the source — they evolve)

- [obra/superpowers](https://github.com/obra/superpowers) (MIT) — the gold standard for dev-workflow
  skills: `test-driven-development`, `systematic-debugging`, `verification-before-completion`,
  `receiving-code-review`, plus newer ones (`brainstorming`, `writing-plans`, `using-git-worktrees`,
  `subagent-driven-development`).
- [anthropics/skills](https://github.com/anthropics/skills) (Apache 2.0 for general skills) —
  official collection; `mcp-builder` and `skill-creator` are strong coding-agent references.
- [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) — a broad
  curated index when hunting for more.

Ask Kram: *"install test-driven-development and systematic-debugging from https://github.com/obra/superpowers"*.
