Đã hiểu, mình đã cập nhật phiên bản **v3** bổ sung thêm **Danh sách chọn Camera**. Nếu trình duyệt mặc định chọn DroidCam, bạn chỉ cần bấm vào ô chọn để đổi sang Camera tích hợp (Integrated Camera) hoặc Webcam khác.

### Bước 1: Tải file mới
Bạn mở file này: **[index_v3.html](sandbox:/mnt/data/index_v3.html)**

### Bước 2: Cách chọn lại Camera
1. Khi trang vừa mở, trình duyệt sẽ hỏi quyền Webcam -> Bấm **Cho phép (Allow)**.
2. Tại mục **Chọn camera**, bấm vào danh sách xổ xuống.
3. Chọn đúng tên Camera bạn muốn dùng (ví dụ: *Integrated Webcam*, *USB Camera*,...).
4. Trang sẽ tự động chuyển luồng hình ảnh sang camera đó.

---

### Nội dung file `index_v3.html` (Đã sửa lỗi nạp thư viện và thêm chọn Camera):

```python
# Tạo file index_v3.html với tính năng chọn Camera và sửa lỗi nạp thư viện
html = r"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>TM → Yolo UNO (v3 - Chọn Camera)</title>
  <style>
    body{font-family: system-ui, -apple-system, sans-serif; margin:16px; background:#f4f7f6}
    .card{background:#fff; border-radius:12px; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.1); margin-bottom:16px}
    .row{display:flex; gap:16px; flex-wrap:wrap}
    video, canvas{border:2px solid #333; border-radius:8px; background:#000; width:320px; height:240px}
    button, select, input{padding:8px 12px; border-radius:6px; border:1px solid #ccc; margin:4px 0}
    button{background:#007bff; color:#fff; cursor:pointer; border:none}
    button:hover{background:#0056b3}
    .log{height:150px; overflow:auto; font-size:12px; background:#222; color:#2ecc71; padding:8px; border-radius:8px; font-family:monospace}
    .pill{padding:2px 8px; border-radius:12px; background:#eee; font-size:13px}
    .err{color:#e74c3c}
  </style>
</head>
<body>
  <h2>AI Recognition → Yolo UNO (v3)</h2>
  
  <div class="card">
    <strong>1. Cấu hình Camera & Model</strong><br>
    Chọn Camera: <select id="camSelect"></select> 
    <button id="btnReloadCam">Làm mới DS</button><br>
    Trạng thái: <span id="state" class="pill">Đang tải...</span>
  </div>

  <div class="card">
    <strong>2. Kết nối & Điều khiển</strong><br>
    <button id="btnSerial" style="background:#27ae60">Kết nối UNO</button>
    <button id="btnTest">Gửi thử TEST</button>
    <span style="margin-left:15px">Ngưỡng:</span> 
    <input id="thresh" type="number" value="0.80" min="0" max="1" step="0.05" style="width:60px">
  </div>

  <div class="row">
    <div>
      <video id="webcam" autoplay playsinline></video>
      <div id="label-container" style="font-weight:bold; margin-top:5px">Đang chờ dự đoán...</div>
    </div>
    <canvas id="canvas"></canvas>
  </div>

  <div class="card" style="margin-top:16px">
    <strong>Nhật ký gửi Serial (Dùng cho Dashboard V1, V2)</strong>
    <div id="log" class="log"></div>
  </div>

  <!-- Load Libraries -->
  <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@3.21.0/dist/tf.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@0.8/dist/teachablemachine-image.min.js"></script>

  <script>
    const MODEL_URL = "https://teachablemachine.withgoogle.com/models/VNcQZmGAi/";
    let model, port, writer, currentStream;
    let lastLabel = "", lastScore = 0;

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

    async function predict() {
      const video