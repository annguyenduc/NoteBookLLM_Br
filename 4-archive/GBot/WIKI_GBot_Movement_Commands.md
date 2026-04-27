---
file_id: "WIKI_GBot_Movement_Commands"
title: "Lệnh di chuyển GBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "GBot", "Programming"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Lệnh di chuyển GBot

## 📌 Định nghĩa cốt lõi
Lệnh di chuyển là các khối lệnh trong phần mềm GaraBlock điều khiển 2 động cơ M1 và M2 để robot thực hiện các quỹ đạo khác nhau (tiến, lùi, xoay, rẽ).

## 🔍 Chi tiết kỹ thuật
Trong GaraBlock, có 2 cách xoay/rẽ chính cần phân biệt:
1. **Rotate (Xoay tại chỗ)**: Trục xoay nằm ở **trung tâm** robot. Hai bánh xe quay ngược chiều nhau (ví dụ: bánh phải tiến, bánh trái lùi). Giúp robot đổi hướng nhanh trong không gian hẹp.
2. **Turn (Rẽ)**: Trục xoay nằm ở **một bánh xe**. Một bánh xe quay, bánh kia đứng yên (ví dụ: bánh phải tiến, bánh trái đứng yên). Tạo ra quỹ đạo hình cung rộng hơn.

**Thiết lập mặc định:**
- Động cơ **M1** thường là bánh xe bên **Trái**.
- Động cơ **M2** thường là bánh xe bên **Phải**.

## 💡 Ví dụ thực tế
Để robot di chuyển theo một hình vuông, học sinh có thể dùng lệnh "Tiến" trong 2 giây, sau đó dùng lệnh "Rotate Left" một góc 90 độ, lặp lại 4 lần.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_Brain_Ports`, `WIKI_GBot_Obstacle_Avoidance_Project`
- Ứng dụng vào: `WIKI_GBot_Square_Path_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | M1 = Trái, M2 = Phải. Phân biệt Rotate (trục trung tâm) và Turn (trục tại bánh xe). |
| **Feelings** | Học sinh thường bị nhầm lẫn giữa Rotate và Turn, dẫn đến việc tính toán quỹ đạo không chính xác. |
| **Findings** | Lệnh Rotate giúp robot quay tại chỗ chính xác hơn khi làm các bài toán sa bàn. |
| **Futures** | Áp dụng để giải các bài toán vượt mê cung hoặc di chuyển theo hình học. |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 16, 17, 18`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 17: Phân biệt Rotate và Turn).
