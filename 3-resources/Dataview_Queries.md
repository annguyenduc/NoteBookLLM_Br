---
file_id: "DATAVIEW_QUERIES"
title: "Bộ truy vấn Dataview cho Wiki NoteBookLLM_Br"
type: synthesis
status: VERIFIED
created: "2026-04-29"
last_updated: "2026-05-14"
---

# 🔍 Dataview Queries — NoteBookLLM_Br (v2.0)

> **Hướng dẫn dùng**: File này chứa các truy vấn động để tổng hợp tri thức từ thư mục `3-resources/wiki/`. Dữ liệu sẽ tự động cập nhật khi bạn tạo hoặc sửa các Atoms.

---

## 📋 1. Review Queue (Status: DRAFT)
*Các trang mới ingest hoặc đang chờ kiểm định.*

```dataview
TABLE 
    title AS "Tiêu đề", 
    type AS "Loại", 
    source_file AS "Nguồn gốc", 
    last_reconciled AS "Cập nhật"
FROM "3-resources/wiki"
WHERE icontains(status, "draft")
SORT last_reconciled DESC
```

---

## ✅ 2. Tri thức đã xác thực (Status: VERIFIED)
*Kho tri thức tin cậy đã qua kiểm định.*

```dataview
TABLE 
    title AS "Tiêu đề", 
    type AS "Loại", 
    tags AS "Tags"
FROM "3-resources/wiki"
WHERE icontains(status, "verified") OR icontains(status, "synthesized")
SORT type ASC, title ASC
```

---

## 💡 3. Nhật ký làm việc (Session Insights)
*Các bài học và ghi chép hệ thống rút ra từ mỗi phiên.*

```dataview
TABLE 
    title AS "Nội dung Insight", 
    last_reconciled AS "Ngày ghi",
    tags AS "Tags"
FROM "3-resources/wiki/session_insights"
SORT last_reconciled DESC
```

---

## 📚 4. Thống kê theo Nguồn (Provenance Tracking)
*Xem mỗi nguồn tài liệu đã đóng góp bao nhiêu Atoms.*

```dataview
TABLE 
    length(rows) AS "Số lượng Atoms",
    rows.file.link AS "Danh sách Atoms"
FROM "3-resources/wiki"
WHERE source_file != null
GROUP BY source_file
SORT length(rows) DESC
```

---

## 📊 5. Dashboard — Tổng quan hệ thống
*Bản đồ mật độ tri thức theo từng phân loại.*

```dataview
TABLE WITHOUT ID
    type AS "Phân loại tri thức",
    length(rows) AS "Số lượng",
    choice(type = "concept", "🧠", choice(type = "insight", "💡", choice(type = "synthesis", "🧱", "📄"))) AS "Icon"
FROM "3-resources/wiki"
WHERE type != null
GROUP BY type
SORT length(rows) DESC
```

---

## 🔗 6. Nhóm Tư duy Hệ thống (Systems Thinking)
*Lọc các khái niệm có tag systems_thinking.*

```dataview
TABLE 
    title AS "Khái niệm", 
    status AS "Trạng thái", 
    source_ref AS "Tham chiếu"
FROM "3-resources/wiki"
WHERE contains(tags, "systems_thinking")
SORT title ASC
```

---

## ⚠️ 7. Cảnh báo: Tri thức "nguội" (Stale Content)
*Các bản nháp chưa được động đến trên 30 ngày.*

```dataview
TABLE 
    title AS "Tiêu đề", 
    last_reconciled AS "Cập nhật lần cuối"
FROM "3-resources/wiki"
WHERE date(last_reconciled) < date(today) - dur(30 days)
  AND icontains(status, "draft")
SORT last_reconciled ASC
```

---

> 💡 **Mẹo vận hành**:
> - Dùng lệnh `/status` của Antigravity để xem báo cáo sức khỏe chi tiết hơn (Link Density).
> - Nếu một file không hiện ở đây, hãy kiểm tra xem nó đã có đủ khối `---` frontmatter ở đầu file chưa.
