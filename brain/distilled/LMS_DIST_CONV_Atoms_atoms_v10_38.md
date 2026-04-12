---
file_id: CONV_Atoms_atoms_v10_38
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v10 38

# Tài Liệu Học Tập: Framework Kiểm Thử Đơn Vị trong Python

## Thông Tin Tài Liệu
| Thuộc Tính | Giá Trị |
|------------|---------|
| **Tiêu Đề** | Framework Kiểm Thử Đơn Vị trong Python: unittest và pytest |
| **Mã ID** | LOM-v4.4-Supreme-UT001 |
| **Ngôn Ngữ** | Vietnamese |
| **Loại Nội Dung** | Technical Training Material |
| **Trình Độ** | Intermediate Developer |

---

## Mục Tiêu Học Tập

Sau khi hoàn thành nội dung này, học viên sẽ có khả năng:

- Hiểu rõ nguyên lý và mục đích của kiểm thử đơn vị (unit testing)
- Sử dụng thành thạo framework `unittest` trong Python
- So sánh và đánh giá giữa `unittest` và `pytest`
- Chuyển đổi từ `unittest` sang `pytest` hiệu quả
- Viết test cases chuyên nghiệp với cả hai framework

---

## Nội Dung Chính

### 1. Giới Thiệu Về Kiểm Thử Đơn Vị

> **Định Nghĩa**: Unit tests được thiết kế để kiểm tra các phần nhỏ của mã nguồn như một hàm hoặc phương thức đơn lẻ nhằm đảm bảo chúng hoạt động đúng kỳ vọng [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

Kiểm thử đơn vị là nền tảng cơ bản trong quá trình phát triển phần mềm chất lượng cao. Nó giúp:
- Phát hiện lỗi sớm trong quá trình phát triển
- Đảm bảo tính chính xác của từng thành phần nhỏ
- Hỗ trợ quá trình tái cấu trúc an toàn

---

### 2. Framework unittest trong Python

#### 2.1. Bản Chất Hướng Đối Tượng

> **Sự Kiện Kỹ Thuật**: `unittest` là một framework kiểm thử đơn vị theo hướng đối tượng (object-oriented) trong Python [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### 2.2. Cấu Trúc Cơ Bản

```python
import unittest

class TestClassName(unittest.TestCase):
    def test_method_name(self):
        # Nội dung kiểm thử
        pass
```

#### 2.3. Quy Tắc Viết Test Case

> **Sự Kiện Kỹ Thuật**: Một phương thức kiểm thử chỉ được trình chạy test (test runner) nhận diện nếu tên phương thức đó bắt đầu bằng tiền tố `test` [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### 2.4. Các Phương Thức Assert

> **Sự Kiện Kỹ Thuật**: `unittest` sử dụng các phương thức assert riêng (như `assertEqual`, `assertTrue`, `assertFalse`) thay vì câu lệnh `assert` tiêu chuẩn để thu thập kết quả và tạo báo cáo [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

| Phương Thức | Mục Đích |
|-------------|----------|
| `assertEqual(a, b)` | Kiểm tra a == b |
| `assertTrue(x)` | Kiểm tra x là True |
| `assertFalse(x)` | Kiểm tra x là False |
| `assertRaises(exc, func, *args, **kwargs)` | Kiểm tra ngoại lệ được ném ra |

> **Sự Kiện Kỹ Thuật**: Phương thức `assertRaises()` được sử dụng để xác minh xem một ngoại lệ (exception) cụ thể có được ném ra khi chương trình gặp lỗi hay không [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

### 3. So Sánh unittest vs pytest

| Đặc Điểm | **Unittest** (Thư Viện Chuẩn) | **Pytest** (Framework Bên Thứ Ba) |
|----------|-------------------------------|-----------------------------------|
| **Cài Đặt** | Có sẵn trong Python (Built-in) | Cần cài đặt: `pip install pytest` |
| **Cấu Trúc Code** | Bắt buộc dùng Class và kế thừa `TestCase` | Có thể dùng Function đơn giản hoặc Class |
| **Câu Lệnh Assert** | Phải dùng `self.assertEqual()`, `self.assertTrue()`... | Chỉ cần dùng từ khóa `assert` cơ bản của Python |
| **Mã Thừa (Boilerplate)** | Nhiều mã thừa (phải tạo class, setup phức tạp) | Rất ít mã thừa, viết cực nhanh |
| **Tính Năng** | Cơ bản, đủ dùng cho các project nhỏ | Rất mạnh với Fixtures, Parametrization |
| **Báo Cáo Lỗi** | Thông tin cơ bản | Rất chi tiết, hiển thị rõ giá trị biến khi lỗi |

#### Ưu và Nhược Điểm

**Unittest:**
- ✅ **Ưu điểm**: Không cần cài đặt thêm, phù hợp với môi trường hạn chế thư viện ngoài, cấu trúc chặt chẽ theo hướng đối tượng
- ❌ **Nhược điểm**: Viết code dài dòng, khó đọc khi số lượng test lớn, cú pháp assert khó nhớ hơn

**Pytest:**
- ✅ **Ưu điểm**: Code cực kỳ ngắn gọn, dễ đọc. Cộng đồng hỗ trợ cực lớn với hàng ngàn plugin. Khả năng tự động tìm kiếm file test thông minh
- ❌ **Nhược điểm**: Là thư viện bên thứ ba (phải quản lý dependency). Đôi khi các tính năng "magic" có thể gây khó hiểu cho người mới bắt đầu

---

### 4. Bài Tập Thực Hành

#### 4.1. Chuyển Đổi từ unittest sang pytest

> **Sự Kiện Kỹ Thuật**: Giao diện dòng lệnh (CLI) của `unittest` cho phép thực thi kiểm thử linh hoạt theo module, theo lớp (class) hoặc theo từng phương thức đơn lẻ [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

##### Bước 1: Cài Đặt Pytest
```bash
pip install pytest
```

##### Bước 2: Viết Code với Pytest
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

##### Bước 3: Chạy Test
```bash
pytest
```

---

## Worksheet: Thực Hành unittest và pytest

### Bài 1: Viết Test Case với unittest

**Yêu cầu**: Viết một lớp test sử dụng `unittest` để kiểm tra hàm tính tổng hai số.

```python
# TODO: Viết code tại đây
```

### Bài 2: Chuyển Đổi sang pytest

**Yêu cầu**: Chuyển đổi test case ở Bài 1 sang sử dụng `pytest`.

```python
# TODO: Viết code tại đây
```

### Bài 3: So Sánh Hiệu Quả

**Câu hỏi**: So sánh số lượng dòng code và mức độ dễ đọc giữa hai cách tiếp cận trên.

---

## Quiz: Kiến Thức Kiểm Thử Đơn Vị

### Câu 1: Phương thức test trong unittest phải bắt đầu bằng tiền tố gì?
A. `check_`
B. `test_`
C. `verify_`
D. `validate_`

### Câu 2: Framework nào sau đây là built-in trong Python?
A. pytest
B. nose
C. unittest
D. behave

### Câu 3: Trong pytest, bạn sử dụng lệnh nào để kiểm tra điều kiện?
A. `self.assertEqual()`
B. `assert`
C. `pytest.assert()`
D. `check()`

### Câu 4: Ưu điểm chính của pytest so với unittest là gì?
A. Không cần cài đặt
B. Cú pháp đơn giản hơn
C. Hỗ trợ GUI tốt hơn
D. Tốc độ chạy nhanh hơn

### Câu 5: Phương thức nào dùng để kiểm tra ngoại lệ trong unittest?
A. `assertException()`
B. `assertError()`
C. `assertRaises()`
D. `assertThrow()`

---

## Scenario: Dự Án Thực Tế

### Tình Huống
Bạn là lập trình viên tại công ty ABC, đang phát triển một hệ thống thương mại điện tử. Bộ phận QA yêu cầu bạn viết test case cho module xử lý giỏ hàng.

### Yêu Cầu
1. Viết test case cho chức năng thêm sản phẩm vào giỏ hàng
2. So sánh giữa unittest và pytest để chọn giải pháp phù hợp
3. Trình bày lý do lựa chọn

### Mô Hình Giỏ Hàng
```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def get_total_items(self):
        return len(self.items)
```

### Nhiệm Vụ
Viết test case cho các tình huống:
- Thêm sản phẩm mới vào giỏ hàng
- Thêm sản phẩm trùng lặp
- Xóa sản phẩm khỏi giỏ hàng
- Đếm tổng số sản phẩm

---

## Tài Nguyên Tham Khảo

- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Pytest Official Documentation](https://docs.pytest.org/)
- Best Practices for Unit Testing in Python
- Test-Driven Development (TDD) Principles

---

## Đánh Giá Kết Quả Học Tập

| Mức Độ | Tiêu Chí |
|--------|----------|
| **Basic** | Hiểu được mục đích của unit testing |
| **Intermediate** | Viết được test case với unittest |
| **Advanced** | Chuyển đổi thành thạo giữa unittest và pytest |
| **Expert** | Áp dụng best practices trong dự án thực tế |

---

> **Lưu ý**: Tất cả nội dung trong tài liệu này đều tuân thủ chuẩn LOM v4.4 Supreme và được cập nhật theo quy trình chưng cất tri thức chuyên nghiệp [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).