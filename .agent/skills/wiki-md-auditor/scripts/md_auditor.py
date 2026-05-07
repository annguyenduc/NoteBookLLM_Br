import re
import os
import pathlib
import shutil
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class MarkdownAuditor:
    def __init__(self):
        # Improved ligature pattern: common OCR failures like "e?ciency"
        self.ligature_pattern = re.compile(r'[a-zA-Z]\?[a-zA-Z]')
        self.img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    def check_ligatures(self, text):
        matches = self.ligature_pattern.findall(text)
        return len(matches)

    def verify_links(self, md_path):
        md_path = pathlib.Path(md_path)
        base_dir = md_path.parent
        missing = []
        
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        links = self.img_pattern.findall(content)
        for link in links:
            img_path = (base_dir / link).resolve()
            if not img_path.exists():
                missing.append(link)
        return missing

    def standardize_assets(self, md_path, prefix, asset_vault, dry_run=True):
        md_path = pathlib.Path(md_path)
        asset_vault = pathlib.Path(asset_vault)
        base_dir = md_path.parent
        
        if not asset_vault.exists() and not dry_run:
            asset_vault.mkdir(parents=True, exist_ok=True)

        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        links = self.img_pattern.findall(content)
        new_content = content
        
        for i, old_link in enumerate(links):
            ext = pathlib.Path(old_link).suffix
            new_name = f"{prefix}_fig_{i:02d}{ext}"
            new_path_str = f"../raw_assets/{new_name}"
            
            # Source image path
            src_img = (base_dir / old_link).resolve()
            dest_img = asset_vault / new_name
            
            # Replace link in content
            new_content = new_content.replace(old_link, new_path_str)
            
            if not dry_run:
                if src_img.exists():
                    logging.info(f"Promoting asset: {src_img.name} -> {new_name}")
                    shutil.copy2(src_img, dest_img)
                else:
                    logging.warning(f"Asset not found: {src_img}")

        # Update MD content with new links
        if not dry_run:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            logging.info(f"Markdown links updated for {md_path.name}")
        
        return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Audit and Standardize Markdown Knowledge")
    parser.add_argument("path", help="Path to Markdown file")
    parser.add_argument("--fix", action="store_true", help="Execute standardization and move assets")
    parser.add_argument("--prefix", help="Prefix for assets (defaults to filename)")
    parser.add_argument("--vault", default="d:/NoteBookLLM_Br/3-resources/raw_assets", help="Path to asset vault")
    
    args = parser.parse_args()
    auditor = MarkdownAuditor()
    
    if not os.path.exists(args.path):
        logging.error(f"File not found: {args.path}")
        sys.exit(1)
        
    with open(args.path, "r", encoding="utf-8") as f:
        text = f.read()
    
    noises = auditor.check_ligatures(text)
    missing = auditor.verify_links(args.path)
    
    print(f"\n--- Audit Report: {os.path.basename(args.path)} ---")
    print(f"Noise (Ligatures): {noises}")
    print(f"Broken Links: {len(missing)}")
    
    if args.fix:
        if noises > 10:
            logging.error("Too much noise. Fix manually before promotion.")
        elif missing:
            logging.error("Missing assets. Fix links before promotion.")
        else:
            prefix = args.prefix if args.prefix else pathlib.Path(args.path).stem
            auditor.standardize_assets(args.path, prefix, args.vault, dry_run=False)
            logging.info("Standardization complete.")
