---
file_id: CONCEPT_META_WIKI_BREAKDOWN_MINING
title: "Wiki Breakdown & Mining (Khai thác và Chia nhỏ Wiki)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_WIKI_GEN_CLONE]]"
---

## ## For future Claude
Trang này mô tả quá trình chủ động tìm kiếm các "lỗ hổng tri thức" thông qua việc khai thác các danh từ cụ thể và các chủ đề tiềm năng từ nội dung hiện có. Breakdown & Mining là cơ chế giúp Wiki "tự lớn" (self-expanding) bằng cách chia tách tri thức cũ để tạo ra các node tri thức mới sâu sắc hơn.

## ## Key Claims / Summary
1.  **Concrete Noun Test**: Quét bài viết để tìm các thực thể chưa có trang định nghĩa riêng.
2.  **Mining Bloated Articles**: Tách các bài viết quá dài thành các tiểu chủ đề hạt nhân.
3.  **Knowledge Expansion**: Sự phát triển tri thức đến từ việc "chia nhỏ" hơn là "viết thêm" một cách rời rạc.

## 1. Kỹ thuật Mining
- **Backlink Ranking**: Các thuật ngữ được nhắc đến nhiều nhưng chưa được định nghĩa là ứng viên hàng đầu.
- **Reclassification**: Đánh giá lại vị trí các bài viết để đảm bảo tính logic của hệ thống.
- **Entity Extraction**: Tự động nhận diện Người, Công cụ, Công ty để tạo các trang Entity.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Hệ thống quét qua 10 bài viết về Cloud, thấy nhắc đến "Vercel" 5 lần nhưng chưa có trang định nghĩa. Lệnh `/wiki breakdown` sẽ đề xuất tạo ngay trang `ENTITY_TOOL_Vercel` để làm giàu kho tri thức. (Nguồn: [[SOURCE_META_WIKI_GEN_CLONE]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một người thợ làm bánh. Khi chiếc bánh (Tri thức tổng quát) đã chín và đủ lớn, ông cắt nó thành những miếng nhỏ (Atoms) để mọi người dễ thưởng thức và hiểu rõ hương vị của từng thành phần bên trong.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Section: Command: /wiki breakdown.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
