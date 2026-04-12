Dưới đây là các bước tiếp theo để bạn hoàn thiện phần xử lý chuỗi `line` và gửi dữ liệu lên Dashboard IoT. Bạn hãy kéo các khối này đặt vào **ngay sau** khối `đặt buf thành...` (vẫn nằm bên trong vòng lặp **While**).

### 1. Kiểm tra và Tách dữ liệu từ `line`
Vì chuỗi có dạng `TM:nhãn:độ_tin_cậy`, chúng ta cần tìm vị trí các dấu `:` để cắt lấy nội dung ở giữa.

**Các khối cần thêm (theo thứ tự):**

1.  **Nếu** `(trong văn bản [line] tìm sự có mặt đầu tiên của ["TM:"]) = 1`:
    *   *(Mục đích: Đảm bảo dòng này đúng là dữ liệu từ Teachable Machine gửi tới)*
2.  `đặt p1 thành (trong văn bản [line] tìm sự có mặt đầu tiên của [":"])`
3.  `đặt tail thành (trong văn bản [line] lấy từ ký tự thứ (p1 + 1) đến ký tự thứ (độ dài của line))`
    *   *(Biến `tail` lúc này sẽ chứa phần "nhãn:độ_tin_cậy")*
4.  `đặt p2_tail thành (trong văn bản [tail] tìm sự có mặt đầu tiên của [":"])`
5.  `đặt p2 thành (p1 + p2_tail)`
6.  **Cắt lấy Label:** `đặt label thành (trong văn bản [line] lấy từ ký tự thứ (p1 + 1) đến ký tự thứ (p2 - 1))`
7.  **Cắt lấy Score:** `đặt score_str thành (trong văn bản [line] lấy từ ký tự thứ (p2 + 1) đến ký tự thứ (độ dài của line))`
8.  `đặt score thành (đổi văn bản [score_str] sang số)`

---

### 2. Gửi lên Dashboard IoT
Sau khi đã có `label` và `score`, bạn dùng khối IoT để gửi lên 2 kênh V1 và V2.

1.  **Nếu** `(label ≠ last_label)` **hoặc** `(giá trị tuyệt đối của (score - last_score) > 0.05)`:
    *   *(Mục đích: Chỉ gửi khi kết quả thay đổi hoặc độ tin cậy biến động đáng kể để tránh làm nghẽn mạng)*
    *   **Gửi dữ liệu lên server IoT:** Kênh **V1**, giá trị **label**
    *   **Gửi dữ liệu lên server IoT:** Kênh **V2**, giá trị **score**
    *   `đặt last_label thành label`
    *   `đặt last_score thành score`

---

### 3. Lưu ý quan trọng trên Dashboard
Để hiển thị được chữ (nhãn vật thể) trên Dashboard, bạn cần kiểm tra lại Widget:
*   **Widget V1 (TM Label):** Trong phần cài đặt Widget, mục **"Cách hiển thị"**, bạn phải chọn là **"Chuỗi/Văn bản"**. Nếu để mặc định là "Số", nó sẽ hiện số 0 vì nhãn (ví dụ: "Apple") không phải là số.
*   **Widget V2 (TM Score):** Để dạng **"Số"** hoặc **"Đồng hồ"** (Min: 0, Max: 1).

---

### Tóm tắt sự kiện kỹ thuật (Knowledge Distillation)
- Fact: [CONV] [Sử dụng thuật toán tìm vị trí ký tự phân cách (delimiter) để tách chuỗi (parsing) dữ liệu Serial trên YoloBit/ESP32.]
- Source: [v01 - Section: Serial Data Parsing]
- Tag: [vv01]

- Fact: [CONV] [Cơ chế lọc dữ liệu (filtering) bằng cách so sánh giá trị hiện tại với giá trị trước đó (last_label/last_score) giúp giảm băng thông truyền tải lên server IoT.]
- Source: [v01 - Section: IoT Optimization]
- Tag: [vv01]

**Bạn hãy thử ráp các khối này, nếu gặp lỗi "không tách được chuỗi", hãy dùng khối "In ra Serial" để kiểm tra biến `line` xem nó có chứa ký tự lạ nào không nhé!**