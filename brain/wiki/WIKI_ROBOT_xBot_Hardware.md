---
file_id: "WIKI_ROBOT_xBot_Hardware"
title: "Phần cứng Robot xBot (xController)"
category: "Hardware Wiki"
prefix: "WIKI"
tags: ["Robotics", "OhStem", "xBot", "xController"]
source: "[[Robot_xBot_de_trac_nghiem_1]]"
status: "verified"
created: "2026-04-25"
last_updated: "2026-04-25"
---

# 🤖 Phần cứng Robot xBot (xController)

xBot là dòng robot giáo dục STEAM của OhStem, sử dụng board mạch điều khiển chính là **xController**.

## 📌 Board mạch xController
xController được thiết kế theo chuẩn kết nối RJ11 giúp học sinh dễ dàng đấu nối mà không sợ ngược cực.

### 🔍 Chi tiết cổng kết nối
- **4 Cổng mở rộng (Port 1, 2, 3, 4)**: Dùng để kết nối các cảm biến và module mở rộng (Siêu âm, dò đường, LCD...).
- **2 Cổng Motor (M1, M2)**: Chuyên dụng cho động cơ DC của robot.
- **2 Cổng Servo (S1, S2)**: Dùng để điều khiển các động cơ Servo (ví dụ: tay gắp).
- **Cổng nguồn (Power)**: Jack DC cho Pin sạc 7.4V.

## 💡 Tính năng tích hợp
- **LED RGB**: Gồm 2 đèn LED đa màu sắc tích hợp sẵn trên board mạch.
- **Buzzer**: Loa phát âm thanh tích hợp để báo hiệu.
- **Nút nhấn**: Tích hợp nút nhấn đa năng.

## 🔗 Liên kết tư duy
- Lập trình cho xBot: [[WIKI_ROBOT_Logic_Master]]
- So sánh với Rover: [[WIKI_ROBOT_Rover_Hardware]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | xController dùng chuẩn RJ11, có 4 port cảm biến, 2 port motor, 2 port servo. |
| **Feelings** | Chuẩn RJ11 giúp học sinh tự tin hơn khi lắp ráp, giảm thiểu rủi ro chập cháy board mạch. |
| **Findings** | Việc tích hợp sẵn LED và Buzzer trên board giúp học sinh có thể thực hành logic lập trình cơ bản ngay cả khi chưa lắp cảm biến. |
| **Futures** | xBot là nền tảng tốt để phát triển các dự án Robot công nghiệp mini hoặc hệ thống phân loại sản phẩm. |

## 📖 Nguồn
`📖 Nguồn: brain/raw/[[brain/raw/Robot_xBot_de_trac_nghiem_1_-_xbot.md]] — Câu 3, 5, 6.`
