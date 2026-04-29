---
file_id: "WIKI_CONCEPT_DSML_CLUSTERING_KMEANS"
title: "Phân cụm K-Means (Clustering & K-Means)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DSML", "Unsupervised"]
source: "`DSML_Data_Analytics_Concepts`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Phân cụm K-Means (Clustering & K-Means)

Phân cụm là kỹ thuật Học không giám sát dùng để nhóm các đối tượng tương đồng lại với nhau mà không cần biết nhãn trước.

## 核心 (Core Principle)
1. **K-Means:** Thuật toán phân cụm phổ biến nhất.
2. **Quy trình:**
   - Chọn $K$ (số lượng cụm muốn tìm).
   - Gán ngẫu nhiên $K$ tâm cụm (Centroids).
   - Gom các điểm dữ liệu về tâm cụm gần nhất.
   - Cập nhật tâm cụm bằng cách tính trung bình các điểm trong cụm đó.
   - Lặp lại cho đến khi tâm cụm không thay đổi.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 55-60 mô tả việc phân khúc khách hàng (Customer Segmentation). Một công ty điện thoại không biết khách hàng của mình gồm những nhóm nào. K-Means tự động tìm ra 3 nhóm: "Người dùng tiết kiệm", "Người dùng công nghệ cao" và "Người dùng giải trí" dựa trên thói quen chi tiêu và dung lượng Data.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử bạn có một đống thẻ bài Pokemon nhưng không biết tên hay hệ của chúng:
- Bạn yêu cầu máy phân thành 4 cụm (K=4) dựa trên "Màu sắc" và "Sức mạnh".
- Máy sẽ tự động gom các thẻ màu đỏ (hệ Lửa) vào một đống, màu xanh (hệ Nước) vào một đống... dù nó không biết "Hệ" là gì.

## Liên kết tư duy
- [[CONCEPT_DSML_Supervised_vs_Unsupervised]]
- [[CONCEPT_DSML_Model_Evaluation_Metrics]]

## 4F — Phản tư sư phạm
- **Facts:** Chọn số lượng cụm $K$ (Elbow method) là bước khó nhất và mang tính chủ quan.
- **Feelings:** Việc thấy dữ liệu thô tự động "vón cục" lại thành các nhóm có ý nghĩa thường gây ngạc nhiên cho người học.
- **Findings:** K-Means rất nhạy cảm với các đơn vị đo lường khác nhau (cần chuẩn hóa dữ liệu trước khi chạy).
- **Futures:** Phân cụm là nền tảng cho các hệ thống gợi ý (Recommendation systems) và phát hiện gian lận (Anomaly detection).

---
Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] (Page 55-65) (Xác nhận Rule 14 từ: `DSML_Data_Analytics_Concepts`)
