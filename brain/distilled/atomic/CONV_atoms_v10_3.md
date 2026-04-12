Đây là một tình huống rất thực tế khi xử lý dữ liệu hàng loạt (ví dụ: một danh sách đơn hàng). Để làm được việc này, bạn cần kết hợp **Dictionary Mapping** với **Vòng lặp (Loop)** và câu lệnh **`continue`**.

Dưới đây là các sự kiện kỹ thuật và hướng dẫn chi tiết:

- Fact: [CONV] Câu lệnh `continue` được sử dụng trong vòng lặp để bỏ qua các dòng code phía dưới nó và nhảy ngay sang lần lặp (iteration) tiếp theo.
- Source: [vv10 - Section: Control Flow]
- Tag: [vv10]

- Fact: [CONV] Có hai cách phổ biến để kiểm tra và bỏ qua một key không tồn tại: Sử dụng toán tử `in` để kiểm tra trước hoặc sử dụng `.get()` và kiểm tra kết quả `None`.
- Source: [vv10 - Section: Dictionary Mapping]
- Tag: [vv10]

---

### 🛠️ Giải pháp 1: Dùng toán tử `in` (Cách này rõ ràng nhất)

Cách này kiểm tra xem loại bánh có nằm trong "thực đơn" (dict) hay không trước khi xử lý.

```python
base_prices = {"chocolate": 10, "vanilla": 8}
orders = ["chocolate", "strawberry", "vanilla"] # Strawberry không có trong dict

for cake_type in orders:
    # 1. Kiểm tra xem có trong dict không
    if cake_type not in base_prices:
        print(f"❌ Loại bánh '{cake_type}' này không có! (Bỏ qua...)")
        continue  # Nhảy sang lần lặp tiếp theo ngay lập tức
    
    # 2. Nếu có thì mới xử lý tiếp
    price = base_prices[cake_type]
    print(f"✅ Đang làm bánh {cake_type} với giá {price}$")
```

---

### 🛠️ Giải pháp 2: Dùng `.get()` kết hợp kiểm tra `None`

Cách này tận dụng đặc tính của `.get()` là trả về `None` nếu không tìm thấy key.

```python
base_prices = {"chocolate": 10, "vanilla": 8}
orders = ["chocolate", "strawberry", "vanilla"]

for cake_type in orders:
    price = base_prices.get(cake_type) # Trả về None nếu không thấy
    
    if price is None:
        print(f"❌ Không tìm thấy loại '{cake_type}' trong hệ thống!")
        continue
        
    print(f"✅ Xử lý bánh {cake_type}: {price}$")
```

---

### 🧠 So sánh và lời khuyên:

| Đặc điểm | Dùng `in` | Dùng `.get() is None` |
|:---|:---|:---|
| **Độ rõ ràng** | Rất cao (Đọc vào hiểu ngay là đang check tồn tại). | Trung bình (Phải hiểu cơ chế trả về None). |
| **Hiệu năng** | Tốt. | Tốt (Thường dùng khi bạn vừa muốn check vừa muốn lấy giá trị luôn). |
| **Ứng dụng** | Dùng khi bạn chỉ muốn kiểm tra sự hiện diện. | Dùng khi bạn muốn lấy dữ liệu và xử lý lỗi thiếu dữ liệu cùng lúc. |

---

### 🚀 Bạn có muốn nâng cấp thêm:
- Mình hướng dẫn cách **ghi lại danh sách các loại bánh bị lỗi** (Error Log) sau khi chạy xong vòng lặp không?
- Hay bạn muốn thử sức với một bài tập **xử lý danh sách đơn hàng phức tạp** có cả loại bánh và size không?

👉 Nếu muốn, hãy nhắn: "**Ghi log lỗi**" hoặc "**Bài tập đơn hàng tổng hợp**" nhé! 🔥