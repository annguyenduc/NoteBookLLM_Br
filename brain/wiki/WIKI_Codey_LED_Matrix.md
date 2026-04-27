---
file_id: "WIKI_Codey_LED_Matrix"
title: "Màn hình LED ma trận của Codey"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "Codey", "Display"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Màn hình LED ma trận của Codey

## 📌 Định nghĩa cốt lõi
Màn hình LED ma trận trên Codey là bộ phận hiển thị chính, bao gồm 128 đèn LED nhỏ được sắp xếp theo dạng lưới, cho phép hiển thị hình ảnh, văn bản và các biểu cảm cảm xúc.

## 🔍 Chi tiết kỹ thuật
- **Kích thước**: 16 hàng ngang x 8 hàng dọc (Tổng cộng 128 đèn LED).
- **Khả năng hiển thị**:
  - **Văn bản**: Hiển thị chữ cái hoặc con số. Có thể điều chỉnh để chữ chạy ngang (scroll).
  - **Hình ảnh/Cảm xúc**: Vẽ các hình đơn giản hoặc chọn từ thư viện cảm xúc (mặt cười, giận dữ, trái tim).
  - **Thời gian hiển thị**: Có thể lập trình để hiển thị trong một khoảng thời gian cố định hoặc hiển thị mãi mãi cho đến khi có lệnh mới.

**Lưu ý lập trình:**
- Nếu nạp lệnh hiển thị mà không có lệnh "đợi" (wait) hoặc hiển thị trong X giây, AI sẽ thực hiện lệnh rất nhanh và chuyển sang lệnh kế tiếp, khiến mắt người khó nhận ra.

## 💡 Ví dụ thực tế
Lập trình cho Codey hiển thị hình "Trái tim" khi học sinh nhấn nút A, và hiển thị chữ "Hello" chạy qua màn hình khi nhấn nút B.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_Codey_Rocky_System]]
- Liên quan trực tiếp: [[WIKI_Codey_LED_Coordinates]], [[WIKI_Codey_Rocky_Sensors]], [[WIKI_Codey_Rocky_Connection]]
- Ứng dụng vào: [[WIKI_Codey_Emotions_Project]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Ma trận 16x8 leds. Hiển thị text, image, emotions. |
| **Feelings** | Học sinh thường quên tính 128 đèn LED này là 16x8, dẫn đến việc thiết kế hình ảnh bị lệch hoặc mất chi tiết. |
| **Findings** | Việc hiển thị cảm xúc giúp robot trở nên có "hồn" hơn, tăng tính tương tác xã hội trong các bài học STEM. |
| **Futures** | Dùng để hiển thị giá trị các cảm biến (ví dụ: hiển thị số đo nhiệt độ hoặc độ sáng) một cách trực quan. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_Codey_de_trac_nghiem_1_-_codey_m1.md]] — Câu 4, 13, 16`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 4: Kích thước 16x8; Câu 16: Hiển thị văn bản nhanh nếu không có lệnh đợi).
