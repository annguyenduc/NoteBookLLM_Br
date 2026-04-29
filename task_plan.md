# Roadmap NoteBookLLM_Br v5.3 (2026-04-29) — Pivot: Data Analyst Wiki (80/20 Rule)

##  PIVOT NOTICE: NGUYÊN TẮC PARETO (80/20) KẾT HỢP NOTEBOOKLM
> **Quyết định từ User**: Sử dụng danh mục nguồn chuẩn từ NotebookLM nhưng áp dụng **quy tắc 80/20**. Thay vì dàn trải cả 7 nhóm, chúng ta chỉ tập trung trích xuất **Nhóm 1, 3, 4, 5** – 20% kiến thức lõi giúp giải quyết 80% công việc thực tế của một Data Analyst (Kéo dữ liệu -> Làm sạch -> Trực quan hóa -> Kể chuyện & Giải quyết vấn đề).

---

##  Bản đồ Nguồn tri thức (Knowledge Map)
Dưới đây là danh mục 7 nhóm nguồn đã được đối chiếu từ NotebookLM. Các nhóm được đánh dấu **[CORE 80/20]** sẽ được ưu tiên trích xuất trước.

###  Các nhóm ưu tiên (The 80/20 Core)
- **Nhóm 1: Tư duy Phân tích & Giải quyết vấn đề [CORE 80/20]**
  - [x] *Thinking with Data*
  - [x] *Problem Solving 101*
  - [x] *Data Science for Business*
- **Nhóm 3: Công cụ Cốt lõi (Excel & SQL) [CORE 80/20]**
  - [x] *SQL Cookbook*
  - [x] *Getting Started with SQL*
  - [x] *SQL for Data Analysis*
  - [x] *Excel Data Analysis*
  - [x] *SQL Pocket Guide*
- [x] **Nhóm 4: Lập trình & Xử lý dữ liệu lớn (Python) [CORE 80/20]**
  - [x] *Python for Data Analysis*
  - [x] *Python Data Science Handbook*
- **Nhóm 5: Trực quan hóa & Kể chuyện (Data Visualization) [CORE 80/20]**
  - [x] *Storytelling with Data (P1, P2, P3)*
  - [x] *How to Design a Dashboard*
  - [x] *Mastering Tableau / Power BI*

###  Các nhóm mở rộng (Đọc bổ trợ sau)
- **Nhóm 2: Thống kê & Toán học Thực chiến**
  - [ ] *Naked Statistics*
  - [ ] *Practical Statistics for Data Scientists*
- **Nhóm 6: Hệ thống & Kỹ thuật Dữ liệu (DE)**
  - [ ] *The Data Warehouse Toolkit*
  - [ ] *Designing Data-Intensive Applications*
- **Nhóm 7: Khoa học Dữ liệu & Học máy (DS/ML)**
  - [ ] *Master Machine Learning Algorithms*
  - [ ] *Marketing Analytics*

---

## ️ Giai đoạn 2: Action Plan (Thực thi ngay)
- [x] **Khởi tạo Dự án**: Tạo `1-projects/2026_Data_Analyst/Ingest_80_20.md` làm file tracking cụ thể các concepts sẽ được tạo từ 4 nhóm ưu tiên.
- [x] **Nhóm 3 & 4 (SQL/Python Atoms)**: Trích xuất các snippet, lệnh thao tác dữ liệu (Data Manipulation) cốt lõi nhất. Tạo các file `ENTITY_SQL`, `ENTITY_PYTHON`, `ENTITY_PANDAS`.
- [x] **Nhóm 5 (Visualization Atoms)**: Trích xuất các nguyên tắc thiết kế dashboard và biểu đồ từ *Storytelling with Data*. Tạo các file `VIZ_...`.
- [x] **Nhóm 1 (Thinking Atoms)**: Củng cố các framework phân tích (RCA, 5 Whys, CRISP-DM) từ *Thinking with Data*. Tạo/cập nhật `THINK_...`.

---

##  Giai đoạn 3: Tích hợp Synthesis
- [x] Kết nối các trang thành một luồng Master: `wiki/synthesis/SYNTHESIS_DA_Core_Workflow.md`.
- [x] Kiểm tra định kỳ bằng `brain_lint.py` để đảm bảo 0 Broken Link, 0 Orphan Page.
