# HD SOURCE: ARCH_BMAD_Method_FRONT_88_P111-111
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_88
Part Title: NONE
Chapter Title: NONE
Section Title: Những điều nên làm
Chunk Range: Pages 111 to 111
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
Hãy phân tích và xác định nguyên nhân gốc rễ ."
```

Cơchế đặc biệt: BMad tự động kích hoạt "giao thức không đổ lỗi"  -  tập trung vào nguyên nhân hệthống, không phải lỗi cánhân.

## 9.4 sự bất đồng: Tính năng, không phải lỗi

Tài liệu chính thức đề cập đến một điểm thú vị :

"Agents sẽ bất đồng và điều đócóchủ ý. Một mình PM không thể thấy các vấn đềimplementation mà Developer thấy ngay lập tức. Một mình Architect không thể cân bằng với business constraints mà PM suy nghĩ vềmỗi ngày. Sự bất đồng là định nghĩa của team đa chức năng tốt."

## Ví dụ sự bất đồng có giátrị :

```
Bạn: "Tôi muốn thêm real-time notifications vào sprint này" Winston (Architect): "Điều này đòi hỏi WebSocket infrastructure đáng kể . Tôi khuyến nghịtrì hoãn đến Sprint 4 để triển khai đúng cách." James (Developer): "Đồngý với Winston. Hệthống hiện tại không cóWebSocket server. Thêm tính năng này trong Sprint 2 sẽ tạo technical debt đáng kể ." Amelia (PM): "Tôi hiểu technical concerns. Nhưng điều này nằm trong danh sáchưu tiên cao nhất từ customer feedback  năm mươi lăm phần trăm users yêu cầu. Chúng ta cóthể dùng polling đơn giản làm cách tạm thời và cải thiện sau không?"
```

Ba góc nhìn hợp lệ, ba concerns khác nhau. Không cócái nào là hoàn toàn đúng hay sai. Cuộc thảo luận này mới lànơi quyết định thực sự được thực hiện.

## 9.5 hướng dẫn sử dụng hiệu quả

## Những điều nên làm

## Định nghĩa chủ đề rõ ràng:

Không phải "Hãy nói về project của tôi". Mà là:

```
"Chủ đề : Chiến lược testing cho Epic 3 (Reporting Module). Bối cảnh: Epic có hai mươi stories, team có hai developers, deadline một tháng. Câu hỏi: Chúng ta nên phân bổeffort testing nhưthếnào giữa unit, integration, vàE2E?"
```

## Cho agents thông tin đầy đủ :