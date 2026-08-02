---
name: wiki-md-auditor
description: "Dùng khi cần đánh giá chất lượng Markdown, sửa lỗi font (ligatures), và chuẩn hóa tên asset trước khi promote vào raw_ingest/. BẮT BUỘC tuân thủ TDD."
---

# Kiểm Duyệt Markdown (MD Auditor)

## Vai Trò
Quality Gate tại `00_Inbox` — chỉ cho phép file Markdown sạch và chuẩn hóa đi vào hệ thống wiki chính thức.

## Quy Tắc Bắt Buộc
- **Cổng bất biến**: Không bao giờ promote file có điểm chất lượng < 90% hoặc link ảnh bị hỏng
- **Chuẩn prefix**: Mọi asset phải đổi tên theo dạng `TENFILE_fig_01.png`
- **Tuân thủ 3-Flatten**: Asset phải chuyển vào thư mục `raw_assets/` phẳng
- **An toàn promote**: Không chạy `promote.py` nếu chưa có dấu PASSED
- **Dry-run trước**: Luôn chạy `--dry-run` trước khi promote thật

## Cấu Trúc Audit Stamp
```yaml
audit:
  score: 0.95        # điểm thực tế (tối đa 1.0)
  date: "YYYY-MM-DD"
  status: "PASSED"   # hoặc FAILED
  auditor: "v1.0"
```
> `promote.py` sẽ từ chối file có `status != PASSED` hoặc `date` quá 7 ngày.

## Quy Trình

**Bước 1 — Audit & Fix:**
```powershell
python scripts/maintenance/md_auditor.py "00_Inbox/Converted_Sources/XXX/RAW_XXX.md" --fix
```
Output: chuẩn hóa link, copy asset vào `raw_assets/`, ghi Audit Stamp vào frontmatter.

**Bước 2 — Promote:**
```powershell
# Xem trước
python scripts/maintenance/circuit_breaker.py promote "00_Inbox/Converted_Sources/XXX/RAW_XXX.md" --dry-run
# Thực thi
python scripts/maintenance/circuit_breaker.py promote "00_Inbox/Converted_Sources/XXX/RAW_XXX.md"
```
Output: file `.md` → `raw_ingest/`, PDF gốc → `raw_sources/`, thư mục tạm bị xóa.

## Chạy Test
```powershell
$env:PYTHONPATH=".agent/skills/wiki-md-auditor/scripts"
python .agent/skills/wiki-md-auditor/tests/test_md_auditor.py
python .agent/skills/wiki-md-auditor/tests/test_promote.py
```