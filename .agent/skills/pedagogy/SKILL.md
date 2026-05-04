---
name: pedagogy
description: Use when designing lesson plans, pedagogical learning sequences, or exporting teaching materials to PPTX, LMS, and H5P formats.
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
