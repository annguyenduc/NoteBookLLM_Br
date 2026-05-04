---
name: wiki-breakdown
description: "TRIGGER: breakdown, knowledge gap, noun test, analyze concepts. Phân tích nội dung Wiki để phát hiện các lỗ hổng tri thức (Knowledge Gaps). Sử dụng 'Concrete Noun Test' để tìm các khái niệm chưa được định nghĩa. Dùng để lập kế hoạch nghiên cứu bổ sung."
---

# Wiki Breakdown Protocol

Năng lực phát hiện "những gì chúng ta chưa biết" (Uncovering Unknowns).

## Step 1: Concrete Noun Test
- Quét các trang Wiki mục tiêu (hoặc toàn bộ vault).
- Trích xuất các danh từ riêng, thuật ngữ kỹ thuật, hoặc tên tổ chức/hệ thống.
- Đối soát với danh sách file trong `3-resources/wiki/concepts/` và `3-resources/wiki/entities/`.

## Step 2: Gap Assessment
- Liệt kê các thuật ngữ xuất hiện nhiều lần nhưng chưa có trang Wiki riêng (Missing Atoms).
- Đánh giá mức độ ưu tiên dựa trên tần suất xuất hiện và tầm quan trọng đối với dự án hiện tại.

## Step 3: Recommendation
- Đề xuất danh sách các trang Wiki cần tạo mới.
- Gợi ý các nguồn (sources) tiềm năng để thực hiện `wiki-ingest` bổ sung.

## Tooling
```powershell
# Chạy script tìm danh từ (khi đã hoàn thiện logic)
python .agent/skills/wiki-breakdown/scripts/noun_miner.py --path [directory]
```
