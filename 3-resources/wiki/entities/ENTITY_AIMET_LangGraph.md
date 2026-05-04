---
title: "ENTITY: LangGraph (Agent Orchestration Framework)"
type: entity
tags: ["Agentic AI", "Framework", "Graph-based", "LLM"]
status: "draft"
created: "2026-05-02"
relationships:
  - type: "part_of"
    target: "[[ENTITY_TOOL_LangChain]]"
  - type: "supports"
    target: "[[CONCEPT_AIMET_MultiAgent_Architecture]]"
---

# LangGraph

**LangGraph** là framework của LangChain để xây dựng agent workflows dưới dạng **state machine/graph**, giúp kiểm soát luồng logic của LLM agents một cách tường minh và có thể debug được.

## Đặc điểm cốt lõi

| Thuộc tính | Mô tả |
|---|---|
| **Paradigm** | Graph-based state machine (nodes + edges) |
| **Strength** | Checkpointing, retries, human-in-the-loop |
| **Best for** | Deterministic workflows, long-running agents |
| **vs CrewAI** | Explicit control vs opinionated role-based |
| **vs AutoGen** | Graph structure vs conversational chat patterns |

## Khi nào dùng LangGraph

- Cần **kiểm soát tường minh** từng bước của agent (explicit state transitions)
- Cần **checkpoint** để resume nếu agent crash giữa chừng
- Cần **human-in-the-loop** tại các boundary cụ thể
- Workflow phức tạp với nhiều nhánh và retry logic

## Anti-pattern cần tránh

> "Copy-pasting demo code và treating the framework as the architecture." (Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 4)

**Fix**: Dùng LangGraph để model domain logic, không phải dùng framework features để tránh viết domain logic.

## Liên kết

- [[CONCEPT_AIMET_MultiAgent_Architecture]] — orchestration patterns
- [[CONCEPT_AIMET_Memory_Management]] — checkpointing trong LangGraph
- [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — nguồn gốc

---
**Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 4 (Pick a Framework)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
