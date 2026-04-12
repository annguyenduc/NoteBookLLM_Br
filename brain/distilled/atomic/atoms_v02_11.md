Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu mã nguồn và phản hồi của Assistant trong Volume v02:

- **Fact:** Cấu trúc quản lý học tập được thiết kế cho lộ trình dài 32 tuần, chia làm 4 học phần (mỗi học phần kéo dài 8 tuần).
- **Source:** Đoạn mã Python và phản hồi của Assistant ("4 học phần × 8 tuần = 32 tuần").
- **Tag:** [vv02]

- **Fact:** Mỗi lớp học trong hệ thống được định cấu hình phân chia thành 8 nhóm (từ Nhóm 1 đến Nhóm 8) để theo dõi và chấm điểm.
- **Source:** Đoạn mã Python (3 weeks x 8 groups) và phản hồi của Assistant ("8 nhóm / lớp").
- **Tag:** [vv02]

- **Fact:** Các trường dữ liệu (cột) dùng để đánh giá hoạt động học tập bao gồm: Học phần, Tuần, Nhóm, Tên bài học, Điểm cộng (+), Điểm trừ (-), và Tổng điểm.
- **Source:** Danh sách cột trong hàm `build_class_template` của mã nguồn.
- **Tag:** [vv02]

- **Fact:** Hệ thống hỗ trợ tính toán tự động chỉ số "Tổng điểm" dựa trên công thức: Tổng điểm = Điểm cộng (+) − Điểm trừ (-).
- **Source:** Phần đề xuất tính năng của Assistant ("tự động tính Tổng điểm = Điểm + − Điểm -").
- **Tag:** [vv02]

- **Fact:** Mẫu cấu trúc quản lý và theo dõi này được thiết kế chuyên biệt cho đối tượng học sinh khối Lớp 10.
- **Source:** Tên file đầu ra trong phản hồi của Assistant ("Lop10_32tuan_8nhom.xlsx").
- **Tag:** [vv02]

- **Fact:** Công cụ kỹ thuật được sử dụng để khởi tạo và xử lý dữ liệu bảng tính là thư viện Pandas và engine Openpyxl trong ngôn ngữ lập trình Python.
- **Source:** Mã nguồn Python (`import pandas as pd`, `engine="openpyxl"`).
- **Tag:** [vv02]

- **Fact:** Quy trình xử lý tên Sheet trong Excel bao gồm việc giới hạn độ dài (31 ký tự) và loại bỏ/thay thế các ký tự đặc biệt (/, \, ?, *, [, ], :) để đảm bảo tính hợp lệ của tệp tin.
- **Source:** Đoạn mã xử lý biến `clean_name` trong vòng lặp tạo sheet.
- **Tag:** [vv02]

- **Fact:** Cấu trúc 32 tuần chia làm 4 học phần thường là khung chương trình phổ biến cho các môn học STEM, Robotics hoặc Tin học ứng dụng tại Việt Nam.
- **Source:** [Unverified_Source] - Suy luận từ cấu trúc phân bổ thời gian và đối tượng Lớp 10 trong ngữ cảnh giáo dục kỹ thuật.
- **Tag:** [vv02]