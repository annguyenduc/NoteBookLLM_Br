---


name: cm-safe-i18n
description: "CORE — Dịch và chuyển đổi nội dung sang nhiều ngôn ngữ an toàn, qua nhiều lô (batches), kiểm tra 8 cổng."
version: 2.0.0
---

# cm-safe-i18n — Safe i18n Translation (LITE)

> **Goal:** Execute language conversion for a system (i18n) with absolute safety, preventing UI crashes, logic errors, or source code format corruption.

## When to Activate

- Translating content files or UI strings to another language
- Auditing language files for key parity
- Extracting hardcoded strings into i18n keys
- Validating that i18n changes did not break runtime behavior

## Instructions

### The Iron Rules (MANDATORY)

- **Batch Limit:** Maximum **30 strings** per batch. Never exceed this.
- **No Autoplay:** Never auto-apply changes without passing all checks.
- **HTML Protection:** Only translate text content — NEVER touch HTML tags or attributes.
- **Key Parity:** All language files must have exactly the same number of keys.

### 8-Gate Audit Lifecycle

| Gate | Check | Command | Pass Criteria |
|------|-------|---------|---------------|
| **1-2** | Syntax (JS/All) | `node -c app.js` | No syntax errors. |
| **3** | Corruption | `grep` pattern check | 0 matches for broken strings. |
| **4** | Delimiters | Mismatched quotes | 0 matches (mixed delimiters). |
| **5** | HTML Integrity | Broken tag spacing | 0 matches (`< div`, `< /div`). |
| **6** | Shadowing | `t` variable check | 0 matches in map/filter. |
| **7** | JSON Valid | `JSON.parse` | Valid JSON structure. |
| **8** | Full Test | `npm run test:gate` | 0 failures. |

### Translation Sync Rules

- **Placeholders:** Preserve `{{param}}` absolutely — never translate content inside curly braces.
- **Tech Terms:** Do NOT translate technical abbreviations (KPI, PPH, CSV, API).
- **Parallel Sync:** Once the source file (e.g., `vi.json`) is verified, translate other language files in parallel.

## Quality Gate (Red Flags)

- ❌ Using regex to fix regex errors (must use a Lexical Scanner instead).
- ❌ Missing Key Parity check after translation completes.
- ❌ Placeholder modified or translated into the target language (causes runtime error).
- ❌ Skipping any of the 8 audit gates.

## Example Triggers

- "Translate the entire blog file to English and Thai."
- "Extract hardcoded strings in app.js into i18n keys."
- "Audit `vi.json` and `en.json` for key parity and corruption."
- "Run the 8-gate check on these language files."
