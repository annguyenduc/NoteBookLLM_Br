---
file_id: "ATOMS_Servo_Motor"
title: "Động cơ Servo"
category: "Atomic Note"
prefix: "ATOMS"
tags: ["Hardware", "Arduino", "Actuator"]
source: "[[LMS_KB_IOT_NORMALIZED.md]]"
status: "draft"
created: "2026-04-13"
last_updated: "2026-04-13"
---

# Động cơ Servo

## 📌 Định nghĩa cốt lõi
Động cơ Servo là một thiết bị đầu ra (actuator) có khả năng xoay và duy trì vị trí trục ở các góc xác định (thường từ 0-180 độ) dựa trên tín hiệu điều khiển PWM (Pulse Width Modulation).

## 🔍 Chi tiết kỹ thuật
<!-- COPY NGUYÊN VĂN từ nguồn — KHÔNG paraphrase -->
- **Fact 1:** Động cơ Servo là một thiết bị đầu ra (output), hoạt động ở điện áp 5V, có 3 dây kết nối (Tín hiệu, VCC, GND).
- **Fact 2:** Động cơ Servo: Dây màu cam là dây tín hiệu, phải được kết nối với các chân Digital có hỗ trợ PWM (ký hiệu dấu ~) trên Arduino như: 3, 5, 6, 9, 10, 11.
- **Fact 3:** Sơ đồ dây động cơ Servo: Dây màu cam là dây tín hiệu (nối chân Digital 2-13), dây màu đỏ là dây nguồn (nối chân 5V), dây màu nâu/đen nối chân GND.
- **Fact 4:** Thứ tự dây Servo tiêu chuẩn: Dây nâu (GND), dây đỏ (5V), dây cam (Tín hiệu - Digital PWM).
- **Fact 5:** Động cơ Servo tiêu chuẩn có 3 dây màu quy ước: Đỏ (Nguồn VCC), Nâu/Xám/Đen (Cực âm GND), và Vàng/Cam (Tín hiệu điều khiển).
- **Fact 6:** Động cơ Servo có 3 dây tín hiệu đặc trưng: dây đỏ (nguồn VCC), dây nâu/xám/đen (đất GND) và dây vàng/cam (tín hiệu Signal).
- **Fact 7:** Động cơ Servo có quy định màu dây chuẩn: chân nguồn (màu đỏ), chân đất (màu nâu/đen) và chân tín hiệu (màu vàng/cam).

## 💡 Ví dụ thực tế
Trong dự án "Thùng rác thông minh", động cơ Servo được lập trình để tự động mở nắp thùng một góc 90 độ khi cảm biến siêu âm phát hiện có người đứng trước thùng rác trong khoảng cách 20cm, và đóng lại sau 3 giây.

## 🔗 Liên kết tư duy
- Nguồn cấp cho động cơ: [[ATOMS_Arduino_Power]]
- Kết nối qua mạch mở rộng: [[ATOMS_Breadboard]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Thiết bị đầu ra, nguồn 5V, quay 0-180 độ. Dây chuẩn: Nâu (GND), Đỏ (VCC), Cam (Tín hiệu). |
| **Feelings** | Học sinh thường lúng túng khi phân biệt 3 màu dây và hay cắm nhầm chân tín hiệu vào các chân Digital không có ký hiệu dấu "~" (PWM). |
| **Findings** | Servo cho phép kiểm soát vị trí chính xác nhờ hệ thống phản hồi bên trong; tuy nhiên cần nguồn 5V ổn định từ Jack DC nếu dùng nhiều servo cùng lúc để tránh sụt áp. |
| **Futures** | Ứng dụng để thiết kế cánh tay robot, điều khiển bánh lái tàu thủy hoặc các cơ cấu gương chiếu hậu thông minh cho xe. |

## 📖 Nguồn
`📖 Nguồn: brain/raw/LMS_KB_IOT_NORMALIZED.md — tag [Servo_Motor]`

---
<!-- ATOM CHECKLIST — @librarian verify trước khi đổi status: verified -->
- [ ] Chỉ có 1 khái niệm duy nhất trong file này
- [ ] Có ít nhất 2 [[wikilinks]]
- [ ] Phần Futures không để trống
- [ ] Nguồn có thể trace về brain/raw/
- [ ] Facts là copy nguyên văn, không paraphrase
