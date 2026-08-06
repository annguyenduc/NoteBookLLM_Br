import os
import re
import pathlib

class LinkHealer:
    def __init__(self, raw_ingest_path, asset_path):
        self.raw_ingest_path = pathlib.Path(raw_ingest_path)
        self.asset_path = pathlib.Path(asset_path)
        self.img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    def find_asset(self, filename):
        """Tìm file ảnh trong toàn bộ asset_path (bao gồm cả subdirs)"""
        for root, dirs, files in os.walk(self.asset_path):
            if filename in files:
                # Trả về đường dẫn tương đối từ raw_ingest đến file ảnh
                # raw_ingest: 3-resources/raw_ingest
                # root: 3-resources/raw_assets/images/...
                rel_path = os.path.relpath(os.path.join(root, filename), self.raw_ingest_path)
                return rel_path.replace('\\', '/')
        return None

    def heal_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        links = self.img_pattern.findall(content)
        new_content = content
        healed_count = 0
        
        for old_link in links:
            # Kiểm tra xem link cũ có tồn tại không
            img_path = (file_path.parent / old_link).resolve()
            if not img_path.exists():
                # Thử tìm lại bằng tên file
                filename = pathlib.Path(old_link).name
                new_link = self.find_asset(filename)
                
                if new_link:
                    print(f"  Healing: {old_link} -> {new_link}")
                    new_content = new_content.replace(old_link, new_link)
                    healed_count += 1
                else:
                    print(f"  WARNING: Could not find asset for {old_link}")

        if healed_count > 0:
            import stat
            # Unlock file if it is read-only
            os.chmod(file_path, stat.S_IWRITE)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Healed {healed_count} links in {file_path.name}")
        else:
            print(f"ℹ️ No links to heal in {file_path.name}")

    def run(self):
        # Chỉ tập trung vào các file THINK bị lỗi
        think_files = [f for f in self.raw_ingest_path.glob('THINK_*.md')]
        for f in think_files:
            print(f"Processing {f.name}...")
            self.heal_file(f)

if __name__ == "__main__":
    healer = LinkHealer(
        "3-resources/raw_ingest",
        "3-resources/raw_assets"
    )
    healer.run()
