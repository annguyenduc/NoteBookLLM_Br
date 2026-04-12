---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_12
  title: 📚 Bài mới: **Review: For Loops in Bash Scripts**
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, mình đã nhận diện được đây là bài học mới về **Vòng lặp For trong Bash**. Mình sẽ thực hiện việc chưng cất tri thức và hướng dẫn thực hành theo đúng quy tắc đã thống nhất.

---

# 📚 Bài mới: **Review: For Loops in Bash Scripts**

---

# 🎯 Mục đích bài học:
- Hiểu cách sử dụng vòng lặp `for` để duyệt qua một danh sách các phần tử (chuỗi, tệp tin).
- Biết cách kết hợp vòng lặp với các lệnh hệ thống như `basename` và `mv` để xử lý tệp tin hàng loạt.
- Ứng dụng thực tế: Đổi tên hàng loạt tệp tin có phần mở rộng cũ sang phần mở rộng mới.

---

# 💎 Trích xuất tri thức (LOM v4.1):

- **Fact:** Vòng lặp `for` trong Bash cho phép thực hiện một tập hợp các lệnh cho mỗi phần tử trong một danh sách xác định.
- **Source:** (v10 - Section: Review: For Loops in Bash Scripts)
- **Tag:** [vv10]

- **Fact:** Cú pháp cơ bản của vòng lặp for là `for var in list; do commands; done`.
- **Source:** (v10 - Section: Review: For Loops in Bash Scripts)
- **Tag:** [vv10]

- **Fact:** Lệnh `basename` được sử dụng để lấy tên tệp tin và loại bỏ phần mở rộng (suffix) của nó. Ví dụ: `basename "file.HTM" .HTM` sẽ trả về "file".
- **Source:** (v10 - Section: Review: For Loops in Bash Scripts)
- **Tag:** [vv10]

- **Fact:** Có thể sử dụng ký tự đại diện (globs) như `*.HTM` trong vòng lặp `for` để tự động lấy danh sách tất cả các tệp tin khớp với mẫu đó trong thư mục hiện hành.
- **Source:** (v10 - Section: Review: For Loops in Bash Scripts)
- **Tag:** [vv10]

---

# 🛠 Hướng dẫn thực hành:

Để thực hành bài này, bạn cần tạo các tệp tin giả lập và script đổi tên.

### Bước 1: Tạo các tệp tin `.HTM` giả lập
Chạy lệnh này trong terminal để tạo nhanh các file mẫu:
```bash
touch old_file1.HTM old_file2.HTM test_page.HTM
```

### Bước 2: Tạo script `rename.sh`
Sử dụng `nano` hoặc trình soạn thảo:
```bash
nano rename.sh
```

**Nội dung script:**
```bash
#!/bin/bash

# Duyệt qua tất cả các file có đuôi .HTM
for file in *.HTM; do
    # Lấy tên gốc của file (loại bỏ .HTM)
    name=$(basename "$file" .HTM)
    # Đổi tên file từ .HTM sang .html
    echo "Renaming $file to $name.html"
    mv "$file" "$name.html"
done
```

### Bước 3: Cấp quyền và chạy script
```bash
chmod +x rename.sh
./rename.sh
```

**Kết quả mong đợi:**
Các file `old_file1.HTM`, `old_file2.HTM`... sẽ biến mất và thay thế bằng `old_file1.html`, `old_file2.html`...

---

# 🏆 Tóm tắt kỹ thuật:

| Lệnh | Chức năng |
|:---|:---|
| `for var in ...` | Khởi tạo vòng lặp duyệt danh sách |
| `basename "$file" .ext` | Trích xuất tên file, cắt bỏ phần đuôi `.ext` |
| `mv source destination` | Di chuyển hoặc đổi tên file |
| `$(command)` | Command Substitution (thực thi lệnh và lấy kết quả gán vào biến) |

---

# 🚀 Gợi ý mở rộng:
- Bạn có muốn mình giao bài tập về việc **đổi tên file hàng loạt kèm theo đánh số thứ tự** không?
- Hoặc hướng dẫn cách **sao lưu (backup) file** trước khi đổi tên để đảm bảo an toàn?

👉 Nếu muốn, hãy nhắn: "**Giao bài tập for loop nâng cao**" hoặc "**Hướng dẫn script backup file**"! 🚀✨