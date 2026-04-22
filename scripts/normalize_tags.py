"""
normalize_tags.py — Chuẩn hóa tags không nhất quán trong file KB
Chạy: python scripts/normalize_tags.py

Vấn đề: Cùng 1 khái niệm nhưng có nhiều tag khác nhau
  [Servo Motor] / [Linh kiện - Servo] / [Servo_Wiring] / [Câu 8] / [Động cơ Servo]
  → Gộp tất cả về 1 tag chuẩn

Output: brain/raw/LMS_KB_IOT_NORMALIZED.md (KHÔNG ghi đè file gốc)
"""

import re
from pathlib import Path

INPUT_FILE  = Path("brain/raw/LMS_KB_IOT_ORIGINAL.md")
OUTPUT_FILE = Path("brain/raw/LMS_KB_IOT_NORMALIZED.md")
DRY_RUN     = False   # ← Đổi False để ghi file thật

# ── BẢNG CHUẨN HÓA TAGS ───────────────────────────────────────────────────────
# Format: "tag_gốc_lowercase" → "TAG_CHUẨN"
# Thêm vào đây khi phát hiện tag mới cần gộp

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
    "câu 4":                        "REVIEW_Uncategorized",
    "câu 5":                        "REVIEW_Uncategorized",
    "câu 8":                        "REVIEW_Uncategorized",
    "câu 9":                        "REVIEW_Uncategorized",
    "câu 11":                       "REVIEW_Uncategorized",
    "câu 28":                       "REVIEW_Uncategorized",
}

# ── REGEX để tìm tag trong dòng fact ──────────────────────────────────────────
# Match: :: [tag nội dung] ở cuối dòng (có thể có ** bao quanh)
TAG_PATTERN = re.compile(r'::\s*\*?\*?\[([^\]]+)\]\*?\*?\s*$', re.MULTILINE)

def normalize_line(line: str) -> tuple[str, str | None, str | None]:
    """
    Trả về (dòng đã normalize, tag_gốc, tag_mới)
    Nếu không có tag hoặc không cần đổi → trả về (dòng gốc, None, None)
    """
    match = TAG_PATTERN.search(line)
    if not match:
        return line, None, None

    tag_original = match.group(1).strip()
    tag_lower = tag_original.lower()

    if tag_lower in TAG_MAP:
        tag_new = TAG_MAP[tag_lower]
        new_line = TAG_PATTERN.sub(f':: [{tag_new}]', line)
        return new_line, tag_original, tag_new

    return line, tag_original, None   # tag không có trong map → giữ nguyên

def run():
    print("=" * 60)
    print(f"  normalize_tags.py — {'DRY RUN' if DRY_RUN else '🚨 GHI FILE THẬT'}")
    print("=" * 60)

    if not INPUT_FILE.exists():
        print(f"[LỖI] Không tìm thấy: {INPUT_FILE}")
        return

    lines = INPUT_FILE.read_text(encoding="utf-8").splitlines(keepends=True)
    print(f"\n  Đọc {len(lines)} dòng từ {INPUT_FILE}\n")

    new_lines = []
    stats = {"changed": 0, "kept": 0, "unknown": set()}

    for line in lines:
        new_line, tag_orig, tag_new = normalize_line(line)

        if tag_new is not None:
            print(f"  ✅ [{tag_orig}] → [{tag_new}]")
            stats["changed"] += 1
        elif tag_orig is not None:
            stats["unknown"].add(tag_orig)
            stats["kept"] += 1

        new_lines.append(new_line)

    # ── BÁO CÁO ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  KẾT QUẢ")
    print("=" * 60)
    print(f"  ✅ Tags đã chuẩn hóa : {stats['changed']}")
    print(f"  ⚪ Tags giữ nguyên   : {stats['kept']}")

    if stats["unknown"]:
        print(f"\n  ⚠️  Tags chưa có trong TAG_MAP ({len(stats['unknown'])} tags):")
        for t in sorted(stats["unknown"]):
            print(f"     [{t}]")
        print("\n  → Thêm các tags này vào TAG_MAP trong script rồi chạy lại.")

    if DRY_RUN:
        print(f"\n  ⚡ DRY RUN — chưa ghi file.")
        print(f"  ⚡ Đổi DRY_RUN = False để ghi ra: {OUTPUT_FILE}")
    else:
        OUTPUT_FILE.write_text("".join(new_lines), encoding="utf-8")
        print(f"\n  ✅ Đã ghi: {OUTPUT_FILE}")
        print(f"  ✅ File gốc {INPUT_FILE} KHÔNG bị thay đổi.")

if __name__ == "__main__":
    run()
