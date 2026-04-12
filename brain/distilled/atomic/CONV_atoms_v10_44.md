Chào bạn, mình là @scout. Mình đã tiếp nhận dữ liệu từ **Volume v10** về chủ đề **Creating Bash Scripts**. 

Dưới đây là phần trích xuất tri thức theo quy tắc **LOM v4.1**, sau đó là phần tóm tắt và hướng dẫn thực hành theo yêu cầu của bạn.

---

### 📝 TRÍCH XUẤT SỰ KIỆN (FACTS) - [vv10]

- **Fact:** [CONV] Một script Bash tiêu chuẩn bắt đầu bằng dòng Shebang `#!/bin/bash` để chỉ định trình thông dịch.
- **Source:** [v10 - Section: Creating Bash Scripts - Line 1]
- **Tag:** [vv10]

- **Fact:** [CONV] Cú pháp `$(date)` được sử dụng để thực thi lệnh `date` và chèn kết quả (thời gian hệ thống) trực tiếp vào chuỗi văn bản.
- **Source:** [v10 - Section: Creating Bash Scripts - Line 2]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `uptime` cung cấp thông tin về thời gian hệ thống đã hoạt động liên tục, số lượng người dùng và tải trung bình (load average).
- **Source:** [v10 - Section: Creating Bash Scripts - Line 6]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `free` hiển thị trạng thái bộ nhớ vật lý (RAM) và bộ nhớ đệm (Swap) của hệ thống.
- **Source:** [v10 - Section: Creating Bash Scripts - Line 10]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `who` liệt kê các người dùng hiện đang đăng nhập vào hệ thống cùng với terminal và thời gian đăng nhập của họ.
- **Source:** [v10 - Section: Creating Bash Scripts - Line 11 (Code block 2)]
- **Tag:** [vv10]

- **Fact:** [CONV] Dấu chấm phẩy `;` được sử dụng như một ký tự phân cách để thực hiện nhiều lệnh liên tiếp trên cùng một dòng code.
- **Source:** [v10 - Section: Creating Bash Scripts - Line 11 (Code block 2)]
- **Tag:** [vv10]

- **Fact:** [CONV] Để thực thi một script Bash, người dùng sử dụng cú pháp `./` kèm theo tên file (ví dụ: `./gather-information.sh`).
- **Source:** [v10 - Section: Creating Bash Scripts - Line 17]
- **Tag:** [vv10]

- **Fact:** [CONV] Trước khi chạy script bằng `./`, file đó bắt buộc phải được cấp quyền thực thi bằng lệnh `chmod +x [tên_file]`.
- **Source:** [Quy trình vận hành Linux tiêu chuẩn]
- **Tag:** [Unverified_Source]

---

# 📚 Tóm tắt bài học: **Creating Bash Scripts**

# 🎯 Mục đích bài này là gì?
- Hướng dẫn bạn cách **tự tạo một file script** để tự động hóa việc chạy nhiều lệnh cùng lúc.
- Giúp bạn gom nhóm các lệnh kiểm tra hệ thống (`date`, `uptime`, `free`, `who`) vào một công cụ duy nhất.
- Giới thiệu cách viết code ngắn gọn trên một dòng bằng dấu `;`.

---

# 📋 Các lệnh quan trọng trong bài:

| Lệnh | Ý nghĩa |
|:--|:--|
| `#!/bin/bash` | Dòng bắt đầu bắt buộc của script Bash (Shebang). |
| `date` | Hiển thị ngày giờ hệ thống. |
| `uptime` | Xem máy đã chạy bao lâu. |
| `free` | Kiểm tra RAM. |
| `who` | Xem ai đang đăng nhập. |
| `;` | Dùng để viết nhiều lệnh trên 1 dòng. |

---

# 🛠 Hướng dẫn tạo file thực hành:

Để thực hành đúng như video, bạn cần tạo file `gather-information.sh`.

### Bước 1: Tạo file
```bash
nano gather-information.sh
```

### Bước 2: Dán nội dung code sau vào (Phiên bản đầy đủ):
```bash
#!/bin/bash

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"
```

### Bước 3: Cấp quyền thực thi (Rất quan trọng)
Linux sẽ không cho phép bạn chạy file nếu chưa cấp quyền:
```bash
chmod +x gather-information.sh
```

### Bước 4: Chạy script
```bash
./gather-information.sh
```

---

# 🚀 Giải thích thêm về dấu `;` và `$(...)`

1.  **Dấu `;` (Semicolon):**
    - Bình thường bạn viết:
      ```bash
      echo "Hello"
      ls
      ```
    - Dùng `;` bạn có thể viết: `echo "Hello"; ls`. Nó giúp script trông gọn hơn nếu các lệnh ngắn.

2.  **Cú pháp `$(command)`:**
    - Đây gọi là **Command Substitution**. Nó thực hiện lệnh bên trong ngoặc trước, sau đó lấy kết quả đó đặt vào vị trí của nó.
    - Ví dụ: `echo "Hôm nay là $(date)"` sẽ in ra "Hôm nay là Thứ Hai..."

---

# 🏆 Bài tập nhỏ cho bạn:

Bạn hãy thử tạo một script tên là `system_check.sh` thực hiện các việc sau:
1. In ra dòng: "Kiểm tra thư mục hiện tại:"
2. Chạy lệnh `ls -l`
3. In ra dòng: "Tên máy tính của tôi là: [kết quả lệnh hostname]" (Gợi ý: dùng `$(hostname)`)

👉 Nếu bạn làm xong hoặc cần mình sửa code, hãy gửi cho mình nhé! 🚀✨