# 🔌 HARDWARE MAP (Yolo Uno / ESP32-S3)
# ---------------------------------------
# Cảm biến độ ẩm đất (Analog): Port P0 (GPIO 1)
# Máy bơm (Relay - Digital): Port P1 (GPIO 2)
# Đèn Led RGB (Tích hợp): NeoPixel Pin 48
# ---------------------------------------

import time # type: ignore
from yolouno import *  # type: ignore
from machine import Pin, ADC # type: ignore

# Cấu hình thiết bị
moisture_sensor = ADC(Pin(1))  # Chân Analog P0
moisture_sensor.atten(ADC.ATTN_11DB)  # Dải đo 0-3.6V

pump = Pin(2, Pin.OUT)  # Chân Digital P1 (Điều khiển Relay)

# Ngưỡng (Thresholds)
DRY_THRESHOLD = 500  # Giá trị ADC (Cần căn chỉnh thực tế)
PUMP_RUN_TIME = 2000  # ms (Thời gian tưới mỗi lần)

# Biến trạng thái (Non-blocking control)
last_check_time = 0
check_interval = 1000  # 1 giây kiểm tra một lần

def read_moisture():
    """Đọc giá trị trung bình từ cảm biến để chống nhiễu."""
    total = 0
    for _ in range(5):
        total += moisture_sensor.read()
        time.sleep_ms(10)
    return total // 5

def start_irrigation():
    """Logic tưới nước an toàn."""
    print("💧 Đang bắt đầu tưới nước...")
    pump.value(1)  # Bật máy bơm
    
    # Sử dụng vòng lặp non-blocking thay vì sleep
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < PUMP_RUN_TIME:
        # Có thể thêm logic kiểm tra an toàn tại đây (vídụ: ngắt khẩn cấp)
        pass
        
    pump.value(0)  # Tắt máy bơm
    print("✅ Đã hoàn tất chu kỳ tưới.")

def main_loop():
    global last_check_time
    
    print("🚀 Hệ thống Tưới cây thông minh đang khởi động...")
    pump.value(0)  # Đảm bảo máy bơm tắt khi khởi động
    
    while True:
        try:
            current_time = time.ticks_ms()
            
            # Kiểm tra định kỳ (Non-blocking)
            if time.ticks_diff(current_time, last_check_time) > check_interval:
                moisture_level = read_moisture()
                print("Moisture Level:", moisture_level)
                
                if moisture_level > DRY_THRESHOLD:
                    start_irrigation()
                
                last_check_time = current_time
                
            # Duy trì hệ thống phản hồi nhanh cho các tác vụ khác (nếu có)
            time.sleep_ms(10)
            
        except Exception as e:
            print("❌ Lỗi hệ thống:", e)
            pump.value(0)  # Tắt máy bơm ngay lập tức nếu có lỗi
            time.sleep(5)  # Đợi trước khi thử lại

# Chạy chương trình
if __name__ == "__main__":
    main_loop()
