---
file_id: CONCEPT_AI_TOOL_DESIGN_STANDARDS
title: "Tool Design Standards (Tiêu chuẩn thiết kế Tool cho Agent)"
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
Trang này định nghĩa các tiêu chuẩn để thiết kế các công cụ (Tools) mà AI có thể sử dụng hiệu quả. Một Tool "thân thiện với AI" khác với một API thông thường. Nó cần các mô tả cực kỳ rõ ràng, cơ chế xử lý lỗi có cấu trúc và khả năng trả về dữ liệu tinh gọn để tiết kiệm ngữ cảnh.

## ## Key Claims / Summary
1.  **Semantic Description**: Mô tả Tool không phải cho lập trình viên mà cho LLM (Giải thích: "Tại sao nên dùng Tool này?" thay vì "Nó làm gì?").
2.  **Structured Error Feedback**: Khi Tool lỗi, nó phải trả về lý do cụ thể (như: "ID không tồn tại, hãy thử list_all để tìm ID đúng") để Agent tự sửa.
3.  **Atomic Tools**: Ưu tiên các Tool nhỏ, thực hiện một nhiệm vụ duy nhất thay vì các Tool "vạn năng" phức tạp.

## 1. Checklist thiết kế Tool
- **Input Validation**: Sử dụng Pydantic/JSON Schema để cưỡng bức định dạng.
- **Output Pruning**: Chỉ trả về những trường dữ liệu mà Agent thực sự cần.
- **Safety Metadata**: Đánh dấu các Tool có tính "phá hủy" (như xóa file) để kích hoạt cơ chế Human-in-the-loop.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Thay vì một Tool `get_user_info` trả về 50 trường dữ liệu (gồm cả ảnh đại diện, hash mật khẩu), kỹ sư thiết kế `get_user_profile_summary` chỉ trả về: `username`, `email`, `role`. Điều này giúp giảm 90% lượng token rác trong context. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 7).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn đưa một hộp dụng cụ cho một người đang bị bịt mắt và hướng dẫn họ qua radio. Nếu trên mỗi chiếc kìm, tua vít có dán nhãn chữ nổi ghi rõ công dụng và cách cầm, người đó sẽ làm việc rất nhanh. Nếu hộp dụng cụ chỉ là một đống lộn xộn, họ sẽ cầm nhầm đồ và gây hỏng hóc.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 7: Tool Use & Function Calling.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
