# kram-skills

Curated skills for [Kram](https://github.com/codexmark/kram). Each directory holds one skill
(`<name>/SKILL.md`, frontmatter + playbook) installable with Kram's `skill_install` tool —
just ask Kram: *"install the skills from https://github.com/codexmark/kram-skills"*.

## Skills in this repo (original, MIT)

Discipline: `investigate-first` · `verify-and-stop` · `surgical-patch` · `safe-refactor` · `diagnosing-bugs`

Quality: `code-review-and-quality` · `code-simplification` · `codebase-design` · `domain-modeling`

Process: `planning-and-task-breakdown` · `security-and-hardening` · `frontend-ui-engineering`

UI/UX: `ui-redesign-existing-product` · `ui-visual-audit` · `ux-heuristic-audit` ·
`web-ui-quality-gate` · `design-system-governance` · `frontend-redesign-pipeline`

Voice: `ponytail` · `caveman`

### UI/UX curation

The UI/UX set is intentionally smaller than the upstream Claude/design-skill ecosystem. It separates
transformation, visual audit, heuristic audit, web quality, and design-system governance so multiple
skills do not compete as independent art directors. `frontend-redesign-pipeline` defines the recommended
sequence for broad redesign work; `frontend-ui-engineering` remains the lightweight default for ordinary
component/page implementation.

See [UI-UX-CURATION.md](UI-UX-CURATION.md) for the reviewed source collections and curation rationale.

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
  official collection; `mcp-builder` and `skill-creator` are the coding-agent picks.
- [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) — the
  curated index when hunting for more.

Ask Kram: *"install test-driven-development and systematic-debugging from https://github.com/obra/superpowers"*.
