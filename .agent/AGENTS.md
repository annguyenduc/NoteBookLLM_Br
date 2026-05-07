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
## ⚡ LỆNH VẬN HÀNH (Wiki 2.0)

| Lệnh | Agent | Làm gì | Skill trỏ tới |
|---|---|---|---|
| `/ingest [file]` | @scout | Nạp raw -> atomic atoms + sơ khởi liên kết | `wiki-ingest` |
| `/absorb` | @librarian | Hợp nhất atoms vào synthesis (Reconciliation) | `wiki-absorb` |
| `/query [query]` | @librarian | Truy vấn tri thức (Hybrid Search + Graph) | `wiki-query` |
| `/breakdown` | @scout | Phát hiện lỗ hổng tri thức (Noun Test) | `wiki-breakdown` |
| `/cleanup` | @auditor | Dọn dẹp & Audit chất lượng (8 Categories) | `wiki-cleanup` |
| `/status` | @pm | Báo cáo sức khỏe & Link Density Dashboard | `wiki-status` |
| `/rebuild` | @engineer | Đồng bộ Index, Backlinks & Infrastructure | `wiki-rebuild` |

> Mọi Agent phải nỗ lực để hệ thống tốt hơn **1%** mỗi ngày. Để **invoke** một Skill, hãy sử dụng đúng lệnh tương ứng.
> Lưu ý: Chỉ **Human** mới có quyền set trạng thái **SYNTHESIZED**.
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
├── 00_Inbox/                ← PROCESSING HUB: Tiếp nhận, Trích xuất, Audit (Temporary)
├── 1-projects/
├── 2-areas/
├── 3-resources/
│   ├── raw_sources/         ← EVIDENCE: File gốc (PDF, HTML). Append-only.
│   ├── raw_ingest/          ← FUEL: HD Markdown đạt chuẩn Audit. Append-only.
│   ├── raw_assets/          ← VISUAL PROOF: Hình ảnh/Biểu đồ phẳng. Append-only.
│   └── wiki/
│       ├── index.md
│       ├── log.md
│       ├── concepts/
│       ├── entities/
│       ├── sources/
│       ├── comparisons/
│       ├── queries/
│       ├── synthesis/
│       ├── decisions/             ← LƯU TRỮ QUYẾT ĐỊNH — Kết quả từ @wiki-council khi giải quyết mâu thuẫn tri thức.
│       ├── review_queue/          ← PENDING — Các Atom mới từ @wiki-ingest chờ Human duyệt.
│       ├── session_insights/      ← NHẬT KÝ NHIỆM VỤ — Báo cáo tổng hợp, Audit log, và insight sau mỗi phiên làm việc.
│       └── wiki_brain.db
│
├── 4-archive/
│   └── legacy_scripts/             ← Nơi lưu trữ nợ kỹ thuật
└── scripts/
    └── mcp_run_mcp.bat             ← Entry point duy nhất còn lại
```

---

## 5 RULES BẮT BUỘC (Hard Stop nếu vi phạm)

**R1 — RAW IS IMMUTABLE (Append-only)**
`3-resources/raw_*/` là khu vực bất biến.
- **Định nghĩa:** Chỉ được thêm mới qua quy trình kiểm định, KHÔNG sửa đổi nội dung, KHÔNG xóa bỏ file hiện có.
- **Ma trận quyền hạn:**
    - `@librarian`: Agent duy nhất có quyền ghi/di chuyển file vào `raw_sources/`, `raw_ingest/`, `raw_assets/`.
    - `@engineer`: Chỉ có quyền ghi vào `00_Inbox/` (để trích xuất/audit).
    - `@others`: Read-only trên toàn bộ khu vực `raw_*/`.
- Vi phạm → @healer rollback ngay.

**R2 — NO FAKE REPORTS**
Tuyệt đối KHÔNG báo "Đã tạo/sửa file" nếu chưa có tool call thành công.
Vi phạm → ghi lỗi vào `CONTINUITY.md` và thông báo user.

**R3 — SOURCE TRACING**
Mọi claim trong wiki phải ghi rõ `Nguồn: [tên file trong raw_sources/] — [section]`.
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
- `@designer` chỉ bắt đầu khi `2-areas/Profiles/Trainer_Profile_[id].md` tồn tại.
- `@engineer` chỉ bắt đầu khi `1-projects/[Project]/Learning_Design_[module].md` tồn tại.
- File chưa có → DỪNG, báo `@pm`, không tự tiếp tục.

**R6 — SEQUENTIAL FOUNDATION**
Tuyệt đối KHÔNG viết bất kỳ dòng code Skill nào cho đến khi Phase 1 (Schema, SOUL, USER) hoàn thành 100% và được xác nhận.

**R7 — PRESSURE TEST MANDATORY**
Mỗi Skill/Script sau khi hoàn thành phải vượt qua ít nhất 1 bài kiểm tra áp lực (Stress Test) với dữ liệu thực tế lớn trước khi chuyển sang Skill tiếp theo.

**R8 — HUMAN-ONLY SYNTHESIS**
Agent tuyệt đối KHÔNG tự ý thiết lập trạng thái `SYNTHESIZED` cho các concept. Đây là quyền hạn duy nhất của User sau khi review `review_queue/`.

**R9 — SURGICAL MINIMALISM**
Tuân thủ nghiêm ngặt **Surgical Changes**: Chỉ thay đổi code tối thiểu để giải quyết vấn đề, không over-engineer, không tự ý refactor code lân cận nếu không liên quan trực tiếp đến task.

**R10 — SEARCH & VISUAL VALIDATION PIPELINE (Quy trình 3 bước)**
Mọi hành động thu thập dữ liệu web BẮT BUỘC phải tuân thủ quy trình 3 bước để đảm bảo tính xác thực và tránh rác:
1. **Bước 1: Discovery (Tìm kiếm)**: Sử dụng `Lightpanda` hoặc `search_web` để tìm kiếm và lọc danh sách URL tiềm năng.
2. **Bước 2: Verification (Xác thực nội dung)**: BẮT BUỘC truy cập URL bằng `Lightpanda` hoặc `Crawl4AI` ở chế độ trích xuất **Markdown/Text** để xác nhận URL tồn tại (HTTP 200) và chứa đúng nội dung tri thức cần tìm. **TUYỆT ĐỐI KHÔNG** chụp ảnh ở bước này.
3. **Bước 3: Visual Capture (Chụp ảnh bằng chứng)**: Chỉ thực hiện chụp ảnh (Screenshot) bằng `Crawl4AI` hoặc `Browser Subagent` sau khi Bước 2 xác nhận nội dung **ĐẠT YÊU CẦU**.
- **Cấm 404/Rác**: Tuyệt đối không chụp ảnh trang lỗi 404, trang trắng, CAPTCHA hoặc trang không liên quan.
- **Vi phạm**: Nếu phát hiện ảnh rác, Agent phải tự động rollback, ghi lỗi vào `3-resources/wiki/log.md` và thực hiện lại cho đến khi có bằng chứng thực.

**R11 — NO AUTO-STUB CREATION**
- `indexer.py` KHÔNG tạo atom cho file < 200 bytes.
- `rebuild.py` SKIP các file không có frontmatter hợp lệ.
- Stub files trong `00_Inbox/` được xử lý hàng tuần, KHÔNG index ngay lập tức.

**R12 — VIETNAMESE ENCODING SAFETY**
- Mọi file tiếng Việt phải đọc/ghi bằng UTF-8 no BOM.
- Khi ghi file bằng PowerShell: luôn dùng `-Encoding UTF8`.
- KHÔNG dùng chuyển mã tự động (latin1/cp1252/utf-8 repair) nếu chưa có yêu cầu explicit từ Human.
- Sau khi sửa file tiếng Việt, phải kiểm tra và đảm bảo không có ký tự lỗi phổ biến (``, `Ã`, `Ä`, `â€™`, `â€œ`, `â€`, `á»`, `áº`).
- Nếu phát hiện lỗi font/ngữ nghĩa: DỪNG, khôi phục từ phiên bản gần nhất, rồi sửa thủ công nội dung.

**R13 — ATOM STATUS LIFECYCLE**
- Mọi atom tạo mới BẮT BUỘC phải có `status = DRAFT`.
- **TUYỆT ĐỐI KHÔNG** tự ý set status = VERIFIED/SYNTHESIZED khi tạo atom.
- Chỉ `ingest.py` và `reconciler.py` được quyền nâng cấp lên **VERIFIED**.
- Chỉ **HUMAN** được quyền thiết lập trạng thái **SYNTHESIZED**.

**RULE: obsidian-cli usage**
- Dùng obsidian-cli KHI: cần set property, append content, search vault đang mở.
- Dùng filesystem KHI: Obsidian không mở hoặc cần batch operation trên nhiều files.
- KHÔNG dùng obsidian-cli trên iPad.
- Obsidian PHẢI đang mở thì CLI mới hoạt động.

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


## RULE: Sync direction
- **DB → File**: CHỈ sync status `SYNTHESIZED` (sau khi human confirm).
- **File → DB**: `rebuild.py` chạy hàng đêm để cập nhật Index.
- **DEPRECATED**: Chỉ tồn tại trong DB. KHÔNG sync ngược về file vật lý. KHÔNG di chuyển file vật lý.
- **Lý do**: File vật lý là Source of Truth. DB là Index. Không để DB ghi đè/xóa file trái ý muốn của Human.
