---
title: "Tiêu chí chấm và thang điểm- Codey M2.docx"
source: "[[Tiêu chí chấm và thang điểm- Codey M2.docx]]"
category: "Robot"
sub_category: "Codey"
type: "RAW_SOURCE"
---

ĐỀ KIỂM TRA THỰC HÀNH - Lập trình robot Codey Module 2
(Đề 1) (Đáp án)

Đề kiểm tra thực hành
Robot Codey (module 2)

1. Yêu cầu:
- Đề thực hành gồm: 2 bài tập lập trình
- Thời gian làm bài: 120 phút
- Yêu cầu nộp bài tập: Nộp file lập trình .mBlock và hình ảnh/video quay lại quá trình robot hoạt động.
Đặt tên file theo mẫu: [Chi nhánh]-[Họ và tên giáo viên]-[Tên môn học]-[Tên bài tập]
[Tên môn học]: Codey 2
Ví dụ: Để nộp bài kiểm tra thực hành 1, giáo viên đặt tên file như sau:  HCM-Nguyễn Văn A-Codey 2-Bai kiem tra thuc hanh

2. Vật tư chuẩn bị:



3. Đề bài:
Hãy lập trình Codey thực hiện nhiệm vụ sau
Bài 1: Khi Codey khởi động, robot đứng yên với màn hình thể hiện khuôn mặt bình thường. Khi nhấn nút A, Codey bắt đầu di chuyển liên tục trên sa bàn. Codey di chuyển cho đến khi người dùng đặt một tấm thẻ màu bất kỳ trên đường đi sa bàn thì dừng di chuyển, xoay một vòng 360 độ, tắt màn hình và dừng lại hoàn toàn.


![Image](../assets/IMG_de_trac_nghiem_1_-_codey_m2_rId44.png)
* Sa bàn có hình dạng là một vòng tròn kín, liên tục, được tạo nên từ băng keo đen và dán trên mặt sàn để robot di chuyển.

Bài 2: Khi Codey khởi động, robot đứng yên với màn hình thể hiện khuôn mặt bình thường. 
Mỗi khi nhấn nút A, Codey sẽ hiện lên màn hình ngẫu nhiên 1 trong 3 chữ “RED / BLUE / GREEN”. Khi đó, người dùng cần cho Codey quét thẻ màu phù hợp. Nếu thẻ màu đúng, Codey sẽ có BIỂU CẢM vui mừng; Nếu thẻ màu sai, Codey sẽ có BIỂU CẢM buồn. Chương trình lặp lại khi nhấn nút A,  khi nhấn nút B thì Codey tắt màn hình và dừng di chuyển.

4. Đáp án:
Code lập trình Bài 1,2:
 
5. Tiêu chí chấm điểm:


Bài 1 (3Đ)


![Image](../assets/IMG_de_trac_nghiem_1_-_codey_m2_rId46.png)
1/ Chương trình có tổng cộng ít nhất 2 sự kiện và 3 câu lệnh điều kiện nằm trong vòng lặp If, repeat until, được sắp xếp như sau:
 <1> - Sự kiện “Khi Codey khởi động”
 <2> - Sự kiện “Khi nhấn nút A”
 <3> ---- Repeat until "Color detect … (thẻ màu tự chọn bất kỳ)"
 <4> -------- If "Color detect “black" (sa bàn có vạch màu đen)
 <5> -------- If "Color detect “white" (sa bàn có nền màu trắng)
(Nếu sa bàn có vạch kẻ và nền màu khác thì chấm dựa theo sa bàn đó)
(0.25x4 = 1đ) 
2/ Sử dụng được 2 câu lệnh sự kiện “Khi khởi động” <1> và “Khi nhấn nút A” <2> để bắt đầu chương trình như đề bài yêu cầu.  (0.5đ)
3/ Sử dụng được câu lệnh Repeat until "Color detect … (thẻ màu tự chọn bất kỳ)" <3> để lập trình được robot kết thúc chương trình khi phát hiện thẻ màu bất kỳ (khác màu so với vạch kẻ và nền của sa bàn). Lập trình được Codey xoay vòng trong 360 độ, tắt màn hình và dừng di chuyển khi phát hiện thẻ màu đó. (0.5đ)


![Image](../assets/IMG_de_trac_nghiem_1_-_codey_m2_rId47.png)
4/  Bên trong vòng lặp “Repeat until”, sử dụng đúng câu lệnh điều kiện “Phát hiện màu … (dựa vào màu sa bàn)” <4,5> để chia các trường hợp khi di chuyển trên sa bàn. (0.5đ)

 (Giả sử sa bàn có vạch kẻ màu đen và nền màu trắng)

![Image](../assets/IMG_de_trac_nghiem_1_-_codey_m2_rId48.png)
5/ Lập trình đúng hành động phù hợp trong mỗi trường hợp phát hiện vạch kẻ/nền của sa bàn
- Phát hiện màu của vạch kẻ: Xoay trái/phải (0.25đ)
- Phát hiện màu của màu nền: Xoay phải/trái (0.25đ)
 (Câu lệnh xoay bình thường hoặc câu lệnh bánh trái-bánh phải đều được)

Bài 2 (7Đ) (Cập nhật)


![Image](../assets/IMG_de_trac_nghiem_1_-_codey_m2_rId49.png)
1/ Chương trình có tổng cộng ít nhất 9 câu lệnh điều kiện nằm trong vòng lặp If, được sắp xếp như sau:
 <1> - Sự kiện “Khi Codey khởi động”
 <2> - Sự kiện “Khi nhấn nút B”
 <3> - Sự kiện “Khi nhấn nút A”
 <4> ---- If "Trường hợp ngẫu nhiên” = “Đỏ”
 <5> -------- If “Phát hiện màu đỏ”
        -------- If “KHÔNG phát hiện màu đỏ”
 <6> ---- If "Trường hợp ngẫu nhiên” = “Xanh dương”
 <7> -------- If “Phát hiện màu xanh dương”
        -------- If “KHÔNG phát hiện màu xanh dương”
 <8> ---- If "Trường hợp ngẫu nhiên” = “Xanh lá”
 <9> -------- If “Phát hiện màu xanh lá”
        -------- If “KHÔNG phát hiện màu xanh lá”
(0.25x12 = 3đ) 
2/ Sử dụng được 3 câu lệnh sự kiện “Khi khởi động” <1>, “Khi nhấn nút A” <2> để bắt đầu và “Khi nhấn nút B” <3> để kết thúc chương trình như đề bài yêu cầu.  (0.5đ)
3/ Sử dụng được câu lệnh Repeat until "Khi nhấn nút B" <3> để lập trình được robot kết thúc chương trình. Lập trình được Codey tắt màn hình và dừng di chuyển khi nhấn nút B. (0.5đ)
3/ Sử dụng được biến số, câu lệnh “pick random” và If để lựa chọn ngẫu nhiên 3 trường hợp màu sắc <4>, <6>, <8>.
- Dùng câu lệnh pick random từ 1 đến 3 (0.5đ) (0.75đ)
- Sử dụng biến số để lưu giá trị random (0.5đ) (0.75đ)
- Sử dụng If và phép so sánh để chia trường hợp (0.5đ)


![Image](../assets/IMG_de_trac_nghiem_1_-_codey_m2_rId50.png)
4/ Trong mỗi trường hợp If <4>, <6>, <8>, lập trình được câu lệnh hiện màn hình chữ “RED” / “BLUE” / “GREEN” và câu lệnh “Đợi 5 giây” trước khi nhận diện màu sắc . (0.5đ)
5/ Trong mỗi trường hợp If, có sử dụng câu lệnh If hoặc If-else và điều kiện phát hiện màu sắc phù hợp để phát hiện thẻ màu được quét có đúng hay không. <5>, <7>, <9>. (0.5đ)


![Image](../assets/IMG_de_trac_nghiem_1_-_codey_m2_rId51.png)
6/ Trong mỗi trường hợp <5>, <7>, <9>, có sử dụng câu lệnh “Emotion” phù hợp theo như đề bài yêu cầu. (0.5đ)
