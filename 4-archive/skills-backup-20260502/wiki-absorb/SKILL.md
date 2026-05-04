---
name: wiki-absorb
description: "TRIGGER: absorb, merge knowledge, reconcile atoms, update synthesis. Hợp nhất các Wiki Atom mới vào các trang Synthesis hiện có. Sử dụng reconciler.py để xử lý mâu thuẫn tri thức và đảm bảo tính nhất quán (Single Source of Truth). Dùng sau khi wiki-ingest hoàn tất."
---

# Wiki Absorb Protocol

Năng lực chuyển hóa tri thức từ dạng Atomic (rời rạc) sang Synthesis (tổng hợp).

## Step 1: Identification
- Xác định các file Atom mới tạo (từ `wiki-ingest`).
- Tìm các trang Synthesis liên quan trong `3-resources/wiki/synthesis/` hoặc `1-projects/`.

## Step 2: Reconciliation (Rule 22)
- Sử dụng `reconciler.py` (hoặc logic suy luận tương đương) để:
  1. So sánh thông tin mới với tri thức cũ.
  2. Phát hiện mâu thuẫn (contradictions).
  3. Hợp nhất thông tin bổ sung mà không làm mất context cũ.
  4. Cập nhật các trích dẫn nguồn (Source Tracing) để bao hàm cả nguồn mới.

## Step 3: Link Density Optimization
- **BẮT BUỘC**: Tạo ít nhất 2-3 wikilinks mới từ nội dung vừa hợp nhất trỏ đến các Concepts/Entities hiện có.
- Đảm bảo mật độ liên kết (Link Density) tăng trưởng sau mỗi lần thực hiện.

## Tooling
```powershell
# Chạy script hợp nhất (khi đã hoàn thiện logic)
python .agent/skills/wiki-absorb/scripts/reconciler.py --input [atoms] --target [synthesis]
```
