---
name: using-superpowers
description: "Dùng khi bắt đầu bất kỳ cuộc trò chuyện nào — xác lập cách tìm và sử dụng đúng skills, bắt buộc gọi tool Skill trước MỌI phản hồi kể cả câu hỏi làm rõ."
---

# Sử Dụng Siêu Năng Lực

## Khi nào dùng
Kích hoạt ở đầu mỗi phiên làm việc để định hướng đúng skill cho task hiện tại.

## Nguyên Tắc Bắt Buộc

**Trước khi trả lời bất kỳ điều gì — kể cả câu hỏi làm rõ — phải thực hiện đủ 3 bước:**

1. **Tìm skill phù hợp** — đọc danh sách skill hiện có trong `.agent/skills/`
2. **Đọc file SKILL.md** của skill được chọn bằng tool `view_file`
3. **Tuân theo hướng dẫn** trong SKILL.md đó trước khi hành động

## Quy Trình Tìm Skill

```
Nhận task → Đọc danh sách .agent/skills/ → Chọn skill phù hợp
→ view_file SKILL.md → Thực hiện theo hướng dẫn
```

## Khi Không Tìm Được Skill Phù Hợp

Nếu không có skill nào khớp với task:
1. Thông báo rõ: "Không tìm thấy skill phù hợp cho task này"
2. Đề xuất tạo skill mới hoặc tiến hành không có skill (với sự đồng ý của user)
3. KHÔNG tự suy luận mà bỏ qua bước tìm skill

## Lỗi Cần Tránh
- Trả lời ngay mà không kiểm tra skill
- Cho rằng đã nhớ skill từ phiên trước (luôn đọc lại)
- Chọn skill dựa vào tên mà không đọc SKILL.md