# Implementation Plan: Module 2 - V-N-N Framework (Grade 10)

Kế hoạch này tập trung vào việc hiện thực hóa nội dung chi tiết cho **Module 2: Khung V-N-N (Vai trò - Nhiệm vụ - Ngữ cảnh)**, kỹ năng đặt lệnh cơ bản giúp học sinh lớp 10 làm chủ Gemini.

## User Review Required

> [!IMPORTANT]
> - **Tiêu chuẩn Swarm**: Toàn bộ nội dung sẽ được kiến tạo bởi Swarm Agents qua 9Router (Verified Traffic).
> - **Trọng tâm KHÔNG CỨNG**: Module này tập trung hoàn toàn vào kỹ năng tư duy ngôn ngữ và cấu trúc lệnh, không liên quan đến phần cứng hay lập trình kéo thả.
> - **Ứng dụng đa môn**: Tích hợp các ví dụ từ bảng `7. Thư viện Prompt mẫu & Chiến lược đa môn học` trong Wiki.

## Proposed Changes

### [brain/distilled](file:///d:/NoteBookLLM_Br/brain/distilled)

#### [NEW] [G10_Mod2_VNN_Framework.md](file:///d:/NoteBookLLM_Br/brain/distilled/G10_Mod2_VNN_Framework.md)
- **Engage**: Thử thách "Đoán ý đồng đội" giữa người và AI để thấy hậu quả của việc ra lệnh mơ hồ.
- **Explore**: Thử nghiệm thêm bớt các thành phần V, N, N vào một prompt đơn giản để quan sát sự thay đổi chất lượng phản hồi của Gemini.
- **Explain**: Định nghĩa sâu về Vai trò (Role), Nhiệm vụ (Task) và Ngữ cảnh (Context).
- **Elaborate**: Thực hành "Giải cấu trúc vấn đề" (Deconstruction) cho các bài toán hoặc bài văn thực tế.
- **Evaluate**: Checklist tự đánh giá chất lượng Prompt dựa trên Rubric chuẩn.

## Swarm Orchestration Sequence (Phase 2)

1. **@profiler** (Llama 70B): Trích xuất tinh hoa từ `Prompt_Engineering_Master.md` (lines 12-18, 103-122).
2. **@designer** (Qwen 32B): Thiết kế kịch bản sư phạm 5E cho V-N-N.
3. **@engineer** (Qwen Coder Plus): Biên soạn nội dung chi tiết bằng Tiếng Việt.

## Open Questions

> [!NOTE]
> 1. **Mức độ phức tạp**: Bạn có muốn giới thiệu sơ qua về **CoT (Chain-of-Thought)** ngay trong Module 2 này như một phần "Mở rộng" nâng cao cho học sinh khá giỏi không?
