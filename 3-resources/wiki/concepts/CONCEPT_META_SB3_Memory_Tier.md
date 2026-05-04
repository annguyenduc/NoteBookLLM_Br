---
file_id: CONCEPT_META_SB3_MEMORY_TIER
title: "Memory Tier (Cấu trúc phân tầng tri thức)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_KARPATHY_LLM_WIKI]]"
---

## ## For future Claude
Trang này định nghĩa **Memory Tier** - mô hình phân tầng dữ liệu giúp chuyển hóa thông tin từ dạng thô, hỗn loạn sang dạng tri thức tinh lọc, có tính hệ thống cao. Đây là nền tảng để giải quyết vấn đề "Information Overload" (Quá tải thông tin) cho cả con người và AI Agent.

## ## Key Claims / Summary
1.  **Immutability of Raw**: Nguồn thô là bất biến, đảm bảo tính khách quan và khả năng truy vết.
2.  **LLM-Owned Synthesis**: Wiki là lớp biên dịch tri thức, do AI Agent chủ động xây dựng và bảo trì.
3.  **Compounding Value**: Tri thức càng lên tầng cao càng có giá trị tổng hợp và tính ứng dụng lớn.

## 1. Cấu trúc 3 Tầng (Standard SB3)
- **Tầng 1: Raw Sources (Dữ liệu thô)**: Immutable. Chứa các file gốc. Không bao giờ thay đổi nội dung ở đây để bảo toàn "chứng cứ thép".
- **Tầng 2: Wiki Atoms (Hạt nhân tri thức)**: LLM-Generated. Chứa Concept, Entity, Source Summary. Đây là lớp tri thức đã được "biên dịch" sang ngôn ngữ mà AI dễ dàng truy xuất.
- **Tầng 3: Synthesis / Synthesis (Tổng hợp)**: Human-AI Co-creation. Chứa các bài phân tích sâu, so sánh đa chiều và kết luận chiến lược.

## 2. Luồng chuyển hóa tri thức
`Raw` --(Ingest)--> `Wiki Atoms` --(Absorb/Query)--> `Synthesis`

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ Công nghệ (Original)
> **Bối cảnh**: Quản lý một dự án phát triển phần mềm phức tạp.
> **Ứng dụng**: 
> - Raw: Log lỗi, code repo, email khách hàng.
> - Wiki Atoms: Tài liệu API, định nghĩa hàm, mô tả bug.
> - Synthesis: Roadmap phát triển, báo cáo phân tích rủi ro, kiến trúc hệ thống tổng thể.
> **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Section: Three-Layer Architecture.

### Ẩn dụ sư phạm (Pedagogical Application)
> **Bối cảnh**: Quá trình học tập và thi cử của một học sinh.
> **Ứng dụng**: 
> - Raw: Sách giáo khoa, bài giảng của thầy cô (nguồn thô).
> - Wiki Atoms: Các thẻ ghi nhớ (Flashcards), các công thức toán học rút gọn (tri thức hạt nhân).
> - Synthesis: Một bài luận tổng kết hoặc một sơ đồ tư duy (Mindmap) kết nối toàn bộ kiến thức để giải quyết một bài toán thực tế phức tạp.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Section: Layers of Knowledge.

## ## History / Revisions
- **2026-05-03**: [@engineer] Khởi tạo concept SB3 Memory Tier.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
