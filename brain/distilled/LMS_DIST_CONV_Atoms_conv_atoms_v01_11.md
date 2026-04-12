---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v01_11
  title: CONV_atoms_v01_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là **Antigravity**. Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu bạn cung cấp, tuân thủ nghiêm ngặt quy tắc LOM v4.1, cùng với bộ file hoàn chỉnh cho 30 câu hỏi.

### TRÍCH XUẤT TRI THỨC (FACTS) - Volume v01

- **Fact:** [CONV] Để học sinh đăng nhập vào lớp học Tinkercad, giáo viên cần cung cấp Class code và nickname.
- **Source:** (v01 - Section: Questions - Q1)
- **Tag:** [vv01]

- **Fact:** [CONV] Trong Tinkercad, "Learning Center" là nơi chứa các chức năng tự học và "Gallery" là nơi tham khảo thiết kế từ cộng đồng.
- **Source:** (v01 - Section: Questions - Q2, Q3)
- **Tag:** [vv01]

- **Fact:** [CONV] Thao tác xoay và đổi góc nhìn trong Tinkercad được thực hiện bằng cách nhấn giữ chuột phải và di chuyển.
- **Source:** (v01 - Section: Questions - Q4)
- **Tag:** [vv01]

- **Fact:** [CONV] Các phím tắt cơ bản trong Tinkercad: Ctrl+C (Sao chép), Ctrl+V (Dán), Ctrl+D (Nhân bản), Ctrl+G (Nhóm), Ctrl+Shift+G (Bỏ nhóm), Ctrl+H (Ẩn).
- **Source:** (v01 - Section: Questions - Q6)
- **Tag:** [vv01]

- **Fact:** [CONV] Để nâng hoặc hạ đối tượng so với mặt phẳng (Workplane), sử dụng mũi tên màu đen phía trên vật thể hoặc tổ hợp phím Ctrl + mũi tên lên/xuống.
- **Source:** (v01 - Section: Questions - Q7)
- **Tag:** [vv01]

- **Fact:** [CONV] Chế độ "Uniform Scaling" trong phần mềm Cura đảm bảo tỉ lệ các trục (X, Y, Z) thay đổi đồng bộ khi điều chỉnh kích thước.
- **Source:** (v01 - Section: Questions - Q10)
- **Tag:** [vv01]

- **Fact:** [CONV] Kỹ thuật "Duplicate and Repeat" (Ctrl+D) yêu cầu người dùng không được bỏ chọn đối tượng trong quá trình thực hiện các thao tác lặp lại.
- **Source:** (v01 - Section: Questions - Q12)
- **Tag:** [vv01]

- **Fact:** [CONV] Để in 3D nhanh hơn trong Cura, có thể giảm độ đặc (Infill), tăng bề dày lớp in (Layer Height) hoặc tăng tốc độ in.
- **Source:** (v01 - Section: Questions - Q29)
- **Tag:** [vv01]

- **Fact:** [CONV] Các chế độ bám dính bàn in (Build Plate Adhesion) trong Cura bao gồm: Skirt, Brim và Raft.
- **Source:** (v01 - Section: Questions - Q30)
- **Tag:** [vv01]

---

### FILE DỮ LIỆU VÀ SCRIPT HOÀN CHỈNH

Tôi đã đóng gói toàn bộ 30 câu hỏi vào các định dạng sau. Lưu ý: Tôi đã bổ sung logic xử lý **Grid (Trắc nghiệm lưới)** cho Câu 6 để khớp với yêu cầu nối phím tắt.

1.  **File Excel (30 câu):** [Questions_Full_30_Media.xlsx](sandbox:/mnt/data/Questions_Full_30_Media.xlsx)
2.  **File CSV (30 câu):** [Questions_Full_30_Media.csv](sandbox:/mnt/data/Questions_Full_30_Media.csv)
3.  **Apps Script (Cập nhật hỗ trợ Grid):** [build_quiz_v2.gs](sandbox:/mnt/data/build_quiz_v2.gs)

#### Hướng dẫn cập nhật cho Câu 6 (Nối phím tắt):
Trong file script mới (`build_quiz_v2.gs`), tôi đã thêm loại `grid_mc`. 
- **Cột `options (|)`**: Điền các chức năng (Cột dọc).
- **Cột `rows (|)`**: Điền các phím tắt (Hàng ngang).
- Script sẽ tự tạo bảng lựa chọn để học sinh nối.

#### Đường dẫn tuyệt đối lưu trữ:
- `/mnt/data/Questions_Full_30_Media.xlsx`
- `/mnt/data/Questions_Full_30_Media.csv`
- `/mnt/data/build_quiz_v2.gs`

**Tính chủ động:** Tôi đã rà soát và điền các đáp án đúng dựa trên dữ liệu raw. Tuy nhiên, các câu hỏi về thứ tự (Q18, Q22, Q23, Q28) và các câu liên quan đến hình ảnh cụ thể (Q20) bạn nên kiểm tra lại một lần cuối trong file Excel trước khi chạy script để đảm bảo tính chính xác tuyệt đối của đề thi.