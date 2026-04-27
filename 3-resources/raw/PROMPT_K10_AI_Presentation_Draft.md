# SLIDE DRAFT V2: ĐỊNH HƯỚNG SƯ PHẠM ĐA MÔN (FULL CONTENT)

## Slide 1: Tiêu đề
- **Tiêu đề**: 🎓 Kỹ thuật Prompt RTC: Chinh phục tri thức đa môn 
- **Phụ đề**: Bản trình chiếu đối soát Toàn phần (Full Disclosure)
- **Model**: ag/gemini-3-flash

---

## Slide 2: Tư duy là sự tập trung
- **Nội dung**: Tại sao chúng ta cần RTC (Role-Task-Context)?
- **Lý luận**: 
- AI sở hữu kho tàng tri thức khổng lồ nhưng hỗn tạp.
- Prompt không cấu trúc (Simple) chỉ kích hoạt tầng mặt của tri thức.
- Prompt cấu trúc (RTC) giúp AI "đóng vai" chuyên gia, kích hoạt đúng vùng sư phạm chuyên sâu.

---

## Slide 3: [TOÁN] - Simple Prompt (Lượt A)
- **Prompt**: "Giải phương trình x² - 5x + 6 = 0 và tính tổng, tích các nghiệm."
- **Response**: 
- Để giải phương trình x² - 5x + 6 = 0 và tính tổng, tích các nghiệm, chúng ta có thể làm theo các bước sau:
- ### 1. Giải phương trình x² - 5x + 6 = 0
- Cách 1: Phân tích thành nhân tử (x - 2)(x - 3) = 0 => x1 = 2, x2 = 3.
- Cách 2: Delta (Δ) = 1 => x1 = 3, x2 = 2.
- ### 2. Tính tổng và tích các nghiệm
- Dựa trên Hệ thức Vi-ét: S = 5, P = 6.

---

## Slide 4: [TOÁN] - RTC Prompt (Lượt B) - Phần 1
- **Prompt**: # ROLE: Giáo viên Toán K-12... # TASK: Giải phương trình bậc hai và chứng minh kết quả bằng hệ thức Vi-ét...
- **Full Response (Part 1)**: 
- Chào các em, hôm nay chúng ta xét phương trình: x² - 5x + 6 = 0
- ### 1. Giải phương trình bằng Delta (Δ)
- Bước 1: Hệ số a = 1, b = -5, c = 6
- Bước 2: Tính Δ = b² - 4ac = (-5)² - 4*1*6 = 25 - 24 = 1
- Bước 3: Tìm nghiệm x1, x2
- x1 = (5 + √1) / 2 = 3
- x2 = (5 - √1) / 2 = 2
- Vậy tập nghiệm S = {2; 3}.

---

## Slide 5: [TOÁN] - RTC Prompt (Lượt B) - Phần 2
- **Full Response (Part 2)**: 
- ### 2. Áp dụng hệ thức Vi-ét kiểm tra
- - Tổng S = x1 + x2 = 3 + 2 = 5. (Theo lý thuyết -b/a = 5) -> Khớp!
- - Tích P = x1 * x2 = 3 * 2 = 6. (Theo lý thuyết c/a = 6) -> Khớp!
- ### 3. Kết luận
- Nghiệm của phương trình là x = 2 và x = 3 hoàn toàn chính xác.

---

## Slide 6: [VẬT LÝ] - Simple Prompt (Lượt A)
- **Prompt**: Giải bài tập xe chuyển động thẳng biến đổi đều (v0=10, a=2).
- **Response (Tóm lược)**: Đưa ra công thức v = 10+2t và s = 10t + t². Ví dụ t=5s => s=75m.

---

## Slide 7: [VẬT LÝ] - RTC Prompt (Lượt B) - Phân tích
- **Full Response (Part 1)**: 
- Chào em, tôi rất vui được đồng hành cùng em trong bài tập Vật lý này. Đây là một bài toán cơ bản về chuyển động thẳng biến đổi đều, giúp em nắm vững cách vận dụng các công thức động học.
- ### (1) Tóm tắt đề bài
- * Vận tốc đầu ($v_0$): $10 \, \text{m/s}$
- * Gia tốc ($a$): $2 \, \text{m/s}^2$
- * Thời gian ($t$): $5 \, \text{s}$
- * Yêu cầu: Tính quãng đường ($s$) xe đi được sau 5 giây.

---

## Slide 8: [VẬT LÝ] - RTC Prompt (Lượt B) - Hiện tượng
- **Full Response (Part 2)**: 
- ### (2) Phân tích hiện tượng
- * **Loại chuyển động:** Vì xe có gia tốc không đổi ($a = 2 \, \text{m/s}^2$) và cùng dấu với vận tốc đầu ($v_0 > 0, a > 0$), nên đây là **chuyển động thẳng nhanh dần đều**.
- * **Diễn biến:** Ngay tại thời điểm bắt đầu quan sát ($t = 0$), xe đã có vận tốc là $10 \, \text{m/s}$. Trong quá trình chuyển động, cứ mỗi giây trôi qua, vận tốc của xe lại tăng thêm $2 \, \text{m/s}$. Do vận tốc tăng dần nên quãng đường xe đi được trong các giây tiếp theo sẽ dài hơn các giây trước đó.
- * **Chiều chuyển động:** Chọn chiều dương là chiều chuyển động của xe.

---

## Slide 9: [VẬT LÝ] - RTC Prompt (Lượt B) - Giải chi tiết
- **Full Response (Part 3)**: 
- ### (3) Các bước áp dụng công thức và giải bài toán
- **Bước 1: Chọn hệ quy chiếu**
- * Gốc thời gian lúc xe bắt đầu chuyển động; Chiều dương là chiều chuyển động.
- **Bước 2: Áp dụng công thức tính quãng đường**
- $$s = v_0 \cdot t + \frac{1}{2} \cdot a \cdot t^2$$
- **Bước 3: Thay số và tính toán**
- $$s = 10 \cdot 5 + \frac{1}{2} \cdot 2 \cdot (5)^2 = 50 + 25 = 75 \, (\text{m})$$
- **Kết luận:** Sau 5 giây, xe đi được quãng đường là **75 mét**.

---

## Slide 10: [HÓA HỌC] - Simple Prompt (Lượt A)
- **Prompt**: Viết cấu hình electron của Magnesium (Z=12).
- **Response**: 1s² 2s² 2p⁶ 3s². Vị trí: Ô 12, Chu kỳ 3, Nhóm IIA.

---

## Slide 11: [HÓA HỌC] - RTC Prompt (Lượt B) - Cấu tạo
- **Full Response (Part 1)**: 
- Chào em, rất vui được đồng hành cùng em trong bài học về Bảng tuần hoàn hóa học.
- ### 1. Cấu tạo nguyên tử Magnesium (Z = 12)
- Số hiệu nguyên tử Z = 12 cho chúng ta biết:
- * **Hạt nhân:** Có 12 proton. Vỏ có 12 electron.
- * **Phân bộ electron:**
-   * Lớp 1: 2 electron.
-   * Lớp 2: 8 electron.
-   * Lớp 3 (ngoài cùng): 2 electron.
- * **Cấu hình:** $1s^2 2s^2 2p^6 3s^2$.

---

## Slide 12: [HÓA HỌC] - RTC Prompt (Lượt B) - Vị trí
- **Full Response (Part 2)**: 
- ### 2. Xác định vị trí trong Bảng tuần hoàn
- 1. **Ô nguyên tố:** Ô số 12 (Số hiệu nguyên tử Z = 12).
- 2. **Chu kỳ (Hàng ngang):** Chu kỳ 3 (Vì có 3 lớp electron).
- 3. **Nhóm (Cột dọc):** Nhóm IIA (Vì có 2 electron lớp ngoài cùng và là nguyên tố s).
- **=> Tóm tắt:** 
- | Đặc điểm | Thông số | Lý do |
- | :--- | :--- | :--- |
- | **Ô số** | 12 | Z = 12 |
- | **Chu kỳ** | 3 | Có 3 lớp electron |
- | **Nhóm** | IIA | Có 2 electron lớp ngoài cùng |

---

## Slide 13: [NGỮ VĂN] - Simple Prompt (Lượt A)
- **Prompt**: Lập dàn ý bài văn nghị luận về mạng xã hội.
- **Response**: Dàn ý 3 phần đơn giản (Mở bài, Thân bài, Kết bài) với các ý liệt kê lợi ích/tác hại cơ bản.

---

## Slide 14: [NGỮ VĂN] - RTC Prompt (Lượt B) - Dẫn dắt
- **Full Response (Part 1)**: 
- Chào bạn, với tư cách là một chuyên gia hướng dẫn tư duy phản biện, tôi sẽ giúp bạn lập dàn ý cho bài văn này...
- ### I. Mở bài: Dẫn dắt và Đặt vấn đề
- * **Dẫn dắt:** "Cảnh tượng những nhóm học sinh ngồi cùng nhau nhưng mỗi người lại dán mắt vào một màn hình điện thoại đã không còn xa lạ."
- * **Luận điểm:** Mạng xã hội là một "con dao hai lưỡi" sắc bén; tầm ảnh hưởng của nó tích cực hay tiêu cực phụ thuộc hoàn toàn vào bản lĩnh và tư duy của người sử dụng.

---

## Slide 15: [NGỮ VĂN] - RTC Prompt (Lượt B) - Thân bài (1)
- **Full Response (Part 2)**: 
- ### II. Thân bài
- #### 1. Giải thích
- Mạng xã hội là hệ thống các trang web/ứng dụng kết nối con người. Đặc điểm: lan tỏa nhanh, tương tác cao nhưng đầy thông tin chưa kiểm chứng.
- #### 2. Tác động tích cực (Mặt sáng)
- * Kho tàng tri thức khổng lồ.
- * Kết nối và sẻ chia đam mê.
- * Giải trí và rèn luyện kỹ năng số.

---

## Slide 16: [NGỮ VĂN] - RTC Prompt (Lượt B) - Thân bài (2)
- **Full Response (Part 3)**: 
- #### 3. Tác động tiêu cực (Mặt tối)
- * Hệ lụy về sức khỏe & học tập (xao nhãng, thức khuya).
- * Tâm lý tiêu cực: FOMO, Áp lực đồng lứa (Peer pressure).
- * Môi trường độc hại: Cyberbullying, fake news.
- #### 4. Phân tích nguyên nhân
- * Khách quan: Thuật toán gây nghiện.
- * Chủ quan: Học sinh thiếu kỹ năng quản lý thời gian.

---

## Slide 17: [NGỮ VĂN] - RTC Prompt (Lượt B) - Tư duy Phản biện
- **Full Response (Part 4)**: 
- #### 5. Bác bỏ và Mở rộng
- * Bác bỏ: "Nên cấm tuyệt đối học sinh dùng mạng xã hội." 
- * Phản biện: Cấm đoán gây ức chế, hãy giáo dục về "Năng lực số" (Digital Literacy).
- ### III. Kết bài
- * Thông điệp: Hãy là người dùng mạng xã hội "tỉnh thức". 
- * "Hãy tắt màn hình để bật lên những kết nối thật..."

---

## Slide 18: [TIẾNG ANH] - Simple Prompt (Lượt A)
- **Prompt**: Sửa lỗi: "I have live here since 5 years."
- **Response**: Đúng là: "I have lived here for 5 years." (Dùng V3 + For + khoảng thời gian).

---

## Slide 19: [TIẾNG ANH] - RTC Prompt (Lượt B) - Sửa lỗi
- **Full Response (Part 1)**: 
- Chào bạn, tôi là chuyên gia ngôn ngữ của bạn.
- ### 1. Câu sửa lỗi: "I have lived here for 5 years."
- ### 2. Giải thích lỗi sai
- * **Lỗi 1 (Chia động từ):** Sai "have live" -> Đúng "have lived" (Cấu trúc Have/Has + V3/ed).
- * **Lỗi 2 (Giới từ thời gian):** Sai "since 5 years" -> Đúng "for 5 years". 
-   * For + Khoảng thời gian (Duration).
-   * Since + Mốc thời gian (Point in time).

---

## Slide 20: [TIẾNG ANH] - RTC Prompt (Lượt B) - Nâng tầm
- **Full Response (Part 2)**: 
- ### 3. Phân biệt Past Simple vs. Present Perfect
- * Present Perfect (Hành động bắt đầu quá khứ, hiện tại vẫn tiếp diễn).
- * Past Simple (Hành động đã kết thúc hoàn toàn).
- ### 4. Gợi ý 2 cách viết tự nhiên hơn
- 1. **Native style:** "I've been living here for five years." (Nhấn mạnh sự liên tục).
- 2. **Daily style:** "It’s been five years since I moved here."

---

## Slide 21: Kết luận
- **Nội dung**: RTC - Chìa khóa mở cửa AI Sư phạm.
- **Lời nhắn**: Các em hãy luôn nhớ: AI chỉ thực sự hỗ trợ tốt nhất khi bạn biết cách đặt "đề bài" (Prompt) đúng chuẩn.
