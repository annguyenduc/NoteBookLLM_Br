---
file_id: CONV_Atoms_conv_atoms_v10_44
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v10 44

# 📚 Tài liệu học tập chuẩn LOM v4.4 Supreme
## LMS_Atoms_conv_atoms_v10_44

| Thuộc tính | Giá trị |
|------------|---------|
| **ID Tài liệu** | LMS_Atoms_conv_atoms_v10_44 |
| **Tiêu đề** | Tạo Script Bash để Tự động Hóa Công Việc Hệ Thống |
| **Loại tài liệu** | Bài học nguyên tử (Atomic Lesson) |
| **Trạng thái** | Đã chuẩn hóa |
| **Nguồn gốc** | [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## 🎯 Mục tiêu học tập

Sau khi hoàn thành bài học này, học viên sẽ có khả năng:
- Viết script Bash đơn giản để tự động hóa các tác vụ hệ thống
- Sử dụng cú pháp Shebang và command substitution hiệu quả
- Kết hợp nhiều lệnh thành một script thực thi duy nhất

---

## 📖 Nội dung chính

### #1. Cấu trúc cơ bản của script Bash

**Khái niệm**: Một script Bash tiêu chuẩn bắt đầu bằng dòng Shebang `#!/bin/bash` để chỉ định trình thông dịch [vv10].

**Cú pháp**:
```bash
#!/bin/bash
# Nội dung script ở đây
```

**Ý nghĩa**: Dòng đầu tiên báo cho hệ điều hành biết rằng file này nên được thực thi bằng trình thông dịch bash.

### #2. Command Substitution - Lấy kết quả lệnh vào chuỗi

**Cú pháp**: `$(lệnh)` hoặc `` `lệnh` ``

**Ví dụ**:
```bash
echo "Thời gian hiện tại: $(date)"
```

**Kết quả**: Hiển thị "Thời gian hiện tại: Thứ Hai 15 Tháng 1 10:30:45 ICT 2024" [vv10].

### #3. Các lệnh hệ thống phổ biến trong script

| Lệnh | Chức năng | Mô tả chi tiết |
|------|-----------|---------------|
| `date` | Hiển thị thời gian hệ thống | Trả về ngày giờ hiện tại của máy tính [vv10] |
| `uptime` | Thông tin thời gian hoạt động | Hiển thị thời gian hệ thống đã chạy, số người dùng, tải trung bình [vv10] |
| `free` | Trạng thái bộ nhớ | Hiển thị thông tin RAM và bộ nhớ Swap [vv10] |
| `who` | Người dùng đang đăng nhập | Liệt kê các tài khoản đang truy cập hệ thống [vv10] |

### #4. Kết hợp nhiều lệnh trên một dòng

**Cú pháp**: Sử dụng dấu chấm phẩy `;` để phân cách các lệnh [vv10].

**Ví dụ**:
```bash
echo "Bắt đầu"; date; echo "Kết thúc"
```

**Lợi ích**: Giúp viết script ngắn gọn và hiệu quả hơn.

---

## 🛠 Hướng dẫn thực hành

### Bước 1: Tạo file script
```bash
nano gather-information.sh
```

### Bước 2: Viết nội dung script hoàn chỉnh
```bash
#!/bin/bash

echo "Bắt đầu thực thi lúc: $(date)"
echo

echo "THỜI GIAN HOẠT ĐỘNG HỆ THỐNG"
uptime
echo

echo "TRẠNG THÁI BỘ NHỚ"
free
echo

echo "NGƯỜI DÙNG HIỆN TẠI"
who
echo

echo "Kết thúc lúc: $(date)"
```

### Bước 3: Cấp quyền thực thi
```bash
chmod +x gather-information.sh
```

> **Lưu ý**: Bước này là bắt buộc để hệ thống cho phép thực thi file script [Unverified_Source].

### Bước 4: Chạy script
```bash
./gather-information.sh
```

---

## 📋 Worksheet: Thực hành viết script

### Bài tập 1: Script kiểm tra hệ thống cơ bản
**Yêu cầu**: Tạo file `system_check.sh` thực hiện các công việc sau:
1. In ra dòng tiêu đề "=== KIỂM TRA HỆ THỐNG ==="
2. Hiển thị thời gian hiện tại
3. Hiển thị tên máy tính sử dụng `$(hostname)`
4. Liệt kê thư mục hiện tại
5. In ra dòng "=== KẾT THÚC KIỂM TRA ==="

**Gợi ý mã nguồn**:
```bash
#!/bin/bash
echo "=== KIỂM TRA HỆ THỐNG ==="
echo "Thời gian: $(date)"
echo "Tên máy: $(hostname)"
ls -la
echo "=== KẾT THÚC KIỂM TRA ==="
```

### Bài tập 2: Script nâng cao
**Yêu cầu**: Viết script hiển thị thông tin hệ thống theo định dạng:
```
Hệ thống: [tên máy] - Thời gian: [giờ hiện tại]
Người dùng đang hoạt động: [số lượng người dùng]
Bộ nhớ còn trống: [RAM còn lại]
```

---

## 🧠 Quiz đánh giá kiến thức

### Câu hỏi 1: Cú pháp nào là đúng để bắt đầu một script Bash?
- A) `#!/bin/sh`
- B) `#!/bin/bash`  
- C) `#bash`
- D) `#!/bash`

**Đáp án đúng**: B

### Câu hỏi 2: Cú pháp `$(date)` thực hiện chức năng gì?
- A) Hiển thị ngày tháng năm
- B) Thực thi lệnh `date` và chèn kết quả vào chuỗi  
- C) Lưu trữ ngày vào biến
- D) So sánh ngày tháng

**Đáp án đúng**: B

### Câu hỏi 3: Dấu `;` trong Bash script dùng để làm gì?
- A) Kết thúc lệnh
- B) Phân cách các lệnh trên cùng một dòng  
- C) Ghi chú
- D) Khai báo biến

**Đáp án đúng**: B

### Câu hỏi 4: Lệnh nào hiển thị người dùng đang đăng nhập?
- A) `users`
- B) `whoami`
- C) `who`  
- D) `login`

**Đáp án đúng**: C

### Câu hỏi 5: Trước khi chạy script bằng `./`, bạn cần làm gì?
- A) Sao chép script
- B) Đổi tên file
- C) Cấp quyền thực thi bằng `chmod +x`  
- D) Di chuyển đến thư mục khác

**Đáp án đúng**: C

---

## 💡 Scenario ứng dụng thực tế

### Tình huống: Quản trị viên hệ thống cần kiểm tra trạng thái máy chủ hàng ngày

**Vấn đề**: Mỗi sáng, quản trị viên phải lần lượt chạy 4-5 lệnh để kiểm tra tình trạng máy chủ: thời gian hoạt động, bộ nhớ, người dùng đang truy cập, v.v.

**Giải pháp**: Viết script Bash tự động hóa toàn bộ quá trình này.

**Script mẫu**:
```bash
#!/bin/bash
# Script kiểm tra hệ thống hàng ngày
# Tác giả: Quản trị viên IT
# Ngày tạo: $(date)

echo "=== BÁO CÁO HỆ THỐNG HÀNG NGÀY ==="
echo "Thời gian kiểm tra: $(date)"
echo "Tên máy chủ: $(hostname)"
echo
echo "[1] Thời gian hoạt động:"
uptime
echo
echo "[2] Bộ nhớ hệ thống:"
free -h
echo
echo "[3] Người dùng đang đăng nhập:"
who
echo
echo "=== KẾT THÚC BÁO CÁO ==="
```

**Lợi ích**: 
- Tiết kiệm thời gian
- Giảm sai sót do bỏ sót lệnh
- Tạo báo cáo chuẩn hóa
- Có thể lên lịch tự động chạy bằng cron job

---

## 🔗 Tài nguyên bổ sung

- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Nguồn tham chiếu chính
- Tài liệu Bash scripting nâng cao
- Video hướng dẫn thực hành tương tác

---

## 📈 Đánh giá kết quả học tập

| Tiêu chí | Mức độ đạt được |
|----------|-----------------|
| Hiểu cấu trúc Shebang | ✅ |
| Sử dụng command substitution | ✅ |
| Kết hợp nhiều lệnh trong script | ✅ |
| Cấp quyền và thực thi script | ✅ |
| Viết script thực tế đơn giản | ✅ |