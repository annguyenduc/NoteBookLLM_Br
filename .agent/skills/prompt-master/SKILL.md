---
name: prompt-master
description: "Trình biên dịch và tối ưu hóa Prompt cho các công cụ AI. Tự động kích hoạt khi user yêu cầu viết, sửa, cải thiện hoặc điều chỉnh Prompt cho một công cụ AI cụ thể (LLMs, Cursor, Antigravity, Midjourney, Claude Code...). KHÔNG kích hoạt cho trò chuyện thông thường hay viết code/tài liệu."
---

# Prompt Master — Chuyên Gia Viết Prompt

## Khi Nào Dùng
- Viết prompt mới cho AI tool cụ thể
- Cải thiện prompt đang hoạt động kém
- Chuyển đổi prompt từ tool này sang tool khác
- Tối ưu hóa prompt để giảm token/tăng độ chính xác

## Quy Trình Chuẩn

### Bước 1 — Phân Tích Yêu Cầu
Trước khi viết, xác định:
- **Tool đích**: Claude, GPT, Gemini, Midjourney, Cursor, Antigravity IDE...?
- **Mục tiêu**: Output mong muốn là gì?
- **Ràng buộc**: Giới hạn token, format output, tone, ngôn ngữ?
- **Context**: Prompt sẽ dùng trong hệ thống nào (system prompt, user prompt, few-shot)?

### Bước 2 — Áp Dụng Kỹ Thuật Phù Hợp

| Kỹ thuật | Khi nào dùng |
|---|---|
| Chain-of-Thought (CoT) | Task cần suy luận nhiều bước |
| Few-shot examples | Output cần format/style cụ thể |
| Role assignment | Cần AI đóng vai chuyên gia |
| Output constraints | Cần control chặt format/độ dài |
| Negative examples | Tránh lỗi lặp lại |

### Bước 3 — Draft & Validate
1. Viết prompt đầu tiên
2. Kiểm tra: có ambiguous instruction không?
3. Test mentally: AI có thể hiểu sai ở đâu?
4. Tinh chỉnh

## Cấu Trúc Prompt Tốt
```
[ROLE/PERSONA] - Ai là AI trong context này?
[CONTEXT] - Background cần biết
[TASK] - Chính xác phải làm gì
[CONSTRAINTS] - Ràng buộc format/nội dung
[OUTPUT FORMAT] - Mẫu output mong muốn
[EXAMPLES] - (tùy chọn) few-shot examples
```

## Lỗi Phổ Biến
- Instruction mơ hồ ("viết hay hơn" → phải nói rõ "hay hơn" nghĩa là gì)
- Quá nhiều yêu cầu trong 1 prompt → tách thành nhiều prompt nhỏ
- Không specify output format → AI tự quyết → không nhất quán
- System prompt và user prompt mâu thuẫn nhau