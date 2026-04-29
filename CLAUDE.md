#  Operational Memory (LOM) — CLAUDE.md

> **Status**: ACTIVE | **Session ID**: AUTO-GENERATE | **Focus**: Data Analyst 80/20 Ingest
> **Cập nhật lần cuối**: 2026-04-29 | **Schema**: v5.3
> ️ **Đây là file Bộ nhớ Trung hạn.** Nó sẽ được reset/archive khi dự án `2026_Data_Analyst` hoàn tất.

---

## ️ Session Context — Dự án Hiện tại

- **Dự án chính**: `1-projects/2026_Data_Analyst/`
- **File tracking**: `1-projects/2026_Data_Analyst/Ingest_80_20.md`
- **Mục tiêu**: Trích xuất 20% kiến thức lõi (SQL, Python/Pandas, Data Visualization, Analytical Thinking) giải quyết 80% công việc của một Data Analyst.
- **Trạng thái Ingest** (Lộ trình 80/20):
  - [x] Nhóm 1 — THINK (Tư duy & Giải quyết vấn đề): **DONE**
  - [x] Nhóm 3 — SQL: **DONE** (Đã audit Rule 17 Double Examples)
  - [x] Nhóm 4 — Python / Pandas: **DONE** (Đã audit Rule 17 Double Examples)
  - [x] Nhóm 5 — Data Visualization & Storytelling: **DONE**
  - [x] Tích hợp Synthesis: **DONE** (`SYNTHESIS_DA_Core_Workflow.md`)
- **Trạng thái Audit**: Đã hoàn thành "Audit chiều sâu" (Rule 5 & 17) cho Nhóm 3 và Nhóm 4. Hệ thống Data Analyst Wiki đang ở trạng thái **XANH**.
- **Hành động tiếp theo**: Ingest Nhóm 2 (Thống kê thực chiến) hoặc tiếp tục phát triển chiều sâu cho các trang Synthesis.

---

##  Wiki Content Standards — Data Analyst

Mọi Wiki Atom thuộc dự án này **BẮT BUỘC** tuân theo các chuẩn sau. Agent phải đọc `3-resources/WIKI_AGENT_GUIDE.md` trước khi tạo/sửa bất kỳ trang nào.

- **No Emojis**: Tuyệt đối không sử dụng Emoji trong nội dung Wiki. Sử dụng text markers như [OK], [TODO], [IMPORTANT] hoặc văn bản thuần túy.

###  Chuẩn cho SQL Atoms (`CONCEPT_SQL_*.md`, `ENTITY_SQL.md`)
1. **Syntax Block**: Mọi khái niệm SQL phải có một code block cú pháp chuẩn (ANSI SQL).
2. **Minimal Working Example**: Tối thiểu 1 ví dụ SQL hoạt động được, có comment giải thích.
3. **Gotchas / Pitfalls**: Ít nhất 1 mục cảnh báo lỗi thường gặp (vd: `NULL` trong `JOIN`, thứ tự `WHERE` vs `HAVING`).
4. **Wikilinks bắt buộc**: Mỗi trang SQL phải link đến `[[ENTITY_SQL]]` và ít nhất 1 concept liên quan.

```sql
-- Ví dụ chuẩn format cho SQL block
SELECT
    department,
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= '2020-01-01'
GROUP BY department
HAVING COUNT(*) > 5
ORDER BY avg_salary DESC;
```

###  Chuẩn cho Python / Pandas Atoms (`CONCEPT_Pandas_*.md`, `ENTITY_Python.md`)
1. **Import block**: Mọi code block phải bắt đầu bằng import statement rõ ràng.
2. **Input → Transform → Output Pattern**: Mỗi ví dụ phải thể hiện rõ 3 giai đoạn: dữ liệu đầu vào, phép biến đổi, kết quả đầu ra.
3. **Docstring-style comment**: Mỗi function/method được giải thích bằng 1 dòng comment `#`.
4. **Wikilinks bắt buộc**: Link đến `[[ENTITY_Python]]` và `[[ENTITY_Pandas]]`.

```python
import pandas as pd

# Input: DataFrame với cột 'age' có giá trị NaN
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Carol'], 'age': [25, None, 30]})

# Transform: Điền giá trị trung bình vào ô trống
df['age'] = df['age'].fillna(df['age'].mean())

# Output: DataFrame sạch, không còn NaN
print(df)
```

###  Chuẩn cho Visualization Atoms (`VIZ_*.md`)
1. **Khi nào dùng (Use Case)**: Mô tả rõ loại dữ liệu / câu hỏi phân tích phù hợp với viz này.
2. **Khi nào KHÔNG dùng (Anti-pattern)**: Tối thiểu 1 ví dụ phản ví dụ.
3. **Design Checklist**: Danh sách 3-5 tiêu chí thiết kế cần đảm bảo (vd: loại bỏ gridlines không cần thiết, dùng màu có mục đích).
4. **Wikilinks bắt buộc**: Link đến ít nhất 2 concept trong `wiki/concepts/` hoặc `wiki/synthesis/`.

###  Chuẩn chung cho mọi Atom (Rule 14 & Rule 17)
- **Rule 14 (Source Integrity)**: Mọi claim phải có ` Nguồn: [tên file raw] — [section]`. Agent phải thực sự mở file đó trong `3-resources/raw/` để xác nhận.
- **Rule 17 (Double Examples)**: Mọi concept phải có **tối thiểu 2 ví dụ** từ các ngữ cảnh khác nhau.
- **YAML Frontmatter bắt buộc**:

```yaml
---
title: "Tên Concept"
type: concept | entity | synthesis | source | viz
domain: SQL | Python | Visualization | Thinking
status: draft | verified
sources:
  - "tên-file-raw.pdf"
tags: [sql, joins, data-manipulation]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## ️ Bộ lệnh Chuẩn (Toolkit v5.3)

| Lệnh | Agent | Mô tả |
| :--- | :--- | :--- |
| `/ingest` | `@scout` → `@engineer` | Quy trình 2 bước: (1) @scout phân tích raw file → tạo `Analysis_PREFIX.md`; (2) User duyệt → @engineer tạo Wiki Atoms & cập nhật synthesis. |
| `/file-back` | `@pm` | Lưu kết quả research/chat có giá trị thành Wiki page mới trong `wiki/queries/` hoặc `wiki/concepts/`. |
| `/lint` | `@librarian` | Chạy `scripts/brain_lint.py`: kiểm tra orphan pages, broken wikilinks, stale claims, concept gaps. |
| `/scout` | `@scout` | Nghiên cứu tự do, đánh giá độ khó, không ghi thẳng vào synthesis. |
| `/heal` | `@healer` | Sửa lỗi liên kết, rollback vi phạm Rule 12, phục hồi tính toàn vẹn. |
| `/heartbeat` | `@librarian` | Tổng hợp trạng thái toàn bộ `3-resources/raw/` và cập nhật đồ thị kiến thức. |
| `/audit-tokens` | `@pm` | Kiểm tra ngân sách token của phiên hiện tại. |

>  **Lệnh đã deprecated**: `/distill`, `/consolidate` — Không còn dùng trong Schema v5+. Thay thế bằng `/ingest`.

---

## ️ Nền tảng Kiến trúc (Nhắc lại nhanh)

### Ba tầng bộ nhớ
| Tầng | File / Thư mục | Đặc điểm |
| :--- | :--- | :--- |
| **Short-term** | Context window của phiên chat | Bốc hơi khi đóng terminal. @pm đẩy insight sang Medium-term. |
| **Medium-term** | `CLAUDE.md`, `task_plan.md`, `Ingest_80_20.md`, `CONTINUITY.md` | "Bàn làm việc". Reset/archive khi dự án kết thúc. |
| **Long-term** | `AGENTS.md`, `WORKSPACE_OVERVIEW.md`, `3-resources/wiki/` | Vĩnh viễn. Chỉ bồi đắp thêm hoặc deprecate vào `4-archive/`. |

### Luồng dữ liệu cốt lõi
```
3-resources/raw/sources/  [IMMUTABLE]
        ↓ /ingest (Two-Step CoT)
1-projects/2026_Data_Analyst/Analysis_*.md  [DRAFT by @scout]
        ↓ User approve
3-resources/wiki/concepts/ & entities/  [ATOMS by @engineer]
        ↓ Knowledge Compounding (Rule 3)
3-resources/wiki/synthesis/  [MASTER by @librarian]
        ↓ /lint
3-resources/wiki/log.md  [APPEND-ONLY]
```

---

##  Các lỗi đã biết (Known Issues — xem chi tiết tại `CONTINUITY.md`)

- Đường dẫn `WIKI_INDEX.md` (cũ) đã được chuẩn hóa thành `wiki/index.md` — mọi reference cũ cần được cập nhật bởi `@healer`.
- Schema v4 dùng thư mục `distilled/` — đã **deprecated**, gộp vào `wiki/synthesis/`. Agent không được tạo file mới trong `distilled/`.

---

*File này là Bộ nhớ Trung hạn — được cập nhật bởi `@pm` sau mỗi phiên làm việc lớn. Khi dự án `2026_Data_Analyst` hoàn tất, file này sẽ được archive vào `4-archive/YYYYMMDD_CLAUDE_DA_Final.md`.*
