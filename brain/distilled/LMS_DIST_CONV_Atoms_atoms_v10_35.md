---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_35
  title: Tạo đối tượng robot1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn! Rất sẵn lòng. Để hiểu về **Class (Lớp)**, chúng ta sẽ đi từ ví dụ thực tế nhất. Hãy tưởng tượng bạn đang thiết kế một trò chơi và cần tạo ra các nhân vật (Robot).

Dưới đây là hướng dẫn từng bước để viết một Class trong Python:

---

### 1. Cấu trúc cơ bản của một Class

Một Class thường có 3 phần chính:
1. **Tên Class**: Viết hoa chữ cái đầu (ví dụ: `Robot`).
2. **Hàm khởi tạo (`__init__`)**: Nơi định nghĩa các đặc điểm (thuộc tính) ban đầu.
3. **Các phương thức (Methods)**: Các hành động mà đối tượng có thể làm.

### 2. Ví dụ thực tế: Class Robot

```python
class Robot:
    # 1. Hàm khởi tạo - Chạy ngay khi tạo Robot mới
    def __init__(self, name, color, battery_level):
        self.name = name            # Thuộc tính: Tên
        self.color = color          # Thuộc tính: Màu sắc
        self.battery = battery_level # Thuộc tính: Mức pin

    # 2. Phương thức - Hành động của Robot
    def introduce(self):
        print(f"Xin chào, tôi là {self.name}. Tôi có màu {self.color}.")

    def charge(self):
        self.battery = 100
        print(f"{self.name} đã được sạc đầy pin!")
```

---

### 3. Giải thích các thành phần quan trọng

- **`class Robot:`**: Khai báo đây là một lớp tên là Robot.
- **`def __init__(self, ...):`**: Đây là hàm đặc biệt. Khi bạn tạo một Robot mới, Python sẽ tự động gọi hàm này để "thiết lập" các thông số ban đầu.
- **`self` là gì?**: Đây là từ khóa quan trọng nhất. `self` đại diện cho **chính con Robot đó**. 
    - Ví dụ: Nếu bạn có Robot A và Robot B, `self` giúp Python biết đang sạc pin cho Robot A hay Robot B.
- **Thuộc tính (`self.name`, `self.color`)**: Là các biến nằm bên trong Class để lưu trữ thông tin.

---

### 4. Cách sử dụng (Tạo đối tượng)

Sau khi có "bản thiết kế" (Class), bạn có thể tạo ra hàng ngàn con Robot khác nhau:

```python
# Tạo đối tượng robot1
robot1 = Robot("R2D2", "Xanh dương", 50)

# Tạo đối tượng robot2
robot2 = Robot("Wall-E", "Vàng", 20)

# Gọi hành động
robot1.introduce() # Output: Xin chào, tôi là R2D2...
robot2.charge()    # Output: Wall-E đã được sạc đầy pin!
```

---

### 🎯 Tại sao Unit Test lại dùng Class?

Bây giờ bạn sẽ thấy mối liên hệ:
Khi bạn viết `class TestPalindrome(unittest.TestCase):`, bạn đang tạo ra một **bản thiết kế cho việc kiểm thử**. 
- `unittest.TestCase` là một Class có sẵn của Python chứa các "đồ nghề" như `assertEqual`.
- Khi bạn kế thừa nó, Class của bạn sẽ có tất cả sức mạnh của bộ đồ nghề đó để đi kiểm tra code.

---

### 🚀 Bài tập thực hành nhỏ cho bạn:

Hãy thử viết một Class tên là **`Rectangle`** (Hình chữ nhật) có:
1. Thuộc tính: `width` (chiều rộng) và `height` (chiều cao).
2. Phương thức: `area(self)` để tính và trả về diện tích (`width * height`).

Sau đó thử tạo một hình chữ nhật có kích thước 5x10 và in diện tích của nó ra nhé!

**Nếu bạn viết xong, hãy gửi code mình xem thử nhé! 🔥**

--------------------------------------------------
**TRÍCH XUẤT TRI THỨC (Scout Report):**

- Fact: [Class là bản thiết kế (blueprint) cho các đối tượng (objects), cho phép đóng gói dữ liệu (attributes) và hành vi (methods) vào một đơn vị duy nhất.]
- Source: [Module 5 - Python Classes Introduction]
- Tag: [vv10]

- Fact: [Phương thức __init__ là hàm khởi tạo đặc biệt, tự động thực thi khi một object được tạo ra để thiết lập các giá trị ban đầu.]
- Source: [Module 5 - Python Classes Structure]
- Tag: [vv10]

- Fact: [Tham số 'self' trong Python đại diện cho instance (thể hiện) hiện tại của class, cho phép truy cập vào các biến và phương thức thuộc về đối tượng đó.]
- Source: [Module 5 - Python Classes Self Keyword]
- Tag: [vv10]

- Fact: [Lập trình hướng đối tượng (OOP) giúp mã nguồn dễ tái sử dụng, quản lý và mở rộng hơn so với lập trình hướng thủ tục khi dự án trở nên phức tạp.]
- Source: [Module 5 - OOP Benefits]
- Tag: [Unverified_Source]