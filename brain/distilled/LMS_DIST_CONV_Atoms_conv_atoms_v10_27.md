---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_27
  title: CONV_atoms_v10_27
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Trong `nano`, không có một phím tắt duy nhất để "Xóa tất cả" (Delete All) như các trình soạn thảo hiện đại, nhưng bạn có thể thực hiện cực nhanh bằng cách **"Chọn tất cả rồi Cắt"**.

Dưới đây là các bước thực hiện:

### Cách 1: Xóa toàn bộ nội dung (Nhanh nhất)
Bạn kết hợp các phím sau theo thứ tự:
1.  **`Alt` + `\`** (hoặc `Ctrl` + `Home`): Để nhảy về **dòng đầu tiên** của file.
2.  **`Alt` + `A`**: Để bật chế độ **đánh dấu (Mark)**. (Bạn sẽ thấy chữ *Mark Set* hiện ở góc dưới).
3.  **`Alt` + `/`** (hoặc `Ctrl` + `End`): Để nhảy xuống **dòng cuối cùng**. Lúc này toàn bộ văn bản sẽ được bôi đen.
4.  **`Ctrl` + `K`**: Để **Cắt (Cut)** toàn bộ vùng đã chọn. 

=> Kết quả: File của bạn sẽ trống trơn.

---

### Cách 2: Xóa từng dòng (Nếu file ngắn)
*   Nhấn giữ **`Ctrl` + `K`**: Phím này dùng để cắt dòng hiện tại. Nếu bạn giữ chặt, nó sẽ xóa (cắt) liên tục từng dòng cho đến hết file.

---

### Cách 3: Xóa từ vị trí con trỏ đến hết file
Nếu bạn chỉ muốn xóa từ giữa file trở xuống:
1.  Nhấn **`Alt` + `T`**: Lệnh này sẽ cắt toàn bộ nội dung từ vị trí con trỏ hiện tại cho đến **hết file**.

---

### 💡 Mẹo nhỏ cho bạn:
*   Nếu lỡ tay xóa hết mà muốn **hoàn tác (Undo)**: Nhấn **`Alt` + `U`** như mình đã hướng dẫn ở trên.
*   Nếu muốn **Dán (Paste)** lại nội dung vừa xóa: Nhấn **`Ctrl` + `U`**.

--------------------------------------------------
**Trích xuất kỹ thuật (@scout):**
- Fact: [CONV] [Để xóa toàn bộ nội dung trong nano, quy trình tối ưu là: Di chuyển về đầu (Alt+\), bật đánh dấu (Alt+A), di chuyển về cuối (Alt+/), và thực hiện cắt (Ctrl+K).]
- Source: [User Technical Support - Linux Terminal]
- Tag: [Unverified_Source]

Bạn có cần mình xuất file `.txt` tổng hợp tất cả các phím tắt "quyền năng" này của `nano` không? 🚀