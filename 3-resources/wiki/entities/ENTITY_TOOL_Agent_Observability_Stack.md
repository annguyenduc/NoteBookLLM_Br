---
file_id: ENTITY_TOOL_AGENT_OBSERVABILITY_STACK
title: "Agent Observability Stack (Bộ công cụ giám sát Agent)"
category: "Wiki Page"
prefix: "ENTITY"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

## ## For future Claude
Trang này tổng hợp các công cụ và chỉ số cần thiết để giám sát hoạt động của Agent. Khi một Agent phản hồi sai, chúng ta không thể chỉ đoán mò. Chúng ta cần nhìn sâu vào từng bước suy luận, từng token được sinh ra và từng kết quả của Tool. Observability (Khả năng quan sát) là nền tảng để tinh chỉnh (fine-tune) và bảo trì hệ thống tri thức.

## ## Key Claims / Summary
1.  **Trace Analysis**: Khả năng theo dõi một yêu cầu từ lúc người dùng nhập vào cho đến khi có câu trả lời cuối cùng, bao gồm cả các vòng lặp ẩn.
2.  **Prompt Versioning**: Theo dõi xem phiên bản prompt nào đang được chạy và tác động của nó đến kết quả đầu ra.
3.  **Unit Economics**: Đo lường chi phí (USD/Tokens) cho mỗi hành động cụ thể của Agent.

## 1. Các công cụ tiêu biểu
- **LangSmith**: Giám sát luồng suy luận và debug các node trong đồ thị.
- **Arize Phoenix**: Phân tích RAG và phát hiện Hallucination.
- **OpenTelemetry for AI**: Tiêu chuẩn hóa việc thu thập log/metrics cho hệ thống Agent.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Sử dụng LangSmith để phát hiện ra rằng Agent thường xuyên bị lặp vô hạn (infinite loop) khi không tìm thấy kết quả từ Tool search. Nhờ Tracing, kỹ sư nhìn thấy LLM liên tục sinh ra cùng một suy nghĩ (Thought) và đã sửa lại System Prompt để thêm một "Exit condition". (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 11).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một chiếc camera hành trình trên ô tô. Nó không giúp chiếc xe chạy nhanh hơn, nhưng nếu có tai nạn (Lỗi AI), bạn có thể tua lại video để xem chính xác chuyện gì đã xảy ra tại giây thứ mấy, do người lái hay do lỗi kỹ thuật, từ đó có biện pháp khắc phục đúng chỗ.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 11: Deployment & Production.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
