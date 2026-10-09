#!/usr/bin/env python3
"""UserPromptSubmit hook: remind the user to break long sessions.

Reads the hook payload from stdin, finds the current context size in the session transcript
(input + cache read + cache write tokens of the latest main-thread response) and, the first time
each threshold is crossed, prints a user-visible warning plus context for the agent.
Never blocks the prompt; any error exits silently.
"""

import argparse
import json
import os
import sys
import tempfile

TAIL_BYTES = 4 * 1024 * 1024

MESSAGES = {
    "en": {
        "user": "claude-optimizer: this conversation is at ~{k}k tokens of context. "
                "At a good pause, consider a handoff and a fresh session.",
        "agent": "[claude-optimizer] Context is at ~{k}k tokens (threshold {t}k crossed). "
                 "Finish the current step, then in one line suggest breaking the session using the "
                 "claude-optimizer handoff procedure. Do not interrupt work in progress.",
    },
    "pt": {
        "user": "claude-optimizer: esta conversa está com ~{k} mil tokens de contexto. "
                "Numa pausa, considere fazer o handoff e abrir uma sessão nova.",
        "agent": "[claude-optimizer] Context is at ~{k}k tokens (threshold {t}k crossed). "
                 "Finish the current step, then in one line suggest breaking the session using the "
                 "claude-optimizer handoff procedure. Do not interrupt work in progress. "
                 "Reply to the user in Portuguese.",
    },
}


def context_tokens(transcript_path):
    size = os.path.getsize(transcript_path)
    with open(transcript_path, "rb") as f:
        f.seek(max(0, size - TAIL_BYTES))
        data = f.read()
    for raw in reversed(data.splitlines()):
        if b'"usage"' not in raw:
            continue
        try:
            entry = json.loads(raw)
        except ValueError:
            continue
        if entry.get("type") != "assistant" or entry.get("isSidechain"):
            continue
        usage = (entry.get("message") or {}).get("usage") or {}
        total = (usage.get("input_tokens", 0) + usage.get("cache_read_input_tokens", 0)
                 + usage.get("cache_creation_input_tokens", 0))
        if total:
            return total
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", default="en", choices=sorted(MESSAGES))
    parser.add_argument("--thresholds", default="120000,250000,400000")
    args = parser.parse_args()
    thresholds = sorted(int(t) for t in args.thresholds.split(",") if t.strip())

    payload = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    transcript = payload.get("transcript_path")
    session = payload.get("session_id") or "unknown"
    if not transcript or not os.path.exists(transcript):
        return

    tokens = context_tokens(transcript)
    if tokens is None:
        return

    state_path = os.path.join(tempfile.gettempdir(), f"claude-optimizer-{session}.json")
    try:
        with open(state_path, encoding="utf-8") as f:
            fired = set(json.load(f))
    except (OSError, ValueError):
        fired = set()

    # Context shrank (compaction, rewind): re-arm the thresholds above the current size.
    fired = {t for t in fired if t <= tokens}
    crossed = [t for t in thresholds if tokens >= t and t not in fired]

    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(sorted(fired | set(crossed)), f)

    if not crossed:
        return
    msg = MESSAGES[args.lang]
    k, t = round(tokens / 1000), round(max(crossed) / 1000)
    print(json.dumps({
        "systemMessage": msg["user"].format(k=k, t=t),
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": msg["agent"].format(k=k, t=t),
        },
    }))  # ASCII-escaped JSON: safe whatever the console encoding


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
