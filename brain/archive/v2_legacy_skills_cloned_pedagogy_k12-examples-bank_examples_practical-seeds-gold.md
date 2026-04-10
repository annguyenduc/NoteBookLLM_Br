# Seed Samples: Practical ML Pipeline (K-12)

Dưới đây là các ví dụ thực tế về cách vận hành một dự án AI/ML cho học sinh.

## 🎞️ Ví dụ 1: Gán nhãn dữ liệu cảm xúc (Text)
- **Dự án:** Make Me Happy.
- **Nhãn:** Tích cực | Tiêu cực.
- **Dữ liệu hạt giống:**
    - *Tích cực:* "Bài hôm nay thú vị lắm!", "Em hiểu rồi, cảm ơn thầy!".
    - *Tiêu cực:* "Em không hiểu bài này chút nào.", "Sao bài này khó thế?".
- **Ghi chú sư phạm:** Yêu cầu HS viết câu đầy đủ > 5 từ để máy có đủ ngữ cảnh.

## 📊 Ví dụ 2: Vòng lặp Phân tích lỗi (Error Analysis Loop)
- **Tình huống:** Model nhận diện nhầm "Tiêu cực" cho câu "Bài này hơi khó nhưng thú vị thầy ơi" (Confidence 61%).
- **Phân tích:** 
    - Model thấy từ "khó" nên gán vào Tiêu cực.
    - Thiếu tính đa dạng cho các câu cảm xúc phức hợp.
- **Giải pháp:** Thêm 4-5 câu có cấu trúc "Mặc dù... nhưng..." vào nhãn Tích cực.
- **Kết quả sau sửa:** Confidence tăng lên 78%, Prediction đúng.

## 🏗️ Ví dụ 3: Thiết kế bài dạy 45 phút
- **Chủ đề:** Phân loại phản hồi học sinh sau hoạt động nhóm.
- **Hoạt động chính:** 
    1. HS viết feedback lên giấy. 
    2. Gõ feedback vào máy để train model.
    3. Kiểm tra xem máy có "hiểu" cảm xúc của bạn mình không?
- **Câu hỏi tư duy:** "Máy tính có thực sự hiểu cảm xúc không, hay chỉ đang nhận dạng các từ khóa?"
