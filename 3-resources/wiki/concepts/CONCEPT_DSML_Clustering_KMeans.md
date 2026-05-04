---
file_id: CONCEPT_DSML_CLUSTERING_KMEANS
title: "K-Means Clustering (Phân cụm K-Means)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_DSML_Data_Analytics_Concepts]]"
---

## ## For future Claude
Trang này định nghĩa thuật toán K-Means - một trong những kỹ thuật phân cụm (Clustering) phổ biến nhất trong Học không giám sát. K-Means giúp tự động khám phá các cấu trúc ẩn và nhóm các đối tượng tương đồng trong dữ liệu mà không cần nhãn trước, ứng dụng rộng rãi trong phân khúc khách hàng và nén hình ảnh.

## ## Key Claims / Summary
1.  **Iterative Centroid Update**: Thuật toán lặp lại việc gán điểm vào tâm cụm và cập nhật tâm cụm cho đến khi hội tụ.
2.  **Sensitivity to Initial Seeds**: Kết quả có thể thay đổi tùy vào vị trí tâm cụm ban đầu (thường dùng K-Means++ để khắc phục).
3.  **Elbow Method**: Kỹ thuật phổ biến để chọn số lượng cụm $K$ tối ưu.

## 1. Định nghĩa
Phân cụm là kỹ thuật Học không giám sát dùng để nhóm các đối tượng tương đồng lại với nhau mà không cần biết nhãn trước.

## 2. Nguyên lý cốt lõi (Core Principle)
1. **K-Means:** Thuật toán phân cụm phổ biến nhất.
2. **Quy trình:**
   - Chọn $K$ (số lượng cụm muốn tìm).
   - Gán ngẫu nhiên $K$ tâm cụm (Centroids).
   - Gom các điểm dữ liệu về tâm cụm gần nhất.
   - Cập nhật tâm cụm bằng cách tính trung bình các điểm trong cụm đó.
   - Lặp lại cho đến khi tâm cụm không thay đổi.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Một công ty điện thoại không biết khách hàng của mình gồm những nhóm nào. K-Means tự động tìm ra 3 nhóm: "Người dùng tiết kiệm", "Người dùng công nghệ cao" và "Người dùng giải trí" dựa trên thói quen chi tiêu và dung lượng Data. (Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] Page 55-60).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn có một thùng thẻ bài Pokemon lộn xộn. Bạn yêu cầu máy phân thành 4 cụm (K=4) dựa trên "Màu sắc" và "Sức mạnh". Máy sẽ tự động gom các thẻ màu đỏ (hệ Lửa) vào một đống, màu xanh (hệ Nước) vào một đống... dù nó không biết khái niệm "Hệ" là gì.

## ## Source Tracing
- **Nguồn**: [[SOURCE_DSML_Data_Analytics_Concepts]] — Page 55-65.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
