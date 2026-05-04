---
file_id: CONCEPT_PY_Matplotlib_Interfaces
title: Hai giao diện lập trình của Matplotlib
category: CONCEPT
domain: [[ENTITY_Python|Python]]
status: verified
---

# Matplotlib: Two Interfaces

Matplotlib cung cấp hai cách tiếp cận khác nhau để tạo biểu đồ, điều này thường gây nhầm lẫn cho người mới bắt đầu.

## 1. MATLAB-style (pyplot)
- **Cách dùng:** Sử dụng `plt.plot()`, `plt.title()`,...
- **Đặc điểm:** State-based (dựa trên trạng thái). Thư viện tự động theo dõi "Figure hiện tại" và "Axes hiện tại".
- **Ưu điểm:** Nhanh, tiện cho các biểu đồ đơn giản.

## 2. Object-Oriented Style (OO)
- **Cách dùng:** Khởi tạo đối tượng `fig, ax = plt.subplots()`, sau đó gọi phương thức trên đối tượng `ax.plot()`, `ax.set_title()`.
- **Đặc điểm:** Explicit (tường minh). Bạn kiểm soát chính xác biểu đồ nào đang được vẽ.
- **Ưu điểm:** Khuyên dùng cho các biểu đồ phức tạp hoặc khi có nhiều biểu đồ con (subplots).

## Lời khuyên
Nên sử dụng giao diện Object-Oriented để code tường minh và dễ bảo trì hơn trong các dự án dài hạn.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Vẽ hai biểu đồ sine và cosine độc lập bằng Giao diện Object-Oriented (OO).*
- **Cách giải quyết:** Các Data Scientist được khuyên dùng giao diện OO cho các biểu đồ có nhiều subplot để dễ quản lý. Ta khởi tạo rõ ràng `fig` (khung hình) và mảng `ax` (các trục), sau đó gọi phương thức `.plot()` trên từng đối tượng.
```python
x = np.linspace(0, 10, 100)

# Khởi tạo rõ ràng Figure và 2 Axes (2 hàng, 1 cột)
fig, ax = plt.subplots(2, 1) 

# Thao tác trực tiếp trên từng đối tượng Axes độc lập
ax[0].plot(x, np.sin(x))
ax[0].set_title('Sine Wave')

ax[1].plot(x, np.cos(x))
ax[1].set_title('Cosine Wave')
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Vẽ Dashboard Báo cáo Điểm thi Giữa kỳ và Cuối kỳ của lớp.*
- **Cách giải quyết:** Giáo viên muốn hiển thị 2 biểu đồ phân phối điểm cạnh nhau để phụ huynh dễ hình dung sự tiến bộ. Bằng giao diện OO của Matplotlib, giáo viên tạo ra khung hình 1 hàng 2 cột.
```python
# Tạo khung vẽ 1 hàng, 2 cột để so sánh
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Vẽ biểu đồ Giữa kỳ trên ax1
ax1.hist(diem_giua_ky, color='blue')
ax1.set_title('Phân phối điểm Giữa kỳ')

# Vẽ biểu đồ Cuối kỳ trên ax2
ax2.hist(diem_cuoi_ky, color='green')
ax2.set_title('Phân phối điểm Cuối kỳ')

plt.tight_layout()
plt.show()
```

---
 Nguồn: [[SOURCE_DS_Python_Data_Science_Handbook]] — Chapter 4
[AUDITOR] Rule 14: Đã xác nhận sự phân biệt giữa plt.interface và OO interface. Ví dụ cho thấy rõ đặc tính State-based vs Explicit Object.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
