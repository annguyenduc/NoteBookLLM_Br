ĐỀ KIỂM TRA TRẮC NGHIỆM - AI Arduino
(Đề 2)
- 30 câu: 12 nhận biết (40%) - 18 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 70% điểm tối đa
- Thời lượng: 60ph

Các kiến thức cần đạt | Nhận biết
(12 câu) | Thông hiểu / Vận dụng
(18 câu)
Tổng quan sử dụng Arduino và giao diện phần mềm mBlock5 | 1,2,3 | 
Cấu tạo và cách sử dụng linh kiện điện tử
- LED đơn
- LED siêu sáng
- Còi Buzzer
- Đèn Laser diode 8cm 3-5V
- Động cơ rung 0834 3-5V
- Mạch thu phát âm thanh ISD1820
- Động cơ Servo
- Breadboard | 4


5
6,7
8
9 | 10

11,12,13
Lập trình điều khiển các linh kiện điện tử
- Event green flag, key pressed, vòng lặp
- Biến số, Repeat Until |  | 14,15,16,17
18,19,20
Lập trình điều khiển các nhân vật truyền tín hiệu qua lại với linh kiện điện tử
- Sử dụng sự kiện khi nhấn nút bàn phím
- Broadcast-Receive message | 21 | 22,23,24
Lập trình nhận diện giọng nói bằng extension Cognitive Services | 25 | 26,27
Lập trình nhận diện hình ảnh bằng extension Teachable Machine | 28 | 29,30

Câu 1 (Nhận biết)
Khẳng định nào dưới đây là SAI?
- A/ Có thể cấp nguồn cho arduino thông qua pin với chân 3,3V hoặc 5V.
- B/ Có thể cấp nguồn cho arduino bằng cách kết nối với máy tính thông qua dây cáp.
- C/ Có thể cấp nguồn cho arduino thông qua dây adapter 9V.
- D/ Có thể cấp nguồn cho arduino thông qua pin với cổng Vin.
Câu 2 (Nhận biết)
Nối tên với các bộ phận tương ứng
![Visual](media/de-2-trac-nghiem-ai-arduino/rId7.png)
- A/ Nút reset
- B/ Cổng USB - type B
- C/ Jack DC
- D/ Các chân nguồn
E/ Các chân pin (chân tín hiệu)
Câu 3 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về chế độ Live và chế độ Upload khi lập trình Arduino trên mBlock5?
- A/ Chế độ Live chỉ hoạt động trong quá trình mở mBlock5 và kết nối với board Arduino.
- B/ Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta ngắt kết nối giữa hai thiết bị, chương trình được tải lên sẽ bị xóa khỏi bộ nhớ của Arduino.
- C/ Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta xóa câu lệnh ở khu vực lập trình, chương trình hoạt động của Arduino sẽ bị thay đổi ngay lập tức.
- D/ Với chế độ Live, ta có thể thấy trực tiếp chương trình đang chạy đến khối lệnh nào khi chọn “Setting - Update firmware - OK”.
Câu 4 (Nhận biết)
Ta có thể phân biệt được chân dương, chân âm của đèn LED siêu sáng bằng cách nào?
![Visual](media/de-2-trac-nghiem-ai-arduino/rId8.png)
- A/ Phần chân âm của đèn led có dấu (-); chân dương của đèn led có dấu (+).
- B/ Phần chân âm của đèn led dài hơn; chân dương của đèn led ngắn hơn.
- C/ Phần chân dương của đèn led được đánh dấu bằng một lỗ tròn nhỏ, chân âm không có. 
- D/ Phần chân dương của đèn led dài hơn; chân âm của đèn led ngắn hơn.
Câu 5 (Nhận biết)
Khối lệnh nào sau đây được sử dụng để điều khiển việc hoạt động/tắt của động cơ rung 0834 3-5V?
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId9.png)
- B/
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId10.png)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId11.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId12.png)
Câu 6 (Nhận biết)
Phát biểu nào sau đây là SAI khi nói về các chân kết nối của mạch thu phát âm thanh ISD1820?
- A/ PLAYE, PLAYL của mạch chỉ có thể được bật bằng cách nhấn nút thủ công.
- B/ Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~): 2, 4, 7, 8, 12, 13.
- C/ Chân VCC của mạch được gắn với cổng 5V của Arduino.
- D/ Chân REC của mạch được gắn với cổng Digital 2-13 của Arduino.
Câu 7 (Nhận biết)
Phát biểu nào sau đây là SAI khi nói về các chân kết nối của mạch thu phát âm thanh ISD1820?
- A/ Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~) như: 2, 4, 7, 8, 12, 13.
- B/ Chân GND của mạch được gắn với cổng GND của Arduino.
- C/ Chân VCC của mạch được gắn với cổng 5V của Arduino.
- D/ Chân REC của mạch được gắn với cổng Digital 2-13 của Arduino.
Câu 8 (Nhận biết)
Phát biểu nào sau đây là sai khi nói về động cơ Servo?
- A/ Servo là thiết bị input.
- B/ Dây màu cam của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital 2-13 của Arduino.
- C/ Điện áp hoạt động của servo là 5V.
- D/ Servo là thiết bị có 2 chân kết nối.
Câu 9 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về cách kết nối các lỗ trên Breadboard?
![Visual](media/de-2-trac-nghiem-ai-arduino/rId13.png)
- A/ Các lỗ ở khu vực B hoặc C được kết nối theo hàng dọc, mỗi cột 5 lỗ được kết nối với nhau.
- B/ Các lỗ ở khu vực A hoặc D được kết nối theo hàng dọc, mỗi cột 2 lỗ được kết nối với nhau.
- C/ Các lỗ ở khu vực B hoặc C được kết nối theo hàng ngang, mỗi hàng 30 lỗ được kết nối với nhau.
- D/ Tất cả các lỗ ở khu vực B hoặc C được kết nối với nhau theo hàng ngang và hàng dọc, tất cả các lỗ trong khu B hoặc C đều có chức năng giống nhau.
Câu 10 (Thông hiểu)
Cách kết nối mạch thu phát âm thanh ISD1820 với Arduino, cách kết nối nào sau đây là sai?
- A/ d
![Visual](media/de-2-trac-nghiem-ai-arduino/rId14.png)
- B/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId15.png)
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId16.png)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId17.png)
Câu 11 (Thông hiểu)
Cho mạch điện Arduino gồm 5 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId18.png)
Hỏi khi bạn thực hiện chương trình sau thì có những đèn nào phát sáng ?
![Visual](media/de-2-trac-nghiem-ai-arduino/rId19.png)
- A/ Chỉ có đèn xanh dương và đèn xám sáng
- B/ Chỉ đèn xanh dương sáng 
- C/ Chỉ có đèn đỏ, đèn xanh lá cây và đèn xám sáng 
- D/ Chỉ có đèn vàng không sáng.
Câu 12 (Thông hiểu)
Cho mạch điện Arduino gồm 5 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId18.png)
Một học sinh lập trình chương trình của Arduino như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId20.png)
Chọn đoạn chương trình phù hợp điền vào chỗ trống để các đèn led hoạt động giống như đoạn gif dưới đây
![Visual](media/de-2-trac-nghiem-ai-arduino/rId21.gif)
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId22.png)
- B/ 
- C/ 
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId23.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId24.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId25.png)
Câu 13 (Thông hiểu)
Cho mạch Arduino gồm các linh kiện điện tử như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId26.png)
Hãy ghép chân của các linh kiện điện tử đã kết nối trên Arduino?
(Dạng ghép nối)
Đáp án

Chân dương (+) LED đỏ | D5
Chân dương (+) LED xanh lá | D10
Chân dương (+) LED xanh dương | D6
Chân dương (+) còi Buzzer | D12
Chân PL mạch thu phát âm thanh | D5
Chân PE mạch thu phát âm thanh | D6
Chân REC mạch thu phát âm thanh | D10

Câu 14 (Thông hiểu)
Một bạn học sinh mắc mạch gồm Arduino, đèn Led và breadboard, quy ước các chân đèn Led được minh họa như hình. Hỏi khi bạn thực hiện chương trình sau thì có những đèn nào phát sáng?
![Visual](media/de-2-trac-nghiem-ai-arduino/rId27.png)
Đây là đoạn chương trình của học sinh đã thực hiện. Hỏi khi nhấn lá cờ xanh, những đèn LED nào sẽ phát sáng?
![Visual](media/de-2-trac-nghiem-ai-arduino/rId28.png)
- A/ Chỉ có đèn xanh dương sáng.
- B/ Chỉ có đèn xanh lá, xanh dương, xám, vàng sáng; Đèn đỏ không sáng.
- C/ Chỉ có đèn đỏ, xanh lá, xanh dương, xám, sáng; Đèn vàng không sáng.
- D/ Cả 5 đèn đều sáng.
Câu 15 (Thông hiểu)
Cho đoạn mạch Arduino và chương trình lập trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId29.gif)
Hãy lập trình để servo xoay qua lại một cách chậm rãi. Khi Servo quay ở một số góc xác định, đèn LED sẽ sáng lên. Sau đó, đèn LED tắt và servo tiếp tục xoay.
![Visual](media/de-2-trac-nghiem-ai-arduino/rId30.png)
Biến số A cần phải bằng bao nhiêu để chương trình quay được các góc như ảnh gif trên?
- A/ 30
- B/ 45
- C/ 60
- D/ 90
Câu 16 (Thông hiểu)
Cho mạch Arduino gồm 1 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId31.png)
Cho đoạn chương trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId32.png)
Hỏi khi nhấn phím mũi tên lên, sau đó 10 giây thì nhấn phím mũi tên xuống, đèn LED sẽ hoạt động như thế nào?
- A/ Khi nhấn phím mũi tên lên, đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím mũi tên xuống, đèn LED tắt trong thời gian ngắn, sau đó tiếp tục chớp tắt liên tục.
- B/ Khi nhấn phím mũi tên lên, đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím mũi tên xuống, đèn LED tắt hẳn.
- C/ Khi nhấn phím mũi tên lên, đèn LED tắt. Khi nhấn phím mũi tên xuống, đèn LED sáng lên.
- D/ Khi nhấn phím mũi tên lên, đèn LED sáng. Khi nhấn phím mũi tên xuống, đèn LED tắt đi.
Câu 17 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId33.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng phím a và b thỏa yêu cầu sau:
- Khi nhấn phím a, động cơ Servo sẽ đứng yên ở vị trí giữa (góc 90 độ).
- Khi nhấn phím b, động cơ Servo sẽ tự động xoay trái (góc 0 độ), phải (góc 180 độ) liên tục đến khi nhấn phím a thì sẽ dừng xoay.
Đáp án nào sau đây thể hiện chương trình của nhân vật  để thực hiện yêu cầu trên?
- A/ B/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId34.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId35.png)
- C/D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId36.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId37.png)
Câu 18 (Thông hiểu)
Cho mạch điện Arduino gồm 5 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId18.png)
Một học sinh đã lập trình một chương trình như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId38.png)
Khi chạy chương trình trên, hỏi các đèn LED hoạt động như thế nào?
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId21.gif)
- B/
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId39.gif)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId40.gif)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId41.gif)
Câu 19 (Thông hiểu)
Cho mạch điện Arduino gồm 5 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId18.png)
Một học sinh đã lập trình một chương trình như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId42.png)
Đoạn code nào có thể tương ứng với đoạn tắt đèn LED (trong hình vuông đỏ)?
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId43.png)
- B/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId44.png)
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId45.png)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId46.png)
Câu 20 (Thông hiểu)
Cho mạch Arduino gồm 1 đèn LED, 1 còi, 1 mạch thu phát âm thanh như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId47.png)
Cho chương trình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId48.png)
Các thiết bị trên mạch Arduino sẽ thực hiện hành động như thế nào ?
Phát biểu nào sau đây là đúng khi nói về các chức năng của chương trình trên?
- A/ Khi nhấn phím Space, sau 3 tiếng kêu ngắt quãng của còi Buzzer, đèn LED sẽ sáng và mạch ISD1820 sẽ phát ra đoạn ghi âm đã được thu.
- B/ Khi nhấn phím Space, đèn LED sẽ sáng đồng thời thu âm giọng của người dùng trong 10 giây rồi tắt.
- C/ Khi nhấn phím Space, sau 3 tiếng kêu ngắt quãng của còi Buzzer, đèn LED sẽ sáng đồng thời thu âm giọng của người dùng trong 10 giây rồi tắt.
- D/ Khi nhấn phím Space, đèn LED tắt đồng thời mạch ISD1820 sẽ phát ra đoạn ghi âm đã được thu, sau đó còi buzzer và đèn LED hoạt động trong 10 giây rồi tắt đi.
Câu 21 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về khối lệnh “Broadcast” và “When I receive message”?
- A/ Các tin nhắn có thể được truyền qua lại giữa nhân vật và Arduino.
- B/ Việc truyền và nhận tin nhắn khi lập trình Arduino có thể sử dụng cả khi dùng chế độ UPLOAD và LIVE.
- C/ Linh kiện điện tử và nhân vật không thể truyền và nhận tin nhắn.
- D/ Chỉ có nhân vật truyền được tin nhắn.
Câu 22 (Thông hiểu)
Cho chương trình gồm 1 nhân vật nút nhấn  và mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId49.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId33.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng nhân vật nút nhấn thỏa yêu cầu sau:
- Khi nhấn vào lá cờ, servo quay về góc 0 độ.
- Khi nhấn vào nút nhấn, nếu servo đang ở góc 0 độ thì sẽ quay sang góc 90 độ. Ngược lại, nếu servo đang ở góc 90 độ thì sẽ quay sang góc 0 độ.
Biết rằng chương trình của Arduino được lập trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId50.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId51.png)
Chương trình của nhân vật như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId52.png)
Hãy điền vào A câu lệnh còn thiếu để chương trình hoạt động theo yêu cầu trên:
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId53.png)
- B/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId54.png)
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId55.png)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId56.png)
Câu 23 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId57.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng hai nhân vật nút nhấn “On”, “Off” thỏa yêu cầu sau:
- Khi nhấn vào nút nhấn “Off”, động cơ Servo sẽ đứng yên ở vị trí giữa (góc 90 độ).
- Khi nhấn vào nút nhấn “On”, động cơ Servo sẽ tự động xoay trái (góc 0 độ), phải (góc 180 độ) liên tục đến khi nhấn “Off” thì sẽ dừng xoay.
Biết rằng chương trình của Arduino được lập trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId58.png)
Đáp án nào sau đây thể hiện chương trình của nhân vật để thực hiện yêu cầu trên?
- A/ B/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId59.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId60.png)
- C/ D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId61.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId62.png)
Câu 24 (Thông hiểu)
Cho mạch điện Arduino với 1 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId63.png)
Cho chương trình gồm 1 nhân vật đèn “Bulb” có 2 trang phục như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId64.png)
Hãy lập trình thiết bị Arduino và nhân vật đèn thỏa các yêu cầu sau:
- Khi nhấn vào nhân vật, nếu nhân vật đang ở trang phục “off” sẽ đổi thành “on” và ngược lại.
- Khi nhân vật ở trang phục “off", đèn LED trên Arduino sẽ tắt; Khi nhân vật ở trang phục “on”,  đèn LED trên Arduino sẽ mở.
Biết rằng chương trình của nhân vật đèn “Bulb” được lập trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId65.png)
Đáp án nào sau đây thể hiện câu lệnh của Arduino để thực hiện yêu cầu trên?
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId66.png)
- B/
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId67.png)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId68.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId69.png)
Câu 25 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về extension “Cognitive Services”?
- A/ Các câu lệnh "Recognize" dùng để hiện lên khung nhận diện (Camera thu hình ảnh và Voice Record để thu âm thanh), có giới hạn số lần sử dụng trong một ngày.
- B/ Để sử dụng nhóm lệnh trên, ta lần lượt thực hiện các thao tác sau: Chọn phần lập trình thiết bị (Devices) > Thêm thiết bị Arduino > Chọn mục Extension > Tìm và chọn nhóm lệnh “Cognitive Services”.
- C/ Các câu lệnh “Recognize” luôn đi kèm với các câu lệnh khác cho ra kết quả nhận diện. Khối lệnh đó luôn cho ra kết quả là một chuỗi ký tự.
- D/ Vì các câu lệnh thực thi “Recognize” luôn mở bảng nhận diện giống nhau nên ta chỉ cần sử dụng 1 câu lệnh cho mọi trường hợp nhận diện, chỉ cần đổi các câu lệnh result cho phù hợp.
Câu 26 (Thông hiểu)
Cho mạch điện Arduino với 2 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId70.png)
Cho chương trình gồm 1 nhân vật có chương trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId71.png)
Biết rằng chương trình của thiết bị Arduino được lập trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId72.png)
Hỏi khi người dùng nhấn phím Space, sau đó nói “Light number two”, đèn LED nào trên mạch Arduino sẽ sáng?
- A/ Đèn LED đỏ sáng, đèn LED xanh lá tắt.
- B/ Cả hai đèn LED đều sáng.
- C/ Cả hai đèn LED đều tắt.
- D/ Đèn LED xanh lá sáng, đèn LED đỏ tắt.
Câu 27 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId57.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng giọng nói với từ khóa “left”/”right”.
- Khi nhấn phím Space, chương trình sẽ hỏi “Servo turn left or right?”
- Khi đó hệ thống sẽ mở lên bảng nhận diện giọng nói và người dùng nói bằng tiếng Anh.
- Nếu trong lời nói chứa từ khóa “left” thì servo sẽ xoay trái (góc 0 độ); Nếu trong lời nói chứa từ khóa “right” thì servo sẽ xoay phải (góc 180 độ).
Biết rằng chương trình của nhân vật được lập trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId73.png)
Đáp án nào sau đây thể hiện chương trình của Arduino để thực hiện yêu cầu trên?
- A/ B/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId74.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId75.png)
- C/ D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId76.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId77.png)
Câu 28 (Nhận biết)
Phát biểu nào sau đây là SAI khi nói về Teachable Machine?
- A/ Cần phải đăng nhập mới được sử dụng extension Teachable Machine.
- B/ Tiện ích mở rộng Teachable Machine nằm trong phần Extension của nhân vật Sprite.
- C/ Teachable machine không yêu cầu đăng nhập tài khoản mBlock và không cần sử dụng Wifi.
- D/ Teachable Machine là một tính năng cho phép người dùng dễ dàng tạo ra các mô hình máy học (Machine learning) và huấn luyện chúng thông qua dữ liệu mà bạn cung cấp, và sau đó sử dụng mô hình đó để phân loại và nhận diện các đối tượng thực tế.
Câu 29 (Thông hiểu)
Cho mạch điện Arduino với 3 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId78.png)
Hãy lập trình một chương trình có thể nhận diện 3 màu sắc đỏ, xanh dương, xanh lá. Từ đó khi người dùng sử dụng giấy màu đặt trước camera nhận diện, đèn LED trên mạch điện sẽ sáng màu tương ứng:
- Hãy dùng công cụ Teachable Machine và dùng hình ảnh thực tế để dạy máy tính phân biệt 3 trường hợp và đặt tên như sau: 
	1/ Giấy A4 màu đỏ (red)
	2/ Giấy A4 màu xanh lá (green)
	3/ Giấy A4 màu xanh dương (blue)
- Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện.
- Nếu camera nhận diện được giấy màu đỏ/xanh lá/xanh dương, thì đèn LED đỏ/xanh lá/xanh dương trên mạch Arduino sẽ tắt, 2 đèn còn lại sẽ sáng.
- Chương trình lặp lại mãi mãi.
Biết rằng chương trình của nhân vật được lập trình như sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId79.png)
Đáp án nào sau đây thể hiện chương trình của Arduino để thực hiện yêu cầu trên?
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId80.png)
- B/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId81.png)
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId82.png)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId83.png)
Câu 30 (Thông hiểu)
Cho mạch điện Arduino với 1 đèn LED như hình sau:
![Visual](media/de-2-trac-nghiem-ai-arduino/rId63.png)
Hãy lập trình một chương trình có thể nhận diện được một người có đang đeo khẩu trang hay không:
- Hãy dùng công cụ Teachable Machine và dùng hình ảnh thực tế để dạy máy tính phân biệt 3 trường hợp và đặt tên như sau: 
	1/ Người đang đeo khẩu trang (mask)
	2/ Người không đeo khẩu trang (nomask)
	3/ Các trường hợp khác (empty)
- Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện khuôn mặt.
- Nếu nhận diện được người đang đeo khẩu trang, đèn LED sẽ sáng. Ngược lại nếu nhận diện người đang không đeo khẩu trang, đèn LED sẽ tắt.
- Chương trình lặp lại mãi mãi.
Đáp án nào sau đây thể hiện câu lệnh của Arduino và phần nhân vật để thực hiện yêu cầu trên?
- A/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId84.png)
- B/
- C/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId85.png)
- D/
![Visual](media/de-2-trac-nghiem-ai-arduino/rId86.png)
![Visual](media/de-2-trac-nghiem-ai-arduino/rId87.png)