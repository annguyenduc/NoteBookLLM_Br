# 📊 Bảng đối chiếu Prompt: Non-RTC vs RTC (Toán 10)

Tài liệu này giúp học sinh thấy rõ sự khác biệt giữa việc đặt câu hỏi thông thường và việc áp dụng kỹ thuật Prompt Engineering (mô hình RTC) khi ôn tập Toán 10.

| Chủ đề | Prompt Non-RTC (Máy giải bài) | Prompt RTC (Gia sư thông minh) | Phân tích Sư phạm: Tại sao RTC thắng? |
|---|---|---|---|
| **1. Nhị thức Newton** | "Giải hộ mình bài Nhị thức Newton $(x+2)^5$." | "Bạn là gia sư Toán. Hãy hướng dẫn mình khai triển $(x+2)^5$ theo công thức Nhị thức Newton. Đừng cho đáp án ngay, hãy gợi ý cho mình cách xác định các hệ số $C_n^k$ trước." | **Hậu quả Non-RTC:** Học sinh chỉ chép đáp án, không hiểu bản chất số hạng. <br>**Quyền năng RTC:** Ép AI trở thành người gợi mở, giúp bồi dưỡng tư duy Logic và kỹ năng tính toán. |
| **2. Bất phương trình** | "Cách giải $x^2 - 5x + 6 > 0$?" | "Đóng vai giáo viên Toán. Hãy giải thích cho mình các bước xét dấu tam thức bậc hai $x^2 - 5x + 6$. Hãy liệt kê các lỗi sai phổ biến học sinh hay mắc ở phần này khi giải bất phương trình." | **Hậu quả Non-RTC:** AI trả lời quá vắn tắt, học sinh dễ làm sai khi gặp bài tương tự. <br>**Quyền năng RTC:** AI cung cấp 'Bối cảnh' (Context) về **bẫy kiến thức**, giúp học sinh tự phòng tránh lỗi. |
| **3. Xác suất** | "Bảng xác suất lấy 2 thẻ từ 10 thẻ." | "Bạn là giáo viên Toán giàu kinh nghiệm. Trong bài toán lấy ngẫu nhiên 2 thẻ từ 10 thẻ đánh số từ 1 đến 10, hãy giúp mình liệt kê 'Không gian mẫu' và hướng dẫn mình cách tính xác suất tổng điểm 2 thẻ là số lẻ theo phương pháp sư phạm." | **Hậu quả Non-RTC:** AI liệt kê danh sách dài, gây rối mắt và lười tư duy. <br>**Quyền năng RTC:** Phân hóa đối tượng (Teacher Persona) giúp AI sử dụng ngôn ngữ sư phạm, chia nhỏ bài toán phức tạp. |
| **4. Đường tròn** | "Lập phương trình đường tròn đi qua A(1,1) và B(3,3)." | "Đóng vai gia sư hình học. Hãy hướng dẫn mình các bước xác định tâm I và bán kính R để lập phương trình đường tròn đi qua A(1,1) và B(3,3). Hãy dùng ví dụ này để ôn tập kiến thức về vectơ pháp tuyến." | **Hậu quả Non-RTC:** AI chọn cách nhanh nhất (thường là dùng máy tính), học sinh không ôn lại được các bước trung gian. <br>**Quyền năng RTC:** Kết nối kiến thức cũ (Vectơ) với kiến thức mới (Đường tròn), tạo sự liền mạch. |

---

## 💡 Kết luận cho học sinh:
- **Non-RTC (Prompt Lười):** AI làm hộ bạn -> Bạn trở thành nô lệ của công nghệ.
- **RTC (Prompt Thông minh):** Bạn điều khiển AI -> AI trở thành nô lệ của trí tuệ bạn.

---

---

## 2. Đối chiếu câu trả lời thực tế (AI Response Comparison)

Dưới đây là nội dung trả lời **chính xác và đầy đủ** từ **Gemini-3-Flash** để học sinh thấy rõ sự khác biệt.

### 🔳 Chủ đề 1: Nhị thức Newton

| Loại Prompt | Nội dung phản hồi từ AI |
|:--- |:--- |
| **❌ Non-RTC** | Chào bạn, mình sẽ giúp bạn khai triển biểu thức $(x+2)^5$ bằng công thức Nhị thức Newton nhé.<br><br>**1. Công thức tổng quát:** $(a+b)^n = \sum_{k=0}^{n} C_n^k a^{n-k} b^k$<br>Trong bài này: $a = x, b = 2, n = 5$.<br><br>**2. Các bước khai triển:**<br>$(x+2)^5 = C_5^0 x^5 2^0 + C_5^1 x^4 2^1 + C_5^2 x^3 2^2 + C_5^3 x^2 2^3 + C_5^4 x^1 2^4 + C_5^5 x^0 2^5$<br><br>**3. Kết quả cuối cùng:**<br>$(x+2)^5 = x^5 + 10x^4 + 40x^3 + 80x^2 + 80x + 32$ |
| **✅ RTC** | Chào bạn! Mình rất vui được đồng hành cùng bạn trong bài toán Nhị thức Newton này. Để khai triển $(x+2)^5$, trước hết chúng ta cần xác định các thành phần: $a=x, b=2, n=5$.<br><br>Bây giờ, hãy tập trung vào các hệ số **$C_n^k$**. Có hai cách giúp bạn tìm nhanh:<br>1. **Tam giác Pascal:** Hãy thử viết tiếp dòng 4 và dòng 5 xem dãy số là gì?<br>2. **Mẹo đối xứng:** Các hệ số này luôn đối xứng nhau.<br><br>**Gợi ý:** Bạn hãy liệt kê 6 giá trị của $C_5^0$ đến $C_5^5$ trước, sau đó mình sẽ hướng dẫn lắp vào công thức. Bạn đã tính ra chúng chưa? |

### 🔳 Chủ đề 2: Bất phương trình bậc hai

| Loại Prompt | Nội dung phản hồi từ AI |
|:--- |:--- |
| **❌ Non-RTC** | Để giải bất phương trình $x^2 - 5x + 6 > 0$, ta làm như sau:<br>1. Giải $x^2 - 5x + 6 = 0 \Rightarrow x = 2$ hoặc $x = 3$.<br>2. Xét dấu: Tam thức có $a=1>0$, trong trái ngoài cùng.<br>3. Kết luận: Tập nghiệm là $x < 2$ hoặc $x > 3$. |
| **✅ RTC** | Chào em! Với tư cách là giáo viên Toán, tôi rất vui được cùng em xử lý tam thức: $f(x) = x^2 - 5x + 6$.<br><br>... (Bảng xét dấu và quy tắc Trong trái - Ngoài cùng)...<br><br>**⚠️ CÁC LỖI SAI PHỔ BIẾN CẦN TRÁNH:**<br>1. **Quên dấu hệ số a:** Nhiều bạn mặc định bên ngoài là (+), điều này chỉ đúng khi $a > 0$.<br>2. **Dùng sai ngoặc:** $f(x) > 0$ dùng ngoặc tròn `()`, có dấu bằng thì mới dùng ngoặc vuông `[]`.<br>3. **Lúng túng khi vô nghiệm:** Nếu $\Delta < 0$, tam thức luôn cùng dấu với $a$. |
### 🔳 Chủ đề 3: Xác suất

| **❌ Non-RTC** | Tổng số cách chọn 2 thẻ từ 10 thẻ là $C_{10}^2 = 45$.<br>Bảng xác suất theo tổng:<br>Sum 3: (1,2) P=1/45<br>Sum 4: (1,3) P=1/45...<br>(AI liệt kê danh sách dài các con số). |
| **✅ RTC** | Chào em! Với tư cách giáo viên Toán, tôi dẫn dắt em tư duy: "Trường hợp nào cộng lại sẽ cho số lẻ?"<br>-> À! Đó là **Chẵn + Lẻ = Lẻ**.<br><br>1. **Không gian mẫu:** $n(\Omega) = C_{10}^2 = 45$.<br>2. **Phân loại:** 5 thẻ lẻ, 5 thẻ chẵn.<br>3. **Thuận lợi:** Chọn 1 lẻ và 1 chẵn: $C_5^1 \times C_5^1 = 25$ cách.<br>4. **Xác suất:** $P(A) = 25/45 = 5/9$.<br><br>Em có thấy phương pháp phân tích này giúp bài toán rõ ràng hơn không? |

### 🔳 Chủ đề 4: Hình học Đường tròn

| **❌ Non-RTC** | Đường tròn nhỏ nhất đi qua $A, B$ có tâm là trung điểm $M(2, 2)$, bán kính $R^2 = 2$.<br>Phương trình: $(x-2)^2 + (y-2)^2 = 2$. |
| **✅ RTC** | Chào bạn! Đây là cơ hội tuyệt vời để ôn tập về **Đường trung trực** và **Vectơ pháp tuyến**:<br>1. Tâm $I$ phải cách đều $A, B$ nên $I$ nằm trên đường trung trực của $AB$.<br>2. Vectơ $\vec{AB}(2, 2)$ vuông góc với trung trực nên nó đóng vai trò là **Vectơ pháp tuyến**.<br>3. Nếu chọn $AB$ làm đường kính, tâm $I$ là trung điểm $M(2, 2)$. Hãy thử tính bán kính $R = IA$ rồi viết phương trình nhé! |
