# HD SOURCE: ARCH_BMAD_Method_FRONT_83_P106-106
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_83
Part Title: NONE
Chapter Title: NONE
Section Title: 8.11 luồng làm việc hàng ngày
Chunk Range: Pages 106 to 106
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

"Quick Flow hoạt động tốt cho dự án hiện có. Nó sẽ tự động phát hiện tech stack, phân tích patterns code hiện có, phát hiện quyước và hỏi xác nhận, tạo spec phong phú về bối cảnh tôn trọng code hiện có."

Điểm đặc biệt của Quick Dev với dự án hiện có:

Auto-detect stack: Không c configuration filesần giải thích tech stack  -  AI phát hiện từ package.json,

Phân tích patterns:

Đọc code hiện có để theo đúng patterns

Confirm conventions: Hỏi bạn xác nhận conventions nóphát hiện được trước khiáp dụng Hỏi vềexisting conventions: "Code này dùng Promises nhất quán. Tôi cónên theo pattern này không?"

## 8.10 quick fixes  -  vá lỗi ngay lập tức

bmad-quick-fixes

Cho những thay đổi thực sựnhỏ không cần planning:

Sửa lỗi đánh máy

Sửa errors cúpháp đơn giả Thay đổi configuration nhỏ Cập nhật chuỗn i hardcoded

## 8.11 luồng làm việc hàng ngày Để dễ tham khảo, đây là quy trình làm việc điển hình trong Giai đoạn Triển khai:

```
Buổi sáng: 1. Kiểm tra sprint-status: bmad-sprint-status 2. Xác định story tiếp theo cần làm 3. Mởfresh chat Triển khai một story: 4. bmad-create-story (nếu story chưa được mở rộng đầy đủ ) 5. [Fresh chat mới] bmad-dev-story 6. [Fresh chat mới] bmad-code-review 7. Sửa các vấn đềnghiêm trọng 8. Merge code 9. Cập nhật sprint-status.yaml Nếu requirements thay đổi: 10. bmad-correctcourse → cập nhật tất cả tài liệu Sau khi epic xong: 11. bmad-retrospective 12. Cập nhật project-context.md với bài học mới
```