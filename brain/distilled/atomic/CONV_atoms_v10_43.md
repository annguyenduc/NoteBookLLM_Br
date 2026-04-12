Chào bạn! Chúng ta lại tiếp tục với phần **Study guide: Basic Linux commands**. Đây là những "viên gạch" đầu tiên và quan trọng nhất để bạn làm chủ hệ thống Linux.

Dưới đây là tóm tắt mục đích bài học và hướng dẫn bạn tạo môi trường thực hành (vì bài đọc đưa ra rất nhiều ví dụ về file mà không chỉ cách tạo).

---

### 🎯 1. Mục đích của bài học: Basic Linux commands
Bài học này giúp bạn thành thạo 2 nhóm kỹ năng cốt lõi:
1.  **Quản lý tệp và thư mục (Managing files and directories):** Biết cách di chuyển (`mv`), sao chép (`cp`) và phân quyền (`chmod`) — những việc cực kỳ quan trọng khi cấu hình ứng dụng hoặc triển khai code.
2.  **Thao tác với nội dung tệp (Operating with content):** Sử dụng các công cụ dòng lệnh mạnh mẽ như `cut` (trích xuất dữ liệu) và `sort` (sắp xếp) để xử lý dữ liệu nhanh mà không cần mở trình soạn thảo văn bản.
3.  **Kết hợp lệnh (Pipelines):** Học cách xâu chuỗi các lệnh đơn giản để giải quyết các bài toán phức tạp (ví dụ: tìm 10 file lớn nhất).

---

### 🛠 2. Hướng dẫn tạo file thực hành
Trong bài có nhắc đến rất nhiều file như `addressbook.csv`, `phones.txt`, `names.txt`,... Để chạy được các lệnh ví dụ, bạn hãy copy và dán đoạn script sau vào Terminal. Nó sẽ tự động tạo toàn bộ thư mục và file mẫu cho bạn:

```bash
# 1. Tạo thư mục và các file cơ bản
mkdir -p dir1
touch myfile.txt file1.txt file2.txt file3.txt file.html

# 2. Tạo file addressbook.csv (Dữ liệu mẫu cho lệnh cut)
echo "John,Doe,New York
Jane,Smith,Los Angeles
Mike,Brown,Chicago" > addressbook.csv

# 3. Tạo file phones.txt (Dữ liệu mẫu cho lệnh cut -c)
echo "012-345-6789
987-654-3210
111-222-3333" > phones.txt

# 4. Tạo file names.txt (Dữ liệu mẫu cho lệnh sort)
echo "Zebra
Apple
Mango
Banana" > names.txt

# 5. Tạo file numbers.txt (Dữ liệu mẫu cho lệnh sort -n)
echo "10
2
100
25" > numbers.txt
```

---

### 💡 3. Giải thích các lệnh quan trọng trong bài

| Lệnh | Điểm cần lưu ý |
| :--- | :--- |
| `mv` | Vừa dùng để **di chuyển**, vừa dùng để **đổi tên**. Linux phân biệt chữ hoa/thường. |
| `cp` | Sao chép file. Nếu copy nhiều file vào 1 chỗ, đối tượng cuối cùng phải là thư mục. |
| `chmod +r` | Cấp quyền "đọc" (read) cho file. Rất quan trọng trước khi đưa file lên web server. |
| `cut -f1 -d","` | `-d` là dấu phân cách (delimiter), `-f1` là lấy cột (field) thứ nhất. |
| `sort -n` | Sắp xếp theo **giá trị số** (1, 2, 10) thay vì sắp xếp theo chữ cái (1, 10, 2). |

---

### 📋 TRÍCH XUẤT SỰ KIỆN (LOM v4.1)

- **Fact:** [CONV] Lệnh `mv` được sử dụng để di chuyển một hoặc nhiều tệp vào thư mục khác, hoặc dùng để đổi tên tệp.
- **Source:** [vv10 - Section: Managing files and directories]
- **Tag:** [vv10]

- **Fact:** [CONV] Linux có phân biệt chữ hoa và chữ thường (case-sensitive), do đó `mv` có thể dùng để đổi kiểu chữ của tên tệp.
- **Source:** [vv10 - Section: Managing files and directories]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `cut` dùng để trích xuất các trường (fields) từ tệp dữ liệu; ví dụ `-f1 -d","` trích xuất trường đầu tiên từ file CSV.
- **Source:** [vv10 - Section: Operating with the content of files]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `sort -n` dùng để sắp xếp nội dung tệp theo giá trị số thay vì thứ tự bảng chữ cái.
- **Source:** [vv10 - Section: Operating with the content of files]
- **Tag:** [vv10]

- **Fact:** [CONV] Có thể kết hợp nhiều lệnh như `ls -l | cut -w -f5,9 | sort -rn | head -10` để tìm 10 tệp có dung lượng lớn nhất trong thư mục hiện hành.
- **Source:** [vv10 - Section: Operating with the content of files]
- **Tag:** [vv10]

---

**Bạn đã sẵn sàng thử chạy các lệnh `cut` và `sort` trên các file vừa tạo chưa? Nếu có chỗ nào kết quả không như ý, hãy nhắn mình nhé!** 🚀