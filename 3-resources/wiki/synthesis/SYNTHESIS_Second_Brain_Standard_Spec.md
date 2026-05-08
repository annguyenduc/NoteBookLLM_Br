---
file_id: SYNTHESIS_Second_Brain_Standard_Spec
title: "SYNTHESIS: Second Brain Standard Specification (Karpathy x Nashsu) [SUPERSEDED]"
type: synthesis
status: DRAFT
tags: 
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-02
last_updated: 2026-05-08
---

# Bản đặc tả Second Brain (Standard Specification)

Bản đặc tả này kết hợp tính **"Low Friction"** (Karpathy) với tính **"High Fidelity Graph"** (Nashsu) để tạo ra một bộ não thứ hai tối ưu cho cả Con người và AI.

## 1. Hệ thống Skill chuẩn (Core Skills)
Một Second Brain hoàn chỉnh phải có 7 "bộ kỹ năng" đóng gói (Module hóa):

1.  **Ingest (Capture)**: Chuyển đổi dữ liệu thô (`raw/`) thành các nguyên tử tri thức (Atoms).
2.  **Absorb (Synthesis)**: Vòng lặp rewrite để tích hợp tri thức mới vào các bài viết cũ, đảm bảo tính mạch lạc (Narrative Coherence).
3.  **Query (Retrieval)**: Truy vấn dựa trên đồ thị (Graph Traversal) để trả lời câu hỏi phức tạp.
4.  **Cleanup (Audit)**: Làm sạch dữ liệu, sửa link hỏng và thực hiện "Steve Jobs Test" (Wikipedia-style quality).
5.  **Breakdown (Mining)**: Chủ động tìm kiếm "Knowledge Gaps" bằng Concrete Noun Test.
6.  **Status (Monitoring)**: Theo dõi mật độ liên kết và sức khỏe hệ thống tri thức.
7.  **Rebuild (Sync)**: Đồng bộ hóa Index và Backlinks để duy trì tính toàn vẹn của đồ thị.

## 2. Cấu trúc Schema chuẩn (Standard Schema)

### A. Cấu trúc thư mục (PARA 2.0)
- `00_Inbox/`: Ghi chép thô, nhanh (Idea File System).
- `1-projects/`: Dự án đang thực hiện.
- `2-areas/`: Mảng quản trị lâu dài.
- `3-resources/`:
    - `raw/`: Nguồn dữ liệu bất biến (Immutable).
    - `wiki/`: Các node tri thức nguyên tử (Concepts, Entities, Sources, Synthesis).
- `4-archive/`: Lưu trữ bài học kinh nghiệm.

### B. Cấu trúc Metadata (YAML Frontmatter)
Mọi file trong `wiki/` phải chứa:
```yaml
file_id: SYNTHESIS_SB_STANDARD_SPEC_TEMPLATE
title: [Tên_trang]
category: "CONCEPT | ENTITY | SOURCE | SYNTHESIS"
tags: ["Tag1", "Tag2"]
source: "[[index]] — [Section/Page]"
relationships:
  - type: "is_a | relates_to | governs"
    target: "[[index]]"
status: "VERIFIED | DRAFT | DEPRECATED"

## 3. Nguyên tắc vận hành (Core Principles)
1.  **Atomic Fidelity**: Một trang, một khái niệm. Không trộn lẫn nhiều chủ đề.
2.  **Source Tracing**: Mọi thông tin phải truy vết được về file gốc trong `raw/`.
3.  **Narrative Over Storage**: Ưu tiên việc viết lại để tạo ra "Mạch truyện" hơn là chỉ lưu trữ các đoạn note rời rạc.
4.  **Async Review**: Luôn có cơ chế gắn cờ (Flagging) các điểm mâu thuẫn để xử lý sau.

## 4. Phản tư sư phạm (4F)
- **Facts**: Karpathy cung cấp "vỏ" (Skills/Workflow), Nashsu cung cấp "lõi" (Graph/Logic).
- **Feelings**: Cảm thấy hệ thống vô cùng vững chãi khi có sự kết hợp này.
- **Findings**: Điểm yếu lớn nhất của các Second Brain thông thường là thiếu **Type Relationships** (Liên kết có định dạng).
- **Futures**: Áp dụng Schema này để chuẩn hóa 33+ META Atoms hiện có.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
