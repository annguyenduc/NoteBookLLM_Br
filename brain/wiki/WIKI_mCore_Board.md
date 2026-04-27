---
file_id: "WIKI_mCore_Board"
title: "Mạch điều khiển mCore (mBot)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "mBot", "Hardware"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Mạch điều khiển mCore (mBot)

## 📌 Định nghĩa cốt lõi
mCore là bo mạch điều khiển trung tâm dành riêng cho robot mBot, được phát triển dựa trên nền tảng Arduino Uno với các cải tiến về cổng kết nối và linh kiện tích hợp sẵn.

## 🔍 Chi tiết kỹ thuật
Các thành phần chính trên mạch mCore:
1. **Linh kiện tích hợp sẵn (On-board)**:
   - **Cảm biến ánh sáng**: Nhận biết cường độ sáng.
   - **2 Đèn LED RGB**: Có thể hiển thị hàng triệu màu (Đỏ + Xanh lá + Xanh dương = Trắng).
   - **Loa (Buzzer)**: Phát tín hiệu âm thanh và âm nhạc (thuộc nhóm lệnh Show).
   - **Cảm biến hồng ngoại (IR)**: Thu phát tín hiệu từ Remote hoặc giữa các robot.
   - **Nút nhấn (Button)**: Có thể lập trình để kích hoạt các đoạn lệnh.
2. **Cổng kết nối mở rộng**:
   - **4 cổng RJ**: Được đánh số từ 1 đến 4. Cảm biến siêu âm và dò đường có thể cắm vào bất kỳ cổng nào trong 4 cổng này.
   - **Cổng Motor (M1, M2)**: Điều khiển tốc độ 2 động cơ DC (M1 là bánh Trái, M2 là bánh Phải).
   - **Cổng nguồn**: Hỗ trợ pin Lithium hoặc hộp 4 pin AA qua Jack DC.
   - **Cổng USB Type B**: Kết nối và nạp code.

## 💡 Ví dụ thực tế
Để kiểm tra robot đã bật nguồn chưa, học sinh có thể lập trình cho 2 đèn LED trên mCore sáng màu Trắng (R=255, G=255, B=255) ngay khi robot khởi động.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_mBot_System]]
- Liên quan trực tiếp: [[WIKI_mBot_Sensors]], [[WIKI_mBot_Programming_and_Modes]]
- Ứng dụng vào: [[WIKI_Robot_Brain_Logic]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Mạch Arduino Uno, cổng USB-B, tích hợp LED RGB, Loa, Cảm biến ánh sáng. |
| **Feelings** | Học sinh thường loay hoay tìm cảm biến ánh sáng vì nó nhỏ và nằm ngay trên mạch điều khiển trung tâm. |
| **Findings** | Việc gộp M1 (Trái) và M2 (Phải) vào một câu lệnh giúp việc lập trình di chuyển đơn giản và logic hơn. |
| **Futures** | Là nền tảng để học sinh học về "Hệ thống nhúng" (Embedded systems) một cách trực quan. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_mBot_de_trac_nghiem_1_-_mon_mbot_m1_2.md]] — Câu 3, 4, 7, 8, 10, 11`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 3: Cảm biến ánh sáng tích hợp; Câu 8: Màu trắng = R+G+B; Câu 10: M1=Trái, M2=Phải).
