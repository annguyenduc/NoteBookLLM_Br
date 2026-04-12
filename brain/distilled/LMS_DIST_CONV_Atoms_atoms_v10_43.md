---
file_id: CONV_Atoms_atoms_v10_43
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v10 43

# 📚 Tài liệu Học tập LOM v4.4 Supreme
## Bài học: Các Lệnh Cơ Bản trên Linux

| Thuộc tính | Giá trị |
|------------|---------|
| **ID Tài liệu** | LMS_Atoms_atoms_v10_43 |
| **Tiêu đề** | Các Lệnh Cơ Bản trên Linux |
| **Loại** | Atomic Note |
| **Trạng thái** | standardized |
| **Nguồn** | [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## 🎯 Mục tiêu Học tập

Sau khi hoàn thành bài học này, học viên sẽ có khả năng:

- **Thao tác với hệ thống tệp tin** mà không cần giao diện đồ họa (GUI)
- **Quản lý cấu trúc hệ thống** thông qua các lệnh di chuyển, sao chép và phân quyền
- **Xử lý dữ liệu nhanh chóng** từ các file văn bản và CSV
- **Kết hợp các lệnh** để tạo chuỗi xử lý dữ liệu phức tạp

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 🛠 Môi trường Thực hành

### Hướng dẫn Thiết lập Môi trường

Để thực hành hiệu quả các lệnh trong bài học, học viên cần tạo các file mẫu sau:

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

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📖 Nội dung Học tập

### A. Quản lý File & Thư mục

#### Lệnh `mv` (Di chuyển/Đổi tên)
- **Mục đích**: Di chuyển file/thư mục hoặc đổi tên
- **Cú pháp**: `mv nguồn đích`
- **Ví dụ**:
  - `mv file1.txt file2.txt`: Đổi tên file1 thành file2
  - `mv file1.txt dir1/`: Chuyển file vào thư mục

#### Lệnh `cp` (Sao chép)
- **Mục đích**: Tạo bản sao của file/thư mục
- **Cú pháp**: `cp nguồn đích`
- **Ví dụ**: `cp file1.txt bản_sao.txt`

#### Lệnh `chmod` (Thay đổi quyền truy cập)
- **Mục đích**: Thay đổi quyền đọc, ghi, thực thi của file/thư mục
- **Cú pháp**: `chmod [quyền] tên_file`
- **Ví dụ**: `chmod +r file.html` - Cho phép mọi người đọc file

### B. Thao tác với Nội dung File

#### Lệnh `cut` (Cắt dữ liệu)
- **Mục đích**: Trích xuất các trường hoặc ký tự cụ thể từ file
- **Các tùy chọn phổ biến**:
  - `-f1`: Lấy trường (field) số 1
  - `-d","`: Dùng dấu phẩy làm dấu phân cách
  - `-c1-3`: Lấy các ký tự từ vị trí 1 đến 3

#### Lệnh `sort` (Sắp xếp)
- **Mục đích**: Sắp xếp các dòng trong file theo thứ tự
- **Các tùy chọn phổ biến**:
  - Mặc định: Sắp xếp theo bảng chữ cái (A-Z)
  - `-r`: Sắp xếp ngược (Z-A)
  - `-n`: Sắp xếp theo giá trị số

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 🔍 Phân tích Pipeline Nâng cao

### Ví dụ: Tìm 10 file lớn nhất trong thư mục

```bash
ls -l | cut -w -f5,9 | sort -rn | head -10
```

**Phân tích từng bước**:

| Bước | Lệnh | Mô tả | Kết quả |
|------|------|-------|---------|
| 1 | `ls -l` | Liệt kê chi tiết file (kích thước ở cột 5, tên ở cột 9) | Danh sách file đầy đủ |
| 2 | `cut -w -f5,9` | `-w`: dùng khoảng trắng làm dấu phân cách; `-f5,9`: chỉ lấy cột 5 và 9 | Kích thước + tên file |
| 3 | `sort -rn` | `-n`: sắp xếp số; `-r`: giảm dần | Sắp xếp theo kích thước giảm dần |
| 4 | `head -10` | Lấy 10 dòng đầu tiên | 10 file lớn nhất |

**Kết quả cuối cùng**: 10 file có dung lượng lớn nhất trong thư mục hiện tại!

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📝 Bài tập Thực hành

### Bài tập 1: Cơ bản
Thực hiện lệnh sau và quan sát kết quả:
```bash
cut -f1 -d"," addressbook.csv | sort -r
```

### Bài tập 2: Trung bình
Tạo một pipeline để tìm 5 tên người đầu tiên theo thứ tự bảng chữ cái từ file `addressbook.csv`.

### Bài tập 3: Nâng cao
Viết lệnh để tìm các file có đuôi `.txt` trong thư mục hiện tại và sắp xếp theo kích thước tăng dần.

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## ✅ Kiểm tra Hiểu biết

### Câu hỏi Trắc nghiệm

**Câu 1**: Lệnh nào dùng để đổi tên file trong Linux?
- A) `rename`
- B) `mv`
- C) `cp`
- D) `rm`

**Câu 2**: Để sắp xếp số theo thứ tự tăng dần, bạn nên dùng tùy chọn nào với lệnh `sort`?
- A) `-r`
- B) `-n`
- C) `-rn`
- D) `-nr`

**Câu 3**: Lệnh `chmod +r file.txt` làm gì?
- A) Xóa quyền đọc của file
- B) Thêm quyền đọc cho file
- C) Thêm quyền ghi cho file
- D) Thêm quyền thực thi cho file

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📚 Tài nguyên Bổ sung

- **Tài liệu tham khảo chính**: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **Video hướng dẫn**: Có thể tìm thấy trong thư viện tài nguyên đi kèm
- **Môi trường thực hành**: Sử dụng bất kỳ hệ điều hành Linux nào hoặc WSL trên Windows

---

## 🏆 Kết luận

Bài học này cung cấp nền tảng vững chắc cho việc tương tác với hệ thống tệp tin Linux thông qua dòng lệnh. Việc thành thạo các lệnh cơ bản này là bước đệm quan trọng cho các tác vụ quản trị hệ thống và xử lý dữ liệu nâng cao sau này.

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)