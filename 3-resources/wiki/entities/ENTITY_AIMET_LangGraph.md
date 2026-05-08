---
file_id: ENTITY_AIMET_LangGraph
title: LangGraph (Agentic Orchestration)
type: entity
status: DRAFT
tags: 
ai-first: true
confidence: 0.85
last_reconciled: 2026-05-08
created: 2026-05-08
last_updated: 2026-05-08
---

# ENTITY_AIMET_LangGraph

> [!NOTE]
> LangGraph là một thư viện xây dựng trên nền tảng [[ENTITY_TOOL_LangChain|LangChain]], cho phép tạo ra các luồng công việc có chu trình (cyclic) cho AI Agents.

## Đặc điểm cốt lõi
1. **Persistence**: Lưu trữ trạng thái (State) của cuộc hội thoại một cách bền vững.
2. **Cyclic Graphs**: Khác với chuỗi (Chain) tuyến tính, LangGraph cho phép Agent quay lại các bước trước đó để sửa lỗi hoặc lặp lại tác vụ.
3. **Human-in-the-loop**: Tích hợp các điểm dừng để con người phê duyệt hoặc can thiệp vào quy trình của Agent.

## Mối liên hệ
- Xây dựng trên: [[ENTITY_TOOL_LangChain]].
- Đối thủ: [[ENTITY_AIMET_CrewAI]], [[ENTITY_AIMET_AutoGen]].
- Ngôn ngữ: [[ENTITY_PYTHON|Python]].

## 4F Reflection
- **Facts**: Phát triển bởi nhóm LangChain để giải quyết bài toán State Management phức tạp.
- **Feelings**: Khó học hơn Chain thông thường nhưng quyền năng hơn gấp bội.
- **Findings**: Khả năng "Self-healing" (tự sửa lỗi) của Agent được tối ưu hóa nhờ cấu trúc Graph.
- **Futures**: Tiêu chuẩn vàng cho Agentic AI trong doanh nghiệp.
