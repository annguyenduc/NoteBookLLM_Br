---
file_id: CONCEPT_AI_MULTIAGENT_COORDINATION
title: "Multi-Agent Coordination (Phối hợp đa Agent)"
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
Trang này mô tả các mô hình phối hợp giữa nhiều Agent chuyên biệt. Khi các bài toán trở nên quá lớn cho một Agent duy nhất, chúng ta cần một hệ thống các thực thể cùng làm việc. Sự phối hợp này yêu cầu các giao thức truyền thông rõ ràng và sự phân định trách nhiệm chặt chẽ để tránh xung đột hoặc lặp lại công việc.

## ## Key Claims / Summary
1.  **Supervisor Pattern**: Một Agent trung tâm quản lý luồng công việc, phân việc cho các Worker Agent và tổng hợp kết quả.
2.  **Autonomous Collaboration**: Các Agent tự giao tiếp với nhau qua các kênh (bus/queue) dựa trên kỹ năng chuyên môn.
3.  **State Handoff**: Chuyển giao trạng thái (state) và lịch sử công việc giữa các Agent để đảm bảo tính liên tục của tri thức.

## 1. Các mô hình phối hợp
- **Hierarchical**: Cấp trên phân việc cho cấp dưới (Supervisor).
- **Sequential**: Agent A làm xong trỏ kết quả cho Agent B.
- **Joint-Action**: Nhiều Agent cùng làm việc trên một không gian trạng thái chung (Shared Space).

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Xây dựng hệ thống viết code tự động gồm 3 Agent: (1) Architect thiết kế cấu trúc, (2) Coder viết mã nguồn, (3) QA viết test và kiểm tra. Supervisor Agent sẽ điều phối: nếu QA báo lỗi, nó sẽ yêu cầu Coder sửa lại cho đến khi đạt yêu cầu mới cho phép đóng task. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một ban nhạc giao hưởng. Nhạc trưởng (Supervisor) không chơi nhạc cụ, nhưng họ biết khi nào thì Violin phải lên tiếng và khi nào thì Trumpet phải dừng lại. Sự phối hợp nhịp nhàng giữa các nhạc công chuyên nghiệp (Specialized Agents) tạo nên bản nhạc hoàn hảo.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9: Agents & Multi-Agents.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
