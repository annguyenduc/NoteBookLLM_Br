---
file_id: CONV_Atoms_conv_atoms_v01_3
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v01 3

# Tài liệu Học Tập: Hệ Thống Nhận Diện AI với Arduino UNO và Camera

## Thông Tin Bài Học
- **Môn học**: IoT & Nhúng
- **Trình độ**: Trung cấp
- **Thời lượng**: 90 phút
- **Loại tài liệu**: Bài thực hành lập trình nhúng

---

## Mục Tiêu Học Tập

Sau bài học này, học viên sẽ có thể:

| Mục tiêu | Mức độ |
|----------|--------|
| Thiết lập hệ thống nhận diện hình ảnh sử dụng TensorFlow.js và Teachable Machine | Hiểu biết |
| Tích hợp camera đa thiết bị vào ứng dụng web | Ứng dụng |
| Kết nối và điều khiển Arduino UNO qua cổng Serial | Phân tích |
| Xây dựng giao diện người dùng tương tác cho hệ thống AI | Tổng hợp |

---

## Nội Dung Bài Học

### 1. Giới Thiệu Hệ Thống

Hệ thống nhận diện AI kết hợp giữa công nghệ học máy tại biên (edge AI) và điều khiển phần cứng thông qua Arduino UNO. Hệ thống cho phép:

- **Nhận diện hình ảnh thời gian thực**
- **Tích hợp đa camera**
- **Điều khiển thiết bị vật lý**
- **Hiển thị kết quả trực quan**

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 2. Kiến Trúc Hệ Thống

#### 2.1 Các Thành Phần Chính

| Thành phần | Chức năng | Công nghệ sử dụng |
|------------|-----------|-------------------|
| Camera | Thu thập dữ liệu hình ảnh | WebRTC API |
| AI Model | Phân loại hình ảnh | TensorFlow.js + Teachable Machine |
| Arduino UNO | Điều khiển thiết bị vật lý | Serial Communication |
| Giao diện Web | Tương tác người dùng | HTML5 + JavaScript |

#### 2.2 Sơ đồ kết nối

![ai_system_architecture](../../brain/raw/lms_multi_media_dump/assets/index_v3_image1.png)

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài Thực Hành

### Bước 1: Cài Đặt và Khởi Tạo

```javascript
// Khởi tạo mô hình AI từ Teachable Machine
const MODEL_URL = "https://teachablemachine.withgoogle.com/models/VNcQZmGAi/";
let model, port, writer, currentStream;

async function init() {
  try {
    document.getElementById('state').innerText = "Đang tải Model...";
    model = await tmImage.load(MODEL_URL + "model.json", MODEL_URL + "metadata.json");
    document.getElementById('state').innerText = "Model OK. Đang mở Cam...";
    
    await listCameras();
    await startCamera();
    
    document.getElementById('state').innerText = "Sẵn sàng!";
    predict();
  } catch (e) {
    document.getElementById('state').innerText = "Lỗi: " + e.message;
  }
}
```

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Bước 2: Quản Lý Camera Đa Thiết Bị

```javascript
async function listCameras() {
  const devices = await navigator.mediaDevices.enumerateDevices();
  const videoDevices = devices.filter(device => device.kind === 'videoinput');
  const select = document.getElementById('camSelect');
  select.innerHTML = '';
  videoDevices.forEach(device => {
    const option = document.createElement('option');
    option.value = device.deviceId;
    option.text = device.label || `Camera ${select.length + 1}`;
    select.appendChild(option);
  });
}

async function startCamera() {
  if (currentStream) {
    currentStream.getTracks().forEach(track => track.stop());
  }
  const deviceId = document.getElementById('camSelect').value;
  const constraints = {
    video: deviceId ? { deviceId: { exact: deviceId } } : true
  };
  currentStream = await navigator.mediaDevices.getUserMedia(constraints);
  document.getElementById('webcam').srcObject = currentStream;
}
```

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bảng Điều Khiển Người Dùng

### Giao diện Điều Khiển

| Nút chức năng | Mô tả | Hành động |
|---------------|-------|-----------|
| **Chọn Camera** | Danh sách camera khả dụng | Thay đổi nguồn video |
| **Làm mới DS** | Cập nhật danh sách thiết bị | Quét lại thiết bị |
| **Kết nối UNO** | Kết nối Arduino qua Serial | Mở cổng giao tiếp |
| **Gửi thử TEST** | Kiểm tra kết nối | Gửi lệnh test |
| **Ngưỡng** | Độ chính xác nhận diện | Điều chỉnh threshold |

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Phiếu Thực Hành

### Câu 1: Thiết Lập Hệ Thống
**Thời gian**: 20 phút

Thực hiện các bước sau:
1. Truy cập file `index_v3.html`
2. Cho phép quyền truy cập webcam khi trình duyệt yêu cầu
3. Chọn đúng camera tích hợp hoặc webcam ngoài
4. Quan sát trạng thái hệ thống

**Kết quả mong đợi**: Camera hoạt động, trạng thái hiển thị "Sẵn sàng!"

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 2: Tích Hợp Arduino UNO
**Thời gian**: 30 phút

1. Kết nối Arduino UNO với máy tính qua cổng USB
2. Nhấp nút "Kết nối UNO"
3. Gửi lệnh test để kiểm tra kết nối
4. Quan sát nhật ký serial

**Kết quả mong đợi**: Kết nối thành công, có phản hồi từ Arduino

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 3: Điều Chỉnh Ngưỡng Nhận Diện
**Thời gian**: 20 phút

1. Thay đổi giá trị ngưỡng từ 0.5 đến 0.9
2. Quan sát sự thay đổi trong quá trình nhận diện
3. Ghi nhận ảnh hưởng của ngưỡng đến độ chính xác

**Kết luận**: Viết báo cáo ngắn về ảnh hưởng của ngưỡng nhận diện

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu Hỏi Kiểm Tra

### Câu hỏi trắc nghiệm

**Câu 1**: Thư viện nào được sử dụng để xử lý AI trong trình duyệt?
- A) OpenCV.js
- B) TensorFlow.js
- C) PyTorch.js
- D) Keras.js

**Câu 2**: API nào được sử dụng để quản lý camera đa thiết bị?
- A) Canvas API
- B) MediaRecorder API
- C) MediaDevices API
- D) WebGL API

**Câu 3**: Giá trị ngưỡng mặc định trong hệ thống là bao nhiêu?
- A) 0.75
- B) 0.80
- C) 0.85
- D) 0.90

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu hỏi tự luận

**Câu 4**: Giải thích cơ chế hoạt động của hệ thống nhận diện hình ảnh thời gian thực kết hợp với điều khiển Arduino UNO.

**Câu 5**: Phân tích ưu điểm và hạn chế của việc xử lý AI tại biên so với xử lý trên đám mây trong hệ thống này.

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Tình Huống Ứng Dụng

### Scenario: Hệ Thống An Ninh Thông Minh

**Bối cảnh**: Một doanh nghiệp nhỏ muốn xây dựng hệ thống an ninh thông minh sử dụng AI để nhận diện người lạ và tự động kích hoạt cảnh báo.

**Yêu cầu hệ thống**:
- Nhận diện khuôn mặt nhân viên đã đăng ký
- Phát hiện người lạ và gửi tín hiệu cảnh báo
- Điều khiển thiết bị cảnh báo (đèn, còi) qua Arduino UNO
- Ghi nhật ký sự kiện

**Nhiệm vụ học viên**:
1. Thiết kế mô hình nhận diện phù hợp
2. Tích hợp hệ thống với thiết bị cảnh báo
3. Xây dựng giao diện giám sát
4. Kiểm thử và đánh giá hiệu suất

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Tài Nguyên Bổ Sung

### Tài Liệu Tham Khảo
- [Teachable Machine Documentation](https://teachablemachine.withgoogle.com/docs)
- [TensorFlow.js Guide](https://www.tensorflow.org/js/guide)
- [Web Serial API Specification](https://wicg.github.io/serial/)

### Video Hướng Dẫn
- [Cài đặt hệ thống nhận diện AI](link_to_video_1)
- [Kết nối Arduino UNO](link_to_video_2)
- [Tùy chỉnh mô hình AI](link_to_video_3)

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Đánh Giá Hiệu Quả Học Tập

| Tiêu chí | Mức độ đạt được | Ghi chú |
|----------|-----------------|---------|
| Cài đặt hệ thống | ✓ Chưa hoàn thành / ✓ Hoàn thành | |
| Kết nối Arduino | ✓ Chưa hoàn thành / ✓ Hoàn thành | |
| Tùy chỉnh camera | ✓ Chưa hoàn thành / ✓ Hoàn thành | |
| Hiểu nguyên lý hoạt động | ✓ Chưa hoàn thành / ✓ Hoàn thành | |

> [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)