---
title: "SYNTHESIS: Agentic Orchestration Frameworks (LangGraph vs CrewAI vs AutoGen)"
type: synthesis
tags: ["Agentic AI", "Comparison", "Frameworks", "Orchestration", "AIMET"]
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-02"
---

# Agentic Orchestration Frameworks

Trang này hợp nhất tri thức về các bộ khung (frameworks) hàng đầu để xây dựng hệ thống Multi-Agent, dựa trên lộ trình kỹ thuật năm 2026.

## ⚖️ 1. Ma trận so sánh (Decision Matrix)

| Tiêu chí | [[ENTITY_AIMET_LangGraph|LangGraph]] | [[ENTITY_AIMET_CrewAI|CrewAI]] | [[ENTITY_TOOL_LangChain|LangChain]] |
|---|---|---|---|
| **Mô hình chính** | State Machine (Graph) | Role-based (Crew) | Chains (Sequential) |
| **Độ kiểm soát** | Tối đa (Explicit Edges) | Trung bình (Opinionated) | Thấp (Implicit) |
| **Độ phức tạp** | Cao | Thấp | Trung bình |
| **Lý tưởng cho** | Production, Long-running | Rapid Prototyping | Standard RAG |

## 🧩 2. Các Pattern tích hợp (Rule 3: Knowledge Compounding)

### Supervisor Pattern
Ứng dụng [[CONCEPT_AIMET_MultiAgent_Architecture]] để phân quyền. 
- Trong **LangGraph**, Supervisor là một node điều hướng (router).
- Trong **CrewAI**, Supervisor là một thuộc tính `manager_llm`.

### Memory & Persistence
- **LangGraph** dẫn đầu với cơ chế **Checkpointing** ([[CONCEPT_AIMET_Memory_Management]]), cho phép lưu trạng thái của toàn bộ đồ thị tri thức.
- **CrewAI** sử dụng bộ nhớ ngắn hạn và dài hạn dựa trên Vector Store ([[CONCEPT_AIMET_RAG_Systems]]).

## 🛠 3. Lộ trình triển khai (Best Practices)

1. **Giai đoạn 1**: Prototype bằng **CrewAI** để định hình các vai trò (Roles) và Tasks.
2. **Giai đoạn 2**: Nếu cần độ tin cậy cao và xử lý lỗi phức tạp, chuyển đổi sang **LangGraph** để model dưới dạng State Machine.
3. **Giai đoạn 3**: Tích hợp các công cụ chuyên biệt qua **Tool schemas** ([[CONCEPT_AIMET_Tool_Integration]]).

## 4. Production & Safety (The 2026 Mandate)
Để đưa các framework trên vào thực tế, hệ sinh thái 2026 bổ sung 2 lớp kiểm soát:
- **Security**: Áp dụng [[CONCEPT_AIMET_Production_Guardrails]] để ngăn chặn Prompt Injection và bảo vệ dữ liệu nhạy cảm thông qua cấu trúc Graph định hướng.
- **Evaluation**: Sử dụng [[CONCEPT_AIMET_Evaluation_Metrics]] (RAGAS, DeepEval) làm thước đo định lượng cho sự thành công của Agent, chuyển dịch từ đánh giá định tính sang kiểm định CI/CD tự động.

## 🔍 5. Trích dẫn nguồn (Rule 14)

- **Nguồn chính**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 4 & 5.
- **Nguồn bổ trợ**: [[ENTITY_AIMET_LangGraph]], [[ENTITY_AIMET_CrewAI]].
- **Fact-check**: Đã đối chiếu sự khác biệt giữa "deterministic workflows" và "conversational autonomy" (Roadmap 2026).

---
WRITE REPORT:
  file: "3-resources/wiki/synthesis/SYNTHESIS_Agentic_Orchestration_Frameworks.md"
  operation: "create"
  added: "TRIGGER: Synthesis Hook (>=3 sources). Hợp nhất tri thức frameworks."
  compliance: "Rule 3 & Rule 14 OK."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
