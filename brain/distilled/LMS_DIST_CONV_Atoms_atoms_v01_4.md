---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v01_4
  title: atoms_v01_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Tiếp theo, bạn cần **tách thông tin** từ biến `line` (đang có dạng `TM:nhãn:tỉ_lệ`) và **gửi lên IoT**. 

Dưới đây là các bước chi tiết để bạn kéo khối tiếp theo (đặt ngay dưới khối `đặt buf = ...` cuối cùng trong vòng lặp **Lặp lại khi** của bạn):

### 1. Kiểm tra dòng có đúng định dạng không
Dùng khối **Nếu** để đảm bảo dòng bắt đầu bằng "TM:":
- **Nếu:** `trong văn bản [line] tìm sự có mặt đầu tiên của ["TM:"]` **= 1**

### 2. Tách Label và Score (Dùng logic "cắt đuôi")
Vì khối của bạn không có "tìm từ vị trí...", chúng ta sẽ làm như sau:
1. **Tìm dấu ":" thứ nhất (p1):**
   - `đặt p1 = trong văn bản [line] tìm sự có mặt đầu tiên của [":"]`
2. **Lấy phần còn lại sau dấu ":" thứ nhất (tail):**
   - `đặt tail = trong văn bản [line] lấy từ ký tự thứ (p1 + 1) đến ký tự thứ (độ dài của line)`
3. **Tìm dấu ":" thứ hai trong phần đuôi (p2_tail):**
   - `đặt p2_tail = trong văn bản [tail] tìm sự có mặt đầu tiên của [":"]`
4. **Tính vị trí dấu ":" thứ hai trên dòng gốc (p2):**
   - `đặt p2 = p1 + p2_tail`

### 3. Cắt lấy giá trị cụ thể
- **Lấy Label:**
  - `đặt label = trong văn bản [line] lấy từ ký tự thứ (p1 + 1) đến ký tự thứ (p2 - 1)`
- **Lấy Score:**
  - `đặt score_str = trong văn bản [line] lấy từ ký tự thứ (p2 + 1) đến ký tự thứ (độ dài của line)`
  - `đặt score_str = cắt các khoảng trắng [Ở hai phía] của [score_str]`
  - `đặt score = đổi [score_str] sang số` (Khối này thường nằm trong mục **Toán tử** hoặc **Văn bản**).

### 4. Gửi lên IoT (V1 và V2)
Để tránh gửi quá nhiều (làm lag thiết bị), bạn nên thêm điều kiện: **Chỉ gửi khi kết quả thay đổi**.

- **Nếu:** `(label ≠ last_label)` **hoặc** `(giá trị tuyệt đối của (score - last_score) > 0.05)`
    - **Gửi dữ liệu lên IoT:** Kênh **V1**, giá trị **label**
    - **Gửi dữ liệu lên IoT:** Kênh **V2**, giá trị **score**
    - `đặt last_label = label`
    - `đặt last_score = score`

---

### Tóm tắt các sự kiện kỹ thuật (Scout Report):
- **Fact:** Dữ liệu Serial từ Web App có cấu trúc định danh `TM:<label>:<score>\n`.
- **Source:** (v01 - HTML Script: predictLoop).
- **Tag:** [vv01]

- **Fact:** Việc tách chuỗi trong Blockly OhStem khi không có tham số "vị trí bắt đầu" yêu cầu kỹ thuật lấy chuỗi con (substring) sau dấu phân cách thứ nhất để tìm dấu phân cách kế tiếp.
- **Source:** (v01 - Logic xử lý chuỗi).
- **Tag:** [Unverified_Source]

- **Fact:** Widget hiển thị văn bản trên Dashboard IoT (như V1 cho Label) cần được cấu hình "Cách hiển thị: Chuỗi/Văn bản" để không bị mặc định về giá trị 0.
- **Source:** (v01 - IoT Dashboard Setup).
- **Tag:** [vv01]

**Lời khuyên:** Sau khi kéo xong, bạn hãy bấm **Gửi thử "TM:TEST:0.99"** trên trang web. Nếu trên Dashboard hiện đúng chữ **TEST** ở V1 và số **0.99** ở V2 là bạn đã thành công!