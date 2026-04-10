---


name: cm-ui-preview
description: "CORE — \"LITE — Tạo prototype UI nhanh bằng Google Stitch/Pencil trước khi phát triển.\""
version: 2.0.0
---

# cm-ui-preview — UI Design Prototyping (LITE)

> **Goal:** "See it before you build it." Transform vague requirements into a detailed technical blueprint for Google Stitch or Pencil.dev to produce professional, brand-consistent prototypes.

## When to Activate

- Starting any new UI feature or screen design
- Reviewing a UI concept before writing any code
- Iterating on visual feedback from the user
- Before calling `cm-brainstorm-idea` concludes with a UI-heavy recommendation

## Instructions

### The 5-Step Design Pipeline

1. **P1: Preflight:** Clarify objective (New vs. Modify) and check MCP connection (Stitch/Pencil).
2. **P2: Extraction:** Find existing `DESIGN.md` or design tokens to use as "Source of Truth."
3. **P3: Enhancement:** Upgrade the raw prompt into a detailed Blueprint (Vibe, Palette, Typography, Layout).
4. **P4: Execution:** Call `create_project` and `generate_screen_from_text`. Present link to user.
5. **P5: Finalization:** User chooses: **Confirm** (AI writes code) / **Revise** (Iterate) / **Skip**.

### Prompt Enhancement Structure

Never send short prompts like "Make a login page." Always structure:
- **Project Vibe:** Context, target audience, style (Modern, minimal, education-focused).
- **Design System:** Platform (Web/Mobile), color palette (Hex), typography, border-radius.
- **Page Structure:** Break down into zones: Nav, Hero, Main Area, Action Bar (CTA).

### Tool Interaction

- **Google Stitch:** Fast — generates prototype from text. Use `generate_screen_from_text`.
- **Pencil.dev:** Pixel-level control — syncs design system. Use `batch_design`.
- **Continuity:** Save design state to `.stitch/next-prompt.md` for next-session sync.

## Quality Gate (Red Flags)

- ❌ Writing React/Vue code immediately without first confirming the prototype.
- ❌ Sending vague prompts to Stitch leading to unsatisfactory results.
- ❌ Assuming success when MCP is erroring (never "hallucinate" a link).
- ❌ Forgetting to apply basic UX laws (Miller's Law, Fitts's Law) to the design blueprint.

## Example Triggers

- "Design a dashboard page for a financial management app."
- "Use Stitch to create a prototype for this landing page."
- "Improve the current interface — make it more professional."
- "Show me a preview before I start building this new screen."
