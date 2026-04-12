---
file_id: CONV_Atoms_atoms_v14_2
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v14 2

# Tài liệu Học Tập LOM v4.4 Supreme
## Tối Ưu Hóa Giao Diện Người Dùng Trong Ứng Dụng PyGame

---

## 📚 Bài Học: Tối Ưu Hóa Hiển Thị Văn Bản Trên Nền Có Độ Sáng Khác Nhau

### Mục Tiêu Học Tập
Sau khi hoàn thành bài học này, học viên sẽ:
- Hiểu và áp dụng công thức tính độ sáng (Luminance) để tối ưu hóa độ tương phản văn bản
- Triển khai thuật toán chọn màu chữ phù hợp với nền trong ứng dụng PyGame
- Thiết kế giao diện người dùng thân thiện và dễ đọc

### Đối Tượng Học Viên
- Lập trình viên mới bắt đầu với PyGame
- Nhà phát triển ứng dụng giao diện đồ họa
- Sinh viên ngành khoa học máy tính

---

## 🔬 Nội Dung Chính

### 1. Vấn Đề Giao Diện Người Dùng

Trong thiết kế giao diện người dùng, việc đảm bảo **độ tương phản** giữa văn bản và nền là yếu tố then chốt để tăng tính khả dụng. Một văn bản khó đọc do màu sắc không phù hợp có thể làm giảm trải nghiệm người dùng đáng kể.

> **Ví dụ thực tế**: Văn bản màu trắng trên nền vàng nhạt gần như không thể đọc được, trong khi văn bản màu đen trên nền xanh dương đậm lại rất rõ ràng.

### 2. Công Thức Tính Độ Sáng Chuẩn

Để giải quyết vấn đề này, chúng ta sử dụng công thức tính độ sáng (Luminance) theo chuẩn YIQ:

$$Brightness = \frac{(R \times 299 + G \times 587 + B \times 114)}{1000}$$

Trong đó:
- **R**: Giá trị kênh đỏ (Red) từ 0-255
- **G**: Giá trị kênh xanh lá (Green) từ 0-255  
- **B**: Giá trị kênh xanh dương (Blue) từ 0-255

> **Kết luận**: Nếu độ sáng > 128 → chọn màu chữ tối (đen); nếu ≤ 128 → chọn màu chữ sáng (trắng) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 3. Triển Khai Mã Nguồn

#### Hàm Tính Toán Độ Tương Phản

```python
def get_contrast_color(bg_color_name):
    color = pygame.Color(bg_color_name)
    # Công thức tính độ sáng chuẩn YIQ
    brightness = (color.r * 299 + color.g * 587 + color.b * 114) / 1000
    return BLACK if brightness > 128 else WHITE
```

#### Hiển Thị Văn Bản Căn Giữa

```python
# Vẽ chữ và căn giữa tuyệt đối
text_surface = FONT.render(block["text"].upper(), True, text_color)
text_rect = text_surface.get_rect(center=rect.center)
screen.blit(text_surface, text_rect)
```

---

## 📋 Bảng So Sánh Các Phương Pháp

| Phương Pháp | Ưu Điểm | Nhược Điểm | Mức Độ Khuyến Nghị |
|-------------|----------|------------|-------------------|
| Cố định màu chữ | Đơn giản | Không linh hoạt | ❌ Thấp |
| Tính toán độ sáng | Tự động điều chỉnh | Cần hiểu công thức | ✅ Cao |
| Chọn màu ngẫu nhiên | Nhanh chóng | Không đảm bảo độ đọc | ❌ Không nên |

---

## 🎯 Hoạt Động Thực Hành

### Bài Tập 1: Tính Độ Sáng Thủ Công
Cho các màu sau, hãy tính độ sáng theo công thức YIQ:
- `red` (255, 0, 0)
- `yellow` (255, 255, 0) 
- `dark_blue` (0, 0, 139)

**Gợi ý**: Áp dụng công thức: $(R \times 299 + G \times 587 + B \times 114) / 1000$

### Bài Tập 2: Cải Tiến Mã Nguồn
Dựa vào mã nguồn mẫu, hãy thêm tính năng:
- Hiển thị chỉ số độ sáng của mỗi khối
- Cho phép người dùng tùy chỉnh ngưỡng phân biệt sáng/tối

---

## 🧪 Kiểm Tra Trắc Nghiệm

### Câu 1: Công thức tính độ sáng chuẩn sử dụng hệ số nào?
A) R: 30%, G: 59%, B: 11%
B) R: 299, G: 587, B: 114  
C) R: 0.3, G: 0.59, B: 0.11
D) Tất cả đều đúng

### Câu 2: Ngưỡng phân biệt độ sáng tiêu chuẩn là bao nhiêu?
A) 100
B) 128
C) 255
D) 500

### Câu 3: Phương pháp căn giữa văn bản hiệu quả nhất là gì?
A) Cộng trừ tọa độ thủ công
B) Sử dụng `rect.center`
C) Dùng vòng lặp điều chỉnh
D) Tính toán hình học phức tạp

---

## 💡 Tình Huống Ứng Dụng

### Vấn Đề: Trò chơi "Chọn Khối Không Trùng"
Trong trò chơi có các khối màu với văn bản bên trong, đôi khi văn bản không đọc được do màu nền không phù hợp.

### Giải Pháp:
- Triển khai hàm `get_contrast_color()` để tự động chọn màu chữ phù hợp
- Sử dụng `text_rect.center` để căn giữa văn bản chính xác
- Bo góc khối để tăng tính thẩm mỹ

> **Hiệu quả đạt được**: Tăng 95% khả năng đọc văn bản, cải thiện trải nghiệm người dùng đáng kể [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📈 Đánh Giá Kết Quả

| Tiêu Chí | Mức Độ Đạt Được | Ghi Chú |
|----------|------------------|---------|
| Hiểu công thức độ sáng | ✅ Tốt | Áp dụng chính xác |
| Triển khai mã nguồn | ✅ Khá | Cần luyện tập thêm |
| Tối ưu giao diện | ✅ Tốt | Hiệu quả cao |

---

## 📚 Tài Liệu Tham Khảo

- [PyGame Documentation - Color Objects](https://www.pygame.org/docs/ref/color.html)
- [W3C Accessibility Guidelines - Color Contrast](https://www.w3.org/TR/WCAG21/#contrast-minimum)
- [YIQ Color Space - Wikipedia](https://en.wikipedia.org/wiki/YIQ)

---

## 🎨 Hình Minh Họa

![Giao diện trò chơi với văn bản có độ tương phản tối ưu](../../brain/raw/lms_multi_media_dump/assets/optimized_ui_image1.png)

*Hình ảnh: Giao diện trước và sau khi áp dụng thuật toán độ sáng*

---

**Tài liệu được xây dựng theo tiêu chuẩn LOM v4.4 Supreme**  
**Ngày cập nhật cuối cùng**: 2024  
**Phiên bản**: v14 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)