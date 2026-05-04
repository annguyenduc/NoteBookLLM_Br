---
file_id: CONCEPT_TOOL_GEMINI_ROLE_PROMPTING
title: "Gemini Role Prompting (Persona Expert Design)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]"
  - "[[SOURCE_META_KARPATHY_LLM_WIKI]]"
---

## ## For future Claude
Trang này định nghĩa kỹ thuật thiết lập "Persona" (vai trò) cho Gemini để tối ưu hóa đầu ra theo domain cụ thể. Thay vì yêu cầu chung chung, Role Prompting ép mô hình vào một khung tư duy (Mental Framework) của chuyên gia. Đây là nền tảng để xây dựng các Agentic Workflows có độ chính xác cao.

## ## Key Claims / Summary
1.  **Expert Persona**: Việc gán vai trò chuyên gia (Senior Engineer, Auditor) giúp giảm tỷ lệ hallucination và tăng độ sâu của câu trả lời.
2.  **Constraint Enforcement**: Role Prompting không chỉ là "là ai" mà còn là "làm gì/không làm gì" (Constraints).
3.  **Context Alignment**: Giúp mô hình ưu tiên các bộ quy tắc cụ thể (ví dụ: Rule 17, Rule 20) trong quá trình thực thi.

## ## Ví dụ đối chiếu (Rule 17)
-   **Ví dụ thực tế (Original)**: `Bạn là một Senior Python Engineer với 10 năm kinh nghiệm. Hãy review đoạn code sau theo tiêu chuẩn PEP8 và tối ưu hóa Big O.`
-   **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc yêu cầu một người đeo "chiếc mặt nạ" của một chuyên gia trước khi bước vào phòng họp. Chiếc mặt nạ không chỉ thay đổi diện mạo mà còn thay đổi cả cách họ phát ngôn và hành xử để phù hợp với kỳ vọng của căn phòng đó.

## ## Detailed Analysis
Role Prompting trong Gemini 1.5 Pro và Flash tận dụng khả năng Long Context để duy trì Persona ổn định qua nhiều lượt chat. Các thành phần của một Role Prompt mạnh mẽ bao gồm:
- **Identity**: Tên vai trò, số năm kinh nghiệm, vị trí trong tổ chức.
- **Goal**: Mục tiêu tối thượng của vai trò này (ví dụ: "Đảm bảo code không có lỗi logic").
- **Knowledge Base**: Các tài liệu hoặc tiêu chuẩn mà vai trò này phải nắm rõ (ví dụ: "Am hiểu sâu sắc về AGENTS.md").
- **Communication Style**: Tông giọng (Professional, Concise, Vietnamese).

## ## Relationships
- `part_of` -> [[CONCEPT_AI_Prompt_Engineering_Basics]]
- `enables` -> [[CONCEPT_AIMET_MultiAgent_Architecture]]
- `source_of` -> [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]

## ## Source Tracing
- **Nguồn**: [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]] — Section 2: Role Prompting Patterns.
- **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Triết lý về "Low Friction" và "Expert persona".

## ## History / Revisions
- **2026-05-03**: [@engineer] Chuyển đổi từ stub sang verified, bổ sung Rule 17 và Rule 20.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
