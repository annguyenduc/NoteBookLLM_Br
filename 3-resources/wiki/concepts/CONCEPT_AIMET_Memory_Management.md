---
file_id: "WIKI_CONCEPT_AIMET_MEMORY_MANAGEMENT"
title: "Memory Management trong Agentic AI Systems"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Agentic AI", "Memory", "Checkpointing", "AIMET"]
source: "SOURCE_AIMET_AgenticAI_Roadmap_2026"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# Memory Management trong Agentic AI Systems

Quản lý bộ nhớ là khả năng lưu trữ, truy xuất và nén thông tin để Agent duy trì ngữ cảnh trong thời gian dài.

## Core Principle
Hệ thống bộ nhớ Agent được chia làm ba loại chính dựa trên thời gian tồn tại và khả năng truy cập:

| Loại | Storage | Scope | Dùng khi |
|---|---|---|---|
| **Short-term** | In-memory (Conversation History) | 1 session | Chat context, tool call history |
| **Long-term** | Vector DB (Pinecone, Chroma) | Cross-session | User preferences, past interactions |
| **Checkpointing** | DB snapshot (LangGraph) | Task-level | Long tasks có thể bị interrupt, resume sau lỗi |

**Nguyên tắc cốt lõi**: Sử dụng **structured state** (typed dict/Pydantic model) làm "source of truth" chính xuyên suốt đồ thị (graph) — tránh việc chỉ dựa vào conversation history không cấu trúc.

## Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ tài liệu (Original)
Khi Context Window bị đầy, áp dụng **Context Budgeting**: Ví dụ, giới hạn 30% cho tài liệu truy xuất, 20% cho tóm tắt bộ nhớ. Khi vượt quá, hệ thống sẽ tự động tóm tắt (summarize) hoặc loại bỏ các nội dung ít giá trị để nhường chỗ cho các chỉ dẫn cốt lõi.
*Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 6, trang 13-14*

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng một học sinh đang ôn thi:
- **Bộ nhớ ngắn hạn:** Là những gì học sinh đang nhẩm trong đầu khi làm bài thi.
- **Bộ nhớ dài hạn:** Là các cuốn sách giáo khoa và vở ghi chép trên giá sách.
- **Checkpointing:** Lưu "bài học đang dang dở" nếu học sinh thoát giữa chừng, hôm sau resume đúng điểm dừng.

## Liên kết tư duy
- [[CONCEPT_AIMET_MultiAgent_Architecture]]
- [[ENTITY_AIMET_LangGraph]]

## 4F Reflection
- **Facts:** Tóm tắt (Summaries) tốt cho việc nhớ "chuyện gì đã xảy ra", còn Embeddings tốt cho việc "tìm kiếm tri thức chi tiết".
- **Feelings:** Memory architecture thường bị underdesigned trong MVP, gây vấn đề lớn khi scale và làm mất lòng tin người dùng nếu Agent "quên" quá nhanh.
- **Findings:** Pattern tốt nhất: structured state làm primary truth, conversation history chỉ đóng vai trò là "log".
- **Futures:** Tích hợp với [[CONCEPT_AIMET_RAG_Systems]] để long-term memory có thể được truy xuất thông minh theo ngữ nghĩa.

---
Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 6 (Memory Management)
Xác nhận Rule 14 từ MarkItDown Conversion (2026-05-03).
