---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v13_10
  title: Thử với tham số cấu hình --psm 3 (tự động phát hiện văn bản)
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu và hướng dẫn tiếp theo để giải quyết vấn đề Tesseract trả về kết quả rỗng.

### **TRÍCH XUẤT TRI THỨC (Facts)**

- **Fact:** [Tesseract OCR là công cụ mã nguồn mở hỗ trợ nhận diện văn bản đa ngôn ngữ, bao gồm tiếng Việt (gói ngôn ngữ 'vie'), hoạt động không cần kết nối internet.]
- **Source:** [v13 - Section: 1. Công cụ miễn phí để chụp ảnh và OCR]
- **Tag:** [vv13]

- **Fact:** [Việc tiền xử lý hình ảnh bằng thư viện OpenCV (như chuyển sang ảnh xám, khử nhiễu bằng medianBlur và sử dụng adaptiveThreshold) là cần thiết để cải thiện độ chính xác của OCR đối với ảnh chất lượng thấp.]
- **Source:** [v13 - Section: 2. Phương án xử lý ảnh trước với Tesseract OCR]
- **Tag:** [vv13]

- **Fact:** [Tự động hóa bằng OCR có thể rút ngắn thời gian xử lý một bản khảo sát xuống còn khoảng 15-20 giây, so với 2 phút khi nhập liệu thủ công.]
- **Source:** [v13 - Section: 1. So sánh thời gian]
- **Tag:** [vv13]

- **Fact:** [Thư viện `pytesseract` trong Python đóng vai trò là giao diện (wrapper) để gọi thực thi tệp `tesseract.exe` từ hệ thống.]
- **Source:** [v13 - Section: 3.1 Mở Command Prompt và cài thư viện]
- **Tag:** [vv13]

---

### **HƯỚNG DẪN TIẾP THEO (Xử lý lỗi kết quả rỗng)**

Việc `image_to_string` không trả về gì (chuỗi rỗng) thường do Tesseract không tìm thấy vùng văn bản nào khả dụng hoặc cấu hình nhận diện chưa phù hợp. Hãy thử các bước kiểm tra sau ngay trong cửa sổ Python (REPL) đang mở:

#### **1. Kiểm tra xem Python có thực sự tìm thấy file ảnh không**
Nhập lệnh sau:
```python
import os
print(os.path.exists(r"C:\Users\anngu\Desktop\test_image.png"))
```
- Nếu kết quả là `False`: Đường dẫn file bị sai hoặc file không nằm ở Desktop.
- Nếu kết quả là `True`: Tiếp tục bước 2.

#### **2. Thử cấu hình Page Segmentation Mode (PSM)**
Đôi khi Tesseract cần được chỉ dẫn cách đọc ảnh (ví dụ: coi ảnh là một khối văn bản duy nhất). Hãy thử lệnh này:
```python
# Thử với tham số cấu hình --psm 3 (tự động phát hiện văn bản)
print(pytesseract.image_to_string(r"C:\Users\anngu\Desktop\test_image.png", config='--psm 3'))
```

#### **3. Kiểm tra bằng một ảnh cực kỳ đơn giản**
Nếu vẫn không ra kết quả, bạn hãy:
1. Mở Notepad, gõ chữ "HELLO WORLD".
2. Chụp màn hình chữ đó và lưu thành `C:\Users\anngu\Desktop\hello.png`.
3. Chạy lệnh:
```python
print(pytesseract.image_to_string(r"C:\Users\anngu\Desktop\hello.png"))
```

**Nếu bước 3 ra chữ "HELLO WORLD"**, nghĩa là hệ thống đã chạy tốt, vấn đề nằm ở chất lượng ảnh `test_image.png` của bạn (quá mờ, quá nhỏ hoặc quá nhiễu).

Hãy thử và cho tôi biết kết quả của từng bước nhé!