---
file_id: "WIKI_GBot_Programming_Modes"
title: "Chế độ lập trình GBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "GBot", "Programming"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Chế độ lập trình GBot

## 📌 Định nghĩa cốt lõi
Robot GBot có 5 chế độ vận hành và lập trình khác nhau, được phân biệt bằng màu sắc của đèn LED trạng thái trên bộ não của robot.

## 🔍 Chi tiết kỹ thuật
Các chế độ được quy định theo màu sắc:
1. **Màu đỏ**: Chế độ điều khiển bằng điện thoại thông qua Bluetooth (App GaraBlock).
2. **Màu trắng**: Chế độ lập trình với máy tính. Đây là chế độ bắt buộc để nạp (upload) chương trình từ máy tính sang robot.
3. **Màu xanh dương**: Chế độ robot tự hành (tránh vật cản tự động).
4. **Màu xanh lá**: Thường dùng cho các chế độ mở rộng hoặc chế độ mặc định khác tùy phiên bản firmware.
5. **Màu vàng**: Chế độ điều khiển hoặc cấu hình phụ.

**Quy tắc nạp chương trình:**
- Khi nạp chương trình từ máy tính sang GBot, robot phải ở **chế độ màu trắng**.
- Công tắc Bluetooth trên robot phải được **TẮT** để tránh xung đột với cổng Serial khi nạp code.

## 💡 Ví dụ thực tế
Khi học sinh muốn lập trình cho GBot tự đi theo vạch đen, các em cần nhấn nút nhấn trên bộ não cho đến khi đèn LED chuyển sang **màu trắng**, sau đó mới nhấn nút "Nạp chương trình" trên máy tính.

## 🔗 Liên kết tư duy
- Khái niệm cha: `WIKI_GBot_Creator_System`
- Liên quan trực tiếp: `WIKI_GBot_GaraBlock_Software`, `WIKI_GBot_Brain_Ports`
- Ứng dụng vào: `WIKI_GBot_Line_Follower_Project`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | GBot có 5 chế độ: đỏ, vàng, xanh lá, xanh dương, trắng. Nạp code dùng màu trắng. |
| **Feelings** | Học sinh thường quên chuyển sang màu trắng hoặc quên tắt Bluetooth dẫn đến lỗi nạp code "Upload failed". |
| **Findings** | Màu sắc đèn LED là giao tiếp trực quan nhất để biết trạng thái sẵn sàng của Robot. |
| **Futures** | Dùng để hướng dẫn học sinh quy trình nạp code chuẩn (Tắt Bluetooth -> Chế độ Trắng -> Nạp). |

## 📖 Nguồn
`📖 Nguồn: Robot_GBot_de_trac_nghiem_1_-_gbot_v1.md — Câu 7, 8, 9, 12`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về 3-resources/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong 3-resources/raw/ và xác nhận fact tồn tại (Câu 7: 5 chế độ; Câu 12: nạp chương trình ở chế độ màu trắng và tắt bluetooth).
