---
description: Workflow chuẩn hóa quy trình ingest bổ sung (Incremental/Additional Ingest) các Atom tri thức còn khuyết thiếu vào Vault từ nguồn tài liệu đã có.
---

# Workflow: incremental-ingest

> Phiên bản 1.0 — 2026-05-23
> Mục tiêu: Thiết lập quy chuẩn an toàn, kiểm soát chặt chẽ quy trình Ingest bổ sung các Atom khuyết thiếu vào Vault Obsidian nhằm bảo vệ tính toàn vẹn của kho tri thức `3-resources/`.

---

## 1. Objective

Triển khai quy trình kiểm soát chất lượng qua các bước độc lập (Wiki Gate) cho việc Ingest bổ sung:

```text
Gap Triage (Phát hiện khoảng cách)
-> Draft Generation (Tạo nháp DRAFT tại 00_Inbox/concepts/)
-> Quality Audit (Kiểm toán chất lượng bằng md_auditor.py)
-> Human Gate (AN duyệt & phê duyệt)
-> Promote & Link (Thăng cấp và tự động kết nối qua promote.py)
-> Rebuild Index (Đồng bộ cơ sở dữ liệu & đóng sổ)
```

Quy trình này đảm bảo không có Atom kém chất lượng, sai định dạng hay liên kết bị vỡ (broken link) nào có thể lọt vào kho tri thức chính thức `3-resources/wiki/concepts/`.

---

## 2. Các Bước Quy Trình Chi Tiết

### Bước 1: Gap Triage (Phân loại khoảng trống)
- **Tác vụ:** Quét outline/manifest của nguồn tài liệu và đối chiếu với danh sách các Atom hiện có trong database SQLite của Vault.
- **Đầu ra:** Bản báo cáo phân tích các Atom bị khuyết thiếu (như đã phân tích cho ARCH_TIS).

### Bước 2: Draft Generation (Tạo nháp)
- **Tác vụ:** Khởi tạo các tệp Atom mới.
- **Trạng thái ban đầu:** Bắt buộc phải đặt `status: "DRAFT"` trong YAML Frontmatter.
- **Vị trí lưu trữ nháp:** Lưu tại thư mục đệm **`00_Inbox/concepts/`**.
- **Yêu cầu nội dung:** Phải đầy đủ cấu trúc: Định nghĩa, Nguyên lý cấu trúc, Ví dụ đối chiếu kép (R18), Phản tư sư phạm (4F) và Trích nguồn (R3).

### Bước 3: Quality Audit (Kiểm toán chất lượng)
- **Tác vụ:** Chạy script kiểm định markdown `md_auditor.py` trên các file nháp.
- **Tiêu chí đạt (Pass):**
  - Không có liên kết bị vỡ (broken links).
  - Tên file tuân thủ quy chuẩn `CONCEPT_TRAP_TIS_*` hoặc `CONCEPT_LEV_TIS_*`.
  - Định dạng YAML frontmatter chuẩn xác 100%.

### Bước 4: Human Gate (Cổng phê duyệt)
- **Tác vụ:** Trình bày danh sách các Atom nháp đã vượt qua bài kiểm toán cho AN và xin ý kiến phê duyệt cuối cùng.
- **Cơ chế an toàn:** Tuyệt đối không tự ý promote khi chưa có lệnh "GO" rõ ràng từ AN.

### Bước 5: Promote & Link (Thăng cấp tri thức)
- **Tác vụ:** Sau khi AN duyệt, chạy script `promote.py` hoặc di chuyển các file DRAFT được duyệt từ `00_Inbox/concepts/` vào `3-resources/wiki/concepts/`.
- **Yêu cầu:** Thiết lập trạng thái `status: "VERIFIED"` sau khi đã audit thành công. (Quy tắc CORE.md: Cấm tuyệt đối Agent tự đặt trạng thái `SYNTHESIZED`).

### Bước 6: Rebuild Index (Đồng bộ cơ sở dữ liệu)
- **Tác vụ:** Chạy script `rebuild_index.py` hoặc gọi lệnh `/rebuild` để cập nhật cơ sở dữ liệu SQLite cục bộ, đồng bộ liên kết chéo và ghi nhận nhật ký kết thúc phiên.

---

## 3. Guardrails (Ranh giới an toàn)

*   **R1 - Raw Immutable:** NGHIÊM CẤM tự ý ghi, sửa đổi trực tiếp bất kỳ tệp tin nào trong `3-resources/` bằng các công cụ viết file thô. Mọi hoạt động phải đi qua thư mục đệm `00_Inbox/` và được promote qua script hệ thống hoặc AN.
*   **Status Guard:** Agent chỉ có quyền đặt trạng thái `DRAFT` hoặc `VERIFIED`. Trạng thái `SYNTHESIZED` chỉ dành riêng cho con người ghi trực tiếp.
*   **Broken Link Prevention:** Trước khi chạy promote, bắt buộc phải quét kiểm tra toàn bộ liên kết chéo `[[CONCEPT_*]]` để đảm bảo chúng trỏ về các Atom có thật.
