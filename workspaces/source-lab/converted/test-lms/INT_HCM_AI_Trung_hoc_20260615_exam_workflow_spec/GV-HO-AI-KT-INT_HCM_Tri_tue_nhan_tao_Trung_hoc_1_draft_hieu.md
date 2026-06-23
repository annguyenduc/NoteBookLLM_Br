# Draft Câu Hỏi Mức Độ Hiểu

- Khóa học: `INT_HCM_Trí tuệ nhân tạo Trung học 1`
- Số câu: `11`
- Mức độ: `Hiểu`
- Trạng thái: `PREVIEW_DRAFT`

## Câu 11 [Hiểu] [Chọn 1 đáp án đúng]
Trong một dự án “từ điển nói”, sau khi học viên nhập từ tiếng Anh, chương trình phải đọc xong bản dịch rồi mới hiện câu hỏi tiếp theo. Cách thiết kế nào phù hợp nhất?

- A. Hỏi từ cần dịch -> dịch từ -> đọc xong bản dịch -> mới hỏi từ tiếp theo
- B. Hỏi từ cần dịch -> đọc ngay từ gốc -> hỏi từ tiếp theo -> cuối cùng mới dịch
- C. Hỏi từ cần dịch -> dịch từ -> hỏi từ tiếp theo ngay lập tức -> phần đọc chạy trễ phía sau
- D. Hỏi từ cần dịch -> phát âm thanh bất kỳ -> dịch từ -> dừng chương trình

- Đáp án đúng: `B`
- Giải thích: Nếu yêu cầu là chương trình phải đọc xong rồi mới sang bước tiếp theo, cần dùng cách đọc theo luồng tuần tự, không phải kiểu chạy đồng thời.
- Trích dẫn: `Module 4 - Nhóm lệnh chuyển văn bản thành giọng nói - Extension Text to speech`
- Yêu cầu media: Nên có `2 ảnh block` để human đối chiếu hành vi.

## Câu 12 [Hiểu] [Chọn nhiều đáp án đúng]
Chọn tất cả nhận định đúng về `Translate` và `Text to Speech` trong Dancing with AI.

- A. `Translate` tạo ra nội dung văn bản đã được chuyển ngôn ngữ
- B. `Speak` hoặc `Text to Speech` có thể đọc nội dung văn bản thành tiếng
- C. Nếu muốn vừa dịch vừa phát âm, có thể cần kết hợp cả `Translate` và `Speak`
- D. `Translate` tự động bật camera để nhận diện khuôn mặt

- Đáp án đúng: `A, B, C`
- Giải thích: `Translate` làm nhiệm vụ chuyển ngôn ngữ, còn `Speak` hoặc các block của `Text to Speech` dùng để phát âm nội dung. Chúng không có chức năng bật camera hay nhận diện khuôn mặt.
- Trích dẫn: `Module 4 - Nhóm lệnh dịch ngôn ngữ - Extension Translate`; `Module 4 - Nhóm lệnh chuyển văn bản thành giọng nói - Extension Text to speech`
- Yêu cầu media: Nên có ảnh `Translate` và `Speak` để user check đúng hành vi.

## Câu 13 [Hiểu] [Ghép nối]
Ghép đúng công cụ AI với đầu ra hoặc tác dụng chính của nó.

| Cột A | Cột B |
| :--- | :--- |
| 1. `Translate` | a. Phân loại hoặc nhận diện theo model đã dạy |
| 2. `Text to Speech` | b. Trả về nội dung văn bản đã được dịch |
| 3. `Face sensing` | c. Đọc văn bản thành giọng nói |
| 4. `Teachable Machine` | d. Theo dõi vị trí hoặc trạng thái khuôn mặt |

- Đáp án đúng: `1-b, 2-c, 3-d, 4-a`
- Giải thích: Mỗi công cụ AI trong khóa học có một kiểu đầu ra chính khác nhau, nên cần hiểu đúng để ghép vào dự án phù hợp.
- Trích dẫn: `Module 4`; `Module 5`; `Module 6`
- Yêu cầu media: Nên có ảnh block AI hoặc code mẫu ngắn.

## Câu 14 [Hiểu] [Chọn 1 đáp án đúng]
Cho hai cách làm phụ kiện di chuyển theo mặt người dùng:

- Cách 1: liên tục dùng `change y by ...`
- Cách 2: dùng block bám theo `nose bridge` hoặc vị trí khuôn mặt trong `forever`

Giải thích nào đúng nhất?

- A. Cả hai cách luôn cho kết quả giống hệt nhau
- B. Cách 1 có thể làm phụ kiện trôi liên tục ra khỏi vị trí mong muốn, còn cách 2 bám theo vị trí khuôn mặt ổn định hơn
- C. Cách 1 chỉ dùng cho Teachable Machine, cách 2 chỉ dùng cho List
- D. Cách 2 không cần camera

- Đáp án đúng: `B`
- Giải thích: Khi chỉ tăng giảm tọa độ bằng `change y by ...`, vật thể có thể tiếp tục trôi mà không bám đúng mốc khuôn mặt. Dùng landmark như `nose bridge` giúp cập nhật vị trí theo khuôn mặt thực tế.
- Trích dẫn: `Module 5 - Nhóm lệnh nhận diện hình ảnh`; `Module 5 - Tổng kết - Công cụ nhận diện khuôn mặt của Dancing with AI`
- Yêu cầu media: Bắt buộc có `2 ảnh code mẫu so sánh`.

## Câu 15 [Hiểu] [Chọn nhiều đáp án đúng]
Một chương trình lần lượt hỏi người dùng tên, tuổi và màu yêu thích. Muốn lưu được cả ba câu trả lời để dùng về sau, các nhận định nào sau đây là đúng?

- A. Cần gán từng giá trị của `Answer` sang các biến riêng hoặc cấu trúc lưu trữ phù hợp
- B. Chỉ cần đọc biến `Answer` ở cuối chương trình là đủ
- C. Nếu không lưu lại trung gian, `Answer` chỉ giữ câu trả lời cuối cùng
- D. Có thể dùng biến hoặc danh sách tùy nhu cầu thiết kế chương trình

- Đáp án đúng: `A, C, D`
- Giải thích: `Answer` chỉ giữ câu trả lời cuối cùng, nên nếu muốn giữ nhiều dữ liệu thì phải chuyển chúng sang biến riêng hoặc cấu trúc lưu trữ khác như danh sách.
- Trích dẫn: `Module 3 - Khối lệnh "Hỏi - Trả lời"`; `Module 3 - Nhóm lệnh Biến số`; `Module 3 - Khối lệnh về Danh sách - List`

## Câu 16 [Hiểu] [Chọn 1 đáp án đúng]
Danh sách hiện có: `Lan, Minh, Huy, An`. Nếu xóa phần tử ở vị trí của `Huy`, điều gì xảy ra?

- A. Các phần tử phía sau giữ nguyên vị trí tuyệt đối
- B. `An` sẽ được dồn lên một vị trí
- C. Toàn bộ danh sách bị xóa
- D. Chỉ có thể xóa phần tử cuối cùng

- Đáp án đúng: `B`
- Giải thích: Khi xóa một phần tử ở giữa danh sách, các phần tử phía sau sẽ được dồn lên một bậc.
- Trích dẫn: `Module 3 - Khối lệnh về Danh sách - List`

## Câu 17 [Hiểu] [Chọn 1 đáp án đúng]
Trong một dự án có hai nhân vật, nhân vật A đếm ngược xong mới gửi tín hiệu để nhân vật B bắt đầu nói. Cách giải thích nào đúng nhất về việc dùng `broadcast` và `when I receive`?

- A. `Broadcast` giúp A gửi tín hiệu đúng thời điểm để B bắt đầu hành động khi nhận được thông điệp
- B. `Broadcast` giúp A đổi ngôn ngữ giao diện sang tiếng Việt trước khi B xuất hiện
- C. `Broadcast` giúp B tự động đọc được dữ liệu từ camera mà không cần nhận thông điệp
- D. `Broadcast` chỉ dùng khi muốn đổi trang phục, còn truyền tín hiệu nên dùng `Translate`

- Đáp án đúng: `A`
- Giải thích: `Broadcast` gửi thông tin sang các sprite khác, còn `when I receive` giúp sprite nhận tín hiệu và thực hiện hành động đúng lúc.
- Trích dẫn: `Module 3 - Khối lệnh Broadcast - Receive message`

## Câu 18 [Hiểu] [Chọn 1 đáp án đúng]
Một nhóm học viên làm ứng dụng hỗ trợ học từ vựng: nhập từ tiếng Anh, chọn ngôn ngữ đích, hiển thị bản dịch rồi đọc to đúng nội dung vừa dịch. Luồng nào hợp lý nhất?

- A. Nhập từ cần dịch -> chọn ngôn ngữ đích -> dịch kết quả -> đọc đúng phần văn bản vừa dịch
- B. Nhập từ cần dịch -> đọc ngay từ gốc -> chọn ngôn ngữ đích -> bỏ qua bước dịch
- C. Bật `use model` -> nhận diện khuôn mặt -> dịch bản dịch có sẵn -> đọc ngẫu nhiên một từ khác
- D. Chọn ngôn ngữ đích -> xóa danh sách -> đọc một câu mẫu -> mới cho người dùng nhập từ

- Đáp án đúng: `A`
- Giải thích: Đây là chuỗi thao tác logic và đúng với chức năng của công cụ Translate và Text to Speech.
- Trích dẫn: `Module 4 - Translate`; `Module 4 - Text to Speech`

## Câu 19 [Hiểu] [Chọn nhiều đáp án đúng]
Trong một dự án face filter, những cách làm nào sau đây giúp hệ thống hoạt động ổn định và dễ quan sát hơn?

- A. Đặt lệnh bám theo khuôn mặt hoặc landmark bên trong `forever`
- B. Cấp quyền camera cho trình duyệt trước khi chạy dự án
- C. Chỉnh độ trong suốt của camera khi cần để nhìn rõ phụ kiện và nhân vật
- D. Tắt camera ngay từ đầu nhưng vẫn yêu cầu nhận diện khuôn mặt liên tục

- Đáp án đúng: `A, B, C`
- Giải thích: Dự án face filter cần camera, cần cập nhật vị trí liên tục và đôi khi cần điều chỉnh độ trong suốt camera để dễ quan sát.
- Trích dẫn: `Module 5 - Nhóm lệnh nhận diện hình ảnh`; `Module 5 - Tổng kết - Công cụ nhận diện khuôn mặt của Dancing with AI`
- Yêu cầu media: Nên có `1 ảnh block face sensing`.

## Câu 20 [Hiểu] [Chọn 1 đáp án đúng]
Một nhóm muốn làm dự án “MC AI trên sân khấu”: khi người dùng nhập từ tiếng Anh, nhân vật dịch và đọc to kết quả; đồng thời một phụ kiện trên mặt nhân vật thật bám theo chuyển động khuôn mặt. Tổ hợp công cụ nào phù hợp nhất?

- A. `Translate` + `Text to Speech` + `Face sensing`
- B. `Translate` + `List` + `Broadcast`
- C. `Teachable Machine` + `Backdrop` + `Sound effect`
- D. `Motion` + `Looks` + `Body Sensing` nhưng không cần công cụ AI ngôn ngữ

- Đáp án đúng: `A`
- Giải thích: Dự án này cần đồng thời dịch ngôn ngữ, đọc thành tiếng và bám theo khuôn mặt nên phải kết hợp đúng ba công cụ AI tương ứng.
- Trích dẫn: `Module 4`; `Module 5`

## Câu 21 [Hiểu] [Chọn nhiều đáp án đúng]
Trong dự án “Mở khóa bằng Face ID”, học viên nhấn phím `B` để mở camera và nhận diện đúng người đã huấn luyện trước đó. Nếu dự án không chạy đúng, những lỗi hoặc bước xử lý nào sau đây là phù hợp?

- A. Quên bật `turn video on` nên camera chưa mở khi nhấn `B`
- B. Chưa cấp quyền camera cho trình duyệt nên hình camera không hiện
- C. Camera chuyển sang màn hình xám sau khi vừa dùng Teachable Machine ở tab khác, cần đóng tab xung đột hoặc cấp lại quyền camera
- D. Đã copy link model nhưng dán sai hoặc chưa dán vào khối `use model`

- Đáp án đúng: `A, B, C, D`
- Giải thích: Đây đều là các lỗi hoặc tình huống thực tế được nhắc trong tài liệu hướng dẫn và phần lưu ý khi dạy.
- Trích dẫn: `Module 6 - Giới thiệu về trình duyệt "Teachable machine" và cách sử dụng`; `Module 8 - Những lưu ý khi dạy`
- Yêu cầu media: Nên có ảnh `turn video on`, `use model` và ảnh lỗi camera xám để user kiểm tra đúng ngữ cảnh.
