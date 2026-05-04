---
file_id: "WIKI_CONCEPT_AIMET_REACT_PATTERN"
title: "ReAct Pattern (Reasoning + Acting)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Agentic AI", "ReAct", "Reasoning", "Planning", "AIMET"]
source: "SOURCE_AIMET_AgenticAI_Roadmap_2026"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# ReAct Pattern (Reasoning + Acting)

ReAct là một mẫu thiết kế (Design Pattern) nơi Agent xen kẽ giữa việc suy luận (Reasoning) và thực hiện hành động (Acting) thông qua các công cụ.

## Core Principle
Bản chất của ReAct là tạo ra một vòng lặp:
**Thought (Suy nghĩ) -> Action (Hành động) -> Observation (Quan sát)**.

1. **Thought:** Agent phân tích tình huống hiện tại và lập kế hoạch cho bước tiếp theo.
2. **Action:** Agent gọi một công cụ (Tool call) hoặc thực hiện một thao tác.
3. **Observation:** Agent nhận kết quả từ hành động và dùng nó để cập nhật suy luận cho vòng lặp tiếp theo.

Cơ chế này cải thiện tính xác thực (Factuality) vì Agent có thể tra cứu thông tin thay vì tự đoán (Hallucination).

## Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ tài liệu (Original)
Một Agent nhận câu hỏi: "Ai là tổng thống hiện tại của Brazil?".
- **Thought:** Tôi cần biết ngày hiện tại và tra cứu danh sách tổng thống Brazil.
- **Action:** Gọi công cụ `web_search`.
- **Observation:** Kết quả trả về là Luiz Inácio Lula da Silva.
- **Thought:** Tôi đã có thông tin.
- **Final Answer:** Luiz Inácio Lula da Silva.
*Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 9.1*

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng một người thợ xây đang xây tường:
- **Reason (Suy luận):** Nhìn bản vẽ và kiểm tra độ phẳng của hàng gạch vừa xây.
- **Act (Hành động):** Đặt viên gạch tiếp theo và gõ nhẹ để căn chỉnh.
- **Observe (Quan sát):** Dùng thước thăng bằng để kiểm tra lại. Nếu gạch bị lệch (Observation), người thợ lại suy luận cách chỉnh (Reason) và tiếp tục hành động.

## Liên kết tư duy
- [[CONCEPT_AIMET_MultiAgent_Architecture]]

## 4F Reflection
- **Facts:** ReAct giúp giải quyết các bài toán "Reasoning-heavy" nơi thông tin không có sẵn trong tham số mô hình.
- **Feelings:** Việc quan sát Agent tự "suy nghĩ" và sửa sai thông qua các bước Thought-Action-Observation mang lại cảm giác minh bạch (Explainability) cao hơn.
- **Findings:** Thách thức kỹ thuật lớn nhất của ReAct là kiểm soát vòng lặp vô tận (Infinite loops) và sự tiêu tốn Token (Context growth).
- **Futures:** Kết hợp với **Planning & Execution separation** để tăng tính an toàn trước khi thực hiện các hành động có rủi ro cao.

---
Nguồn: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 9
Xác nhận Rule 14 từ MarkItDown Conversion (2026-05-03).
