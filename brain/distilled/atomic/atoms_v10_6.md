Chào bạn, tôi là **@scout**. Tôi đã thực hiện chưng cất tri thức từ dữ liệu bạn cung cấp (Volume v10) về các kỹ thuật lập trình và kiểm thử (nền tảng quan trọng cho AI và Robotics). 

Dưới đây là các sự kiện kỹ thuật được trích xuất:

- **Fact:** Unit testing giúp phát hiện lỗi sớm trong quá trình phát triển phần mềm trước khi chúng trở thành các vấn đề lớn và tốn kém hơn để khắc phục.
- **Source:** Đoạn 1 (Paragraph 1)
- **Tag:** [vv10]

- **Fact:** Trong Python, `unittest` là một framework kiểm thử đơn vị (unit testing framework) mà các lập trình viên sử dụng để kiểm tra mã nguồn.
- **Source:** Đoạn 2 (Paragraph 2)
- **Tag:** [vv10]

- **Fact:** Các khối xây dựng (building blocks) của unit tests trong module `unittest` là các "test cases", được tạo ra bằng cách viết các lớp con (subclasses) của `TestCase`.
- **Source:** Section: Test cases
- **Tag:** [vv10]

- **Fact:** Để trình chạy thử nghiệm (test runner) nhận diện được, các phương thức kiểm thử trong lớp `TestCase` phải bắt đầu bằng tiền tố `test`.
- **Source:** Section: Test cases
- **Tag:** [vv10]

- **Fact:** Các phương thức assertion phổ biến bao gồm `assertEqual()` (kiểm tra bằng nhau), `assertTrue()`/`assertFalse()` (xác minh điều kiện), và `assertRaises()` (xác minh ngoại lệ).
- **Source:** Section: Assertions
- **Tag:** [vv10]

- **Fact:** Giao diện dòng lệnh (CLI) của `unittest` cho phép chạy thử nghiệm từ các module, class hoặc thậm chí là các phương thức kiểm thử cá nhân.
- **Source:** Section: Command-line interface
- **Tag:** [vv10]

- **Fact:** Mô hình thiết kế Unit test phổ biến gồm ba giai đoạn: Arrange (chuẩn bị môi trường), Act (thực hiện hành động mục tiêu), và Assert (kiểm tra kết quả).
- **Source:** Section: Unit test design patterns
- **Tag:** [vv10]

- **Fact:** Phương thức `setUp()` được gọi tự động trước mỗi bài test để thiết lập mã, trong khi `tearDown()` giúp dọn dẹp sau khi bài test đã chạy xong.
- **Source:** Section: Test suites
- **Tag:** [vv10]

- **Fact:** `setUpModule()` và `tearDownModule()` được sử dụng để thực hiện các thiết lập và dọn dẹp một lần duy nhất cho toàn bộ module (ví dụ: tạo/xóa file log toàn cục).
- **Source:** [Unverified_Source] (Dựa trên logic code mẫu và phần giải thích "module teardown" trong văn bản).
- **Tag:** [vv10]

--------------------------------------------------

### 💡 Giải đáp về lỗi "Không thấy file original" trong code của bạn:

Lý do bạn không bao giờ thấy file `original_test_file.txt` xuất hiện trong thư mục là do dòng lệnh cuối cùng trong hàm `tearDownModule`:

```python
def tearDownModule():
    # ... (copy file)
    os.remove(ORIGINAL_FILE_PATH)  # <--- ĐÂY LÀ NGUYÊN NHÂN
```

**Giải thích:**
1. Khi bạn chạy chương trình, `setUpModule` tạo ra file `original`.
2. Các bài test chạy và ghi nội dung vào file đó.
3. Khi tất cả test xong, `tearDownModule` được gọi. Nó thực hiện copy file sang vị trí mới (`COPIED_FILE_PATH`) và **ngay lập tức xóa file gốc** bằng lệnh `os.remove`.
4. Vì máy tính xử lý cực nhanh, bạn sẽ không kịp thấy file gốc xuất hiện rồi biến mất.

**Cách khắc phục để bạn có thể nhìn thấy file:**
Hãy comment dòng xóa file lại để kiểm tra:
```python
def tearDownModule():
    shutil.copy2(ORIGINAL_FILE_PATH, COPIED_FILE_PATH)
    # os.remove(ORIGINAL_FILE_PATH)  # Tạm thời tắt lệnh này để xem file
```

Khi đó, sau khi chạy xong, bạn sẽ thấy cả 2 file trong thư mục `test_output`.