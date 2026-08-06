import os
import re

ASSETS_DIR = r"d:/NoteBookLLM_Br/3-resources/assets"

TAXONOMY = {
    "KHMT_AI_THCS": ["ai thcs", "ai_thcs", "khoa học máy tính ai thcs"],
    "KHMT_AI_Tieu_hoc": ["ai tiểu học", "ai_tiểu_học", "ai tieu hoc", "ai_tieu_hoc"],
    "KHMT_Python": ["python"],
    "KHMT_Scratch_Jr": ["scratch jr", "scratch_jr"],
    "KHMT_Scratch": ["scratch"],
    "KHMT_Tynker": ["tynker"],
    "ROBOT_mBot": ["mbot"],
    "ROBOT_xBot": ["xbot"],
    "ROBOT_Rover": ["rover"],
    "ROBOT_Codey": ["codey"],
    "ROBOT_GBot": ["gbot"],
    "ROBOT_Unplugged": ["unplugged"],
    "DESIGN_3D_Tinkercad": ["tinkercad", "3d tinkercad"],
    "DESIGN_Canva": ["canva"],
    "DESIGN_Wordpress": ["wordpress"],
    "DESIGN_Maker_Empire": ["maker empire", "maker_empire"],
    "IOT_AI_Arduino": ["ai arduino", "ai_arduino"],
    "IOT_Arduino": ["arduino"],
    "IOT_Halocode": ["halocode"],
    "IOT_YoloBit": ["yolobit"],
    "PROMPT_K10_Toan": ["k10 toán", "k10_toan"],
    "PROMPT_K10_Van": ["k10 văn", "k10_van"],
    "PROMPT_K10_Anh": ["k10 anh", "k10_anh"]
}

def get_target_prefix(name):
    name_lower = name.lower()
    for target, keywords in TAXONOMY.items():
        for kw in keywords:
            if kw in name_lower:
                return target
    return "UNKNOWN"

def repair():
    print("Repairing Asset Names...")
    all_assets = os.listdir(ASSETS_DIR)
    count = 0
    
    for asset in all_assets:
        if not asset.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')): continue
        
        # Extract Rid
        rid_match = re.search(r'(rId\d+)', asset, re.I)
        rid_str = rid_match.group(1) if rid_match else "img"
        
        # Extract Exam
        exam_match = re.search(r'[Đđ]?[ềe]_?(\d+)', asset, re.I) or re.search(r'De_?(\d+)', asset, re.I)
        exam_str = f"De{exam_match.group(1)}" if exam_match else ""
        
        prefix = get_target_prefix(asset)
        ext = os.path.splitext(asset)[1].lower()
        
        # If the name is already an ASSET_ name, keep it but maybe fix the prefix if it was UNKNOWN
        if asset.startswith("ASSET_"):
            if "_UNKNOWN_" in asset:
                # Try to salvage from the rest of the name
                new_prefix = get_target_prefix(asset.replace("ASSET_UNKNOWN_", ""))
                if new_prefix != "UNKNOWN":
                    new_name = asset.replace("UNKNOWN", new_prefix)
                else:
                    continue # Keep as UNKNOWN for now
            else:
                continue # Already fine
        else:
            new_name = f"ASSET_{prefix}_{exam_str}_{rid_str}{ext}".replace("__", "_")

        if asset != new_name:
            old_path = os.path.join(ASSETS_DIR, asset)
            new_path = os.path.join(ASSETS_DIR, new_name)
            
            # Handle collision
            if os.path.exists(new_path):
                # If collision, we append a small hash or just delete the old one if it's the same
                # For safety, let's just append a counter
                base, ext_part = os.path.splitext(new_name)
                i = 1
                while os.path.exists(os.path.join(ASSETS_DIR, f"{base}_{i}{ext_part}")):
                    i += 1
                new_path = os.path.join(ASSETS_DIR, f"{base}_{i}{ext_part}")
            
            try:
                os.rename(old_path, new_path)
                count += 1
            except Exception as e:
                print(f"Error renaming {asset}: {e}")

    print(f"Repaired {count} assets.")

if __name__ == "__main__":
    repair()
