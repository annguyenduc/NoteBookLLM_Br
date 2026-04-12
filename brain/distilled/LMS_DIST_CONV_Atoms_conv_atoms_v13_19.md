---
file_id: CONV_Atoms_conv_atoms_v13_19
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v13 19

# Tài liệu Học tập LOM v4.4 Supreme
## Chủ đề: Lập trình Python cơ bản và Công cụ giả lập Android cho IoT

---

## 1. Tổng Quan

### Mục tiêu học tập
Sau khi hoàn thành bài học này, học viên sẽ:
- Hiểu và áp dụng được các hàm và cú pháp cơ bản trong Python
- Biết cách kiểm tra số chẵn/lẻ, số nguyên tố, chuỗi đối xứng
- Sử dụng thư viện `re` để xử lý chuỗi và trích xuất dữ liệu
- So sánh và lựa chọn công cụ giả lập Android phù hợp cho IoT
- Hiểu cách tối ưu hóa môi trường giả lập cho các ứng dụng IoT

### Đối tượng học viên
- Học sinh THCS, THPT
- Sinh viên ngành Công nghệ Thông tin, Điện tử Viễn thông
- Người mới bắt đầu học lập trình Python và IoT

---

## 2. Nội dung học tập

### 2.1. Các hàm và cú pháp Python cơ bản

#### Hàm `range()` trong vòng lặp
Trong Python, hàm `range(1, 11)` được sử dụng để tạo ra một dãy số nguyên liên tiếp từ 1 đến 10. Đây là công cụ quan trọng trong việc thực hiện các vòng lặp đếm [vv13].

```python
for i in range(1, 11):
    print(i)
```

#### Kiểm tra số chẵn/lẻ
Để kiểm tra một số là chẵn hay lẻ trong Python, ta sử dụng toán tử chia lấy dư `% 2`. Nếu kết quả bằng 0 thì đó là số chẵn [vv13].

```python
num = int(input("Nhập một số: "))
if num % 2 == 0:
    print(f"{num} là số chẵn")
else:
    print(f"{num} là số lẻ")
```

### 2.2. Xử lý chuỗi trong Python

#### Đảo ngược chuỗi
Cú pháp `text[::-1]` trong Python là một cách ngắn gọn để đảo ngược một chuỗi ký tự, thường dùng để kiểm tra tính đối xứng (palindrome) [vv13].

```python
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("racecar"))  # True
```

#### Kiểm tra loại ký tự
Phương thức `isalpha()` được dùng để nhận biết ký tự chữ cái, trong khi `isdigit()` dùng để nhận biết ký tự chữ số trong một chuỗi [vv13].

| Phương thức | Chức năng |
|-------------|-----------|
| `isalpha()` | Kiểm tra ký tự là chữ cái |
| `isdigit()` | Kiểm tra ký tự là chữ số |
| `isalnum()` | Kiểm tra ký tự là chữ cái hoặc số |

### 2.3. Thuật toán nâng cao

#### Kiểm tra số nguyên tố
Thuật toán kiểm tra số nguyên tố có thể tối ưu bằng cách chỉ kiểm tra các ước số trong khoảng từ 2 đến căn bậc hai của số đó (`int(num**0.5) + 1`) [vv13].

```python
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

#### Trích xuất số từ chuỗi
Thư viện `re` (Regular Expression) với biểu thức `r'\d+'` cho phép tìm và trích xuất tất cả các cụm số (bao gồm số có nhiều chữ số) từ một chuỗi văn bản [vv13].

```python
import re

text = "Tôi có 12 quả táo và 8 quả cam"
numbers = re.findall(r'\d+', text)
total = sum(int(num) for num in numbers)
print(f"Tổng số: {total}")  # 20
```

---

## 3. Công cụ giả lập Android cho IoT

### 3.1. So sánh các trình giả lập

| Trình giả lập | RAM tối thiểu | Hỗ trợ Bluetooth | Ghi chú đặc biệt |
|---------------|---------------|------------------|------------------|
| LDPlayer | 2GB | Không hỗ trợ trực tiếp | [vv13] |
| NoxPlayer | 1.5GB | Có (qua thiết lập hệ thống) | Hỗ trợ Multi-Instance [vv13] |
| Genymotion | Tùy cấu hình | Có (USB forwarding + ADB) | Độ khả thi cao nhất cho Bluetooth [vv13] |
| Phoenix OS | Tùy cấu hình | Có (truy cập phần cứng trực tiếp) | Hệ điều hành Android hoàn chỉnh [vv13] |
| PrimeOS | Tùy cấu hình | Có (truy cập phần cứng trực tiếp) | Hệ điều hành Android hoàn chỉnh [vv13] |

### 3.2. Kết nối Bluetooth trong môi trường giả lập

#### Khó khăn với thiết bị iOS
Module Bluetooth HC-05 thường gặp khó khăn khi kết nối trực tiếp với iPhone do các hạn chế về chính sách hỗ trợ thiết bị của hệ điều hành iOS [vv13].

#### Tối ưu hóa cho nhiều tài khoản
Để tối ưu hóa việc chạy nhiều phiên bản giả lập (nuôi tài khoản), người dùng nên giảm số lượng nhân CPU xuống 1-2 lõi và RAM xuống mức 512MB - 1GB cho mỗi phiên bản [vv13].

---

## 4. Worksheet Thực hành

### Bài 1: Xử lý số trong Python
1. Viết chương trình in ra các số chẵn từ 1 đến 20
2. Viết chương trình kiểm tra một số nhập vào có phải là số nguyên tố không
3. Viết chương trình tính tổng các số chẵn trong đoạn [1, 100]

### Bài 2: Xử lý chuỗi
1. Viết hàm kiểm tra chuỗi có phải là palindrome không
2. Đếm số ký tự chữ cái và chữ số trong một chuỗi bất kỳ
3. Trích xuất tất cả các số từ chuỗi: "Tôi năm nay 16 tuổi, học lớp 9A, ở nhà số 123 đường ABC"

### Bài 3: Lựa chọn công cụ giả lập
So sánh ưu nhược điểm của 3 trình giả lập LDPlayer, NoxPlayer và Genymotion trong việc phát triển ứng dụng IoT có sử dụng Bluetooth.

---

## 5. Quiz Trắc nghiệm

### Câu 1: Cú pháp Python nào sau đây tạo ra dãy số từ 1 đến 10?
A. `range(0, 10)`
B. `range(1, 10)`
C. `range(1, 11)`
D. `range(10)`

### Câu 2: Để kiểm tra số chẵn trong Python, ta dùng biểu thức nào?
A. `n % 3 == 0`
B. `n % 2 == 0`
C. `n // 2 == 0`
D. `n & 1 == 0`

### Câu 3: Cú pháp nào dùng để đảo ngược chuỗi trong Python?
A. `text.reverse()`
B. `text[-1::-1]`
C. `text[::-1]`
D. `reversed(text)`

### Câu 4: Trình giả lập nào có hỗ trợ Bluetooth tốt nhất cho IoT?
A. LDPlayer
B. NoxPlayer
C. Genymotion
D. BlueStacks

### Câu 5: Biểu thức regex nào trích xuất tất cả các số trong chuỗi?
A. `r'[0-9]'`
B. `r'\d'`
C. `r'\d+'`
D. `r'[0-9]+'`

---

## 6. Scenario Thực tế

### Tình huống: Phát triển ứng dụng IoT với Bluetooth
Bạn là kỹ sư IoT đang phát triển ứng dụng Android để điều khiển module Bluetooth HC-05. Ứng dụng cần:
- Giao tiếp với module HC-05 qua Bluetooth
- Hiển thị dữ liệu cảm biến nhận được
- Lưu lịch sử giao tiếp

**Yêu cầu:**
1. Lựa chọn trình giả lập phù hợp nhất cho quá trình phát triển
2. Giải thích lý do lựa chọn
3. Đề xuất phương pháp kiểm thử kết nối Bluetooth
4. Viết đoạn mã Python mô phỏng việc xử lý dữ liệu nhận được từ cảm biến

**Gợi ý giải pháp:**
- Nên chọn Genymotion vì hỗ trợ USB forwarding và ADB [vv13]
- Sử dụng thư viện `re` để xử lý dữ liệu cảm biến dạng chuỗi [vv13]
- Tối ưu hóa tài nguyên khi chạy nhiều phiên bản giả lập [vv13]

---

## 7. Tài nguyên tham khảo

- [vv13] - Bộ tài liệu Volume v13 về Python và IoT
- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

> **Lưu ý:** Tất cả các kiến thức quan trọng đều được dẫn nguồn đầy đủ theo quy tắc [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) [vv13].