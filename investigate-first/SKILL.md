---
name: investigate-first
description: Read the relevant code and reproduce the problem before proposing any change.
---
Before proposing ANY fix or feature change:

1. Read the code paths involved — the actual files, not your assumption of them.
2. Reproduce the problem (run the failing command, hit the endpoint, trigger the bug). If you cannot reproduce it, say so explicitly before proceeding.
3. State the root cause in one sentence, citing file:line evidence.
4. Only then propose the change.

Hard rule: never write "the problem is probably X" — either you verified X or you say you could not.
