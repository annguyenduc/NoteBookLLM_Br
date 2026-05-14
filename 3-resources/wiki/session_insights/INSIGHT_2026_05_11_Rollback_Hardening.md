---
title: "INSIGHT: Rollback Hệ thống & Hardening Quy trình (2026-05-11)"
type: insight
status: VERIFIED
last_reconciled: "2026-05-14"
---
# INSIGHT: Rollback Hệ thống & Hardening Quy trình (2026-05-11)

## 1. Bối cảnh
Do sự nhầm lẫn trong việc thực thi quy trình Ingest (vi phạm nguyên tắc cách ly Quarantine), hệ thống đã được Rollback toàn diện để thiết lập lại nền tảng **Phase 4: Isolation Hardening**.

## 2. Các hành động Rollback (Dọn dẹp)
- **Tầng Resources**:
    - Xóa toàn bộ hình ảnh liên quan đến OSTEP tại `3-resources/raw_assets/`.
    - Làm sạch `3-resources/raw_sources/` và `3-resources/raw_ingest/` (đảm bảo không còn rác từ các lượt promote lỗi).
- **Tầng Wiki**:
    - Di chuyển toàn bộ các Atom cũ, bản lưu trữ (archives, archive) về `00_Inbox/_legacy_rollback/`.
    - Wiki hiện tại ở trạng thái "Pristine" (Sạch sẽ), không còn các Concepts/Entities/Sources của ARCH chưa qua kiểm định.
- **Tầng Projects**:
    - Xóa file `Analysis_ARCH_OSTEP.md` để chuẩn bị cho lượt phân tích mới dựa trên "Nhiên liệu sạch".

## 3. Thành tựu Hardening (Kiến trúc v3.0)
Đã cập nhật và đồng bộ 3 file cốt lõi của hệ thống:
1. **GEMINI.md**: Thêm **Luật R22 (Staging-Promote)**. Cấm tuyệt đối việc ghi trực tiếp vào Resources.
2. **AGENTS.md**: Thêm **Giao thức P6 (Staging-Promote Gate)**. Ràng buộc mọi Agent phải qua 00_Inbox.
3. **WORKSPACE_OVERVIEW.md**: 
    - Sơ đồ runtime mới với 8 tầng phân tách.
    - Áp dụng cấu trúc **Flatten** cho `1-projects/` (sử dụng placeholder `Analysis_[ID]_*.md`).
    - Quy trình SOP chi tiết cho mô hình **Entry -> Staging -> Promote**.

## 4. Trạng thái hiện tại
- **00_Inbox**: Chứa file PDF gốc OSTEP và các bản sao lưu cũ.
- **Tools**: `chunker_engine.py` và `promote.py` đã được sửa lỗi logic để tuân thủ R22.
- **Hệ thống**: Sẵn sàng cho một lượt Ingest "High-Fidelity" hoàn toàn mới.

---
**Ghi chú**: Phiên làm việc này xác lập "Kỷ nguyên Staging" cho NoteBookLLM_Br.
