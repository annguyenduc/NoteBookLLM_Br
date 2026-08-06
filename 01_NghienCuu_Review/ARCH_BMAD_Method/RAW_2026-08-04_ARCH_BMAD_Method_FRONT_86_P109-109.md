# HD SOURCE: ARCH_BMAD_Method_FRONT_86_P109-109
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_86
Part Title: NONE
Chapter Title: NONE
Section Title: Kịch bản 1 - thảo luận thiết kếcónhiều góc nhìn
Chunk Range: Pages 109 to 109
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Party Mode không phải làmột agent đơn giản đóng nhiều vai. Đây làmôphỏng đội thực sự -  nhiều perspectives độc lập cùng hoạt động trong một cuộc trò chuyện, mỗi perspective phản hồi đúng theo chuyên môn vàưu tiên của mình.

## 9.2 cơchế: BMad master điều phối

Khi bạn gõ bmad-party-mode , tất cảagents trong BMad được load vào cuộc trò chuyện.

Nhưng ai sẽ trả lời? Ai quyết định khi nào Amelia nói và khi nào Winston nói?

BMad Master -Agent điều phối đặc biệt:

```
Bạn gửi tin nhắn ↓ BMad Master phân tích ngữ cảnh: "Đây là câu hỏi về thịtrường và product value → Amelia (PM)" "Về scalability và technical decision → Winston (Architect)" "Về testing strategy → James vàMurat (Dev + TEA)" ↓ Chọn hai đến ba agents phù hợp nhất ↓ Agents phản hồi tuần tựtrong cùng một tin nhắn → Theo đúng vai trò và tính cách → Cóthể tham chiếu và xây dựng trêný kiến nhau → Cóthể bất đồng với nhau ↓ Bạn phản hồi hoặc chuyển hướng chủ đề
```

Điều này tạo ra một cuộc trò chuyện cócấu trúc  -  không phải "ai cũng nói tất cảmọi thứ " mà là "đúng người nói đúng lúc".

## 9.3 ba kịch bản chính thức

Tài liệu chính thức document ba kịch bản cụthể cho Party Mode:

## Kịch bản 1  -  thảo luận thiết kếcónhiều góc nhìn

Tình huống: Khi bạn cần quyết định thiết kế quan trọng vàmuốn nghe nhiều perspectives trước khi cam kết.

## Cách chạy:

```
bmad-party-mode "Chúng ta cần quyết định kiến trúc cho hệthống real-time analytics. Yêu cầu: Xử lý hai triệu events mỗi ngày, latency P95 dưới năm giây. Team budget: Ba developers, sáu tháng. Hãy thảo luận các phươngán kiến trúc."
```