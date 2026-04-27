"""
generate_atoms.py — Tạo atomic notes từ file KB đã normalize
Chạy: python scripts/generate_atoms.py

Nguyên tắc:
- Facts được COPY NGUYÊN VĂN từ file nguồn — không paraphrase
- Agent CHỈ cần điền 4F và wikilinks sau
- Mỗi tag → 1 file ATOMS_[tag].md trong 3-resources/wiki/
"""

import re
from pathlib import Path
from datetime import date

INPUT_FILE  = Path("3-resources/raw/LMS_KB_IOT_NORMALIZED.md")
OUTPUT_DIR  = Path("brain/wiki")
DRY_RUN     = False   # ← Đổi False khi muốn ghi file thật

# Tags muốn generate — để trống [] để generate tất cả
TARGET_TAGS = [
    "Arduino_Power",
    "Servo_Motor",
    "Breadboard",
    "Buzzer",
    "Teachable_Machine",
]

# Tags cần bỏ qua
SKIP_TAGS = {
    "REVIEW_Uncategorized",
    "Arduino_M1_Facts",
    "Arduino_M2_Facts",
}

TODAY = date.today().isoformat()

# ── TEMPLATE ──────────────────────────────────────────────────────────────────
ATOM_TEMPLATE = """\
---
file_id: "ATOMS_{tag}"
title: "{title}"
category: "Atomic Note"
prefix: "ATOMS"
tags: {tags_yaml}
source: "[[LMS_KB_IOT_NORMALIZED.md]]"
status: "draft"
created: "{today}"
last_updated: "{today}"
---

# {title}

## 📌 Định nghĩa cốt lõi
> ⚠️ TODO (@scout): Viết 1-2 câu định nghĩa ngắn gọn dựa trên facts bên dưới.

## 🔍 Chi tiết kỹ thuật
<!-- COPY NGUYÊN VĂN từ nguồn — KHÔNG paraphrase -->
{facts_block}

## 💡 Ví dụ thực tế
> ⚠️ TODO (@scout): 1 ví dụ cụ thể gắn với bối cảnh KDI/Arduino/AI cho học sinh 16-18 tuổi.

## 🔗 Liên kết tư duy
> ⚠️ TODO (@scout): Thêm ít nhất 2 wikilinks liên quan.
- [[WIKI_TODO_1]]
- [[WIKI_TODO_2]]

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | _(tự động — xem Chi tiết kỹ thuật)_ |
| **Feelings** | ⚠️ TODO: Học sinh thường gặp khó khăn gì? |
| **Findings** | ⚠️ TODO: Insight / quy luật cốt lõi? |
| **Futures** | ⚠️ TODO: Ứng dụng vào task nào cụ thể? |

## 📖 Nguồn
`📖 Nguồn: 3-resources/raw/LMS_KB_IOT_NORMALIZED.md — tag [{tag}]`

---
<!-- ATOM CHECKLIST — @librarian verify trước khi đổi status: verified -->
- [ ] Chỉ có 1 khái niệm duy nhất trong file này
- [ ] Có ít nhất 2 [[wikilinks]]
- [ ] Phần Futures không để trống
- [ ] Nguồn có thể trace về 3-resources/raw/
- [ ] Facts là copy nguyên văn, không paraphrase
"""

# ── PARSE FACTS ───────────────────────────────────────────────────────────────
FACT_PATTERN = re.compile(
    r'\*{0,2}\[LMS\]\s*\[Fact\]\s*(?:::|::)\s*\*{0,2}(.+?)\s*(?:::|::)\s*\[([^\]]+)\]',
    re.IGNORECASE
)

def parse_facts(content: str) -> dict[str, list[str]]:
    """Trả về dict: tag → [fact1, fact2, ...]"""
    facts_by_tag: dict[str, list[str]] = {}
    for match in FACT_PATTERN.finditer(content):
        fact_text = match.group(1).strip().rstrip('*').strip()
        tag = match.group(2).strip()
        if tag not in facts_by_tag:
            facts_by_tag[tag] = []
        facts_by_tag[tag].append(fact_text)
    return facts_by_tag

def tag_to_title(tag: str) -> str:
    """Arduino_Power → Nguồn điện Arduino"""
    title_map = {
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
        "Arduino_Communication":"Giao tiếp Arduino",
        "YoloBit_Hardware":     "Phần cứng Yolo:Bit",
        "YoloBit_Programming":  "Lập trình Yolo:Bit",
        "Halocode_Hardware":    "Phần cứng Halocode",
        "LED_Matrix":           "Ma trận LED",
        "Motor_Driver_L298":    "Mạch điều khiển động cơ L298N",
        "DHT20_Sensor":         "Cảm biến nhiệt độ/độ ẩm DHT20",
    }
    return title_map.get(tag, tag.replace("_", " "))

def tag_to_yaml_tags(tag: str) -> str:
    category_map = {
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
    return category_map.get(tag, '["Hardware", "Arduino"]')

def build_facts_block(facts: list[str]) -> str:
    lines = []
    for i, fact in enumerate(facts, 1):
        lines.append(f"- **Fact {i}:** {fact}")
    return "\n".join(lines)

# ── MAIN ──────────────────────────────────────────────────────────────────────
def run():
    print("=" * 60)
    print(f"  generate_atoms.py — {'DRY RUN' if DRY_RUN else '🚨 GHI FILE THẬT'}")
    print("=" * 60)

    if not INPUT_FILE.exists():
        print(f"[LỖI] Không tìm thấy: {INPUT_FILE}")
        return

    content = INPUT_FILE.read_text(encoding="utf-8")
    facts_by_tag = parse_facts(content)

    print(f"\n  Tìm thấy {len(facts_by_tag)} tags trong file nguồn")

    tags_to_process = TARGET_TAGS if TARGET_TAGS else list(facts_by_tag.keys())

    stats = {"created": 0, "skipped": 0, "empty": 0}

    for tag in tags_to_process:
        if tag in SKIP_TAGS:
            print(f"  ⏭️  SKIP     [{tag}]")
            stats["skipped"] += 1
            continue

        facts = facts_by_tag.get(tag, [])
        if not facts:
            print(f"  ⚠️  EMPTY    [{tag}] — không tìm thấy facts")
            stats["empty"] += 1
            continue

        title = tag_to_title(tag)
        facts_block = build_facts_block(facts)
        tags_yaml = tag_to_yaml_tags(tag)

        content_out = ATOM_TEMPLATE.format(
            tag=tag,
            title=title,
            tags_yaml=tags_yaml,
            today=TODAY,
            facts_block=facts_block,
        )

        output_path = OUTPUT_DIR / f"ATOMS_{tag}.md"

        print(f"\n  ✅ [{tag}] — {len(facts)} facts → {output_path.name}")
        for f in facts:
            print(f"     • {f[:80]}{'...' if len(f)>80 else ''}")

        if not DRY_RUN:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            if output_path.exists():
                print(f"     ⚠️  File đã tồn tại — bỏ qua")
                stats["skipped"] += 1
            else:
                output_path.write_text(content_out, encoding="utf-8")
                stats["created"] += 1
        else:
            stats["created"] += 1

    print("\n" + "=" * 60)
    print("  KẾT QUẢ")
    print("=" * 60)
    print(f"  ✅ {'Sẽ tạo' if DRY_RUN else 'Đã tạo'} : {stats['created']} files")
    print(f"  ⏭️  Bỏ qua : {stats['skipped']} files")
    print(f"  ⚠️  Trống  : {stats['empty']} tags")

    if DRY_RUN:
        print(f"\n  ⚡ DRY RUN — chưa ghi file.")
        print(f"  ⚡ Đổi DRY_RUN = False để ghi vào {OUTPUT_DIR}/")
    else:
        print(f"\n  ✅ Xong. Facts đã copy nguyên văn.")
        print(f"  → Bước tiếp: @scout điền 4F + wikilinks vào từng file")

if __name__ == "__main__":
    run()
