# Implementation Plan: AI High School Curriculum Framework (THPT)

Kế hoạch này hướng tới việc xây dựng một lộ trình đào tạo bài bản về AI cho học sinh THPT, kết hợp giữa tư duy lập trình mã nguồn mở (OSS) và các phương pháp sư phạm hiện đại.

## User Review Required

> [!IMPORTANT]
> - **Tiêu chuẩn Sư phạm**: Toàn bộ nội dung sẽ tuân thủ mô hình **5E** và quy trình **NASA EDP**.
> - **Chuyển đổi Công nghệ**: Nâng cấp từ lập trình kéo thả (mBlock) sang lập trình văn bản (Python) và tích hợp IoT.
> - **Nguồn gốc Tri thức**: Tuân thủ Rule 10 (Reverse Tracing) - chỉ trích dẫn từ các nguồn LMS đã xác thực trong repository.

## Proposed Changes

### [brain/distilled](file:///d:/NoteBookLLM_Br/brain/distilled)

#### [NEW] [AI_THPT_Curriculum_Map.md](file:///d:/NoteBookLLM_Br/brain/distilled/AI_THPT_Curriculum_Map.md)
- **Cấu trúc khung**: Chia thành 3 giai đoạn (Lớp 10: AI Literacy & Logic; Lớp 11: Machine Learning & Python; Lớp 12: Capstone Projects & Ethics).
- **Phân bổ năng lực**: Đối chiếu với UNESCO ICT CFT v3 (Knowledge Deepening).

#### [MODIFY] [Education_AI_Handbook.md](file:///d:/NoteBookLLM_Br/brain/distilled/Education_AI_Handbook.md)
- Cập nhật thêm các liên kết (cross-links) đến Khung giảng dạy mới.

### [libs/core](file:///d:/NoteBookLLM_Br/libs/core)

#### [NEW] [curriculum_engine.py](file:///d:/NoteBookLLM_Br/libs/core/curriculum_engine.py) (Tùy chọn)
- Một script hỗ trợ tự động kiểm tra tính nhất quán giữa nội dung bài học và Khung năng lực.

## Open Questions

> [!CAUTION]
> 1. **Phạm vi Module mẫu**: Bạn muốn tôi tập trung xây dựng chi tiết cho khối lớp nào trước (ví dụ: Lớp 10 - Nhập môn)?
> 2. **Tích hợp LLM**: Chúng ta có đưa nội dung **Prompt Engineering** vào như một kỹ năng xuyên suốt không?
> 3. **Phần cứng**: Bạn có ưu tiên sử dụng thiết bị phần cứng cụ thể nào (ví dụ: Arduino, ESP32, Yolo Bit) cho các dự án IoT & AI không?

## Verification Plan

### Automated Tests
- Chạy `python scripts/brain_lint.py` để đảm bảo tính toàn vẹn của liên kết trong Wiki.
- Sử dụng `@auditor` để đối soát ngược (Reverse Tracing) nội dung khung giảng dạy với `LMS_KB_AI_DEEP.md`.

### Manual Verification
- Người dùng kiểm tra cấu trúc 5E trong module mẫu đầu tiên.
