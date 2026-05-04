---
ID: CONCEPT_VIZ_Design_Principles
Type: Concept
Topic: Data Visualization
Status: verified
Created: 2026-04-29
Tags: [Design, Affordances, Accessibility, Aesthetics, Acceptance]
---

# Nguyên tắc Thiết kế (Design Principles)

> "Hình thức tuân theo chức năng" (Form follows function). Trong trực quan hóa dữ liệu, chúng ta cần xác định mục tiêu (chức năng) trước khi chọn cách thể hiện (hình thức).

## 1. Khả năng gợi ý (Affordances)
Affordances là những đặc điểm thiết kế gợi ý cách sử dụng sản phẩm. Trong VIZ, chúng ta dùng các tín hiệu thị giác để hướng dẫn khán giả:
- **Nhấn mạnh nội dung quan trọng:** Chỉ nên nhấn mạnh tối đa **10%** diện tích hình ảnh. Việc nhấn mạnh quá nhiều sẽ làm loãng thông điệp.
    - Dùng: Chữ đậm (bold), màu sắc nổi bật, kích thước lớn.
    - Tránh: Chữ nghiêng (italics) hoặc gạch chân (underlining) vì gây nhiễu và khó đọc.
- **Loại bỏ xao nhãng:** "Sự hoàn hảo đạt được không phải khi không còn gì để thêm, mà khi không còn gì để bớt."
    - Summarize dữ liệu nếu không cần chi tiết.
    - Đẩy các yếu tố phụ (gridlines, trục phụ) xuống nền bằng màu xám nhạt.
- **Tạo hệ thống phân cấp thị giác:** Dẫn dắt mắt khán giả theo thứ tự ưu tiên xử lý thông tin.

## 2. Tính dễ tiếp cận (Accessibility)
Thiết kế phải dễ hiểu cho mọi đối tượng, không phân biệt trình độ kỹ thuật.
- **Đừng phức tạp hóa:** "Nếu khó đọc, nó sẽ khó thực hiện." Sử dụng ngôn ngữ đơn giản, tránh biệt ngữ (jargon), dùng phông chữ không chân (Arial, Helvetica) sạch sẽ.
- **Văn bản là người bạn đồng hành:** 
    - **Tiêu đề trục và biểu đồ:** Luôn phải có (hiếm khi có ngoại lệ).
    - **Tiêu đề hành động (Action Titles):** Thay vì đặt tên "Doanh thu 2025", hãy đặt "Doanh thu 2025 tăng 10% nhờ chiến dịch X".
    - **Ghi chú (Annotation):** Giải thích trực tiếp các điểm bất thường hoặc thông tin thú vị ngay trên biểu đồ.

## 3. Tính thẩm mỹ (Aesthetics)
Thiết kế đẹp mắt giúp tăng sự kiên nhẫn của khán giả và làm cho dữ liệu trông đáng tin cậy hơn.
- **Màu sắc thông minh:** Sử dụng bảng màu chuyên nghiệp, tránh "vùng đất cầu vồng" (rainbow land).
- **Căn lề (Alignment):** Tạo ra các đường thẳng đứng và ngang sạch sẽ để thiết lập cảm giác thống nhất. Tránh căn giữa (center alignment) một cách lộn xộn.
- **Khoảng trắng (White Space):** Đừng cố lấp đầy mọi không gian. Khoảng trắng giúp mắt được nghỉ ngơi và phân tách các phần thông tin rõ rệt.

## 4. Sự chấp nhận (Acceptance)
Con người thường sợ thay đổi. Để khán giả chấp nhận thiết kế mới:
- **So sánh song song (Side-by-side):** Cho thấy biểu đồ cũ và biểu đồ mới để chứng minh lợi ích rõ rệt của cách làm mới.
- **Giải thích lợi ích:** Minh bạch về lý do tại sao thay đổi thiết kế giúp đưa ra quyết định nhanh hơn.
- **Lấy ý kiến chuyên gia:** Thuyết phục những người có sức ảnh hưởng trong nhóm trước khi công bố rộng rãi.

## 5. Ví dụ đối chiếu (Rule 17: Double Examples)

### 5.1. Ví dụ từ sách (Original)
*Tình huống: Nhấn mạnh nội dung quan trọng trên Bar chart.*
- **Cách giải quyết:** Trong một biểu đồ cột so sánh hiệu suất của 10 công ty đối thủ. Thay vì tô màu đủ 10 màu cho 10 thanh (cầu vồng), designer chỉ tô màu xám nhạt cho 9 thanh công ty đối thủ, và dùng màu Xanh đậm (màu thương hiệu) cho thanh duy nhất đại diện cho công ty của mình. Mắt khán giả sẽ bị thu hút ngay lập tức vào vị trí công ty mình.

### 5.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Sử dụng Tiêu đề hành động (Action Titles) trong báo cáo học vụ.*
- **Cách giải quyết:** Ban giám hiệu nhận được biểu đồ so sánh chi phí tổ chức ngoại khóa.
  - Tiêu đề cũ (Chỉ mô tả): "Chi phí ngoại khóa học kỳ 1 năm 2025".
  - Tiêu đề mới (Action Title): "Chi phí ngoại khóa HK1 vượt ngân sách 15% do chi phí xe di chuyển tăng cao".
  Ban giám hiệu đọc xong tiêu đề có thể đưa ra quyết định ngay lập tức mà không cần phải tự soi từng con số để mò mẫm kết luận.

---
Nguồn: [[SOURCE_VIZ_Storytelling_with_Data_P1]] (Xác nhận Rule 14 từ: [[SOURCE_VIZ_Storytelling_with_Data_P1]])


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
