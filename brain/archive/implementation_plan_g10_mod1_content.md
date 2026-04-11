# Implementation Plan: Module 1 Content Design (Grade 10)

Kế hoạch này tập trung vào việc hiện thực hóa nội dung chi tiết cho **Module 1: Bản chất của Generative AI** dành cho học sinh lớp 10, đảm bảo tính sư phạm thực tiễn và chuyên sâu.

## User Review Required

> [!IMPORTANT]
> - **Cấu trúc 5E**: Nội dung sẽ được trình bày theo 5 bước (Engage, Explore, Explain, Elaborate, Evaluate).
> - **Nhiệm vụ thực hành**: Tập trung vào việc học sinh quan sát sự khác biệt giữa các tham số (Token, Temperature) và cách Gemini phản hồi.
> - **Nguồn tri thức**: Tuân thủ Rule 10, trích dẫn các khái niệm từ `optimized_part_1_v13.md` (về lựa chọn Model) và `Prompt_Engineering_Master.md`.

## Proposed Changes

### [brain/distilled](file:///d:/NoteBookLLM_Br/brain/distilled)

#### [NEW] [G10_Mod1_Generative_AI_Foundation.md](file:///d:/NoteBookLLM_Br/brain/distilled/G10_Mod1_Generative_AI_Foundation.md)
- **Engage**: Một ví dụ kích thích sự tò mò về khả năng sáng tạo của AI (Text-to-Art hoặc Chatbot Roleplay).
- **Explore**: Yêu cầu học sinh quan sát cách AI dự đoán từ tiếp theo qua một trò chơi nhỏ.
- **Explain**: Định nghĩa sâu về LLM, Tokens (mảnh ghép ngôn ngữ), và Cơ chế dự đoán (Probability). Giải thích về Ảo giác (Hallucination).
- **Elaborate**: Thảo luận về việc tại sao phải "Prompt Engineering" thay vì chỉ hỏi vu vơ.
- **Evaluate**: Checklist tự đánh giá các khái niệm đã học.

### [brain/distilled](file:///d:/NoteBookLLM_Br/brain/distilled)

#### [MODIFY] [AI_THPT_Prompt_Engineering_Map.md](file:///d:/NoteBookLLM_Br/brain/distilled/AI_THPT_Prompt_Engineering_Map.md)
- Cập nhật liên kết đến bài học chi tiết của Module 1.

## Open Questions

> [!NOTE]
> 1. **Độ sâu thực hành**: Bạn có muốn tôi đưa một vài bài tập kỹ thuật nhẹ về **Quantization** (Nén mô hình - trích từ nguồn raw) như một kiến thức đọc thêm không?
> 2. **Ví dụ môn học**: Tôi sẽ lồng ghép ví dụ về **Toán/Văn/Anh** ngay trong phần "Elaborate" để học sinh thấy tính ứng dụng sớm nhất. Đã được bạn đồng thuận ở turn trước.

## Verification Plan

### Automated Tests
- Chạy `python scripts/brain_lint.py` để kiểm tra link mới.
- @auditor kiểm tra tính chính xác của thuật ngữ so với nguồn raw.

### Manual Verification
- @ pm kiểm tra cấu trúc 5E.
