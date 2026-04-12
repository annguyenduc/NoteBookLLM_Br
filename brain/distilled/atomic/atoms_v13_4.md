Để tải mô hình trong **LM Studio** (đặc biệt là các mô hình hỗ trợ lập trình như CodeBERT hoặc các lựa chọn thay thế tốt hơn), bạn hãy làm theo các bước chi tiết sau:

### **Các bước tải mô hình trực tiếp trong LM Studio**

**Bước 1: Mở thanh tìm kiếm (Search)**
- Nhấp vào biểu tượng **Kính lúp** (Search) ở thanh menu bên trái của giao diện LM Studio.

**Bước 2: Nhập từ khóa tìm kiếm**
- Trong ô tìm kiếm ở trên cùng, hãy nhập: `CodeBERT`.
- **Lưu ý quan trọng**: CodeBERT là một mô hình dạng "Encoder" (thường dùng để phân tích mã), trong khi LM Studio tối ưu cho các mô hình dạng "Chat/Instruction" (để hỏi đáp và viết code). 
- **Gợi ý thay thế**: Nếu tìm `CodeBERT` không ra kết quả phù hợp (file GGUF), bạn nên tìm các mô hình lập trình cực mạnh khác mà máy bạn chạy rất mượt:
    - `DeepSeek-Coder-1.3B` (Rất nhẹ, cực giỏi code).
    - `Stable-Code-3B` (Phù hợp với RAM 32GB).
    - `CodeLlama-7B-GGUF` (Tiêu chuẩn cho lập trình).

**Bước 3: Chọn phiên bản từ Hugging Face**
- Sau khi nhấn Enter, một danh sách các phiên bản mô hình từ Hugging Face sẽ hiện ra ở cột bên trái.
- Hãy chọn các bản từ những người đóng gói uy tín như: **TheBloke**, **MaziyarPanahi**, hoặc **bartowski**.

**Bước 4: Chọn độ nén (Quantization) phù hợp với GTX 1650**
- Ở cột bên phải, bạn sẽ thấy danh sách các file có đuôi `.gguf` với các nhãn như `Q4_K_M`, `Q5_K_M`, `Q8_0`.
- **Với card GTX 1650 (4GB VRAM)**: 
    - Hãy ưu tiên chọn bản **Q4_K_M** hoặc **Q5_K_M**. 
    - Tránh chọn các bản quá lớn (như Q8 hoặc FP16) vì sẽ làm tràn bộ nhớ GPU và chạy rất chậm.

**Bước 5: Nhấn Download**
- Nhấn nút **Download** bên cạnh phiên bản bạn đã chọn.
- Quá trình tải sẽ hiển thị ở thanh trạng thái phía dưới cùng của ứng dụng.

---

### **Trích xuất sự kiện kỹ thuật (Technical Facts)**

- **Fact**: LM Studio sử dụng định dạng file .gguf để chạy các mô hình ngôn ngữ lớn trên phần cứng dân dụng.
- **Source**: (vv13 - Section: LM Studio Model Compatibility)
- **Tag**: [vv13]

- **Fact**: Đối với GPU có VRAM thấp như GTX 1650 (4GB), việc sử dụng các bản nén 4-bit (Q4_K_M) là tối ưu để cân bằng giữa tốc độ và độ chính xác.
- **Source**: (vv13 - Section: GPU Optimization)
- **Tag**: [vv13]

- **Fact**: CodeBERT là mô hình chuyên biệt cho lập trình nhưng thường yêu cầu thư viện Transformers để chạy; trong LM Studio, các mô hình Decoder-only như DeepSeek-Coder hoặc CodeLlama thường phổ biến và dễ cài đặt hơn.
- **Source**: [Unverified_Source]
- **Tag**: [Unverified_Source]

---

**Lời khuyên cho bạn**: Sau khi tải xong, bạn nhấn vào biểu tượng **Cái bong bóng chat** (AI Chat) ở bên trái, chọn mô hình vừa tải ở thanh trên cùng (Select a model to load) và bắt đầu dán code vào để hỏi hoặc yêu cầu nó viết code mới. Nếu máy báo lỗi "Out of Memory", hãy giảm mục "GPU Offload" trong phần cài đặt bên phải xuống một chút.