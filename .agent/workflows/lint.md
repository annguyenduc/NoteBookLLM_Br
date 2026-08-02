---
description: Kiểm tra định kỳ sức khỏe hệ thống Wiki (Karpathy Lint Pattern)
---

Workflow `/lint` thực hiện health-check định kỳ theo Karpathy:
> *"Look for: contradictions between pages, stale claims, orphan pages with no inbound links, important concepts lacking their own page, missing cross-references."*

---

## ✅ CHECKPOINT (Bắt buộc trước khi bắt đầu)

```yaml
CHECKPOINT:
  orchestrator: "@pm"        # lập kế hoạch, khai báo CHECKPOINT, tổng hợp báo cáo cuối
  auditor: "@auditor"        # thực hiện các health checks (Check 1–4)
  task: "Thực hiện Health Check (Lint) cho Wiki"
  prerequisites:
    - file: "3-resources/wiki/index.md"
      exists: "YES"
  status: "READY"
```

---

**Khuyến nghị**: Chạy `/lint` sau mỗi đợt `/ingest` lớn, hoặc ít nhất **1 lần/tuần**.

---

## ⚙️ Các bước kiểm tra (Health Checks)

### Check 1 — Orphan Pages (Trang mồ côi)
**Định nghĩa**: Trang Wiki không được bất kỳ trang nào khác liên kết đến.

```powershell
/cleanup
```

Nếu lệnh `/cleanup` gặp lỗi, @auditor thực hiện thủ công:
- Lấy danh sách tất cả trang từ `3-resources/wiki/index.md`.
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

Sau khi @auditor hoàn thành checks, @pm tổng hợp báo cáo theo format:

```markdown
## [YYYY-MM-DD] lint | @pm | Health Check Report
- Orphan pages: X trang → [danh sách]
- Contradictions: X cặp → [danh sách]
- Stale claims: X trang → [danh sách]
- Concept gaps: X links gãy → [danh sách đề xuất]
- Tổng sức khỏe: [HEALTHY / WARNING / CRITICAL]
```

Append vào `3-resources/wiki/logs/log_YYYY_MM_DD.md` nếu User đã duyệt ghi log; nếu không, chỉ báo cáo trong chat.

---

## 🚦 Ngưỡng cảnh báo (Thresholds)

| Chỉ số | HEALTHY | WARNING | CRITICAL |
| :--- | :--- | :--- | :--- |
| Orphan pages | < 5% | 5-15% | > 15% |
| Stale claims | < 10 trang | 10-30 trang | > 30 trang |
| Concept gaps | < 5 links | 5-15 links | > 15 links |

Khi **CRITICAL**: @pm báo BLOCKER, đề xuất gọi `@healer`, và dừng để chờ AN GO. Không tự động sửa, rollback, move/delete, hoặc patch file.

---

## 🔗 Liên kết hệ thống

- Skill vận hành: `wiki-cleanup` (Kích hoạt qua `/cleanup`)
- Sau Lint: Nếu có orphan pages → cân nhắc merge insight hoặc xóa.
- Mâu thuẫn nghiêm trọng → `@auditor` xử lý qua `/council`.
