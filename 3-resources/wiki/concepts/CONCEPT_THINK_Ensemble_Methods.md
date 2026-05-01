---
title: "CONCEPT: Phương pháp Học máy Kết hợp (Ensemble Methods)"
type: concept
tags: ["Thinking", "Modeling", "Optimization", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Phương pháp Học máy Kết hợp (Ensemble Methods)

## 1. Định nghĩa
Ensemble Methods là kỹ thuật kết hợp nhiều mô hình học máy lại với nhau để tạo ra một mô hình duy nhất có hiệu suất cao hơn, ổn định hơn và ít thiên kiến hơn so với bất kỳ mô hình riêng lẻ nào.

## 2. Các kỹ thuật phổ biến
- **Bagging (Bootstrap Aggregating)**: Xây dựng nhiều mô hình độc lập và lấy trung bình kết quả (vd: Random Forest). Giúp giảm phương sai (variance).
- **Boosting**: Xây dựng các mô hình nối tiếp nhau, mô hình sau tập trung sửa lỗi của mô hình trước (vd: XGBoost). Giúp giảm độ chệch (bias).
- **Stacking**: Dùng kết quả đầu ra của các mô hình cơ sở làm đầu vào cho một mô hình cuối cùng để đưa ra dự đoán.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Cuộc thi Netflix Prize về hệ thống gợi ý phim.
> **Ứng dụng**: Đội chiến thắng không sử dụng một thuật toán đơn lẻ mà kết hợp hàng trăm mô hình khác nhau (Ensemble). Sự đa dạng của các mô hình giúp bao quát được nhiều khía cạnh khác nhau trong hành vi của người dùng.
> **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Chương 12.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Hội đồng ban giám khảo chấm điểm một cuộc thi Khoa học Kỹ thuật.
> **Ứng dụng**: 
> - Thay vì chỉ dựa vào ý kiến của 1 giám khảo (có thể thiên kiến), cuộc thi sử dụng 5 giám khảo (Ensemble).
> - **Cơ chế**: Lấy điểm trung bình của 5 người sẽ cho kết quả công bằng và chính xác hơn về năng lực thực sự của học sinh, loại bỏ được các nhận định cực đoan từ cá nhân.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Trang 310-325.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Ensemble_Methods.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, dùng ví dụ Hội đồng ban giám khảo để giải thích Ensemble."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."
