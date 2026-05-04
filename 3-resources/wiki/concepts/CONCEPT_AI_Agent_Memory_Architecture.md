---
file_id: CONCEPT_AI_AGENT_MEMORY_ARCHITECTURE
title: "Agent Memory Architecture (Kiến trúc bộ nhớ Agent)"
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
Trang này mô tả các tầng kiến trúc bộ nhớ cần thiết để Agent duy trì ngữ cảnh qua thời gian. Khác với người dùng cá nhân chỉ cần nhớ lịch sử chat, một Agent cấp độ doanh nghiệp cần một hệ thống bộ nhớ có cấu trúc để "học" từ các sai lầm quá khứ, lưu giữ các quyết định quan trọng và tái hiện lại trạng thái khi cần thiết.

## ## Key Claims / Summary
1.  **Short-term Memory**: Context Window hiện tại - cực kỳ nhanh nhưng có giới hạn.
2.  **Long-term Memory**: Dữ liệu lưu trữ bền vững (Vector DB, Knowledge Graphs) - không giới hạn nhưng chậm hơn.
3.  **Checkpointing**: Khả năng "chụp ảnh" trạng thái của Agent tại một thời điểm để có thể phục hồi (rollback) hoặc phân tích lỗi.

## 1. Phân tầng bộ nhớ
- **Sensory/Episodic**: Ghi lại các sự kiện cụ thể đã xảy ra (Log history).
- **Semantic**: Lưu trữ tri thức cốt lõi và các quy tắc (Wiki/Database).
- **Procedural**: Lưu trữ các kỹ năng và quy trình đã học (Skills/Prompts).

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Sử dụng LangGraph để thực hiện Checkpointing. Sau mỗi hành động gọi Tool, trạng thái của Agent được lưu vào DB. Nếu hệ thống bị sập giữa chừng, Agent có thể tiếp tục công việc ngay tại bước vừa rồi mà không phải gọi lại LLM từ đầu. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 6).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một trò chơi video (Video Game). Bạn có **thanh máu và vị trí hiện tại** (Short-term), **kho đồ và kinh nghiệm** tích lũy qua nhiều màn chơi (Long-term), và quan trọng nhất là các **điểm lưu game - Save points** (Checkpointing) để bạn không phải chơi lại từ màn 1 khi bị "game over".

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 6: Memory Management.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
