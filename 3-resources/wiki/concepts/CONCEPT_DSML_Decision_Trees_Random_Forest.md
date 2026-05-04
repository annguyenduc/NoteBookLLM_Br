---
file_id: CONCEPT_DSML_DECISION_TREES_RANDOM_FOREST
title: "Decision Trees & Random Forest (Cây quyết định và Rừng ngẫu nhiên)"
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
Trang này giải thích về Cây quyết định (Decision Trees) và Rừng ngẫu nhiên (Random Forest). Đây là những mô hình học máy dựa trên cấu trúc phân cấp, nổi bật với khả năng giải thích cao và hiệu suất mạnh mẽ. Random Forest, bằng cách kết hợp nhiều cây, giúp khắc phục nhược điểm lớn nhất của Cây quyết định là tính dễ quá khớp (Overfitting).

## ## Key Claims / Summary
1.  **Hierarchical Splitting**: Chia dữ liệu dựa trên các tiêu chí (Entropy/Gini) để tối đa hóa sự thuần khiết (Purity) trong các nhóm.
2.  **Ensemble Power**: Random Forest sử dụng cơ chế Bagging để giảm phương sai và tăng tính ổn định.
3.  **Feature Importance**: Cung cấp khả năng xếp hạng tầm quan trọng của các đặc trưng trong mô hình.

## 1. Định nghĩa
Đây là các thuật toán dựa trên cấu trúc phân cấp, cực kỳ mạnh mẽ và dễ giải thích trong các bài toán phân tích dữ liệu thực tế.

## 2. Nguyên lý cốt lõi (Core Principle)
1. **Decision Tree (Cây quyết định):** Chia dữ liệu thành các nhóm nhỏ hơn dựa trên các câu hỏi "Có/Không". Dễ hiểu nhưng dễ bị Overfitting.
2. **Random Forest (Rừng ngẫu nhiên):** Kết hợp nhiều cây quyết định lại với nhau. Kết quả cuối cùng là "biểu quyết" (Voting) từ hàng trăm cây, giúp tăng độ chính xác và giảm Overfitting.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Dự đoán khách hàng có rời bỏ (Churn) hay không. Cây quyết định sẽ hỏi: "Hợp đồng > 1 năm?", "Chi tiêu > 50 USD?". Random Forest thực hiện hàng ngàn phép thử như vậy trên các tập con của dữ liệu để đưa ra dự báo tin cậy nhất. (Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] Page 40-45).
- **Ẩn dụ sư phạm (Pedagogical)**: Decision Tree giống như sơ đồ "Nếu... Thì..." để quyết định cuối tuần có đi chơi hay không. Random Forest giống như việc bạn hỏi ý kiến 100 người bạn khác nhau. Ý kiến của số đông (đại diện cho "Rừng") thường sẽ chính xác hơn ý kiến của một người duy nhất.

## ## Source Tracing
- **Nguồn**: [[SOURCE_DSML_Data_Analytics_Concepts]] — Page 40-50.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
