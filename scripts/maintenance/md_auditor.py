import re
import os
import pathlib
import shutil
import logging
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class MarkdownAuditor:
    def __init__(self):
        _secret = os.environ.get("KIRO_AUDIT_SECRET")
        if not _secret:
            self.hmac_key = None
        else:
            self.hmac_key = _secret.encode("utf-8")
        
        # Improved ligature pattern: common OCR failures like "e?ciency"
        self.ligature_pattern = re.compile(r'[a-zA-Z]\?[a-zA-Z]')
        self.img_pattern = re.compile(r'!\[\[(.*?)\]\]|!\[.*?\]\((.*?)\)')

    def check_ligatures(self, text):
        matches = self.ligature_pattern.findall(text)
        return len(matches)

    def verify_links(self, md_path, vault_path=None):
        md_path = pathlib.Path(md_path)
        base_dir = md_path.parent
        missing = []
        
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        links = self.img_pattern.findall(content)
        for wikilink, mdlink in links:
            link = wikilink if wikilink else mdlink
            img_path = (base_dir / link).resolve()
            
            # Special case for HD-converted files: if link points to vault but file is still in local images/
            # Special case for HD-converted files: if link points to vault but file is still in local images/
            if not img_path.exists():
                local_fallback = base_dir / "images" / pathlib.Path(link).name
                if not local_fallback.exists():
                    local_fallback = base_dir / "assets" / pathlib.Path(link).name
                
                if local_fallback.exists():
                    logging.info(f"Asset found in local fallback: {local_fallback.name}")
                    continue
                
                # Check absolute vault path if provided
                if vault_path:
                    vault_img = pathlib.Path(vault_path) / pathlib.Path(link).name
                    if vault_img.exists():
                        logging.info(f"Asset already in vault: {vault_img.name}")
                        continue
                
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
        
        for i, (wikilink, mdlink) in enumerate(links):
            old_link = wikilink if wikilink else mdlink
            ext = pathlib.Path(old_link).suffix
            new_name = f"{prefix}_fig_{i:02d}{ext}"
            
            # Using ![[ ]] for Obsidian consistency
            new_path_str = f"![[{new_name}]]"
            
            # Source image path
            src_img = (base_dir / old_link).resolve()
            if not src_img.exists():
                src_img = (base_dir / "assets" / old_link).resolve()
            if not src_img.exists():
                src_img = (base_dir / "images" / old_link).resolve()
            dest_img = asset_vault / new_name
            
            # Replace link in content (be careful with the full match)
            if wikilink:
                new_content = new_content.replace(f"![[{wikilink}]]", new_path_str)
            else:
                new_content = re.sub(
                    rf'!\[.*?\]\({re.escape(old_link)}\)',
                    new_path_str,
                    new_content,
                    count=1
                )
            
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

    def write_audit_stamp(self, md_path, noises, missing_count):
        from datetime import date
        import importlib.util
        today = date.today().strftime("%Y-%m-%d")
        
        # Calculate score: 1.0 base, -0.05 per noise, -0.1 per missing link
        score = 1.0
        if noises > 0:
            score -= min(0.5, noises * 0.05)
        if missing_count > 0:
            score -= min(0.5, missing_count * 0.1)
        score = round(max(0.0, score), 2)
        score_str = f"{score:.2f}"
        
        import hmac, hashlib
        if self.hmac_key:
            msg = f"{pathlib.Path(md_path).stem}-{score_str}-{today}-v1.0".encode("utf-8")
            signature = hmac.new(self.hmac_key, msg, hashlib.sha256).hexdigest()
        else:
            signature = "UNSIGNED"
            logging.warning("KIRO_AUDIT_SECRET not set. Audit stamp will be UNSIGNED.")
        
        status = "PASSED" if score >= 0.9 else "FAILED"
        
        # Step A: Detect Source PDF
        verify_result = "SKIPPED"
        verify_gaps = []
        
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        pdf_match = re.search(r'^Source PDF:\s*(.*)$', content, re.MULTILINE)
        if pdf_match:
            pdf_filename = pdf_match.group(1).strip()
            md_path_obj = pathlib.Path(md_path)
            
            # Search locations
            root_dir = pathlib.Path(__file__).resolve().parent.parent.parent
            search_paths = [
                md_path_obj.parent,
                root_dir / "00_Inbox",
                root_dir / "3-resources" / "raw_sources"
            ]
            
            pdf_path = None
            for sp in search_paths:
                candidate = (sp / pdf_filename).resolve()
                if candidate.exists():
                    pdf_path = str(candidate)
                    break
            
            # Step B: Call verify_convert
            if pdf_path:
                try:
                    v_script = root_dir / ".agent" / "skills" / "wiki-hd-convert" / "scripts" / "verify_convert.py"
                    if v_script.exists():
                        spec = importlib.util.spec_from_file_location("verify_convert", v_script)
                        vc = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(vc)
                        v_res = vc.verify(pdf_path, str(md_path))
                        verify_result = v_res.get("result", "ERROR")
                        verify_gaps = v_res.get("gaps", [])
                    else:
                        logging.error(f"Verification script missing: {v_script}")
                        verify_result = "ERROR"
                except Exception as e:
                    logging.error(f"Verification error: {e}")
                    verify_result = "ERROR"
            else:
                logging.error(f"Source PDF not found for verification: {pdf_filename}")
                verify_result = "ERROR"

        if verify_result in {"FAIL", "ERROR"}:
            status = "FAILED"

        stamp_lines = [
            "audit_stamp: true",
            "audit:",
            f"  score: {score_str}",
            f"  date: \"{today}\"",
            f"  status: \"{status}\"",
            "  auditor: \"v1.0\"",
            f"  verify_result: \"{verify_result}\"",
            f"  verify_gaps: {verify_gaps}",
            f"  signature: \"{signature}\""
        ]
        stamp_text = "\n".join(stamp_lines)

        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Handle frontmatter or header (search for the first ---)
        # Handle frontmatter (search for the block between --- and ---)
        frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL | re.MULTILINE)
        
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            body = content[frontmatter_match.end():]
            
            # Remove existing audit block from frontmatter
            new_frontmatter = re.sub(r'audit:.*?(?=\n\S|\Z)', '', frontmatter, flags=re.DOTALL).strip()
            
            # Append new stamp to frontmatter
            new_frontmatter = new_frontmatter + "\n" + stamp_text
            new_content = "---\n" + new_frontmatter.strip() + "\n---\n" + body
        else:
            # No frontmatter found, prepend as a new frontmatter block
            new_content = "---\n" + stamp_text + "\n---\n\n" + content

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        return score, status, verify_result

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
    missing = auditor.verify_links(args.path, vault_path=args.vault)
    
    print(f"\n--- Audit Report: {os.path.basename(args.path)} ---")
    print(f"Noise (Ligatures): {noises}")
    print(f"Broken Links: {len(missing)}")
    
    if args.fix:
        if noises > 10:
            logging.error("Too much noise. Fix manually before promotion.")
            sys.exit(1)
        elif missing:
            logging.error("Missing assets. Fix links before promotion.")
            sys.exit(1)
        else:
            prefix = args.prefix if args.prefix else pathlib.Path(args.path).stem
            auditor.standardize_assets(args.path, prefix, args.vault, dry_run=False)
            score, status, verify_result = auditor.write_audit_stamp(args.path, noises, len(missing))
            logging.info(f"Standardization complete. Audit {status} (Score: {score}, Verify: {verify_result})")
            if status != "PASSED":
                sys.exit(1)
