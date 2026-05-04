---
file_id: CONCEPT_AI_CONTEXT_BUDGETING
title: "Context Budgeting (Quản lý ngân sách ngữ cảnh)"
category: "Wiki Page"
prefix: "AI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

## ## For future Claude
Trang này định nghĩa chiến lược Ngân sách ngữ cảnh (Context Budgeting) - nghệ thuật phân bổ tài nguyên Tokens trong cửa sổ ngữ cảnh (Context Window). Khi xây dựng Agent, chúng ta phải coi không gian ngữ cảnh là hữu hạn và quý giá. Việc phân bổ định lượng giúp bảo vệ các hướng dẫn hệ thống (System Instructions) không bị "đẩy ra ngoài" bởi dữ liệu thô từ RAG hay lịch sử trò chuyện quá dài.

## ## Key Claims / Summary
1.  **Quantitative Allocation**: Chia Context Window thành các vùng cố định (ví dụ: 30% RAG, 20% Memory, 50% Instructions/Current Task).
2.  **Compression over Truncation**: Ưu tiên việc tóm tắt, nén hoặc deduplicate dữ liệu thay vì chỉ cắt bỏ (truncate) phần cũ nhất.
3.  **Instruction Protection**: Luôn dành ưu tiên cao nhất cho System Instructions và các ràng buộc an toàn.

## 1. Các kỹ thuật tối ưu hóa
- **Summarization**: Tóm tắt các lượt hội thoại cũ để giữ lại ý chính.
- **Top-K Filtering**: Chỉ lấy những kết quả RAG có độ tương quan cao nhất.
- **Schema Pruning**: Loại bỏ các trường thông tin không cần thiết trong JSON tool outputs.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Khi xây dựng một Agent đọc tài liệu dài, kỹ sư thiết lập ngân sách: tối đa 30% context dành cho các đoạn trích dẫn từ RAG. Nếu dữ liệu vượt quá, hệ thống tự động yêu cầu LLM tóm tắt các đoạn trích đó trước khi đưa vào prompt chính. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 6).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn đóng gói hành lý cho một chuyến bay giá rẻ. Bạn có một chiếc vali giới hạn 7kg (Context Window). Bạn phải quyết định: bao nhiêu chỗ cho quần áo (Data), bao nhiêu cho giấy tờ (Instructions), và bao nhiêu cho quà cáp (Memory). Nếu bạn nhét quá nhiều quần áo, bạn sẽ phải bỏ lại giấy tờ quan trọng.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 3: LLM Fundamentals & Section 6: Memory Management.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
