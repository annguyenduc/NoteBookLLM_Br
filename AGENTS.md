# AGENTS.md — NoteBookLLM_Br

> Đọc file này TRƯỚC KHI thực hiện bất kỳ tác vụ nào.
> Mục tiêu hệ thống: Second brain theo mô hình LLM Wiki — ingest tài liệu thô → atomic wiki nodes → synthesis có thể verify nguồn.

---

## STARTUP (Bắt buộc mỗi phiên)

1. Đọc `AGENTS.md`, `.agent/rules/CORE.md` (Hard Stop Rules), và `WORKSPACE_OVERVIEW.md` (Pipeline Architecture).
   → `GEMINI.md`: CHỈ đọc khi gặp tình huống phức tạp cần tra cứu chéo. KHÔNG inject mặc định.
2. Inject Scoped Context: Đọc `SOUL.md`, `USER.md` và file rules tương ứng với agent đang hoạt động (`.agent/rules/[agent].md`).
3. Khai báo CHECKPOINT (xem cuối file) trước khi bắt đầu task
4. Ghi log vào file nhật ký ngày hiện tại trong `3-resources/wiki/logs/` sau khi hoàn thành

> **Tra cứu Bản đồ 27 rules và WikiCouncil 2.0**: [[GEMINI.md]]

---

## AGENTS

| Agent | Gọi bằng | Làm gì | Rules |
|---|---|---|---|
| **@pm** | `@pm` | Lập kế hoạch, phân task, quản lý pipeline | `.agent/rules/pm.md` |
| **@scout** | `@scout` | Nghiên cứu, phân tích raw file, tạo EXAM_Context | `.agent/rules/scout.md` |
| **@engineer** | `@engineer` | Viết code, tạo wiki atoms, thực thi task | `.agent/rules/engineer.md` |
| **@librarian** | `@librarian` | Quản lý wiki, cập nhật index, synthesis | `.agent/rules/librarian.md` |
| **@auditor** | `@auditor` | Kiểm định nguồn, reverse tracing, lint | `.agent/rules/auditor.md` |
| **@designer** | `@designer` | Thiết kế learning sequence (cần Trainer Profile trước) | `.agent/rules/CORE.md` |
| **@healer** | `@healer` | Sửa lỗi link, rollback vi phạm | `.agent/rules/healer.md` + [[GEMINI.md#R28]] |

> **Nguyên tắc**: Mỗi agent chỉ đọc rules của mình + CORE.md.
> Khi gặp tình huống phức tạp cần tra cứu chéo → đọc [[GEMINI.md]] đầy đủ.

---

## SKILL PATHS
- Antigravity: `.agent/skills/`
- Karpathy Patterns: `.agent/skills/karpathy-core/`
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
| `/gap-summary` | @librarian | Tổng hợp danh sách gap candidates hiện tại | `SOP_Weekly_Gap_Review` |
| `/gap-promote` | @engineer | Thăng cấp candidate thành Atom nháp (review_queue) | `SOP_Weekly_Gap_Review` |
| `/gap-cleanup` | @auditor | Dọn dẹp sạch inbox gap candidates | `SOP_Weekly_Gap_Review` |
| `/gap-retry` | @scout | Xử lý lại các task gap-check bị lỗi trong DLQ | `SOP_DLQ_Recovery` |

---

## CẤU TRÚC THƯ MỤC

```
NoteBookLLM_Br/              ← root
│
├── AGENTS.md                ← root level
├── GEMINI.md                ← Hiến pháp tối cao (R1-R27)
├── EXAMPLES.md              ← Ví dụ đối chiếu mẫu
├── SOUL.md                  ← Linh hồn hệ thống
├── USER.md                  ← Chân dung User
│
├── 00_Inbox/                ← PROCESSING HUB
├── 1-projects/
├── 2-areas/
├── 3-resources/
│   ├── raw_sources/         ← EVIDENCE: File gốc (PDF, HTML)
│   ├── raw_ingest/          ← FUEL: HD Markdown đạt chuẩn
│   ├── raw_assets/          ← VISUAL PROOF: Hình ảnh/Biểu đồ
│   └── wiki/
│       ├── index.md         ← SOURCE OF TRUTH: Mục lục tổng của Wiki.
│       ├── log.md           ← INDEX: Chỉ mục dẫn đến các file log ngày.
│       ├── logs/            ← ARCHIVE: log_YYYY_MM_DD.md
│       ├── concepts/        ← Tri thức nguyên tử (Atomic Nodes)
│       ├── entities/        ← Thực thể (Tool, Person, Org)
│       ├── sources/         ← Nguồn trích dẫn (Source Nodes)
│       ├── comparisons/     ← Bảng đối chiếu
│       ├── queries/         ← Kết quả truy vấn phức tạp
│       ├── synthesis/       ← Tri thức tổng hợp (đã duyệt)
│       ├── decisions/       ← Kết quả từ @wiki-council
│       ├── review_queue/    ← PENDING: Atom chờ duyệt
│       ├── session_insights/ ← Audit log & Insight phiên làm việc
│       └── wiki_brain.db    ← DATABASE: Vector & Graph Index
├── scripts/                ← PRODUCTION: Tooling, Maintenance, Official Tests.
└── scratch/                ← SANDBOX: Debug, Quick tests, One-off scripts.
```

---


## HẠ TẦNG KỸ THUẬT (Infrastructure)
- **Runtime:** Python 3.11 (Core) / Python 3.12 (Sandbox/Harness).
- **Sandbox:** Localsandbox (WASM) + Deno Runtime (Đã kiểm thử thành công).
- **Database:** SQLite 3 (wiki_brain.db).
- **Encoding:** UTF-8 no BOM (Bắt buộc).


## ⚡ GIAO THỨC VẬN HÀNH (Operation Protocols)

### P1 — CHECKPOINT PROTOCOL
- Khai báo trạng thái READY/BLOCKED trước khi thực hiện task phức tạp.

### P2 — VISIBILITY (Safe-Diff Workflow)
- **Tạo mới:** Agent tạo file mồi -> Sửa nội dung để User thấy Diff xanh.
- **Sửa đổi:** Ưu tiên dùng công cụ hiện Diff (UI) cho User review.

### P3 — SAFETY (Encoding Guard)
- BẮT BUỘC hậu kiểm bằng Python cho mọi file có Tiếng Việt.
- Cấm mọi hình thức lỗi font: Unicode Escape, Mojibake, ký tự rác.

### P4 — ISOLATION (Sandbox First)
- BẮT BUỘC chạy code thử nghiệm trong Localsandbox (WASM).

### P5 — SYNC DIRECTION
- **File vật lý là Source of Truth**. Sync từ File vào Database hàng đêm.

### P6 — STAGING-PROMOTE GATE (R22 Enforcement)
- **Mọi Agent** (@scout, @engineer, @pm) tuyệt đối không được tự ý ghi đè file vào `3-resources` thủ công.
- Dữ liệu thô mới phải được xử lý tại `00_Inbox` cho đến khi đạt trạng thái **VERIFIED** (Audit Stamp).
- Chỉ sử dụng `scripts/promote.py` để thăng cấp dữ liệu vào kho lưu trữ chính thức.

## 🛡️ BỘ QUY TẮC QUẢN TRỊ

> **Kiến trúc phân tầng** — Rules được phân bổ theo agent, không nhồi vào một chỗ.
> Chi tiết đầy đủ 27 rules và diễn giải: [[GEMINI.md]]

### Tầng 1 — Constitutional Rules (Mọi agent, mọi lúc)
Xem: `.agent/rules/CORE.md`
- **R1** Raw Immutable | **R2** Proactive Integrity | **R5** Prereq Gate | **R8** Human Supremacy

### Tầng 2 — Agent-Scoped Rules (Chỉ đọc khi là agent đó)

| Agent | File | Rules |
|---|---|---|
| @scout | `.agent/rules/scout.md` | R10, R11, R13, R24, R25 |
| @engineer | `.agent/rules/engineer.md` | R4, R9, R12, R18, R19, R26 |
| @auditor | `.agent/rules/auditor.md` | R3, R20, R21, R27 |
| @librarian | `.agent/rules/librarian.md` | R13, R14, R15, R17, R26 |
| @pm | `.agent/rules/pm.md` | R5, R6, R7, R16 |

### Tầng 3 — Enforcement bằng Code (Không cần Agent nhớ)

| Rule | Enforced bởi |
|---|---|
| R8 Human Supremacy | `synthesis_guard.py check <file>` — BLOCKED nếu write vào `synthesis/` hoặc modify SYNTHESIZED atom |
| R8 Human Approve | `synthesis_guard.py approve <file>` — CHỈ Human gọi để set SYNTHESIZED |
| R22 Staging-Promote | `circuit_breaker.py` chặn write trực tiếp vào `3-resources/` |
| R23 Promotion Gate | `promote.py` là wrapper duy nhất được phép move file |
| R20 YAML Validity | `ingest.py` schema validation — tự reject nếu YAML invalid |
| R14 Log Rotation | `session_seal.py` tự tạo file log đúng tên |

### Tầng 4 — Reference (Tra cứu khi cần, không inject mặc định)
[[GEMINI.md]] — Toàn bộ 27 rules + WikiCouncil 2.0 (Bản đồ Hiến pháp).

---

## R16 — CHECKPOINT PROTOCOL

```yaml
CHECKPOINT:
  agent: "@[tên]"
  task: "[mô tả cụ thể]"
  output_file: "[đường dẫn]"
  prerequisites_ok: "YES | NO"
  status: "READY | BLOCKED"
```
