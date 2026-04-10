---

name: cm-document-publishing
description: "CORE — LITE — Pipeline toàn vẹn để tạo tài liệu chuẩn B2B từ 3 giai đoạn: tạo nội dung, trình bày/định dạng, và xuất bản."
version: 2.0.0
---

# cm-document-publishing — STEAM Document Publishing (LITE)

> **Goal:** Automate the production of professional STEAM documents (Lesson plans, Slides, Digibooks) through a quality-controlled skill chain pipeline.

## When to Activate

- Publishing a lesson plan or 5E unit plan as slides or Word documents
- Converting educational content from Markdown/HTML to PPTX or DOCX
- Producing B2B-standard training materials for teachers
- Running the full pipeline from content creation through to final export

## Instructions

### 3-Step Pipeline Flow

| Step | Action | Delegate Skills |
|------|--------|-----------------|
| **1. CONTENT** | Draft 5E/SOP/Worksheet content. | `module-architect`, `cm-dockit`, `steam-content-factory`. |
| **2. RENDER** | HTML Preview (review layout before export). | `cm-vn-typography`, `k12-math-renderer`. |
| **3. PUBLISH** | Convert HTML → Final output file. | `cm-pptx-converter` (PPTX/DOCX). |

### Design & Styling (B2B Standards)

- **Palette:** Navy (`#134A85`) Header, Off-white background.
- **Font:** Montserrat (Heading), Arial (Body).
- **Presentation:** 16:9 ratio. **Do NOT use `overflow-y: auto`**.
- **Media:** `max-height: 55vh` for slide images.

### Pipeline Gate Rules

- **Step 3 only runs AFTER Step 2 is user-approved.** Never skip the layout review.
- Vietnamese diacritics must be verified at Step 2 using `cm-vn-typography`.
- CSS rules in the HTML template must match what `cm-pptx-converter` expects.

## Quality Gate (Red Flags)

- ❌ Slide exceeds 5 bullet points (must split into separate slides).
- ❌ Missing Vietnamese diacritics or broken font (use `cm-vn-typography`).
- ❌ Render does not match PPTX Converter output (check CSS rules).
- ❌ Running Step 3 before Step 2 has been user-approved.

## Example Triggers

- "Create B2B documents for the Grade 10 AI lesson."
- "Make a teacher training slide deck from this 5E lesson plan."
- "Export the Robotics module lesson plans as Word documents."
- "Run the full document publishing pipeline on this content."
