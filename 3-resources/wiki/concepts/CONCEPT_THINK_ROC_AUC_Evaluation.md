---
title: "CONCEPT: Đánh giá mô hình bằng ROC và AUC"
type: concept
tags: ["Thinking", "Evaluation", "Metrics", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Đánh giá mô hình bằng ROC và AUC

## 1. Định nghĩa
**Đường cong ROC** (Receiver Operating Characteristic) là biểu đồ thể hiện khả năng phân loại của mô hình ở mọi ngưỡng threshold. **AUC** (Area Under the Curve) là diện tích dưới đường cong đó, đại diện cho xác suất mô hình xếp hạng một cá thể dương tính cao hơn một cá thể âm tính.

## 2. Nguyên lý / Cấu trúc
- **Trục tung (Y)**: True Positive Rate (Sensitivity) - Khả năng tìm thấy đúng người có bệnh.
- **Trục hoành (X)**: False Positive Rate (1 - Specificity) - Tỷ lệ báo động nhầm.
- **AUC = 1.0**: Mô hình hoàn hảo.
- **AUC = 0.5**: Mô hình tương đương với việc tung đồng xu (ngẫu nhiên).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: So sánh hai mô hình dự đoán gian lận tín dụng.
> **Ứng dụng**: Mô hình A có độ chính xác (Accuracy) 90% nhưng AUC chỉ 0.6. Mô hình B có Accuracy 85% nhưng AUC lên đến 0.8. Tác giả khuyên dùng mô hình B vì nó ổn định hơn trong việc phân tách các nhóm đối tượng ở các ngưỡng rủi ro khác nhau.
> **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Chương 7 & 8.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Đánh giá một bài kiểm tra trắc nghiệm giúp phân loại học sinh "Đạt" và "Không đạt".
> **Ứng dụng**: 
> - Nếu một bài kiểm tra có AUC thấp, nghĩa là câu hỏi quá dễ hoặc quá khó đến mức không phân biệt được học sinh giỏi và học sinh yếu.
> - Một bài kiểm tra chất lượng (AUC cao) sẽ giúp giáo viên tự tin rằng những em đạt điểm cao thực sự nắm vững kiến thức hơn những em điểm thấp.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Trang 180-205.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_ROC_AUC_Evaluation.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, giải thích trực giác AUC qua chất lượng bài kiểm tra."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
