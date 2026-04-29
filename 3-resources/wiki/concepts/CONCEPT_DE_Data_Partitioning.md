---
file_id: "WIKI_CONCEPT_DE_DATA_PARTITIONING"
title: "Phân vùng dữ liệu (Data Partitioning)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DE", "Performance"]
source: "`DE_Fundamentals_of_Data_Engineering`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Phân vùng dữ liệu (Data Partitioning)

Phân vùng là kỹ thuật chia một bảng dữ liệu khổng lồ thành các phần nhỏ hơn (Partitions) để quản lý dễ dàng hơn và tăng hiệu suất truy vấn.

## 核心 (Core Principle)
1. **Partition by Range:** Chia theo khoảng giá trị (ví dụ: chia theo Năm hoặc Tháng).
2. **Partition by List:** Chia theo danh mục (ví dụ: chia theo Khu vực: Miền Bắc, Miền Nam).
3. **Partition by Hash:** Chia đều dữ liệu dựa trên một hàm băm (dùng khi không có tiêu chí chia rõ ràng).
4. **Lợi ích:** "Partition Pruning" – Hệ thống chỉ đọc phân vùng cần thiết, bỏ qua phần còn lại.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 100-105 mô tả việc quản lý bảng giao dịch ngân hàng có hàng tỷ dòng. Bằng cách phân vùng theo `transaction_date`, một câu hỏi về "doanh số ngày hôm qua" sẽ chỉ quét một phân vùng nhỏ thay vì quét toàn bộ lịch sử 10 năm của ngân hàng.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng tủ hồ sơ học sinh:
- **Không phân vùng:** Tất cả hồ sơ để chung một ngăn kéo (Phải tìm rất lâu).
- **Phân vùng:** Mỗi ngăn kéo chứa hồ sơ của một Khối lớp (Khối 10, Khối 11, Khối 12).
Khi cần tìm học sinh lớp 10, bạn chỉ cần mở ngăn kéo tương ứng. Đây là cách trực quan nhất để giải thích về hiệu suất truy vấn.

## Liên kết tư duy
- [[CONCEPT_DE_Indexing_Optimization]]
- [[CONCEPT_DE_Data_Architecture_Basics]]

## 4F — Phản tư sư phạm
- **Facts:** Phân vùng giúp "chia để trị" đống dữ liệu khổng lồ.
- **Feelings:** Nhà phân tích thường "quên" lọc theo cột phân vùng (ví dụ: quên lọc Ngày), dẫn đến việc truy vấn tốn kém không cần thiết.
- **Findings:** Phân vùng quá nhỏ (Over-partitioning) cũng có thể làm giảm hiệu suất do overhead quản lý file.
- **Futures:** Các hệ thống hiện đại như BigQuery tự động quản lý việc phân vùng để giảm tải cho con người.

---
Nguồn: [[SOURCE_DE_Fundamentals_of_Data_Engineering]] (Page 100-115, Chapter 4) (Xác nhận Rule 14 từ: `DE_Fundamentals_of_Data_Engineering`)
