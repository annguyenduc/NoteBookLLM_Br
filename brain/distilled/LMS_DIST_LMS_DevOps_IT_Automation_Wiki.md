---
file_id: LMS_DevOps_IT_Automation_Wiki
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS DevOps IT Automation Wiki

# 📚 Tài Liệu Học Tập DevOps & Tự Động Hóa IT

## Thông Tin Tài Liệu
| Thuộc Tính | Giá Trị |
|------------|---------|
| **Tiêu Đề** | DevOps & Tự Động Hóa IT Cơ Bản |
| **Mã Học Phần** | DEVOPS-101 |
| **Thời Lượng** | 40 giờ học |
| **Đối Tượng** | Kỹ sư hệ thống, lập trình viên |
| **Trình Độ** | Trung cấp |
| **Ngôn Ngữ** | Tiếng Việt |

---

## 🎯 Mục Tiêu Học Tập

Sau khi hoàn thành khóa học này, học viên sẽ có khả năng:

- **Hiểu biết nền tảng** về lập trình Python trong môi trường DevOps [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **Thực hiện tự động hóa** các tác vụ hệ thống Windows/Linux [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **Quản trị mạng cơ bản** và xử lý sự cố kết nối [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **Áp dụng các công cụ giám sát** và phân tích log hệ thống [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📖 Bài Học 1: Lập Trình Python Cho DevOps

### 1.1 Nguyên Tắc Lập Trình Cơ Bản

#### ✅ **Nguyên Tắc DRY (Don't Repeat Yourself)**
- **Định nghĩa**: Tránh lặp lại mã nguồn, tái sử dụng logic lập trình
- **Lợi ích**: Giảm lỗi, dễ bảo trì, tăng hiệu quả phát triển
- **Ví dụ thực tế**: Tạo hàm chung thay vì copy-paste đoạn mã xử lý file [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### ✅ **Đặt Tên Biến Gợi Nhớ**
```python
# ❌ Sai
x = 5
y = 10

# ✅ Đúng
user_age = 5
max_attempts = 10
```

### 1.2 Cấu Trúc Lặp Trong Python

| Loại Vòng Lặp | Mục Đích | Ví Dụ |
|---------------|----------|-------|
| `for` | Lặp qua dãy dữ liệu | `for i in range(10):` |
| `while` | Lặp điều kiện | `while condition:` |
| `Recursion` | Hàm gọi chính nó | `factorial(n)` |

### 1.3 Xử Lý Lỗi Thường Gặp

| Lỗi | Mô Tả | Cách Xử Lý |
|-----|-------|------------|
| `FileNotFoundError` | Không tìm thấy file | Kiểm tra đường dẫn tồn tại |
| `ModuleNotFoundError` | Module không được cài đặt | Cài đặt package cần thiết |
| `PermissionError` | Thiếu quyền truy cập | Kiểm tra quyền hệ thống |

---

## 🌐 Bài Học 2: Mạng Máy Tính & Quản Trị Hệ Thống

### 2.1 Kiến Thức Mạng Cơ Bản

#### 🔧 **IP Addressing**
- **IPv4**: 192.168.1.1 (32-bit)
- **IPv6**: 2001:0db8::1 (128-bit)
- **Subnet Mask**: Xác định mạng con [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### 🔗 **WAN/LAN**
- **LAN**: Mạng cục bộ (trong văn phòng)
- **WAN**: Mạng diện rộng (liên kết nhiều chi nhánh)

### 2.2 Công Cụ Quản Trị Hệ Thống

#### 📊 **Phân Tích Log (File Mining)**

| Lệnh | Mô Tả | Ứng Dụng |
|------|-------|----------|
| `tail -f /var/log/syslog` | Theo dõi log thời gian thực | Giám sát hệ thống |
| `grep -i "error" logfile.txt` | Tìm kiếm lỗi (không phân biệt hoa thường) | Phát hiện sự cố |
| `cut -d',' -f2 log.csv \| sort \| uniq -c` | Trích xuất, sắp xếp, đếm tần suất | Phân tích dữ liệu |

#### ⚙️ **Quản Lý Tiến Trình**

| Lệnh | Mô Tả | Mục Đích |
|------|-------|----------|
| `top` hoặc `htop` | Giám sát tài nguyên hệ thống | Theo dõi CPU/RAM |
| `kill -15 <pid>` | Gửi tín hiệu kết thúc nhẹ nhàng | Shutdown graceful |
| `kill -9 <pid>` | Buộc dừng ngay lập tức | Force kill |

---

## 🤖 Bài Học 3: Tự Động Hóa Với Python

### 3.1 Framework Pytest

#### ✅ **Ưu Điểm Của Pytest**
- Dễ đọc, dễ viết test case
- Hỗ trợ fixture mạnh mẽ
- Tích hợp tốt với CI/CD

#### 🧪 **Cấu Trúc Test Cơ Bản**
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def test_divide():
    assert divide(10, 2) == 5
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

### 3.2 Error Handling Trong Tự Động Hóa

#### 🛡️ **Sử Dụng Try-Except**
```python
try:
    # Thao tác I/O hoặc API call
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File không tồn tại!")
except PermissionError:
    print("Không đủ quyền truy cập!")
```

---

## 📋 Phiếu Thực Hành (Worksheet)

### Bài Tập 1: Viết Script Python Cơ Bản

**Yêu cầu**: Viết chương trình Python thực hiện các chức năng sau:
1. Đọc file log hệ thống
2. Tìm kiếm các dòng chứa từ khóa "ERROR"
3. Đếm số lượng lỗi tìm thấy
4. Xuất kết quả ra màn hình

**Hướng dẫn**:
- Sử dụng `open()` để đọc file
- Dùng `readlines()` để đọc từng dòng
- Áp dụng `if` để kiểm tra từ khóa
- Sử dụng `count()` để đếm số lượng [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Bài Tập 2: Tự Động Hóa Quản Trị

**Yêu cầu**: Tạo script Python thực hiện:
1. Kiểm tra trạng thái dịch vụ trên hệ thống
2. Nếu dịch vụ ngừng hoạt động, gửi thông báo email
3. Ghi log hoạt động vào file

**Công cụ đề xuất**: `subprocess`, `smtplib`, `logging`

---

## 🧠 Câu Hỏi Trắc Nghiệm (Quiz)

### Câu 1: Nguyên tắc DRY trong lập trình có nghĩa là gì?
A. Don't Repeat Yourself  
B. Do Run Yourself  
C. Data Return Yearly  
D. Dynamic Resource Yield  

**Đáp án đúng**: A [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 2: Lệnh nào dùng để theo dõi log thời gian thực?
A. `cat /var/log/syslog`  
B. `tail -f /var/log/syslog`  
C. `head /var/log/syslog`  
D. `less /var/log/syslog`  

**Đáp án đúng**: B [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 3: Trong Python, lỗi nào xảy ra khi không tìm thấy module?
A. `FileNotFoundError`  
B. `ImportError`  
C. `ModuleNotFoundError`  
D. `NameError`  

**Đáp án đúng**: C [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 🎭 Tình Huống Thực Tế (Scenario)

### Tình Huống: Giám Sát Hệ Thống Sản Xuất

**Bối cảnh**: Bạn là kỹ sư DevOps tại một công ty thương mại điện tử. Hệ thống đang gặp sự cố gián đoạn dịch vụ định kỳ mỗi ngày vào buổi sáng.

**Nhiệm vụ**:
1. Thiết kế script giám sát log hệ thống
2. Phát hiện nguyên nhân sự cố
3. Tự động hóa quá trình khắc phục
4. Báo cáo cho quản lý

**Yêu cầu kỹ thuật**:
- Sử dụng Python để phân tích log
- Tích hợp với hệ thống cảnh báo
- Tự động restart dịch vụ khi cần
- Ghi nhật ký hoạt động [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📚 Tài Liệu Tham Khảo

- **Python Official Documentation** - Tài liệu chính thức Python
- **Linux Command Line** - Hướng dẫn dòng lệnh Linux
- **DevOps Best Practices** - Thực hành tốt trong DevOps
- **Network Fundamentals** - Kiến thức mạng cơ bản [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 🏆 Kết Luận

Khóa học này cung cấp nền tảng vững chắc về DevOps và tự động hóa IT, giúp học viên:
- Hiểu rõ quy trình vận hành hệ thống
- Thành thạo công cụ quản trị
- Phát triển kỹ năng lập trình ứng dụng
- Chuẩn bị cho vị trí DevOps Engineer [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

> **Ghi chú**: Nội dung được cập nhật với DNA Công nghệ ML4Kids @librarian v4.4  
> **📖 Nguồn xác thực**: Master Automation Scripts & Windows Ops Logs [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)