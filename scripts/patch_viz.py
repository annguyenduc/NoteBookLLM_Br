import os

files = {
    '3-resources/wiki/concepts/CONCEPT_VIZ_Dashboard_Design_Best_Practices.md': (
        '---\n<!-- [AUDITOR]',
        '## 6. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Áp dụng tính Súc tích (Succinct)\n*Tình huống: Một bảng điều khiển bán hàng có 15 biểu đồ khác nhau.*\n- Thay vì để tất cả 15 biểu đồ, ta gom nhóm các chỉ số phụ vào một tab riêng và chỉ giữ lại 3 chỉ số quan trọng nhất (Doanh thu, Lợi nhuận, Khách hàng mới) trên màn hình chính.\n\n### Ví dụ 2: Lựa chọn biểu đồ (Visualization Selection)\n*Tình huống: Cần thể hiện tỷ trọng doanh số theo từng khu vực.*\n- Tránh dùng Pie chart nếu có 8 khu vực. Chuyển sang dùng Bar chart để người dùng dễ dàng so sánh kích thước các thanh với nhau thay vì nhìn các góc của bánh.\n\n---\n<!-- [AUDITOR]'
    ),
    '3-resources/wiki/concepts/CONCEPT_VIZ_Data_Storytelling_Framework.md': (
        '---\n<!-- [AUDITOR]',
        '## 6. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Cấu trúc 3 Hồi trong báo cáo Marketing\n*Tình huống: Trình bày chiến dịch quảng cáo.*\n- **Hồi 1:** Chi phí đang tăng cao nhưng tỷ lệ chuyển đổi giảm. **Hồi 2:** Dữ liệu cho thấy tệp khách hàng trẻ tuổi đang rời bỏ ứng dụng. **Hồi 3:** Kêu gọi đầu tư 50.000$ vào chiến dịch TikTok.\n\n### Ví dụ 2: Bing, Bang, Bongo\n*Tình huống: Thuyết trình về ngân sách IT.*\n- **Bing:** Hôm nay ta bàn về việc cắt giảm 10% ngân sách. **Bang:** Chi tiết các khoản dư thừa trong mảng cloud. **Bongo:** Chốt lại yêu cầu phê duyệt chuyển nhà cung cấp cloud vào tháng sau.\n\n---\n<!-- [AUDITOR]'
    ),
    '3-resources/wiki/concepts/CONCEPT_VIZ_Design_Principles.md': (
        '---\n<!-- [AUDITOR]',
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Nhấn mạnh nội dung quan trọng\n*Tình huống: Một biểu đồ Bar chart có 10 thanh.*\n- Thay vì tô màu cả 10 thanh, tô màu xám nhạt cho 9 thanh và tô màu Xanh đậm cho thanh duy nhất đại diện cho công ty của mình để thu hút sự chú ý ngay lập tức.\n\n### Ví dụ 2: Tiêu đề hành động (Action Titles)\n*Tình huống: Biểu đồ thể hiện chi phí hoạt động.*\n- Tiêu đề cũ: "Chi phí hoạt động Q1 2025".\n- Tiêu đề mới (Action Title): "Chi phí Q1 2025 vượt ngân sách 15% do biến động giá xăng dầu".\n\n---\n<!-- [AUDITOR]'
    ),
    '3-resources/wiki/concepts/CONCEPT_VIZ_Effective_Visual_Selection.md': (
        '---\n<!-- [AUDITOR]',
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Zero Baseline\n*Tình huống: Vẽ Bar chart so sánh lợi nhuận 90k và 100k.*\n- Nếu trục Y bắt đầu từ 80k, cột 100k sẽ trông cao gấp đôi cột 90k, gây hiểu lầm nghiêm trọng. Bắt buộc trục Y bắt đầu từ 0.\n\n### Ví dụ 2: Horizontal Bar cho nhãn dài\n*Tình huống: Vẽ biểu đồ so sánh doanh thu của 10 Danh mục sản phẩm với tên rất dài.*\n- Đừng xoay chữ 45 độ trên cột dọc. Hãy chuyển sang Horizontal Bar Chart, chữ sẽ đọc tự nhiên từ trái sang phải.\n\n---\n<!-- [AUDITOR]'
    ),
    '3-resources/wiki/concepts/CONCEPT_VIZ_Eliminating_Clutter.md': (
        '---\n<!-- [AUDITOR]',
        '## 7. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Nguyên tắc Tiệm cận (Proximity)\n*Tình huống: Trong một bảng số liệu tài chính.*\n- Xóa bỏ tất cả các đường viền sọc dọc (vertical gridlines), chỉ để lại khoảng trắng đủ rộng giữa các cột. Mắt người vẫn sẽ tự động gộp các con số nằm sát nhau thành một nhóm cột.\n\n### Ví dụ 2: Dán nhãn trực tiếp (Label directly)\n*Tình huống: Biểu đồ Line chart với 3 đường biểu diễn 3 công ty.*\n- Thay vì để chú giải (Legend) ở góc biểu đồ buộc mắt phải lia qua lia lại, hãy đặt tên công ty bằng chữ cùng màu ngay tại điểm kết thúc của mỗi đường dây.\n\n---\n<!-- [AUDITOR]'
    ),
    '3-resources/wiki/concepts/CONCEPT_VIZ_Focusing_Attention.md': (
        '---\n<!-- [AUDITOR]',
        '## 6. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Độ bão hòa màu sắc (Saturation)\n*Tình huống: Bảng Heatmap rủi ro.*\n- Tô màu các ô rủi ro thấp bằng màu cam nhạt, rủi ro cao bằng màu đỏ đậm. Mắt sẽ lập tức bị thu hút vào các điểm đỏ đậm.\n\n### Ví dụ 2: Vị trí vàng (Top Left)\n*Tình huống: Thiết kế slide thuyết trình dữ liệu.*\n- Luôn đặt kết luận quan trọng nhất hoặc con số Hero metric ở góc trên cùng bên trái. Đừng phí vị trí này cho logo công ty.\n\n---\n<!-- [AUDITOR]'
    ),
    '3-resources/wiki/concepts/CONCEPT_VIZ_Importance_of_Context.md': (
        '---\n<!-- [AUDITOR]',
        '## 6. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Who - What - How\n*Tình huống: Báo cáo ngân sách cho Giám đốc Tài chính.*\n- **Who:** CFO (Rất bận, quan tâm ROI). **What:** Cần họ phê duyệt thêm ngân sách IT. **How:** Dùng biểu đồ đường cho thấy chi phí downtime đang vượt quá chi phí đầu tư server mới.\n\n### Ví dụ 2: Big Idea\n*Tình huống: Trình bày vấn đề giữ chân nhân sự.*\n- **Câu Big Idea:** "Bằng cách tăng lương cơ bản thêm 5%, chúng ta sẽ giữ chân được 20 kỹ sư lõi và tiết kiệm 2 triệu đô chi phí tuyển dụng lại trong năm tới."\n\n---\n<!-- [AUDITOR]'
    ),
    '3-resources/wiki/concepts/CONCEPT_VIZ_PowerBI_vs_Tableau.md': (
        '---\n<!-- [AUDITOR]',
        '## 5. Ví dụ minh họa (Rule 17: Double Examples)\n\n### Ví dụ 1: Chọn Power BI cho hệ sinh thái có sẵn\n*Tình huống: Một công ty đang dùng Office 365 và SQL Server, có 100 nhân viên Sales cần xem báo cáo.*\n- Giải pháp: Mua gói Power BI Pro ($10/user) rất tiết kiệm, đồng thời nhúng thẳng báo cáo vào Microsoft Teams để mọi người tiện theo dõi.\n\n### Ví dụ 2: Chọn Tableau cho khám phá dữ liệu sâu\n*Tình huống: Một đội ngũ Data Scientists cần tạo ra biểu đồ tương tác phức tạp (vd: biểu đồ mạng nhện, phân tích không gian) với lượng dữ liệu 50 triệu dòng.*\n- Giải pháp: Tableau Desktop là lựa chọn tốt hơn nhờ Hyper engine xử lý cực nhanh và khả năng tùy biến viz vô hạn.\n\n---\n<!-- [AUDITOR]'
    )
}

for path, (target, replacement) in files.items():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf8') as f:
            content = f.read()
        if target in content and 'Rule 17: Double Examples' not in content:
            new_content = content.replace(target, replacement)
            with open(path, 'w', encoding='utf8') as f:
                f.write(new_content)
            print(f'Patched {path}')
        else:
            print(f'Skipped {path}')
