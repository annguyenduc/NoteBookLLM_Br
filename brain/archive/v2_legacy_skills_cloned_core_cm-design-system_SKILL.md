---


name: cm-design-system
description: "CORE — Trích xuất, quản lý và tái sử dụng design tokens (màu sắc, font, spacing) để tạo giao diện nhất quán."
version: 2.0.0
---

# cm-design-system — Design System Intelligence (LITE)

> **Goal:** Establish a consistent design system by extracting (Harvester mode) from an existing website, or scaffolding from premium Kit presets (Shadcn, Halo, Lunaris). Output is a standardized `DESIGN.md` file.

## When to Activate

- Starting a new project and need a consistent visual language
- Extracting a design system from an existing site or brand
- Syncing design tokens with Google Stitch or Pencil.dev
- Ensuring UI components follow the established token system

## Instructions

### Operation Modes

| Mode | Action | Output |
|------|--------|--------|
| **Harvester** | Analyze URL/Image → Extract colors, fonts, spacing. | `DESIGN.md` (Extracted). |
| **Kits (Default)** | Use preset kits: Shadcn, Halo, Nitro, Lunaris. | `DESIGN.md` (Scaffolded). |
| **Stitch Path** | Use JSON block to sync with Google Stitch AI generator. | `STITCH_TOKENS` block. |
| **Pencil Path** | Use Pencil MCP to create and manage `.pen` files directly. | `.pen` design files. |

### Token Standards (DESIGN.md)

Every design system must include:
- **Semantic Colors:** Primary, Secondary, Success, Warning, Danger.
- **Neutral Ramps:** Gray scale from 50-900 (required).
- **Typography Scales:** Font-size, weight, line-height.
- **Spacing & Icons:** Grid system, border-radius, shadow.
- **Wrapper:** Must wrap JSON in `<!-- STITCH_TOKENS_START -->`.

### Pencil.dev Workflow

1. `open_document()` → Initialize `.pen` file.
2. `get_style_guide()` → Get suggested color palette and typography.
3. `set_variables()` → Apply design tokens to system variables.
4. `batch_design()` → Create reusable components (Buttons, Cards, etc.).

## Quality Gate (Red Flags)

- ❌ Writing UI code (React/Vue) directly within this skill (must delegate to `cm-ui-preview`).
- ❌ Skipping the `STITCH_TOKENS` wrapper — Google Stitch cannot parse without it.
- ❌ Reading `.pen` files with `view_file` (must use `mcp_pencil_batch_get`).
- ❌ Missing interactive state variables (Hover, Active, Disabled) in the design.

## Example Triggers

- "Extract the design system from apple.com for me."
- "Create a premium Dark Mode design system using the Halo Kit."
- "Set up Design Tokens in Pencil.dev for a SaaS Dashboard."
- "Harvest the brand colors and fonts from this competitor site."
