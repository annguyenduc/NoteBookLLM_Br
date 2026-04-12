ĐỀ KIỂM TRA TRẮC NGHIỆM - Robot Rover (Không nâng cao)
(Đề 3)
- 60 câu: 12 nhận biết (40%) - 18 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 70% điểm tối đa
- Thời gian làm bài: 40 phút (30 câu)

Các kiến thức cần đạt |  | 
Các kiến thức cần đạt | Nhận biết
(12 câu) | Thông hiểu /
 Vận dụng
(18 câu)
Sử dụng mạch Yolobit và robot Rover
- Các bộ phận, phần cứng trên mạch Yolobit
- Các bước kết nối, lập trình Yolobit
- Chế độ Live và Upload
- Cách reset bộ nhớ trên Yolobit
- Lưu trữ và chia sẻ dự án
- Sử dụng pin Rover
- Các bộ phận, phần cứng trên robot Rover | 1,2,5


                3
                4
                6
                7 | 
Lập trình Rover sáng đèn LED | 8 | 9,10,11
Lập trình Rover di chuyển | 12 | 13,14,15,16
Lập trình Rover điều khiển tay gắp với Servo |  | 17,18
Lập trình hiển thị các thông số của cảm biến
- Vị trí các loại cảm biến (CB nhiệt độ, ánh sáng, gia tốc)
- Hiển thị thông tin với "Cửa sổ thông tin" và "Cửa sổ nhập lệnh"
- Lập trình với nút nhấn A,B
- Biến số | 19 | 21,22,23

20
Lập trình Rover dò đường
- Cảm biến dò đường trên robot
- Câu lệnh cảm biến dò đường | 24 | 25,26
Lập trình Rover né vật cản
- Cảm biến siêu âm trên robot
- Câu lệnh cảm biến siêu âm | 27 | 28
29,30

Câu 1 (Nhận biết)
Chọn tên cảm biến và thiết bị phù hợp với vị trí của nó trên bảng mạch Yolo:Bit
![Visual](media/de-trac-nghiem-3-rover/rId7.png)
1: Nút A
2: Cảm biến nhiệt độ
3: Màn hình LED nhiều màu
4: Cảm biến ánh sáng
5: Nút B
6: Chân cắm mở rộng
Câu 2 (Nhận biết)
Phần cứng nào sau đây KHÔNG được gắn trên mạch Yolobit?
![Visual](media/de-trac-nghiem-3-rover/rId8.png)
- A/ Cảm biến dò đường
- B/ Cảm biến nhiệt độ, độ ẩm
- C/ Anten wifi và Bluetooth
- D/ Cảm biến gia tốc, cảm biến nghiêng
Câu 3 (Nhận biết)
Mục đích của việc reset bộ nhớ trên Yolobit là gì?
(Nhiều đáp án)
- A/ Xóa các câu lệnh đang nhớ để khôi phục cài đặt gốc trên Yolobit
- B/ Rút ngắn thời gian khởi động và chạy chương trình sau khi người dùng đã nạp nhiều chương trình trước đó
- C/ Nạp lại chương trình mặc định cho Rover
- D/ Xóa nhanh tất cả câu lệnh trên giao diện lập trình của máy tính
Câu 4 (Nhận biết)
Để lưu trữ các dự án lập trình Yolobit, người dùng có thể thực hiện bằng (những) cách nào?
- A/ Đặt tên chương trình và nhấn vào nút Lưu  trên thanh công cụ
![Visual](media/de-trac-nghiem-3-rover/rId9.png)
- B/ Nhấn vào nút quản lý chương trình  trên thanh công cụ, chọn “Export Project”
![Visual](media/de-trac-nghiem-3-rover/rId10.png)
- C/ Nhấn vào nút quản lý chương trình  trên thanh công cụ, chọn “Chia sẻ project”, lưu đường dẫn và mã QR
![Visual](media/de-trac-nghiem-3-rover/rId10.png)
- D/ Nhấn vào nút Chức năng cấp cao  trên thanh công cụ, chọn “Lưu project vào thiết bị”
![Visual](media/de-trac-nghiem-3-rover/rId11.png)
Câu 5 (Nhận biết)
Màn hình LED nhiều màu trên mạch Yolobit có bao nhiêu đèn LED?
- A/ 25
- B/ 6
- C/ 20
- D/ 36
Câu 6 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về việc sử dụng pin của robot Rover?
- A/ Khi sạc, đèn trên robot sẽ sáng màu đỏ/cam, khi đầy đèn sẽ sáng màu xanh lá.
- B/ Pin dùng cho Rover có thể sạc qua đêm.
- C/ Pin dùng cho Rover không cần phân biệt cực âm, dương, do đó có thể gắn vào robot chiều nào cũng được.
- D/ Chỉ khi gắn mạch Yolobit vào thân robot Rover, ta mới có thể sạc được pin trên robot.
Câu 7 (Nhận biết)
Nối các bộ phận của robot Rover với tên tương ứng.
![Visual](media/de-trac-nghiem-3-rover/rId12.png)
Số 1: Cảm biến siêu âm
Số 2: Mắt nhận tia hồng ngoại
Số 3: Cảm biến dò đường
Số 4: Cổng mở rộng
Số 5: Động cơ
Số 6: Đèn LED nhiều màu
Câu 8 (Nhận biết)
Khối lệnh nào sau đây có tác dụng làm sáng tất cả đèn LED  trên robot Rover cùng một màu?
- A/
![Visual](media/de-trac-nghiem-3-rover/rId13.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId14.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId15.png)
![Visual](media/de-trac-nghiem-3-rover/rId16.png)
Câu 9 (Thông hiểu)
Đoạn chương trình nào chỉ làm LED số 1 sáng tắt 2 lần sau đó tắt hẳn?
- A/
![Visual](media/de-trac-nghiem-3-rover/rId17.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId18.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId19.png)
![Visual](media/de-trac-nghiem-3-rover/rId20.png)
Câu 10 (Thông hiểu)
Đoạn chương trình nào sau đây phù hợp để lập trình robot sáng đèn LED như hình sau đây khi nhấn nút A trên mạch Yolobit?
![Visual](media/de-trac-nghiem-3-rover/rId21.gif)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId22.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId23.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId24.png)
![Visual](media/de-trac-nghiem-3-rover/rId25.png)
Câu 11 (Thông hiểu)
Đoạn chương trình nào chỉ làm LED số 1 sáng tắt 2 lần sau đó tắt hẳn?
- A/
![Visual](media/de-trac-nghiem-3-rover/rId26.png)
- B/
- C/
- D/
![Visual](media/de-trac-nghiem-3-rover/rId27.png)
![Visual](media/de-trac-nghiem-3-rover/rId19.png)
![Visual](media/de-trac-nghiem-3-rover/rId28.png)
Câu 12 (Nhận biết)
Quỹ đạo di chuyển nào sau đây là đúng khi nói về khối lệnh di chuyển dưới đây?
![Visual](media/de-trac-nghiem-3-rover/rId29.png)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId30.png)
- B/ 
- C/ 
- D/
![Visual](media/de-trac-nghiem-3-rover/rId31.png)
![Visual](media/de-trac-nghiem-3-rover/rId32.png)
![Visual](media/de-trac-nghiem-3-rover/rId33.png)
Câu 13 (Thông hiểu)
Robot di chuyển như thế nào khi nạp đoạn lệnh dưới đây và nhấn nút A?
- A/
![Visual](media/de-trac-nghiem-3-rover/rId34.png)
![Visual](media/de-trac-nghiem-3-rover/rId35.gif)
- B/
- C/
- D/
![Visual](media/de-trac-nghiem-3-rover/rId36.gif)
![Visual](media/de-trac-nghiem-3-rover/rId37.gif)
![Visual](media/de-trac-nghiem-3-rover/rId38.gif)
Câu 14 (Thông hiểu)
![Visual](media/de-trac-nghiem-3-rover/rId39.png)
Đoạn lệnh nào còn thiếu trong chương trình sau đây để robot đi được quỹ đạo như hình trên.
![Visual](media/de-trac-nghiem-3-rover/rId40.png)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId41.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId42.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId43.png)
![Visual](media/de-trac-nghiem-3-rover/rId44.png)
Câu 15 (Thông hiểu)
![Visual](media/de-trac-nghiem-3-rover/rId45.gif)
Đoạn lệnh nào còn thiếu trong chương trình dưới đây để lập trình robot có hiệu ứng di chuyển và đèn LED lặp lại mãi mãi như hình trên?
![Visual](media/de-trac-nghiem-3-rover/rId46.png)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId47.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId48.png)
![Visual](media/de-trac-nghiem-3-rover/rId49.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId50.png)
Câu 16 (Thông hiểu)
![Visual](media/de-trac-nghiem-3-rover/rId51.png)
Robot sẽ thực hiện những hành động gì khi chạy chương trình trên?
- A/ Robot đi tới trong 1 giây sau đó đi lùi mãi mãi; Khi đi tới, đèn LED sáng đèn màu xanh lá, khi đi lùi, đèn LED sáng màu đỏ.
- B/ Robot đi tới-lùi sau mỗi 1 giây, lặp lại mãi mãi; Khi đi tới, đèn LED sáng đèn màu xanh lá, khi đi lùi, đèn LED sáng màu đỏ.
- C/ Robot đi tới trong 1 giây sau đó đi lùi mãi mãi; Khi đi tới, đèn LED sáng đèn màu đỏ, khi đi lùi, đèn LED sáng màu xanh lá.
- D/ Robot đi tới-lùi sau mỗi 1 giây, lặp lại mãi mãi; Khi đi tới, đèn LED sáng đèn màu đỏ, khi đi lùi, đèn LED sáng màu xanh lá.
Câu 17 (Thông hiểu)
Sử dụng động cơ Servo, đoạn chương trình nào sau đây phù hợp để lập trình robot đóng, mở tay gắp, lặp lại mãi mãi như hình sau đây?
![Visual](media/de-trac-nghiem-3-rover/rId52.gif)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId53.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId54.png)
![Visual](media/de-trac-nghiem-3-rover/rId55.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId56.png)
Câu 18 (Thông hiểu)
Sử dụng động cơ Servo, đoạn chương trình nào sau đây phù hợp để lập trình robot thực hiện yêu cầu sau:
- Mỗi khi nhấn nút A trên mạch Yolobit, tay gắp sẽ mở thêm một góc 30 độ.
- Mỗi khi nhấn nút B trên mạch Yolobit, tay gắp sẽ đóng lại một góc 30 độ.
- A/
![Visual](media/de-trac-nghiem-3-rover/rId57.png)
- B/
- C/
- D/
![Visual](media/de-trac-nghiem-3-rover/rId58.png)
![Visual](media/de-trac-nghiem-3-rover/rId59.png)
![Visual](media/de-trac-nghiem-3-rover/rId60.png)
Câu 19 (Nhận biết)
Phần cứng khoanh tròn dưới đây trên mạch Yolobit được gọi là gì?
![Visual](media/de-trac-nghiem-3-rover/rId61.png)
- A/ Cảm biến gia tốc
- B/ Cảm biến ánh sáng
- C/ Cảm biến nhiệt độ, độ ẩm
- D/ Vi xử lý
Câu 20 (Thông hiểu)
Đoạn chương trình nào thực hiện yêu cầu sau đây:
- Khi khởi động, Rover đứng yên và tắt hết đèn.
- Mỗi khi nhấn nút A, tất cả đèn trên Rover đổi màu 3 lần xong tắt đi.
(Nhiều đáp án)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId62.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId63.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId64.png)
![Visual](media/de-trac-nghiem-3-rover/rId65.png)
Câu 21 (Thông hiểu)
Cho yêu cầu sau:
- Khi khởi động, robot tắt tất cả đèn LED.
- Khi nhấn nút A, hiện lên màn hình Yolobit mức nhiệt độ hiện tại.
- Khi nhấn nút B, hiện lên màn hình Yolobit mức độ sáng hiện tại.
Đoạn lệnh nào để robot thực hiện được yêu câu trên?
- A/
![Visual](media/de-trac-nghiem-3-rover/rId66.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId67.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId68.png)
![Visual](media/de-trac-nghiem-3-rover/rId69.png)
Câu 22 (Thông hiểu)
Cho chương trình như sau:
![Visual](media/de-trac-nghiem-3-rover/rId70.png)
Kết quả của chương trình khi người dùng đặt Rover ở nhiều vị trí khác nhau trong phòng:
- A/ Rover hiển thị mức độ sáng lên màn hình lập trình và màn hình LED trên mạch Yolobit mỗi 0.5 giây
- B/ Rover hiển thị mức độ sáng lên màn hình lập trình và cửa sổ nhập lệnh mỗi 0.5 giây
- C/ Rover hiển thị mức độ sáng lên cửa sổ nhập lệnh và màn hình LED trên mạch Yolobit mỗi 0.5 giây
- D/ Rover không hiển thị gì cả vì chương trình bị lỗi
Câu 23 (Thông hiểu)
Hãy lựa chọn chương trình phù hợp để điều khiển robot liên tục  hiển thị số đo khoảng cách lên màn hình lập trình và màn hình LED trên mạch Yolobit khi đặt vật cản ở các khoảng cách khác nhau trước robot.
![Visual](media/de-trac-nghiem-3-rover/rId71.gif)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId72.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId73.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId74.png)
![Visual](media/de-trac-nghiem-3-rover/rId75.png)
Câu 24 (Nhận biết)
Cảm biến dò đường của Rover có bao nhiêu mắt cảm biến?
- A/ 2
- B/ 3
- C/ 4
- D/ 5
Câu 25 (Thông hiểu)
Đặt robot lên vạch kẻ đen và cho đoạn chương trình như hình sau đây:
![Visual](media/de-trac-nghiem-3-rover/rId76.png)
![Visual](media/de-trac-nghiem-3-rover/rId77.png)
![Visual](media/de-trac-nghiem-3-rover/rId78.png)
Hỏi đèn pha trên Robot sẽ sáng như thế nào?
- A/ Đèn pha bên trái sáng, bên phải tắt.
- B/ Đèn pha bên trái tắt, bên phải sáng.
- C/ Cả hai bên đèn pha đều sáng.
- D/ Cả hai bên đèn pha đều tắt.
Câu 26 (Thông hiểu)
Hãy lựa chọn chương trình phù hợp nhất để điều khiển robot di chuyển mãi mãi bên trong vòng tròn đen đến khi tìm được lối ra.
![Visual](media/de-trac-nghiem-3-rover/rId79.png)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId80.png)
- B/
![Visual](media/de-trac-nghiem-3-rover/rId81.png)
- C/
![Visual](media/de-trac-nghiem-3-rover/rId82.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId83.png)
Câu 27 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về cảm biến siêu âm trên robot Rover ?
![Visual](media/de-trac-nghiem-3-rover/rId84.png)
- A/ Robot Rover có tổng cộng 2 cảm biến siêu âm.
- B/ Cảm biến siêu âm dùng để đo khoảng cách từ cảm biến đến vật cản phía trước.
- C/ Cảm biến gồm một đầu phát và một đầu thu tín hiệu hồng ngoại.
- D/ Đầu phát tín hiệu ở bên trái, đầu thu tín hiệu ở bên phải.
Câu 28 (Thông hiểu)
Đâu là ứng dụng của cảm biến siêu âm trên Rover?
(Nhiều đáp án)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId71.gif)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId85.gif)
https://drive.google.com/file/d/1yQJT-aOCp8VwyT59W6a5Er7q12BqyeO1/view?usp=drive_link 
- D/
![Visual](media/de-trac-nghiem-3-rover/rId86.png)
![Visual](media/de-trac-nghiem-3-rover/rId88.png)
https://drive.google.com/file/d/1lmbcyK3qXMiyOjxF9JwRuyJKWETTMW6p/view?usp=drive_link
Câu 29 (Thông hiểu)
Đoạn lệnh nào sau đây giúp robot thực hiện yêu cầu sau?
Yêu cầu: Robot di chuyển theo người/đối tượng với một khoảng cách 20-30 cm thì dừng lại.
![Visual](media/de-trac-nghiem-3-rover/rId90.png)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId91.png)
- B/
![Visual](media/de-trac-nghiem-3-rover/rId92.png)
- C/
![Visual](media/de-trac-nghiem-3-rover/rId93.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId94.png)
Câu 30 (Thông hiểu)
Đặt robot Rover trong một vòng tròn có vạch kẻ đen, cùng các chướng ngại vật như hình sau:
![Visual](media/de-trac-nghiem-3-rover/rId95.png)
Hãy lựa chọn chương trình phù hợp để điều khiển robot di chuyển mãi mãi bên trong vòng tròn và báo hiệu tín hiệu khi gặp chướng ngại vật. 
Khi gặp chướng ngại vật, robot dừng di chuyển và phát âm thanh. Đợi đến khi người dùng lấy chướng ngại vật ra ngoài và nhấn nút A, robot mới tiếp tục công việc di chuyển trong vòng tròn và tìm vật cản.
Đoạn lệnh nào còn thiếu trong chương trình sau đây để robot thực hiện yêu cầu trên?
![Visual](media/de-trac-nghiem-3-rover/rId96.png)
- A/
![Visual](media/de-trac-nghiem-3-rover/rId97.png)
- B/
- C/
![Visual](media/de-trac-nghiem-3-rover/rId98.png)
![Visual](media/de-trac-nghiem-3-rover/rId99.png)
- D/
![Visual](media/de-trac-nghiem-3-rover/rId100.png)