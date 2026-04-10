ĐỀ KIỂM TRA TRẮC NGHIỆM - Robot Rover
(Đề 1)
- 30 câu: 12 nhận biết (40%) - 18 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 75% điểm tối đa

Các kiến thức cần đạt | Nhận biết
(12 câu) | Thông hiểu / Vận dụng
(18 câu)
Tổng quát về robot Rover và giao diện lập trình của OhStem | 1,2 | 
Lập trình đơn giản Rover di chuyển và LED |  | 3,4
Xử lý dữ liệu
- Cảm biến gia tốc của robot, các trục nghiêng của robot
- Vận dụng với câu lệnh điều kiện | 5 | 6,7
Lập trình Rover dò đường
- Cảm biến dò đường trên robot
- Câu lệnh cảm biến dò đường | 8 | 9,10
Lập trình Rover né vật cản
- Cảm biến siêu âm trên robot
- Câu lệnh cảm biến siêu âm | 11 | 12,13
Lập trình điều khiển Rover từ xa
- Điều khiển bằng remote IR
- Điều khiển bằng Gamepad trên app OhStem
- Hàm | 14
15 | 16,17,18
Lập trình Yolobit/Rover kết hợp với “lập trình AI” (nhận diện giọng nói)
- Nhóm lệnh “Hiển thị” (màn hình AI Code Runner)
- Nhóm lệnh “Giọng nói”
- Vận dụng chuyển thông tin từ “lập trình AI” đến thiết bị Yolobot/Rover | 19

21 | 20


22,23
Lập trình Yolobit/Rover kết hợp với “mô hình AI” (Teachable machine)
- Quy trình huấn luyện AI (Teachable Machine)
- Ý nghĩa nhóm lệnh “M-Learning” và vận dụng chuyển thông tin từ “lập trình AI” đến thiết bị | 24 | 25,26
Lập trình Rover kết hợp với “bảng điều khiển IOT” (Wifi và IOT dashboard)
- Một số widget trong IOT dashboard
- Ý nghĩa các câu lệnh trong nhóm lệnh MQTT
- Vận dụng gửi dữ liệu từ dashboard đến thiết bị
- Vận dụng gửi dữ liệu từ thiết bị đến dashboard | 27
28 | 29
30

Câu 1 (Nhận biết)
Hãy sắp xếp các tên bộ phận của robot Rover theo theo thứ tự phù hợp của hình sau đây.
![Visual](media/de-trac-nghiem-1-rover/rId6.png)
- A/ Đèn LED nhiều màu
	B/ Động cơ
	C/ Cảm biến siêu âm
	D/ Cảm biến dò đường
	E/ Cổng mở rộng
	F/ Mắt nhận tia hồng ngoại
- A/ C-F-D-E-B-A
- B/ F-D-C-E-B-A
- C/ D-B-A-F-E-C
- D/ D-C-F-A-E-B
Câu 2 (Nhận biết)
Khi bật công tắc nguồn và nhấn nút A trên Yolobit gắn trên robot Rover, đèn trên Yolobit sáng màu xanh dương, hỏi hiện tại robot đang trong chế độ nào?
- A/ Chế độ né tránh vật cản
- B/ Chế độ điều khiển
- C/ Chế độ dò đường
- D/ Chế độ di chuyển theo vật cản
Câu 3 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId7.png)
Robot sẽ thực hiện những hành động gì khi chạy chương trình trên?
- A/ Robot đi tới trong 1 giây sau đó đi lùi mãi mãi; Khi đi tới, đèn LED sáng đèn màu xanh lá, khi đi lùi, đèn LED sáng màu đỏ
- B/ Robot đi tới-lùi sau mỗi 1 giây, lặp lại mãi mãi; Khi đi tới, đèn LED sáng đèn màu xanh lá, khi đi lùi, đèn LED sáng màu đỏ
- C/ Robot đi tới trong 1 giây sau đó đi lùi mãi mãi; Khi đi tới, đèn LED sáng đèn màu đỏ, khi đi lùi, đèn LED sáng màu xanh lá
- D/ Robot đi tới-lùi sau mỗi 1 giây, lặp lại mãi mãi; Khi đi tới, đèn LED sáng đèn màu đỏ, khi đi lùi, đèn LED sáng màu xanh lá
Câu 4 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId8.png)
Robot sẽ thực hiện những hành động gì khi chạy chương trình trên?
- A/ Khi khởi động, đèn LED không sáng và robot xoay vòng tròn theo cùng chiều kim đồng hồ trong 5 giây sau đó đi thẳng trong 1 giây rồi dừng lại. Khi dừng lại, tất cả đèn LED đổi màu xanh lá-đỏ liên tục sau mỗi 1 giây, lặp lại mãi mãi.
- B/ Khi khởi động, đèn LED không sáng và robot xoay vòng tròn ngược chiều kim đồng hồ trong 5 giây sau đó đi thẳng trong 1 giây rồi dừng lại. Khi dừng lại, tất cả đèn LED đổi màu xanh lá-đỏ liên tục sau mỗi 1 giây, lặp lại mãi mãi.
- C/ Khi khởi động, tất cả đèn LED đổi màu xanh lá-đỏ liên tục sau mỗi 1 giây, lặp lại mãi mãi.Trong lúc đèn đổi màu, robot xoay vòng tròn theo cùng chiều kim đồng hồ trong 5 giây sau đó đi thẳng trong 1 giây rồi dừng lại.
- D/ Khi khởi động, tất cả đèn LED đổi màu xanh lá-đỏ liên tục sau mỗi 1 giây, lặp lại mãi mãi.Trong lúc đèn đổi màu, robot xoay vòng tròn ngược chiều kim đồng hồ trong 5 giây sau đó đi thẳng trong 1 giây rồi dừng lại.
Câu 5 (Nhận biết)
Trên robot Rover có cảm biến gia tốc thể hiện qua 3 trục xoay x, y, z, hỏi trục mũi tên màu đỏ thể hiện cho trục nào ?
![Visual](media/de-trac-nghiem-1-rover/rId9.png)
- A/ Trục Y
- B/ Trục X
- C/ Trục Z
Câu 6 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId10.gif)
Đoạn lệnh nào sau đây giúp robot thực hiện hành động trên?
- A/
![Visual](media/de-trac-nghiem-1-rover/rId11.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId12.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId13.png)
![Visual](media/de-trac-nghiem-1-rover/rId14.png)
Câu 7 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId15.png)
Khi bật công tắc nguồn, hỏi robot sẽ thực hiện hành động gì khi nhấn nút A trên Yolobit 5 lần sau đó nhấn nút B?
- A/ Robot di chuyển tới-lùi liên tục
- B/ Robot xoay vòng tròn theo hướng cùng chiều kim đồng hồ
- C/ Robot không di chuyển, đèn LED sáng mỗi đèn một màu khác nhau
- D/ Robot không di chuyển, tất cả đèn LED sáng màu đỏ
Câu 8 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về cảm biến dò đường trên robot Rover ?
(Nhiều đáp án)
- A/ Robot Rover có 4 cảm biến dò line
- B/ Cảm biến dò đường sử dụng sóng siêu âm để nhận biết màu trắng, đen.
- C/ Mỗi cảm biến dò đường gồm một đầu phát và một đầu thu tín hiệu hồng ngoại
- D/ Mắt đọc dò đường sẽ phát ra và thu về hồng ngoại. Tùy theo mức độ hồng ngoại nhận lại mà xác định được bên dưới là vạch đen hay nền trắng.
E/ Phía trên Rover có các đèn báo hiệu tương ứng với từng mắt đọc:đọc được nền đen = đèn sáng, đọc được nền trắng = đèn tắt
Câu 9 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId16.png)
![Visual](media/de-trac-nghiem-1-rover/rId17.png)
![Visual](media/de-trac-nghiem-1-rover/rId18.png)
Khi đặt robot lên vạch kẻ đen như hình trên và chạy câu lệnh sau và nhấn nút B, hỏi đèn pha trên Robot sẽ sáng như thế nào ?
- A/ Đèn pha bên trái sáng, bên phải tắt
- B/ Đèn pha bên trái tắt, bên phải sáng
- C/ Cả hai bên đèn pha đều sáng
- D/ Cả hai bên đèn pha đều tắt
Câu 10 (Thông hiểu)
Đoạn lệnh nào sau đây giúp Rover luôn di chuyển trên vạch đen với 3 trường hợp sau?
![Visual](media/de-trac-nghiem-1-rover/rId19.png)
- A/
![Visual](media/de-trac-nghiem-1-rover/rId20.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId21.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId22.png)
![Visual](media/de-trac-nghiem-1-rover/rId23.png)
Câu 11 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về cảm biến siêu âm trên robot Rover ?
![Visual](media/de-trac-nghiem-1-rover/rId24.png)
- A/ Robot Rover có tổng cộng 2 cảm biến siêu âm
- B/ Cảm biến siêu âm dùng để đo khoảng cách từ cảm biến đến vật cản phía trước
- C/ Cảm biến gồm một đầu phát và một đầu thu tín hiệu hồng ngoại
- D/ Đầu phát tín hiệu ở bên trái, đầu thu tín hiệu ở bên phải
Câu 12 (Thông hiểu)
Đoạn lệnh nào sau đây giúp robot thực hiện yêu cầu sau?
Yêu cầu: Robot di chuyển theo người/đối tượng với một khoảng cách 20-30 cm thì dừng lại.
![Visual](media/de-trac-nghiem-1-rover/rId25.png)
- A/
![Visual](media/de-trac-nghiem-1-rover/rId26.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId27.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId28.png)
![Visual](media/de-trac-nghiem-1-rover/rId29.png)
Câu 13 (Thông hiểu)
Đoạn lệnh nào sau đây KHÔNG giúp robot thực hiện yêu cầu sau?
Yêu cầu: Robot đi thẳng nếu gặp vật cản (khoảng cách từ robot đến vật cản nhỏ hơn 20cm) thì xoay đi hướng khác, sau đó tiếp tục đi thẳng.
![Visual](media/de-trac-nghiem-1-rover/rId30.gif)
- A/
![Visual](media/de-trac-nghiem-1-rover/rId31.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId32.png)
![Visual](media/de-trac-nghiem-1-rover/rId33.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId34.png)
Câu 14 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về remote điều khiển từ xa của robot Rover ?
(Nhiều đáp án)
![Visual](media/de-trac-nghiem-1-rover/rId35.png)
- A/ Tín hiệu truyền từ remote đến robot là tia hồng ngoại
- B/ Tín hiệu truyền từ remote đến robot là sóng siêu âm
- C/ Trên robot có 4 cảm biến dò đường có thể nhận tín hiệu hồng ngoại từ remote, ký hiệu là S1, S2, S3, S4.
- D/ Trên robot có 1 mắt nhận tín hiệu hồng ngoại từ remote đặt ở dưới cảm biến siêu âm của robot
Câu 15 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về app Gamepad của OhStem?
(Nhiều đáp án)
- A/ Để sử dụng app Gamepad cần phải kết nối bluetooth giữa thiết bị dùng Gamepad với Yolobit
- B/ Để sử dụng app Gamepad cần phải kết nối bluetooth giữa thiết bị dùng Gamepad với thiết bị lập trình câu lệnh Yolobit
- C/ Khi kết nối Gamepad với thiết bị sẽ có một biến số “chuỗi” được tạo tự động, đại diện cho tín hiệu truyền đi khi nhấn bất cứ nút nào trên Gamepad
- D/ Sau khi kết nối app Gamepad với thiết bị, ta cần tạo một biến số bất kỳ để nhận tín hiệu được truyền khi nhấn bất cứ nút nào trên Gamepad
Câu 16 (Thông hiểu)
Cho 2 đoạn lệnh A và B như sau:
![Visual](media/de-trac-nghiem-1-rover/rId36.png)
![Visual](media/de-trac-nghiem-1-rover/rId37.png)
Nhận định nào sau đây là đúng khi chạy 2 chương trình trên và nhấn nút B trên Yolobit?
(Nhiều đáp án)
- A/ Ở đoạn lệnh A, trong lúc robot đi tới-lùi 3 lần, robot sẽ có thêm hành động nháy đèn 3 lần.
- B/ Ở đoạn lệnh B, trong lúc robot đi tới-lùi 3 lần xong, sau đó dừng lại rồi mới bắt đầu nháy đèn 3 lần.
- C/ Ở đoạn lệnh A, trong lúc robot đi tới-lùi 3 lần xong, sau đó dừng lại rồi mới bắt đầu nháy đèn 3 lần.
- D/ Ở đoạn lệnh B, trong lúc robot đi tới-lùi 3 lần, robot sẽ có thêm hành động nháy đèn 3 lần.
Câu 17 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId38.gif)
![Visual](media/de-trac-nghiem-1-rover/rId35.png)
Đoạn lệnh nào sau đây giúp robot thực hiện hành động trên?
- A/
![Visual](media/de-trac-nghiem-1-rover/rId39.png)
- B/
![Visual](media/de-trac-nghiem-1-rover/rId40.png)
- C/
- D/
![Visual](media/de-trac-nghiem-1-rover/rId41.png)
![Visual](media/de-trac-nghiem-1-rover/rId42.png)
Câu 18 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId43.png)
Khi chạy chương trình trên, để tất cả đèn LED trên robot sáng màu đỏ ta cần làm gì?
- A/ Nhấn nút A trên Gamepad kết nối bằng bluetooth với robot/Yolobit 1,3,5,... (số lẻ) lần
- B/ Nhấn nút A trên Yolobit 1,3,5,... (số lẻ) lần 
- C/ Nhấn nút A trên remote hồng ngoại 1,3,5,... (số lẻ) lần 
- D/ Không có cách nào để robot sáng đèn đỏ, vì tất cả đèn luôn màu xanh dương do đang kết nối bluetooth
Câu 19 (Nhận biết)
Đáp án nào sau đây thể hiện chính xác trục tọa độ của màn hình Console của chế độ lập trình AI?
![Visual](media/de-trac-nghiem-1-rover/rId44.png)
- A/
![Visual](media/de-trac-nghiem-1-rover/rId45.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId46.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId47.png)
![Visual](media/de-trac-nghiem-1-rover/rId48.png)
Câu 20 (Thông hiểu)
![Visual](media/de-trac-nghiem-1-rover/rId49.png)
Đáp án nào sau đây thể hiện chính xác kết quả của màn hình console khi chạy đoạn lệnh trên ?
- A/
![Visual](media/de-trac-nghiem-1-rover/rId50.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId51.png)
![Visual](media/de-trac-nghiem-1-rover/rId52.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId53.png)
Câu 21 (Nhận biết)
Nhận định nào sau đây là đúng khi nói về nhóm lệnh “Giọng nói” của chế độ lập trình AI?
(Nhiều đáp án)
![Visual](media/de-trac-nghiem-1-rover/rId54.png)
- A/ Khối lệnh thứ 1 có khả năng phát âm một chuỗi ký tự, ngôn ngữ khi nói lên có thể chỉnh sang tiếng Việt bằng khối lệnh thứ 2
- B/ Khối lệnh thứ 1 có khả năng phát âm một chuỗi ký tự, ngôn ngữ khi nói lên có thể chỉnh sang tiếng Việt bằng khối lệnh thứ 6
- C/ Khối lệnh thứ 6 có khả năng thu lại âm thanh từ người dùng rồi chuyển dữ liệu thành một chuỗi ký tự, được lưu ở khối lệnh thứ 8
- D/ Khối lệnh thứ 6 chỉ có khả năng thu lại âm thanh với ngôn ngữ là tiếng Việt, tiếng Anh
E/ Khối lệnh thứ 9 mang giá trị True/False: True khi kết quả nhận diện được có cả hai “từ 1” và “từ 2” trong phần âm thanh nhận diện; Ngược lại, False khi kết quả nhận diện không có một trong hai từ đó.
Câu 22 (Thông hiểu)
Đoạn lệnh nào sau đây tạo nên màn hình console như hình sau:
10 chữ “Hello” viết to dần từ trên xuống dưới
![Visual](media/de-trac-nghiem-1-rover/rId55.png)
- A/
![Visual](media/de-trac-nghiem-1-rover/rId56.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId57.png)
![Visual](media/de-trac-nghiem-1-rover/rId58.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId59.png)
Câu 23 (Thông hiểu)
Đoạn lệnh nào sau đây giúp robot thực hiện yêu cầu sau:
- Điều khiển Rover sáng đèn LED bằng nhận diện giọng nói (Tiếng Việt)
- Khi người dùng nói “Bật đèn Đỏ/Xanh/Vàng” khi đó tất cả đèn sáng màu tương ứng
- Khi người dùng nói “Tắt đèn” khi đó tất cả đèn tắt, nếu không đèn sẽ không tắt hay đổi màu
- A/
![Visual](media/de-trac-nghiem-1-rover/rId60.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId61.png)
![Visual](media/de-trac-nghiem-1-rover/rId62.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId63.png)
Câu 24 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về chế độ “Mô hình AI” và lập trình điều khiển Rover qua việc nhận diện hình ảnh?
(Nhiều đáp án)
- A/ Chế độ “Mô hình AI” có chức năng duy nhất là huấn luyện máy tính nhận diện các sự vật thông qua các hình ảnh được cung cấp
- B/ Khi huấn luyện, ta càng cung cấp nhiều hình ảnh, độ chính xác khi nhận diện hình ảnh càng cao
- C/ Để lập trình robot hoạt động dựa trên các hình ảnh đã huấn luyện, ta cần kết nối bluetooth với tab “Lập trình AI” và kết nối bằng dây hoặc tải chương trình thẳng vào thiết bị Yolobit/Rover.
- D/ Sau khi kết nối bluetooth và tải chương trình vào thiết bị, ta có thể cập nhật trực tiếp những thay đổi ở tab “Mô hình AI” (Ví dụ: Thêm hay đổi tên thêm một nhóm sự vật)
Câu 25 (Thông hiểu)
Hãy sắp xếp thứ tự phù hợp để dùng chế độ “Mô hình AI” và lập trình điều khiển Rover qua việc nhận diện hình ảnh?
	A/ Kết nối Bluetooth và tải chương trình vào thiết bị
	B/ Lập trình ở chế độ “Lập trình AI” và “Lập trình thiết bị”
	C/ Mở chế độ “Mô hình AI”, chọn “Tạo mô hình nhận diện hình ảnh”
	D/ Mở webcam, chụp ảnh hoặc tải ảnh từ máy tính
	E/ Chọn “Huấn luyện mô hình”
	F/ Đặt tên nhóm cần huấn luyện nhận diện hình ảnh hình
	G/ Đặt tên dự án và lưu mô hình
- A/ C-F-D-E-G-B-A
- B/ F-D-C-E-G-B-A
- C/ D-B-A-F-E-G-C
- D/ D-C-F-A-E-G-B
Câu 26 (Thông hiểu)
Đoạn lệnh nào sau đây giúp robot thực hiện yêu cầu sau:
- Điều khiển Rover sáng đèn LED bằng huấn luyện nhận diện hình ảnh
- Khi người giơ 1/2/3 ngón tay, Rover sáng đèn LED màu đỏ/xanh/vàng tương ứng.
- A/
![Visual](media/de-trac-nghiem-1-rover/rId64.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId65.png)
![Visual](media/de-trac-nghiem-1-rover/rId66.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId67.png)
Câu 27 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về chế độ “Bảng điều khiển IOT”?
- A/ Chế độ “Bảng điều khiển IOT” có chức năng gần giống với ứng dụng Gamepad trong chế độ “Lập trình thiết bị” và được kết nối bằng bluetooth với thiết bị
- B/ Chế độ “Bảng điều khiển IOT” vừa có thể là nguồn Input truyền dữ liệu cho thiết bị, vừa có thể là nơi Output các dữ liệu thu thập được qua các cảm biến của thiết bị Yolobit/Rover
- C/ Ta chỉ có thể dùng “Bảng điều khiển IOT” để làm một lúc một trong hai việc: làm nguồn Input truyền dữ liệu cho thiết bị hoặc làm nơi Output các thông tin từ cảm biến
- D/ Các Widget trong “Bảng điều khiển IOT” đều kết nối đến chung một kênh thông tin lớn trong server của OhStem
Câu 28 (Nhận biết)
Để kết nối Wifi, truyền dữ liệu qua lại giữa thiết bị và bảng điều khiển IOT, ta cần tải mục mở rộng nào sau đây?
- A/
![Visual](media/de-trac-nghiem-1-rover/rId68.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId69.png)
![Visual](media/de-trac-nghiem-1-rover/rId70.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId71.png)
Câu 29 (Thông hiểu)
Cho một bảng điều khiển có widget joystick như hình sau:
![Visual](media/de-trac-nghiem-1-rover/rId72.png)
Đoạn lệnh nào sau đây giúp Rover di chuyển theo các hướng của joystick?
- A/
![Visual](media/de-trac-nghiem-1-rover/rId73.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-rover/rId74.png)
![Visual](media/de-trac-nghiem-1-rover/rId75.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId76.png)
Câu 30 (Thông hiểu)
Cho một bảng điều khiển có widget joystick như hình sau:
![Visual](media/de-trac-nghiem-1-rover/rId77.png)
![Visual](media/de-trac-nghiem-1-rover/rId78.png)
Đoạn lệnh nào sau đây giúp Rover thực hiện yêu cầu sau:
- Robot di chuyển hình vuông liên tục, lặp lại cho đến khi nhấn nút B trên Yolobit thì dừng lại
- Mỗi 2 giây, robot gửi thông tin nhiệt độ đo được đến widget biểu đồ trên dashboard
- Robot có chức năng bật/tắt đèn pha bằng công tắc trên dashboard
- A/
![Visual](media/de-trac-nghiem-1-rover/rId79.png)
- B/
![Visual](media/de-trac-nghiem-1-rover/rId80.png)
- C/
![Visual](media/de-trac-nghiem-1-rover/rId81.png)
- D/
![Visual](media/de-trac-nghiem-1-rover/rId82.png)