import os
import subprocess
from pathlib import Path

# Cấu hình đường dẫn gốc
RAW_ROOT = Path(r"d:\NoteBookLLM_Br\brain\raw")
OUTPUT_DIR = RAW_ROOT

def convert(docx_path, output_name):
    output_path = OUTPUT_DIR / output_name
    # print(f"Converting: {docx_path.name} -> {output_name}") # Tạm tắt print để tránh lỗi Terminal
    try:
        subprocess.run(["npx", "mammoth", str(docx_path), str(output_path), "--output-format=markdown"], 
                       check=True, shell=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        pass

def main():
    # 1. Tìm Arduino 2
    arduino2_dir = next(RAW_ROOT.rglob("Arduino 2"), None)
    if arduino2_dir:
        for f in arduino2_dir.glob("*.docx"):
            convert(f, f"IOT_Arduino_M2_{f.stem.replace(' ', '_')}.md")

    # 2. Tìm Arduino 1+2 root
    arduino12_dir = next(RAW_ROOT.rglob("Arduino 1+2"), None)
    if arduino12_dir:
        for f in arduino12_dir.glob("*.docx"):
            convert(f, f"IOT_Arduino_M1_2_{f.stem.replace(' ', '_')}.md")
        
        # 3. Arduino 1 subfolder
        arduino1_dir = arduino12_dir / "Arduino 1"
        if arduino1_dir.exists():
            for i, f in enumerate(arduino1_dir.glob("*.docx"), 1):
                convert(f, f"IOT_Arduino_M1_De_{i}.md")

    # 4. AI Arduino
    ai_arduino_dir = next(RAW_ROOT.rglob("AI Arduino"), None)
    if ai_arduino_dir:
        for f in ai_arduino_dir.glob("*.docx"):
            # Phân biệt AI Arduino thuần và Tự động hóa
            prefix = "IOT_AI_Arduino_" if "AI Arduino" in f.name else "IOT_Tu_dong_hoa_AI_"
            # Tìm số đề
            import re
            match = re.search(r"(\d+)", f.name)
            num = match.group(1) if match else "X"
            convert(f, f"{prefix}De_{num}.md")

    # 5. YoloBit
    yolobit_dir = next(RAW_ROOT.rglob("YoloBit"), None)
    if yolobit_dir:
        for i, f in enumerate(yolobit_dir.glob("*.docx"), 1):
            convert(f, f"IOT_YoloBit_De_{i}.md")

    # 6. Halocode
    halocode_dir = next(RAW_ROOT.rglob("Halocode"), None)
    if halocode_dir:
        for i, f in enumerate(halocode_dir.glob("*.docx"), 1):
            convert(f, f"IOT_Halocode_De_{i}.md")

if __name__ == "__main__":
    main()
