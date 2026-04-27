---
file_id: "WIKI_Codey_Rocky_Connection"
title: "Kết nối và Nguồn cho Codey Rocky"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Robotics", "CodeyRocky", "Hardware"]
source: "[[WIKI_INDEX.md]]"
status: "draft"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Kết nối và Nguồn cho Codey Rocky

## 📌 Định nghĩa cốt lõi
Để lập trình và vận hành Codey Rocky, người dùng cần nắm rõ quy trình kết nối với máy tính và cách quản lý năng lượng cho robot.

## 🔍 Chi tiết kỹ thuật
### 1. Quy trình kết nối máy tính (Cáp USB):
- **Bước 1**: Cắm cáp USB vào robot Codey và cổng USB trên máy tính.
- **Bước 2**: Nhấn nút nguồn trên Codey.
- **Bước 3**: Trên phần mềm mBlock, nhấn nút **"Connect"**.
- **Bước 4**: Chọn đúng cổng **COM** tương ứng và nhấn kết nối lại một lần nữa.

### 2. Năng lượng và Sạc pin:
- **Loại pin**: Sử dụng pin Lithium sạc được tích hợp sẵn bên trong robot.
- **Cách sạc**: Kết nối Codey với máy tính thông qua dây USB (robot sẽ tự động nạp năng lượng, không cần khởi động robot trong khi sạc).
- **Lưu ý**: Không sử dụng các loại pin rời như pin AAA cho dòng Codey Rocky này.

## 💡 Ví dụ thực tế
Nếu robot Codey không bật lên được, học sinh nên kiểm tra xem pin có hết không bằng cách cắm vào máy tính. Nếu đèn báo sạc sáng, nghĩa là robot đang được nạp điện.

## 🔗 Liên kết tư duy
- Khái niệm cha: [[WIKI_Codey_Rocky_System]]
- Liên quan trực tiếp: [[WIKI_mBlock_5_Software]], [[WIKI_Codey_Rocky_Sensors]]
- Ứng dụng vào: [[WIKI_Robot_Setup_Guide]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Kết nối qua USB/Bluetooth. Sạc pin qua cổng USB. Pin Lithium tích hợp. |
| **Feelings** | Học sinh thường lo lắng khi robot không kết nối được, đa phần là do chọn sai cổng COM hoặc chưa bật nguồn robot. |
| **Findings** | Việc sạc pin trực tiếp qua USB giúp tiết kiệm chi phí mua pin rời và bảo vệ môi trường. |
| **Futures** | Ứng dụng kết nối không dây (Bluetooth) để điều khiển robot từ xa trong các dự án di động. |

## 📖 Nguồn
`📖 Nguồn: [[brain/raw/Robot_Codey_de_trac_nghiem_1_-_codey_m1.md]] — Câu 2, 3`

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã mở file nguồn trong brain/raw/ và xác nhận fact tồn tại (Câu 2: Quy trình kết nối cổng COM; Câu 3: Cách sạc pin Lithium qua USB).
