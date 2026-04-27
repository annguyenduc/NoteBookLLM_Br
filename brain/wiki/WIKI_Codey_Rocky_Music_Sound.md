---
file_id: "WIKI_Codey_Rocky_Music_Sound"
title: "Âm thanh và Nhạc trên Codey Rocky"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "CodeyRocky", "Output"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Âm thanh và Nhạc trên Codey Rocky

## 📌 Định nghĩa cốt lõi
Codey Rocky tích hợp một loa nhỏ cho phép phát các hiệu ứng âm thanh có sẵn hoặc chơi các nốt nhạc theo ý muốn của người lập trình.

## 🔍 Chi tiết kỹ thuật
### 1. Hiệu ứng âm thanh (Sound Effects):
- Robot có sẵn thư viện âm thanh đa dạng: tiếng cười (laugh), lời chào (hello), tiếng còi, tiếng thú vật...
- Có 2 chế độ phát:
  - **Phát âm thanh cho đến khi hết (Play sound until done)**: Robot sẽ phát xong âm thanh đó rồi mới thực hiện câu lệnh tiếp theo.
  - **Bắt đầu phát âm thanh (Start sound)**: Robot vừa phát âm thanh vừa thực hiện ngay câu lệnh tiếp theo (thích hợp cho các hành động song song).

### 2. Chơi nhạc (Music):
- Có thể chọn các nốt nhạc (C4, D4, E4...) và quy định thời gian phát (phần của giây hoặc số phách).

## 💡 Ví dụ thực tế
Lập trình cho robot: Khi khởi động, robot phát âm thanh 'hello' cho đến khi hết, sau đó mới bắt đầu di chuyển. Điều này giúp người dùng biết robot đã sẵn sàng.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_Codey_Rocky_System]]
- Liên quan trực tiếp: [[WIKI_Codey_LED_Matrix]], [[WIKI_Codey_Rocky_Movement]]
- Ứng dụng vào: [[WIKI_Codey_Musical_Performance]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Hỗ trợ phát âm thanh hệ thống và nốt nhạc tự do. Có chế độ chờ phát xong hoặc phát song song. |
| **Feelings** | Học sinh thường thắc mắc tại sao âm thanh bị cắt ngang (do dùng lệnh 'Start sound' liên tiếp mà không có lệnh chờ). |
| **Findings** | Việc kết hợp âm thanh với biểu cảm trên màn hình LED giúp robot giao tiếp hiệu quả hơn với con người. |
| **Futures** | Ứng dụng âm thanh để báo động trong các dự án nhà thông minh hoặc robot an ninh. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_Codey_de_trac_nghiem_1_-_codey_m1.md]] — Câu 17, 20`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file của trang Wiki này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 17: Phân biệt 'Start sound' và 'Play sound until done'; Câu 20: Kết hợp âm thanh với hiển thị màn hình LED).
