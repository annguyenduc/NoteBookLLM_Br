---
file_id: SYNTHESIS_Agentic_AI_Synthesis_20260508
title: Agentic AI — Synthesis
type: synthesis
status: DRAFT
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-08
last_updated: 2026-05-08
---

## Core Idea
Agentic AI đại diện cho sự chuyển dịch từ các ứng dụng LLM thụ động sang các hệ thống tác tử (Agent) có khả năng tự trị, giao tiếp, điều phối đa Agent và tương tác với môi trường bên ngoài bằng công cụ (Tool Integration) để giải quyết các tác vụ phức tạp.

## Key Points
- **Tích hợp công cụ (Tool Integration):** Kỹ năng cốt lõi giúp Agent vượt qua giới hạn chỉ xử lý văn bản, thực thi API và code thông qua Pydantic schema và Decorators (ví dụ: `@tool`). Dẫn nguồn từ: [[CONCEPT_AIMET_Tool_Integration]] & [[SYNTHESIS_AIMET_Agentic_AI_Interview_Practice]].
- **Điều phối Đa Agent (Multi-Agent Orchestration):** Khi độ phức tạp của bài toán tăng, việc chia nhỏ nhiệm vụ (Supervisor/Critic) giúp giảm thiểu hiện tượng Hallucination. Dẫn nguồn từ: [[SYNTHESIS_Agentic_Orchestration_Frameworks]].
- **Lựa chọn Frameworks chiến lược:**
  - **AutoGen:** Hội thoại linh hoạt, giải quyết vấn đề sáng tạo. [[ENTITY_AIMET_AutoGen]]
  - **CrewAI:** Tổ chức dựa trên vai trò/quy trình rõ ràng, phù hợp hành chính/nghiên cứu. [[ENTITY_AIMET_CrewAI]]
  - **LangGraph:** Quản lý bằng đồ thị trạng thái, kiểm soát chặt chẽ phù hợp cho Production. [[ENTITY_AIMET_LangGraph]]
- **Bộ nhớ và RAG:** Quản lý Context Window và giải quyết hiện tượng "Lost in the middle" qua Re-ranking là cực kỳ quan trọng đối với khả năng ghi nhớ dài hạn của Agent. Dẫn nguồn từ: [[SYNTHESIS_AIMET_Agentic_AI_Interview_Practice]].

## Open Questions / Tensions
- Làm thế nào để đảm bảo tính ổn định và tránh lỗi logic khi một Agent trong luồng LangGraph gặp sự cố (Failures) ở bước tích hợp Tool? (Sự giằng co giữa tính linh hoạt của AutoGen và tính tin cậy của LangGraph).
- Mặc dù khái niệm "Multi-Agent Architecture" là trụ cột của hệ thống, tuy nhiên Atom `[[CONCEPT_AIMET_MultiAgent_Architecture]]` hiện chỉ là một bản nháp STUB (độ tin cậy 0.10) và chưa có định nghĩa chính thức.

## Next Actions
- Đọc và bổ sung nội dung cho Atom `[[CONCEPT_AIMET_MultiAgent_Architecture]]` từ các tài liệu RAW trong thư mục Inbox.
- Chạy hệ thống kiểm thử thực tế (Ví dụ: Build một pipeline với CrewAI và Custom Tools) để nâng cấp trạng thái từ DRAFT lên SYNTHESIZED.
- Chạy lệnh `/rebuild` để đồng bộ lại File vật lý và Database vì quá trình query phát hiện sự lệch pha ở Prefix (VD: CONCEPT_AI vs CONCEPT_AIMET).
