---
file_id: "ENTITY_[CATEGORY]_[Name]"
# CATEGORY must be one of: AI | EDU | STEAM | TOOL | VIZ | SYS | MGT | BIZ | MISC
# Use MISC only if no category fits — flag for human review.
title: "[Entity Name]"
type: "entity"
status: "DRAFT"
tags:
  - "category"
ai-first: true
confidence: 0.0
entity_type: "tool | language | person | org | framework"
kwsr_type: "knowledge"  # knowledge | workflow | skill | rule
ecosystem: "ecosystem_name (e.g., Python, Google AI)"
version: "v1.0.0"
affiliation: "organization_name"
relationships:
  - type: "part_of | instance_of | relates_to"
    target: "[[ENTITY_ID]]"
last_reconciled: "2026-05-08"
source_file: ""    # RAW_YYYY-MM-DD_filename.md that this Atom was created from
source_ref: ""     # [[SOURCE_CATEGORY_Name]] — link to the Source Atom
created: "2026-05-08"
last_updated: "2026-05-08"
---

## For future Claude (AI Preamble)
> [Tóm tắt 3-5 câu bằng Tiếng Việt về thực thể này: Nó là gì, thuộc hệ sinh thái nào và tại sao nó lại quan trọng đối với Agent.]

# [Title]

## 1. Tổng quan
[Mô tả vai trò và chức năng chính của thực thể này.]

## 2. Khả năng & Đặc tính
[Liệt kê các tính năng cốt lõi (nếu là Tool) hoặc thành tựu/chuyên môn (nếu là Person).]

## 3. Ví dụ ứng dụng (R18: Practical Use)
> **Bối cảnh**: [Mô tả tình huống sử dụng thực tế]
> **Thực thi**: [Cách thực thể này giải quyết vấn đề]

## 4. Phản tư (4F)
- **Facts**: [Dữ liệu khách quan về thực thể]
- **Feelings**: [Đánh giá về tính hữu dụng hoặc độ phức tạp]
- **Findings**: [Bài học rút ra khi làm việc với thực thể này]
- **Future**: [Kế hoạch tích hợp thực thể này vào workflow tiếp theo]

---
*Phiên bản Template V3.0 (Language Aligned).*
