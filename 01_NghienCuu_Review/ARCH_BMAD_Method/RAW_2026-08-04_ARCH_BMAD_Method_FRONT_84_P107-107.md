# HD SOURCE: ARCH_BMAD_Method_FRONT_84_P107-107
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_84
Part Title: NONE
Chapter Title: NONE
Section Title: Tóm tắt chương 8
Chunk Range: Pages 107 to 107
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Thực hành ngay

## Bài tập 1  -  Phân Tích Story Quality:

Lấy một story bất kỳ bạn đang có và kiểm tra: Cóuser story theo format "Với tưcách là... Tôi muốn... Để ..." không? Cótiêu chíchấp nhận cụthể , cóthể kiểm chứng không? Cótechnical notes tham chiếu kiến trúc không?

Developer Agent cóthể triển khai mà không cần hỏi thêm câu hỏi không?

## Bài tập 2  -  Quick Dev Thực Tế :

Chọn một task nhỏ trong dự án:

```
bmad-quick-dev # Spec: "[môtả cụthểmột dòng]" # Constraints: "[những gìAI cần và không cầ
```

```
n làm]"
```

Quan sát cách AI auto-detect conventions và hỏi xác nhận.

## Tóm tắt chương 8

Giai đoạn 4 là vòng lặp: Sprint Planning → Create Story → Dev Story → Code Review → lặp lại sprint-status.yaml: Nguồn sựthật duy nhất về tiến độ -được khởi tạo bởi bmadsprint-planning Tiêu chuẩn "Sẵn sàng phát triển": User story, tiêu chíchấp nhận, ghi chú kỹ thuật, phụthuộc, định nghĩa hoàn thành Mỗi story = Fresh chat riêng -  nguyên tắc Fresh Chatáp dụng nghiêm túc nhấtở đây Developer Agent đọc: story + architecture + projectcontext + codebase → code nhất quán Code Review đối nghịch: Bắt buộc tìm vấn đề . Lọc false positives là trách nhiệm của bạn Quick Dev  năm nguyên tắc: Néný định, đường đi an toàn nhỏnhất, chạy tựchủ , chẩn đoán đúng layer, giảm human-in-the-loop Quick Dev tự động phát hiện tech stack và conventions trong dự án hiện có `bmad-correct-course`: Dùng khi scope thay đổi  -  cập nhật nhất quán qua tất cả tài liệu

Retrospective sau mỗi epic: Học hỏi + cập nhật project-context = cải thiện tích lũy