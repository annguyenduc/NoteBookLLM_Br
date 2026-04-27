---
file_id: "WIKI_GBot_GaraBlock_Software"
title: "Phần mềm GaraBlock"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Software", "GBot", "Programming"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Phần mềm GaraBlock

## 📌 Định nghĩa cốt lõi
GaraBlock là môi trường lập trình kéo thả (Block-based programming) được phát triển riêng cho dòng robot GBot, giúp người dùng chuyển đổi các logic tư duy thành mã lệnh máy tính một cách trực quan.

## 🔍 Chi tiết kỹ thuật
- **Nền tảng**: Dựa trên Scratch 3.0, hỗ trợ cả phiên bản trên máy tính và ứng dụng di động.
- **Tính năng chính**:
  - Giao diện kéo thả các khối lệnh màu sắc.
  - Tích hợp sẵn thư viện (Extension) dành riêng cho GBot Creator.
  - Khả năng nạp code trực tiếp xuống bo mạch Arduino Uno.
- **Quy trình kết nối**:
  1. Thêm Extension "01: G-Robot Creator".
  2. Chọn Boards: "Arduino Uno".
  3. Kết nối (Connect) qua cổng Serial Port (COM).
  4. Nạp code bằng nút "Upload to Arduino".

## 💡 Ví dụ thực tế
Để nạp code, học sinh mở GaraBlock, chọn đúng cổng COM của robot, kéo lệnh "Khi khởi động" ghép với lệnh "Tiến tới", sau đó nhấn nút nạp màu xanh.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_Programming_Modes`, `WIKI_GBot_Movement_Commands`
- Ứng dụng vào: `WIKI_Robotics_Programming_Fundamentals`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Phần mềm lập trình kéo thả cho GBot, dựa trên Scratch. |
| **Feelings** | Học sinh thường bối rối khi không tìm thấy khối lệnh robot (do chưa thêm Extension "G-Robot Creator"). |
| **Findings** | Việc ẩn sân khấu (Hide stage layout) giúp không gian kéo thả rộng rãi và tập trung hơn cho việc lập trình robot. |
| **Futures** | Bước đệm hoàn hảo để học sinh chuyển từ tư duy hình ảnh sang tư duy mã nguồn (C/C++). |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 10, 11`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 10: Phần mềm GaraBlock; Câu 11: Quy trình thêm extension và nạp code).
