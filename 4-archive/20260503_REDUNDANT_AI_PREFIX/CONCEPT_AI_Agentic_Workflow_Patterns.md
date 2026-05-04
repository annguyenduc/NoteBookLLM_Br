---
file_id: "WIKI_CONCEPT_AI_AGENTIC_WORKFLOW_PATTERNS"
title: "Các mẫu luồng công việc Agentic (Agentic Workflow Patterns)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["AI", "Agents", "Architecture", "ReAct", "Supervisor"]
source: "RAW_PDF_Agentic_AI_Roadmap"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# Các mẫu luồng công việc Agentic (Agentic Workflow Patterns)

Các mẫu thiết kế (Design Patterns) giúp điều phối các Agent để giải quyết các tác vụ phức tạp một cách tin cậy.

## Core Principle
Bản chất của các mẫu này là việc **Phân rã (Decomposition)** tác vụ lớn thành các bước nhỏ và áp dụng cơ chế **Vòng lặp phản hồi (Feedback Loops)** để tự sửa lỗi.

1. **ReAct (Reason + Act):** Agent xen kẽ giữa việc suy luận (Plan) và hành động (Tool call). Quan sát kết quả (Observation) để quyết định bước tiếp theo.
2. **Supervisor (Người giám sát):** Một Agent trung tâm điều phối các Agent chuyên biệt (Retriever, Coder, Critic), phân chia nhiệm vụ và hợp nhất kết quả.
3. **Planning & Execution:** Tách biệt giai đoạn lập kế hoạch (Planner) và giai đoạn thực thi (Executor) để tăng tính an toàn và kiểm soát.

## Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ tài liệu (Original)
Một hệ thống RAG phức tạp có thể dùng Supervisor để điều phối:
`Retrieve (Agent 1) -> Summarize (Agent 2) -> Draft (Agent 3) -> Verify (Agent 4)`. Nếu Agent 4 (Critic) phát hiện lỗi, Supervisor sẽ ra lệnh cho Agent 1 lấy thêm nguồn dữ liệu mới.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng quy trình xây một ngôi nhà:
- **Mẫu ReAct:** Người thợ xây vừa xây vừa nhìn bản vẽ, nếu thấy gạch bị lệch thì sẽ điều chỉnh ngay lập tức dựa trên quan sát thực tế.
- **Mẫu Supervisor:** Một kiến trúc sư trưởng (Supervisor) chỉ đạo thợ điện, thợ nước và thợ nề. Khi thợ nề xây xong, kiến trúc sư kiểm tra, nếu chưa đạt thì yêu cầu làm lại trước khi cho thợ điện vào làm.

## Liên kết tư duy
- [[CONCEPT_AI_Agentic_Architecture_2026]]
- [[CONCEPT_AI_Multi_Agent_Coordination]]

## 4F Reflection
- **Facts:** ReAct giúp giảm hallucination (ảo tưởng) vì Agent có thể tra cứu thông tin thay vì tự đoán. Supervisor hiệu quả cho các bài toán cần chuyên môn hóa cao.
- **Feelings:** Việc nhìn thấy các Agent tự giao tiếp và sửa lỗi cho nhau mang lại cảm giác về một hệ thống "sống" và có trí tuệ thực sự.
- **Findings:** Sự tách biệt giữa Planning và Execution là chìa khóa để triển khai Agent trong môi trường sản xuất (Production) một cách an toàn.
- **Futures:** Xu hướng 2026 sẽ chuyển từ các Agent đơn lẻ sang các "Quần thể Agent" (Agent Swarms) với giao thức giao tiếp (Protocols) chặt chẽ.

---
Nguồn: [[RAW_PDF_Agentic_AI_Roadmap]] (Section 9: Agents & Multi-Agents)
Xác nhận Rule 14 từ MarkItDown Conversion (2026-05-03).
