---
name: pedagogy
description: "Use when designing lesson plans or learning sequences from Wiki Atoms, converting comparison content to PPTX slides, or packaging content for LMS/H5P export. Requires a Trainer Profile before starting. Do NOT use for raw data ingest or routine Wiki maintenance."
---

# Pedagogy Protocol

Trợ lý thiết kế sư phạm và xuất bản học liệu chuyên sâu cho NoteBookLLM_Br. Đảm bảo tính kế thừa từ Raw Source và tuân thủ các khung năng lực K-12.

## When to Use
- Thiết kế chuỗi hoạt động học tập (Learning Sequence) từ các Wiki Atom.
- Chuyển đổi nội dung so sánh (Comparison) sang bài giảng trình chiếu (PPTX).
- Đóng gói học liệu sang định dạng chuẩn LMS (Scorm/H5P).
- **Trường hợp KHÔNG dùng**: Bảo trì Wiki thông thường hoặc nạp dữ liệu thô.

## Core Pattern: Extraction & Design

### Rule 16: Performance Tracking
Mọi tệp tin trung gian trong `1-projects/[Project]/` PHẢI dùng cấu trúc từ:
`.agent/skills/pedagogy/resources/PROCESS_TEMPLATE.md`.
Bắt buộc có **Bảng thống kê hiệu suất Khai thác (Mining Stats)** ở đầu file.

### Rule 11: Sequential Pipeline
1. **@profiler**: Xác định đối tượng người học (Trainer Profile).
2. **@designer**: Xây dựng cấu trúc sư phạm (Learning Design).
3. **@engineer**: Thực thi viết nội dung/code bài giảng.

## Quick Reference: Export & Conversion

| Mục tiêu | Lệnh thực thi | Ghi chú |
| :--- | :--- | :--- |
| **Xuất PPTX** | `python .agent/skills/pedagogy/scripts/export_comparison_to_pptx.py --input [draft.md] --output [result.pptx]` | Hỗ trợ markdown cấu trúc # và ## |
| **Slide K10** | `python .agent/skills/pedagogy/scripts/generate_standard_slides_k10.py` | Template chuẩn khối 10 |
| **LMS/H5P** | `python .agent/skills/pedagogy/scripts/convert_h5p.py` | Xuất file JSON/H5P cho LMS |
| **IoT/KHMT** | `python .agent/skills/pedagogy/scripts/convert_all_iot.py` | Chuyển đổi chuyên biệt STEAM |

## Common Mistakes
- **Thiếu Trainer Profile**: Bắt đầu thiết kế mà chưa biết dạy cho ai.
- **Hardcode nội dung**: Không sử dụng `presentation_draft.md` làm trung gian trước khi xuất PPTX.
- **Sai tỉ lệ slide**: Script mặc định dùng 16:9, không nên thay đổi nếu không có yêu cầu đặc biệt.
- **Quên ghi log**: Không append thay đổi vào `3-resources/wiki/log.md`.
description: Use when designing learning sequences from wiki atoms, exporting comparison content to slides, or packaging training materials for LMS or H5P, but only after the required trainer profile exists.
---

# Pedagogy

## Overview
Use this skill for instructional-design outputs, not for routine wiki maintenance. The folder contains export and conversion utilities for slides and LMS packaging, plus a process template for structured intermediate work.

## Guardrails
- Start only when the required `Trainer_Profile_[id].md` exists.
- Respect the pipeline: trainer profile first, learning design second, content production third.
- Use `.agent/skills/pedagogy/resources/PROCESS_TEMPLATE.md` for substantial intermediate files.
- Several scripts in this folder still assume legacy `d:/NoteBookLLM_Br/brain/...` paths. Inspect the target script before running it in the current vault layout.

## Workflow
1. Confirm the pedagogical prerequisites exist.
2. Create or update the working draft using the process template.
3. Choose the export path that matches the task:
   comparison to PPTX, HTML-to-slide generation, LMS conversion, or H5P relabeling.
4. Run the relevant script and verify the produced artifact before publishing it onward.

## Quick Reference
- Comparison to PPTX:
  `python .agent/skills/pedagogy/scripts/export_comparison_to_pptx.py --input <draft.md> --output <deck.pptx>`
- Standard slide generation:
  `python .agent/skills/pedagogy/scripts/generate_standard_slides_k10.py`
- H5P relabeling:
  `python .agent/skills/pedagogy/scripts/convert_h5p.py`
- LMS conversion utilities:
  `final_lms_conversion.py`, `convert_all_iot.py`, `convert_all_khmt.py`

## Common Mistakes
- Running a legacy script without checking its hard-coded paths.
- Starting design work before the trainer profile exists.
- Treating export scripts as if they also validate pedagogy quality.
