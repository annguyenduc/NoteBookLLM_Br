---
file_id: "WIKI_ROBOT_Rover_Hardware"
title: "Phần cứng Robot Rover (Yolo:Bit)"
category: "Hardware Wiki"
prefix: "WIKI"
tags: ["Robotics", "OhStem", "Rover", "YoloBit"]
source: "[[Robot_Rover_de_trac_nghiem_1]]"
status: "verified"
created: "2026-04-25"
last_updated: "2026-04-25"
---

# 🏎️ Phần cứng Robot Rover (Yolo:Bit)

Rover là dòng robot di động sử dụng **Yolo:Bit** làm bộ não trung tâm, kết hợp với mạch mở rộng (Rover Shield).

## 📌 Bộ não Yolo:Bit
Yolo:Bit là mạch học lập trình tích hợp nhiều tính năng:
- **Ma trận LED 5x5**: Hiển thị hình ảnh (ví dụ: `Image.HEART`, `Image.SMILE`), ký tự và thông số.
- **2 Nút nhấn (A, B)**: Dùng để tương tác và kích hoạt lệnh.
- **Cảm biến tích hợp**: Gia tốc kế (đo độ nghiêng), la bàn, cảm biến ánh sáng và nhiệt độ.

## 🔍 Rover Shield (Mạch mở rộng)
Mạch shield giúp Yolo:Bit có thể điều khiển động cơ và kết nối cảm biến:
- **Cổng kết nối RJ11**: Gồm 4 cổng mở rộng (Port 1-4).
- **Cổng Motor**: Điều khiển 2 động cơ DC (M1, M2).
- **Cảm biến tích hợp**: 
    - 2 mắt **dò đường (Line Follower)** ở mặt dưới (thường nối qua Port 2 nếu dùng module rời). (Nguồn: [[Robot_Rover_de_trac_nghiem_5]])
    - 2 đèn **LED RGB** (mắt robot) ở mặt trước.
    - **Cảm biến siêu âm**: Thường cắm tại **Port 1** để tránh vật cản.

## 🔗 Liên kết tư duy
- Lập trình cho Rover: [[WIKI_ROBOT_Logic_Master]]
- Board mạch xBot: [[WIKI_ROBOT_xBot_Hardware]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Não là Yolo:Bit, có ma trận 5x5. Shield có 4 cổng RJ11. Siêu âm cắm Port 1. |
| **Feelings** | Ma trận LED 5x5 giúp robot "biểu cảm" hơn, thu hút học sinh tiểu học và THCS. |
| **Findings** | Rover linh hoạt hơn xBot nhờ sự tích hợp của Yolo:Bit, phù hợp cho các bài toán về tương tác người - máy. |
| **Futures** | Ứng dụng trong xe tự hành, trạm quan trắc di động hoặc robot thám hiểm địa hình. |

## 📖 Nguồn
`📖 Nguồn: brain/raw/[[brain/raw/Robot_Rover_de_trac_nghiem_1_-_rover.md]] + [[brain/raw/Robot_Rover_de_trac_nghiem_2_-_rover_-_rut_gon.md]]
