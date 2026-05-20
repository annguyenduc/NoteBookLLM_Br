# SPEC — Learning Pack Reader View

Source context: `NoteBookLLM_Br` Learning UX layer  
Scope owner: `@librarian` for content contract, `@engineer` for renderer implementation  
Status: `DRAFT`  
Phase target: `Minimal static reader`

## 1. Problem Statement

`wiki-learning-pack` can now organize existing Wiki atoms into a Learning Pack, but Markdown alone is not ideal for focused reading.

The user needs a nicer reading surface without turning the workflow into a dashboard, web app, or synthesis system.

Current risk if no reader contract exists:
- agents may place HTML files in inconsistent folders
- UI may drift away from the Markdown source of truth
- future implementation may accidentally write into `synthesis/` or atom folders
- Learning Pack artifacts may become hard to scan when Markdown, HTML, CSS, and JS are mixed flat in one folder

## 2. Objective

Add a static HTML reader view for Learning Packs while keeping Markdown as the canonical source.

The reader must:
- render one Learning Pack Markdown file into one readable HTML file
- preserve source trace visibility
- provide a clean reading layout with table of contents and section styling
- keep all UI assets under a predictable folder
- avoid any database, rebuild, ingest, atom creation, or synthesis side effect

## 3. Canonical Paths

### 3.1 Markdown Source

Markdown Learning Pack source stays canonical:

```text
3-resources/wiki/learning_packs/LEARNING_PACK_[SOURCE_ID]_[Name].md
```

Example:

```text
3-resources/wiki/learning_packs/LEARNING_PACK_ARCH_TIS_Fast_Start.md
```

### 3.2 HTML Reader Output

HTML reader output goes under `reader/`:

```text
3-resources/wiki/learning_packs/reader/LEARNING_PACK_[SOURCE_ID]_[Name].html
```

Example:

```text
3-resources/wiki/learning_packs/reader/LEARNING_PACK_ARCH_TIS_Fast_Start.html
```

### 3.3 Shared Reader Assets

Shared CSS/JS assets go under:

```text
3-resources/wiki/learning_packs/reader/assets/
```

Initial asset targets:

```text
3-resources/wiki/learning_packs/reader/assets/learning-pack.css
3-resources/wiki/learning_packs/reader/assets/learning-pack.js
```

### 3.4 Renderer Script

Renderer implementation should live outside `3-resources/`:

```text
scripts/learning/render_learning_pack.py
```

If `scripts/learning/` does not exist, create it during implementation only after AN GO.

### 3.5 Optional Template

If the renderer needs a reusable HTML template, place it at:

```text
scripts/learning/templates/learning_pack_reader.html
```

Do not place templates inside `3-resources/wiki/learning_packs/`.

## 4. Target Layout

```text
3-resources/wiki/learning_packs/
├── LEARNING_PACK_ARCH_TIS_Fast_Start.md
└── reader/
    ├── LEARNING_PACK_ARCH_TIS_Fast_Start.html
    └── assets/
        ├── learning-pack.css
        └── learning-pack.js
```

Implementation files:

```text
scripts/learning/
├── render_learning_pack.py
└── templates/
    └── learning_pack_reader.html
```

## 5. Scope

Phase 1 covers:
- one static HTML reader per Learning Pack Markdown file
- local file viewing in browser
- table of contents from Markdown headings
- readable typography and spacing
- section treatments for:
  - `Big Picture`
  - `Key Concepts`
  - `Concept Map`
  - `Must-Know Atoms`
  - `Failure Modes`
  - `Practice Task`
  - `Review Questions`
  - `Source Trace`
  - `Missing Context`
- collapsible `Source Trace`
- visual warning style for `Missing Context`
- responsive mobile layout

## 6. Non-Goals

Phase 1 does not:
- create a web app or server
- create dashboards
- write to `synthesis/`
- create, edit, or promote atoms
- run ingest, rebuild, scrape, OCR, or PDF conversion
- modify `wiki_brain.db`
- make NotebookLM output canonical
- replace the Markdown Learning Pack source
- add external dependencies unless AN explicitly approves them

## 7. Reader Behavior

Input:

```text
scripts/learning/render_learning_pack.py \
  --input 3-resources/wiki/learning_packs/LEARNING_PACK_ARCH_TIS_Fast_Start.md \
  --output 3-resources/wiki/learning_packs/reader/LEARNING_PACK_ARCH_TIS_Fast_Start.html
```

Expected behavior:
- read Markdown as UTF-8
- derive page title from first `#` heading or filename
- generate table of contents from headings
- render sections into semantic HTML
- link shared assets with relative paths
- preserve inline code, lists, tables, and links
- render source trace in a collapsible block
- render missing context with a visible warning style
- never mutate the Markdown source

## 8. UI Requirements

The reader should feel like a focused study document, not a marketing page.

Required layout:
- left or top table of contents depending on viewport
- main reading column with comfortable width
- section headers with stable hierarchy
- compact cards only for individual learning units, not nested page sections
- clear callout for `Practice Task`
- clear warning for `Missing Context`
- collapsible block for `Source Trace`

Visual constraints:
- no gradient/orb decoration
- no landing page hero
- no dark, low-contrast reading surface by default
- avoid one-note color palettes
- text must not overlap or overflow on mobile

## 9. Governance And Safety

Markdown is source of truth. HTML is presentation only.

Rules:
- Do not edit `3-resources/wiki/concepts/`, `entities/`, `sources/`, `comparisons/`, `queries/`, or `synthesis/`.
- Do not set `SYNTHESIZED`.
- Do not write directly into `3-resources/raw_*`.
- Do not create a Learning Pack artifact or reader output without explicit AN GO for the exact target path.
- Do not run database rebuild or promote operations for this feature.
- If implementation needs dependencies, stop and ask AN first.

## 10. Implementation Plan

1. Confirm target Learning Pack Markdown path.
2. Create `scripts/learning/render_learning_pack.py`.
3. Create `scripts/learning/templates/learning_pack_reader.html` only if needed.
4. Create shared assets:
   - `3-resources/wiki/learning_packs/reader/assets/learning-pack.css`
   - `3-resources/wiki/learning_packs/reader/assets/learning-pack.js`
5. Render one HTML file:
   - `3-resources/wiki/learning_packs/reader/LEARNING_PACK_ARCH_TIS_Fast_Start.html`
6. Validate:
   - UTF-8 read/write
   - HTML file exists
   - relative asset links resolve
   - table of contents links work
   - no source Markdown mutation
7. Open locally only if AN asks or approves browser/file launch.

## 11. Acceptance Criteria

- `LEARNING_PACK_ARCH_TIS_Fast_Start.md` remains the canonical source.
- HTML output exists only under `3-resources/wiki/learning_packs/reader/`.
- Shared reader assets exist only under `3-resources/wiki/learning_packs/reader/assets/`.
- Renderer code exists only under `scripts/learning/`.
- The generated HTML can be opened directly in a browser.
- The reader includes table of contents, section styling, collapsible source trace, and missing-context warning.
- No atom, ingest, rebuild, promote, raw, database, or synthesis changes occur.
- UTF-8 validation passes for Markdown input, HTML output, CSS/JS assets, and log updates.

## 12. First Execution Target

Use this as the first real target after AN approves implementation:

Markdown source:

```text
3-resources/wiki/learning_packs/LEARNING_PACK_ARCH_TIS_Fast_Start.md
```

HTML output:

```text
3-resources/wiki/learning_packs/reader/LEARNING_PACK_ARCH_TIS_Fast_Start.html
```

Assets:

```text
3-resources/wiki/learning_packs/reader/assets/learning-pack.css
3-resources/wiki/learning_packs/reader/assets/learning-pack.js
```

Renderer:

```text
scripts/learning/render_learning_pack.py
```

## 13. Agent Execution Note

Any future agent implementing this spec must start by reading this file and must not infer alternate paths.

If a requested path conflicts with this spec:
- stop
- report the conflicting path
- ask AN whether to update the spec or override for that run

