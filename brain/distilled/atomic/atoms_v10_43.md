Chào bạn! Rất tuyệt vời, chúng ta lại tiếp tục với một phần cực kỳ nền tảng: **Basic Linux Commands**.

Dưới đây là tóm tắt mục đích bài học và hướng dẫn bạn tạo toàn bộ môi trường để thực hành các lệnh này một cách trơn tru nhất.

---

# 🎯 1. Mục đích của bài học: Basic Linux Commands

Bài học này nhằm trang bị cho bạn kỹ năng **thao tác trực tiếp với hệ thống tệp tin** mà không cần giao diện đồ họa (GUI). Cụ thể:
- **Quản lý cấu trúc hệ thống:** Di chuyển (`mv`), sao chép (`cp`), và phân quyền (`chmod`) cho các file cấu hình hoặc mã nguồn.
- **Xử lý dữ liệu nhanh (Data Processing):** Trích xuất thông tin cụ thể từ các file văn bản/CSV (`cut`) và sắp xếp chúng (`sort`) theo ý muốn.
- **Kết hợp sức mạnh (Chaining):** Sử dụng Pipe (`|`) để biến các lệnh đơn lẻ thành một quy trình phân tích dữ liệu phức tạp (ví dụ: tìm 10 file lớn nhất).

---

# 🛠 2. Hướng dẫn tạo file thực hành (Vì trong bài không có bước tạo)

Để chạy được các ví dụ trong bài, bạn hãy copy và dán đoạn lệnh shell này vào Terminal. Nó sẽ tự động tạo thư mục và các file mẫu (`addressbook.csv`, `phones.txt`, v.v.) cho bạn:

```bash
# 1. Tạo thư mục mẫu
mkdir -p dir1

# 2. Tạo các file trống để thực hành di chuyển/sao chép
touch myfile.txt file1.txt file2.txt file3.txt file.html

# 3. Tạo file addressbook.csv (Dữ liệu: Tên, Họ, Số điện thoại)
echo -e "John,Doe,555-1234\nJane,Smith,555-5678\nAlice,Wong,555-8765\nBob,Brown,555-4321" > addressbook.csv

# 4. Tạo file phones.txt (Định dạng: 123-456-7890)
echo -e "123-456-7890\n987-654-3210\n555-000-1111" > phones.txt

# 5. Tạo file names.txt (Danh sách tên lộn xộn)
echo -e "Zebra\nApple\nMonkey\nBanana\nCat" > names.txt

# 6. Tạo file numbers.txt (Danh sách số để sắp xếp)
echo -e "10\n2\n100\n25\n1" > numbers.txt

echo "--- Đã tạo xong tất cả file thực hành! ---"
```

---

# 📚 3. Giải thích các lệnh quan trọng trong bài

### A. Quản lý File & Thư mục
*   **`mv` (Move/Rename):** 
    *   `mv file1.txt file2.txt`: Đổi tên file1 thành file2.
    *   `mv file1.txt dir1/`: Chuyển file vào thư mục.
*   **`cp` (Copy):** Tạo bản sao. `cp file1.txt bản_sao.txt`.
*   **`chmod` (Change Mode):** Thay đổi quyền truy cập. 
    *   `chmod +r file.html`: Cho phép mọi người đọc file này.

### B. Thao tác với nội dung File
*   **`cut` (Cắt dữ liệu):**
    *   `-f1`: Lấy trường (field) số 1.
    *   `-d","`: Dùng dấu phẩy làm vật phân cách (delimiter).
    *   `-c1-3`: Lấy các ký tự (character) từ vị trí 1 đến 3.
*   **`sort` (Sắp xếp):**
    *   Mặc định: Sắp xếp theo bảng chữ cái (A-Z).
    *   `-r`: Sắp xếp ngược (Z-A).
    *   `-n`: Sắp xếp theo giá trị số (1, 2, 10 thay vì 1, 10, 2).

---

# 🏆 4. Phân tích Pipeline "thần thánh" cuối bài

Lệnh này rất hay, hãy cùng mổ xẻ nó:
```bash
ls -l | cut -w -f5,9 | sort -rn | head -10
```
1.  **`ls -l`**: Liệt kê danh sách file chi tiết (có kích thước file ở cột 5 và tên file ở cột 9).
2.  **`cut -w -f5,9`**: 
    *   `-w`: Coi các khoảng trắng là vật phân cách.
    *   `-f5,9`: Chỉ lấy cột 5 (kích thước) và cột 9 (tên file).
3.  **`sort -rn`**: 
    *   `-n`: Sắp xếp theo số.
    *   `-r`: Giảm dần (lớn nhất lên đầu).
4.  **`head -10`**: Chỉ lấy 10 dòng đầu tiên.

👉 **Kết quả:** Bạn tìm được **10 file có dung lượng lớn nhất** trong thư mục hiện tại!

---

# 🚀 Bạn đã sẵn sàng chưa?

Bây giờ bạn có thể thử gõ các lệnh trong Study Guide vào Terminal vì các file đã được tạo sẵn rồi đấy!

**Gợi ý bài tập nhỏ:**
Bạn hãy thử lệnh này và cho mình biết kết quả nhé:
`cut -f1 -d"," addressbook.csv | sort -r`

Nếu bạn muốn mình giải thích sâu hơn về **quyền hạn file (chmod)** hoặc các **tham số nâng cao của cut**, hãy nhắn mình ngay nhé! 🎯🚀