---
file_id: CONCEPT_TOOL_PYDANTIC
title: "Pydantic (Data Validation & Settings)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@scout"
status: "stub"
source: "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

# Pydantic (Data Validation & Settings)

## Core Principle
Pydantic là thư viện kiểm soát dữ liệu (Data Validation) mạnh mẽ nhất trong Python, đóng vai trò là "xương sống" cho việc trao đổi thông tin có cấu trúc giữa Agent và các Tools. Nó sử dụng Python Type Annotations để ép buộc kiểu dữ liệu và tự động tạo Schema.

## Vai trò trong Agentic AI
1. **Tool Definition**: Định nghĩa Schema cho các công cụ (Tools) để LLM biết chính xác tham số cần truyền.
2. **Structured Output**: Ép LLM trả về dữ liệu định dạng JSON hợp lệ thông qua `BaseModel`.
3. **Error Handling**: Tự động phát hiện lỗi khi LLM truyền sai tham số và cung cấp thông báo lỗi có cấu trúc để Agent tự sửa (Self-correction).

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Khi định nghĩa một công cụ lấy thời tiết, Pydantic đảm bảo tham số `city` phải là String và `days` phải là Integer từ 1-7.
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một "Cửa an ninh" tại sân bay: Chỉ những hành khách có giấy tờ (dữ liệu) đúng quy chuẩn mới được đi qua. Nếu thiếu hoặc sai, cửa sẽ báo động (Error) và yêu cầu cung cấp lại chính xác.

## 4F Reflection
- **Facts**: Pydantic v2 (viết bằng Rust) nhanh hơn gấp nhiều lần so với v1.
- **Feelings**: Mang lại sự an tâm tuyệt đối khi làm việc với các LLM không ổn định.
- **Findings**: Việc kết hợp Pydantic với FastAPI là bộ đôi hoàn hảo cho Agent Backend.
- **Futures**: Xu hướng tích hợp trực tiếp Pydantic vào các LLM SDK (như OpenAI, Google) đang ngày càng phổ biến.

## Nguồn tham khảo
- [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9.2 (Strong typing via Pydantic).
