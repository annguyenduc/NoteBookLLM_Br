---
file_id: "WIKI_Python_Data_Types"
title: "Python — Các kiểu dữ liệu cơ bản"
category: "Atomic Note"
prefix: "WIKI"
tags: ["Python", "K10", "Variables", "DataTypes"]
source: "brain/raw/KHMT_Python_K10_Raw_Master.md"
status: "verified"
created: "2026-04-23"
last_updated: "2026-04-23"
---

# Python — Các kiểu dữ liệu cơ bản

## 📌 Định nghĩa cốt lõi
Trong Python, kiểu dữ liệu (Data Type) xác định loại giá trị mà một biến có thể lưu trữ và các phép toán có thể thực hiện trên đó. Python là ngôn ngữ có kiểu dữ liệu động (dynamic typing), nghĩa là bạn không cần khai báo kiểu dữ liệu trước.

## 🔍 Chi tiết kỹ thuật
- **Fact 1: Kiểu số nguyên (Integer - `int`)**: Dùng cho các số không có phần thập phân. Ví dụ: `x = 10`, `y = -5`.
- **Fact 2: Kiểu số thực (Floating point - `float`)**: Dùng cho các số có phần thập phân. Ví dụ: `pi = 3.14`, `price = 99.9`.
- **Fact 3: Kiểu chuỗi (String - `str`)**: Dùng cho văn bản, đặt trong dấu ngoặc đơn `' '` hoặc ngoặc kép `" "`. Ví dụ: `name = "Antigravity"`.
- **Fact 4: Kiểu Boolean (`bool`)**: Chỉ có hai giá trị: `True` hoặc `False`.
- **Fact 5: Hàm `type()`**: Dùng để kiểm tra kiểu dữ liệu của một đối tượng. Ví dụ: `type(10)` trả về `<class 'int'>`.

## 💡 Ví dụ thực tế
Chương trình tính tổng hai số nhập từ bàn phím. Lưu ý: Dữ liệu từ `input()` luôn là kiểu `str`, nên cần ép kiểu (type casting) sang `int` hoặc `float` trước khi tính toán.
```python
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Tổng là:", a + b)
```

## 🔗 Liên kết tư duy
- [[WIKI_Python_K10_System]]
- [[WIKI_Python_Control_Structures]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Python hỗ trợ 4 kiểu dữ liệu cơ bản: int, float, str, bool. Ép kiểu là bắt buộc khi xử lý input từ người dùng. |
| **Feelings** | Học sinh hay quên ép kiểu `int()` hoặc `float()` khi dùng `input()`, dẫn đến lỗi logic (ví dụ "1" + "2" = "12"). |
| **Findings** | Hiểu rõ sự khác biệt giữa kiểu dữ liệu giúp tránh được các lỗi `TypeError` và tối ưu hóa việc lưu trữ dữ liệu. |
| **Futures** | Là kiến thức nền tảng để làm việc với các cấu trúc dữ liệu phức tạp hơn như List, Tuple, Dictionary và Set. |

## 📖 Nguồn
`📖 Nguồn: brain/raw/KHMT_Python_K10_Raw_Master.md`

---
<!-- WIKI CHECKLIST — @librarian verify trước khi đổi status: verified -->
- [x] Chỉ có 1 khái niệm duy nhất
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Facts là copy nguyên văn hoặc tóm lược kỹ thuật chính xác
- [x] Futures không để trống
