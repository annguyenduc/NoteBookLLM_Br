# AGENTS.md — NoteBookLLM_Br

> Đọc file này TRƯỚC KHI thực hiện bất kỳ tác vụ nào.
> Mục tiêu hệ thống: Second brain theo mô hình LLM Wiki — ingest tài liệu thô → atomic wiki nodes → synthesis có thể verify nguồn.

---

## STARTUP (Bắt buộc mỗi phiên)

1. Đọc `AGENTS.md`, `SOUL.md`, `USER.md` và `WORKSPACE_OVERVIEW.md`
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

> Agents giáo dục (@evaluator, @profiler, @creative) → xem `SKILL.md` trong `.agent/skills/pedagogy/`

---

## SKILL PATHS
- Antigravity: `.agent/skills/`
- Codex: `.codex/skills/` (symlink → `.agent/skills/`)

---
## LỆNH VẬN HÀNH (Wiki 2.0)

| Lệnh | Agent | Làm gì | Skill trỏ tới |
|---|---|---|---|
| `/ingest [file]` | @scout | Nạp raw -> atomic atoms + sơ khởi liên kết | `wiki-ingest` |
| `/absorb` | @librarian | Hợp nhất atoms vào synthesis (Reconciliation) | `wiki-absorb` |
| `/query [query]` | @librarian | Truy vấn tri thức (Hybrid Search + Graph) | `wiki-query` |
| `/breakdown` | @scout | Phát hiện lỗ hổng tri thức (Noun Test) | `wiki-breakdown` |
| `/cleanup` | @auditor | Dọn dẹp & Audit chất lượng (8 Categories) | `wiki-cleanup` |
| `/status` | @pm | Báo cáo sức khỏe & Link Density Dashboard | `wiki-status` |
| `/rebuild` | @engineer | Đồng bộ Index, Backlinks & Infrastructure | `wiki-rebuild` |

> Mọi Agent phải nỗ lực để hệ thống tốt hơn **1%** mỗi ngày.
> Để **invoke** một Skill, hãy sử dụng đúng lệnh tương ứng.
> Lưu ý: Chỉ Human mới có quyền set trạng thái **SYNTHESIZED**.

> Các lệnh bổ trợ: `/scout` (nghiên cứu sâu), `/heal` (sửa lỗi link), `/ingest-inbox` (xử lý folder inbox).
---

## CẤU TRÚC THƯ MỤC

```
NoteBookLLM_Br/              ← root
│
├── AGENTS.md                ← root level
├── SOUL.md                  ← root level  
├── USER.md                  ← root level
│
├── .agent/
│   ├── skills/
│   │   ├── wiki-ingest/
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       ├── ingest.py
│   │   │       └── magika_router.py
│   │   ├── pedagogy/
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       ├── export_comparison_to_pptx.py
│   │   │       └── convert_h5p.py
│   │   ├── wiki-rebuild/
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       ├── rebuild.py
│   │   │       └── indexer.py
│   │   ├── wiki-absorb/
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       └── reconciler.py
│   │   ├── wiki-query/
│   │   │   └── SKILL.md
│   │   ├── wiki-breakdown/
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       └── noun_miner.py
│   │   ├── wiki-cleanup/
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       └── lint_engine.py
│   │   ├── wiki-status/
│   │   │   └── SKILL.md
│   │   └── wiki-council/
│   │       └── SKILL.md
│   ├── mcp/
│   │   ├── mcp_server.py
│   │   └── notebooklm_bridge.py
│   └── references/                ← chỉ sparse checkout, không load thường trực
│
├── 00_Inbox/
├── 1-projects/
├── 2-areas/
├── 3-resources/
│   ├── raw/
│   │   └── MASTER_SOURCE_INDEX.md
│   └── wiki/
│       ├── index.md
│       ├── log.md
│       ├── concepts/
│       ├── entities/
│       ├── sources/
│       ├── comparisons/
│       ├── queries/
│       ├── synthesis/
│       ├── decisions/             ← THÊM MỚI — conflict ambiguous từ wiki-council
│       ├── review_queue/          ← THÊM MỚI — PENDING atoms chờ Human Gate
│       ├── session_insights/      ← THÊM MỚI — log_session_insight() output
│       └── wiki_brain.db
│
├── 4-archive/
│   └── legacy_scripts/             ← Nơi lưu trữ nợ kỹ thuật
└── scripts/
    └── mcp_run_mcp.bat             ← Entry point duy nhất còn lại
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
Mọi lần ghi file (create/modify) vào Wiki BẮT BUỘC phải append vào `3-resources/wiki/log.md`:
```
## [YYYY-MM-DD HH:MM] <TYPE> | <agent> | <mô tả>
- File: [đường dẫn]
- Lý do: [1 câu]
```
Encoding bắt buộc: **UTF-8 no BOM**. Nếu dùng PowerShell: luôn thêm `-Encoding UTF8`.

**R5 — PREREQUISITE GATE (Pedagogical Pipeline)**
@designer chỉ bắt đầu khi `Trainer_Profile_[id].md` tồn tại.
@engineer chỉ bắt đầu khi `Learning_Design_[module].md` tồn tại.
Nếu file chưa có → DỪNG, báo @pm, không tự tiếp tục.

**R10 — VISUAL PROOF MANDATORY**
Mọi hành động cào dữ liệu BẮT BUỘC phải đi kèm ảnh chụp bằng chứng (PNG/WebP) **hiển thị rõ nội dung thực tế của trang**. Tuyệt đối KHÔNG dùng ảnh "Generating recording" làm bằng chứng. Nếu không thể chụp ảnh nội dung, phải DỪNG và báo lỗi ngay.

**R11 — NO AUTO-STUB CREATION**
- `indexer.py` KHÔNG tạo atom cho file < 200 bytes.
- `rebuild.py` SKIP các file không có frontmatter hợp lệ.
- Stub files trong `00_Inbox/` được xử lý hàng tuần, KHÔNG index ngay lập tức.

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

## RULE: Atom Status Creation
- Mọi atom tạo mới phải có status = DRAFT
- KHÔNG set status = VERIFIED/SYNTHESIZED khi tạo atom
- Chỉ ingest.py và reconciler.py được set VERIFIED
- Chỉ HUMAN được set SYNTHESIZED

## RULE: Sync direction
- **DB → File**: CHỈ sync status `SYNTHESIZED` (sau khi human confirm).
- **File → DB**: `rebuild.py` chạy hàng đêm để cập nhật Index.
- **DEPRECATED**: Chỉ tồn tại trong DB. KHÔNG sync ngược về file vật lý. KHÔNG di chuyển file vật lý.
- **Lý do**: File vật lý là Source of Truth. DB là Index. Không để DB ghi đè/xóa file trái ý muốn của Human.
