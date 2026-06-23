# Draft Câu Hỏi Mức Độ Vận Dụng

- Khóa học: `INT_HCM_Trí tuệ nhân tạo Trung học 1`
- Số câu: `9`
- Mức độ: `Vận dụng`
- Trạng thái: `PREVIEW_DRAFT`

## Câu 22 [Vận dụng] [Chọn 1 đáp án đúng]
Giáo viên muốn học viên làm một ứng dụng nhập từ tiếng Anh, dịch sang tiếng Việt rồi đọc to đúng kết quả vừa dịch. Chương trình mẫu nào dưới đây là hợp lý nhất?

- A. `when green flag clicked -> ask [English word?] and wait -> set [ban_dich] to (translate (answer) to [Vietnamese]) -> speak (ban_dich)`
- B. `when green flag clicked -> ask [English word?] and wait -> speak (answer) -> set [ban_dich] to (translate [hello] to [Vietnamese])`
- C. `when green flag clicked -> ask [English word?] and wait -> set [ban_dich] to (translate (answer) to [Vietnamese]) -> speak (answer)`
- D. `when green flag clicked -> use model [...] -> when model detects [Class 1] -> speak [ban_dich]`

- Đáp án đúng: `A`
- Giải thích: Bài toán yêu cầu nhập từ, dịch ngôn ngữ rồi đọc đúng phần đã dịch. Phương án A dùng đúng chuỗi `ask -> translate(answer) -> speak(ban_dich)`, còn các phương án khác hoặc đọc sai dữ liệu, hoặc bỏ qua bước dịch phù hợp.
- Trích dẫn: `Module 3 - Khối lệnh "Hỏi - Trả lời"`; `Module 4 - Nhóm lệnh dịch ngôn ngữ - Extension Translate`; `Module 4 - Nhóm lệnh chuyển văn bản thành giọng nói - Extension Text to speech`
- Yêu cầu media: Cần `4 ảnh code đáp án` tương ứng `cau_22_a.png` đến `cau_22_d.png`, và `1 file .sb3` để human load kiểm tra phương án đúng.

## Câu 23 [Vận dụng] [Chọn nhiều đáp án đúng]
Trong hoạt động luyện từ vựng nâng cao, học viên phải nhập từ tiếng Anh, chọn một trong ba ngôn ngữ đích, rồi chương trình mới hiển thị và đọc to kết quả. Những thành phần nào cần có để chương trình làm đúng yêu cầu này?

- A. Cách nhận dữ liệu từ người dùng, ví dụ `Ask/Answer`
- B. Biến hoặc danh sách để lưu lựa chọn ngôn ngữ đích nếu chương trình cần dùng lại
- C. Công cụ `Translate` kết hợp với `Text to Speech` hoặc `Speak`
- D. Chỉ cần `Face sensing` là đủ vì có thể đoán ngôn ngữ theo khuôn mặt

- Đáp án đúng: `A, B, C`
- Giải thích: Hoạt động này cần nhập dữ liệu, xử lý dịch và đọc kết quả. `Face sensing` không phải thành phần bắt buộc của bài toán này.
- Trích dẫn: `Module 3 - Khối lệnh "Hỏi - Trả lời"`; `Module 4 - Translate`; `Module 4 - Text to Speech`
- Yêu cầu media: Cần `4 ảnh đáp án` nếu dùng phương án dạng code, và `1 file .sb3` minh họa luồng đúng.

## Câu 24 [Vận dụng] [Chọn nhiều đáp án đúng]
Một dự án face filter có mũ, khuyên tai và cho phép đổi ngẫu nhiên phụ kiện khi nhấn phím `space`. Chọn tất cả nhận định đúng.

- A. Nên dùng `forever` để phụ kiện liên tục bám theo vị trí khuôn mặt hoặc landmark
- B. Có thể dùng sự kiện nhấn phím `space` để kích hoạt việc đổi costume
- C. Có thể chỉ đặt phụ kiện ở một vị trí `x, y` cố định nếu người dùng không di chuyển đầu quá nhiều
- D. Cần chọn landmark phù hợp cho từng phụ kiện, ví dụ vùng đầu cho mũ hoặc vùng tai cho khuyên tai

- Đáp án đúng: `A, B, D`
- Giải thích: Nếu chỉ đặt cố định theo `x, y` thì phụ kiện sẽ không bám đúng khi người dùng di chuyển đầu. Dự án cần camera, landmark phù hợp và sự kiện đổi costume.
- Trích dẫn: `Module 2 - Sự kiện (Events)`; `Module 5 - Nhóm lệnh nhận diện hình ảnh`; `Module 7 - Bài tập thực hành - AI TrH`
- Yêu cầu media: Cần `4 ảnh code đáp án` và `1 file .sb3` để human kiểm tra chính xác block và landmark.

## Câu 25 [Vận dụng] [Chọn nhiều đáp án đúng]
Mục tiêu dạy học là làm một ứng dụng điểm danh bằng AI: mở camera, nhận diện người đã học trước đó và thông báo ai có mặt. Những thành phần nào cần có?

- A. `use model` với link model đã dạy
- B. Camera, ví dụ `turn video on`
- C. Cơ chế phát hiện khi model nhận ra đúng đối tượng
- D. Dùng `Translate` để dịch tên học viên sang tiếng Anh rồi coi như đã điểm danh xong

- Đáp án đúng: `A, B, C`
- Giải thích: Điểm danh bằng AI cần mô hình, camera và cơ chế kích hoạt khi nhận diện đúng đối tượng. Đổi màu không giải quyết bài toán nhận diện.
- Trích dẫn: `Module 6 - Giới thiệu về trình duyệt "Teachable machine" và cách sử dụng`
- Yêu cầu media: Nên có `4 ảnh code đáp án` và `1 file .sb3` minh họa bài toán điểm danh.

## Câu 26 [Vận dụng] [Chọn 1 đáp án đúng]
Trong ứng dụng điểm danh bằng Teachable Machine, giáo viên muốn lưu tên các học viên đã được nhận diện để cuối giờ thông báo ai đã có mặt và ai còn vắng. Cấu trúc dữ liệu nào phù hợp nhất để lưu nhiều tên học viên và cập nhật linh hoạt trong quá trình điểm danh?

- A. Một biến duy nhất và mỗi lần có người mới thì ghi đè tên cũ
- B. Một danh sách (`List`)
- C. Ba biến riêng cố định, mỗi biến cho đúng một học viên, dù số lượng học viên có thể thay đổi
- D. Một phông nền (`Backdrop`) chứa sẵn tên học viên

- Đáp án đúng: `B`
- Giải thích: Danh sách phù hợp để lưu nhiều tên học viên, thêm người mới được nhận diện và kiểm tra ai đã có mặt hoặc còn vắng.
- Trích dẫn: `Module 3 - Khối lệnh về Danh sách - List`; `Module 7 - Bài tập thực hành - AI TrH`
- Yêu cầu media: Nên có `1 ảnh code mẫu lưu danh sách` và `1 file .sb3` để human xem cách lưu tên.

## Câu 27 [Vận dụng] [Chọn nhiều đáp án đúng]
Lớp học cần một ứng dụng có các chức năng sau: điểm danh đầu giờ, lưu danh sách học viên đã có mặt và hiển thị trạng thái cảm xúc cơ bản của học viên khi được nhận diện. Chọn các chương trình mẫu đúng.

- A. `turn video on -> use model -> if detect [An] and [An] not in [co_mat] then add [An] to [co_mat] -> if face is [happy] then show [vui]`
- B. `turn video on -> forever add (detected name) to [co_mat]` mà không kiểm tra trùng lặp -> đổi màu nền mỗi vòng
- C. `when green flag clicked -> clear [co_mat] -> turn video on -> dùng model để nhận diện người -> dùng face sensing để kiểm tra biểu cảm -> chỉ thêm tên khi chưa có trong danh sách`
- D. `translate [happy] to [Vietnamese] -> speak [present]` mà không dùng model, không dùng list

- Đáp án đúng: `A, C`
- Giải thích: Hai chương trình đúng đều có đủ ba phần: nhận diện, kiểm tra trùng khi thêm vào danh sách và xử lý trạng thái khuôn mặt/cảm xúc. Phương án B sai vì thêm trùng liên tục, còn D không có phần điểm danh thật.
- Trích dẫn: `Module 3 - Khối lệnh về Danh sách - List`; `Module 5 - Nhóm lệnh nhận diện hình ảnh`; `Module 6 - Giới thiệu về trình duyệt "Teachable machine" và cách sử dụng`
- Yêu cầu media: Cần `4 ảnh đáp án` nếu dùng code theo phương án và `1 file .sb3` để human load kiểm tra.

## Câu 28 [Vận dụng] [Chọn 1 đáp án đúng]
Trong một face filter nâng cao, người dùng có thể:

- đổi costume của từng phụ kiện,
- quay lại costume nguyên mẫu,
- bật cùng lúc 2 hoặc 3 phụ kiện.

Cách tổ chức nào hợp lý nhất?

- A. `khi nhấn 1 -> bật/tắt mũ; khi nhấn 2 -> bật/tắt kính; khi nhấn R -> tất cả quay về costume gốc; mỗi phụ kiện có biến trạng thái riêng`
- B. `khi nhấn space -> xóa toàn bộ sprite phụ kiện -> tạo lại từ đầu`
- C. `dùng một biến chung tên [phu_kien] cho tất cả phụ kiện, không lưu costume gốc`
- D. `tắt camera mỗi lần đổi costume rồi mở lại sau`

- Đáp án đúng: `A`
- Giải thích: Muốn quản lý nhiều phụ kiện cùng lúc, bật độc lập 2-3 phụ kiện và quay về costume gốc, cần có biến trạng thái rõ ràng cho từng phụ kiện và một cơ chế reset.
- Trích dẫn: `Module 2 - Sự kiện (Events)`; `Module 3 - Biến số`; `Module 5 - Nhóm lệnh nhận diện hình ảnh`; `Module 7 - Bài tập thực hành - AI TrH`
- Yêu cầu media: Cần `4 ảnh code đáp án` và `1 file .sb3` để human kiểm tra cách back về costume gốc và bật đồng thời nhiều phụ kiện.

## Câu 29 [Vận dụng] [Chọn 1 đáp án đúng]
Giả sử giáo viên yêu cầu ứng dụng chấm công cuối giờ phải:

- mở camera đúng lúc,
- nhận diện học viên bằng model AI,
- lưu danh sách học viên đã có mặt,
- chỉ bật camera khi thực sự cần điểm danh và nếu không có người trong một khoảng thời gian thì tự tắt để tiết kiệm năng lượng,
- và cuối giờ thông báo ai vắng.

Phương án thuật toán nào hợp lý nhất?

- A. `khi bắt đầu điểm danh -> turn video on -> dùng model nhận diện -> nếu tên chưa có thì thêm vào list -> nếu 10 giây không phát hiện ai thì turn video off -> cuối giờ so sánh list có mặt với danh sách lớp`
- B. `turn video on` từ đầu buổi đến cuối buổi -> mỗi lần thấy khuôn mặt thì thêm tên vào list, không kiểm tra trùng -> không tự tắt camera
- C. Không bật camera, chỉ phát âm tên học viên lần lượt rồi xem như đã điểm danh
- D. Dùng `Translate` để dịch tên học viên và suy ra ai có mặt

- Đáp án đúng: `A`
- Giải thích: Phương án A có đủ chuỗi xử lý hợp lý: mở camera, dùng model, tránh cộng trùng bằng kiểm tra danh sách, rồi tổng hợp người vắng ở cuối giờ.
- Trích dẫn: `Module 3 - Khối lệnh về Danh sách - List`; `Module 6 - Giới thiệu về trình duyệt "Teachable machine" và cách sử dụng`; `Module 7 - Bài tập thực hành - AI TrH`
- Yêu cầu media: Cần `4 ảnh code đáp án` và `1 file .sb3` để human kiểm tra thuật toán điểm danh.

## Câu 30 [Vận dụng] [Chọn nhiều đáp án đúng]
Giả sử đề bài cuối khóa là:

`Thiết kế một ứng dụng lớp học dùng AI để học viên nhập từ tiếng Anh, chương trình dịch và đọc to kết quả; sau đó có thêm một phần nhận diện khuôn mặt hoặc model AI để tạo tương tác trực quan.`

Những cách tổ chức chương trình hoặc luồng song song nào dưới đây là phù hợp?

- A. Một luồng xử lý nhập từ -> dịch -> đọc kết quả; một luồng khác chờ tín hiệu để bật phần face sensing hoặc model AI khi cần tương tác
- B. Camera chỉ bật khi bước tương tác AI bắt đầu; nếu không có người trong 10 giây thì tự tắt
- C. Mỗi lần đổi costume phụ kiện thì xóa toàn bộ danh sách dữ liệu của dự án để tránh lỗi
- D. Dùng `broadcast` để đồng bộ giữa luồng học từ vựng và luồng tương tác khuôn mặt hoặc model AI

- Đáp án đúng: `A, B, D`
- Giải thích: Phương án đúng cần có luồng xử lý rõ ràng, bật camera đúng lúc để tiết kiệm tài nguyên và có cơ chế đồng bộ giữa các phần của dự án. Xóa toàn bộ dữ liệu mỗi khi đổi costume không phải cách tổ chức hợp lý.
- Trích dẫn: `TEMPLATE_HUONG_DAN_DU_AN.md - Phần trắc nghiệm và yêu cầu biên soạn`; `Module 7 - Bài tập thực hành - AI TrH`; `Module 8 - Vận hành giảng dạy`
- Yêu cầu media: Nên có `4 ảnh chương trình mẫu` tương ứng 4 đáp án, và nếu dựng project minh họa thì có `1 file .sb3`.
