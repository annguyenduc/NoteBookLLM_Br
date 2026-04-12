ĐỀ KIỂM TRA THỰC HÀNH - Lập trình GRobot
(Đề 1)
Đề gồm 3 bài tập lớn, mỗi bài chứa nhiều câu hỏi nhỏ. Mỗi câu hỏi nhỏ được tính theo thang điểm 5.
Nội dung kiến thức bao gồm: LED, phát nhạc, di chuyển, dò đường, tránh vật cản.
Cách thực hiện đề kiểm tra:
Chuẩn bị vật tư: Gbot, sa bàn theo đề bài yêu cầu.
Thực hiện các bài thực hành lập trình trên phần mềm Garastem.
Với mỗi câu hỏi nhỏ của bài tập, giáo viên cần lưu lại 1 file lập trình riêng hoặc lưu lại hình ảnh code lập trình. Ví dụ: Đặt tên file cho câu hỏi 1.1 như sau: “Họ tên - Bài 1.1”.
Thời gian thực hiện bài tập: 2h.
Điểm tối đa: 25 điểm.
Điểm đạt: 14.25 điểm (75%).
Bài 1 - LED, âm thanh, di chuyển
Hãy lập trình cho Gbot  thực thi được các hành động theo các yêu cầu sau:
1.1. Không sử dụng chức năng dò line, khi khởi động, robot di chuyển theo quỹ đạo “số 5”, bắt đầu từ vị trí điểm A và dừng lại ở vị trí điểm D.
Với mỗi đoạn đường di chuyển, vòng đèn LEDs của robot sáng như sau:
- Đoạn AB: màu đỏ
- Đoạn BC: màu vàng
- Đoạn CD: màu xanh dương
![Visual](media/de-thuc-hanh-1-gbot/rId6.png)
1.2. Tiếp nối câu hỏi trên, với mỗi vị trí cột mốc B, C, D, trước khi di chuyển đến vị trí tiếp theo, robot thực hiện các nhiệm vụ như sau:
a/ Tại vị trí điểm B, toàn bộ vòng đèn LEDs đổi màu lần lượt thành đỏ, vàng, xanh dương, lặp lại 3 lần, mỗi lần 0.5 giây.
b/ Tại vị trí điểm C, vòng đèn LEDs sáng đèn ở các vị trí như hình sau trong 3 giây.
![Visual](media/de-thuc-hanh-1-gbot/rId7.png)
c/ Tại vị trí điểm D, robot dừng di chuyển, và phát âm thanh cho đoạn nhạc sau:
![Visual](media/de-thuc-hanh-1-gbot/rId8.png)
Biết rằng cao độ và trường độ của các nốt nhạc được lập trình dựa vào bảng quy đổi các nốt nhạc như sau:
![Visual](media/de-thuc-hanh-1-gbot/rId9.png)
Bài 2 - Cảm biến siêu âm
Cho mê cung có các bức tường bao xung quanh và đặt Gbot ở bên trong như hình sau:
![Visual](media/de-thuc-hanh-1-gbot/rId10.png)
Sử dụng giấy roki, bìa carton hoặc các vật dụng cần thiết để tạo một mê cung như hình minh hoạ ở trên.
Hãy lập trình cho Gbot thực thi được các hành động theo các yêu cầu sau:
Khi khởi động, robot di chuyển bên trong các bức tường. Khi robot gặp bức tường (với khoảng cách nhỏ hơn 5cm), robot sẽ tự động xoay hướng khác và tiếp tục di chuyển thẳng.
Tiếp nối câu hỏi trên, khi gặp vật cản, hướng xoay của robot sẽ được lựa chọn ngẫu nhiên trái hoặc phải. Khi robot di chuyển thẳng và không gặp vật cản, vòng đèn LEDs sáng màu xanh lá; khi robot gặp vật cản và xoay trái, vòng đèn LEDs sáng màu vàng; khi robot gặp vật cản và xoay phải, vòng đèn LEDs sáng màu xanh dương.
Bài 3 - Cảm biến dò line
Cho sa bàn có các vạch kẻ màu đen (độ rộng từ 1.5cm đến 5cm) như hình sau:
![Visual](media/de-thuc-hanh-1-gbot/rId11.png)
Hãy lập trình cho Gbot thực thi được các hành động theo các yêu cầu sau:
3.1. Khi khởi động, robot bắt đầu từ một vị trí bất kỳ trên sa bàn và di chuyển mãi mãi theo vạch kẻ của sa bàn. Trên sa bàn có đặt một vật cản (ví dụ chai nước), nên khi gặp vật cản thì robot phải di chuyển vòng qua vật cản để sau đó lại tiếp tục di chuyển theo vạch kẻ của sa bàn (lưu ý, vòng cung khi robot đi vòng qua vật cản là nhỏ nhất).
![Visual](media/de-thuc-hanh-1-gbot/rId12.png)
3.2. Đặt robot nằm ngoài sa bàn và trên sa bàn sẽ có hai vật cản (ví dụ chai nước) ở vị trí như hình vẽ sau. Hãy lập trình khi khởi động, từ vị trí A bên ngoài sa bàn, robot sáng đèn màu xanh lá và di chuyển thẳng đến khi gặp vật cản tại vị trí B. Khi đó, robot đổi màu đèn LED sang màu vàng và bắt đầu di chuyển trên vạch kẻ của sa bàn. Robot có thể di chuyển mãi trên vạch kẻ của sa bàn. Khi gặp vật cản lần 2 tại vị trí C (vị trí này không cố định), robot dừng di chuyển và tắt vòng đèn LED.
![Visual](media/de-thuc-hanh-1-gbot/rId13.png)
ĐÁP ÁN
Bài 1
1.1.
Lưu ý: Tốc độ quay và thời gian chờ của câu lệnh trong đáp án chỉ mang tính chất tượng trưng. Khi chấm điểm cần kèm theo video quay lại quá trình di chuyển của robot.
![Visual](media/de-thuc-hanh-1-gbot/rId14.png)
1.2.
![Visual](media/de-thuc-hanh-1-gbot/rId15.png)
![Visual](media/de-thuc-hanh-1-gbot/rId16.png)
Bài 2
Lưu ý: Người thực hiện có thể có đáp án khác miễn đáp ứng được yêu cầu đề bài.
![Visual](media/de-thuc-hanh-1-gbot/rId17.png)
Bài 3
3.1.
Lưu ý: Các câu lệnh và tốc độ quay, thời gian chờ của câu lệnh trong đáp án chỉ đại diện cho một cách giải quyết vấn đề. Người thực hiện có thể có đáp án khác miễn đáp ứng được yêu cầu đề bài.
![Visual](media/de-thuc-hanh-1-gbot/rId18.png)
3.2.
Lưu ý: Các câu lệnh và tốc độ quay, thời gian chờ của câu lệnh trong đáp án chỉ đại diện cho một cách giải quyết vấn đề. Người thực hiện có thể có đáp án khác miễn đáp ứng được yêu cầu đề bài. (VD: Sử dụng Wait until, repeat until…)
![Visual](media/de-thuc-hanh-1-gbot/rId19.png)
TIÊU CHÍ VÀ THANG ĐIỂM
Bài 1

Bài tập | Mô tả tiêu chí | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm
Bài tập | Mô tả tiêu chí | 5 | 4 | 3 | 2 | 1
1.1. Robot di chuyển hình “số 5” và sáng đèn vòng đèn LED ở từng đoạn đường:
- AB: đỏ
- BC: vàng
- CD: xanh dương | Đoạn đường robot di chuyển và các câu lệnh được chia làm các phần nhỏ như sau:
  + Khởi động tại điểm A, robot sáng đèn LED màu đỏ.
  + Robot di chuyển thẳng một đoạn AB rồi dừng lại.
  + Robot xoay trái 1 góc phù hợp tại điểm B.
  + Vòng đèn LED đổi sang màu vàng tại điểm B
  + Robot di chuyển thẳng một đoạn BC rồi dừng lại.
  + Robot xoay trái 1 góc phù hợp tại điểm C
  + Vòng đèn LED đổi sang màu xanh dương tại điểm C
  + Robot di chuyển theo đường cong đoạn CD bằng câu lệnh bánh trái, bánh phải và chờ.
  + Robot dừng di chuyển ở vị trí điểm D.

Mỗi đoạn robot di chuyển gần giống với quỹ đạo và có câu lệnh phù hợp, sắp xếp thứ tự chính xác, người làm đạt 1 tiêu chí.

Tổng cộng:  9 tiêu chí | Đạt 9/9 tiêu chí | Đạt 7/9 tiêu chí | Đạt 5/9 tiêu chí | Đạt 3/9 tiêu chí | Đạt 1/9 tiêu chí
1.2.a. Tại điểm B: vòng LED sáng đèn đỏ - vàng - xanh dương, lặp lại 3 lần | - Sử dụng chính xác câu lệnh sáng toàn bộ vòng đèn LED
- Điều chỉnh đúng màu vòng đèn LED theo thứ tự đề bài yêu cầu: đỏ - vàng - xanh dương.
- Các câu lệnh chờ được sắp xếp hợp lý và đúng theo yêu cầu đề bài: mỗi lần 0.5 giây.
- Lặp lại hiệu ứng 3 lần
- Sắp xếp các câu lệnh vào vị trí chính xác để robot thực hiện khi ở vị trí điểm B

Tổng cộng: 4 tiêu chí | Đạt 5/5 tiêu chí | Đạt 4/5 tiêu chí | Đạt 3/5 tiêu chí | Đạt 2/5 tiêu chí | Đạt 1/5 tiêu chí
1.2.b. Tại điểm C: vòng đèn LED sáng một số đèn nhất định | Đáp án gồm 4 câu lệnh, trong đó mỗi câu lệnh được xét theo 3 tiêu chí như sau:
- Sử dụng chính xác câu lệnh sáng 1 đèn LED nhất định
- Điều chỉnh đúng vị trí đèn LED được yêu cầu: 0,3,6,9
- Điều chỉnh màu đúng theo yêu cầu đề bài: vàng - đỏ - xanh lá - xanh dương

Tổng cộng: 12 tiêu chí (3 tiêu chí / 1 câu lệnh) | Đạt 12/12 tiêu chí | Đạt 10/12 tiêu chí | Đạt 8/12 tiêu chí | Đạt 6/12 tiêu chí | Đạt 4/12 tiêu chí
1.2.c. Tại điểm D: phát nhạc | Đáp án gồm 1 câu lệnh dừng di chuyển và 11 câu lệnh phát nhạc.
Mỗi câu lệnh đúng với đáp án, người làm đạt 1 tiêu chí.

Tổng cộng: 12 tiêu chí | Đạt 12/12 tiêu chí | Đạt 10/12 tiêu chí | Đạt 8/12 tiêu chí | Đạt 6/12 tiêu chí | Đạt 4/12 tiêu chí

Bài 2

Bài tập | Mô tả tiêu chí | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm
Bài tập | Mô tả tiêu chí | 5 | 4 | 3 | 2 | 1
2. Robot di chuyển bên trong mê cung kín, xoay một hướng ngẫu nhiên khi gặp bức tường và sáng đèn LED | - Điều chỉnh được câu lệnh cảm biến siêu âm cho đúng cổng kết nối trên robot.  
- Câu lệnh điều kiện, phép toán đúng với yêu cầu đề bài: gặp vật cản với khoảng cách nhỏ hơn 5cm.
- Khi không gặp vật cản, robot di chuyển thẳng.
- Khi không gặp vật cản, robot sáng đèn xanh lá.
- Khi gặp vật cản, robot luôn luôn chỉ xoay được một trong hai hướng trái hoặc phải
- Khi gặp vật cản, robot có thể ngẫu nhiên xoay trái hoặc phải.
- Khi gặp vật cản và xoay, robot có thể sáng đèn LED màu vàng hoặc xanh dương theo yêu cầu đề bài. 

Tổng cộng: 7 tiêu chí | Đạt 7/7 tiêu chí | Đạt 5/7 tiêu chí | Đạt 3/7 tiêu chí | Đạt 2/7 tiêu chí | Đạt 1/7 tiêu chí

Bài 3

Bài tập | Mô tả tiêu chí | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm | Tiêu chí và thang điểm
Bài tập | Mô tả tiêu chí | 5 | 4 | 3 | 2 | 1
3.1. Robot di chuyển mãi mãi bên trong sa bàn và vượt qua vật cản. | - Điều chỉnh được câu lệnh cảm biến siêu âm và cảm biến dò đường cho đúng cổng kết nối trên robot.
- Khi có vật cản, robot có thể tìm đường vòng qua vật cản
- Robot có thể đi thẳng trên những đường line
- Robot có thể rẽ những khúc cua và vẫn đi trên đường line
- Robot có thể tự tìm đường quay trở về đường line khi lệch hẳn khỏi đường line

Tổng cộng: 5 tiêu chí | Đạt 5/5 tiêu chí | Đạt 4/5 tiêu chí | Đạt 3/5 tiêu chí | Đạt 2/5 tiêu chí | Đạt 1/5 tiêu chí
3.2. Robot di chuyển theo các vị trí trên sa bàn | - Điều chỉnh được câu lệnh cảm biến siêu âm và cảm biến dò đường cho đúng cổng kết nối trên robot.
- Khi khởi động, robot có thể di chuyển từ ngoài sa bàn vào trong và dừng lại khi gặp vật cản thứ 1 tại điểm A.
(Có thể sử dụng câu lệnh bất kỳ miễn thỏa được yêu cầu đề bài)
- Nếu bị lệch khỏi vạch kẻ, robot có thể tự tìm đường quay lại vạch kẻ
- Trước khi gặp vật cản lần 2, robot có thể di chuyển hết phần đường line tính đến vị trí C trên vạch kẻ.
- Robot dừng lại hoàn toàn khi gặp vật cản lần 2.
- Robot có thể sáng và tắt đèn đúng với từng đoạn đường mà đề bài yêu cầu.

Tổng cộng: 6 tiêu chí | Đạt 6/6 tiêu chí | Đạt 5/5 tiêu chí | Đạt 4/5 tiêu chí | Đạt 3/5 tiêu chí | Đạt 2/5 tiêu chí
