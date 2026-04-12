Dưới đây là các sự kiện (Facts) về đáp án và barem điểm cho Đề B (Data-only) dựa trên dữ liệu đã khởi tạo:

- **Fact: [CONV] Logic cốt lõi (Ground Truth) của bộ dữ liệu Đề B**
  - Nhãn `close_door = 1` (Đóng cửa) được xác lập khi thỏa mãn ít nhất một trong ba điều kiện:
    1. Khoảng cách (`distance_cm`) < 25 cm.
    2. Độ ồn (`noise_db`) > 65 dB.
    3. Nhiệt độ (`temp_c`) > 38°C.
  - Ngược lại, `close_door = 0` (Mở cửa).
- **Source:** [vv04 - Section: Create a small synthetic dataset for a no-hardware selection task]
- **Tag:** [vv04]

- **Fact: [CONV] Chỉ số kỹ thuật tham chiếu (Đáp án lý tưởng)**
  - Nếu đội thi tìm ra đúng 3 ngưỡng trên, các chỉ số sẽ đạt:
    - Accuracy (Độ chính xác): 100% (1.0).
    - F1-Score: 1.0.
  - Ma trận nhầm lẫn (Confusion Matrix) sẽ không có sai số (FP=0, FN=0).
- **Source:** [vv04 - Section: Build the official answer key & scoring rubric for Đề B]
- **Tag:** [vv04]

- **Fact: [CONV] Barem điểm chi tiết Đề B (Thang 100)**
  1. **Quy trình & Kiểm thử (20đ):** Biết chia dữ liệu để thử nghiệm, không dùng chính dữ liệu đã biết đáp án để khoe kết quả.
  2. **Kết quả kỹ thuật (20đ):** Tìm ra được các ngưỡng gần đúng (ví dụ: khoảng cách quanh mức 25, nhiệt độ quanh mức 38). Accuracy đạt trên 80% là đạt yêu cầu.
  3. **Logic & Fail-safe (20đ):** Giải thích được tại sao chọn ngưỡng đó. Đề xuất được phương án khi cảm biến hỏng (ví dụ: "Nếu cảm biến nhiệt độ lỗi, mặc định coi là nóng để đóng cửa cho an toàn").
  4. **Design Thinking & Kế hoạch (15đ):** Phân công vai trò rõ ràng (ai code/tính toán, ai làm slide, ai thuyết trình). Có lộ trình cho 2 ngày bán kết.
  5. **Pitch & Q&A (15đ):** Thuyết trình tự tin, trả lời được câu hỏi "Tại sao AI lại quan trọng hơn quy tắc If-Else thông thường trong bài này?".
  6. **Kỷ luật (10đ):** Nộp bài đúng hạn, đúng định dạng file.
- **Source:** [vv04 - Section: Rubric chấm “no-hardware”]
- **Tag:** [vv04]

- **Fact: [CONV] Tiêu chí Tie-break (Xử lý bằng điểm)**
  - Ưu tiên 1: Đội có đủ thành viên cam kết tham gia đủ 4 mốc thời gian quan trọng.
  - Ưu tiên 2: Đội có điểm Pitch cao hơn (năng lực trình bày tại chung kết).
  - Ưu tiên 3: Đội có sự phân bổ vai trò cân bằng (AI/Điện tử/Pitch).
- **Source:** [vv04 - Section: Bước 3 — Xếp hạng & chọn]
- **Tag:** [vv04]

- **Fact: [CONV] Công cụ hỗ trợ chấm điểm**
  - Sử dụng file `NoCode_AI_Test_Recorder.xlsx` để nhập kết quả dự đoán của học sinh và tự động tính Accuracy mà không cần lập trình.
- **Source:** [vv04 - Section: Create a no-code testing workbook]
- **Tag:** [vv04]