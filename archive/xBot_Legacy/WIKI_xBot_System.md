---
file_id: "WIKI_xBot_System"
title: "Hệ thống Robot xBot"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "xBot", "System"]
source: "`WIKI_INDEX.md`"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Hệ thống Robot xBot

## 📌 Định nghĩa cốt lõi
xBot là một robot giáo dục lập trình STEM cao cấp của OhStem, được xây dựng trên nền tảng vi điều khiển **xController** (tương thích Arduino). Robot này được thiết kế để giảng dạy lập trình kéo thả và lập trình Python cho học sinh từ cấp Tiểu học đến THPT.

## 🔍 Chi tiết kỹ thuật
Hệ thống xBot bao gồm:
1. **Mạch điều khiển xController**: Bộ não trung tâm với chip xử lý mạnh mẽ, tích hợp sẵn các cổng kết nối RJ và linh kiện điện tử.
2. **Cấu trúc cơ khí**: Khung nhôm chắc chắn, di chuyển bằng 2 động cơ DC.
3. **Module mở rộng**: Cảm biến siêu âm, cảm biến dò đường (Line Follower), cảm biến màu sắc, v.v.
4. **Hệ sinh thái OhStem**: Lập trình qua ứng dụng web `app.ohstem.vn` hoặc ứng dụng di động OhStem App.

**Đặc điểm nổi bật:**
- Kết nối bằng cáp **USB Type C** hiện đại hoặc Bluetooth.
- Có 6 cổng mở rộng để cắm thêm các module linh kiện.
- Hỗ trợ nạp code chạy offline (Lưu project vào thiết bị).

## 💡 Ví dụ thực tế
Trong các giải thi đấu Robotics, xBot thường được dùng để thi chạy sa bàn tốc độ cao nhờ cảm biến dò đường 4 mắt (V2) có độ chính xác và tốc độ phản hồi nhanh.

## 🔗 Liên kết tư duy
- Khái niệm con: `WIKI_xBot_xController_Board`, `WIKI_xBot_Line_Follower_V2`, `WIKI_OhStem_App_Software`
- Khái niệm liên quan: `WIKI_xBot_Movement_and_Speed`
- Ứng dụng vào: `WIKI_STEAM_Education_K12`

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Mạch xController (Arduino), cổng USB-C, 6 cổng RJ mở rộng. |
| **Feelings** | Học sinh thường cảm thấy xBot chuyên nghiệp và mạnh mẽ hơn các dòng robot đồ chơi nhựa thông thường nhờ khung nhôm và cổng USB-C. |
| **Findings** | Việc sử dụng cổng USB Type C giúp quá trình nạp code ổn định hơn và không sợ cắm ngược đầu dây. |
| **Futures** | Là nền tảng để triển khai các dự án IoT (Internet of Things) và AI nâng cao. |

## 📖 Nguồn
`📖 Nguồn: Robot_xBot_de_trac_nghiem_1_-_xbot.md — Câu 1, 2, 3, 7`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 `wikilinks`
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 1: 6 cổng mở rộng; Câu 2: Mạch xController; Câu 3: Cáp USB Type C).
