# Claude Code Full Course 2026: Build Mastery & Antigravity Audit

Tài liệu này tổng hợp tri thức từ Khóa học Toàn diện Claude Code 2026, tập trung vào kỹ thuật phát triển sản phẩm (Build) và tối ưu hóa hệ thống Automations trong Antigravity.

---

## 🏗️ Module 1: Claude Code Build Mastery (Technical)

Claude Code 2026 không chỉ là một Agentic CLI mà là một **AI OS** cho nhà phát triển.

### 1. Quy trình Setup & Project Architecture
- **Structure**: Luôn giữ `src/` phẳng (flat) cho logic nghiệp vụ, tách biệt hoàn toàn với `scripts/` hỗ trợ.
- **Metadata**: Sử dụng các file `.claude-code/config.json` để định nghĩa bối cảnh dự án (Project Context) mà không làm loãng codebase.
- **TDD (Test-Driven Development)**:
    - Sử dụng lệnh `claude test` để agent tự động viết và sửa unit tests cho đến khi đạt pass rate 100%.
    - **Pattern**: Red (Viết test lỗi) -> Green (Agent code để pass) -> Refactor (Agent tối ưu hóa code).

### 2. Kỹ thuật "Build" tăng tốc
- **Context Pinning**: Ghim các file định nghĩa kiến trúc quan trọng (như `CLAUDE.md`) vào bộ nhớ làm việc.
- **Safe Replace**: Sử dụng cơ chế `search & replace` tích hợp kiểm định (Verification Pass) thay vì ghi đè file mù quáng.

---

## 🧠 Module 2: Second Brain (LOM v3.5)

Kiến trúc bộ nhớ tối ưu cho Agent vận hành trường kỳ.

### 1. Cấu trúc Indexing
- **Map of Content (MOC)**: Tạo các tệp `_index.md` tại mỗi thư mục con để định tuyến Agent.
- **Atomic Notes**: Mỗi tệp tri thức trong `brain/distilled/` chỉ nên giải quyết một chủ đề duy nhất (độ dài lý tưởng < 1500 token).

### 2. Linking & Discovery
- **WikiLinks**: Luôn sử dụng `[[Tên File]]` để tạo mạng lưới liên kết.
- **Graph Metadata**: Thêm metadata vào đầu file `.md` để hỗ trợ các công cụ Graphify phân cụm tri thức tốt hơn.

---

## 🤖 Module 3: Antigravity Automation Framework (Audit)

Bản đối chiếu Knowledge Gap giữa lý thuyết khóa học và hệ thống thực tế.

| Hạng mục | Lý thuyết Claude Code 2026 | Hiện trạng Antigravity v3.0 | Đánh giá | Đề xuất (v3.5) |
| :--- | :--- | :--- | :--- | :--- |
| **Agent Meta** | Có `latency_target`, `token_budget` | Chỉ có `Kỹ năng`, `Trọng tâm` | ⚠️ Thiếu định lượng | Thêm `budget` vào `AGENTS.md` |
| **Self-Healing** | Tự động triệu hồi `@healer` khi lỗi | USER phải ra lệnh hoặc Agent tự làm thủ công | ⚠️ Chậm | Thêm Rule: `AUTO_HEAL_ON_ERROR = True` |
| **Skill Audit** | Mỗi Skill phải có `Audit-ID` định danh | Chỉ có `name`, `version`, `description` | ⚠️ Khó kiểm định | Thêm `audit_id` vào YAML frontmatter |
| **Swarm Sync** | Sử dụng `Context Handoff` protocol | Sử dụng Continuity file | ✅ Tương đồng | Tối ưu hóa file `CONTINUITY.md` thành cấu trúc JSON |

---

## 🛠️ Action Plan cho Antigravity v3.5
1. **Chuẩn hóa Skill**: Cập nhật toàn bộ tệp trong `skills/` để bao gồm meta-data kiểm định.
2. **Nâng cấp AGENTS.md**: Thêm các quy tắc tự phục hồi (Self-Healing) tự động.
3. **Triển khai MOC**: Tạo tệp `brain/_index.md` để Agent điều hướng nhanh hơn.

---
*Chưng cất bởi @pm | Nguồn: Khóa học Toàn diện Claude Code 2026 | Standard: LOM v3.5*
