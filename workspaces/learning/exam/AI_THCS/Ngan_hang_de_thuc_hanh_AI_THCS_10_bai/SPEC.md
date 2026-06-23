# Spec: Ngân hàng đề thực hành AI THCS 10 bài

## Mục tiêu

Tạo một ngân hàng 10 bài thực hành cho khóa `Trí tuệ nhân tạo Trung học cơ sở`, giữ đúng cấu trúc biên soạn của template thực hành để sau này có thể chọn ra 3 bài ghép thành đề kiểm tra cuối khóa.

## Nguồn tham chiếu

- `D:\NoteBookLLM_Br\workspaces\learning\exam\[Template] Bài kiểm tra cuối khóa.md`
- `D:\NoteBookLLM_Br\workspaces\learning\exam\GV-HO-AI-KT-Tri tue nhan tao Trung hoc co so.md`
- `D:\NoteBookLLM_Br\workspaces\learning\exam\TEMPLATE_HUONG_DAN_DU_AN.md`
- Bản nháp gốc: `D:\NoteBookLLM_Br\workspaces\learning\exam\AI_THCS\Bai_kiem_tra_thuc_hanh_AI_THCS.md`

## Phạm vi đầu ra

- 1 file markdown ngân hàng đề 10 bài.
- 1 thư mục media đi kèm.
- 1 bộ tài liệu nội bộ gồm spec, plan, checklist và readme.

## Chuẩn nội dung phải giữ

Mỗi bài phải giữ đủ 5 mục theo template:

1. Nội dung đề bài
2. Yêu cầu kỹ thuật chi tiết
3. Sản phẩm yêu cầu bàn giao
4. Đáp án gợi ý
5. Tiêu chí chấm điểm

## Chuẩn định vị tài liệu

- Tài liệu này được định vị là `ngân hàng đề`.
- Không tự nhận là `đề thi cuối khóa` hoàn chỉnh.
- Khi xuất bản đề cuối khóa chính thức, chỉ chọn 3 bài và đưa sang template cuối khóa.

## Đánh giá khả thi kỹ thuật

| Bài | Mức khả thi | Nhận định kỹ thuật ngắn |
| :---: | :---: | :--- |
| BT1 | Khả thi cao | Translate + TTS + biến điểm/vòng lặp là tổ hợp cơ bản, làm được ổn định. |
| BT2 | Khả thi cao | Truyện tương tác nhiều cảnh dùng backdrop, costume, broadcast, TTS và Translate phù hợp với Scratch-style blocks. |
| BT3 | Khả thi cao | Bài toán nhiều nhánh điều kiện, list lịch sử và TTS là logic lập trình cơ bản, dễ kiểm chứng. |
| BT4 | Khả thi cao | Quiz 5 câu với list, broadcast, Translate, TTS là trong phạm vi công cụ. |
| BT5 | Khả thi có điều kiện | Phụ thuộc webcam và độ ổn định nhận diện cảm xúc; nên dùng tiêu chí chấm quan sát được thay vì kỳ vọng độ chính xác tuyệt đối. |
| BT6 | Khả thi có điều kiện | Body Sensing làm được nếu không gian quay đủ rộng và webcam nhận đủ khung người. |
| BT7 | Khả thi trung bình-khá | Tổ hợp nhiều extension cùng lúc khả thi, nhưng cần giới hạn số trạng thái và thứ tự xử lý để tránh xung đột tương tác. |
| BT8 | Khả thi có điều kiện | Face Sensing + tính điểm làm được, nhưng cần yêu cầu ánh sáng đủ và tốc độ phản hồi chấp nhận được. |
| BT9 | Khả thi trung bình-khá | Body Sensing + Translate + TTS phù hợp, nhưng cần mô tả sản phẩm rõ để tránh rubric mơ hồ. |
| BT10 | Khả thi có điều kiện cao | Teachable Machine làm được nếu chuẩn bị sẵn nhãn/lớp dữ liệu, thống nhất quy trình train và kiểm tra môi trường camera. |

## Quyết định về plugin và test tự động

- Không cần cài plugin Playwright để hoàn thành nội dung ngân hàng đề.
- Nếu sau này cần test bản HTML hoặc thao tác giao diện LMS, Playwright chỉ nên dùng cho smoke test giao diện, không thay thế được việc kiểm tra hành vi AI theo webcam.

## Tiêu chí hoàn thành

- Đủ 10 bài.
- Mỗi bài đủ 5 mục đúng format.
- Media đi kèm đủ để tham chiếu từng bài.
- Tên thư mục không trùng và phản ánh rõ đây là ngân hàng đề.
