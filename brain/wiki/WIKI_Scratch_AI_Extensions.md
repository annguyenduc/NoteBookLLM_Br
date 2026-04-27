---
file_id: "WIKI_Scratch_AI_Extensions"
title: "Các nhóm lệnh mở rộng AI trong Scratch"
category: "Wiki Page"
prefix: "WIKI"
tags: ["KHMT", "AI_THCS", "Programming"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Các nhóm lệnh mở rộng AI trong Scratch

## 📌 Định nghĩa cốt lõi
Để thực hiện các chức năng thông minh, Scratch (phiên bản MIT AI) cung cấp các nhóm lệnh mở rộng (Extensions) cho phép lập trình viên tương tác với camera, âm thanh và các dịch vụ trí tuệ nhân tạo trực tuyến.

## 🔍 Chi tiết kỹ thuật
Các nhóm lệnh phổ biến:
1. **Text to Speech (Văn bản thành giọng nói)**:
   - `set voice to [ ]`: Chọn giọng đọc (nữ cao, nam trầm, khổng lồ...).
   - `set language to [ ]`: Chọn ngôn ngữ đọc.
   - `speak [ ]`: Phát âm thanh nội dung văn bản.
2. **Translate (Dịch thuật)**:
   - `translate [ ] to [ ]`: Dịch một từ/câu sang ngôn ngữ mục tiêu.
   - `viewer language`: Trả về ngôn ngữ của trình duyệt người dùng.
3. **Face Sensing (Nhận diện khuôn mặt)**:
   - Nhận diện các điểm landmarks trên mặt (mắt, mũi, miệng).
   - `go to [nose]`: Đưa nhân vật đến vị trí mũi của người dùng trên camera.
4. **Hand Sensing (Nhận diện bàn tay)**:
   - Xác định tọa độ các ngón tay (ngón cái, ngón trỏ...).
   - Thường dùng trong các trò chơi tương tác như chém hoa quả bằng tay.

**Lưu ý**: Một số extension yêu cầu bật Camera (Video Sensing) để có thể hoạt động đồng bộ.

## 💡 Ví dụ thực tế
Lập trình ứng dụng "Thông dịch viên": Người dùng nhập từ tiếng Việt -> Robot dịch sang tiếng Anh -> Robot đổi giọng sang tiếng Anh và phát âm từ đó.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_AI_THCS_System]]
- Liên quan trực tiếp: [[WIKI_AI_THCS_Software_MIT_Scratch]], [[WIKI_Machine_Learning_Teachable_Machine]]
- Ứng dụng vào: [[WIKI_Face_Filter_Project]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Text to speech (đọc văn bản), Translate (dịch thuật), Face/Hand sensing (nhận diện cơ thể). |
| **Feelings** | Học sinh thường rất hào hứng khi thấy nhân vật trên màn hình có thể "đeo" được cái mũ đúng vị trí trên đầu mình qua camera. |
| **Findings** | Các câu lệnh này hoạt động tốt nhất khi có kết nối mạng ổn định và ánh sáng môi trường đủ tốt cho camera. |
| **Futures** | Ứng dụng để tạo ra các app hỗ trợ người khiếm thị (đọc văn bản) hoặc người nước ngoài (dịch tức thời). |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/KHMT_AI_THCS_de_trac_nghiem_1_-_ai_thcs.md]] — Câu 1, 17, 19, 24, 25`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 17: Ý nghĩa các lệnh Translate/TTS; Câu 24: Nhận diện ngón tay; Câu 25: Đeo mũ bằng Face sensing).
