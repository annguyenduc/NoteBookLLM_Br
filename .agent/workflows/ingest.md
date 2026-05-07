---
description: Quy trình chuẩn nạp dữ liệu mới vào hệ thống Wiki (Karpathy Ingest Pattern)
---

Workflow `/ingest` chuẩn hóa cách tiếp nhận một nguồn dữ liệu mới và tích hợp nó vào Wiki.
Karpathy: *"A single source might touch 10-15 wiki pages."*

---

## ✅ CHECKPOINT (Bắt buộc trước khi bắt đầu)

```yaml
CHECKPOINT:
  agent: "@scout"
  task: "Phân tích [tên_file] và tạo Analysis draft"
  step: "1 / 4"
  output_file: "1-projects/[Project]/Analysis_[PREFIX]_[tên_file].md"
  stop_condition: "Sau khi tạo xong Analysis file và chờ user duyệt"
  prerequisites:
    - file: "3-resources/raw_sources/[tên_file]"
      exists: "YES | NO"
    - file: ".agent/skills/wiki-ingest/resources/WIKI_AGENT_GUIDE.md"
      exists: "YES | NO"
    - file: ".agent/skills/wiki-ingest/resources/SOURCE_TEMPLATE.md"
      exists: "YES | NO"
  status: "READY | BLOCKED"
  blocked_reason: ""
```

Nếu file nguồn KHÔNG tồn tại trong `raw/sources/` → **DỪNG**, báo user, KHÔNG tiếp tục.

---

## 📋 Điều kiện tiên quyết (Prerequisites)

**Auto-detect** (nếu `/ingest` không có tham số):
1. List tất cả files trong `3-resources/raw_sources/` hoặc `3-resources/raw_ingest/`
2. So sánh với các `ingest` entries trong `3-resources/wiki/log.md`
3. Files chưa xuất hiện trong log = chưa ingest → báo cáo danh sách cho user chọn

Trước khi chạy `/ingest [file]`, kiểm tra:
- [ ] File nguồn đã được đặt vào `3-resources/raw_sources/` hoặc `3-resources/raw_ingest/` (Rule 1 — chỉ User mới được thêm vào raw_*/).
- [ ] File đặt tên đúng chuẩn: `[PREFIX]_[TÊN].md` theo Rule 7 (Snake_Case, Prefix 2 cấp).
- [ ] Không file nào trong `3-resources/raw_*/` bị ghi đè.

---

## ⚙️ Các bước thực hiện (Flow cố định)

### Bước 1 (Analysis) — @scout: Đọc và Phân tích cấu trúc (Structured Analysis)

**Đọc trước khi làm:**
- `.agent/skills/wiki-ingest/resources/WIKI_AGENT_GUIDE.md` — quy tắc tạo atoms
- `3-resources/wiki/index.md` — kiểm tra concept đã tồn tại chưa (tránh duplicate)
- `3-resources/purpose.md` — định hướng wiki (ưu tiên sư phạm K-12)

Tạo file `1-projects/[Project_Name]/Analysis_[PREFIX]_[tên_file].md` theo cấu trúc:

```markdown
# Analysis: [Tên file gốc]
**Nguồn**: `3-resources/raw_sources/[tên_file]` hoặc `3-resources/raw_ingest/[tên_file]`
**Phân tích bởi**: @scout | **Ngày**: YYYY-MM-DD

## Mining Stats
| Chỉ số | Số lượng |
|:---|:---:|
| Key Concepts phát hiện | N |
| Entities phát hiện | N |
| Connections với wiki hiện tại | N |
| Atoms đề xuất tạo mới | N |

## Tóm tắt cốt lõi
3-5 key takeaways quan trọng nhất.

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

## Mâu thuẫn (Contradictions & Tensions)
Chỉ ra sự khác biệt/xung đột với kiến thức đã có.

## Master Files cần bồi đắp (Rule 3)
- `wiki/synthesis/[file].md` — section nào cần update

## Câu hỏi đào sâu (Deep Research Queries)
Đề xuất các từ khóa/câu hỏi để bổ sung chỗ hổng kiến thức.

## ⏸️ CHỜ USER DUYỆT
- ✅ Approve toàn bộ → gõ `/ingest-execute`
- ✏️ Chỉnh sửa danh sách → edit file này rồi gõ `/ingest-execute`
- ❌ Hủy → gõ `/ingest-cancel`
```

**DỪNG TẠI ĐÂY — chờ user duyệt.**

### Bước 2 (Generation) — @engineer: Khởi tạo & Bồi đắp Wiki (Wiki Generation)

**CHECKPOINT bắt buộc trước Bước 2:**
```yaml
CHECKPOINT:
  agent: "@engineer"
  task: "Viết Wiki Atoms từ Analysis_[tên_file].md"
  step: "2 / 4"
  prerequisites:
    - file: "1-projects/[Project]/Analysis_[PREFIX]_[tên_file].md"
      exists: "YES"
    - file: ".agent/skills/wiki-ingest/resources/SOURCE_TEMPLATE.md"
      exists: "YES"
  status: "READY"
```

Dựa trên bản phân tích đã được duyệt, `@engineer` tiến hành sinh file:
1. **Đọc lại file nguồn gốc** trong `raw_sources/` hoặc `raw_ingest/` — KHÔNG dùng từ Analysis file (Rule 14).
2. **Tạo trang Source**: Tạo `3-resources/wiki/sources/SOURCE_[PREFIX].md` (chứa source summary, frontmatter type/title/sources).
3. **Tạo/Cập nhật trang Khái niệm & Thực thể**:
   - Khởi tạo các trang trong `3-resources/wiki/concepts/` và `3-resources/wiki/entities/` theo chuẩn `WIKI_TEMPLATE.md`.
   - **BẮT BUỘC (Rule 17)**: Mỗi trang phải có khối `## Ví dụ đối chiếu (Rule 17: Double Examples)` với đúng 2 ví dụ: gốc từ sách + ứng dụng sư phạm.
   - **BẮT BUỘC (Rule 2)**: Tối thiểu 2 `[[wikilinks]]` đến pages khác.
   - Đảm bảo có Cross-references (liên kết chéo) giữa các trang.
4. **Bồi đắp Master (Direct Compounding)**: Cập nhật trực tiếp kiến thức mới vào các Master pages trong `3-resources/wiki/synthesis/`.
5. **Review Items**: Trình bày danh sách các điểm cần User/con người đánh giá lại (human judgment).

**Sau mỗi atom được tạo — WRITE REPORT bắt buộc (Rule 18)**:
```
WRITE REPORT:
  file: "3-resources/wiki/[layer]/[TênAtom].md"
  operation: "create | patch"
  added: "[tóm tắt 1 câu]"
  removed: "NONE"
```

### Bước 3 — @librarian: Cập nhật Index & Tổng hợp
```powershell
/rebuild
```
Cập nhật `3-resources/wiki/index.md` và `overview.md` để phản ánh các trang mới.

### Bước 4 — @pm: Ghi log
Append vào `3-resources/wiki/log.md`:
```
## [YYYY-MM-DD HH:MM] ingest | @pm | [Tên file raw]
- Atomic Files: [danh sách N file wiki]
- Master Compounded: [danh sách M file synthesis]
- Số concept: [X]
```

---

## 🔴 Quy tắc bất biến (Non-negotiable Rules)

- **Raw là bất biến**: Tuyệt đối không sửa file trong `3-resources/raw/` (Rule 12).
- **Source Integrity**: Mọi claim trong Wiki PHẢI trích dẫn nguồn từ file raw (Rule 14).
- **Không hallucinate**: Nếu không tìm thấy trong raw → ghi `[KHÔNG TÌM THẤY NGUỒN]`, báo @auditor.
- **@auditor** luôn là chốt chặn cuối: Review ít nhất 20% trang mới tạo sau mỗi đợt ingest lớn.

---

## 🚦 Quality Gate (Red Flags)

- ❌ @engineer bắt đầu Bước 2 khi chưa có duyệt từ user
- ❌ Viết atom mà không mở file raw gốc (vi phạm Rule 14)
- ❌ Atom thiếu Double Examples (vi phạm Rule 17)
- ❌ Atom có < 2 wikilinks (vi phạm Rule 2)
- ❌ Báo cáo "Đã tạo" mà chưa có tool call thực thi (vi phạm Rule 15)
- ❌ Ghi vào `raw/sources/` (vi phạm Rule 12)
- ⚡ Benchmark: Ít hơn 5 trang/nguồn = phân tích chưa đủ sâu. Mục tiêu: 10-15 trang.
- 🔄 Prefer update: Chỉ tạo trang mới khi chủ đề chưa có trang nào phù hợp.

---

## 🔗 Liên kết hệ thống

- Template phân tích: `3-resources/wiki/sources/` (Sử dụng làm đầu vào)
- Template Wiki: `.agent/skills/wiki-ingest/resources/`
- Kiểm tra sức khỏe sau ingest: `/lint` (Sẽ cập nhật quy trình `/cleanup`)
- Triggers: `/ingest [file]` | `/ingest` (auto-detect) | `/ingest-execute` (sau duyệt) | `/ingest-cancel`
