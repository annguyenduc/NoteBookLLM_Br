---

name: steam-continuity
description: "ToT — Bộ nhớ xuyên phiên làm việc (Long-term Memory) cho chuyên viên thiết kế STEAM K-12."
version: 2.0.0
---

# steam-continuity — STEAM Long-Term Memory (LITE)

> **Goal:** Maintain context, pedagogical preferences, and experiential lessons across multiple work sessions. Enables the agent to self-improve in accuracy and personalization over time.

## When to Activate

- Starting a new session on a continuing STEAM design project
- Recording a significant lesson learned or design preference
- When a user corrects the agent ("That's wrong" or "Not like that")
- When ending a session — must persist context for the next session

## Instructions

### 3-Layer Memory Model

| Layer | File Path | Purpose |
|-------|-----------|---------|
| **Working** | `.memory/last-session.md` | Summary of the most recent session, in-progress tasks. |
| **Episodic** | `.memory/learnings.md` | Recorded corrections (Correction) and preferences (Preference). |
| **Semantic** | `.memory/profile.md` | Pedagogical profile: School, Grade level, Subject, Style (5E/PBL). |

### Session Lifecycle

- **START:** Read all 3 files above → Summarize "Recall from last session" → Alert "Errors to avoid."
- **PROCESS:** Automatically record to `learnings.md` when the user corrects or praises.
- **END:** Summarize the current session → Save `last-session.md` → Update `profile.md`.

### Auto-Update Triggers

| Signal | Action |
|--------|--------|
| User says "Wrong," "Not like that," "Fix it..." | Record correction in `learnings.md`. |
| User says "Good," "Use this style next time," "Correct!" | Record preference in `learnings.md`. |
| User requests something the agent lacks a good skill for | Log as skill gap for `skill-forge`. |

## Quality Gate (Red Flags)

- ❌ Asking for information already in `.memory/profile.md`.
- ❌ Repeating a mistake already recorded in `learnings.md`.
- ❌ Starting a new session as if it's a fresh start (must summarize previous context).
- ❌ Forgetting to update `last-session.md` before ending the session.

## Example Triggers

- "Remember this lesson plan format for future lessons."
- "Where did we get to in this project last time?"
- "What lessons did you draw from our previous session?"
- "Initialize session context from memory."
