---
file_id: "WIKI_GBot_Brain_Ports"
title: "Cổng kết nối bộ não GBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "GBot", "Hardware"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Cổng kết nối bộ não GBot

## 📌 Định nghĩa cốt lõi
Bộ não GBot (Controller) được thiết kế với các cổng kết nối chuyên dụng để người dùng dễ dàng gắn các linh kiện điện tử (động cơ, cảm biến) mà không cần hàn mạch.

## 🔍 Chi tiết kỹ thuật
Các loại cổng chính trên bộ não GBot:
1. **Cổng RJ (RJ Ports)**: Có 6 cổng được đánh số từ 1 đến 6.
   - Cổng 1, 2, 3, 4: Thường dùng để kết nối các cảm biến (Siêu âm, Dò đường) thông qua dây cáp RJ.
   - Cổng 5, 6: Chuyên dụng cho các thiết bị điều khiển như Servo.
2. **Cổng Động cơ (Motor Ports)**: Ký hiệu là M1 và M2. Dùng để kết nối 2 động cơ DC cho bánh xe (trái/phải).
3. **Cổng Nguồn (Power Port)**: Dùng để cắm hộp pin cung cấp năng lượng cho robot.
4. **Cổng nạp chương trình (USB Port)**: Dùng kết nối với máy tính để nạp code.
5. **Nút nhấn (On-board Button)**: Nút nhấn đa năng nằm ở trung tâm robot, dùng để chuyển đổi giữa 5 chế độ lập trình.

## 💡 Ví dụ thực tế
Khi lắp ráp Robot GBot cơ bản, động cơ bánh trái sẽ cắm vào cổng M1, động cơ bánh phải cắm vào cổng M2. Cảm biến dò đường thường được cắm vào cổng RJ số 3 hoặc 4 để robot có thể nhận diện vạch đen.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_Programming_Modes`, `WIKI_GBot_Ultrasonic_Sensor`
- Ứng dụng vào: `WIKI_GBot_Basic_Assembly`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | 6 cổng RJ, 2 cổng motor M1/M2, cổng nguồn và USB. |
| **Feelings** | Học sinh thường cắm nhầm Servo vào cổng 1-4 (không chạy) hoặc cắm ngược cổng M1/M2 dẫn đến robot đi lùi thay vì tiến. |
| **Findings** | Việc đánh số cổng rõ ràng giúp giảm thiểu lỗi kết nối phần cứng. |
| **Futures** | Dùng để hướng dẫn sơ đồ kết nối chuẩn cho các dự án Robotics khác nhau. |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 3, 4, 6, 25`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 3: cổng nguồn; Câu 4: Servo cổng 5,6; cổng motor M1, M2; Câu 25: nút nhấn trung tâm dùng chuyển chế độ).
