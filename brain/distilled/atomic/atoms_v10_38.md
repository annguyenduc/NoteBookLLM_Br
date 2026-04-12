Chào bạn, tôi là **@scout**. Tôi đã thực hiện chưng cất tri thức từ nguồn dữ liệu **Volume v10** bạn cung cấp về `unittest`. 

Dưới đây là các sự kiện kỹ thuật (Facts) được trích xuất theo quy tắc **LOM v4.1**:

### 📋 TRÍCH XUẤT SỰ KIỆN (FACTS) - UNITTEST

- **Fact:** Unit tests được thiết kế để kiểm tra các phần nhỏ của mã nguồn như một hàm hoặc phương thức đơn lẻ nhằm đảm bảo chúng hoạt động đúng kỳ vọng.
- **Source:** Đoạn 1 (Unit tests help to isolate errors...).
- **Tag:** [vv10]

- **Fact:** `unittest` là một framework kiểm thử đơn vị theo hướng đối tượng (object-oriented) trong Python.
- **Source:** Đoạn 2 (You’ve also learned about the object-oriented concepts of unittest...).
- **Tag:** [vv10]

- **Fact:** Để viết các test case, lập trình viên cần tạo các lớp con (subclasses) của `unittest.TestCase` hoặc sử dụng `FunctionTestCase`.
- **Source:** Phần Test cases (To write test cases, developers need to write subclasses of TestCase...).
- **Tag:** [vv10]

- **Fact:** Một phương thức kiểm thử chỉ được trình chạy test (test runner) nhận diện nếu tên phương thức đó bắt đầu bằng tiền tố `test`.
- **Source:** Phần Test cases (the TestCase subclass needs to implement a test method that starts with the name test...).
- **Tag:** [vv10]

- **Fact:** `unittest` sử dụng các phương thức assert riêng (như `assertEqual`, `assertTrue`, `assertFalse`) thay vì câu lệnh `assert` tiêu chuẩn để thu thập kết quả và tạo báo cáo.
- **Source:** Phần Assertions (Each of these assert methods is used in place of the standard assert statement...).
- **Tag:** [vv10]

- **Fact:** Phương thức `assertRaises()` được sử dụng để xác minh xem một ngoại lệ (exception) cụ thể có được ném ra khi chương trình gặp lỗi hay không.
- **Source:** Phần Assertions (An assertRaises() to verify that a specific exception gets raised).
- **Tag:** [vv10]

- **Fact:** Giao diện dòng lệnh (CLI) của `unittest` cho phép thực thi kiểm thử linh hoạt theo module, theo lớp (class) hoặc theo từng phương thức đơn lẻ.
- **Source:** Phần Command-line interface (run tests from modules, classes, or even individual test methods).
- **Tag:** [vv10]

---

### 🚀 CHUYỂN TIẾP: TỪ UNITTEST SANG PYTEST

Sau khi đã nắm vững `unittest`, việc chuyển sang `pytest` là một bước tiến lớn giúp tối ưu hóa hiệu suất làm việc. Dưới đây là bảng so sánh ưu và nhược điểm:

#### 1. So sánh Unittest và Pytest

| Đặc điểm | **Unittest** (Standard Library) | **Pytest** (Third-party Framework) |
|:---|:---|:---|
| **Cài đặt** | Có sẵn trong Python (Built-in). | Cần cài đặt: `pip install pytest`. |
| **Cấu trúc code** | Bắt buộc dùng Class và kế thừa `TestCase`. | Có thể dùng Function đơn giản hoặc Class. |
| **Câu lệnh Assert** | Phải dùng `self.assertEqual()`, `self.assertTrue()`... | Chỉ cần dùng từ khóa `assert` cơ bản của Python. |
| **Boilerplate** | Nhiều mã thừa (phải tạo class, setup phức tạp). | Rất ít mã thừa, viết cực nhanh. |
| **Tính năng** | Cơ bản, đủ dùng cho các project nhỏ. | Rất mạnh với Fixtures, Parametrization (test nhiều bộ data). |
| **Báo cáo lỗi** | Thông tin cơ bản. | Rất chi tiết, hiển thị rõ giá trị biến khi lỗi. |

#### 2. Ưu và Nhược điểm

**Đối với Unittest:**
*   ✅ **Ưu điểm:** Không cần cài đặt thêm, phù hợp với các môi trường hạn chế cài thư viện ngoài, cấu trúc chặt chẽ theo hướng đối tượng.
*   ❌ **Nhược điểm:** Viết code dài dòng, khó đọc khi số lượng test lớn, cú pháp assert khó nhớ hơn.

**Đối với Pytest:**
*   ✅ **Ưu điểm:** Code cực kỳ ngắn gọn, dễ đọc. Cộng đồng hỗ trợ cực lớn với hàng ngàn plugin. Khả năng tự động tìm kiếm file test thông minh.
*   ❌ **Nhược điểm:** Là thư viện bên thứ ba (phải quản lý dependency). Đôi khi các tính năng "magic" (như Fixtures) có thể gây khó hiểu cho người mới bắt đầu.

---

### 🎯 BÀI TẬP THỰC HÀNH ĐẦU TIÊN VỚI PYTEST

Để bạn thấy sự khác biệt, hãy thử chuyển đổi bài test `ClothingFactory` từ `unittest` sang `pytest`.

**Bước 1: Cài đặt**
```bash
pip install pytest
```

**Bước 2: Viết code (File: `test_clothing_pytest.py`)**
*Lưu ý: Không cần import unittest, không cần tạo Class.*

```python
from clothing_factory import ClothingFactory

def test_create_clothing():
    cloth = ClothingFactory("shirt", "M")
    assert cloth.clothing_type == "shirt"
    assert cloth.size == "M"
    assert cloth.price == 22  # Chỉ dùng assert đơn giản!

def test_add_color():
    cloth = ClothingFactory("pants", "S")
    cloth.add_color("red")
    assert "red" in cloth.colors
    assert cloth.price == 26
```

**Bước 3: Chạy test**
Bạn chỉ cần gõ lệnh sau trong terminal:
```bash
pytest
```

👉 **Bạn có muốn tôi hướng dẫn sâu hơn về "Fixtures" trong Pytest - tính năng mạnh mẽ nhất giúp thay thế `setUp` và `tearDown` của Unittest không?** Hãy nhắn **"Hướng dẫn Pytest Fixtures"** nhé!