---
file_id: "WIKI_CONCEPT_DSML_OVERFITTING_PREVENTION"
title: "Phòng tránh quá khớp (Overfitting Prevention)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DSML", "Model_Health"]
source: "`DSML_Data_Analytics_Concepts`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Phòng tránh quá khớp (Overfitting Prevention)

Overfitting là hiện tượng mô hình học quá kỹ dữ liệu huấn luyện (bao gồm cả nhiễu) dẫn đến khả năng dự báo kém trên dữ liệu mới.

## 核心 (Core Principle)
1. **Dấu hiệu:** Độ chính xác trên tập Train cực cao, nhưng trên tập Test cực thấp.
2. **Nguyên nhân:** Mô hình quá phức tạp hoặc dữ liệu huấn luyện quá ít.
3. **Cách khắc phục:**
   - **Cross-Validation:** Chia dữ liệu thành nhiều phần để kiểm tra chéo.
   - **Regularization:** Phạt các tham số quá lớn (L1/L2).
   - **Pruning:** Cắt tỉa bớt các nhánh không quan trọng (trong cây quyết định).
   - **Early Stopping:** Dừng học sớm khi thấy sai số trên tập kiểm tra bắt đầu tăng.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Tài liệu (trang 25-30) lấy ví dụ về việc học thuộc lòng các câu trả lời trong một đề thi cũ. Khi đi thi thật với câu hỏi có chút thay đổi, người học thuộc lòng sẽ thất bại vì không hiểu bản chất (đây chính là Overfitting).

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng một vận động viên điền kinh:
- **Overfitting:** Anh ta chỉ tập chạy trên đúng một con đường mòn quen thuộc trong nhà. Khi ra thi đấu ở sân vận động ngoài trời với gió và địa hình khác, anh ta không thể chạy được.
- **Giải pháp:** Phải cho anh ta tập ở nhiều môi trường khác nhau (Cross-validation) để tăng tính thích nghi (Generalization).

## Liên kết tư duy
- [[CONCEPT_DSML_Model_Evaluation_Metrics]]
- [[CONCEPT_DSML_Supervised_vs_Unsupervised]]

## 4F — Phản tư sư phạm
- **Facts:** Overfitting là "kẻ thù" lớn nhất của các mô hình Machine Learning phức tạp.
- **Feelings:** Nhà phân tích mới thường rất hào hứng khi thấy Accuracy đạt 99% mà không biết đó là dấu hiệu của thảm họa Overfitting.
- **Findings:** Sự đánh đổi giữa Bias (Độ lệch) và Variance (Phương sai) là cốt lõi của bài toán này.
- **Futures:** AutoML đang tích hợp sẵn các cơ chế chống Overfitting tự động.

---
Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] (Page 25-32) (Xác nhận Rule 14 từ: `DSML_Data_Analytics_Concepts`)
