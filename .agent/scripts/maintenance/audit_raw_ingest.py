import os
import re
import pathlib
import sys

# Thêm path của md_auditor để reuse logic nếu cần, hoặc copy logic sang đây
# Ở đây tôi sẽ viết logic đơn giản tập trung vào link hỏng và encoding

class RawIngestAuditor:
    def __init__(self, raw_ingest_path, asset_path):
        self.raw_ingest_path = pathlib.Path(raw_ingest_path)
        self.asset_path = pathlib.Path(asset_path)
        self.img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
        self.ligature_pattern = re.compile(r'[a-zA-Z]\?[a-zA-Z]')

    def audit_file(self, file_path):
        results = {
            'file': file_path.name,
            'noise': 0,
            'broken_links': [],
            'status': 'PASSED'
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            results['status'] = 'ENCODING_ERROR'
            return results

        # Check noise
        results['noise'] = len(self.ligature_pattern.findall(content))
        
        # Check links
        links = self.img_pattern.findall(content)
        for link in links:
            # Resolve link relative to the file
            # In raw_ingest, links are usually ../raw_assets/...
            if link.startswith('../'):
                # Correct relative path
                img_path = (file_path.parent / link).resolve()
            else:
                # Absolute or local path (likely broken in raw_ingest context)
                img_path = (file_path.parent / link).resolve()
            
            if not img_path.exists():
                results['broken_links'].append(link)
        
        if results['noise'] > 10 or results['broken_links']:
            results['status'] = 'FAILED'
            
        return results

    def run_audit(self):
        all_results = []
        files = list(self.raw_ingest_path.glob('*.md'))
        for f in files:
            all_results.append(self.audit_file(f))
        return all_results

    def generate_table(self, results):
        lines = []
        lines.append("| File | Noise | Broken Links | Status |")
        lines.append("| :--- | :---: | :---: | :--- |")
        for r in results:
            links_str = len(r['broken_links']) if r['broken_links'] else 0
            status_icon = "✅" if r['status'] == 'PASSED' else "❌"
            lines.append(f"| `{r['file']}` | {r['noise']} | {links_str} | {status_icon} {r['status']} |")
        return "\n".join(lines)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Audit Raw Ingest Metadata and Links")
    parser.add_argument("--file", help="Path to a specific file to audit")
    args = parser.parse_args()

    # Force UTF-8 for Windows terminal
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding='utf-8')
        
    auditor = RawIngestAuditor(
        "3-resources/raw_ingest",
        "3-resources/raw_assets"
    )
    
    if args.file:
        file_path = pathlib.Path(args.file)
        if not file_path.exists():
            print(f"ERROR: File not found: {args.file}")
            sys.exit(1)
        results = [auditor.audit_file(file_path)]
    else:
        results = auditor.run_audit()
        
    print("\n### [POST-INGESTION AUDIT REPORT]")
    print(auditor.generate_table(results))
    
    # Exit with code 1 if any file failed (useful for automation)
    if any(r['status'] == 'FAILED' for r in results):
        sys.exit(1)

