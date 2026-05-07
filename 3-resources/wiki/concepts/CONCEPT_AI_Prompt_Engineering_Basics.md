---
file_id: CONCEPT_AI_PROMPT_ENGINEERING_BASICS
title: "Prompt Engineering Basics (Cơ bản về kỹ nghệ gợi nhắc)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]"
  - "SOURCE_META_KARPATHY_LLM_WIKI"
---

## ## For future Claude
Trang này định nghĩa các nguyên tắc cơ bản của Prompt Engineering - nghệ thuật giao tiếp hiệu quả với LLM. Bằng cách cấu trúc chỉ dẫn một cách khoa học, chúng ta có thể điều khiển hành vi của mô hình, giảm thiểu sai sót và tối ưu hóa chất lượng output cho các tác vụ cụ thể.

## ## Key Claims / Summary
1.  **Instruction Clarity**: Chỉ dẫn càng rõ ràng, kết quả càng chính xác. Tránh các yêu cầu mơ hồ.
2.  **Context Injection**: Cung cấp đủ ngữ cảnh cần thiết để mô hình hiểu được phạm vi công việc.
3.  **Iterative Refinement**: Prompt Engineering là một quá trình thử nghiệm và tinh chỉnh liên tục.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng kỹ thuật "Few-shot prompting" bằng cách đưa ra 3 ví dụ về cách phân loại cảm xúc (Tích cực, Tiêu cực, Trung lập) trước khi yêu cầu LLM phân loại một câu mới. Điều này giúp mô hình hiểu đúng định dạng mong muốn.
- **Ẩn dụ sư phạm (Pedagogical)**: [Phóng tác] Giống như việc bạn dạy một đứa trẻ làm việc nhà. Thay vì nói "Hãy dọn phòng đi" (Zero-shot), bạn làm mẫu cho nó: "Đây là cách gấp chăn, đây là cách xếp đồ chơi vào giỏ" (Few-shot). Đứa trẻ sẽ hiểu nhanh và làm đúng hơn nhiều.

## ## Source Tracing
- **Nguồn**: [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]] — Section 2: Basic Prompting.
- **Nguồn**: SOURCE_META_KARPATHY_LLM_WIKI — Concept: Prompt as a Program.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
