---
file_id: "WIKI_CONCEPT_STAT_CENTRAL_LIMIT_THEOREM"
title: "Định lý giới hạn trung tâm (Central Limit Theorem)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Sampling"]
source: "`STAT_Practical_Statistics_for_Data_Scientists`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Định lý giới hạn trung tâm (Central Limit Theorem)

Định lý giới hạn trung tâm (CLT) là nền tảng của mọi kỹ thuật lấy mẫu và suy diễn thống kê trong khoa học dữ liệu.

## 核心 (Core Principle)
1. **Nguyên lý:** Khi bạn lấy nhiều mẫu ngẫu nhiên từ một quần thể, giá trị trung bình của các mẫu đó sẽ có xu hướng hình thành một **Phân phối chuẩn**, bất kể quần thể gốc có hình dạng gì.
2. **Điều kiện:** Kích thước mẫu ($n$) phải đủ lớn (thường là $n \ge 30$).
3. **Ý nghĩa:** Cho phép chúng ta sử dụng các công cụ thống kê dành cho phân phối chuẩn (như Z-score, P-value) lên hầu hết mọi loại dữ liệu thực tế.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 55-60 mô tả thí nghiệm lấy mẫu từ một phân phối cực kỳ lệch (Skewed). Sau khi thực hiện lấy trung bình mẫu hàng ngàn lần, đồ thị kết quả biến thành hình chuông đối xứng hoàn hảo. Điều này chứng minh rằng chúng ta có thể ước lượng trung bình quần thể từ các mẫu nhỏ.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử bạn muốn biết chiều cao trung bình của học sinh toàn thành phố:
- Bạn không thể đo tất cả (Quần thể).
- Bạn chọn ngẫu nhiên 30 học sinh ở 50 trường khác nhau.
- Trung bình chiều cao của mỗi nhóm 30 bạn này sẽ tuân theo quy luật CLT, giúp bạn tính toán được chiều cao trung bình toàn thành phố với một độ tin cậy nhất định.

## Liên kết tư duy
- [[CONCEPT_STAT_Probability_Distributions]]
- [[CONCEPT_STAT_Confidence_Intervals]]

## 4F — Phản tư sư phạm
- **Facts:** CLT là "phép màu" của toán học giúp biến sự hỗn loạn thành trật tự.
- **Feelings:** Học sinh thường thấy khó tin rằng "bất kể hình dạng gốc là gì" kết quả vẫn ra hình chuông.
- **Findings:** Sai số tiêu chuẩn (Standard Error) giảm đi khi kích thước mẫu tăng lên.
- **Futures:** Cần cho học sinh thực hành tung xúc xắc hoặc dùng code Python để tự mô phỏng CLT nhằm "thấy mới tin".

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 55-65, Chapter 2) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)
