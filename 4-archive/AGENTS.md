# AGENTS.md — NoteBookLLM_Br

> Đọc file này TRƯỚC KHI thực hiện bất kỳ tác vụ nào.
> Mục tiêu hệ thống: Second brain theo mô hình LLM Wiki — ingest tài liệu thô → atomic wiki nodes → synthesis có thể verify nguồn.

---

## STARTUP (Bắt buộc mỗi phiên)

1. Đọc `AGENTS.md` (file này) và `WORKSPACE_OVERVIEW.md`
2. Khai báo CHECKPOINT (xem cuối file) trước khi bắt đầu task
3. Ghi log vào `3-resources/wiki/log.md` sau khi hoàn thành

---

## AGENTS

| Agent | Gọi bằng | Làm gì |
|---|---|---|
| **@pm** | `@pm` | Lập kế hoạch, phân task, quản lý pipeline |
| **@scout** | `@scout` | Nghiên cứu, phân tích raw file, tạo EXAM_Context |
| **@engineer** | `@engineer` | Viết code, tạo wiki atoms, thực thi task |
| **@librarian** | `@librarian` | Quản lý wiki, cập nhật index, synthesis |
| **@auditor** | `@auditor` | Kiểm định nguồn, reverse tracing, lint |
| **@designer** | `@designer` | Thiết kế learning sequence (cần Trainer Profile trước) |
| **@healer** | `@healer` | Sửa lỗi link, rollback vi phạm |

> Agents giáo dục (@evaluator, @profiler, @creative) → xem `SKILL.md` trong `.agents/skills/pedagogy/`

---

## LỆNH THƯỜNG DÙNG

| Lệnh | Làm gì |
|---|---|
| `/ingest [file]` | @scout phân tích raw → user duyệt → @engineer tạo wiki atoms |
| `/file-back` | Lưu kết quả chat/research thành QUERY_ page |
| `/lint` | @auditor kiểm toàn bộ wiki (broken links, orphans, frontmatter) |
| `/scout [topic]` | Nghiên cứu + đánh giá độ khó |
| `/heal` | @healer sửa lỗi theo log |
| `/ingest-inbox` | Xử lý toàn bộ `00_Inbox/` |

---

## CẤU TRÚC THƯ MỤC

```
00_Inbox/          ← Drop files vào đây, xử lý hàng tuần
1-projects/        ← Mỗi dự án 1 folder (vd: 2026_TOT_STEAM/)
2-areas/           ← Curriculum/ | Assessment/ | Profiles/
3-resources/
  ├── raw/         ← IMMUTABLE — chỉ user mới thêm file
  └── wiki/
      ├── index.md
      ├── log.md
      ├── concepts/     ← Atomic concept nodes
      ├── entities/     ← Tools, systems, organizations
      ├── sources/      ← Tóm tắt sách đã ingest
      ├── queries/      ← Kết quả research (prefix QUERY_)
      └── synthesis/    ← Knowledge compounding, bài kiểm tra
4-archive/         ← File hoàn thành, prefix YYYYMMDD_
```

---

## 5 RULES BẮT BUỘC (Hard Stop nếu vi phạm)

**R1 — RAW IS IMMUTABLE**
`3-resources/raw/` là read-only với mọi agent. Vi phạm → @healer rollback ngay.

**R2 — NO FAKE REPORTS**
Tuyệt đối KHÔNG báo "Đã tạo/sửa file" nếu chưa có tool call thành công.
Vi phạm → ghi lỗi vào `CONTINUITY.md` và thông báo user.

**R3 — SOURCE TRACING**
Mọi claim trong wiki phải ghi rõ `Nguồn: [tên file trong raw/] — [section]`.
Không tìm thấy nguồn → ghi `[KHÔNG TÌM THẤY NGUỒN]`, KHÔNG tự điền thay thế.

**R4 — LOG EVERY WRITE**
Mọi lần ghi file → append vào `log.md`:
```
## [YYYY-MM-DD HH:MM] <type> | <agent> | <mô tả>
- File: [đường dẫn]
- Lý do: [1 câu]
```
Dùng UTF-8 (no BOM). Nếu dùng PowerShell: bắt buộc thêm `-Encoding UTF8`.

**R5 — PREREQUISITE GATE (Pedagogical Pipeline)**
@designer chỉ bắt đầu khi `Trainer_Profile_[id].md` tồn tại.
@engineer chỉ bắt đầu khi `Learning_Design_[module].md` tồn tại.
Nếu file chưa có → DỪNG, báo @pm, không tự tiếp tục.

---

## CHECKPOINT (Khai báo trước mọi task)

```yaml
CHECKPOINT:
  agent: "@[tên]"
  task: "[mô tả cụ thể]"
  output_file: "[đường dẫn]"
  prerequisites_ok: "YES | NO — [lý do nếu NO]"
  status: "READY | BLOCKED"
```
