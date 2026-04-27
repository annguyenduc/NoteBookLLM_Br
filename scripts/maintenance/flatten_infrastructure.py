import os
import shutil
import glob

# Constants
BASE_DIR = r"d:\NoteBookLLM_Br"
ASSETS_SRC = os.path.join(BASE_DIR, "3-resources", "raw", "lms_multi_media_dump", "assets")
ASSETS_DEST = os.path.join(BASE_DIR, "3-resources", "assets")
RAW_SRC = os.path.join(BASE_DIR, "3-resources", "raw", "lms_tests_raw")
RAW_DEST = os.path.join(BASE_DIR, "3-resources", "raw")
ARCHIVE_DEST = os.path.join(BASE_DIR, "3-resources", "archive")

def flatten_assets():
    print(f"Flattening assets from {ASSETS_SRC} to {ASSETS_DEST}...")
    if not os.path.exists(ASSETS_SRC):
        print("Source assets folder not found.")
        return
    
    files = glob.glob(os.path.join(ASSETS_SRC, "*"))
    for f in files:
        filename = os.path.basename(f)
        # Prefix using Rule 8: Machine-readability + Snake_Case
        new_name = "LMS_IMG_" + filename.replace(" ", "_")
        dest_path = os.path.join(ASSETS_DEST, new_name)
        
        if not os.path.exists(dest_path):
            shutil.move(f, dest_path)
            print(f"Moved: {filename} -> {new_name}")
        else:
            print(f"Skipped (Exists): {new_name}")

def flatten_raw_sources():
    print(f"Flattening raw sources from {RAW_SRC} to {RAW_DEST}...")
    if not os.path.exists(RAW_SRC):
        print("Source raw folder not found.")
        return
    
    files = glob.glob(os.path.join(RAW_SRC, "*"))
    for f in files:
        filename = os.path.basename(f)
        # Prefix for Raw
        new_name = "LMS_RAW_" + filename.replace(" ", "_")
        dest_path = os.path.join(RAW_DEST, new_name)
        
        if not os.path.exists(dest_path):
            shutil.move(f, dest_path)
            print(f"Moved: {filename} -> {new_name}")
        else:
            print(f"Skipped (Exists): {new_name}")

def cleanup():
    print("Performing cleanup...")
    # Move original (empty) folders to archive instead of deleting
    for folder in [RAW_SRC, os.path.dirname(ASSETS_SRC)]:
        if os.path.exists(folder):
            folder_name = os.path.basename(folder)
            dest = os.path.join(ARCHIVE_DEST, folder_name)
            if not os.path.exists(dest):
                shutil.move(folder, dest)
                print(f"Archived: {folder_name}")
            else:
                print(f"Folder {folder_name} already in archive.")

if __name__ == "__main__":
    flatten_assets()
    flatten_raw_sources()
    cleanup()
