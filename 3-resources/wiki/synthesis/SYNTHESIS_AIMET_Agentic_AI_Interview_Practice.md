---
file_id: SYNTHESIS_AIMET_AGENTIC_AI_INTERVIEW_PRACTICE
title: "Agentic AI Interview Practice (Q&A Bank)"
category: "Synthesis"
prefix: "SYNTHESIS"
agent_id: "@engineer"
status: "verified"
tags: ["Interview", "Agentic AI", "Python", "RAG", "Multi-Agent"]
source: "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

# Agentic AI Interview Practice (Q&A Bank)

Tập hợp các câu hỏi phỏng vấn thực tế và kịch bản giải quyết vấn đề trích xuất từ lộ trình AIMET 2026.

## 1. Python for Agentic AI
- **Q: Tại sao Pydantic lại quan trọng trong Agentic AI?**
  - **A**: Agent cần giao tiếp qua dữ liệu có cấu trúc (Structured Data). Pydantic đảm bảo dữ liệu đầu vào/đầu ra tuân thủ đúng Schema, giúp LLM thực hiện Function Calling chính xác và giảm thiểu lỗi logic khi tích hợp Tool.
- **Q: Decorator đóng vai trò gì trong các Agent Frameworks?**
  - **A**: Các framework như LangChain hay CrewAI sử dụng Decorators (vd: `@tool`) để đăng ký các hàm Python thông thường thành các công cụ mà Agent có thể nhận diện và sử dụng.

## 2. LLM & Prompting Strategy
- **Q: Sự khác biệt giữa Context Window và Token Limit là gì?**
  - **A**: Token Limit là giới hạn tối đa mô hình có thể xử lý trong một lần gọi. Context Window là toàn bộ "bộ nhớ ngắn hạn" hiện hữu. Trong Agentic AI, việc quản lý Context Window là sống còn để duy trì trí nhớ hội thoại (Memory Management).
- **Q: Làm thế nào để giảm Hallucination trong Multi-Agent systems?**
  - **A**: Sử dụng mẫu **Supervisor/Critic**. Một Agent thực hiện nhiệm vụ, một Agent khác đóng vai trò phản biện (Critic) để kiểm tra tính xác thực của kết quả trước khi trả về.

## 3. RAG & Memory
- **Q: "Lost in the middle" là hiện tượng gì?**
  - **A**: LLM có xu hướng ghi nhớ tốt thông tin ở đầu và cuối ngữ cảnh nhưng bỏ sót thông tin ở giữa. Giải pháp: Sử dụng Re-ranking để đẩy thông tin quan trọng nhất lên đầu.

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng kịch bản "Self-Correction" - Nếu Agent gọi Tool bị lỗi, hệ thống sẽ gửi thông báo lỗi ngược lại cho Agent để nó tự sửa tham số và gọi lại.
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một buổi thi vấn đáp: Không chỉ là việc bạn thuộc lòng (LLM Knowledge), mà là cách bạn xử lý khi giám khảo đưa cho bạn một tài liệu mới (RAG) và yêu cầu bạn sử dụng các công cụ có sẵn để giải quyết một bài toán thực tế (Tool Use).

## Nguồn tham khảo
- [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Toàn văn bộ câu hỏi phỏng vấn 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
