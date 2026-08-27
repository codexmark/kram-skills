---
name: code-review-and-quality
description: Review code by risk: correctness first, then clarity, then style — with concrete evidence per finding.
---
When reviewing code (a diff, a PR, a file):

1. Order findings by risk: correctness bugs → security issues → missing error handling → unclear logic → naming/style. Never lead with style.
2. Every finding needs: the location (file:line), the concrete failure scenario ("if X is empty, this panics"), and a suggested fix.
3. Distinguish "must fix" from "consider" explicitly.
4. Verify suspicions before reporting them — read the callee, check the type, run the test. A review full of "might be an issue?" is noise.
5. Say what is GOOD too, briefly — reviewers who only find faults train authors to hide code.
