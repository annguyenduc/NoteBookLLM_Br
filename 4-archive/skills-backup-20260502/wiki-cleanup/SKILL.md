---
name: wiki-cleanup
description: "TRIGGER: cleanup, audit wiki, quality check, broken links, source tracing, self-audit. Thực hiện dọn dẹp và kiểm soát chất lượng Wiki NoteBookLLM_Br theo 8 danh mục chuẩn. Dùng để tối ưu hóa link density và bảo trì tính nhất quán của Second Brain. Không dùng để nạp nguồn mới."
---

# Wiki Lint Protocol (Local Version)

This skill overrides the global lint behavior to enforce workspace-specific auditing for NoteBookLLM_Br.

## Step 1: Automated Validation (Rule 21)
Trước khi thực hiện bất kỳ lệnh nào, hãy tự kiểm tra (Self-audit) các file mới nhất vừa được tạo/sửa:
- Đối soát nội dung file với Template tương ứng.
- Kiểm tra tính hợp lệ của YAML Frontmatter.
- Kiểm tra Encoding (Bắt buộc UTF-8 no BOM).

## Step 2: Source Integrity Audit (Rule 10)
**BẮT BUỘC (Rule 10 - Absolute)**: Khi thực hiện reverse tracing, agent (đóng vai `@auditor`) phải:
1. Chỉ trích dẫn từ file có trong `3-resources/raw/` hoặc `3-resources/wiki/synthesis/`.
2. Với mỗi claim, ghi rõ: `Nguồn: [tên file] — [dòng/section cụ thể]`.
3. Nếu không tìm thấy nguồn: → Ghi `[KHÔNG TÌM THẤY NGUỒN]`.

## Step 3: Structural Health Checks
- **Broken Wikilinks**: Link `[[...]]` trỏ đến trang không tồn tại.
- **Orphan Pages**: Trang không có link inbound (ngoại trừ index.md).
- **Index Consistency**: Đảm bảo mọi file `.md` trong `wiki/` đều có mặt trong `index.md`.
- **Rule 17 Compliance**: Kiểm tra mọi trang Concept/Entity có đúng 2 ví dụ (Original + Pedagogical) hay không.

## Severity Ranking
### 🔴 Errors (Must Fix)
- Broken wikilinks.
- Rule 17 violation (thiếu ví dụ đối chiếu).
- Claim thiếu nguồn (`[KHÔNG TÌM THẤY NGUỒN]`).

### 🟡 Warnings (Should Fix)
- Orphan pages.
- Index entries lệch danh mục.
- Stale claims (tri thức cũ so với nguồn mới nạp).

## Report & Action
- Báo cáo số lượng Error/Warning.
- Đề xuất fix cụ thể cho từng mục.
- Ghi log vào `3-resources/wiki/log.md` (PowerShell: thêm `-Encoding UTF8`):
```powershell
python .agent/skills/wiki-lint/scripts/brain_lint.py
```

## Related Rules
- **Rule 10**: Anti-Hallucination Reverse Tracing.
- **Rule 21**: Self-Audit Integrity Loop.
- **AUDITOR_Protocol.md**: Giao thức kiểm định chi tiết.
