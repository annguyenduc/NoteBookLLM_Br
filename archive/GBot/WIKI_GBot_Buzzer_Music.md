---
file_id: "WIKI_GBot_Buzzer_Music"
title: "Loa và nốt nhạc trên GBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "GBot", "Output"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Loa và nốt nhạc trên GBot

## 📌 Định nghĩa cốt lõi
Loa (Buzzer) trên GBot là một linh kiện phát ra âm thanh, cho phép robot phát tín hiệu cảnh báo hoặc chơi các bản nhạc đơn giản bằng cách lập trình tần số nốt nhạc.

## 🔍 Chi tiết kỹ thuật
- **Nốt nhạc (Note)**: Mỗi nốt nhạc (Đô, Rê, Mi...) tương ứng với một tần số âm thanh nhất định.
- **Trường độ (Duration)**: Là thời gian phát nốt nhạc đó (ví dụ: nốt đen, nốt trắng, nốt móc đơn). Trong GaraBlock, thông số này thường được điều chỉnh để bản nhạc nhanh hoặc chậm.
- **Bảng quy đổi**: GaraBlock cung cấp giao diện trực quan để chọn nốt nhạc (ví dụ: Middle C - C4) thay vì phải nhớ tần số.

## 💡 Ví dụ thực tế
Lập trình cho robot kêu "bíp bíp" khi lùi xe, hoặc phát bài nhạc "Happy Birthday" khi khởi động.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_Programming_Modes`, `WIKI_GBot_RGB_LED_Control`
- Ứng dụng vào: `WIKI_GBot_Musical_Robot_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Buzzer dùng để phát âm thanh. Điều chỉnh Nốt và Trường độ để tạo nhạc. |
| **Feelings** | Học sinh rất hào hứng khi robot phát được nhạc, đây là cách dạy về "thông số đầu vào" (parameters) rất hiệu quả. |
| **Findings** | Việc tính toán trường độ nốt nhạc giúp học sinh rèn luyện tư duy toán học và tính kiên nhẫn. |
| **Futures** | Dùng để báo động khi cảm biến phát hiện vật cản hoặc vạch đen. |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 19, 20, 21`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 19: Điều chỉnh trường độ nốt nhạc; Câu 20: Bảng quy đổi nốt nhạc).
