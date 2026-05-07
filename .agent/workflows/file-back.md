---
description: Tự động lưu kết quả phân tích có giá trị thành Wiki page mới (Karpathy File-Back Pattern)
---

Workflow `/file-back` hiện thực hóa nguyên tắc "Query Compounding" của Karpathy:
> *"Good answers can be filed back into the wiki as new pages. These are valuable and shouldn't disappear into chat history."*

---

## ✅ CHECKPOINT (Bắt buộc trước khi bắt đầu)

```yaml
CHECKPOINT:
  agent: "@librarian"
  task: "Thực hiện File-Back insight mới vào Wiki"
  output_file: "3-resources/wiki/concepts/CONCEPT_[PREFIX]_[Name].md"
  prerequisites:
    - file: "3-resources/wiki/index.md"
      exists: "YES"
  status: "READY"
```

---

## 🎯 Triggers (Khi nào kích hoạt)

Agent **tự động** thực hiện File-Back khi đáp ứng **bất kỳ điều kiện nào** sau đây:

| # | Trigger | Dấu hiệu nhận biết |
| :--- | :--- | :--- |
| **T1** | Agent tổng hợp **2+ trang Wiki** để trả lời 1 câu hỏi | Đọc ≥2 file trong `3-resources/wiki/concepts/` hoặc `entities/` |
| **T2** | Agent tạo ra **bảng so sánh** hoặc **phân tích đối chiếu** mới | Response chứa bảng Markdown với ≥2 cột so sánh |

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

**Câu hỏi 2**: *"Insight này đã được lưu trong index.md chưa?"*
- Đọc **section CONCEPT PAGES** của `3-resources/wiki/index.md`.
- Tìm trang có title/summary tương tự với insight vừa tạo ra.
- Nếu **đã có** → Cập nhật trang hiện tại (update), không tạo mới.
- Nếu **chưa có** → Tiếp tục tạo trang mới.

---

## ⚙️ Quy trình thực thi (Execution Flow)

Sau khi Judgment xác nhận "insight mới", Agent thực hiện **trong cùng lượt phản hồi**:

### Bước 1: Đặt tên trang
- Tên file: `CONCEPT_[PREFIX]_[Tên_chủ_đề].md` (hoặc `ENTITY_`) theo chuẩn Rule 7.
- Ví dụ: `CONCEPT_ROBOT_Sensor_Comparison.md`, `CONCEPT_PROMPT_K10_Vector_Exercises.md`

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
write_to_file("3-resources/wiki/concepts/CONCEPT_[PREFIX]_[Tên].md", content)
Append("3-resources/wiki/log.md", "## [YYYY-MM-DD HH:MM] file-back | @librarian | [Tên trang]")
```

**BẮT BUỘC (Rule 17)**: Nội dung file-back phải bao gồm 2 ví dụ đối chiếu (Original + Pedagogical).

### Bước 4: Thông báo cho User (1 dòng)
> 📁 **File-Back [T1/T2]**: Đã lưu → [`CONCEPT_[Tên].md`](file:///d:/NoteBookLLM_Br/3-resources/wiki/concepts/CONCEPT_[Tên].md)

---

## 🔗 Liên kết hệ thống

- Triết lý gốc: `llm-wiki.md` dòng 39 — *"Query Compounding"*.
- Kiểm tra trùng lặp: `3-resources/wiki/index.md` → section **CONCEPT PAGES**.
- Dọn dẹp định kỳ: `/cleanup` — phát hiện mâu thuẫn và trang dư thừa sau File-Back.
