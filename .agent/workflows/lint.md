---
description: Kiểm tra định kỳ sức khỏe hệ thống Wiki (Karpathy Lint Pattern)
---

Workflow `/lint` thực hiện health-check định kỳ theo Karpathy:
> *"Look for: contradictions between pages, stale claims, orphan pages with no inbound links, important concepts lacking their own page, missing cross-references."*

**Khuyến nghị**: Chạy `/lint` sau mỗi đợt `/ingest` lớn, hoặc ít nhất **1 lần/tuần**.

---

## ⚙️ Các bước kiểm tra (Health Checks)

### Check 1 — Orphan Pages (Trang mồ côi)
**Định nghĩa**: Trang Wiki không được bất kỳ trang nào khác liên kết đến.

```powershell
# Chạy script lint tự động
python scripts/brain_lint.py
```

Nếu script chưa tồn tại, @healer thực hiện thủ công:
- Lấy danh sách tất cả trang từ `brain/WIKI_INDEX.md`.
- Với mỗi trang, tìm xem có trang nào khác chứa `[[Tên_trang]]` không.
- Báo cáo danh sách trang có 0 inbound links.

### Check 2 — Mâu thuẫn (Contradictions)
**Đây là nhiệm vụ của /lint, KHÔNG phải /file-back.**

@auditor thực hiện Reverse Tracing trên các cặp trang có khả năng mâu thuẫn:
- Ưu tiên kiểm tra: Trang được tạo bởi `/file-back` (status: "draft").
- Dấu hiệu: Cùng chủ đề nhưng kết luận trái chiều.
- Kết quả: Ghi rõ mâu thuẫn, đề xuất trang nào cần cập nhật.

### Check 3 — Stale Claims (Nội dung lỗi thời)
- Tìm trang Wiki có `last_updated` cách hiện tại > 30 ngày.
- Kiểm tra: File raw tương ứng có được cập nhật không?
- Nếu có raw mới hơn → đánh dấu trang Wiki là `status: "stale"`.

### Check 4 — Concept Gaps (Khái niệm thiếu trang riêng)
- Quét toàn bộ CONCEPT PAGES tìm [[Wikilinks]] trỏ đến trang CHƯA TỒN TẠI.
- Mỗi link gãy = 1 concept gap cần tạo trang mới.
- Lập danh sách đề xuất cho User quyết định có muốn tạo không.

---

## 📊 Báo cáo Lint (Output chuẩn)

Sau khi hoàn thành, @pm tạo báo cáo theo format:

```markdown
## [YYYY-MM-DD] lint | @pm | Health Check Report
- Orphan pages: X trang → [danh sách]
- Contradictions: X cặp → [danh sách]
- Stale claims: X trang → [danh sách]
- Concept gaps: X links gãy → [danh sách đề xuất]
- Tổng sức khỏe: [HEALTHY / WARNING / CRITICAL]
```

Append vào `brain/log.md` và thông báo tóm tắt cho User.

---

## 🚦 Ngưỡng cảnh báo (Thresholds)

| Chỉ số | HEALTHY | WARNING | CRITICAL |
| :--- | :--- | :--- | :--- |
| Orphan pages | < 5% | 5-15% | > 15% |
| Stale claims | < 10 trang | 10-30 trang | > 30 trang |
| Concept gaps | < 5 links | 5-15 links | > 15 links |

Khi **CRITICAL**: Tự động triệu hồi `@healer` để sửa trước khi tiếp tục ingest mới.

---

## 🔗 Liên kết hệ thống

- Script: `scripts/brain_lint.py`
- Sau Lint: Nếu có orphan pages → `/file-back` để merge insight vào trang hiện có.
- Mâu thuẫn nghiêm trọng → `@auditor` xử lý theo `AUDITOR_Protocol.md`.
