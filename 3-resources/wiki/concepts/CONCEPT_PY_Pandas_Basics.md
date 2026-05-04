---
file_id: "WIKI_CONCEPT_PY_PANDAS_BASICS"
title: "Cơ bản về Pandas (Pandas Basics)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Python", "Pandas", "Data_Analysis", "Basics"]
source: "[[SOURCE_PY_Python_for_Data_Analysis]]"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# Cơ bản về Pandas (Pandas Basics)

**Pandas** là thư viện nền tảng của hệ sinh thái dữ liệu Python, cung cấp các cấu trúc dữ liệu mạnh mẽ để làm việc với dữ liệu bảng (Tabular Data).

## 核心 (Core Principle)
Bản chất của Pandas là **Sự trừu tượng hóa dữ liệu bảng**. Nó biến các mảng thô (Array) thành các đối tượng có nhãn (Labeled Objects), cho phép chúng ta thao tác với dữ liệu bằng "tên gọi" thay vì "chỉ số vị trí".

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trong tài liệu *Python for Data Analysis*, Wes McKinney mô tả việc truy cập dữ liệu bằng `loc` và `iloc`:
- **iloc**: Truy cập theo vị trí nguyên số (vd: hàng 0, cột 1).
- **loc**: Truy cập theo nhãn (vd: hàng có index '2026-01-01', cột 'Revenue').
- **Ứng dụng**: Giúp code tường minh và tránh lỗi khi thứ tự hàng/cột thay đổi.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng về một chiếc **Tủ thuốc gia đình**:
- **Truy cập iloc (Vị trí)**: Bạn bảo con: "Lấy cho bố lọ thuốc ở ngăn thứ 2, hàng thứ 3 bên trái". Nếu ai đó sắp xếp lại tủ, con sẽ lấy nhầm thuốc.
- **Truy cập loc (Nhãn)**: Bạn bảo: "Lấy cho bố lọ có nhãn 'Thuốc ho'". Dù lọ thuốc nằm ở đâu, con vẫn lấy đúng.
- **Kết luận**: Trong phân tích dữ liệu, việc dùng `loc` (nhãn) giống như dán nhãn cho lọ thuốc, giúp quy trình làm việc an toàn và bền vững hơn.

## Liên kết tư duy
- [[CONCEPT_PY_Pandas_Data_Cleaning]]
- [[CONCEPT_PY_Pandas_Data_Transformation]]
- [[ENTITY_PANDAS]]

## 4F — Phản tư sư phạm
- **Facts:** Pandas DataFrame thực chất là tập hợp của nhiều Series (cột) có chung chỉ số (Index).
- **Feelings:** Người mới bắt đầu thường cảm thấy choáng ngợp với hàng trăm hàm của Pandas, dẫn đến tâm lý "nhớ vẹt" code thay vì hiểu bản chất.
- **Findings:** Hiểu rõ về **Index** là chìa khóa để làm chủ Pandas. Index không chỉ là số thứ tự, nó là định danh của dữ liệu.
- **Futures:** Khi dữ liệu vượt quá bộ nhớ RAM, chúng ta sẽ chuyển từ Pandas sang **Polars** hoặc **Dask**, nhưng tư duy "Labeled Objects" vẫn là nền tảng không đổi.

---
Nguồn: [[SOURCE_PY_Python_for_Data_Analysis]] (Wes McKinney)
Xác nhận Rule 14 từ NotebookLM Ingest (2026-05-03).


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
