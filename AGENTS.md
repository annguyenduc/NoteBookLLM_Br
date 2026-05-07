# AGENTS.md — NoteBookLLM_Br

> Đọc file này TRƯỚC KHI thực hiện bất kỳ tác vụ nào.
> Mục tiêu hệ thống: Second brain theo mô hình LLM Wiki — ingest tài liệu thô → atomic wiki nodes → synthesis có thể verify nguồn.

---

## STARTUP (Bắt buộc mỗi phiên)

1. Đọc `AGENTS.md`, `GEMINI.md` (Hiến pháp), `SOUL.md`, `USER.md` và `WORKSPACE_OVERVIEW.md`
2. Khai báo CHECKPOINT (xem cuối file) trước khi bắt đầu task
3. Ghi log vào file nhật ký tháng hiện tại trong `3-resources/wiki/logs/` sau khi hoàn thành

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

---

## CẤU TRÚC THƯ MỤC

```
NoteBookLLM_Br/              ← root
│
├── AGENTS.md                ← root level
├── GEMINI.md                ← Hiến pháp tối cao (R1-R18)
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
└── scripts/
```

---

## 🛡️ BỘ QUY TẮC QUẢN TRỊ (R1-R18)
> Codex/Antigravity BẮT BUỘC tuân thủ. Chi tiết kỹ thuật & Template tại [[GEMINI.md]].

| Rule | Tên Luật | Hành vi BẮT BUỘC / CẤM | Chi tiết |
|---|---|---|---|
| **R1** | Raw Immutable | CẤM sửa/xóa trong `3-resources/raw_*/`. | [[GEMINI.md#R1]] |
| **R2** | No Fake Report | CẤM báo cáo ảo khi chưa có tool call thành công. | [[GEMINI.md#R2]] |
| **R3** | Source Tracing | Mọi claim phải có Nguồn rõ ràng. | [[GEMINI.md#R3]] |
| **R4** | Safe Logging | Ghi log bằng Python (UTF-8). CẤM PowerShell. | [[GEMINI.md#R4]] |
| **R5** | Prereq Gate | Kiểm tra Trainer Profile/Design trước khi chạy. | [[GEMINI.md#R5]] |
| **R9** | Surgical Min | Chỉ thay đổi code tối thiểu (Surgical Changes). | [[GEMINI.md#R9]] |
| **R10** | 3-Step Search | Tìm kiếm -> Xác thực (MD) -> Chụp ảnh (Screenshot). | [[GEMINI.md#R10]] |
| **R12** | Encoding Safety | Mọi file Tiếng Việt phải là UTF-8 no BOM. | [[GEMINI.md#R12]] |
| **R14** | Log Rotation | Log phân mảnh theo ngày: `log_YYYY_MM_DD.md`. | [[GEMINI.md#R14]] |
| **R16** | Checkpoint | Khai báo trạng thái (READY/BLOCKED) trước task. | [[GEMINI.md#R16]] |
| **R17** | Sync Direction | File vật lý là Source of Truth. | [[GEMINI.md#R17]] |
| **R18** | Mandat. Examples | BẮT BUỘC đối soát với [[EXAMPLES.md]]. | [[GEMINI.md#R18]] |

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
