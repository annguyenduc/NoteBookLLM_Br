# 🧠 Session Insight: Pipeline V2.0 Hardening (Separation of Concerns)
**Ngày**: 2026-05-11 | **Bối cảnh**: Nâng cấp hệ thống nạp dữ liệu từ "One-long-chain" sang "Modular Pipeline".

---

## 🎯 Mục tiêu & Thay đổi chính
Chúng ta đã chuyển đổi từ mô hình nạp dữ liệu tập trung (ingest làm hết mọi việc) sang mô hình **Phân rã giai đoạn** để đảm bảo tính kỷ luật và khả năng mở rộng.

### 1. Tách biệt Chuyển đổi (HD Convert) và Đăng ký (Ingest)
- **Lý do**: Database Wiki chỉ nên chứa dữ liệu đã "sẵn sàng". Việc nhào nặn PDF (Chunking, trích xuất ảnh) là tác vụ thô, dễ lỗi và tốn tài nguyên.
- **Giải pháp**:
    - `hd_converter.py` xử lý PDF -> Markdown tại `00_Inbox`.
    - `ingest.py` chỉ làm nhiệm vụ đăng ký file từ `raw_ingest` vào DB.

### 2. Nâng cấp Docling-powered Chunking
- Giải quyết triệt để lỗi OOM (Out of Memory) bằng cách chia nhỏ PDF ngay từ đầu.
- Tự động hóa việc đặt tên ảnh theo Chunk để tránh trùng lặp.

---

## 🛠️ Danh sách file lõi (Core Files for Agents)
Mọi Agent thực hiện tác vụ Ingest phải nắm vững các file này:

| File | Chức năng |
|:---|:---|
| `.agent/skills/wiki-hd-convert/scripts/hd_converter.py` | Engine chuyển đổi PDF/Office chính (Docling). |
| `.agent/skills/wiki-ingest/scripts/ingest.py` | Đăng ký file vào Database Wiki. |
| `.agent/skills/wiki-ingest/scripts/magika_router.py` | Bộ định tuyến chọn công cụ (PDF -> Docling, MD -> Native). |
| `.kiro/circuit_breaker.py` | Giám sát và thực thi việc Promote (nhập kho). |
| `.agent/workflows/ingest-v2.md` | Bản SOP (Quy trình chuẩn) 4 giai đoạn. |

---

## 🛡️ Bài học kinh nghiệm (Hardening Lessons)
- **R22 (Isolation)**: Giữ cho kho lưu trữ chính (`3-resources`) luôn sạch sẽ. Chỉ cho phép dữ liệu đã qua Audit được đi qua "Cửa khẩu" `promote.py`.
- **Review Queue**: Sử dụng Database như một bảng điều khiển luồng công việc, không chỉ là nơi chứa metadata.
- **Traceability**: Mỗi Atom phải có nguồn gốc rõ ràng từ một file vật lý đã được hash-verify.

---
*Được ghi lại bởi Antigravity. Đây là cơ sở kiến trúc cho Phase 5 (Atomization of Large Sources).*
