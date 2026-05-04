---
file_id: CONCEPT_DSML_OVERFITTING_PREVENTION
title: "Overfitting Prevention (Phòng tránh quá khớp)"
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
Trang này giải thích về Overfitting - "kẻ thù" lớn nhất của các mô hình Machine Learning. Overfitting xảy ra khi mô hình học cả nhiễu trong dữ liệu huấn luyện, dẫn đến khả năng dự báo kém trên dữ liệu thực tế. Chúng ta cần áp dụng các kỹ thuật Regularization và Cross-Validation để đảm bảo mô hình có tính tổng quát hóa cao.

## ## Key Claims / Summary
1.  **Generalization Goal**: Mục tiêu cuối cùng là mô hình hoạt động tốt trên dữ liệu mới, không phải đạt 100% trên dữ liệu cũ.
2.  **Regularization**: Kỹ thuật "phạt" các tham số quá lớn để giữ cho mô hình đơn giản.
3.  **Cross-Validation**: Phương pháp kiểm tra tính ổn định của mô hình bằng cách chia nhỏ dữ liệu nhiều lần.

## 1. Định nghĩa
Overfitting là hiện tượng mô hình học quá kỹ dữ liệu huấn luyện dẫn đến khả năng dự báo kém trên dữ liệu mới.

## 2. Các kỹ thuật phòng tránh chính
- **Cross-Validation:** Chia dữ liệu thành nhiều phần để kiểm tra chéo.
- **Regularization:** Phạt các tham số quá lớn (L1/L2).
- **Pruning:** Cắt tỉa bớt các nhánh không quan trọng (trong cây quyết định).
- **Early Stopping:** Dừng học sớm khi thấy sai số trên tập kiểm tra bắt đầu tăng.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Học thuộc lòng các câu trả lời trong một đề thi cũ. Khi đi thi thật với câu hỏi có chút thay đổi, người học thuộc lòng sẽ thất bại vì không hiểu bản chất (đây chính là Overfitting). (Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] Page 25-30).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một vận động viên điền kinh chỉ tập chạy trên đúng một con đường mòn quen thuộc trong nhà. Khi ra thi đấu ở sân vận động ngoài trời với gió và địa hình khác, anh ta không thể chạy được. Anh ta cần tập ở nhiều môi trường khác nhau (Cross-validation) để tăng tính thích nghi.

## ## Source Tracing
- **Nguồn**: [[SOURCE_DSML_Data_Analytics_Concepts]] — Page 25-32.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
