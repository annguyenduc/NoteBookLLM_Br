---
file_id: "WIKI_THINK_DATA_MINING_TASKS"
title: "9 Nhiệm vụ Khai thác Dữ liệu Phổ biến"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Thinking", "Data_Mining", "Tasks", "Taxonomy"]
source: "[[SOURCE_THINK_Data_Science_for_Business]]"
status: "draft"
created: "2026-04-28"
last_updated: "2026-04-28"
---

# 📌 9 Nhiệm vụ Khai thác Dữ liệu Phổ biến

![Minh họa 9 Nhiệm vụ](file:///d:/NoteBookLLM_Br/3-resources/wiki/assets/WIKI_IMG_THINK_Data_Mining_Tasks.png)

## 1. Phân loại nhiệm vụ (Taxonomy)

| Nhóm | Nhiệm vụ | Mô tả ngắn |
| :--- | :--- | :--- |
| **Dự đoán (Predictive)** | **Classification** | Dự đoán đối tượng thuộc nhóm nào (Nhãn). |
| | **Regression** | Dự đoán một giá trị số cụ thể. |
| | **Link Prediction** | Dự đoán sự tồn tại của mối quan hệ. |
| **Mô tả (Descriptive)** | **Similarity Matching** | Tìm các thực thể giống nhau nhất. |
| | **Clustering** | Nhóm tự động các thực thể tương đồng. |
| | **Co-occurrence** | Tìm các món đồ hay xuất hiện cùng nhau. |
| | **Profiling** | Đặc tả hành vi tiêu biểu của một nhóm. |
| | **Data Reduction** | Nén thông tin nhưng giữ bản chất. |
| | **Causal Modeling** | Tìm hiểu nguyên nhân gây ra kết quả. |

## 2. Chi tiết các nhiệm vụ trọng tâm (Structural Fidelity - Trang 21-25)

1.  **Classification (Phân lớp)**: Trả lời câu hỏi "Có hay Không?" hoặc "A hay B?". Đây là nhiệm vụ phổ biến nhất.
2.  **Regression (Hồi quy)**: Trả lời câu hỏi "Bao nhiêu?".
3.  **Similarity Matching**: Nền tảng của các hệ thống gợi ý (Recommendation).
4.  **Clustering**: Dùng để khám phá cấu trúc dữ liệu mà không cần nhãn trước (Unsupervised).
5.  **Co-occurrence Grouping**: Còn gọi là Market Basket Analysis. "Nếu khách mua X, họ thường mua thêm Y".

---

## 3. 💡 Ví dụ đối chiếu (Mandatory)

### 3.1. Ví dụ từ sách (Original)
**Tình huống**: Quản lý khách hàng của một ngân hàng (Trang 21).
-   **Classification**: Dự đoán khách hàng nào sẽ phản hồi với lời mời mở thẻ tín dụng mới.
-   **Clustering**: Nhóm khách hàng dựa trên hành vi chi tiêu để thiết kế các gói ưu đãi riêng biệt.
-   **Similarity Matching**: Tìm các khách hàng có hành vi giống với những khách hàng tốt nhất hiện tại.
-   **Profiling**: Xác định mức chi tiêu "bình thường" để phát hiện các giao dịch gian lận (Anomaly Detection).

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
**Tình huống**: Quản lý thiết bị trong phòng Lab STEAM.
-   **Classification**: Dự đoán một bo mạch (Arduino/YoloBit) có khả năng bị hỏng dựa trên số giờ sử dụng và độ ẩm.
-   **Co-occurrence**: [Phóng tác] Thấy rằng học sinh mượn Cảm biến khoảng cách thường mượn kèm Loa Buzzer (để làm xe tránh vật cản).
-   **Data Reduction**: Nén dữ liệu từ các cảm biến IoT (nhiệt độ, ánh sáng mỗi giây) thành các giá trị trung bình hàng giờ để tiết kiệm bộ nhớ và dễ phân tích xu hướng.

## 4. 4F — Phản tư sư phạm
-   **Facts**: Hầu hết mọi bài toán kinh doanh đều có thể quy về 1 hoặc kết hợp nhiều nhiệm vụ trong 9 loại này.
-   **Feelings**: Giúp giáo viên/nhà quản lý cảm thấy tự tin khi "đặt hàng" (Scoping) cho các chuyên gia dữ liệu.
-   **Findings**: Sai lầm lớn nhất là dùng nhầm nhiệm vụ (ví dụ: dùng Clustering khi thực tế cần Classification).
-   **Futures**: Hướng dẫn học sinh phân loại ý tưởng dự án của mình vào 9 nhóm này để chọn thuật toán phù hợp.

## 📖 Nguồn
-   [[SOURCE_THINK_Data_Science_for_Business]] — Trang 19-26.

---
[AUDITOR] Rule 14: Đã xác nhận fact tồn tại trong file raw gốc.
