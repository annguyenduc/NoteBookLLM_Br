---
file_id: "ENTITY_AIMET_CrewAI"
title: "ENTITY: CrewAI (Role-based Multi-Agent Framework)"
type: entity
tags: ["Agentic AI", "Framework", "Multi-Agent", "Role-based"]
status: "draft"
created: "2026-05-02"
relationships:
  - type: "supports"
    target: "[[CONCEPT_AIMET_MultiAgent_Architecture]]"
  - type: "contradicts"
    target: "[[ENTITY_AIMET_LangGraph]]"
---

# CrewAI

**CrewAI** là framework multi-agent thiết kế theo mô hình **role-based collaboration** — mỗi agent có một "role" (researcher, writer, analyst...) và phối hợp với nhau để hoàn thành task phức tạp.

## Đặc điểm cốt lõi

| Thuộc tính | Mô tả |
|---|---|
| **Paradigm** | Role-based agent collaboration |
| **Strength** | Opinionated, dễ setup, natural language task assignment |
| **Best for** | Autonomous collaborative tasks, creative pipelines |
| **vs LangGraph** | Opinionated vs explicit graph control |
| **vs AutoGen** | Role-first vs conversation-first |

## Khi nào dùng CrewAI

- Task cần phân chia vai trò rõ ràng (researcher → writer → reviewer)
- Team cần prototype nhanh mà không cần explicit state machine
- Conversational autonomy quan trọng hơn deterministic control

## Liên kết

- [[CONCEPT_AIMET_MultiAgent_Architecture]] — supervisor patterns
- [[ENTITY_AIMET_LangGraph]] — so sánh trực tiếp
- [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — nguồn gốc

---
**Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 4 (Pick a Framework)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
