---
file_id: SOURCE_AIMET_AGENTIC_ROADMAP_2026
title: "Agentic AI Engineer Roadmap (2026)"
category: "Source Summary"
prefix: "SOURCE"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
raw_hash: "594aa6b60f34756085749f27b999f8df"
source_type: "PDF Roadmap"
author: "Lamhot Siagian"
year: 2026
---

## ## For future Claude
Tài liệu này là một lộ trình toàn diện để trở thành Kỹ sư AI Agentic vào năm 2026. Nó không chỉ liệt kê các công nghệ mà còn tập trung vào tư duy kỹ thuật (Software Engineering) cần thiết để xây dựng các hệ thống Agent ổn định, an toàn và có khả năng triển khai thực tế. Tài liệu được cấu trúc dưới dạng câu hỏi phỏng vấn Q&A, giúp người học nắm bắt nhanh các khái niệm then chốt và các cạm bẫy thường gặp.

## ## Key Takeaways
1.  **Python is Foundation**: Python không chỉ là ngôn ngữ lập trình mà là một hệ sinh thái (FastAPI, Pydantic, Async) giúp làm "cứng" (harden) các hệ thống Agent.
2.  **Deterministic over Stochastic**: Ưu tiên các luồng công việc xác định (LangGraph, State Machines) để kiểm soát sự ngẫu nhiên của LLM.
3.  **Context as a Resource**: Quản lý Context Window như một tài nguyên có hạn thông qua chiến lược "Context Budgeting".
4.  **Security-First Tooling**: Phân tách quyền hạn công cụ (Least Privilege) và sử dụng Sandbox để giảm thiểu rủi ro từ Agent tự trị.

## ## Content Map (Atoms)
### Technical Standards (AI_ prefix)
- **Programming**: [[CONCEPT_AI_Agentic_Python_Standards]]
- **Reasoning**: [[CONCEPT_AI_Agent_Reasoning_Patterns]], [[CONCEPT_AI_Grounded_Generation]]
- **Architecture**: [[CONCEPT_AI_MultiAgent_Coordination]], [[ENTITY_TOOL_LangGraph]]
- **Infrastructure**: [[CONCEPT_AI_Context_Budgeting]], [[CONCEPT_AI_Agent_Memory_Architecture]]
- **Operations**: [[CONCEPT_AI_Tool_Design_Standards]], [[CONCEPT_AI_Production_Readiness_for_Agents]], [[ENTITY_TOOL_Agent_Observability_Stack]]

### Legacy/Specific Patterns (AIMET_ prefix)
- [[CONCEPT_AIMET_ReAct_Pattern]] | **ReAct Pattern** — Reasoning + Acting loop.
- [[CONCEPT_AIMET_Memory_Management]] | **Memory Management** — Short/Long-term, Checkpointing.
- [[CONCEPT_AIMET_RAG_Systems]] | **RAG Systems** — Vector Stores, Embeddings.
- [[CONCEPT_AIMET_Tool_Integration]] | **Tool Integration** — Custom Tools, Pydantic schemas.
- [[CONCEPT_AIMET_MultiAgent_Architecture]] | **Multi-Agent Architecture** — Supervisor patterns.
- [[CONCEPT_AIMET_LCEL]] | **LCEL** — LangChain Expression Language.
- [[CONCEPT_AIMET_Runnables]] | **Runnables** — Standard Execution Units.
- [[CONCEPT_AIMET_Error_Handling_Patterns]] | **Error Handling Patterns**.

## ## Source Tracing
- **Gốc**: `3-resources/raw/sources/RAW_PDF_Agentic_AI_Roadmap.md`
- **File gốc (.pdf)**: `AIMET_Complete_Roadmap_to_Become_an_Agentic_AI_Engineer.pdf`
- **Nội dung**: Bao gồm 11 chương từ Python Fundamentals đến Production Readiness.
- **Phân tích bổ sung**: Tài liệu 23 trang của Lamhot Siagian (2026) cấu trúc lộ trình học "foundation-first".


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
