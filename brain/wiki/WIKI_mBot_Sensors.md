---
file_id: "WIKI_mBot_Sensors"
title: "Hệ thống cảm biến mBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "mBot", "Sensor"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Hệ thống cảm biến mBot

## 📌 Định nghĩa cốt lõi
Hệ thống cảm biến giúp mBot có khả năng cảm nhận môi trường (ánh sáng, khoảng cách, vạch đen) để thực hiện các hành động tự động thông minh.

## 🔍 Chi tiết kỹ thuật
Các cảm biến chính của mBot:
1. **Cảm biến Siêu âm (Ultrasonic Sensor)**:
   - Tác dụng: Phát hiện vật cản và đo khoảng cách (đơn vị cm).
   - Kết nối: Cổng RJ 1, 2, 3 hoặc 4.
   - Nhóm lệnh: Sensor (Cảm biến). Trả về giá trị là một con số.
2. **Cảm biến Dò đường (Line Follower Sensor)**:
   - Tác dụng: Nhận diện vạch đen/trắng dựa trên nguyên lý hấp thụ/phản xạ tia hồng ngoại.
   - Cấu tạo: Gồm 2 mắt (Trái và Phải).
   - Kết nối: Cổng RJ 1, 2, 3 hoặc 4.
3. **Cảm biến Ánh sáng (Light Sensor)**:
   - Tác dụng: Đo độ sáng của môi trường.
   - Vị trí: Tích hợp sẵn trên bo mạch mCore.

**Quy trình xử lý logic:**
- Robot liên tục đọc giá trị từ cảm biến (Input) -> So sánh với điều kiện lập trình (Logic) -> Thực hiện hành động như di chuyển hoặc sáng đèn (Output).

## 💡 Ví dụ thực tế
Lập trình mBot di chuyển theo vật cản:
- Nếu khoảng cách < 15cm: Đi lùi.
- Nếu khoảng cách từ 15cm đến 30cm: Đứng yên.
- Nếu khoảng cách > 30cm: Đi tới.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_mBot_System]]
- Liên quan trực tiếp: [[WIKI_mCore_Board]], [[WIKI_mBot_Programming_and_Modes]]
- Ứng dụng vào: [[WIKI_mBot_Obstacle_Avoidance_Project]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Cảm biến siêu âm (cổng 1-4), cảm biến dò đường 2 mắt, cảm biến ánh sáng on-board. |
| **Feelings** | Học sinh thường cảm thấy thú vị nhất với cảm biến siêu âm vì nó giống như đôi mắt của robot. |
| **Findings** | Việc cắm sai cổng RJ so với khai báo trong code là lỗi phổ biến nhất khiến cảm biến không hoạt động. |
| **Futures** | Là nền tảng để hiểu về "Hệ thống tự hành" (Autonomous systems) trong thực tế. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_mBot_de_trac_nghiem_1_-_mon_mbot_m1_2.md]] — Câu 11, 12, 13, 26`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 11: Cổng RJ cho cảm biến siêu âm; Câu 12: Nguyên lý cảm biến dò đường; Câu 26: Di chuyển theo vật cản).
