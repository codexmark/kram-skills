---
name: claude-optimizer
description: Session hygiene for long agent work — notice when a conversation has grown too long or drifted topics, write a handoff file that preserves the thread, and resume cleanly in a fresh session. Use at session start, when a context-size reminder arrives, or when the user says "handoff", "break the session", "resume" or "continue from HANDOFF".
---
Long conversations cost more on every turn (the whole history is re-read) and get worse at remembering
early details. The fix is to break the session at a natural pause — without losing the thread.
Reply to the user in their own language.

## 1. At session start (when loaded)

Confirm in ONE line that session hygiene is on. No lecture. Then work normally, keeping these habits:

- One topic per session. A new, unrelated topic is a reason to break.
- Read file ranges, not whole large files. Filter command output (errors only, last lines) instead of dumping logs.
- Subagents only for broad searches whose conclusion matters more than the raw output. Multi-agent workflows only when the task truly needs many agents — they multiply usage.
- Match model and effort to the task: routine work on a mid-tier model / medium effort; the top model and max effort only for genuinely hard problems.
- Plan before large changes — correcting a plan is cheaper than redoing code.

## 2. Signals that it is time to break

Any one is enough:

- A `[claude-optimizer]` context reminder arrived (from the optional hook below).
- Roughly 40+ exchanges, or several big tool outputs (long logs, large files, screenshots) in context.
- The topic changed and the old one is done or parked.
- You notice yourself re-reading files you already read, or you are unsure about something decided earlier.
- The user repeats a correction or says "we already talked about this".

When a signal fires: finish the current step first (never interrupt mid-edit), then tell the user in one line
and offer the handoff. Ask, don't force. If they decline, don't ask again until the next signal.

## 3. Writing the handoff (keeping the thread)

Write `HANDOFF.md` in the project root (or `.claude/handoff/HANDOFF-<yyyy-mm-dd>-<slug>.md` if one already
exists for another thread). Build it from evidence, not memory: check `git status` / `git diff --stat`, the
files you edited, and the last command results. Keep it under ~60 lines.

```markdown
# Handoff — <short title> (<date>)

## Goal
<what we are trying to achieve, 1-3 lines, in the user's words>

## Current state
<what works now, what is half done; branch name; last verified result>

## Decisions (and why)
- <decision> — <reason>; rejected: <alternative> because <reason>

## Files touched
- path/to/file — <what changed>

## How to verify
<exact command(s) and expected result>

## Next steps (in order)
1. <next concrete action>

## Open questions / waiting on the user
- <question>

## Gotchas — don't redo
- <dead ends already tried, traps, env quirks>
```

Then:
- Move durable facts (preferences, project conventions) to memory or CLAUDE.md — not into the handoff.
- Show the user the file path and the exact line to start the next session with:
  `Continue from HANDOFF.md` (or the dated file name).
- Tell them they can now start a new session.

## 4. Resuming in a new session

When the user says "continue from HANDOFF..." (or a HANDOFF file is mentioned):

1. Read the handoff file — and only the files it points to that the next step needs.
2. Verify it still matches reality (`git status`, branch, quick run of the verify command if cheap). Report any drift.
3. Restate in 3 lines: goal, current state, next step. Ask only the open questions that block the next step.
4. Continue the work. When the thread is finished, delete or archive the handoff so stale ones don't mislead.

## 5. Optional: automatic reminders (Claude Code)

`scripts/context_guard.py` is a `UserPromptSubmit` hook. On each user message it reads the size of the
current context from the session transcript and, the first time a threshold is crossed (default 120k,
250k and 400k tokens), shows the user a short warning and tells the agent to suggest a handoff at the next
natural pause. It never blocks a prompt and stays silent below the thresholds.

Install: copy this folder to `~/.claude/skills/claude-optimizer/`, then add to `~/.claude/settings.json`
(use `python3` instead of `python` on macOS/Linux):

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python ~/.claude/skills/claude-optimizer/scripts/context_guard.py --lang en"
          }
        ]
      }
    ]
  }
}
```

Options: `--lang en|pt` for the message language, `--thresholds 100000,200000,350000` to change the
limits. Thresholds re-arm after the context shrinks (for example after compaction).
