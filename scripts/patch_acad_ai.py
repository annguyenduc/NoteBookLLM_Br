import os
import re

files = {
    '3-resources/wiki/concepts/CONCEPT_ACAD_AI_Cutoff_vs_Drift.md': (
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Knowledge Cutoff trong thi cử\n*Tình huống: Học sinh dùng AI để ôn thi môn Lịch sử.* \n- **Đầu vào:** Sự kiện chiến tranh thế giới thứ hai.\n- **Cách giải quyết:** AI trả lời rất tốt vì sự kiện này nằm gọn trong Knowledge Cutoff. Tuy nhiên, nếu hỏi về kết quả kỳ bầu cử tổng thống vừa diễn ra ngày hôm qua, AI sẽ không biết do giới hạn Cutoff.\n\n### Ví dụ 2: Model Drift trong chấm điểm tự động\n*Tình huống: Một hệ thống AI được dùng để chấm điểm tự động bài luận Tiếng Anh của học sinh.*\n- **Đầu vào:** Từ vựng tuổi teen và tiếng lóng mới xuất hiện trong năm nay.\n- **Cách giải quyết:** Do Model Drift, AI chấm sai hoặc không hiểu các từ lóng mới vì nó được huấn luyện trên dữ liệu ngữ pháp chuẩn từ 3 năm trước. Cần fine-tune lại mô hình với tập dữ liệu mới.\n\n'
    ),
    '3-resources/wiki/concepts/CONCEPT_ACAD_AI_Data_Bias.md': (
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Thiên lệch dữ liệu tuyển sinh\n*Tình huống: Xây dựng AI dự đoán khả năng trúng tuyển Đại học.*\n- **Đầu vào:** Hệ thống được huấn luyện 80% dựa trên hồ sơ của học sinh khu vực thành thị.\n- **Cách giải quyết:** Khi áp dụng cho học sinh nông thôn, AI đánh giá sai lệch, cho điểm thấp một cách bất công do Data Bias. Giải pháp là phải thu thập lại tập dữ liệu huấn luyện cân bằng (Balanced dataset) giữa các vùng miền.\n\n### Ví dụ 2: Thiên lệch ngôn ngữ trong giáo dục\n*Tình huống: Hệ thống AI gợi ý sách đọc thêm trong thư viện trường.*\n- **Đầu vào:** Lịch sử mượn sách đa số là các tiểu thuyết khoa học viễn tưởng.\n- **Cách giải quyết:** Do thiên lệch thuật toán (Confirmation Bias), hệ thống chỉ liên tục gợi ý sách khoa học viễn tưởng, vô tình thu hẹp thế giới quan của học sinh. Giải pháp là đưa yếu tố ngẫu nhiên (Serendipity) vào thuật toán đề xuất.\n\n'
    ),
    '3-resources/wiki/concepts/CONCEPT_ACAD_AI_Human_In_The_Loop.md': (
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Human-in-the-loop trong chấm thi\n*Tình huống: Ứng dụng AI để quét và chấm điểm bài trắc nghiệm nhanh cho toàn trường.*\n- **Đầu vào:** AI tự động chấm 500 bài thi. Nhưng có 10 bài AI báo lỗi do học sinh tô mờ hoặc bôi xóa.\n- **Cách giải quyết:** Giáo viên (Human) can thiệp vào vòng lặp, kiểm tra lại 10 bài thi đó và đưa ra quyết định cuối cùng, đảm bảo không có học sinh nào bị điểm 0 oan.\n\n### Ví dụ 2: Human-in-the-loop trong soạn giáo án\n*Tình huống: Giáo viên dùng AI tạo nhanh giáo án môn Sinh học.*\n- **Đầu vào:** AI sinh ra giáo án dài 5 trang.\n- **Cách giải quyết:** Giáo viên không bê nguyên xi vào lớp mà phải kiểm duyệt, điều chỉnh ngữ điệu, cắt bỏ phần quá khó và thêm các ví dụ thực tế địa phương. AI làm phần thô, Human làm phần tinh.\n\n'
    ),
    '3-resources/wiki/concepts/CONCEPT_ACAD_AI_Information_Toolkit.md': (
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Trợ lý thông tin trong lớp học ảo\n*Tình huống: Tích hợp AI chatbot vào hệ thống LMS của nhà trường.*\n- **Đầu vào:** Sinh viên hỏi "Lịch thi môn Toán rời rạc là ngày nào?".\n- **Cách giải quyết:** AI Information Toolkit tự động truy vấn (Query) database của phòng đào tạo để lấy lịch thi mới nhất và trả lời sinh viên ngay lập tức, thay vì tìm kiếm trong dữ liệu huấn luyện cũ.\n\n### Ví dụ 2: Xử lý thông tin đa luồng\n*Tình huống: Phân tích hiệu suất học tập của một lớp.*\n- **Đầu vào:** Điểm danh, điểm giữa kỳ, log truy cập video bài giảng.\n- **Cách giải quyết:** AI dùng Information Toolkit để tổng hợp dữ liệu từ 3 nguồn khác nhau, vẽ biểu đồ tương quan và cảnh báo giáo viên về 5 sinh viên có nguy cơ rớt môn cao nhất.\n\n'
    ),
    '3-resources/wiki/concepts/CONCEPT_ACAD_AI_Knowledge_Cutoff.md': (
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Cập nhật quy chế thi cử\n*Tình huống: Học sinh dùng ChatGPT (phiên bản không nối mạng) để hỏi về quy chế thi THPT Quốc gia năm nay.*\n- **Đầu vào:** Quy chế mới vừa ban hành tháng trước.\n- **Cách giải quyết:** Do Knowledge Cutoff của AI dừng ở năm ngoái, AI sẽ trả lời sai dựa trên quy chế cũ. Giải pháp: Giáo viên phải hướng dẫn học sinh cung cấp văn bản mới cho AI (qua prompt) để nó xử lý.\n\n### Ví dụ 2: Viết luận văn công nghệ mới\n*Tình huống: Sinh viên IT cần viết báo cáo về công nghệ chip bán dẫn mới nhất.*\n- **Đầu vào:** Dữ liệu về công nghệ chip ra mắt tuần trước.\n- **Cách giải quyết:** AI báo lỗi hoặc bịaa (hallucinate) vì không có thông tin. Sinh viên khắc phục bằng cách sử dụng công cụ AI có tính năng duyệt web (Web Search) để vượt qua rào cản Cutoff.\n\n'
    ),
    '3-resources/wiki/concepts/CONCEPT_ACAD_AI_Learning_Habits.md': (
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Thay đổi thói quen tự học\n*Tình huống: Học sinh gặp một bài toán khó khi làm bài tập về nhà.*\n- **Đầu vào:** Thay vì hỏi bạn bè hoặc chờ đến hôm sau hỏi thầy.\n- **Cách giải quyết:** Học sinh hình thành thói quen (Learning Habit) chụp ảnh bài toán và yêu cầu AI "Đừng giải, hãy gợi ý cho tôi bước đầu tiên". Điều này rèn luyện tư duy tự lập thay vì ỷ lại.\n\n### Ví dụ 2: Thói quen đối soát sự thật (Fact-checking)\n*Tình huống: Sinh viên dùng AI để thu thập tài liệu làm tiểu luận Lịch sử.*\n- **Đầu vào:** AI cung cấp 5 sự kiện lịch sử kèm năm diễn ra.\n- **Cách giải quyết:** Thay vì sao chép mù quáng, sinh viên đã hình thành thói quen kiểm chứng (Cross-validation) bằng cách tra cứu đối chiếu lại trên Google Scholar trước khi đưa vào bài làm.\n\n'
    ),
    '3-resources/wiki/concepts/CONCEPT_ACAD_AI_Model_Drift.md': (
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Suy giảm chất lượng dự báo tuyển sinh\n*Tình huống: Trường đại học dùng mô hình AI để dự báo số lượng thí sinh nhập học.*\n- **Đầu vào:** Mô hình được train trên dữ liệu năm 2015-2019.\n- **Cách giải quyết:** Sau đại dịch COVID-19 (2021), hành vi và sở thích chọn ngành của thí sinh thay đổi mạnh. Mô hình gặp Concept Drift và dự báo sai lệch hoàn toàn. Trường phải thu thập lại dữ liệu 2021-2023 để retrain mô hình.\n\n### Ví dụ 2: Hệ thống phát hiện gian lận thi cử\n*Tình huống: AI giám sát thi trực tuyến (Proctoring) nhận diện các hành vi gian lận.*\n- **Đầu vào:** Sinh viên phát minh ra các chiêu thức gian lận tinh vi mới (ví dụ dùng tai nghe siêu nhỏ ẩn).\n- **Cách giải quyết:** Mô hình bị Data Drift vì không nhận diện được hành vi mới này. Quản trị viên hệ thống (LMS Admin) phải liên tục cập nhật video mẫu về các thủ đoạn mới để giữ mô hình luôn nhạy bén.\n\n'
    )
}

for path, replacement in files.items():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf8') as f:
            content = f.read()
        
        if 'Rule 17: Double Examples' not in content:
            # find the last '---' separator
            parts = content.rsplit('---\n', 1)
            if len(parts) == 2:
                new_content = parts[0] + replacement + '---\n' + parts[1]
                with open(path, 'w', encoding='utf8') as f:
                    f.write(new_content)
                print(f'Patched {path}')
            else:
                print(f'Could not split {path}')
        else:
            print(f'Already patched {path}')
