Chào bạn, tôi là **@scout**. Dưới đây là các sự kiện kỹ thuật (Facts) quan trọng về **Class trong Python** được chưng cất để giúp bạn nắm vững cấu trúc này, phục vụ cho việc lập trình tự động hóa và Robotics.

- **Fact:** [CONV] [Class là một "bản thiết kế" (blueprint) dùng để tạo ra các đối tượng (objects), giúp đóng gói dữ liệu (attributes) và hành vi (methods) vào một thực thể duy nhất.]
- **Source:** [Module 5 - Object-Oriented Programming Basics]
- **Tag:** [vv10]

- **Fact:** [CONV] [Phương thức `__init__` (Constructor) được tự động gọi khi một đối tượng mới được tạo ra để khởi tạo các giá trị ban đầu cho thuộc tính của đối tượng đó.]
- **Source:** [Module 5 - Class Structure]
- **Tag:** [vv10]

- **Fact:** [CONV] [Từ khóa `self` là tham số bắt buộc đầu tiên trong các phương thức của class, dùng để tham chiếu đến chính thực thể (instance) hiện tại của class đó để truy cập dữ liệu nội bộ.]
- **Source:** [Module 5 - Class Methods]
- **Tag:** [vv10]

- **Fact:** [CONV] [Kế thừa (Inheritance) cho phép một class mới (class con) tiếp nhận toàn bộ đặc tính từ một class đã có (class cha), giúp tái sử dụng code và mở rộng tính năng mà không cần viết lại.]
- **Source:** [Module 5 - Inheritance]
- **Tag:** [vv10]

- **Fact:** [CONV] [Trong Unit Testing, việc sử dụng Class (kế thừa từ `unittest.TestCase`) giúp tổ chức các bài kiểm tra thành các nhóm logic, dễ quản lý và chạy tự động.]
- **Source:** [Module 5 - Unit Test Structure]
- **Tag:** [vv10]

--------------------------------------------------

### 🚀 HƯỚNG DẪN VIẾT CLASS CƠ BẢN (VÍ DỤ ROBOTICS)

Để bạn dễ hình dung, hãy thử viết một Class quản lý một con Robot đơn giản:

```python
# 1. Định nghĩa Class (Bản thiết kế)
class Robot:
    # 2. Hàm khởi tạo (Xác định các đặc điểm ban đầu)
    def __init__(self, name, version):
        self.name = name          # Thuộc tính: Tên robot
        self.version = version    # Thuộc tính: Phiên bản
        self.battery = 100        # Thuộc tính mặc định: Pin 100%

    # 3. Phương thức (Hành động của Robot)
    def say_hello(self):
        print(f"Xin chào! Tôi là {self.name}, phiên bản {self.version}.")

    def move(self, distance):
        if self.battery > 10:
            print(f"{self.name} đang di chuyển {distance} mét...")
            self.battery -= 10
        else:
            print("Cảnh báo: Pin yếu, không thể di chuyển!")

# 4. Tạo đối tượng (Object) từ Class
my_robot = Robot("YoloBit_Bot", "v1.0")

# 5. Sử dụng đối tượng
my_robot.say_hello()  # Gọi hành động
my_robot.move(5)      # Gọi hành động di chuyển
print(f"Pin hiện tại: {my_robot.battery}%") # Kiểm tra thuộc tính
```

### 💡 Giải thích nhanh cho bạn:
1.  **`class Robot:`**: Khai báo tên lớp (luôn viết hoa chữ cái đầu).
2.  **`def __init__(self, ...):`**: Giống như việc bạn lắp ráp robot, bạn cần đặt tên và cài phiên bản cho nó ngay từ đầu.
3.  **`self`**: Hãy tưởng tượng `self` giống như từ "của tôi". `self.name` nghĩa là "tên của tôi". Nó giúp các hàm bên trong class nhận biết chúng đang làm việc với dữ liệu của chính nó.
4.  **`my_robot = Robot(...)`**: Đây là lúc bạn tạo ra một con robot thật sự từ bản thiết kế trên giấy.

Bạn có muốn tôi hướng dẫn cách áp dụng Class này vào việc **viết Unit Test** để kiểm tra xem Robot có hoạt động đúng như mong đợi không? 🤖🔥