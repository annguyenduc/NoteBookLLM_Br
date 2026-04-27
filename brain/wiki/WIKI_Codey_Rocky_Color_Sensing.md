---
file_id: "WIKI_Codey_Rocky_Color_Sensing"
title: "Nhận diện màu sắc trên Codey Rocky"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "CodeyRocky", "Sensor"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Nhận diện màu sắc trên Codey Rocky

## 📌 Định nghĩa cốt lõi
Cảm biến màu sắc (Color Sensor) nằm ở mặt dưới của Rocky, cho phép robot nhận biết các màu sắc khác nhau của bề mặt hoặc vật cản bằng cách phân tích phản xạ ánh sáng.

## 🔍 Chi tiết kỹ thuật
- **Nguyên lý RGB**: Cảm biến nhận biết màu sắc theo hệ màu RGB (Red - Green - Blue). Mỗi thông số R, G, B có giá trị từ **0 đến 255**.
- **Tính năng hồng ngoại**: Ngoài nhận diện màu sắc, cảm biến này còn tích hợp 2 đèn hồng ngoại:
  - **Đèn phát (Emitter)**: Phát tia hồng ngoại.
  - **Đèn thu (Receiver)**: Thu tín hiệu hồng ngoại phản hồi để nhận biết vật cản.
- **Vị trí**: Nằm ở mặt dưới của Rocky, phía trước cụm bánh xích.

**Chế độ hoạt động:**
1. **Nhận biết màu**: Trả về tên màu (Đỏ, Xanh, Vàng...) hoặc giá trị RGB.
2. **Dò đường (Line Follow)**: Sử dụng sự khác biệt về độ phản xạ giữa vạch đen và nền trắng.
3. **Nhận biết vật cản (Proximity)**: Trả về giá trị Logic (True/False) khi có vật cản phía trước.

## 💡 Ví dụ thực tế
Lập trình cho robot: "Nếu phát hiện màu Đỏ thì dừng lại, nếu phát hiện màu Xanh thì đi tiếp". Ứng dụng trong bài toán robot phân loại sản phẩm theo màu sắc.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_Codey_Rocky_Sensors]]
- Liên quan trực tiếp: [[WIKI_Codey_Rocky_System]], [[WIKI_Codey_Rocky_Movement]]
- Ứng dụng vào: [[WIKI_Codey_Color_Sorting_Project]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Nhận diện màu qua RGB 0-255. Tích hợp đèn phát/thu hồng ngoại. |
| **Feelings** | Học sinh thường ngạc nhiên khi biết cảm biến màu sắc cũng chính là cảm biến nhận diện vật cản. |
| **Findings** | Ánh sáng môi trường (quá tối hoặc quá sáng) có thể làm thay đổi giá trị RGB trả về, cần "hiệu chuẩn" (calibrate) trong điều kiện thực tế. |
| **Futures** | Ứng dụng trong công nghiệp tự động hóa để kiểm tra chất lượng sản phẩm qua màu sắc. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_Codey_de_trac_nghiem_1_-_codey_m2.md]] — Câu 10, 13`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 10: Đèn phát/thu hồng ngoại; Câu 13: Giá trị màu RGB 0-255).
