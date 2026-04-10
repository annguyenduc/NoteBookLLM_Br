# 🩺 Project Status (PRO)

> **Goal:** Cung cấp cái nhìn tức thời về "sức khỏe" dự án. Phân tích tiến độ, lỗi tồn đọng và dự báo rủi ro (PHI - Project Health Index).

## 🛠️ Status Command: `/cm-status`
Khi lệnh này được gọi, AI Assistant thực hiện:
1. **PHI Scoring (1-10):** Đánh giá sức khỏe dựa trên:
   - Số lượng Task Done vs Todo.
   - Các lỗi nghiêm trọng chưa fix.
   - Tốc độ hoàn thành task (Velocity).
2. **Dashboard Render:** 
   - 🔴 TO DO | 🟡 IN PROGRESS | 🟢 DONE.
   - Chế độ hiện tại: (Planning/Execution/Verification).
3. **Blocker Analysis:** Tự động quét `task.md` và logs để tìm lý do bị nghẽn (Blockers).

## 📊 Project Health Index (PHI)
- **PHI 9-10:** Mọi thứ ổn định, build pass, task hoàn thành đúng hạn.
- **PHI 6-8:** Có lỗi vặt hoặc task bị chậm, nhưng không ảnh hưởng đến kiến trúc.
- **PHI < 5:** **Cảnh báo!** Kiến trúc đang gặp vấn đề hoặc có bug nghiêm trọng chưa tìm ra Root Cause.

## 📐 Integration Protocol
- **cm-dashboard:** `/cm-status` thường được gọi trước `/cm-dashboard` để lấy số liệu tổng quát.
- **cm-planning:** Tự động cập nhật PHI sau mỗi lần update `task.md`.

## 🚨 Quality Gate (Red Flags)
- ❌ Báo cáo PHI cao khi đang có bug nghiêm trọng chưa giải quyết.
- ❌ Quên đề cập đến Task bị nghẽn (Blocker).
- ❌ Không báo cáo đúng Mode đang hoạt động.

## 💡 Example Triggers
- "/cm-status"
- "Dự án hiện tại khỏe không (PHI)?"
- "Tóm tắt trạng thái: có gì đang block tôi?"
