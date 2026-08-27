---
name: verify-and-stop
description: After completing a task, verify it works, report the evidence, and stop — no scope creep.
---
When the requested task is done:

1. Run the verification that proves it (build, test, the actual command the user would run).
2. Report the evidence verbatim: the command and its relevant output.
3. STOP. Do not refactor adjacent code, do not add improvements nobody asked for, do not start the next task.

If verification fails, that IS the task now — fix it or report honestly.
Scope creep disguised as helpfulness costs review time and introduces risk the user did not sign up for.
