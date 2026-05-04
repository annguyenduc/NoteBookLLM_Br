---
file_id: CONCEPT_PY_Matplotlib_OO_vs_Pyplot
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
tags: ["Matplotlib", "Coding_Style", "Python"]
source: "[[SOURCE_PY_Matplotlib_QuickStart]]"
created: "2026-05-03"
---

# Concept: OO Style vs Pyplot Style

## 1. Core Principle (Bản chất cốt lõi)
Matplotlib cung cấp hai giao diện lập trình:
- **OO Style (Explicit)**: Khởi tạo Figure/Axes rõ ràng và gọi phương thức trực tiếp (`ax.plot()`). Phù hợp cho code sản xuất và tùy biến sâu.
- **Pyplot Style (Implicit)**: Sử dụng hàm toàn cục (`plt.plot()`) để tự động quản lý Figure hiện tại. Phù hợp cho thăm dò nhanh (EDA).

## 2. Ví dụ đối chiếu (Rule 17 - Double Examples)

### Ví dụ 1: Trích dẫn tài liệu (Original Context)
```python
# OO Style
fig, ax = plt.subplots()
ax.plot(x, y)

# Pyplot Style
plt.plot(x, y)
```
**Nguồn**: `WEBSITE_PY_Matplotlib_QuickStart` — Section "Coding Styles"

### Ví dụ 2: Ẩn dụ sư phạm (Pedagogical Application)
- **OO Style**: Giống như bạn tự tay cầm từng chiếc đĩa, xếp vào vị trí mình muốn trên bàn tiệc.
- **Pyplot Style**: Giống như bạn gọi "Phục vụ ơi, lên món!", và người phục vụ tự đặt đĩa vào chỗ trống gần nhất.

## 3. 4F Reflection
- **Facts**: OO Style thường dùng `ax.set_xlabel()`, còn Pyplot dùng `plt.xlabel()`.
- **Feelings**: Người mới thường thích Pyplot vì ngắn gọn, nhưng sẽ thấy bế tắc khi muốn vẽ nhiều biểu đồ phức tạp.
- **Findings**: Luôn khuyến khích dùng OO Style (`fig, ax = plt.subplots()`) ngay từ đầu để tránh nợ kỹ thuật.
- **Futures**: Tích hợp chuẩn này vào các script tự động báo cáo.

---
Nguồn: [[SOURCE_PY_Matplotlib_QuickStart]]
[[CONCEPT_PY_Matplotlib_Basics]]


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
