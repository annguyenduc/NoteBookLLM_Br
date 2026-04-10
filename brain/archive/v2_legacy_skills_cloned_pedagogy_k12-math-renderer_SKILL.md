---

name: k12-math-renderer
description: "K-12 — Chuyển đổi nội dung Markdown chứa LaTeX thành bản xem trước (HTML/Word) đẹp mắt."
version: 2.0.0
---

# k12-math-renderer — LaTeX Math Preview Renderer (LITE)

> **Goal:** Display mathematical formulas (LaTeX) as visual, textbook-quality output through MathJax rendering in HTML.

## When to Activate

- Rendering a LaTeX-containing Markdown file as a beautiful HTML preview
- Checking that a lesson plan's math formulas display correctly
- Generating a math preview before converting to PPTX or DOCX
- Any time LaTeX notation needs to be made human-readable

## Instructions

### Execution Workflow

1. **Extract:** Get the Markdown content containing LaTeX formulas.
2. **Save:** Write to `docs/exports/math_preview.md`.
3. **Transform:** Run the command:
   ```
   python scripts/transformer.py docs/exports/math_preview.md --html
   ```
4. **Deliver:** Send the resulting `.html` file link to the user.

### Quality Standards

| Standard | Requirement |
|----------|------------|
| **Rendering Engine** | MathJax (must be embedded in the HTML output). |
| **Styling** | Use the Kit's `style.css` for a premium look. |
| **Readability** | Formulas must not break or lose symbols in any modern browser. |

## Quality Gate (Red Flags)

- ❌ Missing `$` or `$$` delimiters surrounding LaTeX formulas.
- ❌ HTML file fails to load the MathJax library (network error or script path issue).
- ❌ File encoding is not UTF-8 — causes special character errors in rendered output.

## Example Triggers

- "Render the LaTeX in this analysis section."
- "Show me a math preview for this lesson."
- "Display this formula in a beautiful readable format."
- "Preview the equations in this unit plan before I convert to slides."
