---
file_id: "WIKI_CONCEPT_SQL_PERFORMANCE_TUNING"
title: "Tối ưu hóa hiệu năng SQL (SQL Performance Tuning)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["SQL", "Optimization", "Database", "Performance"]
source: "SQL_Pocket_Guide"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-02"
agent_id: "@engineer"
---

# Tối ưu hóa hiệu năng SQL (SQL Performance Tuning)

Tối ưu hóa hiệu năng SQL là nghệ thuật tinh chỉnh các câu lệnh truy vấn để đạt được tốc độ xử lý tối đa với chi phí tài nguyên thấp nhất.

## 核心 (Core Principle)
1. **Minh bạch hóa chi phí (Cost Visibility):** Sử dụng `EXPLAIN` hoặc `Execution Plan` để hiểu cách Database Engine "nhìn" câu lệnh của bạn.
2. **Nguyên tắc "Lọc sớm, Lấy ít" (Filter Early, Select Less):** Giảm diện tích tiếp xúc của dữ liệu ngay từ những bước đầu tiên của Pipeline.
3. **Chiến lược Indexing thông minh:** Không phải cứ thêm Index là tốt; cần hiểu rõ Index B-Tree vs Bitmap và quy tắc cột bên trái (Leftmost prefix).

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trong cuốn *SQL Pocket Guide*, tác giả nhấn mạnh việc tránh sử dụng hàm trên cột được đánh Index. Thay vì dùng `WHERE YEAR(JoinDate) = 2023` (buộc DB phải duyệt toàn bộ bảng - Full Table Scan), hãy dùng `WHERE JoinDate >= '2023-01-01' AND JoinDate < '2024-01-01'` để tận dụng Index Seek.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng bạn đang tìm một cuốn sách trong thư viện khổng lồ:
- **Cách chưa tối ưu:** Bạn đi từng kệ, mở từng cuốn sách để xem tiêu đề (Full Table Scan).
- **Cách tối ưu:** Bạn dùng thẻ tra cứu (Index) để biết chính xác cuốn sách nằm ở Kệ A, Hàng 3. Việc này nhanh hơn hàng nghìn lần so với việc kiểm tra thủ công. **Performance Tuning** giống như việc thủ thư sắp xếp lại thẻ tra cứu sao cho độc giả tìm thấy sách nhanh nhất.

## Liên kết tư duy
- [[CONCEPT_SQL_Execution_Order]]
- [[CONCEPT_SQL_CTEs]]
- [[ENTITY_SQL]]

## 4F — Phản tư sư phạm
- **Facts:** Hầu hết các vấn đề về hiệu năng SQL đến từ việc thiếu Index hoặc viết câu lệnh gây ra Full Table Scan một cách vô ý.
- **Feelings:** Một lập trình viên mới thường cảm thấy "kỳ diệu" khi một câu lệnh chạy từ 10 phút giảm xuống còn 1 giây chỉ sau một thay đổi nhỏ. Đó là sự hài lòng của việc làm chủ hệ thống.
- **Findings:** Tối ưu hóa không phải là "đoán mò". Mọi thứ đều được hiển thị rõ ràng trong Execution Plan. Nếu không xem Plan, bạn chỉ đang mò mẫm trong bóng tối.
- **Futures:** Trong kỷ nguyên Big Data, viết SQL "chạy được" là chưa đủ. Viết SQL "chạy nhanh và rẻ" (Cost-effective) là tiêu chuẩn bắt buộc cho mọi Senior Data Analyst.

---
Nguồn: [[SOURCE_TOOL_SQL_Pocket_Guide]] (Chapter 8: Performance Tuning)
Xác nhận Rule 14 từ NotebookLM Query (2026-05-02).


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
