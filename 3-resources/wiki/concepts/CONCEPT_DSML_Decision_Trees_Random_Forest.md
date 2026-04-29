---
file_id: "WIKI_CONCEPT_DSML_DECISION_TREES_RANDOM_FOREST"
title: "Cây quyết định và Rừng ngẫu nhiên (Decision Trees & Random Forest)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DSML", "Algorithms"]
source: "`DSML_Data_Analytics_Concepts`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Cây quyết định và Rừng ngẫu nhiên

Đây là các thuật toán dựa trên cấu trúc phân cấp, cực kỳ mạnh mẽ và dễ giải thích trong các bài toán phân tích dữ liệu thực tế.

## 核心 (Core Principle)
1. **Decision Tree (Cây quyết định):** Chia dữ liệu thành các nhóm nhỏ hơn dựa trên các câu hỏi "Có/Không". Dễ hiểu nhưng dễ bị Overfitting.
2. **Random Forest (Rừng ngẫu nhiên):** Kết hợp nhiều cây quyết định lại với nhau. Kết quả cuối cùng là "biểu quyết" (Voting) từ hàng trăm cây, giúp tăng độ chính xác và giảm Overfitting.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 40-45 mô tả việc dự đoán khách hàng có rời bỏ (Churn) hay không. Cây quyết định sẽ hỏi: "Hợp đồng > 1 năm?", "Chi tiêu > 50 USD?". Random Forest sẽ thực hiện hàng ngàn phép thử như vậy trên các tập con của dữ liệu để đưa ra dự báo tin cậy nhất.

### 2. Ứng dụng sư phạm (Pedagogical Application)
- **Decision Tree:** Giống như một sơ đồ "Nếu... Thì..." để quyết định cuối tuần có đi chơi hay không (Nếu trời mưa -> Ở nhà; Nếu trời nắng -> Đi chơi).
- **Random Forest:** Giống như việc bạn hỏi ý kiến 100 người bạn khác nhau về việc có nên mua một món đồ hay không. Ý kiến của số đông (đại diện cho "Rừng") thường sẽ chính xác hơn ý kiến của một người duy nhất.

## Liên kết tư duy
- [[CONCEPT_DSML_Supervised_vs_Unsupervised]]
- [[CONCEPT_DSML_Overfitting_Prevention]]

## 4F — Phản tư sư phạm
- **Facts:** Random Forest là thuật toán "quốc dân" vì nó hoạt động tốt trên hầu hết mọi tập dữ liệu mà không cần tinh chỉnh nhiều.
- **Feelings:** Học sinh rất thích Cây quyết định vì nó có thể vẽ ra biểu đồ trực quan (Visualize), giúp các em hiểu máy tính "nghĩ" như thế nào.
- **Findings:** Sự đa dạng của các cây trong rừng chính là chìa khóa tạo nên sức mạnh.
- **Futures:** XGBoost và LightGBM là những phiên bản nâng cao hơn của cây quyết định mà nhà phân tích cần tìm hiểu sau này.

---
Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] (Page 40-50) (Xác nhận Rule 14 từ: `DSML_Data_Analytics_Concepts`)
