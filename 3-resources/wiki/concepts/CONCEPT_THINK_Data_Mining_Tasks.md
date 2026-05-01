---
title: "CONCEPT: Các Tác vụ Khai thác Dữ liệu (Data Mining Tasks)"
type: concept
tags: ["Thinking", "Data_Mining", "Tasks", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Các Tác vụ Khai thác Dữ liệu (Data Mining Tasks)

## 1. Định nghĩa
Tác vụ khai thác dữ liệu là những bài toán cụ thể mà Data Analyst cần giải quyết bằng các thuật toán. Việc xác định đúng tác vụ là bước then chốt trong giai đoạn *Modeling* của CRISP-DM.

## 2. 8 Tác vụ chính (Phân loại theo DS for Business)
1.  **Classification (Phân loại)**: Dự đoán một cá thể thuộc nhóm nào (Có/Không).
2.  **Regression (Hồi quy)**: Dự đoán một giá trị số cụ thể.
3.  **Similarity Matching (Tìm kiếm tương đồng)**: Tìm cá thể giống cá thể X.
4.  **Clustering (Gom cụm)**: Chia quần thể thành các nhóm có đặc điểm chung.
5.  **Co-occurrence Grouping (Tìm quy luật đồng thời)**: Mua A thì thường mua B.
6.  **Profiling (Phác họa chân dung)**: Mô tả hành vi điển hình của một nhóm.
7.  **Link Prediction (Dự đoán liên kết)**: Đề xuất bạn bè trên MXH.
8.  **Data Reduction (Giảm chiều dữ liệu)**: Giữ lại thông tin quan trọng nhất.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Hệ thống gợi ý của Amazon.
> **Ứng dụng**: Sử dụng *Co-occurrence Grouping* để biết khách hàng mua "Sách lập trình" thường mua kèm "Chuột máy tính". Sử dụng *Similarity Matching* để gợi ý các cuốn sách cùng chủ đề.
> **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Chương 2.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Phân tích dữ liệu học tập của học sinh trên LMS.
> **Ứng dụng**: 
> - **Classification**: Dự đoán học sinh có nguy cơ trượt môn (Pass/Fail).
> - **Clustering**: Nhóm học sinh thành các mức độ năng lực (Khá, Giỏi, Trung bình) để có phương pháp dạy phù hợp.
> - **Profiling**: Phác họa chân dung "Học sinh tích cực" (vd: Đăng nhập hàng ngày, tham gia thảo luận).

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Trang 19-26.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Data_Mining_Tasks.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, liệt kê đầy đủ 8 tác vụ khai thác dữ liệu."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."
