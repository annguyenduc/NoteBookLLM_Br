Trong `nano`, không có một phím tắt duy nhất để "Xóa tất cả" (Select All -> Delete) như trong Windows, nhưng bạn có thể làm cực nhanh theo các bước sau:

### Cách 1: Xóa toàn bộ nội dung (Nhanh nhất)
1. **Di chuyển về đầu file:** Nhấn **`Alt`** + **`\`** (hoặc `Esc` rồi nhấn `\`).
2. **Bật chế độ chọn văn bản (Mark):** Nhấn **`Alt`** + **`A`** (Bạn sẽ thấy chữ *Mark Set* hiện ra ở góc dưới).
3. **Di chuyển xuống cuối file:** Nhấn **`Alt`** + **`/`** (hoặc `Esc` rồi nhấn `/`). Lúc này toàn bộ văn bản sẽ được bôi đen.
4. **Xóa (Cắt):** Nhấn **`Ctrl`** + **`K`**. 

=> Toàn bộ nội dung đã biến mất!

---

### Cách 2: Xóa từng dòng (Nếu file ngắn)
- Nhấn giữ **`Ctrl`** + **`K`**. Mỗi lần nhấn nó sẽ "cắt" (xóa) một dòng. Nhấn giữ cho đến khi trắng trang.

---

### Cách 3: Thoát ra không lưu (Nếu bạn lỡ tay làm hỏng file)
Nếu bạn muốn xóa hết để làm lại từ đầu mà không muốn nhấn phím nhiều:
1. Nhấn **`Ctrl`** + **`X`**.
2. Khi máy hỏi *Save modified buffer?*, nhấn **`N`** (No).
3. Sau đó mở lại file bằng lệnh `nano` cũ, file sẽ quay về trạng thái lúc chưa sửa.

---

### 💡 Mẹo nhỏ từ Terminal (Không cần vào nano)
Nếu bạn đang ở ngoài Terminal và muốn làm trống hoàn toàn một file (xóa sạch nội dung bên trong), chỉ cần gõ:
```bash
> ten_file.txt
```
(Dấu `>` sẽ ghi đè nội dung rỗng vào file đó).

---

**Trích xuất thông tin kỹ thuật (Scout Mode):**
- Fact: Trong trình soạn thảo nano, để xóa toàn bộ văn bản, quy trình chuẩn là di chuyển về đầu file (`Alt+\`), đặt dấu chọn (`Alt+A`), di chuyển đến cuối file (`Alt+/`) và thực hiện lệnh cắt (`Ctrl+K`).
- Source: [Kiến thức kỹ thuật hệ thống Linux]
- Tag: [Unverified_Source]

Bạn có cần mình xuất file `.txt` tổng hợp tất cả các phím tắt `nano` và lệnh `shortcut` đã học từ nãy đến giờ không? 🚀