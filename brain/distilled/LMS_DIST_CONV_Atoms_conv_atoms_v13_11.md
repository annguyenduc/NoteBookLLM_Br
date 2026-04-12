---
file_id: CONV_Atoms_conv_atoms_v13_11
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v13 11

# Tài liệu Học Tập: Xử Lý Ngắt Dòng Sai Trong OCR với Tesseract và Python

## Thông Tin Tài Liệu
| Thuộc tính | Giá trị |
|------------|---------|
| Mã tài liệu | LOM-v4.4-Supreme-VV13 |
| Ngôn ngữ | Tiếng Việt |
| Loại nội dung | Hướng dẫn lập trình thực hành |
| Đối tượng học viên | Lập trình viên Python, Kỹ sư xử lý ảnh |
| Thời lượng ước tính | 45 phút |

---

## Mục Tiêu Học Tập

Sau khi hoàn thành tài liệu này, học viên sẽ có khả năng:

- Hiểu nguyên nhân gây ra hiện tượng ngắt dòng sai trong kết quả OCR của Tesseract
- Áp dụng các kỹ thuật xử lý hậu kỳ để nối các từ bị gãy do ngắt dòng sai
- Sử dụng đúng chế độ phân đoạn trang (`--psm`) để tối ưu hóa kết quả OCR
- Triển khai giải pháp xử lý văn bản tiếng Việt từ ảnh quét

---

## Kiến Thức Cơ Sở

### 1. Ký tự đại diện trong Regex
> **[CONV]** Trong Biểu thức Chính quy (Regex), ký tự `.` đại diện cho bất kỳ ký tự đơn nào ngoại trừ ký tự dòng mới (`\n`).  
*Tag: [vv13]* [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 2. Ký tự định vị trong Regex
> **[CONV]** Các ký tự định vị trong Regex bao gồm `^` (khớp vị trí bắt đầu chuỗi) và `$` (khớp vị trí kết thúc chuỗi).  
*Tag: [vv13]* [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 3. Cài đặt ngôn ngữ tiếng Việt cho Tesseract
> **[CONV]** Để Tesseract nhận diện tiếng Việt chính xác, cần tải tệp `vie.traineddata` vào thư mục `tessdata` và thiết lập tham số `lang='vie'`.  
*Tag: [vv13]* [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 4. Chế độ phân đoạn trang PSM 6
> **[CONV]** Chế độ `--psm 6` (Page Segmentation Mode) trong Tesseract giúp xử lý hình ảnh dưới dạng một khối văn bản đồng nhất, giúp cải thiện độ chính xác cho các đoạn văn bản có cấu trúc đều.  
*Tag: [vv13]* [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 5. Tiền xử lý ảnh trước OCR
> **[CONV]** Thư viện `Pillow` (PIL) có thể dùng để tiền xử lý ảnh (chuyển thang xám, làm sắc nét) trước khi đưa vào OCR để giảm nhiễu.  
*Tag: [vv13]* [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Vấn Đề Thường Gặp

Khi sử dụng Tesseract để nhận diện văn bản tiếng Việt từ ảnh, người dùng thường gặp hiện tượng:

- **Ngắt dòng sai**: Văn bản bị chia cắt không đúng vị trí, ví dụ: "Đại diện" bị tách thành "Đại" và "ện"
- **Thiếu khoảng trắng**: Các từ bị dính liền nhau do xử lý sai bố cục
- **Hiểu sai cấu trúc văn bản**: Tesseract nhầm lẫn giữa các đoạn văn và tiêu đề

---

## Giải Pháp Thực Hành

### So Sánh Mã Nguồn

| **Mã Gốc (Bị lỗi ngắt dòng)** | **Mã Cải Tiến (Xử lý từ bị gãy)** |
| :--- | :--- |
| ```python
import pytesseract
from PIL import Image

# Mở ảnh
img = Image.open(r"C:\Users\anngu\Desktop\test_image.png")

# OCR cơ bản
text = pytesseract.image_to_string(img, lang='vie')
print(text)
``` | ```python
import pytesseract
from PIL import Image
import re

# 1. Cấu hình đường dẫn (nếu cần)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 2. Mở ảnh
img = Image.open(r"C:\Users\anngu\Desktop\test_image.png")

# 3. Sử dụng cấu hình --psm 6 để đọc khối văn bản tốt hơn
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, lang='vie', config=custom_config)

# 4. Xử lý hậu kỳ: Nối các từ bị gãy do xuống dòng sai
# Nếu một dòng không kết thúc bằng dấu câu (.!?:), nối nó với dòng sau
lines = text.splitlines()
cleaned_lines = []
for i in range(len(lines)):
    line = lines[i].strip()
    if not line: continue
    # Nếu dòng hiện tại không kết thúc bằng dấu ngắt câu, nối với dòng tiếp theo
    if i < len(lines) - 1 and not line.endswith(('.', ':', '!', '?')):
        cleaned_lines.append(line + " ")
    else:
        cleaned_lines.append(line + "\n")

final_text = "".join(cleaned_lines)
print(final_text)
``` |

---

## Phân Tích Giải Pháp

### 1. Sử dụng `--psm 6`
Chế độ phân đoạn trang 6 giả định ảnh là một khối văn bản duy nhất, giúp Tesseract ít bị "loạn" khi thấy các ký tự đặc biệt.

### 2. Logic nối dòng thông minh
Đoạn code mới kiểm tra: Nếu một dòng kết thúc mà không có dấu chấm hay dấu hai chấm, hệ thống hiểu rằng từ đó đang bị gãy và sẽ tự động nối lại thành một câu hoàn chỉnh.

### 3. Hàm `strip()`
Loại bỏ các khoảng trắng thừa ở đầu và cuối dòng để tránh việc chữ bị dính vào nhau một cách lộn xộn.

---

## Bài Tập Thực Hành

### Worksheet: Xử Lý Văn Bản OCR Bị Gãy Từ

**Hướng dẫn**: Sử dụng đoạn mã cải tiến bên trên để xử lý các tình huống sau:

#### Tình Huống 1: Văn bản bị ngắt giữa từ
```
Input: "Đại\nện"
Output mong muốn: "Đại diện"
```

#### Tình Huống 2: Văn bản có nhiều dòng liên tục
```
Input: 
"Hôm nay trời đẹp.\nChúng ta đi\nchơi công viên."

Output mong muốn:
"Hôm nay trời đẹp.\nChúng ta đi chơi công viên."
```

#### Tình Huống 3: Văn bản có dấu câu đặc biệt
```
Input:
"Xin chào!\nTôi tên là\nAn."

Output mong muốn:
"Xin chào!\nTôi tên là An."
```

---

## Câu Hỏi Kiểm Tra

### Quiz: Xử Lý OCR với Tesseract

**Câu 1**: Chế độ `--psm 6` trong Tesseract có tác dụng gì?
- A. Phát hiện ngôn ngữ tự động
- B. Xử lý hình ảnh dưới dạng một khối văn bản đồng nhất
- C. Tăng tốc độ xử lý ảnh
- D. Giảm kích thước bộ nhớ đệm

**Câu 2**: Ký tự nào trong Regex đại diện cho bất kỳ ký tự đơn nào ngoại trừ ký tự dòng mới?
- A. `^`
- B. `$`
- C. `.`
- D. `*`

**Câu 3**: Để Tesseract nhận diện tiếng Việt chính xác, cần thiết lập tham số nào?
- A. `lang='en'`
- B. `lang='vi'`
- C. `lang='vie'`
- D. `lang='vn'`

**Câu 4**: Hàm nào được sử dụng để loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi?
- A. `trim()`
- B. `strip()`
- C. `clean()`
- D. `remove()`

**Câu 5**: Khi nào nên nối dòng hiện tại với dòng tiếp theo trong xử lý hậu kỳ?
- A. Khi dòng hiện tại kết thúc bằng dấu chấm
- B. Khi dòng hiện tại không kết thúc bằng dấu ngắt câu
- C. Khi dòng hiện tại có ít hơn 3 từ
- D. Khi dòng hiện tại chứa số

---

## Tài Nguyên Bổ Sung

- [Tài liệu chính thức Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Hướng dẫn cài đặt ngôn ngữ tiếng Việt](https://github.com/tesseract-ocr/tessdata)
- [Thư viện Pillow cho xử lý ảnh](https://pillow.readthedocs.io/)
- [Biểu thức chính quy trong Python](https://docs.python.org/3/library/re.html)

---

## Ghi Chú Hệ Thống

> **Lưu ý**: Tất cả các sự kiện kỹ thuật quan trọng trong tài liệu này đều có liên kết đến nguồn gốc tại [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) để đảm bảo tính toàn vẹn và khả năng truy xuất nguồn thông tin.

![Minh họa quy trình OCR](../../brain/raw/lms_multi_media_dump/assets/input_image1.png)  
*Hình 1: Sơ đồ quy trình xử lý OCR với các bước tiền xử lý và hậu xử lý*

---

*Tài liệu được tạo bởi Content Engineer theo tiêu chuẩn LOM v4.4 Supreme*  
*Ngày tạo: [DATE_STAMP]*  
*Phiên bản: 1.0*