---
file_id: SYNTHESIS_DA_Core_Workflow
title: Quy trình làm việc cốt lõi của Data Analyst (80/20 & Deepening)
category: SYNTHESIS
domain: Data_Analysis
status: verified
---

relationships:
  - type: "relates_to"
    target: "[[ENTITY_PANDAS]]"
  - type: "relates_to"
    target: "[[ENTITY_Python]]"
# Data Analyst Core Workflow (End-to-End)

> [!IMPORTANT]
> Đây là trang tổng hợp kết nối toàn bộ 8 nhóm kỹ năng quan trọng nhất thành một quy trình làm việc thực tế, từ lúc nhận bài toán đến khi triển khai các phân tích chuyên sâu.

## 1. Giai đoạn 1: Hiểu bài toán & Hạ tầng (Thinking & DE)
Trước khi chạm vào dữ liệu, phải hiểu rõ mục tiêu và nơi lưu trữ.
- **Xác định bối cảnh:** Sử dụng framework [[CONCEPT_THINK_CoNVO_Framework]] để hiểu Context, Need, Vision, và Outcome.
- **Hiểu hạ tầng:** Biết dữ liệu nằm ở [[CONCEPT_DE_Data_Architecture_Basics]] (Warehouse hay Lake) và được xử lý qua quy trình [[CONCEPT_DE_ETL_ELT_Workflows]].
- **Thiết kế bảng:** Nắm vững [[CONCEPT_DE_Data_Modeling_Star_Schema]] để thiết kế Schema tối ưu cho truy vấn.
- **Tối ưu hóa hạ tầng:** Sử dụng [[CONCEPT_DE_Indexing_Optimization]] và [[CONCEPT_DE_Data_Partitioning]] để quản lý và truy vấn các bảng dữ liệu khổng lồ.

## 2. Giai đoạn 2: Trích xuất & Tiền xử lý ([[ENTITY_SQL|SQL]], [[ENTITY_PANDAS|Pandas]] & DE)
- **Truy vấn:** Sử dụng [[CONCEPT_SQL_Select_And_Filter]], [[CONCEPT_SQL_Joins]] và các hàm nâng cao như [[CONCEPT_SQL_Window_Functions]], [[CONCEPT_SQL_CTEs]].
- **Tiền xử lý:** Thực hiện [[CONCEPT_PY_Pandas_Data_Cleaning]] và [[CONCEPT_DSML_Feature_Engineering_Basics]] để chuẩn bị dữ liệu cho mô hình.
- **Kiểm soát chất lượng:** Áp dụng [[CONCEPT_DE_Data_Quality_Framework]] để đảm bảo dữ liệu "sạch" trước khi phân tích.

## 3. Giai đoạn 3: Phân tích Khám phá & Suy luận (STAT)
- **Thống kê mô tả (EDA):** Sử dụng [[CONCEPT_STAT_Estimates_of_Location]] (Mean, Median) và [[CONCEPT_STAT_Estimates_of_Variability]] (SD, IQR) để hiểu đặc tính dữ liệu.
- **Lấy mẫu:** Cẩn trọng với các loại [[CONCEPT_STAT_Sampling_Biases]] có thể làm sai lệch kết quả.
- **Kiểm chứng:** Sử dụng [[CONCEPT_STAT_Hypothesis_Testing_PValue]] và [[CONCEPT_STAT_T_Test_ANOVA]] để so sánh sự khác biệt giữa các nhóm dữ liệu.
- **Độ tin cậy:** Áp dụng [[CONCEPT_STAT_Confidence_Intervals]] để báo cáo sai số.

## 4. Giai đoạn 4: Mô hình hóa & Dự báo (STAT & DSML)
- **Hồi quy:** Dự báo giá trị liên tục qua [[CONCEPT_STAT_Linear_Regression]].
- **Phân loại & Phân cụm:** Sử dụng [[CONCEPT_DSML_Decision_Trees_Random_Forest]] cho bài toán phân loại và [[CONCEPT_DSML_Clustering_KMeans]] cho bài toán không giám sát.
- **Đánh giá:** Sử dụng các chỉ số trong [[CONCEPT_DSML_Model_Evaluation_Metrics]] (Accuracy, Recall, RMSE) và tránh [[CONCEPT_DSML_Overfitting_Prevention]].

## 5. Giai đoạn 5: Trực quan hóa & Dashboard (Visualization)
- **Tâm lý học thị giác:** Áp dụng [[CONCEPT_VIZ_Gestalt_Laws_in_Design]] để thiết kế thu hút.
- **Thiết kế:** Áp dụng [[CONCEPT_VIZ_Design_Principles]], [[CONCEPT_VIZ_Eliminating_Clutter]] và [[CONCEPT_VIZ_Focusing_Attention]].
- **Hệ thống tương tác:** Xây dựng [[CONCEPT_VIZ_Interactive_Dashboard_Design]] để người dùng tự khám phá dữ liệu.
- **Kể chuyện:** Xây dựng bài thuyết trình theo [[CONCEPT_VIZ_Data_Storytelling_Framework]].

---

## Mối liên hệ giữa các công cụ
- **SQL vs Pandas:** [[CONCEPT_SQL_Data_Preparation_Workflow]] giúp quyết định khi nào nên dùng SQL, khi nào dùng Pandas.
- **Power BI vs Tableau:** [[CONCEPT_VIZ_PowerBI_vs_Tableau]] giúp chọn công cụ báo cáo.

---
Nguồn: Tổng hợp từ lộ trình 80/20 & Deepening (Thinking with Data, SQL Cookbook, [[ENTITY_Python|Python]] for Data Analysis, Storytelling with Data, Practical Statistics, Fundamentals of DE, DSML Concepts).
[AUDITOR] Rule 14: Đã kết nối thành công TOÀN BỘ 8 nhóm tri thức thành một Master Workflow hoàn chỉnh (Vòng 2).


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
