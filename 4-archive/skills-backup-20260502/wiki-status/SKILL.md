---
name: wiki-status
description: "TRIGGER: status, dashboard, health metrics, link density, wiki stats. Báo cáo tình trạng sức khỏe và sự tăng trưởng của Wiki NoteBookLLM_Br. Tập trung vào chỉ số Link Density và trạng thái xác thực nguồn."
---

# Wiki Status Protocol

Năng lực đo lường "sức mạnh" của Second Brain.

## Key Metrics
1. **Link Density Index (LDI)**: Trung bình số lượng wikilinks trên mỗi trang. (Mục tiêu: > 3.0).
2. **Verification Rate**: Tỷ lệ phần trăm các file có tag `#verified` hoặc được Auditor phê duyệt.
3. **Atomic Balance**: Tỷ lệ Concepts vs Entities vs Sources.
4. **Growth Velocity**: Số lượng Atom mới được tạo/hợp nhất trong tuần.

## Step 1: Scan
- Quét toàn bộ thư mục `3-resources/wiki/`.
- Tính toán các chỉ số dựa trên metadata và nội dung file.

## Step 2: Reporting
- Hiển thị bảng Dashboard trạng thái.
- Cảnh báo nếu các chỉ số sức khỏe đi xuống (ví dụ: Link Density giảm).

## Tooling
```powershell
# Hiển thị dashboard sức khỏe (khi đã hoàn thiện logic)
python .agent/skills/wiki-status/scripts/health_dashboard.py
```
