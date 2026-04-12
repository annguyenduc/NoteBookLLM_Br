Dưới đây là đoạn mã hoàn chỉnh để liệt kê các tệp và thư mục trong thư mục "website", cùng với giải thích chi tiết và các sự kiện kỹ thuật theo yêu cầu của bạn.

### Mã Python hoàn chỉnh:

```python
import os

dir_path = "website"

# Kiểm tra xem thư mục có tồn tại không trước khi liệt kê
if os.path.exists(dir_path):
    for name in os.listdir(dir_path):
        # Tạo đường dẫn đầy đủ để kiểm tra thuộc tính
        fullname = os.path.join(dir_path, name)
        
        if os.path.isdir(fullname):
            print(f"Thư mục: {fullname}")
        else:
            print(f"Tập tin: {fullname}")
else:
    print(f"Thư mục '{dir_path}' không tồn tại.")
```

### Giải thích:
1.  **`os.listdir(dir)`**: Trả về một **danh sách (list)** chứa tên của các tệp tin và thư mục con nằm trong thư mục được chỉ định.
2.  **`os.path.join(dir, name)`**: Kết hợp tên thư mục và tên tệp để tạo thành một đường dẫn đầy đủ. Điều này rất quan trọng vì `os.listdir` chỉ trả về tên (ví dụ: `index.html`), không phải đường dẫn (ví dụ: `website/index.html`).
3.  **`os.path.isdir(fullname)`**: Kiểm tra xem đường dẫn đó là một thư mục hay là một tệp tin để bạn có thể xử lý riêng biệt.

---

### Trích xuất tri thức kỹ thuật (@scout):

- **Fact**: Lệnh `os.listdir()` trả về danh sách các tên tệp và thư mục trong một đường dẫn cụ thể, nhưng không bao gồm các ký hiệu đặc biệt như `.` hoặc `..`.
- **Source**: [vv16 - Section: Python OS Module Operations]
- **Tag**: [vv16]

- **Fact**: `os.path.join()` là phương thức tối ưu để tạo đường dẫn tệp vì nó tự động điều chỉnh dấu gạch chéo (`/` hoặc `\`) phù hợp với hệ điều hành đang chạy (Windows, macOS, hoặc Linux).
- **Source**: [vv16 - Section: Path Manipulations]
- **Tag**: [vv16]

- **Fact**: Trước khi thực hiện các thao tác như liệt kê hoặc xóa, việc sử dụng `os.path.exists()` giúp ngăn chặn lỗi `FileNotFoundError` trong Python.
- **Source**: [vv16 - Section: Error Handling in File Systems]
- **Tag**: [vv16]

- **Fact**: Trong lập trình Robot và IoT (như trên YoloBit hoặc Raspberry Pi), việc quản lý đường dẫn tuyệt đối (Absolute Path) giúp chương trình hoạt động ổn định hơn khi chạy dưới dạng dịch vụ hệ thống (system service).
- **Source**: [Unverified_Source]
- **Tag**: [Unverified_Source]