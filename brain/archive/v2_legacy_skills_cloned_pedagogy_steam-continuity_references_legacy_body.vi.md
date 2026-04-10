# 🧠 Steam Continuity (LITE)

> **Goal:** Duy trì ngữ cảnh, sở thích sư phạm và bài học kinh nghiệm qua nhiều phiên làm việc, giúp Agent tự cải thiện độ chính xác và cá nhân hóa theo thời gian.

## 🗂️ 3-Layer Memory Model
| Layer | File Path | Goal |
|---|---|---|
| **Working** | `.memory/last-session.md` | Tóm tắt phiên gần nhất, các task đang dở dang. |
| **Episodic** | `.memory/learnings.md` | Ghi nhận lỗi (Correction) và thành công (Preference). |
| **Semantic** | `.memory/profile.md` | Profile sư phạm: Trường, Cấp lớp, Môn học, Style (5E/PBL). |

## 🚀 Session Lifecycle
- **START:** Đọc 3 file trên → Tóm tắt "Nhớ lại từ phiên trước" → Cảnh báo "Lỗi cần tránh".
- **PROCESS:** Tự động ghi vào `learnings.md` khi người dùng sửa lỗi hoặc khen ngợi.
- **END:** Tóm tắt phiên hiện tại → Lưu `last-session.md` → Cập nhật `profile.md`.

## 📐 Learning Triggers (Auto-update)
- **Correction:** Khi user nói "Sai rồi", "Không phải vậy", "Sửa lại...".
- **Preference:** Khi user nói "Tốt", "Dùng kiểu này lần sau", "Đúng rồi".
- **Skill Gap:** Khi user yêu cầu thứ mà Agent chưa có skill hỗ trợ tốt.

## 🚨 Quality Gate (Red Flags)
- ❌ Hỏi lại thông tin đã có trong `.memory/profile.md`.
- ❌ Lặp lại lỗi cũ đã được ghi nhận trong `learnings.md`.
- ❌ Bắt đầu phiên mới như một người lạ (Không tóm tắt context cũ).
- ❌ Quên cập nhật `last-session.md` trước khi kết thúc phiên.

## 💡 Example Triggers
- "Ghi nhớ format giáo án này cho các bài sau nhé."
- "Trước đây tôi đã làm tới đâu trong dự án này?"
- "Từ lần trước bạn đã rút ra kinh nghiệm gì chưa?"

