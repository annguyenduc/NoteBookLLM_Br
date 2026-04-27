---
title: "Đề thực hành 1 - Gbot.docx"
source: "[[Đề thực hành 1 - Gbot.docx]]"
category: "Robot"
sub_category: "GBot"
type: "RAW_SOURCE"
---

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


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId6.png)
1.2. Tiếp nối câu hỏi trên, với mỗi vị trí cột mốc B, C, D, trước khi di chuyển đến vị trí tiếp theo, robot thực hiện các nhiệm vụ như sau:
a/ Tại vị trí điểm B, toàn bộ vòng đèn LEDs đổi màu lần lượt thành đỏ, vàng, xanh dương, lặp lại 3 lần, mỗi lần 0.5 giây.
b/ Tại vị trí điểm C, vòng đèn LEDs sáng đèn ở các vị trí như hình sau trong 3 giây.


![Image](../assets/IMG_de_trac_nghiem_1_-_gbot_v1_rId11.png)
c/ Tại vị trí điểm D, robot dừng di chuyển, và phát âm thanh cho đoạn nhạc sau:


![Image](../assets/IMG_de_trac_nghiem_1_-_gbot_v1_rId35.png)
Biết rằng cao độ và trường độ của các nốt nhạc được lập trình dựa vào bảng quy đổi các nốt nhạc như sau:


![Image](../assets/IMG_de_trac_nghiem_1_-_gbot_v1_rId29.png)
Bài 2 - Cảm biến siêu âm
Cho mê cung có các bức tường bao xung quanh và đặt Gbot ở bên trong như hình sau:


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId10.png)
Sử dụng giấy roki, bìa carton hoặc các vật dụng cần thiết để tạo một mê cung như hình minh hoạ ở trên.
Hãy lập trình cho Gbot thực thi được các hành động theo các yêu cầu sau:
 Khi khởi động, robot di chuyển bên trong các bức tường. Khi robot gặp bức tường (với khoảng cách nhỏ hơn 5cm), robot sẽ tự động xoay hướng khác và tiếp tục di chuyển thẳng.
Tiếp nối câu hỏi trên, khi gặp vật cản, hướng xoay của robot sẽ được lựa chọn ngẫu nhiên trái hoặc phải. Khi robot di chuyển thẳng và không gặp vật cản, vòng đèn LEDs sáng màu xanh lá; khi robot gặp vật cản và xoay trái, vòng đèn LEDs sáng màu vàng; khi robot gặp vật cản và xoay phải, vòng đèn LEDs sáng màu xanh dương.

Bài 3 - Cảm biến dò line
Cho sa bàn có các vạch kẻ màu đen (độ rộng từ 1.5cm đến 5cm) như hình sau:


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId11.png)
Hãy lập trình cho Gbot thực thi được các hành động theo các yêu cầu sau:
3.1. Khi khởi động, robot bắt đầu từ một vị trí bất kỳ trên sa bàn và di chuyển mãi mãi theo vạch kẻ của sa bàn. Trên sa bàn có đặt một vật cản (ví dụ chai nước), nên khi gặp vật cản thì robot phải di chuyển vòng qua vật cản để sau đó lại tiếp tục di chuyển theo vạch kẻ của sa bàn (lưu ý, vòng cung khi robot đi vòng qua vật cản là nhỏ nhất).


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId12.png)
3.2. Đặt robot nằm ngoài sa bàn và trên sa bàn sẽ có hai vật cản (ví dụ chai nước) ở vị trí như hình vẽ sau. Hãy lập trình khi khởi động, từ vị trí A bên ngoài sa bàn, robot sáng đèn màu xanh lá và di chuyển thẳng đến khi gặp vật cản tại vị trí B. Khi đó, robot đổi màu đèn LED sang màu vàng và bắt đầu di chuyển trên vạch kẻ của sa bàn. Robot có thể di chuyển mãi trên vạch kẻ của sa bàn. Khi gặp vật cản lần 2 tại vị trí C (vị trí này không cố định), robot dừng di chuyển và tắt vòng đèn LED.


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId13.png)


ĐÁP ÁN
Bài 1
1.1.
Lưu ý: Tốc độ quay và thời gian chờ của câu lệnh trong đáp án chỉ mang tính chất tượng trưng. Khi chấm điểm cần kèm theo video quay lại quá trình di chuyển của robot.



![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId14.png)
1.2.


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId15.png)



![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId16.png)
Bài 2
Lưu ý: Người thực hiện có thể có đáp án khác miễn đáp ứng được yêu cầu đề bài.


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId17.png)
Bài 3
3.1.
Lưu ý: Các câu lệnh và tốc độ quay, thời gian chờ của câu lệnh trong đáp án chỉ đại diện cho một cách giải quyết vấn đề. Người thực hiện có thể có đáp án khác miễn đáp ứng được yêu cầu đề bài.


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId18.png)
3.2.
Lưu ý: Các câu lệnh và tốc độ quay, thời gian chờ của câu lệnh trong đáp án chỉ đại diện cho một cách giải quyết vấn đề. Người thực hiện có thể có đáp án khác miễn đáp ứng được yêu cầu đề bài. (VD: Sử dụng Wait until, repeat until…)


![Image](../assets/IMG_MASTER_Robotics_GBot_Đề_thực_hành_1_-_Gbot_rId19.png)






TIÊU CHÍ VÀ THANG ĐIỂM
Bài 1


Bài 2


Bài 3




