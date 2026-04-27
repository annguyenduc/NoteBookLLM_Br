---
file_id: "WIKI_GBot_RGB_LED_Control"
title: "Điều khiển đèn LED RGB GBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "GBot", "Output"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Điều khiển đèn LED RGB GBot

## 📌 Định nghĩa cốt lõi
Vòng đèn LED RGB trên GBot là tập hợp các đèn LED có khả năng hiển thị nhiều màu sắc khác nhau, được dùng để thông báo trạng thái hoặc làm đẹp cho robot.

## 🔍 Chi tiết kỹ thuật
- **Vị trí**: Đèn LED được bố trí thành một vòng tròn trên mặt trên của robot.
- **Đánh số**: Các đèn LED được đánh số từ 0. Ví dụ: Đèn LED số 3 thường nằm ở vị trí góc phía trên (Vị trí A theo đề thi).
- **Điều khiển màu sắc**: Có thể lập trình từng đèn lẻ hoặc cả vòng đèn sáng các màu như Đỏ, Xanh lá, Xanh dương, Vàng, Trắng...
- **Chương trình**: Sử dụng khối lệnh "Set LED [số] color [màu]" trong GaraBlock.

## 💡 Ví dụ thực tế
Lập trình cho robot làm "xe cảnh sát" bằng cách cho đèn số 0 sáng màu đỏ, đèn số 1 sáng màu xanh dương và lặp lại liên tục.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_Programming_Modes`, `WIKI_GBot_Ultrasonic_Sensor`
- Ứng dụng vào: `WIKI_GBot_Light_Show_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Các đèn LED đánh số từ 0. Có thể chỉnh màu RGB cho từng đèn. |
| **Feelings** | Học sinh rất thích thú khi đổi màu đèn, đây là cách tốt để bắt đầu dạy về logic "vòng lặp" (loop). |
| **Findings** | Việc nạp nhiều lệnh đổi màu liên tiếp mà không có lệnh "Chờ" (Wait) sẽ khiến mắt người chỉ thấy được màu cuối cùng. |
| **Futures** | Dùng đèn LED để báo hiệu khi robot gặp vật cản hoặc khi hoàn thành một nhiệm vụ. |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 13, 14, 15`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 13: Vị trí đèn LED số 3; Câu 15: Nếu không có lệnh chờ thì đèn chỉ hiện màu cuối cùng).
