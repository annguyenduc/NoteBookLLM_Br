---
file_id: "WIKI_CONCEPT_AIMET_MULTIAGENT_ARCHITECTURE"
title: "Kiến trúc Đa Agent (Multi-Agent Architecture)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Agentic AI", "Multi-Agent", "Supervisor", "Orchestration", "AIMET"]
source: "SOURCE_AIMET_AgenticAI_Roadmap_2026"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# Kiến trúc Đa Agent (Multi-Agent Architecture)

Kiến trúc Đa Agent là thiết kế hệ thống trong đó nhiều Agent chuyên biệt phối hợp với nhau để giải quyết các tác vụ phức tạp vượt quá khả năng của một Agent đơn lẻ.

## Core Principle
Nguyên tắc cốt lõi là **Chuyên môn hóa (Specialization)** và **Điều phối (Orchestration)**. Thay vì một Agent "biết tuốt", chúng ta có nhiều Agent chuyên trách:
- Mỗi Agent có một **Vai trò (Role)** cụ thể.
- Mỗi Agent sở hữu một **Bộ công cụ (Tool set)** riêng biệt.
- Giao tiếp thông qua các **Thông điệp có cấu trúc (Structured Messages)**.

**Mẫu Supervisor (Người giám sát):** Đây là mẫu phổ biến nhất, trong đó một Agent trung tâm điều phối các Agent chuyên biệt (Retriever, Coder, Critic), phân chia nhiệm vụ và hợp nhất kết quả.

## Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ tài liệu (Original)
Hệ thống phân tích thị trường chứng khoán:
`Supervisor` nhận yêu cầu -> phân công: `DataFetcher` (lấy dữ liệu), `Analyst` (tính toán chỉ số), `Writer` (tạo báo cáo). `Supervisor` sau đó kiểm tra tính nhất quán và trả kết quả cho người dùng.
*Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 9*

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng quy trình xây một ngôi nhà:
Một kiến trúc sư trưởng (**Supervisor**) chỉ đạo thợ điện, thợ nước và thợ nề. Khi thợ nề xây xong, kiến trúc sư kiểm tra, nếu đạt yêu cầu thì mới ra lệnh cho thợ điện vào làm. Việc chuyên môn hóa giúp thợ điện không cần biết xây tường, nhưng vẫn tạo ra một ngôi nhà hoàn chỉnh thông qua sự điều phối.

## Liên kết tư duy
- [[CONCEPT_AIMET_ReAct_Pattern]]
- [[ENTITY_AIMET_LangGraph]]
- [[ENTITY_AIMET_CrewAI]]

## 4F Reflection
- **Facts:** Đa Agent giúp tăng tính tin cậy vì lỗi của một Agent chuyên biệt có thể được phát hiện và sửa chữa bởi Agent khác (ví dụ: Critic).
- **Feelings:** Độ phức tạp tăng lên đáng kể; việc theo dõi (Observability) luồng giao tiếp giữa các Agent mang lại cảm giác như đang quản lý một đội ngũ nhân sự thực thụ.
- **Findings:** Giao thức giao tiếp (Agent Protocols) là yếu tố sống còn để các Agent không hiểu lầm ý nhau.
- **Futures:** Xu hướng 2026 sẽ là các **Agent Swarms** (Quần thể Agent) có khả năng tự tổ chức (Self-organizing) dựa trên yêu cầu của tác vụ.

---
Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 9 (Agents & Multi-Agents)
Xác nhận Rule 14 từ MarkItDown Conversion (2026-05-03).
