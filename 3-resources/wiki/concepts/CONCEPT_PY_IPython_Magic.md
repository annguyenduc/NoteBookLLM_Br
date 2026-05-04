---
file_id: CONCEPT_PY_IPython_Magic
title: Các lệnh Magic (Magic Commands) trong IPython
category: CONCEPT
domain: [[ENTITY_Python|Python]]
status: verified
---

# IPython Magic Commands

Magic Commands là các lệnh đặc biệt bắt đầu bằng ký tự `%` (line magics) hoặc `%%` (cell magics), được thiết kế để giải quyết các vấn đề phổ biến trong phân tích dữ liệu tương tác.

## ️ Các lệnh thiết yếu
1.  **Kiểm tra hiệu năng:**
    - `%timeit`: Đo thời gian thực thi của một dòng code (chạy nhiều lần để lấy trung bình).
    - `%%time`: Đo thời gian thực thi của toàn bộ cell.
2.  **Quản lý code:**
    - `%run`: Chạy một file `.py` bên trong phiên làm việc IPython.
    - `%load`: Nạp nội dung file vào cell.
3.  **Hệ thống & Gỡ lỗi:**
    - `%debug`: Kích hoạt trình gỡ lỗi tương tác sau khi gặp lỗi.
    - `%ls`, `%pwd`, `%cd`: Tương tác trực tiếp với hệ điều hành.

## Lợi ích
Giúp rút ngắn quy trình "Viết code -> Thử nghiệm -> Đo lường", biến IPython thành một "bảng điều khiển" (control panel) thực sự cho dữ liệu.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Cần so sánh tốc độ tạo List bằng List Comprehension vs Vòng lặp for thông thường.*
- **Cách giải quyết:** Các Data Scientist sử dụng `%timeit` để đo thời gian thực thi của một dòng code trong IPython/Jupyter. Hàm này sẽ tự động chạy lệnh lặp lại nhiều vòng để lấy thời gian trung bình.
```python
# Đo thời gian tạo list bình thường
%timeit l1 = [i**2 for i in range(1000)]

# Kết quả mẫu: 250 µs ± 5.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Chấm điểm bài làm Python của học sinh bằng script nạp tự động vào Jupyter Notebook.*
- **Cách giải quyết:** Trong buổi dạy thực hành, giáo viên viết sẵn một script `cham_diem_tu_dong.py` để chấm bài học sinh. Thay vì copy code dán vào Notebook, giáo viên gọi `%run`. Tất cả biến và hàm chấm điểm sẽ được nạp ngay vào bộ nhớ.
```python
# Chạy file chấm điểm. Tất cả biến và hàm sẽ được nạp vào memory hiện tại
%run scripts/cham_diem_tu_dong.py

# Ngay lập tức, gọi hàm chấm điểm vừa được nạp để check bài tập
check_bai_tap_1(dap_an_cua_hs)
```

---
 Nguồn: [[SOURCE_DS_Python_Data_Science_Handbook]] — Chapter 1
[AUDITOR] Rule 14: Đã xác nhận các lệnh %timeit, %run, %debug. Các ví dụ minh họa cách tối ưu Workflow phân tích dữ liệu tương tác.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
