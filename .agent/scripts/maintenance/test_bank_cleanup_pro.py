import os
import re
import base64
import hashlib

# Paths
TEST_BANK_DIR = r"d:/NoteBookLLM_Br/3-resources/test-bank"
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

def standardize_name(raw_name, content=""):
    raw_name_lower = raw_name.lower()
    content_lower = content.lower()
    
    for target, keywords in TAXONOMY.items():
        for kw in keywords:
            if kw in raw_name_lower or kw in content_lower:
                return target
    return "UNKNOWN"

def extract_base64_images(content, file_prefix):
    """Find base64 images, save them, and replace with links."""
    # Pattern for data:image/png;base64,....
    pattern = r'data:image/(?P<ext>png|jpeg|jpg|gif);base64,(?P<data>[A-Za-z0-9+/=]+)'
    
    def replacer(match):
        ext = match.group('ext')
        data = match.group('data')
        try:
            img_data = base64.b64decode(data)
            # Use hash for filename to avoid duplicates
            h = hashlib.md5(img_data).hexdigest()[:10]
            filename = f"ASSET_{file_prefix}_B64_{h}.{ext}"
            filepath = os.path.join(ASSETS_DIR, filename)
            
            if not os.path.exists(filepath):
                with open(filepath, 'wb') as f:
                    f.write(img_data)
            return f"../assets/{filename}"
        except:
            return match.group(0) # Keep original if failed

    new_content = re.sub(pattern, replacer, content)
    return new_content

def cleanup():
    print("Starting Deep Cleanup v2...")
    
    # 1. Map and Rename Assets
    asset_map = {}
    all_assets = os.listdir(ASSETS_DIR)
    for asset in all_assets:
        if not asset.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')): continue
        
        prefix = standardize_name(asset)
        exam_match = re.search(r'[Đđ]ề_?(\d+)', asset, re.I) or re.search(r'De_?(\d+)', asset, re.I)
        exam_str = f"De{exam_match.group(1)}" if exam_match else ""
        rid_match = re.search(r'(rId\d+)', asset, re.I)
        rid_str = rid_match.group(1) if rid_match else "img"
        
        ext = os.path.splitext(asset)[1]
        new_name = f"ASSET_{prefix}_{exam_str}_{rid_str}{ext}".replace("__", "_")
        
        if asset != new_name:
            old_path = os.path.join(ASSETS_DIR, asset)
            new_path = os.path.join(ASSETS_DIR, new_name)
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
            asset_map[asset] = new_name
        else:
            asset_map[asset] = asset

    # 2. Process Files
    all_files = os.listdir(TEST_BANK_DIR)
    processed_content = {} 
    files_to_delete = []
    
    for filename in all_files:
        if not filename.endswith(".md"): continue
        path = os.path.join(TEST_BANK_DIR, filename)
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue
            
        target_prefix = standardize_name(filename, content)
        
        # Extract ID (De_Q)
        id_match = re.search(r'(?i)De_?(\d+)_?Q_?(\d+)', filename) or re.search(r'(?i)De_?(\d+)_?Q_?(\d+)', content)
        if id_match:
            suffix = f"De{id_match.group(1)}_Q{id_match.group(2)}"
        else:
            suffix = filename.replace(".md", "").replace(target_prefix + "_", "").replace("MCQ_", "")
            suffix = re.sub(r'[^a-zA-Z0-9_]', '', suffix)

        new_filename = f"{target_prefix}_MCQ_{suffix}.md"
        
        # Extract Base64 if any
        if "data:image" in content:
            content = extract_base64_images(content, f"{target_prefix}_{suffix}")
            
        # Standardize links
        def img_replacer(match):
            alt = match.group(1)
            old_img = os.path.basename(match.group(2))
            if old_img in asset_map:
                return f"![{alt}](../assets/{asset_map[old_img]})"
            # Try to catch partial matches or already renamed but lowercase
            for old, new in asset_map.items():
                if old.lower() == old_img.lower():
                    return f"![{alt}](../assets/{new})"
            return match.group(0)

        content = re.sub(r'!\[(.*?)\]\(\.\./assets/(.*?)\)', img_replacer, content)
        
        # Update IDs
        new_id = new_filename.replace(".md", "")
        content = re.sub(r'file_id: ".*?"', f'file_id: "{new_id}"', content)
        
        # Resolve duplicates (prefer non-bloated)
        is_bloated = "data:image" in content
        if new_filename not in processed_content or (not is_bloated and "data:image" in processed_content[new_filename]):
            processed_content[new_filename] = content
            
        if filename != new_filename:
            files_to_delete.append(path)

    # 3. Finalize
    for fname, body in processed_content.items():
        with open(os.path.join(TEST_BANK_DIR, fname), 'w', encoding='utf-8') as f:
            f.write(body)
            
    for p in files_to_delete:
        if os.path.exists(p): os.remove(p)

    print("Cleanup v2 complete.")

if __name__ == "__main__":
    cleanup()
