---
file_id: "WIKI_Codey_LED_Coordinates"
title: "Hệ tọa độ trên màn hình LED Codey"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "Codey", "Display"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Hệ tọa độ trên màn hình LED Codey

## 📌 Định nghĩa cốt lõi
Để điều khiển chính xác từng điểm sáng trên màn hình LED ma trận 16x8 của Codey, người lập trình sử dụng hệ tọa độ Descartes (X, Y).

## 🔍 Chi tiết kỹ thuật
- **Trục X (Ngang)**: Có giá trị từ **0 đến 15**. (Số 0 là điểm ngoài cùng bên trái).
- **Trục Y (Dọc)**: Có giá trị từ **0 đến 7**. (Số 0 là điểm cao nhất).
- **Điểm ảnh (Pixel)**: Mỗi điểm sáng được xác định bởi cặp giá trị (x, y).

**Câu lệnh sử dụng:**
- `Set pixel at x:[ ] y:[ ] to [on/off]`: Bật hoặc tắt một đèn LED cụ thể.
- `Show image [ ] at x:[ ] y:[ ]`: Hiển thị một hình ảnh tại vị trí tọa độ xác định.

## 💡 Ví dụ thực tế
Để bật đèn LED ở chính giữa màn hình, học sinh có thể đặt tọa độ X=7 (hoặc 8) và Y=3 (hoặc 4). Để di chuyển một khuôn mặt từ trái sang phải, ta chỉ cần thay đổi giá trị X tăng dần trong một vòng lặp.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_Codey_LED_Matrix]]
- Liên quan trực tiếp: [[WIKI_Codey_Rocky_System]], [[WIKI_mBlock_5_Software]]
- Ứng dụng vào: [[WIKI_Codey_Game_Development]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | X từ 0-15, Y từ 0-7. Dùng tọa độ để bật tắt từng điểm LED. |
| **Feelings** | Học sinh thường bị nhầm lẫn và đếm số từ 1 thay vì từ 0, dẫn đến việc hình ảnh bị lệch 1 pixel. |
| **Findings** | Việc dạy về tọa độ trên robot là cách trực quan nhất để học sinh hiểu về toán học đồ họa. |
| **Futures** | Ứng dụng để lập trình các trò chơi đơn giản như Hứng bóng hoặc Rắn săn mồi trên màn hình Codey. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_Codey_de_trac_nghiem_1_-_codey_m2.md]] — Câu 8, 9`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 8: Xác định tọa độ X, Y trên LED; Câu 9: Kết quả hiển thị dựa trên tọa độ).
