---
file_id: "WIKI_GBot_Line_Follower_Sensor"
title: "Cảm biến dò đường GBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "GBot", "Sensor"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Cảm biến dò đường GBot

## 📌 Định nghĩa cốt lõi
Cảm biến dò đường (Line Follower Sensor) là thiết bị giúp robot nhận biết vạch kẻ đường (thường là vạch đen trên nền trắng) bằng cách sử dụng tia hồng ngoại.

## 🔍 Chi tiết kỹ thuật
- **Cấu tạo**: Gồm các mắt hồng ngoại (mỗi mắt có 1 đầu phát tia hồng ngoại và 1 đầu thu). GBot thường có loại cảm biến 2 mắt hoặc 4 mắt.
- **Nguyên lý**: 
  - Màu trắng phản xạ tia hồng ngoại tốt -> Cảm biến nhận tín hiệu mạnh.
  - Màu đen hấp thụ tia hồng ngoại -> Cảm biến nhận tín hiệu yếu hoặc không nhận được.
- **Giá trị trả về**: Trả về giá trị 0 hoặc 1 (hoặc True/False). 
  - Giá trị 0: Mắt cảm biến đang ở trên vùng màu đen (vạch đường).
  - Giá trị 1: Mắt cảm biến đang ở trên vùng màu trắng (nền).
- **Kết nối**: Cắm vào cổng RJ số 3 hoặc 4 trên bộ não GBot.

## 💡 Ví dụ thực tế
Trong dự án "Robot đi theo vạch", nếu cả 2 mắt cảm biến đều báo giá trị 0 (đang ở vùng tối), robot sẽ đi thẳng. Nếu mắt trái báo 1, mắt phải báo 0, robot cần rẽ phải để quay lại vạch.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_Brain_Ports`, `WIKI_GBot_Movement_Commands`
- Ứng dụng vào: `WIKI_GBot_Line_Follower_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Hoạt động dựa trên sự hấp thụ/phản xạ hồng ngoại. Giá trị 0 là Đen, 1 là Trắng. |
| **Feelings** | Học sinh hay bị ngược logic giữa 0 và 1. Cần nhấn mạnh "Đen là 0" (giống như tắt đèn). |
| **Findings** | Ánh sáng môi trường quá mạnh có thể làm nhiễu cảm biến, cần che chắn hoặc hiệu chỉnh. |
| **Futures** | Cơ sở cho các bài toán robot vận chuyển hàng hóa tự động trong nhà kho. |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 6, 28, 29, 30`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 28: nguyên lý hấp thụ tia sáng; Câu 29: Giá trị 0 là đen, 1 là sáng).
