---


name: cm-brainstorm-idea
description: "CORE — Khám phá vấn đề bằng Design Thinking + 9 Windows (TRIZ) + Double Diamond. Đề xuất 2–3 hướng giải quyết có căn cứ."
version: 2.0.0
---

# cm-brainstorm-idea — Strategic Brainstorming (LITE)

> **Goal:** Deeply understand the nature of a problem before planning. Use systems thinking (TRIZ) and design thinking to produce 2-3 substantially differentiated solution options — and avoid jumping into code before the problem is clear.

## When to Activate

- Task is vague, ambiguous, or has multiple possible interpretations
- Evaluating architectural or product decisions before committing
- User asks "how should we approach this?" or "what are our options?"
- Before calling `cm-planning` on a complex or novel problem

## Instructions

### The 5-Phase Strategic Workflow

| Phase | Action | Goal |
|-------|--------|------|
| **1. Discover** | Codebase scan + user interview. | Understand current state & pain points. |
| **2. Define** | TRIZ 9 Windows Analysis. | Identify the "Real Problem" (not the surface request). |
| **3. Develop** | Ideation (Diverge). | Propose 2-3 options that differ fundamentally in approach. |
| **4. Evaluate** | Scoring Matrix (Converge). | Score and recommend the best option. |
| **5. Handoff** | Package context for `cm-planning`. | Clean hand-off with full problem + recommendation context. |

### TRIZ 9 Windows Matrix

Analyze the problem across 3 system levels and 3 time horizons:
- **System levels:** Super-system (Ecosystem) / System (Product) / Sub-system (Components).
- **Time:** Past / Present / Future.

### Multi-Dimensional Scoring

Score each option across:
- **Tech (25%):** Feasibility, maintainability, scalability.
- **Product (30%):** User value, product-market fit.
- **Design (20%):** UX/UI quality, polish, delight.
- **Business (25%):** ROI, speed to ship, strategic alignment.

### UI Preview Integration (Phase 4.5)

If the option involves UI changes, propose a preview before planning:
- **Tool:** Auto-select Google Stitch (fast) or Pencil (detailed control).
- **Action:** Delegate to `cm-ui-preview` to create concept screens.

## Quality Gate (Red Flags)

- ❌ Presenting only **ONE** option (no choice = weak analysis).
- ❌ Proposing 4+ options (causes decision paralysis).
- ❌ Jumping straight to Planning without completing the Define phase.
- ❌ Skipping effort estimation for each option.

## Example Triggers

- "How should we improve this feature?"
- "Brainstorm the next development directions for this project."
- "Run 9 Windows analysis on this page load performance issue."
- "We have multiple approaches — help me evaluate which is best."
