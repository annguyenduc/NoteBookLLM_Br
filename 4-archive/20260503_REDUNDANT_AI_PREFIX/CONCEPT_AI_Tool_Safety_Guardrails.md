---
file_id: "WIKI_CONCEPT_AI_TOOL_SAFETY_GUARDRAILS"
title: "Rào chắn an toàn cho Công cụ (Tool Safety Guardrails)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["AI", "Safety", "Tools", "Sandboxing", "Guardrails"]
source: "RAW_PDF_Agentic_AI_Roadmap"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# Rào chắn an toàn cho Công cụ (Tool Safety Guardrails)

Các cơ chế kiểm soát nhằm đảm bảo Agent sử dụng các công cụ ngoại vi một cách an toàn, bảo mật và không gây hại cho hệ thống.

## Core Principle
Nguyên tắc cốt lõi là **Đặc quyền tối thiểu (Least Privilege)** và **Phân tách trách nhiệm (Separation of Concerns)**.
1. **Sandbox (Môi trường cô lập):** Giới hạn quyền hạn của công cụ (ví dụ: chỉ được đọc/ghi trong một thư mục nhất định, không có quyền truy cập internet tự do).
2. **Allowlist (Danh sách cho phép):** Chỉ cho phép Agent gọi các công cụ đã được phê duyệt.
3. **Human-in-the-loop (Con người kiểm soát):** Các hành động có rủi ro cao (xóa dữ liệu, thanh toán, gửi email) bắt buộc phải có sự xác nhận của con người trước khi thực thi.

## Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ tài liệu (Original)
Một Agent có công cụ `web_search`. Để tránh Tool Abuse, chúng ta đặt **Policy Gate**: Executor (Trình thực thi) sẽ kiểm tra giới hạn tốc độ (rate limit) và phạm vi truy cập (scope) trước khi thực sự gọi API. Nếu Agent yêu cầu truy cập một URL nhạy cảm, Policy Gate sẽ từ chối ngay lập tức.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng một phòng thí nghiệm hóa học trong trường học:
- **Sandbox:** Các phản ứng nguy hiểm phải được thực hiện trong tủ hút (fume hood).
- **Human-in-the-loop:** Học sinh không được tự ý lấy hóa chất nồng độ cao trừ khi giáo viên (con người) đồng ý và giám sát trực tiếp.
- **Tool Friendly:** Các lọ hóa chất đều có nhãn ghi rõ tên, nồng độ và cách sử dụng (tương đương với Structured Input Schema trong code).

## Liên kết tư duy
- [[CONCEPT_AI_Agentic_Workflow_Patterns]]
- [[ENTITY_TOOL_Lightpanda]]

## 4F Reflection
- **Facts:** Các công cụ "Agent-friendly" cần có schema đầu vào rõ ràng, đầu ra có cấu trúc (JSON/Dict) và cơ chế báo lỗi tường minh (Error Codes).
- **Feelings:** Việc thiết lập rào chắn mang lại sự an tâm khi triển khai các Agent có khả năng can thiệp vào thế giới thực.
- **Findings:** Sandbox và Allowlist là tiêu chuẩn bắt buộc cho bất kỳ hệ thống Agent nào xử lý mã code hoặc dữ liệu nhạy cảm.
- **Futures:** Trong tương lai, các "Hệ điều hành cho Agent" sẽ tự động quản lý quyền hạn (Permissions) ở mức hạt nhân (Kernel level) giống như cách Android hay iOS quản lý quyền ứng dụng.

---
Nguồn: [[RAW_PDF_Agentic_AI_Roadmap]] (Section 7: Tool Integration)
Xác nhận Rule 14 từ MarkItDown Conversion (2026-05-03).
