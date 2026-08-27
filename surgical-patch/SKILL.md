---
name: surgical-patch
description: Make the smallest change that correctly fixes the issue — measured in blast radius, not lines.
---
When fixing a bug or making a focused change:

1. Identify the minimal set of lines whose change fixes the ROOT cause (investigate-first applies).
2. Do not reformat, rename, reorder, or "clean up" anything you are not changing — every touched line is review surface and merge-conflict surface.
3. If you notice unrelated problems, list them at the end instead of fixing them inline.
4. Prefer a change that is obviously correct over a clever one that needs explanation.

A good patch reads like it was always meant to be there. Diff noise is a defect.
