import os
import re

WIKI_DIR = os.path.join("3-resources", "wiki")

def convert_to_h5p():
    count = 0
    # Từ khóa dành riêng cho H5P (tránh nhầm với "khớp nối" của Tinkercad)
    pattern = re.compile(r'(nối hình ảnh|dạng ghép nối|hãy ghép|nối tên với|sắp xếp thứ tự|nối cột|nối ô|kéo thả)', re.IGNORECASE)
    
    for filename in os.listdir(WIKI_DIR):
        if filename.startswith("QUESTION_") or filename.startswith("NEEDS_REVIEW_QUESTION_"):
            filepath = os.path.join(WIKI_DIR, filename)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            if pattern.search(content):
                # Đổi prefix và ID bên trong file
                new_content = content.replace('prefix: "QUESTION"', 'prefix: "H5P"')
                new_content = new_content.replace('file_id: "QUESTION_', 'file_id: "H5P_')
                new_content = new_content.replace('# [QUESTION]', '# [H5P]')
                new_content = re.sub(r'file_id:\s*"NEEDS_REVIEW_QUESTION_', 'file_id: "NEEDS_REVIEW_H5P_', new_content)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                
                # Đổi tên file
                if filename.startswith("NEEDS_REVIEW_QUESTION_"):
                    new_filename = filename.replace("NEEDS_REVIEW_QUESTION_", "NEEDS_REVIEW_H5P_")
                else:
                    new_filename = filename.replace("QUESTION_", "H5P_")
                    
                new_filepath = os.path.join(WIKI_DIR, new_filename)
                
                os.replace(filepath, new_filepath)
                count += 1
                print(f"Renamed: {filename} -> {new_filename}")
                
    print(f"\nConverted {count} questions to H5P format.")

if __name__ == "__main__":
    convert_to_h5p()
