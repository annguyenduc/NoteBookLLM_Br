---
file_id: "WIKI_CONCEPT_AIMET_PRODUCTION_GUARDRAILS"
title: "Rào chắn sản xuất (Production Guardrails)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Security", "Guardrails", "Production", "Reliability", "AIMET"]
source: "SOURCE_AIMET_AgenticAI_Roadmap_2026"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# Rào chắn sản xuất (Production Guardrails)

Production Guardrails là tập hợp các rào chắn kiến trúc và logic được thiết kế để kiểm soát tính phi định hướng (non-determinism) của LLM, đảm bảo Agent vận hành an toàn và tin cậy.

## Core Principle
Hệ thống rào chắn hiện đại tuân thủ nguyên tắc **Đặc quyền tối thiểu (Least Privilege)** và **Bảo mật đa lớp (Defense in Depth)**:

1. **Lớp Thực thi (Execution Layer):** Sử dụng **Sandbox** (môi trường cô lập) và **Allowlist** để giới hạn quyền hạn của công cụ.
2. **Lớp Quy trình (Plan Layer):** Sử dụng **Human-in-the-loop (HITL)** để dừng lại và xin phê duyệt cho các hành động rủi ro cao (thanh toán, xóa dữ liệu).
3. **Lớp Dữ liệu (Data Layer):** Kiểm tra tính hợp lệ của tham số đầu vào (Schema Enforcement) và lọc thông tin nhạy cảm (PII Redaction).

## Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ tài liệu (Original)
Một Agent có công cụ `web_search`. Để tránh lạm dụng (Tool Abuse), trình thực thi (**Executor**) sẽ kiểm tra giới hạn tốc độ (rate limit) và phạm vi truy cập (scope) trước khi gọi API. Nếu Agent cố gắng truy cập một URL trong danh sách đen, hệ thống sẽ từ chối và ghi log cảnh báo.
*Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 7*

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng một phòng thí nghiệm hóa học trong trường học:
- **Sandbox:** Các phản ứng nguy hiểm phải được thực hiện trong tủ hút.
- **Human-in-the-loop:** Học sinh không được tự ý lấy hóa chất nồng độ cao trừ khi giáo viên (**Supervisor**) đồng ý và giám sát trực tiếp.
Việc thiết lập các rào chắn này giúp học sinh có thể thực hành (Execute) mà vẫn đảm bảo an toàn tuyệt đối cho bản thân và nhà trường.

## Liên kết tư duy
- [[CONCEPT_AIMET_Error_Handling_Patterns]]
- [[ENTITY_AIMET_LangGraph]]

## 4F Reflection
- **Facts:** Công cụ "Agent-friendly" cần có schema rõ ràng và cơ chế báo lỗi tường minh để Guardrails có thể làm việc hiệu quả.
- **Feelings:** Việc thiết lập rào chắn mang lại sự an tâm khi triển khai các Agent có khả năng can thiệp trực tiếp vào dữ liệu sản xuất.
- **Findings:** Các chính sách bảo mật nên được lập trình trực tiếp vào cấu trúc luồng công việc (Governance-as-Code).
- **Futures:** Xu hướng tương lai là các "Hệ điều hành Agent" tự động quản lý quyền hạn ở mức hạt nhân tương tự như Android/iOS.

---
Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 4 & 7
Xác nhận Rule 14 từ MarkItDown Conversion (2026-05-03).
