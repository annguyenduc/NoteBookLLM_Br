---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v04_4
  title: atoms_v04_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, mình đã biên soạn lại file **Word (DOCX)** với đầy đủ mô tả chi tiết cho từng tiêu chí chấm điểm (Rubric). 

File này được thiết kế để Ban giám khảo có thể cầm trên tay, đối chiếu các mức độ hoàn thiện (Xuất sắc, Khá, Đạt, Chưa đạt) để cho điểm chính xác nhất.

### 📥 Tải file tại đây:
- **File Word (Chi tiết tiêu chí):** [Rubric_IoT_Chi_Tiet_Tieu_Chi.docx](sandbox:/mnt/data/Rubric_IoT_Chi_Tiet_Tieu_Chi.docx)
- **File Excel (Để nhập điểm tự động):** [Rubric_IoT_THTP.xlsx](sandbox:/mnt/data/Rubric_IoT_THTP.xlsx)

---

### 📝 Tóm tắt nội dung tiêu chí trong file Word:

#### **PHẦN 1: SƠ ĐỒ KHỐI (20 ĐIỂM)**
1.  **Phần cứng (6đ):** Đầy đủ khối Nguồn, Điều khiển, ≥3 Cảm biến, ≥2 Chấp hành.
2.  **Luồng dữ liệu (6đ):** Mũi tên có hướng, có nhãn (đọc/điều khiển), ghi rõ chu kỳ hoặc loại tín hiệu.
3.  **Logic vận hành (4đ):** Có ngưỡng định lượng (ví dụ: >30°C), có lọc nhiễu (hysteresis) và thứ tự ưu tiên khi xung đột.
4.  **An toàn & Fail-safe (3đ):** Có cơ chế tự ngắt (timeout), trạng thái an toàn khi mất điện, và báo lỗi cảm biến.
5.  **Giao diện UI (1đ):** Mô tả rõ thông tin hiển thị trên LCD/App.

#### **PHẦN 2: THIẾT KẾ & LẮP RÁP (25 ĐIỂM)**
1.  **Bố trí phần cứng (8đ):** Vị trí lắp đặt hợp lý, có cao độ, khoảng cách an toàn, không cản trở thao tác.
2.  **Làm được & Lắp ráp (9đ):**
    *   *Cố định (3đ):* Dùng ốc M3, khe trượt hoặc khớp nối (không chỉ dùng keo tạm bợ).
    *   *Đi dây & Nguồn (3đ):* Tuyến dây gọn gàng, có đầu nối (connector), tách nguồn tải nặng qua Relay.
    *   *Quy trình (3đ):* Có 4-6 bước lắp ráp rõ ràng và checklist kiểm tra sau khi lắp.
3.  **Thẩm mỹ & Nhận diện (8đ):** Có poster dự án, màu sắc đồng bộ, nhãn dán icon rõ ràng cho các nút bấm/cảm biến.

---
**Thông tin trích xuất tri thức kỹ thuật (@scout):**
- **Fact:** Tiêu chí chấm lắp ráp (9đ) tập trung vào 3 yếu tố: Cách cố định vật lý, Kế hoạch đi dây/nguồn và Quy trình bảo trì.
- **Source:** [vv04] - Section: ASSISTANT response regarding "Barem dùng cho phần Thiết kế".
- **Tag:** [vv04]

- **Fact:** Sơ đồ khối IoT đạt điểm tối đa khi thể hiện được tính an toàn (Fail-safe) và logic xử lý xung đột thiết bị.
- **Source:** [vv04] - Section: ASSISTANT response regarding "Sơ đồ khối IoT (20đ)".
- **Tag:** [vv04]