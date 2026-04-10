---

name: steam-dashboard
description: "ToT — Tạo dashboard theo dõi tiến độ đào tạo và trạng thái workflow đang hoạt động."
version: 2.0.0
---

# steam-dashboard — STEAM K-12 Interactive Dashboard (LITE)

> **Goal:** Provide a control center for lesson design specialists. Display a Kanban board, lesson statistics, session memory, and quick skill activation shortcuts.

## When to Activate

- Opening a session and need a visual overview of all pending work
- Tracking progress across multiple lesson plan designs in parallel
- Using quick-launch shortcuts to invoke a STEAM skill rapidly
- User types "dashboard" or "open dashboard"

## Instructions

### Interactive Features

| Feature | Description |
|---------|-------------|
| **Kanban Tracker** | 4 columns: Backlog, Draft, Review, Done. Double-click to advance status. |
| **Real-time Stats** | Auto-count total lessons, completion rate, tasks in progress. |
| **Quick Launch** | List of STEAM K-12 skills with one-click trigger buttons. |
| **Memory Log** | Quick-record important decisions directly on the dashboard. |
| **Persistence** | Stored via `localStorage` — no data loss on refresh or browser close. |

### Implementation Workflow

When user types "dashboard" or "open dashboard":
1. **Generate File:** Create `steam-dashboard.html` in the current working directory.
2. **Inject Content:** Insert self-contained HTML/CSS/JS (Lightweight) into the file.
3. **Notify User:** Report: "✅ Dashboard ready at `steam-dashboard.html`. Open it in your browser."

### Design Standards

- **Style:** Premium Dark Mode, modern Kanban interface.
- **No Dependencies:** No external libraries — runs 100% on Vanilla JS/CSS.
- **Self-contained:** All logic and storage fits inside a single HTML file.

## Quality Gate (Red Flags)

- ❌ Requiring the user to install a server or complex environment to run the dashboard.
- ❌ Storage data lost after closing the browser (must use `localStorage`).
- ❌ Interface too simple — insufficient "WOW factor" (must feel premium).
- ❌ Missing Quick Launch buttons — a dashboard without action shortcuts is just a viewer.

## Example Triggers

- "Open a lesson progress tracking dashboard."
- "Show me a STEAM project overview."
- "dashboard"
- "Generate the K-12 design dashboard."
