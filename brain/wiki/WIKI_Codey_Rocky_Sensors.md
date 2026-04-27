---
file_id: "WIKI_Codey_Rocky_Sensors"
title: "Hệ thống cảm biến Codey Rocky"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "CodeyRocky", "Sensor"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Hệ thống cảm biến Codey Rocky

## 📌 Định nghĩa cốt lõi
Codey Rocky được trang bị một hệ thống cảm biến phong phú tích hợp sẵn trên cả hai bộ phận Codey và Rocky, giúp robot có khả năng tương tác mạnh mẽ với môi trường xung quanh.

## 🔍 Chi tiết kỹ thuật
Các cảm biến được phân bổ như sau:

### 1. Trên bộ phận Codey:
- **Cảm biến Ánh sáng**: Nhận biết cường độ ánh sáng của môi trường.
- **Cảm biến Âm thanh**: Nhận biết mức độ tiếng ồn xung quanh.
- **Con quay hồi chuyển (6-axis Gyroscope/Accelerometer)**: Nhận biết các hành động như nghiêng trái/phải, ngửa mặt lên/xuống, lắc hoặc rơi tự do.

### 2. Trên bộ phận Rocky:
- **Cảm biến Hồng ngoại tiệm cận (IR Proximity)**: Nhận biết vật cản phía trước.
- **Cảm biến Màu sắc (Color Sensor)**: Nhận diện màu sắc của bề mặt bên dưới hoặc vật cản (được tích hợp chung với cảm biến hồng ngoại).

## 💡 Ví dụ thực tế
Lập trình cho Codey: Khi robot bị "nghiêng sang trái", màn hình LED sẽ hiện mũi tên chỉ sang trái; khi bị "lắc", robot sẽ phát ra âm thanh 'start' và hiển thị một số ngẫu nhiên từ 1 đến 100.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_Codey_Rocky_System]]
- Liên quan trực tiếp: [[WIKI_Codey_Rocky_Color_Sensing]], [[WIKI_Codey_LED_Matrix]], [[WIKI_Codey_Rocky_Connection]]
- Ứng dụng vào: [[WIKI_Codey_Smart_Nightlight_Project]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Cảm biến ánh sáng/âm thanh/nghiêng ở Codey. Hồng ngoại/màu sắc ở Rocky. |
| **Feelings** | Học sinh rất thích thú với cảm biến "nghiêng" và "lắc" vì nó làm robot có cảm giác giống như một sinh vật sống biết phản ứng. |
| **Findings** | Việc hiểu rõ vị trí cảm biến (Codey hay Rocky) giúp học sinh viết code điều khiển chính xác hơn (ví dụ: muốn tránh vật cản thì phải gọi cảm biến của Rocky). |
| **Futures** | Là tiền đề để dạy về các hệ thống điều khiển tự động dựa trên phản hồi của cảm biến (Feedback loop). |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_Codey_de_trac_nghiem_1_-_codey_m1.md]] — Câu 5, 6, 22, 23, 24`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 5, 6: Vị trí các cảm biến; Câu 22, 23, 24: Các ví dụ về lập trình dựa trên cảm biến nghiêng, lắc, ánh sáng).
