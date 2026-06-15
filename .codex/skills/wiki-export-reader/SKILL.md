---
name: wiki-export-reader
description: "Xuất bản tài liệu học tập của một nguồn (source_id) thành HTML Reader tự chứa và sách EPUB cho Apple Books/Safari di động theo đúng thứ tự Gói học nhanh (Learning Pack)."
---

# wiki-export-reader

## Purpose

Export knowledge atoms of a specific source (e.g., `ARCH_TIS`) into high-fidelity, offline-ready HTML Reader and mobile-optimized EPUB book formats for Apple Books/Safari. The compiled books are sequenced exactly according to the curated pedagogical flow defined in the source's Gói học nhanh (Learning Pack).

## When to use

Use this skill when the user asks to:
- Export or compile a source's atoms into an EPUB book (`.epub`) or offline HTML Reader (`.html`).
- Read study materials on Apple Books (iPad/iPhone) or offline on Safari.
- Sync, publish, or compile a Learning Pack into reading formats.
- Update the compiled book outputs after modifying atoms or the Learning Pack checklist.

Do NOT use this skill for:
- Creating or editing raw atoms (use `wiki-ingest` or edit manually).
- Organizing the initial learning packs (use `wiki-learning-pack`).
- Creating presentation slides or lesson plans (use `pedagogy`).

## Prerequisites

1. **Pandoc CLI:** Ensure Pandoc is installed. A portable binary can be placed in `scripts/learning/bin/` or resolved from system PATH.
2. **Manifest File:** A YAML manifest file must exist at `exports/reader/[source_id].reader.yml`.
3. **Learning Pack:** A Gói học nhanh Markdown file must exist under `workspaces/learning/dashboard/packs/` (e.g., `LEARNING_PACK_SOURCE_[source_id]_*.md`) to define the chapter sequence.
4. **Stylesheets & Templates:** Ensure `epub_style.css` and `learning_pack_reader.html` exist in `scripts/learning/templates/`.

## Input

Accepts:
- `source_id` (e.g., `ARCH_TIS`).
- Manifest file path (optional, defaults to `exports/reader/[source_id].reader.yml`).

## Output

Generates:
- **HTML Reader:** An offline, self-contained single-page HTML file under `workspaces/learning/dashboard/packs/html/` with CSS and JS embedded.
- **EPUB Book:** A mobile-optimized EPUB book under `workspaces/learning/dashboard/packs/epub/` with simplified Table of Contents (TOC depth 1).

## Workflow

1. **Verify Manifest:** Ensure `exports/reader/[source_id].reader.yml` contains:
   - `source_id`, `title`, `author`, `language`.
   - `include` patterns pointing to the raw markdown atoms.
   - `outputs` paths for HTML and EPUB.
   - `epub` settings (e.g., `toc: true`, `toc_depth: 1`, and `css` template path).
2. **Check Learning Pack:** Locate `workspaces/learning/dashboard/packs/` for a file matching `*[source_id]*.md` and verify it contains `[[ATOM_ID]]` references representing the desired chapter sequence.
3. **Compile Book:** Execute the export script:
   ```powershell
   python scripts/learning/export_epub.py --manifest exports/reader/[source_id].reader.yml
   ```
4. **Update Dashboard:** Ensure `workspaces/learning/dashboard/LEARNING_DASHBOARD.md` is updated to include links to the newly generated `[🌐 HTML Reader]` and `[📚 Sách EPUB]`.
5. **Verify Outputs:** Validate that:
   - Files are successfully created at the target paths.
   - File sizes are non-zero.
   - Chapter order matches the Learning Pack.
   - TOC only includes atom names and no H2 sub-sections.

## Guardrails

- **Surgical Execution:** Never modify files outside the active worktree (worktree directory: `D:\_agent_worktrees\`).
- **No Hardcoded Absolute Paths:** Use paths relative to repository root (`repo_root`).
- **Clean Titles:** Strip English sub-headings or parentheses from titles (e.g., `(Leverage Points)` becomes `Leverage Points`).
- **Single-File HTML:** Ensure CSS and JS are fully embedded into the generated HTML Reader for perfect offline reading.
