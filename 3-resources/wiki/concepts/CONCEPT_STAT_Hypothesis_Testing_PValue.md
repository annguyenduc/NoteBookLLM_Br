---
file_id: "WIKI_CONCEPT_STAT_HYPOTHESIS_TESTING_PVALUE"
title: "Kiểm định giả thuyết và P-Value (Hypothesis Testing & P-Value)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Testing"]
source: "`STAT_Practical_Statistics_for_Data_Scientists`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Kiểm định giả thuyết và P-Value

Đây là quy trình ra quyết định dựa trên dữ liệu để xác định xem một kết quả quan sát được là thực sự có ý nghĩa hay chỉ là do ngẫu nhiên.

## 核心 (Core Principle)
1. **Giả thuyết không ($H_0$):** Giả định rằng không có sự khác biệt (ví dụ: Thuốc này không có tác dụng).
2. **Giả thuyết thay thế ($H_1$):** Giả định có sự khác biệt.
3. **P-Value:** Xác suất thu được kết quả quan sát (hoặc cực đoan hơn) nếu $H_0$ là đúng.
   - Nếu P-Value $\le$ mức ý nghĩa ($\alpha$, thường là 0.05): Bác bỏ $H_0$ -> Kết quả có ý nghĩa thống kê.
   - Nếu P-Value $> 0.05$: Không đủ bằng chứng để bác bỏ $H_0$.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 90-100 thảo luận về thử nghiệm A/B cho một trang web. Chúng ta so sánh tỷ lệ nhấn chuột (CTR) của nút màu xanh và nút màu đỏ. P-Value sẽ cho biết liệu sự chênh lệch CTR là do màu sắc thực sự hay chỉ là biến động ngẫu nhiên của người dùng trong ngày hôm đó.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử giáo viên áp dụng phương pháp dạy mới (Project-based learning) và thấy điểm trung bình tăng từ 7 lên 7.5:
- **$H_0$:** Phương pháp mới không làm thay đổi điểm số.
- **P-Value = 0.02:** (nhỏ hơn 0.05). Giáo viên có thể tự tin kết luận rằng phương pháp mới thực sự hiệu quả và không phải do học sinh "gặp may" trong bài kiểm tra này.

## Liên kết tư duy
- [[CONCEPT_STAT_T_Test_ANOVA]]
- [[CONCEPT_STAT_Confidence_Intervals]]

## 4F — Phản tư sư phạm
- **Facts:** P-Value không đo lường độ lớn của hiệu ứng (Effect size), chỉ đo lường độ tin cậy của kết quả.
- **Feelings:** P-Value < 0.05 thường được coi là "tấm vé vàng" trong nghiên cứu, dẫn đến việc lạm dụng (P-hacking).
- **Findings:** Ý nghĩa thống kê không đồng nghĩa với ý nghĩa thực tế (Practical significance).
- **Futures:** Cần dạy học sinh cách kết hợp P-Value với Effect size để có cái nhìn toàn diện hơn.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 90-110, Chapter 3) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)
