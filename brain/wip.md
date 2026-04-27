# 🚧 Work In Progress — Session Continuity Log
> **Dành cho LLM Agent:** Đọc ngay sau `brain/index.md`. File này lưu task đang dở dang giữa các phiên.
> **Quy tắc:** Luôn CẬP NHẬT file này khi bắt đầu và kết thúc phiên. KHÔNG xóa dòng cũ — gạch qua (~~text~~) nếu hoàn thành.

---

## 🔴 Đang Dang Dở (Active WIP)

### [2026-04-23] Wiki Migration — Giai đoạn cuối
- **Agent phụ trách:** @engineer, @librarian
- **Vấn đề:** `brain/distilled/` hiện rỗng — cần populate từ wiki đã verify
- **Bước tiếp theo:**
  - [ ] Populate `brain/distilled/` với KB đã verify từ modules hoàn tất
  - [ ] Bắt đầu atomize GBot / Codey / xBot (Makeblock Robotics)
  - [ ] Audit Unicode toàn hệ thống (ký tự lỗi trong wiki pages)
  - [ ] Tạo `approved.json` / `rejected.json` cho feedback loop

### [2026-04-23] Lint Report — Lỗi Gateway chưa sửa
- **Vấn đề:** `brain/lint_report.md` ghi nhận lỗi `HTTPConnectionPool localhost:4000` khi chạy AI analysis
- **Nguyên nhân:** Gateway Port 4000 chưa chạy khi lint
- **Bước tiếp theo:**
  - [ ] Khởi động Gateway trước khi chạy `/lint` (xem `/start-gateway`)
  - [ ] Re-run lint sau khi Gateway ổn định

---

## ✅ Hoàn thành Gần đây (Last 7 days)

| Ngày | Task | Agent |
|---|---|---|
| 2026-04-23 | Tạo `brain/index.md` và `brain/wip.md` (Gap fix từ NotebookLM) | @pm |
| 2026-04-22 | Hoàn tất atomize AI Arduino D1-D4 (2,391 wiki pages tổng) | @engineer |
| 2026-04-22 | Hoàn tất atomize Rover Robotics (5 bộ đề, 15 nodes) | @engineer |
| 2026-04-22 | Hoàn tất YoloBit D1-D4, mBot M1-M2 | @engineer |
| 2026-04-21 | Tái thiết lập repo chuẩn Flatness (0.67 MB) + Git LFS | @devops |

---

## 📋 Backlog (Chưa lên kế hoạch)

- [ ] Tích hợp MemPalace / ChromaDB khi wiki pages > 3,000
- [ ] Auto-pruning cho `brain/lessons/` (expire sau 30 ngày)
- [ ] Semantic Search nâng cao (cm-semantic-search skill)
- [ ] Tách `QUESTION_*` và `ATOMS_*` thành 2 sub-namespace riêng

---

## 🧩 Context Handoff (Đọc khi tiếp tục phiên mới)

```
Trạng thái hiện tại:
- Wiki: 2,391 wiki pages | 69 raw sources | distilled/ CÒN RỖNG
- Taxonomy: KHMT(241) | IOT(1,227) | Robot(477) | DESIGN(261)
- Còn thiếu: GBot, Codey, xBot atomization
- Lint: cần Gateway running trước
- Gap đã fix hôm nay: index.md, wip.md
```

---

*Được quản lý bởi tất cả agents. Cập nhật mỗi đầu/cuối phiên.*
*Format cập nhật: `- [x] Task hoàn thành` hoặc gạch qua: `~~task~~`*
