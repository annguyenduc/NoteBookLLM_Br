---
description: Thăng cấp (Promote) kết quả phân tích có giá trị thành Wiki page mới (Wiki 2.0 File-Back Pattern)
---

Workflow `/file-back` hiện thực hóa nguyên tắc "Query Compounding" của Karpathy trong môi trường Wiki 2.0:
> *"Good answers can be filed back into the wiki as new pages. These are valuable and shouldn't disappear into chat history."*
Tuy nhiên, mọi tri thức được File-Back phải đi qua cơ chế DRAFT để ngăn chặn Hallucination Loop.

---

## ✅ CHECKPOINT (Bắt buộc trước khi bắt đầu)

```yaml
CHECKPOINT:
  agent: "@librarian"
  task: "Thăng cấp Insight/Query thành Wiki Atom chính thức"
  output_file: "3-resources/wiki/.../[Name].md"
  prerequisites:
    - file: "3-resources/wiki/index.md"
      exists: "YES"
  status: "READY"
```

---

## 🎯 Triggers (Khi nào kích hoạt)

Agent **tuyệt đối KHÔNG tự động** thực hiện File-Back để tránh sinh rác (Spam). Workflow này chỉ được kích hoạt chủ động (Explicitly):

| # | Trigger | Dấu hiệu nhận biết |
| :--- | :--- | :--- |
| **T1** | Lệnh trực tiếp từ User | User gõ `/file-back` hoặc yêu cầu rõ ràng: *"Lưu bài chat này thành concept"* |
| **T2** | Thăng cấp (Promotion) | User yêu cầu: *"Kiểm tra thư mục `queries/` hoặc `session_insights/` xem có insight nào đủ tốt để file-back không?"* |

**Không** kích hoạt File-Back khi:
- Câu trả lời chỉ lặp lại nội dung của 1 trang Wiki duy nhất.
- Response là debug, sửa lỗi kỹ thuật, hoặc điều hướng hệ thống.
- User chưa đưa ra lệnh phê duyệt.

> [!NOTE]
> **Luật R8 (Human Supremacy)**: Mọi thao tác File-Back đều phải có sự ủy quyền của con người. Không tự ý nhét file vào Database.

---

## 🛡️ Pre-flight Check (Kiểm tra trước khi thực thi)

Dù được User ra lệnh (T1/T2), Agent vẫn phải rà soát nhanh để tránh làm bẩn Database:

**1. Kiểm tra Trùng lặp (Duplication Check)**:
- Kiểm tra nhanh (hoặc đọc `3-resources/wiki/index.md`) xem khái niệm này đã tồn tại chưa.
- Nếu **đã có** → Đề xuất: *"Trang này đã tồn tại, tôi đề xuất cập nhật (Update) file cũ thay vì tạo file mới"*. Không được tự ý ghi đè.
- Nếu **chưa có** → Tiến hành tạo trang mới.

**2. Đảm bảo chất lượng (Quality Check - Luật R11)**:
- Nếu nội dung quá mỏng (< 200 bytes) hoặc chỉ là chat vụn vặt, Agent phải cảnh báo: *"Nội dung này chưa đủ điều kiện để file-back thành Atom Wiki."*.

---

## ⚙️ Quy trình thực thi (Execution Flow)

Sau khi User xác nhận rõ `GO` cho thao tác ghi file, Agent mới được thực hiện:

### Bước 1: Quyết định đích đến & Đặt tên trang
- Kiến thức nguyên tử: Lưu vào `concepts/CONCEPT_[PREFIX]_[Tên].md`.
- Bài tổng hợp dài: Lưu vào `synthesis/SYNTHESIS_[Tên].md`.

### Bước 2: Tạo nội dung với template chuẩn (Luật R13)
**BẮT BUỘC:** Đọc và áp dụng đúng cấu trúc của Template tương ứng trước khi viết file:
- Kiến thức nguyên tử: Xem `D:\NoteBookLLM_Br\.agent\skills\references\CONCEPT_TEMPLATE.md`
- Bài tổng hợp dài: Xem `D:\NoteBookLLM_Br\.agent\skills\references\SYNTHESIS_TEMPLATE.md`

**BẮT BUỘC:** `status` phải là `DRAFT` để đưa vào Review Queue chờ Human Review.
Thêm nội dung phân tích + [[Wikilinks]] đến các trang gốc đã tham khảo.

### Bước 3: Ghi file và Cập nhật Log (Tuân thủ Luật R14)
**Bắt buộc có AN GO trước bước này.** Nếu chưa có GO, chỉ xuất preview/diff trong chat và dừng.

```text
# Lưu file đúng định dạng
write_to_file("3-resources/wiki/concepts/CONCEPT_[PREFIX]_[Tên].md", content) 
# HOẶC "3-resources/wiki/synthesis/SYNTHESIS_[Tên].md"

# Ghi nhật ký vào đúng file của ngày hôm nay (Phân mảnh Log)
Append("3-resources/wiki/logs/log_YYYY_MM_DD.md", "## [HH:MM] file-back | @librarian | [Tên trang]")
```

### Bước 4: Thông báo cho User (1 dòng)
> 📁 **File-Back**: Đã lưu (DRAFT) → [`[Tên].md`](file:///d:/NoteBookLLM_Br/3-resources/wiki/concepts/[Tên].md). Đang chờ Human Review.

---

## 🔗 Liên kết hệ thống

- Triết lý gốc: `llm-wiki.md` dòng 39 — *"Query Compounding"*.
- Kiểm tra trùng lặp: `3-resources/wiki/index.md` → section **CONCEPT PAGES**.
- Dọn dẹp định kỳ: `/cleanup` — phát hiện mâu thuẫn và trang dư thừa sau File-Back.
