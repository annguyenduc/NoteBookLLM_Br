---
file_id: "WIKI_Codey_Rocky_Movement"
title: "Lập trình di chuyển cho Codey Rocky"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "CodeyRocky", "Programming"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Lập trình di chuyển cho Codey Rocky

## 📌 Định nghĩa cốt lõi
Di chuyển là chức năng chính của bộ phận Rocky, cho phép robot di chuyển theo nhiều quỹ đạo khác nhau dựa trên việc điều khiển tốc độ của hai bánh xích.

## 🔍 Chi tiết kỹ thuật
### 1. Thông số công suất (Power):
- Trong dạy học, khuyến khích học sinh đặt công suất di chuyển trong khoảng **30% đến 70%** để đảm bảo robot di chuyển ổn định và bảo vệ động cơ.

### 2. Các hướng di chuyển cơ bản:
- **Tiến/Lùi**: Cả hai bánh quay cùng chiều.
- **Xoay phải (Rotate Right)**: Bánh trái quay tiến, bánh phải quay lùi (ví dụ: Trái 70, Phải -70).
- **Xoay trái (Rotate Left)**: Bánh trái quay lùi, bánh phải quay tiến (ví dụ: Trái -70, Phải 70).

### 3. Logic điều khiển:
- **Lệnh di chuyển theo thời gian**: "Tiến tới với công suất 50% trong 1 giây" -> Robot sẽ dừng sau 1 giây.
- **Lệnh di chuyển liên tục**: "Tiến tới với công suất 50%" -> Robot sẽ đi mãi mãi cho đến khi gặp lệnh dừng hoặc hết pin.

## 💡 Ví dụ thực tế
Để lập trình cho Codey Rocky đi theo hình ziczac: Robot tiến tới 2 giây, sau đó xoay phải 1 góc, rồi lại tiến tới. Quá trình này lặp lại liên tục.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_Codey_Rocky_System]]
- Liên quan trực tiếp: [[WIKI_Codey_Rocky_Sensors]], [[WIKI_Codey_LED_Matrix]]
- Ứng dụng vào: [[WIKI_Codey_Rocky_Ziczac_Project]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Công suất an toàn 30-70%. Điều khiển tốc độ riêng lẻ bánh trái/phải. |
| **Feelings** | Học sinh thường cho robot chạy 100% công suất khiến robot khó kiểm soát hướng chính xác. |
| **Findings** | Việc sử dụng giá trị âm cho tốc độ (ví dụ -70) giúp robot di chuyển ngược lại mà không cần thay đổi khối lệnh "tiến". |
| **Futures** | Cơ sở để dạy về các bài toán robot vận chuyển trong nhà kho thông minh. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_Codey_de_trac_nghiem_1_-_codey_m1.md]] — Câu 12, 18, 19, 21, 30`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 12: Công suất 30-70%; Câu 18, 19: Thông số bánh trái/phải cho lệnh lùi và xoay; Câu 30: Di chuyển hình ziczac).
