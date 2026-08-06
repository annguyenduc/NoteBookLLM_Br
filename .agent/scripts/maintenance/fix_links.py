import os
import re

TEST_BANK_DIR = r"d:/NoteBookLLM_Br/3-resources/test-bank"
ASSETS_DIR = r"d:/NoteBookLLM_Br/3-resources/assets"

def fix_links():
    print("Fixing broken links in test-bank...")
    
    # Pre-scan assets to build a map of (exam, rid) -> filename
    # Also handle rid alone as fallback
    asset_map = {}
    rid_only_map = {}
    
    all_assets = os.listdir(ASSETS_DIR)
    for asset in all_assets:
        rid_match = re.search(r'rId(\d+)', asset, re.I)
        exam_match = re.search(r'De(\d+)', asset, re.I)
        
        if rid_match:
            rid = rid_match.group(1).lower()
            exam = exam_match.group(1).lower() if exam_match else "none"
            
            # Map by (exam, rid)
            # Prioritize non-UNKNOWN
            if (exam, rid) not in asset_map or "UNKNOWN" in asset_map[(exam, rid)]:
                asset_map[(exam, rid)] = asset
            
            # Map by rid (only if not already there, or prioritize non-UNKNOWN)
            if rid not in rid_only_map or "UNKNOWN" in rid_only_map[rid]:
                rid_only_map[rid] = asset

    count = 0
    files = os.listdir(TEST_BANK_DIR)
    print(f"Total files in dir: {len(files)}")
    for file in files:
        if not file.endswith(".md"): continue
        
        path = os.path.join(TEST_BANK_DIR, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # Match ![Image](../assets/...)
        img_pattern = r'!\[Image\]\(.*?assets/([^)]+)\)'
        
        def replacer(match):
            original_link = match.group(1)
            
            # If the link is UNKNOWN, we WANT to replace it even if it exists
            # Otherwise, if it exists and NOT unknown, keep it
            if "UNKNOWN" not in original_link and os.path.exists(os.path.join(ASSETS_DIR, original_link)):
                return match.group(0)
            
            # Try to extract rid and exam from the broken/unknown link
            rid_match = re.search(r'rId(\d+)', original_link, re.I)
            exam_match = re.search(r'De(\d+)', original_link, re.I)
            
            if rid_match:
                rid = rid_match.group(1).lower()
                exam = exam_match.group(1).lower() if exam_match else "none"
                
                # Try specific match
                if (exam, rid) in asset_map and "UNKNOWN" not in asset_map[(exam, rid)]:
                    return f"![Image](../assets/{asset_map[(exam, rid)]})"
                
                # Try rid only match
                if rid in rid_only_map and "UNKNOWN" not in rid_only_map[rid]:
                    return f"![Image](../assets/{rid_only_map[rid]})"
            
            return match.group(0) # Give up, keep original

        new_content = re.sub(img_pattern, replacer, content, flags=re.IGNORECASE)
        
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            
    print(f"Fixed links in {count} files.")

if __name__ == "__main__":
    fix_links()
