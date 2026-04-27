---
file_id: "WIKI_xBot_xController_Board"
title: "Mạch điều khiển xController"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "xBot", "Hardware"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Mạch điều khiển xController

## 📌 Định nghĩa cốt lõi
xController là bo mạch lập trình trung tâm của robot xBot, đóng vai trò tiếp nhận mã lệnh từ phần mềm và điều khiển các thiết bị ngoại vi như động cơ, cảm biến, đèn LED.

## 🔍 Chi tiết kỹ thuật
- **Nền tảng**: Tương thích với Arduino, mạnh mẽ và ổn định.
- **Cổng kết nối**:
  - **6 cổng mở rộng RJ**: Dùng để kết nối nhanh các module cảm biến/hiển thị.
  - **Cổng USB Type C**: Dùng để nạp code và giao tiếp Serial.
- **Linh kiện tích hợp sẵn**:
  - **Loa (Buzzer)**: Phát âm thanh và nhạc.
  - **Đèn LED RGB**: 2 đèn LED có thể đổi màu tùy ý (thường dùng báo hiệu hoặc trang trí).
  - **Cổng Motor**: Điều khiển trực tiếp 2 động cơ DC (M1, M2).
- **Lưu ý**: Mạch xController **không** tích hợp sẵn cảm biến siêu âm hay cảm biến dò line (các linh kiện này là module rời cắm vào cổng RJ).

## 💡 Ví dụ thực tế
Để tạo hiệu ứng đèn xe cảnh sát trên xBot, học sinh lập trình cho 2 đèn LED RGB trên mạch xController nháy luân phiên màu Đỏ và Xanh dương.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_xBot_System`
- Liên quan trực tiếp: `WIKI_OhStem_App_Software`, `WIKI_xBot_Line_Follower_V2`
- Ứng dụng vào: `WIKI_Robot_Brain_Function`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Mạch Arduino-based, có 2 LED RGB và 1 Buzzer tích hợp. 6 cổng RJ. |
| **Feelings** | Học sinh thường thích thú với việc chỉ cần 1 sợi dây USB-C duy nhất là có thể nạp code thay vì phải dùng nhiều loại dây cáp khác nhau. |
| **Findings** | Việc không tích hợp sẵn cảm biến giúp học sinh học được cách lắp ráp và cấu hình cổng RJ một cách chủ động. |
| **Futures** | Dùng để xây dựng các hệ thống nhúng (Embedded system) phức tạp hơn. |

## 📖 Nguồn
`📖 Nguồn: Robot_xBot_de_trac_nghiem_1_-_xbot.md — Câu 1, 4, 13, 20`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 1: 6 cổng mở rộng; Câu 4: Không tích hợp sẵn cảm biến siêu âm; Câu 13: Có 2 đèn LED RGB; Câu 20: Có loa tích hợp).
