---
name: skill-authoring
description: Create, review, and maintain reusable Kram skills with narrow scope, clear triggers, deterministic workflows, safety boundaries, and minimal overlap with existing skills.
---
Use when creating a new skill or refactoring an existing skill collection.

1. Define the exact job of the skill in one sentence.
2. Search the current skill library for overlap before adding another capability.
3. Prefer one orthogonal responsibility over a giant skill that tries to direct every phase of work.
4. Write frontmatter with a stable `name` and a description that explains when the skill should trigger.
5. Encode workflow, decision rules, stop conditions, evidence expectations, and explicit non-goals.
6. Put project/user/domain authority above the skill; a skill is reusable guidance, not a license to override local standards.
7. Avoid provider-specific tool syntax unless the skill is intentionally provider-specific.
8. For third-party material, preserve license/provenance and avoid copying content whose license is unclear.
9. Include examples only when they remove ambiguity; do not bloat every skill into a textbook.
10. Test the skill against at least one normal case, one edge case, and one conflicting-instruction case.
11. Update catalog/docs when adding, renaming, or deprecating skills.
12. Deprecate duplicates instead of keeping multiple near-identical authorities indefinitely.

A good skill should make the agent more predictable, not merely more verbose.
