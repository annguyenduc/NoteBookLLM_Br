---
file_id: CASE_STUDY_Churn_Prediction
prefix: WIKI
tags: [DA, CASE_STUDY, DSML, PYTHON, EDUCATION]
source: `DA_Practical_Scenarios`
status: drafting
created: "2026-04-29"
last_updated: "2026-04-29"
---

# 🕵️ Case Study #1: Dự báo nguy cơ học viên bỏ học (Churn Prediction)

## 1. Bài toán (Problem Statement)
Một trung tâm EdTech nhận thấy tỷ lệ học viên không gia hạn khóa học tăng cao. Mục tiêu là xây dựng một mô hình dự báo sớm những học viên có khả năng "rời bỏ" (Churn) dựa trên lịch sử tương tác và điểm số để giáo viên có thể hỗ trợ kịp thời.

## 2. Dữ liệu (Data Description)
*   `student_id`: ID định danh.
*   `login_frequency`: Số lần đăng nhập mỗi tuần.
*   `avg_score`: Điểm trung bình các bài kiểm tra.
*   `forum_activity`: Số bài viết/thảo luận trên diễn đàn.
*   `churn`: (Label) 1 nếu bỏ học, 0 nếu tiếp tục.

## 3. Quy trình thực hiện (Execution Steps)

### Bước 1: Khám phá & Làm sạch (Exploratory Data Analysis - EDA)
*   Sử dụng [[CONCEPT_Pandas_Data_Cleaning]] để xử lý dữ liệu thiếu (ví dụ: học viên chưa bao giờ đăng nhập).
*   Sử dụng [[CONCEPT_STAT_Estimates_of_Location]] để xem mức độ tương tác trung bình.

### Bước 2: Phân tích nhân tố (Feature Engineering)
*   Tính toán `engagement_score` từ `login_frequency` và `forum_activity`.
*   Áp dụng [[CONCEPT_DSML_Feature_Engineering_Basics]].

### Bước 3: Mô hình hóa (Modeling)
*   Sử dụng [[CONCEPT_DSML_Decision_Trees_Random_Forest]] để phân loại học viên.
*   Giải thích lý do học viên bỏ học (ví dụ: điểm thấp hay lười đăng nhập?).

### Bước 4: Đánh giá (Evaluation)
*   Sử dụng [[CONCEPT_DSML_Model_Evaluation_Metrics]] (Focus vào **Recall** để không bỏ sót học viên nguy cơ).

## 4. 4F — Phản tư sư phạm
*   **Facts:** Dữ liệu cho thấy 80% học viên bỏ học có `login_frequency` < 1 lần/tuần trong tháng cuối.
*   **Feelings:** DA thường cảm thấy "áp lực" khi phải cân bằng giữa độ chính xác và tính giải thích được của mô hình cho giáo viên.
*   **Findings:** Tương tác diễn đàn (`forum_activity`) là chỉ báo mạnh mẽ hơn cả điểm số trong việc dự báo churn.
*   **Futures:** Cần thiết kế hệ thống cảnh báo tự động (Alert) gửi thẳng cho trợ giảng khi học viên có chỉ số engagement sụt giảm đột ngột.

---
## 🔗 Liên kết tư duy
- [[CONCEPT_DSML_Supervised_vs_Unsupervised]]
- [[CONCEPT_VIZ_Interactive_Dashboard_Design]]
- [[SYNTHESIS_DA_Case_Study_Library]]
