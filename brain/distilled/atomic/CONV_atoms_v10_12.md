Chào bạn, mình đã nhận được nội dung bài mới về **For Loops in Bash Scripts**. Đúng theo quy trình, mình sẽ tóm tắt kiến thức và trích xuất các sự kiện kỹ thuật (Facts) theo chuẩn @scout (LOM v4.1).

---

# 📚 Bài mới: **Review: For Loops in Bash Scripts**

### 🎯 Mục đích bài học:
- Hiểu cách sử dụng vòng lặp `for` để duyệt qua một danh sách các phần tử.
- Ứng dụng vòng lặp `for` kết hợp với **Globs** để xử lý tệp tin hàng loạt.
- Sử dụng lệnh `basename` để xử lý chuỗi tên tệp (cắt bỏ phần mở rộng).

---

### 📋 Trích xuất kiến thức (Facts) - [LOM v4.1]:

- **Fact:** [CONV] Vòng lặp `for` trong Bash cho phép thực hiện một tập hợp các lệnh cho mỗi phần tử trong một danh sách (chuỗi văn bản, danh sách tệp, v.v.).
- **Source:** (v10 - Section: Review: For Loops in Bash Scripts - Example 1)
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `basename` được sử dụng để lấy tên tệp từ một đường dẫn và có thể loại bỏ phần đuôi mở rộng (suffix) nếu được chỉ định. Ví dụ: `basename "file.HTM" .HTM` sẽ trả về `file`.
- **Source:** (v10 - Section: Review: For Loops in Bash Scripts - Example 2)
- **Tag:** [vv10]

- **Fact:** [CONV] Việc kết hợp vòng lặp `for` với các ký tự đại diện (Globs như `*.HTM`) là phương pháp hiệu quả để tự động hóa các tác vụ quản lý tệp tin hàng loạt như đổi tên (`mv`).
- **Source:** (v10 - Section: Review: For Loops in Bash Scripts - Example 2)
- **Tag:** [vv10]

---

### 🛠 Hướng dẫn thực hành (Tạo file script):

Để thực hành bài này, bạn nên tạo các file sau để thấy rõ sức mạnh của `for`:

#### 1. Tạo script đổi tên file (`rename.sh`):
```bash
#!/bin/bash

# Tạo một vài file .HTM giả lập để test
touch file1.HTM file2.HTM sample.HTM

echo "Đang đổi tên các file .HTM thành .html..."

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    echo "Đang xử lý: $file -> $name.html"
    mv "$file" "$name.html"
done

echo "Hoàn tất!"
ls *.html
```

#### 2. Cấp quyền và chạy:
```bash
chmod +x rename.sh
./rename.sh
```

---

### 🏆 Tóm tắt nhanh:

| Lệnh/Cú pháp | Chức năng |
|:---|:---|
| `for var in list; do ... done` | Cấu trúc vòng lặp qua danh sách |
| `basename "$file" .ext` | Cắt bỏ phần mở rộng `.ext` khỏi tên file |
| `mv old_name new_name` | Đổi tên hoặc di chuyển file |

---

### 🚀 Gợi ý cho bạn:
Bạn đã nắm được cách lặp qua danh sách cố định và danh sách file. 
- Bạn có muốn mình giao **bài tập thực hành dùng `for` để sao lưu (backup) các file quan trọng** không?
- Hoặc mình hướng dẫn cách dùng **vòng lặp `for` với dãy số (sequence)** như `{1..10}`?

👉 Nếu muốn, hãy nhắn: "**Giao bài tập for loop backup**" hoặc "**Hướng dẫn for loop với sequence**"! 🚀✨