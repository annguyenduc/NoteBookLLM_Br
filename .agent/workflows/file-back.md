---
description: Tự động lưu kết quả phân tích có giá trị thành Wiki page mới (Karpathy File-Back Pattern)
---

Workflow `/file-back` hiện thực hóa nguyên tắc "Query Compounding" của Karpathy:
> *"Good answers can be filed back into the wiki as new pages. These are valuable and shouldn't disappear into chat history."*

---

## 🎯 Triggers (Khi nào kích hoạt)

Agent **tự động** thực hiện File-Back khi đáp ứng **bất kỳ điều kiện nào** sau đây:

| # | Trigger | Dấu hiệu nhận biết |
| :--- | :--- | :--- |
| **T1** | Agent tổng hợp **2+ trang Wiki** để trả lời 1 câu hỏi | Đọc ≥2 file trong `brain/wiki/` trong cùng 1 lượt phản hồi |
| **T2** | Agent tạo ra **bảng so sánh** hoặc **phân tích đối chiếu** mới | Response chứa bảng Markdown với ≥2 cột so sánh và thông tin không có trong wiki đơn lẻ nào |

**Không** kích hoạt File-Back khi:
- Câu trả lời chỉ lặp lại nội dung của 1 trang Wiki duy nhất.
- Response là debug, sửa lỗi kỹ thuật, hoặc điều hướng hệ thống.
- Sau khi thực hiện "Judgment" (bước dưới), phát hiện insight đã tồn tại trong Index.

> [!NOTE]
> **Không dùng**: Phát hiện mâu thuẫn → đây là nhiệm vụ của `/lint`, không phải File-Back.
> **Không dùng**: Đợi User xác nhận từ khóa → mục tiêu là hệ thống tự vận hành.

---

## 🧠 Judgment Process (Phán xét nội tại — bắt buộc trước khi ghi)

Trước khi tạo trang mới, Agent **bắt buộc** thực hiện 2 câu hỏi sau:

**Câu hỏi 1**: *"Nội dung tôi vừa tổng hợp có tạo ra một insight KHÔNG có trong bất kỳ trang nào tôi đã đọc không?"*
- Nếu **Không** (chỉ là tóm tắt lại) → **Dừng. Không File-Back.**
- Nếu **Có** → Tiếp tục Câu hỏi 2.

**Câu hỏi 2**: *"Insight này đã được lưu trong WIKI_INDEX chưa?"*
- Đọc **section CONCEPT PAGES** của `brain/WIKI_INDEX.md` (chỉ đọc section này, không cần đọc toàn bộ file).
- Tìm trang có title/summary tương tự với insight vừa tạo ra.
- Nếu **đã có** → Cập nhật trang hiện tại (update), không tạo mới.
- Nếu **chưa có** → Tiếp tục tạo trang mới.

---

## ⚙️ Quy trình thực thi (Execution Flow)

Sau khi Judgment xác nhận "insight mới", Agent thực hiện **trong cùng lượt phản hồi**:

### Bước 1: Đặt tên trang
- Tên file: `WIKI_[PREFIX]_[Tên_chủ_đề].md` theo chuẩn Rule 7.
- Ví dụ: `WIKI_ROBOT_Sensor_Comparison.md`, `WIKI_PROMPT_K10_Vector_Exercises.md`

### Bước 2: Tạo nội dung với template chuẩn
```yaml
---
file_id: "[ID]"
title: "[Tiêu đề phân tích]"
category: "File-Back Insight"
tags: ["[tag1]", "[tag2]"]
source: "Chat synthesis — [ngày]"
trigger: "[T1|T2]"
status: "draft"
created: "[YYYY-MM-DD]"
---
```
Thêm nội dung phân tích + [[Wikilinks]] đến các trang đã đọc.

### Bước 3: Ghi file và log
```
write_to_file("brain/wiki/WIKI_[PREFIX]_[Tên].md", content)
Append("brain/log.md", "## [YYYY-MM-DD HH:MM] file-back | @[agent] | [Tên trang]")
```

### Bước 4: Thông báo cho User (1 dòng)
> 📁 **File-Back [T1/T2]**: Đã lưu → [`WIKI_[Tên].md`](file:///d:/NoteBookLLM_Br/brain/wiki/WIKI_[Tên].md)

---

## 🔗 Liên kết hệ thống

- Triết lý gốc: `llm-wiki.md` dòng 39 — *"Query Compounding"*.
- Kiểm tra trùng lặp: `brain/WIKI_INDEX.md` → section **CONCEPT PAGES** (36 trang, scan nhanh).
- Dọn dẹp định kỳ: `/lint` — phát hiện mâu thuẫn và trang dư thừa sau File-Back.
