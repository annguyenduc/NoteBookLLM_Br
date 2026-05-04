---
file_id: CONCEPT_PY_Matplotlib_Basics
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
tags: ["Matplotlib", "Visualization", "Python"]
source: "[[SOURCE_PY_Matplotlib_QuickStart]]"
created: "2026-05-03"
---

# Concept: Matplotlib Basics (Figure & Axes)

## 1. Core Principle (Bản chất cốt lõi)
Matplotlib vận hành theo mô hình phân tầng (Hierarchical Model). Mọi biểu đồ đều là một **Figure** (khung tranh), bên trong chứa một hoặc nhiều **Axes** (vùng tọa độ). Các thành phần nhỏ hơn như đường thẳng, văn bản được gọi là **Artists**.

## 2. Ví dụ đối chiếu (Rule 17 - Double Examples)

### Ví dụ 1: Trích dẫn tài liệu (Original Context)
> "Matplotlib graphs your data on Figures... each of which can contain one or more Axes."
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots() # Tạo Figure và 1 Axes
ax.plot([1, 2, 3], [4, 5, 6]) # Vẽ lên Axes
```
**Nguồn**: `WEBSITE_PY_Matplotlib_QuickStart` — Section "Parts of a Figure"

### Ví dụ 2: Ẩn dụ sư phạm (Pedagogical Application)
Hãy tưởng tượng **Figure** là một "Tờ giấy vẽ", và **Axes** là "Các khung biểu đồ" bạn kẻ trên tờ giấy đó. Bạn có thể kẻ 2 khung (subplot) trên cùng 1 tờ giấy để so sánh dữ liệu.
- **Figure**: Tờ giấy A4.
- **Axes**: Khung lưới tọa độ bạn vẽ tay vào.
- **Artists**: Các nét bút màu bạn tô vẽ lên đó.

## 3. 4F Reflection
- **Facts**: Figure là đối tượng cấp cao nhất, quản lý toàn bộ các thành phần con.
- **Feelings**: Việc phân biệt Figure và Axes lúc đầu có thể gây nhầm lẫn (Axes không phải là số nhiều của Axis).
- **Findings**: Hiểu rõ cấu trúc này giúp tùy chỉnh biểu đồ (customization) linh hoạt hơn thay vì chỉ dùng hàm mặc định.
- **Futures**: Cần thực hành tạo nhiều Subplots (mosaic) để nắm vững việc quản lý Figure.

---
Nguồn: [[SOURCE_PY_Matplotlib_QuickStart]]
[[CONCEPT_PY_Pandas_Basics]]


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
