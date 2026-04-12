Chào bạn, với tư cách là **@scout**, tôi đã trích xuất các sự kiện kỹ thuật và yêu cầu từ nguồn dữ liệu **v04** để xây dựng phương án tuyển chọn 2 đội từ 3 đội hiện có. Việc loại 1 đội cần dựa trên các "điểm chạm" thực tế của cuộc thi (Camera AI, YoloUno, Design Thinking).

Dưới đây là các sự kiện (Facts) và đề xuất hình thức tuyển chọn:

### I. TRÍCH XUẤT SỰ KIỆN (FACTS) TỪ NGUỒN [vv04]

- **Fact 1:** [CONV] Cuộc thi yêu cầu thí sinh phải tham gia đầy đủ các mốc thời gian: Tập huấn (11/10), Sơ loại (01/11), Bán kết (22-23/11) và Chung kết (28/11).
- **Source:** [vv04] - Section: DỮ LIỆU RAW.
- **Tag:** [vv04]

- **Fact 2:** [CONV] Kỹ thuật cốt lõi bao gồm: Lập trình Python, xử lý Camera AI, điện-điện tử cơ bản (Arduino/micro:bit/OhStem) và tư duy thiết kế (Design Thinking).
- **Source:** [vv04] - Section: Gợi ý chuyển hóa thành tiêu chí chọn học sinh (Mục 5).
- **Tag:** [vv04]

- **Fact 3:** [CONV] Vòng Bán kết kéo dài 2 ngày liên tục (22-23/11) tập trung vào thực hiện sản phẩm và triển lãm; Vòng Chung kết yêu cầu thuyết trình sân khấu.
- **Source:** [vv04] - Section: DỮ LIỆU RAW.
- **Tag:** [vv04]

- **Fact 4:** [CONV] Thí sinh bắt buộc phải có thiết bị (laptop/camera AI) để lập trình và vận hành dự án.
- **Source:** [vv04] - Section: Gợi ý chuyển hóa thành tiêu chí chọn học sinh (Mục 2).
- **Tag:** [vv04]

---

### II. ĐỀ XUẤT HÌNH THỨC TUYỂN CHỌN: "AI HACK-PITCH 90 PHÚT"

Để chọn chính xác 2 đội mạnh nhất, bạn nên tổ chức một buổi đánh giá trực tiếp (hoặc online có bật cam) với 3 phần chính:

#### 1. Kiểm tra điều kiện tiên quyết (Pass/Fail)
Dựa trên **Fact 1** và **Fact 4**, đội nào không đáp ứng được các điểm sau sẽ bị loại ngay để tránh rủi ro cho nhà trường:
- **Cam kết thời gian:** 100% thành viên có mặt tại các mốc 01/11, 22-23/11 và 28/11.
- **Sẵn sàng thiết bị:** Đội đã có sẵn laptop đủ cấu hình chạy Python/AI và webcam/thiết bị ngoại vi.

#### 2. Thử thách kỹ thuật nhanh (45 phút) - [Unverified_Source]
Yêu cầu các đội thực hiện một nhiệm vụ nhỏ mô phỏng vòng Bán kết (**Fact 3**):
- **Nhiệm vụ:** Sử dụng một công cụ AI (như Teachable Machine hoặc Python MediaPipe) để nhận diện 2 loại vật thể liên quan đến chủ đề STEM.
- **Yêu cầu:** Giải thích được luồng dữ liệu (Pipeline): Thu thập dữ liệu -> Huấn luyện -> Xuất lệnh điều khiển (giả lập gửi tín hiệu sang YoloUno/Arduino).

#### 3. Thuyết trình giải pháp (Pitching) (15 phút)
Dựa trên **Fact 2** (Design Thinking) và **Fact 3** (Thuyết trình sân khấu):
- Mỗi đội có 5 phút trình bày ý tưởng dự án sẽ làm tại Bán kết.
- **Tiêu chí chấm:** Tính mới của ý tưởng AI, khả năng ứng dụng thực tế, và kỹ năng nói trước đám đông của thành viên đại diện.

---

### III. BẢNG ĐIỂM ĐỀ XUẤT (RUBRIC)

| Tiêu chí | Trọng số | Cách đánh giá |
| :--- | :---: | :--- |
| **Kỹ thuật AI & Phần cứng** | 40% | Khả năng demo nhanh và hiểu logic kết nối Camera AI với Kit điều khiển. |
| **Ý tưởng & Design Thinking** | 30% | Giải pháp có giải quyết đúng vấn đề thực tế không? |
| **Kỹ năng Thuyết trình** | 20% | Sự tự tin, mạch lạc (chuẩn bị cho vòng Chung kết 28/11). |
| **Tính kỷ luật & Cam kết** | 10% | Sự chuẩn bị thiết bị, đúng giờ, thái độ làm việc nhóm. |

**Lời khuyên từ @scout:** Vì vòng Bán kết diễn ra trong 2 ngày liên tiếp (**Fact 3**), bạn nên ưu tiên chọn đội có **sự phân công vai trò rõ ràng** (1 bạn chuyên code AI, 1 bạn chuyên phần cứng/mô hình, 1 bạn chuyên thuyết trình/nội dung). Đội nào "lệch" kỹ năng (ví dụ chỉ biết code mà không biết làm mô hình) sẽ rất khó trụ lại ở vòng triển lãm.