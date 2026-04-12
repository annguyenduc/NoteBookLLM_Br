# 📊 SOP: Quy trình Kiểm định Độ khó & Tải nhận thức (CLT)

> **Mục tiêu**: Đảm bảo mọi tri thức được truyền đạt cho học sinh đều nằm trong "Vùng phát triển gần" (ZPD), không gây quá tải nhận thức (Cognitive Overload) nhưng vẫn đủ thử thách.
> **Dẫn chứng**: Sweller (1998), Brunsell (2011), Paas (1992).

---

## 1. Ma trận Đánh giá 5 Tiêu chí (Cognitive Load Matrix)

Mỗi tiêu chí được chấm từ 1 (Dễ) đến 5 (Khó). Tổng điểm tối đa là 25.

| Tiêu chí | Mô tả |
| :--- | :--- |
| **1. Sự trừu tượng (Abstraction)** | HS có thể quan sát/chạm vào được (1) hay hoàn toàn là lý thuyết trừu tượng (5)? |
| **2. Rào cản Kỹ thuật (Technical)** | Không cần kiến thức nền (1) hay cần hiểu sâu về Logic/Coding/Math (5)? |
| **3. Tải Thuật ngữ (Terminology)** | Dùng ngôn ngữ phổ thông (1) hay dùng nhiều thuật ngữ chuyên môn mới (5)? |
| **4. Tư duy bậc cao (Meta-cognition)** | Làm theo mẫu (1) hay phải tự thiết kế, phản tư, đánh giá hệ thống (5)? |
| **5. Rủi ro Ảo giác (AI-Specific)** | Câu trả lời của AI luôn đúng (1) hay dễ bị sai/ảo giác cần HS kiểm chứng (5)? |

---

## 2. Ngưỡng phân loại & Hành động theo Khối lớp

| Khối lớp | Thang điểm "An toàn" | Thang điểm "Thử thách" | Chiến lược Sư phạm bắt buộc |
| :--- | :--- | :--- | :--- |
| **Khối 10** | 8 - 12đ | **> 13đ** | Sử dụng Ẩn dụ (Analogies) mạnh + Bổ sung Bài tập mẫu gợi ý (Faded Examples). |
| **Khối 11** | 10 - 15đ | **> 16đ** | Sử dụng Phương pháp Socratic kết hợp thực hành lặp (Iterative Practice). |
| **Khối 12** | 12 - 18đ | **> 19đ** | Tập trung vào Tư duy Kiến trúc & Đánh giá mạng lưới (Evaluation level). |

---

## 3. Quy trình thực thi (Swarm Workflow)

1. **Bước 1 (@scout)**: Sau khi nạp tri thức mới, thực hiện chấm điểm theo Ma trận trên. Lập báo cáo `DIFFICULTY_REPORT.md`.
2. **Bước 2 (@pm)**: Kiểm tra tổng điểm so với khối lớp mục tiêu.
    - Nếu vượt ngưỡng: Thêm phần **"Ẩn dụ sư phạm"** và **"Scaffolding"** vào giáo án.
    - Nếu vượt ngưỡng quá xa (> 22đ): Đề xuất chia nhỏ module thành nhiều buổi học lẻ.
3. **Bước 3 (@librarian)**: Review lại giáo án xem các hỗ trợ sư phạm đã đủ để hạ thấp "Tải ngoại lai" (Extraneous load) chưa.

---

## 🔗 Tài liệu tham khảo
- Bybee, R. W. (2006) - 5E Model.
- NASA JPL - Engineering Design Process.
- Sweller, J. (1998) - Cognitive Load Theory.
