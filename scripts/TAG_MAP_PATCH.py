# PATCH — Thay toàn bộ TAG_MAP trong normalize_tags.py
# Tìm dòng "TAG_MAP = {" và thay đến dòng "}" đóng

TAG_MAP = {
    # ── SERVO MOTOR ───────────────────────────────────────────────
    "servo motor":                  "Servo_Motor",
    "linh kiện - servo":            "Servo_Motor",
    "servo_wiring":                 "Servo_Motor",
    "động cơ servo":                "Servo_Motor",
    "động cơ":                      "Servo_Motor",
    "yolobit_servo":                "Servo_Motor",

    # ── LED ───────────────────────────────────────────────────────
    "led polarity":                 "LED_Polarity",
    "led_polarity":                 "LED_Polarity",
    "linh kiện - led":              "LED_Polarity",
    "led component":                "LED_Polarity",
    "cấu tạo led":                  "LED_Polarity",
    "led matrix":                   "LED_Matrix",
    "halocode led":                 "LED_Matrix",

    # ── ARDUINO POWER ─────────────────────────────────────────────
    "arduino power":                "Arduino_Power",
    "arduino powering":             "Arduino_Power",
    "arduino_voltage":              "Arduino_Power",
    "arduino_connection":           "Arduino_Power",
    "nguồn điện arduino":           "Arduino_Power",
    "điện áp":                      "Arduino_Power",
    "connectivity":                 "Arduino_Power",

    # ── ARDUINO COMMUNICATION ─────────────────────────────────────
    "arduino communication":        "Arduino_Communication",
    "wireless communication":       "Arduino_Communication",
    "yolobit_wireless":             "Arduino_Communication",

    # ── BREADBOARD ────────────────────────────────────────────────
    "breadboard":                   "Breadboard",
    "breadboard layout":            "Breadboard",
    "kỹ thuật lắp mạch":            "Breadboard",
    "sensor wiring":                "Breadboard",
    "wiring":                       "Breadboard",
    "kết nối phần cứng":            "Breadboard",

    # ── TEACHABLE MACHINE ─────────────────────────────────────────
    "machine learning":             "Teachable_Machine",
    "ai - teachable machine":       "Teachable_Machine",
    "teachable_machine_extension":  "Teachable_Machine",

    # ── BUZZER ────────────────────────────────────────────────────
    "linh kiện - buzzer":           "Buzzer",
    "linh kiện buzzer":             "Buzzer",
    "buzzer_specs":                 "Buzzer",

    # ── ISD1820 ───────────────────────────────────────────────────
    "isd1820":                      "ISD1820",
    "linh kiện - isd1820":          "ISD1820",
    "isd1820_logic":                "ISD1820",

    # ── MBLOCK ────────────────────────────────────────────────────
    "mblock5 modes":                "mBlock_Modes",
    "mblock modes":                 "mBlock_Modes",
    "lập trình live":               "mBlock_Modes",
    "mblock_live_mode":             "mBlock_Modes",
    "mblock workflow":              "mBlock_Modes",
    "mblock5 messaging":            "mBlock_Messaging",
    "lập trình - giao tiếp":        "mBlock_Messaging",
    "mblock_variable_creation":     "mBlock_Variable",
    "lập trình khối":               "mBlock_Variable",
    "mblock cloud services":        "mBlock_Cloud",

    # ── AI EXTENSION ──────────────────────────────────────────────
    "ai extension":                 "AI_Extension",
    "cognitive services":           "AI_Extension",

    # ── SENSORS ───────────────────────────────────────────────────
    "ir sensor":                    "IR_Sensor",
    "ir sensor components":         "IR_Sensor",
    "cảm biến hồng ngoại":          "IR_Sensor",
    "pir sensor":                   "PIR_Sensor",
    "linh kiện - pir":              "PIR_Sensor",
    "cảm biến":                     "Sensor_General",
    "linh kiện - cảm biến":         "Sensor_General",
    "nguyên lý cảm biến":           "Sensor_General",
    "sensor calibration":           "Sensor_General",
    "ultrasonic sensor":            "Ultrasonic_Sensor",
    "dht20 sensor":                 "DHT20_Sensor",

    # ── JOYSTICK ──────────────────────────────────────────────────
    "joystick":                     "Joystick",
    "joystick component":           "Joystick",
    "lập trình joystick":           "Joystick",

    # ── LCD / I2C ─────────────────────────────────────────────────
    "i2c protocol":                 "I2C_LCD",
    "lcd i2c":                      "I2C_LCD",

    # ── MOTOR DRIVER ──────────────────────────────────────────────
    "l298n driver":                 "Motor_Driver_L298",
    "mạch công suất l298":          "Motor_Driver_L298",
    "vibration_motor_wiring":       "Vibration_Motor",

    # ── IOT ───────────────────────────────────────────────────────
    "iot definition":               "IoT_Definition",
    "halocode_iot":                 "IoT_Definition",

    # ── HALOCODE ──────────────────────────────────────────────────
    "halocode hardware":            "Halocode_Hardware",
    "halocode_hardware":            "Halocode_Hardware",
    "halocode_connection":          "Halocode_Hardware",
    "halocode_programming":         "Halocode_Programming",
    "halocode_sensor":              "Halocode_Sensor",

    # ── YOLOBIT ───────────────────────────────────────────────────
    "cấu tạo yolo:bit":             "YoloBit_Hardware",
    "yolo:bit hardware":            "YoloBit_Hardware",
    "yolobit_hardware":             "YoloBit_Hardware",
    "yolobit_logic":                "YoloBit_Programming",
    "lập trình khối":               "YoloBit_Programming",
    "giao diện lập trình":          "YoloBit_Programming",
    "hiển thị":                     "YoloBit_Display",
    "yolobit_analog":               "YoloBit_Sensor",
    "yolobit_sensor":               "YoloBit_Sensor",
    "yolobit_software":             "YoloBit_Software",
    "tính năng phần mềm":           "YoloBit_Software",
    "quản lý dự án":                "YoloBit_Software",
    "hệ thống":                     "YoloBit_Software",
    "storage":                      "YoloBit_Software",

    # ── CÂU HỎI → GOM THEO MODULE ─────────────────────────────────
    # Arduino Module 1
    "arduino_module_1_q1":          "Arduino_M1_Facts",
    "arduino_module_1_q2":          "Arduino_M1_Facts",
    "arduino_module_1_q3":          "Arduino_M1_Facts",
    "arduino_module_1_q6":          "Arduino_M1_Facts",
    "arduino_module_1_q7":          "Arduino_M1_Facts",
    "arduino_module_1_q10, q11":    "Arduino_M1_Facts",
    "arduino_module_1_q13":         "Arduino_M1_Facts",
    "arduino_module_1_q14":         "Arduino_M1_Facts",
    "arduino_module_1_q15":         "Arduino_M1_Facts",
    "arduino m1,2 - q1":            "Arduino_M1_Facts",
    "arduino m1,2 - q2":            "Arduino_M1_Facts",
    "arduino m1,2 - q3":            "Arduino_M1_Facts",
    "arduino m1,2 - q4":            "Arduino_M1_Facts",
    "arduino m1,2 - q5":            "Arduino_M1_Facts",
    "arduino m1,2 - q6":            "Arduino_M1_Facts",
    "arduino m1,2 - q7":            "Arduino_M1_Facts",
    "arduino m1,2 - q9, q11":       "Arduino_M1_Facts",
    "arduino m1,2 - q10":           "Arduino_M1_Facts",
    "arduino m1,2 - q13":           "Arduino_M1_Facts",

    # Arduino Module 2
    "arduino m2 - câu 1":           "Arduino_M2_Facts",
    "arduino m2 - câu 2":           "Arduino_M2_Facts",
    "arduino m2 - câu 4":           "Arduino_M2_Facts",
    "arduino m2 - câu 4, 7":        "Arduino_M2_Facts",
    "arduino m2 - câu 4/7":         "Arduino_M2_Facts",
    "arduino m2 - câu 8":           "Arduino_M2_Facts",
    "arduino m2 - câu 9":           "Arduino_M2_Facts",
    "arduino m2 - câu 10":          "Arduino_M2_Facts",
    "arduino m2 - câu 12":          "Arduino_M2_Facts",
    "arduino m2 - câu 13":          "Arduino_M2_Facts",
    "arduino m2 - đề 1":            "Arduino_M2_Facts",
    "arduino m2 - đề 2":            "Arduino_M2_Facts",

    # Câu số đơn lẻ → gom về Uncategorized để review sau
    "câu 1":                        "REVIEW_Uncategorized",
    "câu 1, 13":                    "REVIEW_Uncategorized",
    "câu 1, câu 9":                 "REVIEW_Uncategorized",
    "câu 2":                        "REVIEW_Uncategorized",
    "câu 3":                        "REVIEW_Uncategorized",
    "câu 3, câu 4":                 "REVIEW_Uncategorized",
    "câu 5, câu 19":                "REVIEW_Uncategorized",
    "câu 6, 7":                     "REVIEW_Uncategorized",
    "câu 7":                        "REVIEW_Uncategorized",
    "câu 8, câu 12":                "REVIEW_Uncategorized",
    "câu 10":                       "REVIEW_Uncategorized",
    "câu 12":                       "REVIEW_Uncategorized",
    "câu 14":                       "REVIEW_Uncategorized",
    "câu 17":                       "REVIEW_Uncategorized",
    "câu 20":                       "REVIEW_Uncategorized",
    "câu 21":                       "REVIEW_Uncategorized",
    "câu 25":                       "REVIEW_Uncategorized",
    "câu 29":                       "REVIEW_Uncategorized",
    "câu 31":                       "REVIEW_Uncategorized",
}
