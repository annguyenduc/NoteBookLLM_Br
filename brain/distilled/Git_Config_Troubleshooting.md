---
title: Khắc phục lỗi AI (Antigravity) không phản hồi do Git Config
date: 2026-04-09
source: User Contribution (Reddit/viduthalaim)
tags: [Troubleshooting, Git, Antigravity, BugFix]
confidence: 100% (Verified Solution)
---

# 🛠️ Khắc phục lỗi AI không phản hồi (Git Worktree Config)

> **Tình trạng**: AI không trả lời tin nhắn, nút "Stop" nháy rồi biến mất ngay lập tức. Đây là lỗi do cấu hình Git `worktreeConfig` không còn được hỗ trợ gây xung đột với cơ chế quét workspace của IDE.

## 📋 Hướng dẫn chi tiết (Vietnamese)

### 1. Triệu chứng
- AI không xử lý dữ liệu đầu vào.
- Trạng thái UI nháy "Stop" rồi trả về trạng thái chờ nguyên trạng.
- Không có lỗi hiển thị rõ ràng trên Console nhưng AI "câm lặng".

### 2. Nguyên nhân
Do cài đặt Git cũ bị kẹt lại trong file cấu hình cục bộ của workspace:
`extensions.worktreeConfig = true`

### 3. Cách khắc phục (3 Bước)
1. **Mở file cấu hình**: Truy cập `.git/config` tại thư mục gốc dự án. (Lưu ý: Thư mục `.git` thường bị ẩn).
2. **Xóa dòng lỗi**: Tìm và xóa dòng `extensions.worktreeConfig = true`.
3. **Khởi động lại**: Tắt hoàn toàn và mở lại Antigravity.

## 🔗 Liên kết liên quan
- [[ECC_CodyMaster_Hybrid_Philosophy]]
- [[DevOps_IT_Automation_Wiki]]

---
*Lưu trữ bởi Antigravity v3.6 | Insight từ cộng đồng*
