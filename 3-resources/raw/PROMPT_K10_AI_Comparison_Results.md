# Phản hồi thực tế từ AI (Gemini-3-Flash)

## Chủ đề: Nhị thức Newton

### ❌ Prompt Non-RTC (Kết quả thụ động)
Chào bạn, mình sẽ giúp bạn khai triển biểu thức $(x+2)^5$ bằng công thức Nhị thức Newton nhé.

### 1. Công thức tổng quát
Công thức Nhị thức Newton là:
$$(a+b)^n = \sum_{k=0}^{n} C_n^k a^{n-k} b^k$$
Trong đó $C_n^k$ là tổ hợp chập $k$ của $n$ phần tử.

### 2. Áp dụng vào bài toán
Với biểu thức $(x+2)^5$, ta có:
*   $a = x$
*   $b = 2$
*   $n = 5$

Khai triển chi tiết:
$$(x+2)^5 = C_5^0 x^5 2^0 + C_5^1 x^4 2^1 + C_5^2 x^3 2^2 + C_5^3 x^2 2^3 + C_5^4 x^1 2^4 + C_5^5 x^0 2^5$$

### 3. Tính toán từng số hạng
*   $C_5^0 x^5 \cdot 1 = 1 \cdot x^5 \cdot 1 = \mathbf{x^5}$
*   $C_5^1 x^4 \cdot 2 = 5 \cdot x^4 \cdot 2 = \mathbf{10x^4}$
*   $C_5^2 x^3 \cdot 4 = 10 \cdot x^3 \cdot 4 = \mathbf{40x^3}$
*   $C_5^3 x^2 \cdot 8 = 10 \cdot x^2 \cdot 8 = \mathbf{80x^2}$
*   $C_5^4 x^1 \cdot 16 = 5 \cdot x \cdot 16 = \mathbf{80x}$
*   $C_5^5 \cdot 1 \cdot 32 = 1 \cdot 1 \cdot 32 = \mathbf{32}$

### 4. Kết quả cuối cùng
$$(x+2)^5 = x^5 + 10x^4 + 40x^3 + 80x^2 + 80x + 32$$

**Mẹo nhỏ:** Bạn có thể dùng Tam giác Pascal để tìm nhanh các hệ số $C_5^k$ (dòng thứ 5 là: 1, 5, 10, 10, 5, 1) để việc tính toán nhanh hơn.

### ✅ Prompt RTC (Kết quả dẫn dắt - Guided Learning)
Chào bạn! Mình rất vui được đồng hành cùng bạn trong bài toán Nhị thức Newton này.

Để khai triển $(x+2)^5$, trước hết chúng ta cần xác định các thành phần cơ bản trong công thức tổng quát:
$$(a+b)^n = \sum_{k=0}^{n} C_n^k a^{n-k} b^k$$

Trong trường hợp này, ta có:
*   $a = x$
*   $b = 2$
*   $n = 5$

Bây giờ, hãy tập trung vào các hệ số **$C_n^k$** (còn gọi là số tổ hợp chập $k$ của $n$). Với $n=5$, các hệ số này sẽ chạy từ $C_5^0$ đến $C_5^5$.

Có hai cách phổ biến để bạn tìm các hệ số này, bạn hãy chọn cách nào mình thấy dễ hiểu nhất nhé:

### Cách 1: Sử dụng Tam giác Pascal
Bạn hãy viết các dòng của tam giác Pascal cho đến dòng thứ 5 (dòng đầu tiên là dòng 0 chỉ có số 1):
*   Dòng 0: 1
*   Dòng 1: 1  1
*   Dòng 2: 1  2  1
*   Dòng 3: 1  3  3  1
*   ...
**Bạn có thể viết tiếp dòng 4 và dòng 5 không?** Các con số ở dòng 5 chính là các giá trị $C_5^k$ mà chúng ta cần.

### Cách 2: Sử dụng công thức tính tổ hợp
Nếu bạn có máy tính cầm tay hoặc muốn tính tay, hãy dùng công thức:
$$C_n^k = \frac{n!}{k!(n-k)!}$$
Hoặc bấm máy tính: `5` `Shift` `nCr` `k` (với $k$ lần lượt là 0, 1, 2, 3, 4, 5).

**Gợi ý cho bạn:**
Bạn hãy thử liệt kê 6 giá trị của $C_5^0, C_5^1, C_5^2, C_5^3, C_5^4, C_5^5$ ra giấy. Có một đặc điểm thú vị là các hệ số này sẽ **đối xứng** nhau đấy!

Sau khi bạn tìm được dãy số này, mình sẽ hướng dẫn bạn bước tiếp theo là kết hợp chúng với $x$ và $2$ nhé. Bạn đã tính ra các hệ số đó là bao nhiêu chưa?

---

## Chủ đề: Bất phương trình

### ❌ Prompt Non-RTC (Kết quả thụ động)
Để giải bất phương trình $x^2 - 5x + 6 > 0$, bạn có thể thực hiện theo các bước sau:

### Bước 1: Giải phương trình bậc hai tương ứng
Trước hết, ta tìm nghiệm của phương trình:
$$x^2 - 5x + 6 = 0$$

Bạn có thể dùng công thức nghiệm ($\Delta$) hoặc phân tích thành nhân tử:
*   **Phân tích thành nhân tử:** Tìm hai số có tổng là $-5$ và tích là $6$. Đó là $-2$ và $-3$.
    $$(x - 2)(x - 3) = 0$$
*   **Nghiệm:** $x = 2$ hoặc $x = 3$.

### Bước 2: Xét dấu của tam thức bậc hai
Tam thức $f(x) = x^2 - 5x + 6$ có hệ số $a = 1$ (số dương).

Theo quy tắc xét dấu tam thức bậc hai ("Trong trái, ngoài cùng" - trong khoảng hai nghiệm thì trái dấu với $a$, ngoài khoảng hai nghiệm thì cùng dấu với $a$):
*   Trong khoảng $(2; 3)$: $f(x) < 0$ (trái dấu với $a$).
*   Ngoài khoảng $(-\infty; 2)$ và $(3; +\infty)$: $f(x) > 0$ (cùng dấu với $a$).

### Bước 3: Kết luận
Bất phương trình yêu cầu tìm $x$ để $x^2 - 5x + 6 > 0$. Dựa vào kết quả xét dấu ở trên, ta có:

**Nghiệm của bất phương trình là:**
$$x < 2 \quad \text{hoặc} \quad x > 3$$

**Viết dưới dạng tập hợp:**
$$S = (-\infty; 2) \cup (3; +\infty)$$

### ✅ Prompt RTC (Kết quả dẫn dắt - Guided Learning)
Chào em! Với tư cách là giáo viên Toán, tôi rất vui được đồng hành cùng em. Việc xét dấu tam thức bậc hai là nền tảng cực kỳ quan trọng để giải bất phương trình và các bài toán khảo sát hàm số sau này.

Chúng ta sẽ cùng đi qua từng bước để xử lý tam thức: $f(x) = x^2 - 5x + 6$.

---

### PHẦN 1: CÁC BƯỚC XÉT DẤU TAM THỨC BẬC HAI

Để xét dấu biểu thức $f(x) = ax^2 + bx + c$, chúng ta thực hiện theo 3 bước chuẩn sau:

#### Bước 1: Xác định hệ số $a$ và tìm nghiệm của tam thức
*   Hệ số $a = 1$ (vì $1 > 0$, đây là chi tiết rất quan trọng để quyết định dấu).
*   Giải phương trình $x^2 - 5x + 6 = 0$.
    *   Em có thể bấm máy tính hoặc tính $\Delta = (-5)^2 - 4.1.6 = 25 - 24 = 1 > 0$.
    *   Phương trình có hai nghiệm phân biệt: $x_1 = 2$ và $x_2 = 3$.

#### Bước 2: Lập bảng xét dấu
Chúng ta áp dụng quy tắc vàng: **"Trong trái - Ngoài cùng"** (Trong khoảng hai nghiệm thì trái dấu với $a$, ngoài khoảng hai nghiệm thì cùng dấu với $a$).

| $x$ | $-\infty$ | | $2$ | | $3$ | | $+\infty$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |

*Giải thích bảng:*
*   Hệ số $a = 1$ mang dấu **Dương (+)**.
*   **Trong** khoảng hai nghiệm $(2; 3)$: Dấu phải **Trái** với $a$ $\rightarrow$ mang dấu **Âm (-)**.
*   **Ngoài** khoảng hai nghiệm $(-\infty; 2)$ và $(3; +\infty)$: Dấu phải **Cùng** với $a$ $\rightarrow$ mang dấu **Dương (+)**.

#### Bước 3: Kết luận
Dựa vào bảng xét dấu, ta có:
*   $f(x) > 0$ khi $x \in (-\infty; 2) \cup (3; +\infty)$.
*   $f(x) < 0$ khi $x \in (2; 3)$.
*   $f(x) = 0$ khi $x = 2$ hoặc $x = 3$.

---

### PHẦN 2: CÁC LỖI SAI PHỔ BIẾN HỌC SINH HAY MẮC PHẢI

Khi chấm bài, tôi thấy các bạn thường vấp phải những lỗi sau đây, em hãy lưu ý để tránh nhé:

**1. Quên không xét dấu của hệ số $a$:**
Nhiều bạn mặc định lúc nào bên ngoài cũng là dấu $(+)$ và bên trong là dấu $(-)$. Điều này chỉ đúng khi $a > 0$. Nếu gặp bài $-x^2 + 5x - 6$, quy tắc sẽ đảo ngược lại hoàn toàn.

**2. Nhầm lẫn quy tắc "Trong trái - Ngoài cùng" với quy tắc của nhị thức bậc nhất:**
Quy tắc của bậc nhất ($ax+b$) là "Phải cùng - Trái khác". Nhiều bạn học loạn lên rồi áp dụng nhầm "Phải cùng - Trái khác" cho tam thức bậc hai, dẫn đến sai toàn bộ bảng xét dấu.

**3. Sai sót khi sử dụng ký hiệu ngoặc (Tròn `()` vs Vuông `[]`):**
*   Khi giải bất phương trình $f(x) > 0$ hoặc $f(x) < 0$, ta dùng ngoặc tròn `()`.
*   Khi giải bất phương trình có dấu bằng $f(x) \geq 0$ hoặc $f(x) \leq 0$, ta phải dùng ngoặc vuông `[]` tại các giá trị nghiệm.
*   *Lưu ý:* Tại các đầu cực vô cùng $(-\infty; +\infty)$ **luôn luôn** dùng ngoặc tròn.

**4. Dùng sai ký hiệu hợp ($\cup$) và và ($;$):**
Khi kết luận tập nghiệm gồm hai khoảng, phải dùng ký hiệu hợp $\cup$. Nhiều bạn viết $x \in (-\infty; 2)$ và $(3; +\infty)$ hoặc dùng dấu phẩy là chưa chính xác về mặt toán học.

**5. Lỗi khi tam thức vô nghiệm hoặc có nghiệm kép:**
*   Nếu $\Delta < 0$ (vô nghiệm): $f(x)$ luôn **cùng dấu với $a$** với mọi $x$. Nhiều bạn thấy vô nghiệm thì kết luận không xét dấu được hoặc cho bằng 0 là sai.
*   Nếu $\Delta = 0$ (nghiệm kép $x_0$): $f(x)$ luôn **cùng dấu với $a$** với mọi $x \neq x_0$. Tại $x_0$ thì $f(x)=0$. Các bạn hay quên mất điểm $x_0$ này.

**Lời khuyên của giáo viên:** Sau khi lập bảng xét dấu xong, em hãy thử lấy một số bất kỳ trong khoảng đó thay vào biểu thức ban đầu để kiểm tra lại. Ví dụ: Trong khoảng $(2; 3)$, ta chọn $x = 2.5$. Thay vào $f(2.5) = (2.5)^2 - 5(2.5) + 6 = 6.25 - 12.5 + 6 = -0.25$ (Số âm). Đúng với bảng xét dấu!

Chúc em học tốt và không bao giờ mắc phải những lỗi trên nhé!

---

## Chủ đề: Xác suất

### ❌ Prompt Non-RTC (Kết quả thụ động)
Để lập bảng xác suất cho việc lấy 2 thẻ từ 10 thẻ (giả sử các thẻ được đánh số từ 1 đến 10), chúng ta cần xác định rõ hai trường hợp phổ biến nhất:

1.  **Lấy không hoàn lại (Lấy cùng lúc):** Không thể lấy cùng một thẻ hai lần, thứ tự không quan trọng.
2.  **Lấy có hoàn lại:** Có thể lấy cùng một thẻ hai lần, thứ tự có thể quan trọng.

Dưới đây là phân tích và bảng xác suất cho trường hợp phổ biến nhất: **Lấy 2 thẻ không hoàn lại.**

### 1. Thông số cơ bản
*   **Tổng số thẻ:** $n = 10$
*   **Số cách chọn 2 thẻ từ 10 thẻ:** $C_{10}^2 = \frac{10 \times 9}{2} = 45$ cách.
*   **Xác suất của mỗi cặp thẻ cụ thể:** $P = \frac{1}{45} \approx 0,0222$ (hay $2,22\%$).

---

### 2. Bảng phân phối xác suất theo TỔNG của 2 thẻ
Đây là bảng thường được dùng trong các bài toán thống kê. Tổng nhỏ nhất là $1+2=3$ và lớn nhất là $9+10=19$.

| Tổng (S) | Các cặp số có thể | Số cách | Xác suất (Phân số) | Xác suất (%) |
| :--- | :--- | :--- | :--- | :--- |
| **3** | (1,2) | 1 | 1/45 | 2,22% |
| **4** | (1,3) | 1 | 1/45 | 2,22% |
| **5** | (1,4), (2,3) | 2 | 2/45 | 4,44% |
| **6** | (1,5), (2,4) | 2 | 2/45 | 4,44% |
| **7** | (1,6), (2,5), (3,4) | 3 | 3/45 | 6,67% |
| **8** | (1,7), (2,6), (3,5) | 3 | 3/45 | 6,67% |
| **9** | (1,8), (2,7), (3,6), (4,5) | 4 | 4/45 | 8,89% |
| **10** | (1,9), (2,8), (3,7), (4,6) | 4 | 4/45 | 8,89% |
| **11** | (1,10), (2,9), (3,8), (4,7), (5,6) | 5 | 5/45 | 11,11% |
| **12** | (2,10), (3,9), (4,8), (5,7) | 4 | 4/45 | 8,89% |
| **13** | (3,10), (4,9), (5,8), (6,7) | 4 | 4/45 | 8,89% |
| **14** | (4,10), (5,9), (6,8) | 3 | 3/45 | 6,67% |
| **15** | (5,10), (6,9), (7,8) | 3 | 3/45 | 6,67% |
| **16** | (6,10), (7,9) | 2 | 2/45 | 4,44% |
| **17** | (7,10), (8,9) | 2 | 2/45 | 4,44% |
| **18** | (8,10) | 1 | 1/45 | 2,22% |
| **19** | (9,10) | 1 | 1/45 | 2,22% |
| **Tổng** | | **45** | **1/1** | **100%** |

---

### 3. Bảng xác suất theo tính Chẵn/Lẻ
Trong 10 thẻ có 5 thẻ chẵn (2, 4, 6, 8, 10) và 5 thẻ lẻ (1, 3, 5, 7, 9).

| Loại cặp thẻ | Cách tính | Số cách | Xác suất |
| :--- | :--- | :--- | :--- |
| **2 thẻ cùng Lẻ** | $C_5^2$ | 10 | $10/45 \approx 22,2\%$ |
| **2 thẻ cùng Chẵn** | $C_5^2$ | 10 | $10/45 \approx 22,2\%$ |
| **1 Lẻ, 1 Chẵn** | $5 \times 5$ | 25 | $25/45 \approx 55,6\%$ |

---

### 4. Trường hợp Lấy có hoàn lại (Lấy thẻ 1, ghi nhớ, bỏ lại, lấy thẻ 2)
*   **Tổng số kết quả:** $10 \times 10 = 100$.
*   **Xác suất mỗi cặp (có thứ tự):** $1/100 = 1\%$.
*   Trong trường hợp này, bạn có thể lấy được các cặp trùng nhau như (1,1), (2,2)... với xác suất mỗi cặp là 1%.

**Lời khuyên:** Nếu bạn đang làm bài tập toán, hãy sử dụng **Trường hợp 2 (Lấy không hoàn lại)** vì đây là dạng phổ biến nhất trong các đề thi.

### ✅ Prompt RTC (Kết quả dẫn dắt - Guided Learning)
Chào em! Rất vui được đồng hành cùng em trong bài toán xác suất này. Với tư cách là một giáo viên Toán, tôi sẽ không chỉ đưa ra đáp án mà sẽ dẫn dắt em từng bước để em hiểu rõ bản chất vấn đề nhé.

Chúng ta có 10 thẻ đánh số từ 1 đến 10. Lấy ngẫu nhiên 2 thẻ.

---

### Bước 1: Xác định Không gian mẫu ($\Omega$)

Trước hết, em hãy tự hỏi: "Lấy 2 thẻ từ 10 thẻ mà không quan tâm đến thứ tự thì dùng công thức nào?"

Đúng rồi, đó là **Tổ hợp**.

*   **Cách tính:** Số cách chọn 2 thẻ từ 10 thẻ là $C_{10}^2$.
*   **Công thức:** $n(\Omega) = \frac{10 \times 9}{2 \times 1} = 45$.
*   **Liệt kê (để em dễ hình dung):** Các cặp số có thể là (1,2), (1,3)... (1,10), (2,3), (2,4)... (9,10). Tổng cộng có 45 cặp như vậy.

---

### Bước 2: Phân tích điều kiện của biến cố (Tổng là số lẻ)

Bây giờ, chúng ta cần tìm các cặp có tổng là một số lẻ. Tôi có một câu hỏi gợi mở cho em:

> **"Trong toán học, khi cộng hai số lại với nhau, trường hợp nào sẽ cho kết quả là một số lẻ?"**

Em hãy thử nhẩm nhé:
*   Chẵn + Chẵn = ? (Ví dụ: 2 + 4 = 6 -> Chẵn)
*   Lẻ + Lẻ = ? (Ví dụ: 1 + 3 = 4 -> Chẵn)
*   **Chẵn + Lẻ = ? (Ví dụ: 2 + 3 = 5 -> Lẻ)**

À! Vậy để tổng 2 thẻ là số lẻ, bắt buộc chúng ta phải chọn được **một thẻ mang số chẵn và một thẻ mang số lẻ**.

---

### Bước 3: Tính số kết quả thuận lợi cho biến cố ($A$)

Để chọn được 1 thẻ chẵn và 1 thẻ lẻ, chúng ta cần biết trong 10 thẻ đó có bao nhiêu thẻ chẵn, bao nhiêu thẻ lẻ:
*   **Tập hợp số lẻ:** $\{1, 3, 5, 7, 9\}$ $\rightarrow$ Có 5 thẻ.
*   **Tập hợp số chẵn:** $\{2, 4, 6, 8, 10\}$ $\rightarrow$ Có 5 thẻ.

Bây giờ, em hãy thực hiện hai hành động liên tiếp:
1.  Chọn 1 thẻ từ 5 thẻ lẻ: Có $C_5^1 = 5$ cách.
2.  Chọn 1 thẻ từ 5 thẻ chẵn: Có $C_5^1 = 5$ cách.

Theo quy tắc nhân, số cách để lấy được 2 thẻ có tổng lẻ là:
$$n(A) = 5 \times 5 = 25 \text{ (cách)}$$

---

### Bước 4: Tính xác suất

Công thức tính xác suất rất đơn giản: $P(A) = \frac{n(A)}{n(\Omega)}$.

Em thay số vào nhé:
$$P(A) = \frac{25}{45}$$

Rút gọn phân số này cho 5, ta được:
$$P(A) = \frac{5}{9}$$

---

### Tổng kết bài học:
1.  **Không gian mẫu:** $n(\Omega) = 45$.
2.  **Tư duy cốt lõi:** Tổng lẻ = 1 Chẵn + 1 Lẻ.
3.  **Kết quả:** Xác suất là $5/9$ (khoảng 55,5%).

Em có thấy phương pháp phân tích "Chẵn + Lẻ = Lẻ" giúp bài toán trở nên rõ ràng hơn không? Nếu có bước nào chưa rõ, em cứ hỏi tôi nhé!

---

## Chủ đề: Đường tròn

### ❌ Prompt Non-RTC (Kết quả thụ động)
Để lập phương trình đường tròn đi qua hai điểm $A(1, 1)$ và $B(3, 3)$, chúng ta cần lưu ý rằng có **vô số** đường tròn như vậy. Tâm của các đường tròn này luôn nằm trên đường trung trực của đoạn thẳng $AB$.

Dưới đây là hai cách tiếp cận phổ biến:

### Trường hợp 1: Phương trình đường tròn đường kính AB (Đường tròn nhỏ nhất)
Đây là trường hợp cụ thể và phổ biến nhất khi bài toán không cho thêm điều kiện.

1.  **Tìm tâm $I$:** Tâm $I$ là trung điểm của $AB$.
    $$x_I = \frac{1+3}{2} = 2; \quad y_I = \frac{1+3}{2} = 2 \Rightarrow I(2, 2)$$
2.  **Tính bán kính $R$:** $R = IA = \sqrt{(2-1)^2 + (2-1)^2} = \sqrt{1^2 + 1^2} = \sqrt{2}$.
3.  **Phương trình đường tròn:**
    $$(x - 2)^2 + (y - 2)^2 = 2$$

---

### Trường hợp 2: Phương trình tổng quát của họ đường tròn
Nếu bạn cần tìm dạng tổng quát cho tất cả các đường tròn đi qua $A$ và $B$:

1.  **Tìm đường trung trực của $AB$:**
    *   Vectơ $\vec{AB} = (2, 2)$, chọn vectơ pháp tuyến là $\vec{n} = (1, 1)$.
    *   Điểm đi qua là trung điểm $M(2, 2)$.
    *   Phương trình đường trung trực $\Delta$: $1(x-2) + 1(y-2) = 0 \Leftrightarrow x + y - 4 = 0$.
2.  **Tâm $I$ nằm trên $\Delta$:** Gọi $I(a, 4-a)$.
3.  **Bán kính $R^2 = IA^2$:**
    $$R^2 = (a-1)^2 + (4-a-1)^2 = (a-1)^2 + (3-a)^2 = 2a^2 - 8a + 10$$
4.  **Phương trình tổng quát:**
    $$(x - a)^2 + (y - (4-a))^2 = 2a^2 - 8a + 10$$
    *(Với mỗi giá trị của $a$, ta được một đường tròn tương ứng).*

---

**Kết luận:**
*   Nếu bài tập yêu cầu một phương trình cụ thể, bạn nên chọn phương trình đường tròn đường kính $AB$: **$(x - 2)^2 + (y - 2)^2 = 2$**.
*   Nếu đề bài có thêm điều kiện (ví dụ: tâm nằm trên trục $Ox$, hoặc bán kính bằng bao nhiêu đó), bạn hãy thay vào phương trình tổng quát ở Trường hợp 2 để giải tìm $a$.

### ✅ Prompt RTC (Kết quả dẫn dắt - Guided Learning)
Chào bạn! Với tư cách là gia sư hình học, mình rất vui được đồng hành cùng bạn.

Bài toán lập phương trình đường tròn đi qua hai điểm $A(1,1)$ và $B(3,3)$ là một ví dụ tuyệt vời để chúng ta ôn tập về **đường trung trực** và **vectơ pháp tuyến**.

### 1. Phân tích bài toán
Một đường tròn đi qua hai điểm $A$ và $B$ thì tâm $I$ của nó phải cách đều $A$ và $B$ ($IA = IB$).
Trong hình học phẳng, tập hợp các điểm cách đều hai điểm $A$ và $B$ chính là **đường trung trực của đoạn thẳng AB**.

**Lưu ý quan trọng:** Vì đề bài chỉ cho 2 điểm, nên sẽ có **vô số** đường tròn đi qua $A$ và $B$. Tâm $I$ có thể là bất kỳ điểm nào nằm trên đường trung trực của $AB$. Để bài toán cụ thể hơn, mình sẽ hướng dẫn bạn tìm phương trình của "đường tròn đường kính AB" (trường hợp đặc biệt và phổ biến nhất).

---

### 2. Các bước xác định tâm I và bán kính R

#### Bước 1: Tìm trung điểm M của AB
Tâm của đường tròn đường kính $AB$ chính là trung điểm $M$ của đoạn thẳng $AB$.
Công thức: $x_M = \frac{x_A + x_B}{2}; y_M = \frac{y_A + y_B}{2}$
*   $x_M = \frac{1 + 3}{2} = 2$
*   $y_M = \frac{1 + 3}{2} = 2$
=> Vậy tâm **$I(2, 2)$**.

#### Bước 2: Tính bán kính R
Bán kính $R$ chính là khoảng cách từ tâm $I$ đến điểm $A$ (hoặc $B$).
$R = IA = \sqrt{(x_A - x_I)^2 + (y_A - y_I)^2}$
*   $R = \sqrt{(1 - 2)^2 + (1 - 2)^2} = \sqrt{(-1)^2 + (-1)^2} = \sqrt{2}$
=> Vậy **$R = \sqrt{2}$**.

#### Bước 3: Lập phương trình đường tròn
Phương trình có dạng: $(x - a)^2 + (y - b)^2 = R^2$
*   $(x - 2)^2 + (y - 2)^2 = (\sqrt{2})^2$
*   **$(x - 2)^2 + (y - 2)^2 = 2$**

---

### 3. Ôn tập kiến thức về Vectơ pháp tuyến ($\vec{n}$)

Bây giờ, hãy giả sử đề bài yêu cầu tìm một tâm $I$ khác (không phải trung điểm). Khi đó ta phải viết phương trình **đường trung trực $\Delta$ của AB**. Đây là lúc kiến thức về vectơ pháp tuyến phát huy tác dụng.

**Định nghĩa:** Vectơ pháp tuyến của một đường thẳng là vectơ có giá vuông góc với đường thẳng đó.

**Ứng dụng vào bài toán này:**
1.  **Tìm vectơ chỉ phương:** Vectơ $\vec{AB} = (3-1, 3-1) = (2, 2)$.
2.  **Xác định vectơ pháp tuyến:** Vì đường trung trực $\Delta$ vuông góc với đoạn thẳng $AB$, nên vectơ $\vec{AB}$ chính là **vectơ pháp tuyến** của đường trung trực $\Delta$.
    *   $\vec{n}_{\Delta} = \vec{AB} = (2, 2)$.
    *   Để đơn giản, ta có thể chọn $\vec{n}_{\Delta} = (1, 1)$ (vì các vectơ cùng phương đều là vectơ pháp tuyến).

3.  **Viết phương trình đường trung trực $\Delta$:**
    Đường thẳng $\Delta$ đi qua $M(2, 2)$ và có vectơ pháp tuyến $\vec{n} = (1, 1)$:
    *   Công thức: $a(x - x_0) + b(y - y_0) = 0$
    *   $1(x - 2) + 1(y - 2) = 0 \Leftrightarrow x + y - 4 = 0$.

**Kết luận ôn tập:**
*   Nếu bạn có vectơ $\vec{AB} = (a, b)$, thì $\vec{AB}$ sẽ là **vectơ pháp tuyến** của bất kỳ đường thẳng nào vuông góc với $AB$.
*   Mọi điểm $I(x; y)$ nằm trên đường thẳng $x + y - 4 = 0$ đều có thể làm tâm của đường tròn đi qua $A$ và $B$.

### Tóm tắt ghi nhớ:
1.  **Tâm I** nằm trên đường trung trực của $AB$.
2.  **Vectơ $\vec{AB}$** vuông góc với đường trung trực nên nó đóng vai trò là **vectơ pháp tuyến**.
3.  **Bán kính R** luôn bằng khoảng cách từ tâm $I$ vừa tìm được đến một trong hai điểm $A$ hoặc $B$.

Bạn có muốn mình mở rộng thêm bài toán này bằng cách đặt tâm $I$ nằm trên một đường thẳng khác (ví dụ trục $Ox$) không?

---

