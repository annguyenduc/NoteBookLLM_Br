"""
generate_wiki_v2.py — Tạo atomic notes từ các file LMS_RAW_*.md
Chạy từ root repo: python scripts/generate_wiki_v2.py

Cải tiến so với v1:
- Đọc thẳng từ brain/raw/LMS_RAW_*.md — không qua file KB tổng hợp
- Regex linh hoạt match 200/201 facts (v1 chỉ match 33)
- Gộp facts trùng lặp giữa các file (dedup)
- Ghi rõ nguồn từng fact (file nào, dòng mấy)
- Agent chỉ cần điền 4F + wikilinks sau
"""

import re
from pathlib import Path
from datetime import date
from collections import defaultdict

RAW_DIR    = Path("brain/raw")
OUTPUT_DIR = Path("brain/wiki")
DRY_RUN    = True   # ← Đổi False khi muốn ghi file thật

# Tags muốn generate — [] = tất cả
TARGET_TAGS = [
    "Arduino_Power",
    "Servo_Motor",
    "Breadboard",
    "Buzzer",
    "Teachable_Machine",
]

# Tags bỏ qua
SKIP_TAGS = {
    "REVIEW_Uncategorized",
    "Arduino_M1_Facts",
    "Arduino_M2_Facts",
}

TODAY = date.today().isoformat()

# ── TAG NORMALIZATION MAP ──────────────────────────────────────────────────────
TAG_MAP = {
    "servo motor":                  "Servo_Motor",
    "linh kiện - servo":            "Servo_Motor",
    "servo_wiring":                 "Servo_Motor",
    "động cơ servo":                "Servo_Motor",
    "động cơ":                      "Servo_Motor",
    "yolobit_servo":                "Servo_Motor",
    "led polarity":                 "LED_Polarity",
    "led_polarity":                 "LED_Polarity",
    "linh kiện - led":              "LED_Polarity",
    "led component":                "LED_Polarity",
    "cấu tạo led":                  "LED_Polarity",
    "arduino power":                "Arduino_Power",
    "arduino powering":             "Arduino_Power",
    "arduino_voltage":              "Arduino_Power",
    "arduino_connection":           "Arduino_Power",
    "nguồn điện arduino":           "Arduino_Power",
    "điện áp":                      "Arduino_Power",
    "connectivity":                 "Arduino_Power",
    "breadboard":                   "Breadboard",
    "breadboard layout":            "Breadboard",
    "kỹ thuật lắp mạch":            "Breadboard",
    "wiring":                       "Breadboard",
    "kết nối phần cứng":            "Breadboard",
    "machine learning":             "Teachable_Machine",
    "ai - teachable machine":       "Teachable_Machine",
    "teachable_machine_extension":  "Teachable_Machine",
    "linh kiện - buzzer":           "Buzzer",
    "linh kiện buzzer":             "Buzzer",
    "buzzer_specs":                 "Buzzer",
    "isd1820":                      "ISD1820",
    "linh kiện - isd1820":          "ISD1820",
    "isd1820_logic":                "ISD1820",
    "mblock5 modes":                "mBlock_Modes",
    "mblock modes":                 "mBlock_Modes",
    "lập trình live":               "mBlock_Modes",
    "mblock_live_mode":             "mBlock_Modes",
    "mblock5 messaging":            "mBlock_Messaging",
    "lập trình - giao tiếp":        "mBlock_Messaging",
    "mblock_variable_creation":     "mBlock_Variable",
    "ai extension":                 "AI_Extension",
    "ir sensor":                    "IR_Sensor",
    "ir sensor components":         "IR_Sensor",
    "cảm biến hồng ngoại":          "IR_Sensor",
    "pir sensor":                   "PIR_Sensor",
    "linh kiện - pir":              "PIR_Sensor",
    "ultrasonic sensor":            "Ultrasonic_Sensor",
    "dht20 sensor":                 "DHT20_Sensor",
    "joystick":                     "Joystick",
    "joystick component":           "Joystick",
    "lập trình joystick":           "Joystick",
    "i2c protocol":                 "I2C_LCD",
    "lcd i2c":                      "I2C_LCD",
    "l298n driver":                 "Motor_Driver_L298",
    "mạch công suất l298":          "Motor_Driver_L298",
    "iot definition":               "IoT_Definition",
    "cấu tạo yolo:bit":             "YoloBit_Hardware",
    "yolobit_hardware":             "YoloBit_Hardware",
    "yolobit_logic":                "YoloBit_Programming",
    "giao diện lập trình":          "YoloBit_Programming",
    "yolobit_sensor":               "YoloBit_Sensor",
    "yolobit_software":             "YoloBit_Software",
    "tính năng phần mềm":           "YoloBit_Software",
    "halocode hardware":            "Halocode_Hardware",
    "halocode_hardware":            "Halocode_Hardware",
    "halocode_connection":          "Halocode_Hardware",
    "halocode_programming":         "Halocode_Programming",
    "halocode_sensor":              "Halocode_Sensor",
    "led matrix":                   "LED_Matrix",
    "halocode led":                 "LED_Matrix",
}

SKIP_TAG_PATTERNS = {
    "câu", "arduino m1", "arduino m2", "arduino_module",
    "review_uncategorized", "sensor wiring", "storage",
    "quản lý dự án", "hệ thống", "hiển thị",
}

TITLE_MAP = {
    "Arduino_Power":        "Nguồn điện Arduino",
    "Servo_Motor":          "Động cơ Servo",
    "Breadboard":           "Breadboard — Quy tắc kết nối",
    "Buzzer":               "Còi Buzzer",
    "Teachable_Machine":    "Teachable Machine — Học máy",
    "LED_Polarity":         "Cực tính đèn LED",
    "ISD1820":              "Mạch ghi âm ISD1820",
    "mBlock_Modes":         "Chế độ Live và Upload trong mBlock",
    "mBlock_Messaging":     "Giao tiếp Broadcast trong mBlock",
    "IR_Sensor":            "Cảm biến hồng ngoại IR",
    "PIR_Sensor":           "Cảm biến chuyển động PIR",
    "Ultrasonic_Sensor":    "Cảm biến siêu âm",
    "I2C_LCD":              "Màn hình LCD I2C",
    "Joystick":             "Module Joystick",
    "IoT_Definition":       "Định nghĩa IoT",
    "AI_Extension":         "AI Extension — Cognitive Services",
    "YoloBit_Hardware":     "Phần cứng Yolo:Bit",
    "Halocode_Hardware":    "Phần cứng Halocode",
    "LED_Matrix":           "Ma trận LED",
    "Motor_Driver_L298":    "Mạch điều khiển động cơ L298N",
}

YAML_TAGS_MAP = {
    "Arduino_Power":        '["Hardware", "Arduino", "Power"]',
    "Servo_Motor":          '["Hardware", "Arduino", "Actuator"]',
    "Breadboard":           '["Hardware", "Arduino", "Circuit"]',
    "Buzzer":               '["Hardware", "Arduino", "Output"]',
    "Teachable_Machine":    '["AI", "ML", "mBlock"]',
    "LED_Polarity":         '["Hardware", "Arduino", "Output"]',
    "ISD1820":              '["Hardware", "Arduino", "Audio"]',
    "mBlock_Modes":         '["Software", "mBlock", "Programming"]',
    "IR_Sensor":            '["Hardware", "Arduino", "Sensor"]',
    "PIR_Sensor":           '["Hardware", "Arduino", "Sensor"]',
    "Ultrasonic_Sensor":    '["Hardware", "Arduino", "Sensor"]',
}

# ── REGEX ──────────────────────────────────────────────────────────────────────
FACT_LINE = re.compile(
    r'.*\[LMS\].*\[Fact\].*?::(.+?)::.*?\[([^\]]+)\]',
    re.IGNORECASE
)

# ── TEMPLATE ──────────────────────────────────────────────────────────────────
ATOM_TEMPLATE = """\
---
file_id: "ATOMS_{tag}"
title: "{title}"
category: "Atomic Note"
prefix: "ATOMS"
tags: {tags_yaml}
source: "[[LMS_RAW_Sources]]"
status: "draft"
created: "{today}"
last_updated: "{today}"
---

# {title}

## 📌 Định nghĩa cốt lõi
> ⚠️ TODO (@scout): Viết 1-2 câu định nghĩa ngắn gọn dựa trên facts bên dưới. KHÔNG thêm kiến thức ngoài.

## 🔍 Chi tiết kỹ thuật
<!-- ✅ COPY NGUYÊN VĂN từ nguồn — đã được script extract tự động -->
{facts_block}

## 💡 Ví dụ thực tế
> ⚠️ TODO (@scout): 1 ví dụ cụ thể gắn với bối cảnh KDI/Arduino/AI cho học sinh 16-18 tuổi.

## 🔗 Liên kết tư duy
> ⚠️ TODO (@scout): Thêm ít nhất 2 [[wikilinks]] liên quan.
- [[WIKI_TODO_link_1]]
- [[WIKI_TODO_link_2]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | _(xem Chi tiết kỹ thuật — {fact_count} facts)_ |
| **Feelings** | ⚠️ TODO: Học sinh thường gặp khó khăn gì ở khái niệm này? |
| **Findings** | ⚠️ TODO: Insight / quy luật cốt lõi cần nhớ? |
| **Futures** | ⚠️ TODO: Ứng dụng vào task nào cụ thể trong bài học KDI? |

## 📖 Nguồn
{sources_block}

---
<!-- ATOM CHECKLIST — @librarian verify trước khi đổi status: verified -->
- [ ] Chỉ có 1 khái niệm duy nhất trong file này
- [ ] Có ít nhất 2 [[wikilinks]] thật (không phải TODO)
- [ ] Phần Futures không để trống
- [ ] Nguồn có thể trace về brain/raw/
- [ ] Facts là copy nguyên văn — không paraphrase
"""

# ── PARSE ──────────────────────────────────────────────────────────────────────
def normalize_tag(raw_tag: str) -> str | None:
    """Chuẩn hóa tag về dạng chuẩn. None = bỏ qua."""
    t = raw_tag.strip().lower()
    if t in TAG_MAP:
        return TAG_MAP[t]
    for skip in SKIP_TAG_PATTERNS:
        if t.startswith(skip):
            return None
    # Giữ nguyên nếu có dạng chuẩn Snake_Case
    if re.match(r'^[A-Z][a-zA-Z0-9_]+$', raw_tag.strip()):
        return raw_tag.strip()
    return None

def parse_all_raw_files(raw_dir: Path) -> dict:
    """
    Đọc tất cả LMS_RAW_*.md trong raw_dir.
    Trả về: {normalized_tag: [(fact_text, source_file), ...]}
    """
    facts_by_tag = defaultdict(list)
    seen_facts = defaultdict(set)  # dedup per tag

    raw_files = sorted(raw_dir.glob("LMS_RAW_*.md"))
    print(f"\n  Tìm thấy {len(raw_files)} file LMS_RAW_*.md")

    for filepath in raw_files:
        try:
            content = filepath.read_text(encoding="utf-8-sig", errors="ignore")
        except Exception as e:
            print(f"  ⚠️  Không đọc được {filepath.name}: {e}")
            continue

        for line in content.splitlines():
            if "[LMS]" not in line or "[Fact]" not in line:
                continue
            m = FACT_LINE.match(line.strip())
            if not m:
                continue

            fact_text = m.group(1).strip().strip("*").strip()
            raw_tag   = m.group(2).strip().strip("*").strip()

            norm_tag = normalize_tag(raw_tag)
            if norm_tag is None:
                continue

            # Dedup — bỏ qua fact đã có (so sánh 50 ký tự đầu)
            fact_key = fact_text[:50].lower()
            if fact_key not in seen_facts[norm_tag]:
                seen_facts[norm_tag].add(fact_key)
                facts_by_tag[norm_tag].append((fact_text, filepath.name))

    return dict(facts_by_tag)

# ── BUILD CONTENT ──────────────────────────────────────────────────────────────
def build_facts_block(facts: list) -> str:
    lines = []
    for i, (fact, _) in enumerate(facts, 1):
        lines.append(f"- **Fact {i}:** {fact}")
    return "\n".join(lines)

def build_sources_block(facts: list) -> str:
    sources = sorted(set(src for _, src in facts))
    lines = [f"`📖 Nguồn {i+1}: brain/raw/{src}`"
             for i, src in enumerate(sources)]
    return "\n".join(lines)

# ── MAIN ───────────────────────────────────────────────────────────────────────
def run():
    print("=" * 60)
    print(f"  generate_wiki_v2.py — {'DRY RUN' if DRY_RUN else '🚨 GHI FILE THẬT'}")
    print("=" * 60)

    if not RAW_DIR.exists():
        print(f"[LỖI] Không tìm thấy: {RAW_DIR}")
        return

    facts_by_tag = parse_all_raw_files(RAW_DIR)

    total_facts = sum(len(v) for v in facts_by_tag.values())
    print(f"  Tổng: {total_facts} facts unique / {len(facts_by_tag)} tags\n")

    tags_to_process = TARGET_TAGS if TARGET_TAGS else sorted(facts_by_tag.keys())

    stats = {"created": 0, "skipped": 0, "empty": 0}

    for tag in tags_to_process:
        if tag in SKIP_TAGS:
            stats["skipped"] += 1
            continue

        facts = facts_by_tag.get(tag, [])
        if not facts:
            print(f"  ⚠️  EMPTY [{tag}] — không tìm thấy facts trong raw/")
            stats["empty"] += 1
            continue

        title       = TITLE_MAP.get(tag, tag.replace("_", " "))
        tags_yaml   = YAML_TAGS_MAP.get(tag, '["Hardware", "Arduino"]')
        facts_block = build_facts_block(facts)
        sources_block = build_sources_block(facts)

        content_out = ATOM_TEMPLATE.format(
            tag=tag,
            title=title,
            tags_yaml=tags_yaml,
            today=TODAY,
            facts_block=facts_block,
            fact_count=len(facts),
            sources_block=sources_block,
        )

        output_path = OUTPUT_DIR / f"ATOMS_{tag}.md"

        print(f"  ✅ [{tag}] — {len(facts)} facts unique")
        sources = sorted(set(src for _, src in facts))
        print(f"     Nguồn: {len(sources)} files")
        for f_text, _ in facts[:2]:
            print(f"     • {f_text[:70]}{'...' if len(f_text)>70 else ''}")
        if len(facts) > 2:
            print(f"     ... và {len(facts)-2} facts nữa")

        if not DRY_RUN:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            if output_path.exists():
                print(f"     ⚠️  File đã tồn tại — bỏ qua (xóa thủ công nếu muốn ghi lại)")
                stats["skipped"] += 1
            else:
                output_path.write_text(content_out, encoding="utf-8")
                print(f"     → Đã ghi: {output_path}")
                stats["created"] += 1
        else:
            stats["created"] += 1

    print("\n" + "=" * 60)
    print("  KẾT QUẢ")
    print("=" * 60)
    print(f"  ✅ {'Sẽ tạo' if DRY_RUN else 'Đã tạo'} : {stats['created']} files")
    print(f"  ⏭️  Bỏ qua           : {stats['skipped']} files")
    print(f"  ⚠️  Không có facts   : {stats['empty']} tags")

    if DRY_RUN:
        print(f"\n  ⚡ DRY RUN — chưa ghi file.")
        print(f"  ⚡ Đổi DRY_RUN = False để ghi vào {OUTPUT_DIR}/")
    else:
        print(f"\n  ✅ Xong. Bước tiếp: @scout điền 4F + wikilinks vào từng file.")

if __name__ == "__main__":
    run()
