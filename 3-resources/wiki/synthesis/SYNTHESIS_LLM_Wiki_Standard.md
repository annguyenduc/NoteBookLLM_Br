---
file_id: SYNTHESIS_LLM_WIKI_STANDARD
title: "LLM Wiki Golden Standard (Tiêu chuẩn Vàng Wiki 2.0)"
category: "Synthesis"
prefix: "WIKI"
agent_id: "@librarian"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_KARPATHY_LLM_WIKI]]"
  - "[[SOURCE_META_NASHUS_LLMWIKI]]"
  - "[[CONCEPT_META_Atomic_Methodology]]"
---

# Tiêu chuẩn Vàng Wiki 2.0: Hợp nhất Karpathy & Nashus

## 1. Tầm nhìn chiến lược
Hệ thống NoteBookLLM_Br không chỉ là một kho lưu trữ (Storage), mà là một thực thể tri thức sống động. Chúng ta kết hợp triết lý **"Compounding Wiki"** của Karpathy với hạ tầng **"Graph Intelligence"** của Nashus để tạo ra một Second Brain có khả năng tự tiến hóa.

## 2. Các trụ cột kiến trúc (The Pillars)

### A. Triết lý Vận hành (Karpathy Pattern)
- **Obsidian là IDE / LLM là Coder**: Mọi trang Wiki phải được đối xử như mã nguồn. Phải có linting, version control (Git) và tính module hóa tuyệt đối.
- **Wiki vs RAG**: Ưu tiên việc "biên dịch" tri thức tại thời điểm nạp (Ingest-time Compilation) để giảm tải cho quá trình truy vấn và tăng độ chính xác.

### B. Hạ tầng Đồ thị (Nashus Pattern)
- **Relevance Model 4 tín hiệu**: Sử dụng trọng số Direct Link, Source Overlap, Adamic-Adar và Type Affinity để định vị tri thức.
- **Louvain Community Detection**: Tự động phát hiện các cộng đồng tri thức và các lỗ hổng (Gaps) thông qua phân tích Topology.

## 3. Cấu trúc bộ nhớ 3 Tầng (Memory Tiering)
| Tầng | Tên | Đặc tính | Quyền sở hữu |
| :--- | :--- | :--- | :--- |
| **Tier 1** | **Raw Sources** | Immutable (Bất biến) | User / Scout |
| **Tier 2** | **Wiki Atoms** | Atomic, Interlinked | AI Agent (Engineer) |
| **Tier 3** | **Synthesis** | Strategic, High-Level | Human + AI (Librarian) |

## 4. Quy trình vận hành chuẩn (SOP)
1.  **Ingest**: Nạp nguồn thô -> Phân tích CoT 2 bước -> Tạo Wiki Atoms.
2.  **Query**: Đọc `index.md` -> Truy vết đồ thị (Graph Traversal) -> Tổng hợp có trích dẫn.
3.  **Absorb**: Hợp nhất các tri thức mới từ Query/Research vào Wiki Atoms hiện có.
4.  **Lint/Audit**: Kiểm tra mâu thuẫn tri thức, link hỏng và Link Density Index (LDI).

## 5. Phép thử thành công (The Success Test)
> "Nếu bạn nạp 10 nguồn tri thức mới và đặt một câu hỏi tổng hợp, hệ thống phải đưa ra được một insight mà bạn không thể tìm thấy nếu chỉ đọc 10 nguồn đó một cách rời rạc."

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Toàn bộ mô hình Gist.
- **Nguồn**: [[SOURCE_META_NASHUS_LLMWIKI]] — Toàn bộ mô hình Graph.

## ## History / Revisions
- **2026-05-03**: [@librarian] Khởi tạo Synthesis tiêu chuẩn vàng Wiki 2.0.


## 4F Reflection
- **Facts**: Hệ thống build được đầy đủ về kỹ thuật nhưng 289 atoms cũ không có content thật. Agent hallucinate nếu không có human check.
- **Feelings**: Hứng thú ban đầu → thực tế phức tạp hơn. Cần kiểm soát nhiều hơn tưởng.
- **Findings**: Human Gate không phải optional — là thứ duy nhất ngăn vault đầy rác. Hiểu lý do agents sai quan trọng hơn biết agents làm gì.
- **Futures**: Tuần tới: ingest có chọn lọc thay vì bulk. Mỗi atom phải qua mắt mình trước khi VERIFIED.
