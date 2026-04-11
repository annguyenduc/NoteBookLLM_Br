# Implementation Plan: AI High School Curriculum Map (Prompt Engineering Focus)

Kế hoạch này tái định hướng khung giảng dạy AI THPT, lấy **Prompt Engineering** làm kỹ năng cốt lõi "xuyên suốt", loại bỏ phần cứng để tập trung vào năng lực giao tiếp và cộng tác với AI.

## User Review Required

> [!IMPORTANT]
> - **Kỹ năng xuyên suốt**: Prompt Engineering không chỉ là một bài học, mà là phương thức thực hiện mọi bài tập trong chương trình.
> - **Lộ trình phân bậc**: Từ V-N-N (Lớp 10) -> CREATE/CoT (Lớp 11) -> AI Agents/Second Brain (Lớp 12).
> - **Loại bỏ phần cứng**: Tạm thời gỡ bỏ các module IoT/Arduino để tối ưu hóa thời lượng cho Generative AI.

## Proposed Changes

### [brain/distilled](file:///d:/NoteBookLLM_Br/brain/distilled)

#### [NEW] [AI_THPT_Prompt_Engineering_Map.md](file:///d:/NoteBookLLM_Br/brain/distilled/AI_THPT_Prompt_Engineering_Map.md)
- **Cấu trúc khung**:
    - **Lớp 10 (Foundation)**: AI Literacy, Khung V-N-N, AI Gia sư (Socratic Method).
    - **Lớp 11 (Advanced)**: Kỹ thuật CREATE, Chain-of-Thought (CoT), Few-shot Prompting.
    - **Lớp 12 (Personal Systems)**: AI Agents (ReAct), Xây dựng Second Brain/Wiki cá nhân, Đạo đức & Tương lai nghề nghiệp.
- **Tiêu chí đánh giá**: Sử dụng **Prompt Quality Rubric** (đã có trong Wiki).

#### [MODIFY] [Education_AI_Handbook.md](file:///d:/NoteBookLLM_Br/brain/distilled/Education_AI_Handbook.md)
- Cập nhật mục THPT để phản ánh trọng tâm mới về Prompt Engineering.

## Open Questions

> [!NOTE]
> 1. **Môn học tích hợp**: Bạn có muốn tôi thiết kế các ví dụ Prompt Engineering mẫu cho từng môn học cụ thể (Toán, Văn, Anh) ngay trong khung giảng dạy lớp 10 không?
> 2. **Công cụ ưu tiên**: Chúng ta sẽ mặc định sử dụng ChatGPT/Gemini hay các công cụ mã nguồn mở qua 9Router để học sinh thực hành?

## Verification Plan

### Automated Tests
- Chạy `python scripts/brain_lint.py` để kiểm tra tính liên kết tri thức.
- @auditor đối soát nội dung với [Prompt_Engineering_Master.md](file:///d:/NoteBookLLM_Br/brain/distilled/Prompt_Engineering_Master.md).

### Manual Verification
- Người dùng kiểm tra tính khả thi của lộ trình phân bậc (10-11-12).
