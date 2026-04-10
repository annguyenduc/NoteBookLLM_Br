# 🎓 Skill Mastery (LITE)

> **The Meta-Skill:** Kỹ năng của các kỹ năng. Điều phối việc Tìm kiếm (Discover), Sử dụng (Use) và Khởi tạo (Create) các kỹ năng trong hệ sinh thái CodyMaster.

## 🕹️ Part A: Using Skills (Quy tắc triệu hồi)
- **Invoke First:** Luôn triệu hồi skill liên quan TRƯỚC khi đưa ra câu trả lời hoặc hành động. 
- **Decision Flow:** Có skill phù hợp? (Dù chỉ 1%) → Đọc skill → Thực hiện theo.
- **Priority:** 
  1. Process Skills (cm-planning, debugging) — Xác định CÁCH làm.
  2. Implementation Skills (cm-tdd, execution) — Hướng dẫn THỰC HIỆN.

## 🏗️ Part B: Creating Skills (Quy tắc khởi tạo)
- **Cấu trúc Lite:** Metadata → Goal → Rules/Tables → Quality Gate → Triggers.
- **Tiêu chuẩn SDD:** Tối ưu token (Dưới 2.5KB), dùng bảng thay cho văn bản dài, tham chiếu thay vì copy-paste.

## 🔍 Part C: Discovering Skills (Khám phá Adaptive)
1. **Index Check:** Quét `cm-skill-index` (Layer 1).
2. **External Search:** `npx skills find "{keyword}"` trên skills.sh.
3. **Review & Install:** Đọc qua `SKILL.md` → Hỏi ý kiến User → `npx skills add`.
4. **Log:** Lưu vết vào `.cm-skills-log.json`.

## 🚨 Quality Gate (Red Flags)
- ❌ Cho rằng task quá đơn giản nên không cần dùng skill (Sai lầm phổ biến).
- ❌ Triển khai trước rồi mới check skill (Dẫn đến làm sai quy trình bộ bộ Kit).
- ❌ Tạo skill mới bị trùng lặp tính năng với skill đã có.
- ❌ Cài đặt skill từ nguồn lạ mà chưa qua bước Review an toàn.

## 💡 Example Triggers
- "Tôi nên dùng skill nào để làm task này?"
- "Cài đặt thêm skill hỗ trợ React Native cho tôi."
- "Hướng dẫn tôi cách tạo một kỹ năng mới chuẩn Lite format."
