---
file_id: CONCEPT_TOOL_Context_Injection_Techniques
title: Context Injection Techniques (Kỹ thuật tiêm ngữ cảnh)
type: concept
status: VERIFIED
tags:
  - Wiki Page
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-03
last_updated: 2026-05-03
---

## ## For future Claude
Trang này định nghĩa các phương pháp tối ưu để đưa dữ liệu bên ngoài vào cửa sổ ngữ cảnh (Context Window) của LLM. Mục tiêu là tối đa hóa "Signal-to-Noise Ratio" (Tỷ lệ tín hiệu trên nhiễu), giúp mô hình tập trung vào thông tin quan trọng nhất mà không bị lạc lối trong các dữ liệu dư thừa.

## ## Key Claims / Summary
1.  **Structured Injection**: Sử dụng các ký tự phân tách rõ ràng (XML tags, Markdown headers) để bao bọc dữ liệu ngữ cảnh.
2.  **Strategic Placement**: Đặt thông tin quan trọng nhất ở đầu hoặc cuối prompt để tận dụng hiệu ứng "Lost in the Middle" (Mô hình thường chú ý tốt nhất ở 2 đầu).
3.  **Dynamic Pruning**: Chỉ tiêm các phần dữ liệu thực sự liên quan (thông qua RAG hoặc phân tích tiền xử lý) thay vì tiêm toàn bộ tài liệu.

## ## Ví dụ đối chiếu (R18)
-   **Ví dụ thực tế (Original)**: Sử dụng XML tags để tiêm code: `<SOURCE_CODE> [Nội dung code] </SOURCE_CODE>`. Điều này giúp Gemini phân biệt rõ đâu là chỉ dẫn của lập trình viên và đâu là dữ liệu cần được phân tích.
-   **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn gửi một tập hồ sơ cho sếp. Thay vì ném một đống giấy lộn xộn lên bàn, bạn kẹp chúng vào các bìa hồ sơ có dán nhãn màu sắc rõ ràng (XML tags) và đặt bản tóm tắt quan trọng nhất lên trên cùng (Strategic Placement). Việc này giúp sếp xử lý công việc nhanh và chính xác hơn rất nhiều.

## ## Detailed Analysis
Các kỹ thuật cụ thể:
- **XML Wrapper**: Cực kỳ hiệu quả với các dòng mô hình Claude và Gemini.
- **Variable Placeholder**: Sử dụng định dạng `{{CONTEXT_HERE}}` để tự động hóa việc tiêm dữ liệu từ code.
- **Reference Tagging**: Đánh số thứ tự cho các đoạn văn bản truy xuất được để LLM có thể trích dẫn ngược lại (Citations).
- **Summary Injection**: Thay vì tiêm 10 trang tài liệu, chỉ tiêm bản tóm tắt cực gọn được tạo ra từ một lượt LLM call trước đó.

## ## Relationships
- `part_of` -> [[CONCEPT_AI_Prompt_Engineering_Basics]]
- `enables` -> [[CONCEPT_AIMET_RAG_Systems]]
- `SOURCE_OF` -> [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]

## ## Source Tracing
- **Nguồn**: [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]] — Section 3: Context Management.
- **Nguồn**: SOURCE_META_KARPATHY_LLM_WIKI — Triết lý về "Low Friction" và "Contextual Recall".

## ## History / Revisions
- **2026-05-03**: [@engineer] Chuyển đổi từ stub sang verified, bổ sung R18 và Rule 20.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
