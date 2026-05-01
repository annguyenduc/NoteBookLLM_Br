name: wiki-ingest
description: "WIKI — Nạp nguồn tri thức mới vào hệ thống: @scout phân tích raw file, tạo Analysis draft, chờ user duyệt trước khi @engineer viết Wiki Atoms."
version: 1.0.0
audit_id: AG-WIKI-001
---

# wiki-ingest — LLM Wiki Ingest Workflow

> **Goal:** Biến một file thô trong `raw/sources/` thành các Wiki Atoms có cấu trúc trong `wiki/concepts/`, `wiki/entities/`, `wiki/sources/` — đảm bảo Anti-Hallucination (Rule 10, 14) và Double Examples (Rule 17).

## When to Activate

- User chạy lệnh `/ingest [tên_file]` hoặc `/ingest` (không có tham số)
- Có file mới trong `raw/sources/` hoặc `00_Inbox/` chưa được xử lý
- User muốn compile một tài liệu cụ thể vào wiki

## Pre-conditions (CHECKPOINT bắt buộc)

Trước khi bắt đầu, agent khai báo CHECKPOINT:

```yaml
CHECKPOINT:
  agent: "@scout"
  task: "Phân tích [tên_file] và tạo Analysis draft"
  step: "1 / 2"
  output_file: "1-projects/[Project]/Analysis_[PREFIX]_[tên_file].md"
  stop_condition: "Sau khi tạo xong Analysis file và chờ user duyệt"
  prerequisites:
    - file: "3-resources/raw/sources/[tên_file]"
      exists: "YES | NO"
    - file: "3-resources/WIKI_AGENT_GUIDE.md"
      exists: "YES | NO"
    - file: "3-resources/SOURCE_TEMPLATE.md"
      exists: "YES | NO"
  status: "READY | BLOCKED"
  blocked_reason: ""
```

Nếu file nguồn KHÔNG tồn tại trong `raw/sources/` → DỪNG, báo user, KHÔNG tiếp tục.

## Instructions

### Step 1 — @scout: Phân tích & tạo Analysis file

**Đọc trước khi làm:**
- `3-resources/WIKI_AGENT_GUIDE.md` — quy tắc tạo atoms
- `3-resources/purpose.md` — định hướng wiki (ưu tiên sư phạm K-12)
- `3-resources/wiki/index.md` — kiểm tra concept đã tồn tại chưa (tránh duplicate)

**Thực hiện:**

1. Mở file gốc trong `3-resources/raw/sources/[tên_file]` — đọc toàn bộ.
2. Trích xuất:
   - **Key Concepts** — các khái niệm cốt lõi (ưu tiên 20% giải quyết 80% vấn đề)
   - **Entities** — công cụ, tổ chức, người, hệ thống được nhắc đến
   - **Connections** — các concept đã có trong `wiki/` có thể link đến
   - **Pedagogical Angles** — cách áp dụng vào dạy học K-12/STEAM (Rule 17 prep)
3. Tạo file `1-projects/[Project]/Analysis_[PREFIX]_[tên_file].md` theo cấu trúc:

```markdown
# Analysis: [Tên file gốc]
**Nguồn**: `3-resources/raw/sources/[tên_file]`
**Phân tích bởi**: @scout
**Ngày**: YYYY-MM-DD

## Mining Stats
| Chỉ số | Số lượng |
|:---|:---:|
| Key Concepts phát hiện | N |
| Entities phát hiện | N |
| Connections với wiki hiện tại | N |
| Atoms đề xuất tạo mới | N |

## Atoms đề xuất

### Concepts (wiki/concepts/)
- [ ] `THINK_[TênKháiNiệm].md` — [mô tả 1 câu]
- [ ] `[DOMAIN]_[TênKháiNiệm].md` — [mô tả 1 câu]

### Entities (wiki/entities/)
- [ ] `ENTITY_[Tên].md` — [mô tả 1 câu]

### Source Summary (wiki/sources/)
- [ ] `SOURCE_[TênFile].md` — tóm tắt toàn bộ tài liệu

## Connections với Wiki hiện tại
- `[[THINK_XYZ]]` — liên quan vì...
- `[[ENTITY_ABC]]` — cần cập nhật thêm...

## Master Files cần bồi đắp (Rule 3)
- `wiki/synthesis/[file].md` — section nào cần update

## Pedagogical Notes (cho Rule 17)
[Ghi chú về cách áp dụng vào K-12/STEAM cho từng concept]

## ⏸️ CHỜ USER DUYỆT
Danh sách atoms trên đã sẵn sàng. Vui lòng:
- ✅ Approve toàn bộ → gõ `/ingest-execute`
- ✏️ Chỉnh sửa danh sách → edit file này rồi gõ `/ingest-execute`
- ❌ Hủy → gõ `/ingest-cancel`
```

4. Ghi log:
```
## [YYYY-MM-DD HH:MM] SCOUT | @scout | Phân tích [tên_file]
- File tạo: 1-projects/[Project]/Analysis_[PREFIX]_[tên_file].md
- Lý do: Bước 1/2 của /ingest workflow
```

**DỪNG TẠI ĐÂY — chờ user duyệt.**

---

### Step 2 — @engineer: Viết Wiki Atoms (chỉ sau khi user approve)

Trigger: User gõ `/ingest-execute` sau khi đã duyệt Analysis file.

**CHECKPOINT bắt buộc trước Step 2:**

```yaml
CHECKPOINT:
  agent: "@engineer"
  task: "Viết Wiki Atoms từ Analysis_[tên_file].md"
  step: "2 / 2"
  output_file: "3-resources/wiki/[layer]/[TênAtom].md"
  stop_condition: "Sau khi tạo đủ N atoms đã được duyệt"
  prerequisites:
    - file: "1-projects/[Project]/Analysis_[PREFIX]_[tên_file].md"
      exists: "YES"
    - file: "3-resources/SOURCE_TEMPLATE.md"
      exists: "YES"
  status: "READY"
```

**Thực hiện với từng atom được duyệt:**

1. **Đọc lại file nguồn gốc** trong `raw/sources/` — KHÔNG dùng từ Analysis file (Rule 14).
2. Tạo mỗi atom với YAML frontmatter chuẩn:

```yaml
---
title: "[Tên Concept]"
type: concept | entity | synthesis | source
domain: THINK | SQL | Python | STEAM | STAT
status: draft
sources:
  - "[tên-file-raw.pdf]"
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

3. Mọi atom **BẮT BUỘC** có:
   - `## Ví dụ đối chiếu (Rule 17: Double Examples)` — 2 ví dụ: gốc + sư phạm
   - `Nguồn: [tên file raw] — [section cụ thể]` — xác nhận thực sự đã mở file
   - Tối thiểu 2 `[[wikilinks]]` đến pages khác (Rule 2)
   - Checklist: `- [ ] [Rule 14] Đã mở file nguồn và xác nhận fact tồn tại`

4. Sau mỗi atom được tạo:
   - Cập nhật `3-resources/wiki/index.md`
   - Bồi đắp `wiki/synthesis/` liên quan (Rule 3)
   - Ghi WRITE REPORT:
   ```
   WRITE REPORT:
     file: "3-resources/wiki/concepts/[TênAtom].md"
     operation: "create"
     added: "Atom mới về [tên concept]"
     removed: NONE
   ```

5. Sau khi hoàn thành toàn bộ batch:
   - Ghi log tổng kết vào `3-resources/wiki/log.md`
   - Cập nhật Mining Stats trong Analysis file (đánh dấu ✅ các atoms đã tạo)
   - Báo cáo: "Đã tạo N/M atoms. Sẵn sàng chạy `/lint` để kiểm tra."

## Quality Gate (Red Flags)

- ❌ @engineer bắt đầu Step 2 khi chưa có duyệt từ user
- ❌ Viết atom mà không mở file raw gốc (vi phạm Rule 14)
- ❌ Atom thiếu Double Examples (vi phạm Rule 17)
- ❌ Atom có < 2 wikilinks (vi phạm Rule 2)
- ❌ Báo cáo "Đã tạo" mà chưa có tool call thực thi (vi phạm Rule 15)
- ❌ Ghi vào `raw/sources/` (vi phạm Rule 12)

## Example Triggers

- `/ingest Problem_Solving_101.pdf`
- `/ingest` (agent tự hỏi file nào cần xử lý trong 00_Inbox/)
- `/ingest-execute` (sau khi user đã duyệt Analysis file)
- `/ingest-cancel` (hủy workflow hiện tại)
