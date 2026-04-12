Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v23 theo tiêu chuẩn LOM v4.1:

**1. Lĩnh vực: Robotics & Aerospace (Quy trình hạ cánh sao Hỏa)**
- **Fact:** Sáu thiết bị nổ được kích hoạt đồng thời để loại bỏ mảng chắn nhiệt, giúp lộ mô-đun hạ cánh của tàu thăm dò sao Hỏa.
- **Source:** Đoạn 2 - Quy trình hạ cánh sao Hỏa.
- **Tag:** [vv23]

- **Fact:** Chân hạ cánh của tàu được triển khai bằng thiết bị nổ sau khi mảng chắn nhiệt tách ra 10 giây.
- **Source:** Đoạn 3 - Quy trình hạ cánh sao Hỏa.
- **Tag:** [vv23]

- **Fact:** Radar hạ cánh đo đạc độ cao và tốc độ di chuyển của tàu bằng cách gửi các xung về phía bề mặt sao Hỏa.
- **Source:** Đoạn 4 - Quy trình hạ cánh sao Hỏa.
- **Tag:** [vv23]

- **Fact:** Động cơ của mô-đun hạ cánh phải dừng ngay lập tức tại thời điểm tiếp xúc mặt đất để tránh lật úp tàu.
- **Source:** Đoạn 6 - Quy trình hạ cánh sao Hỏa.
- **Tag:** [vv23]

**2. Lĩnh vực: AI & Software Development (Môi trường ảo & VS Code)**
- **Fact:** Công cụ `virtualenv` (Python) hoặc `conda` (đa ngôn ngữ) được sử dụng để tạo môi trường ảo độc lập trong VS Code.
- **Source:** Conversation: Create Virtual Environment VSCode - Assistant's 1st response.
- **Tag:** [vv23]

- **Fact:** Để kết nối môi trường ảo với VS Code thủ công, cần cấu hình đường dẫn `"python.pythonPath"` trong tệp `settings.json` tại thư mục `.vscode`.
- **Source:** Conversation: Create Virtual Environment VSCode - Step 7.
- **Tag:** [vv23]

**3. Lĩnh vực: IoT & Data Integration (Google Sheets API)**
- **Fact:** Thư viện `gspread` và `pandas` cho phép chuyển đổi dữ liệu từ Google Sheets trực tiếp thành DataFrame để xử lý trong Python.
- **Source:** Conversation: Create Virtual Environment VSCode - Section: "đọc một sheet từ google sheet".
- **Tag:** [vv23]

- **Fact:** Tài khoản dịch vụ (Service Account) của Google Cloud cung cấp địa chỉ email định danh và tệp JSON chứa khóa xác thực để ứng dụng truy cập API mà không cần thông tin đăng nhập cá nhân.
- **Source:** Conversation: Create Virtual Environment VSCode - Section: "SERVICE_ACCOUNT_EMAIL".
- **Tag:** [vv23]

- **Fact:** Tệp JSON của khóa dịch vụ Google Cloud không thể khôi phục nếu bị mất; giải pháp duy nhất là tạo một khóa mới trên Google Cloud Console.
- **Source:** Conversation: Create Virtual Environment VSCode - Section: "Nếu tôi có một tài khoản dịch vụ nhưng bị thất lạc file .json".
- **Tag:** [vv23]

- **Fact:** Lỗi `PERMISSION_DENIED` (403) trong `gspread` thường do người dùng chưa chia sẻ quyền truy cập (Share) tệp Google Sheet cho địa chỉ email của Service Account.
- **Source:** Conversation: Create Virtual Environment VSCode - Section: "gspread.exceptions.APIError".
- **Tag:** [vv23]

- **Fact:** Phương thức `get_all_records()` yêu cầu các tiêu đề cột (headers) trong sheet phải là duy nhất; nếu trùng lặp sẽ gây lỗi `GSpreadException`.
- **Source:** Conversation: Create Virtual Environment VSCode - Section: "gspread.exceptions.GSpreadException".
- **Tag:** [vv23]

**4. Lĩnh vực: Arduino & Robotics (Cảm biến & Servo)**
- **Fact:** Công thức tính khoảng cách bằng cảm biến siêu âm (đơn vị cm) trong Arduino là: `distance = duration * 0.034 / 2`.
- **Source:** Conversation: Servo & Ultrasonic Alert - Arduino Code.
- **Tag:** [vv23]

- **Fact:** Thư viện `Servo.h` trong Arduino IDE cung cấp các hàm `attach()` để khai báo chân tín hiệu và `write()` để điều khiển góc quay của động cơ servo.
- **Source:** Conversation: Servo & Ultrasonic Alert - Arduino Code.
- **Tag:** [vv23]

- **Fact:** Để duy trì trạng thái của hệ thống (ví dụ: giữ servo mở cho đến khi tàu đi qua hết), cần sử dụng biến cờ hiệu (boolean flag) như `obstacleDetected` để kiểm soát logic vòng lặp.
- **Source:** Conversation: Servo & Ultrasonic Alert - Section: "Tôi mong muốn khi tàu đi qua hết thì servo mới đóng lại".
- **Tag:** [vv23]