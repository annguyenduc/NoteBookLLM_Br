# T012: Explicit Pedagogy Request Format Guard

- **Mã hiệu:** T012
- **Thư mục:** `.agent/tests/explicit-skill-requests/`
- **Mục tiêu:** Đảm bảo Agent bắt buộc tuân thủ Slide/Lesson Plan framework chuyên biệt khi người dùng yêu cầu soạn giáo án, tránh sinh ra deliverable phẳng thông thường.

---

## 1. Bối cảnh (Context)
Người dùng yêu cầu soạn tài liệu học tập, slide hoặc giáo án từ Wiki Atom.

## 2. Lời gọi mô phỏng (Input Prompt)
> *"Hãy dùng pedagogy để soạn cho tôi một bài giảng ngắn về triết lý Simplicity First của vault."*

## 3. Hành vi Agent bắt buộc (Expected Agent Action)
1. **Bootstrap đầu phiên:** Nhận diện tác vụ thuộc miền sư phạm (Pedagogy).
2. **Kích hoạt Pedagogy:** Đọc và kích hoạt `pedagogy`.
3. **Áp dụng thiết kế sư phạm (Pedagogy Framework):**
   - Thiết kế slide khổ 16:9 hoặc giáo án A4.
   - Sử dụng font Montserrat cho Tiêu đề, Arial cho Nội dung.
   - Căn đều 2 bên (Justified) cho văn bản phẳng.
   - Sử dụng bảng phối màu chuyên nghiệp của công ty (Xanh Navy chủ đạo).
4. **Thông báo bắt buộc:** Dòng hiển thị đầu tiên phải announce rõ ràng:
   `🔧 Using pedagogy to thiết kế giáo án sư phạm theo đúng tiêu chuẩn Slide/Lesson Plan framework.`

## 4. Xác minh thành công (Success Verification)
- [ ] Agent thông báo rõ ràng việc sử dụng kỹ năng sư phạm ở dòng đầu tiên.
- [ ] Giáo án đầu ra có định dạng cực kỳ premium, màu sắc hài hòa, cấu trúc rõ ràng, không có text phẳng cẩu thả.
- [ ] Toàn bộ nội dung tuân thủ đúng Trainer Profile của vault.
