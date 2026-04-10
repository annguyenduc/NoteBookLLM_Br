# 📚 STEAM Examples Bank (PRO Blueprint)

> **Goal:** Cung cấp các ví dụ mẫu (Few-shot samples) và khuôn mẫu (Blueprints) chất lượng cao. Các ví dụ này được chiết xuất từ các sản phẩm "Gold Standard" để đảm bảo AI mô phỏng đúng cấu trúc sư phạm chuyên sâu.

## 📐 1. Core Blueprints (Layer 4 Standards) — [ACTIVE]
Các khuôn mẫu này đã được triển khai và sẵn sàng để tham chiếu:
- **[ToT Module Blueprint](./examples/pattern-tot-module.md):** Cấu trúc giáo án đào tạo GV tổng quan (Bloom, Knowledge Map, Schedule).
- **[Assessment Blueprint](./examples/pattern-assessment.md):** Cấu trúc bộ đánh giá (MCQ, Practice, Scenario).
- **[Analogy Logic](./examples/pattern-analogy-logic.md):** Cách giải thích thuật ngữ kỹ thuật bằng ngôn ngữ K-12 "bình dân học vụ".

## 🎞️ 2. Example: Invisible Standards in Action
- **Trạng thái cũ:** Ghi nhãn "SAMR: Redefinition" vào slide.
- **Trạng thái mới (PRO):** Thiết kế hoạt động buộc HS phải dùng máy tính để làm điều "trước đây không thể làm được" (VD: Phỏng vấn chuyên gia qua Zoom) mà không cần ghi nhãn. Tinh thần SAMR nằm ở **Bản chất hoạt động**.

## 📊 3. Example: Error Analysis Loop (Process)
Khi thiết kế module kỹ thuật/AI, luôn áp dụng Loop:
1. **Thử nghiệm:** Chạy code/model.
2. **Phát hiện lỗi:** "Tại sao kết quả không như ý?"
3. **Cải tiến:** Sửa đổi tham số/dữ liệu.
4. **Đối chiếu:** Kiểm tra lại Accuracy.

## 🚨 Quality Gate (Red Flags)
- ❌ Ví dụ không có Annotation giải thích "Tại sao nó tốt?".
- ❌ Cấu trúc lỏng lẻo, không tuân thủ Bloom's Taxonomy.
- ❌ Thiếu các rào cản (Constraints) sư phạm để kích thích tư duy.
- ⚠️ Hậu kiểm: Luôn đối chiếu với `k12-shared-references` để dùng đúng thuật ngữ chuẩn.

## 💡 Example Triggers
- "cho tôi ví dụ bài học 5E về vật lý"
- "mẫu rubric cho dự án thiết kế xe đua"
- "áp dụng cấu trúc ToT module cho bài Thunkable"
- "giải thích khái niệm API bằng ẩn dụ"

