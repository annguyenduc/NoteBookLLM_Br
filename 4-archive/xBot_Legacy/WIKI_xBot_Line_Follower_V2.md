---
file_id: "WIKI_xBot_Line_Follower_V2"
title: "Cảm biến dò đường xBot V2"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "xBot", "Sensor"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Cảm biến dò đường xBot V2

## 📌 Định nghĩa cốt lõi
Cảm biến dò đường xBot V2 là module linh kiện gắn rời, giúp robot nhận diện vạch kẻ đường (đen/trắng) để di chuyển tự động theo sa bàn.

## 🔍 Chi tiết kỹ thuật
- **Nguyên lý**: Sử dụng tia hồng ngoại (Infrared) để nhận diện độ tương phản của bề mặt.
- **Cấu tạo**: Gồm **4 mắt cảm biến** giúp robot bám vạch chính xác hơn so với loại 2 mắt thông thường.
- **Kết nối**: Có thể cắm vào bất kỳ cổng RJ nào trong số 6 cổng trên mạch xController.

**Quy trình hiệu chuẩn (Calibration):**
Đây là bước cực kỳ quan trọng để robot nhận diện vạch đen chuẩn nhất:
1. Đặt cả 4 mắt của cảm biến nằm lên vạch đen trên sa bàn.
2. Nhấn nút nhấn vật lý trên module cảm biến dò đường.
3. Cảm biến sẽ tự động ghi nhớ giá trị độ đen của vạch để so sánh khi hoạt động.

## 💡 Ví dụ thực tế
Trong nhiệm vụ "Robot đi theo vạch đen", nếu mắt cảm biến số 1 (ngoài cùng bên trái) chạm vạch trắng trong khi mắt 2 và 3 vẫn ở vạch đen, robot sẽ tự động rẽ phải để đưa mắt 1 quay lại vạch đen.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_xBot_System`
- Liên quan trực tiếp: `WIKI_xBot_xController_Board`, `WIKI_xBot_Movement_and_Speed`
- Ứng dụng vào: `WIKI_xBot_Line_Following_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | 4 mắt cảm biến hồng ngoại. Hiệu chuẩn bằng nút bấm trên module khi đặt trên vạch đen. |
| **Feelings** | Học sinh thường quên bước hiệu chuẩn khiến robot chạy loạn xạ hoặc không nhận vạch. |
| **Findings** | Việc sử dụng 4 mắt cho phép lập trình các mức độ rẽ (rẽ nhẹ, rẽ gắt) mượt mà hơn. |
| **Futures** | Ứng dụng trong các robot kho bãi tự động vận hành theo chỉ dẫn vạch kẻ. |

## 📖 Nguồn
`📖 Nguồn: Robot_xBot_de_trac_nghiem_1_-_xbot.md — Câu 5, 27, 28`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 27: Nguyên lý hồng ngoại; Câu 28: Cách hiệu chuẩn bằng nút nhấn khi đặt trên vạch đen).
