# HD SOURCE: ARCH_BMAD_Method_FRONT_06_P023-023
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_06
Part Title: NONE
Chapter Title: NONE
Section Title: 1.1 vấn đề với cách dùng AI thông thường
Chunk Range: Pages 23 to 23
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Bạn sẽ học được gì?

Sau khi đọc chương này, bạn sẽ hiểu rõ:

- Vấn đề căn bản khi dùng AI theo cách thông thường và tại sao nó dẫn đến kết quả trung bình
- Định nghĩa chính xác và triết lýcốt lõi của BMad Method
- Bốn giai đoạn chính thức trong vòng đời dự án theo BMad
- Quick Flow là gì và khi nào sử dụng
- Toàn bộ hệ sinh thái BMad: Core, BMM và bốn module mở rộng
- Tại sao hơn bốn mươi ba nghìn developer đang sử dụng framework này

## 1.1 vấn đề với cách dùng AI thông thường

Hãy cùng phân tích một kịch bản quen thuộc.

Một developer đang xây dựng mộtứng dụng SaaS. Anh ta mở Claude và bắt đầu hỏi: "Hãy giúp tôi thiết kế database schema choứng dụng quản lý dự án." AI trả lời. Tốt. Anh ta tiếp tục: "Viết cho tôi API endpoint để tạo task mới." AI viết. Anh ta lại hỏi tiếp vềauthentication, vềfrontend component, về deployment script.

Sau vài tuần, codebase hình thành. Nhưng có vấn đề :

- Schema database dùng snake\_case, nhưng API trả về camelCase vì developer hỏi theo thói quen khác nhau trong mỗi session
- Authentication dùng JWT nhưng một sốendpoint lại dùng session-based vì hỏiở hai context khác nhau
- Error handling không nhất quán  -  một sốchỗ throw exception, một sốchỗ return null, một sốchỗ return error object
- Không cótài liệu nào về quyết định kiến trúc vìmọi thứ xảy ra trong nhiều cuộc hội thoại riêng lẻ Đây không phải lỗi của developer. Đây là hệ quả tựnhiên của việc dùng AI theo môhình phảnứng thụ động -  hỏi khi cần, nhận câu trả lời, tiếp tục  -  mà không cócấu trúc nào liên kết các quyết định với nhau.

Cụthể, môhình thông thường cónăm vấn đề cố hữu:

Thứnhất: Không có bối cảnh tích lũy. Mỗi cuộc hội thoại bắt đầu từ đầu. AI không biết những gì bạn đã quyết định trong session trước. Bạn phải nhắc lại context mỗi lần, vàngay cả khi nhắc, bạn cũng cóthểnhắc không đầy đủ hoặc không nhất quán.