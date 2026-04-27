---
file_id: "WIKI_GBot_Ultrasonic_Sensor"
title: "Cảm biến siêu âm GBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "GBot", "Sensor"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Cảm biến siêu âm GBot

## 📌 Định nghĩa cốt lõi
Cảm biến siêu âm (Ultrasonic Sensor) là thiết bị đo khoảng cách bằng cách phát ra sóng siêu âm và đo thời gian sóng phản hồi lại từ vật cản.

## 🔍 Chi tiết kỹ thuật
- **Cấu tạo**: Gồm 1 đầu phát (Trig) và 1 đầu thu (Echo) nhìn giống như hai mắt của robot.
- **Phạm vi hoạt động hiệu quả**: Từ 0cm đến khoảng 100cm (theo tài liệu GBot).
- **Nguyên lý**: Phát sóng -> Chạm vật cản -> Phản xạ -> Thu sóng -> Tính toán khoảng cách.
- **Kết nối**: Thường được kết nối với bộ não GBot thông qua một bo mạch chuyển đổi (Adapter) và cắm vào các cổng RJ (thường là cổng số 3 hoặc 4).

## 💡 Ví dụ thực tế
Trong dự án "Robot tránh vật cản", nếu khoảng cách từ cảm biến siêu âm đến vật cản nhỏ hơn 10cm, robot sẽ được lập trình để dừng lại hoặc rẽ trái để không va chạm.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_Brain_Ports`, `WIKI_GBot_Movement_Commands`
- Ứng dụng vào: `WIKI_GBot_Obstacle_Avoidance_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Phát hiện vật cản 0-100cm. Có 1 đầu phát và 1 đầu thu. |
| **Feelings** | Học sinh hay nhầm lẫn cảm biến này với "mắt" (camera) và nghĩ nó có thể nhận diện màu sắc (thực tế nó chỉ thấy khoảng cách). |
| **Findings** | Khoảng cách an toàn tối ưu cho robot di chuyển trong lớp học là 10-20cm. |
| **Futures** | Ứng dụng trong các bài toán tự hành, dừng khẩn cấp hoặc giữ khoảng cách an toàn. |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 22, 30`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 22: phạm vi 0-100cm, gồm 1 đầu phát và 1 đầu thu).
