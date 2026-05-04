# Kế hoạch Tái cấu trúc Hệ thống Skill (Wiki 2.0)

## 1. Mục tiêu
Đưa toàn bộ năng lực vận hành của hệ thống về chuẩn **7 Lệnh vận hành (Operational Commands)**. Đảm bảo tính nhất quán, tự động hóa cao và tuân thủ tuyệt đối Schema V3.0, đồng thời tích hợp các pattern hiện đại từ các Second Brain Framework hàng đầu.

## 2. Cơ sở Tham chiếu (Benchmarks)
Hệ thống được thiết kế dựa trên các "best practices" từ cộng đồng Claude Code & Second Brain:

| Repo Tham khảo | Insight Chủ chốt | Áp dụng cho Skill |
| :--- | :--- | :--- |
| `eugeniughelbur/obsidian-second-brain` | Pattern `reconciler` xử lý mâu thuẫn tri thức & Dashboard link density. | `wiki-absorb`, `wiki-status` |
| `Ar9av/obsidian-wiki` | Cấu trúc skill sạch, cơ chế Sync Index & Backlinks tự động. | `wiki-ingest`, `wiki-rebuild` |
| `agricidaniel/claude-obsidian` | Giá trị tri thức = **Link Density** (Mật độ liên kết). Audit 8 categories. | `wiki-cleanup`, Core Logic |
| `NicholasSpisak/second-brain` | Luồng Ingest thô (`raw/`) -> Tinh lọc (`wiki/`) đơn giản, hiệu quả. | `wiki-ingest` |

## 3. Kiến trúc 7 Skill Vận hành (Operational Skills)

### Nhóm A: Tiếp nhận & Chuyển hóa (Input/Transform)
1. **`wiki-ingest`** (Ref: `Ar9av` & `NicholasSpisak`):
   - **Logic**: `Raw` -> `Automated Analysis` -> `Atomic Atoms`.
   - **Cải tiến**: Tự động tạo kết nối (links) ngay khi nạp file. Gán Prefix dựa trên Taxonomy (`AIMET_`, `DSML_`...).
2. **`wiki-absorb`** (Ref: `eugeniughelbur`):
   - **Logic**: Hợp nhất Atom mới vào Master Synthesis hiện có.
   - **Tooling**: `reconciler.py`. Xử lý mâu thuẫn (conflicts) giữa thông tin cũ và mới, đảm bảo tính nhất quán của "Sự thật duy nhất" (Single Source of Truth).

### Nhóm B: Khai thác & Truy vấn (Mining/Query)
3. **`wiki-query`** (Ref: `Ar9av` + QMD):
   - **Logic**: Kết hợp Keyword Search (Lexical) + Vector Search (Semantic) + Graph Traversal.
   - **Output**: Trả lời tổng hợp kèm trích dẫn nguồn (Source Tracing) theo Rule 14.
4. **`wiki-breakdown`** (Unique Design):
   - **Logic**: **"Concrete Noun Test"**. Quét nội dung để phát hiện các danh từ riêng/khái niệm chưa có trang Wiki tương ứng.
   - **Mục tiêu**: Chủ động phát hiện "lỗ hổng tri thức" để yêu cầu nghiên cứu bổ sung.

### Nhóm C: Bảo trì & Sức khỏe (Maintenance/Health)
5. **`wiki-cleanup`** (Ref: `agricidaniel`):
   - **Logic**: Audit 8 danh mục chất lượng (Link hỏng, Thiếu nguồn, Trùng lặp, Tone không chuẩn...).
   - **Tooling**: `lint_agent`. Thực hiện "Steve Jobs Test" cho cấu trúc Wiki.
6. **`wiki-status`** (Ref: `eugeniughelbur`):
   - **Logic**: Đo lường **Link Density Index**. Thống kê tỷ lệ file `verified` vs `draft`.
   - **Output**: Visual Dashboard (Bảng trạng thái) về sức khỏe toàn hệ thống.
7. **`wiki-rebuild`** (Ref: `Ar9av`):
   - **Logic**: Tự động hóa việc cập nhật `index.md`, `tags.md` và tệp `_backlinks.json`.
   - **Mục tiêu**: Đảm bảo cấu trúc điều hướng luôn phản ánh đúng dữ liệu thực tế.

## 4. Lộ trình triển khai (Roadmap)

### Giai đoạn 1: Cấu trúc & Metadata (Ưu tiên cao)
- [ ] Thiết lập folder `.agent/skills/` theo chuẩn phẳng, dễ trigger.
- [ ] Chuẩn hóa `SKILL.md` cho 7 lệnh, tích hợp triết lý "Link Density".
- [ ] Cập nhật `AGENTS.md` và `GEMINI.md` để mapping lệnh vận hành.

### Giai đoạn 2: Phát triển Công cụ hỗ trợ
- [ ] Build `reconciler.py` (Dùng cho `wiki-absorb`).
- [ ] Build `noun_miner.py` (Dùng cho `wiki-breakdown`).
- [ ] Hoàn thiện script `wiki-rebuild` để tự động hóa Sync Index.

### Giai đoạn 3: Vận hành Thử nghiệm
- [ ] Chạy chu kỳ: `ingest` -> `absorb` -> `rebuild` -> `status`.
- [ ] Kiểm định mật độ liên kết tăng trưởng sau mỗi lần absorb.

## 5. Rủi ro & Giải pháp
- **Rủi ro**: Quá tải token khi thực hiện `wiki-absorb` trên các tệp Synthesis lớn.
- **Giải pháp**: Sử dụng kỹ thuật "Chunk-based Reconciliation" và cập nhật từng phần (Surgical Updates).

---
**Phê duyệt**: Kế hoạch này được điều chỉnh để tối ưu hóa giá trị của Second Brain thông qua kết nối thay vì lưu trữ thuần túy.
