---
source_id: SOURCE_META_KARPATHY_LLM_WIKI
title: "WEB: Andrej Karpathy's [[CONCEPT_META_SB3_LLM_Wiki|LLM Wiki Pattern]] (Gist Guide)"
author: "Andrej Karpathy"
category: "WEB"
domain: "Knowledge Management"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
---

relationships:
  - type: "relates_to"
    target: "[[CONCEPT_META_SB3_LLM_Wiki]]"

# WEB Karpathy's [[CONCEPT_META_SB3_LLM_Wiki|LLM Wiki Pattern]]

## 📝 1. Phân tích Ingest (Analysis - Step 1)
- **Thực thể & Khái niệm then chốt:** Wiki vs RAG, [[CONCEPT_META_SB3_Memory_Tier|Three-Layer Architecture]], [[CONCEPT_META_SB3_Task_Ledger|Task Ledger]], [[CONCEPT_META_SB3_Graph_Traversal|Graph Traversal]], Idea Files.
- **Kết nối Wiki:** Cung cấp triết lý "Obsidian là IDE, LLM là lập trình viên, Wiki là codebase".
- **Điểm khác biệt/Mâu thuẫn:** Phản biện mô hình RAG truyền thống (rediscovering knowledge from scratch) bằng mô hình Compounding Wiki.
- **Đề xuất cấu trúc:** Xây dựng hệ thống CONCEPT_META_SB3 để định nghĩa tiêu chuẩn Second Brain 3.0.

## 📖 2. Tổng quan nguồn (Overview - Step 2)
Tài liệu định nghĩa sự chuyển dịch từ việc dùng Token cho Code sang dùng Token cho **Tri thức**. Thay vì truy xuất dữ liệu thô (RAG), hệ thống "biên dịch" (compile) nguồn thô thành một Wiki có cấu trúc, cho phép tri thức tích lũy (compound) theo thời gian.

### So sánh Wiki vs RAG (Karpathy Standard)
| Đặc tính | Traditional RAG | LLM Wiki |
| :--- | :--- | :--- |
| **Thời điểm xử lý** | Khi truy vấn (mọi lúc) | Khi nạp (một lần) |
| **Liên kết chéo** | Khám phá ad-hoc | Được xây dựng sẵn |
| **Mâu thuẫn** | Dễ bị bỏ qua | Được gắn cờ khi nạp |
| **Tích lũy tri thức** | Không có (bắt đầu lại mỗi query) | Tích lũy bền vững (Compounding) |

## 🚀 3. Các Concept đã trích xuất (Rule 14 & 17)
- [[CONCEPT_META_SB3_LLM_Wiki]] | **LLM Wiki Pattern** - Mô hình biên dịch tri thức thay vì truy xuất thô.
- [[CONCEPT_META_SB3_Memory_Tier]] | **Three-Layer Architecture** - Cấu trúc 3 tầng: Raw (Immutable) -> Wiki (LLM-Owned) -> Schema (Rules).
- [[CONCEPT_META_SB3_Task_Ledger]] | **Task Ledger** - Nhật ký tác vụ bền vững để Agent không quên ngữ cảnh.
- [[CONCEPT_META_SB3_Graph_Traversal]] | **Graph Traversal** - Truy vết đồ thị để tìm liên kết ẩn thay vì search keyword.

## 🔍 4. Review Items (Dành cho Human)
- [ ] Triển khai script `lint` để tự động phát hiện mâu thuẫn tri thức giữa các trang.
- [ ] Thiết lập quy trình "Save to Wiki" cho các câu trả lời có giá trị từ Chat.

--- 
**Nguồn thô:** `AIMET_Karpathys_LLM_Wiki_Guide.md`
**Deep Research Query:** `Andrej Karpathy LLM Wiki vs RAG architecture`



## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
