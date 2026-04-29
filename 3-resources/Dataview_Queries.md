---
file_id: "DATAVIEW_QUERIES"
title: "Bộ truy vấn Dataview cho Wiki NoteBookLLM_Br"
category: "System"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# 🔍 Dataview Queries — NoteBookLLM_Br

> **Hướng dẫn dùng**: Cài plugin **Dataview** trong Obsidian (Settings → Community Plugins → Tìm "Dataview" → Enable). Mỗi block `dataview` dưới đây sẽ tự động render thành bảng khi mở file này trong Obsidian.

---

## 📋 1. Tất cả trang cần Review (status: draft)

```dataview
TABLE title AS "Tên trang", source AS "Nguồn", last_updated AS "Cập nhật lần cuối"
FROM "3-resources/wiki"
WHERE status = "draft"
SORT last_updated DESC
```

---

## ✅ 2. Các trang đã xác thực (status: verified)

```dataview
TABLE title AS "Tên trang", category AS "Loại", source AS "Nguồn"
FROM "3-resources/wiki"
WHERE status = "verified"
SORT title ASC
```

---

## 📚 3. Tiến độ Ingest theo Nguồn sách

```dataview
TABLE rows.file.link AS "Các trang Wiki", length(rows) AS "Số trang"
FROM "3-resources/wiki"
WHERE source != null
GROUP BY source
SORT length(rows) DESC
```

---

## 🏷️ 4. Phân loại theo Tag

```dataview
TABLE rows.title AS "Trang", rows.status AS "Trạng thái"
FROM "3-resources/wiki"
WHERE tags != null
FLATTEN tags AS tag
GROUP BY tag
SORT length(rows) DESC
```

---

## 🗺️ 5. Tất cả trang Summary (Nguồn sách đã Ingest)

```dataview
TABLE title AS "Tên sách", last_updated AS "Ngày hoàn tất"
FROM "3-resources/wiki"
WHERE category = "Source Summary"
SORT last_updated DESC
```

---

## 🏢 6. Tất cả trang Entity

```dataview
TABLE title AS "Thực thể", last_updated AS "Cập nhật"
FROM "3-resources/wiki"
WHERE category = "Entity Page"
SORT title ASC
```

---

## 🆕 7. Trang mới nhất (7 ngày gần nhất)

```dataview
TABLE title AS "Tên trang", category AS "Loại", created AS "Ngày tạo"
FROM "3-resources/wiki"
WHERE date(created) >= date(today) - dur(7 days)
SORT created DESC
```

---

## 📊 8. Dashboard — Tổng quan toàn Wiki

```dataview
TABLE WITHOUT ID
  "**Wiki Pages**" AS "Loại",
  length(rows) AS "Số lượng"
FROM "3-resources/wiki"
GROUP BY category
SORT length(rows) DESC
```

---

## 🔗 9. Trang THINK — Nhóm tư duy phân tích

```dataview
TABLE title AS "Công cụ", status AS "Trạng thái", source AS "Nguồn"
FROM "3-resources/wiki"
WHERE contains(file.name, "THINK")
SORT file.name ASC
```

---

## ⚠️ 10. Cảnh báo: Trang tạo từ lâu chưa update (30+ ngày)

```dataview
TABLE title AS "Tên trang", last_updated AS "Cập nhật lần cuối"
FROM "3-resources/wiki"
WHERE date(last_updated) < date(today) - dur(30 days)
  AND status = "draft"
SORT last_updated ASC
```

---

## 📖 Distilled Master Pages

```dataview
TABLE title AS "Tên trang", last_updated AS "Cập nhật"
FROM "3-resources/distilled"
SORT last_updated DESC
```

---

> 💡 **Mẹo cho người mới dùng Obsidian**:
> - Nhấn `Ctrl + P` → gõ "Graph" → mở **Graph View** để xem toàn bộ mạng lưới liên kết.
> - Trong Graph View, tắt filter "Existing files only" để thấy các trang được **nhắc đến qua Wikilinks nhưng chưa được tạo** (node màu đỏ/xám).
> - Dùng **Local Graph** (click phải vào tab bất kỳ) để xem kết nối của từng trang Wiki riêng lẻ.
