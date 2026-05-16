import argparse
import hashlib
import hmac
import importlib.util
import logging
import os
import pathlib
import re
import shutil
import sys
from datetime import date

import pypdf


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

VERIFY_SCOPES = ("full-source", "chunk", "package")


def safe_print(message: str):
    try:
        print(message)
    except UnicodeEncodeError:
        clean = (
            message.replace("✅", "[PASS]")
            .replace("⚠️", "[WARN]")
            .replace("❌", "[FAIL]")
            .replace("→", "->")
            .replace("ℹ️", "[INFO]")
        )
        print(clean)


class MarkdownAuditor:
    def __init__(self):
        secret = os.environ.get("KIRO_AUDIT_SECRET")
        self.hmac_key = secret.encode("utf-8") if secret else None
        self.ligature_pattern = re.compile(r"[a-zA-Z]\?[a-zA-Z]")
        self.img_pattern = re.compile(r"!\[\[(.*?)\]\]|!\[.*?\]\((.*?)\)")
        self.root_dir = pathlib.Path(__file__).resolve().parent.parent.parent

    def check_ligatures(self, text):
        return len(self.ligature_pattern.findall(text))

    def verify_links(self, md_path, vault_path=None):
        md_path = pathlib.Path(md_path)
        base_dir = md_path.parent
        missing = []

        with open(md_path, "r", encoding="utf-8") as handle:
            content = handle.read()

        links = self.img_pattern.findall(content)
        for wikilink, mdlink in links:
            link = wikilink if wikilink else mdlink
            img_path = (base_dir / link).resolve()
            if not img_path.exists():
                local_fallback = base_dir / "images" / pathlib.Path(link).name
                if not local_fallback.exists():
                    local_fallback = base_dir / "assets" / pathlib.Path(link).name

                if local_fallback.exists():
                    logging.info(f"Asset found in local fallback: {local_fallback.name}")
                    continue

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

        with open(md_path, "r", encoding="utf-8") as handle:
            content = handle.read()

        links = self.img_pattern.findall(content)
        new_content = content

        for index, (wikilink, mdlink) in enumerate(links):
            old_link = wikilink if wikilink else mdlink
            ext = pathlib.Path(old_link).suffix
            new_name = f"{prefix}_fig_{index:02d}{ext}"
            new_path_str = f"![[{new_name}]]"

            src_img = (base_dir / old_link).resolve()
            if not src_img.exists():
                src_img = (base_dir / "assets" / old_link).resolve()
            if not src_img.exists():
                src_img = (base_dir / "images" / old_link).resolve()
            dest_img = asset_vault / new_name

            if wikilink:
                new_content = new_content.replace(f"![[{wikilink}]]", new_path_str)
            else:
                new_content = re.sub(
                    rf"!\[.*?\]\({re.escape(old_link)}\)",
                    new_path_str,
                    new_content,
                    count=1,
                )

            if not dry_run:
                if src_img.exists():
                    logging.info(f"Promoting asset: {src_img.name} -> {new_name}")
                    shutil.copy2(src_img, dest_img)
                else:
                    logging.warning(f"Asset not found: {src_img}")

        if not dry_run:
            with open(md_path, "w", encoding="utf-8") as handle:
                handle.write(new_content)
            logging.info(f"Markdown links updated for {md_path.name}")

        return True

    def strip_frontmatter(self, text: str) -> str:
        match = re.match(r"^---\s*\n.*?\n---\s*\n?", text, re.DOTALL)
        if match:
            return text[match.end() :]
        return text

    def get_source_pdf_path(self, content: str, md_path: pathlib.Path):
        pdf_match = re.search(r"^Source PDF:\s*(.*)$", content, re.MULTILINE)
        if not pdf_match:
            return None

        pdf_filename = pdf_match.group(1).strip()
        search_paths = [
            md_path.parent,
            self.root_dir / "00_Inbox",
            self.root_dir / "3-resources" / "raw_sources",
        ]
        for search_path in search_paths:
            candidate = (search_path / pdf_filename).resolve()
            if candidate.exists():
                return candidate
        logging.error(f"Source PDF not found for verification: {pdf_filename}")
        return None

    def resolve_chunk_range(self, md_path: pathlib.Path, content: str):
        metadata_match = re.search(r"Chunk Range:\s*Pages\s+(\d+)\s+to\s+(\d+)", content)
        if metadata_match:
            return int(metadata_match.group(1)), int(metadata_match.group(2)), "frontmatter"

        filename_match = re.search(r"_P(\d+)-(\d+)\.md$", md_path.name)
        if filename_match:
            return int(filename_match.group(1)), int(filename_match.group(2)), "filename"

        return None, None, None

    def load_manifest_pages(self, manifest_path: pathlib.Path, chunk_name: str):
        if not manifest_path or not manifest_path.exists():
            return None

        pattern = rf"\|\s*\d+\s*\|\s*(\d+)-(\d+)\s*\|\s*`{re.escape(chunk_name)}`\s*\|"
        manifest_text = manifest_path.read_text(encoding="utf-8", errors="replace")
        match = re.search(pattern, manifest_text)
        if not match:
            return None
        return int(match.group(1)), int(match.group(2))

    def read_verify_convert_module(self):
        verify_script = self.root_dir / ".agent" / "skills" / "wiki-hd-convert" / "scripts" / "verify_convert.py"
        if not verify_script.exists():
            raise FileNotFoundError(f"Verification script missing: {verify_script}")
        spec = importlib.util.spec_from_file_location("verify_convert", verify_script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def verify_full_source(self, pdf_path: pathlib.Path, md_path: pathlib.Path):
        try:
            verify_module = self.read_verify_convert_module()
            return verify_module.verify(str(pdf_path), str(md_path))
        except Exception as exc:
            logging.error(f"Verification error: {exc}")
            return {"result": "ERROR", "gaps": [], "verify_scope": "full-source"}

    def verify_chunk_scope(self, pdf_path: pathlib.Path, md_path: pathlib.Path, content: str, manifest_path=None):
        start_page, end_page, range_source = self.resolve_chunk_range(md_path, content)
        if start_page is None and manifest_path:
            manifest_pages = self.load_manifest_pages(pathlib.Path(manifest_path), md_path.name)
            if manifest_pages:
                start_page, end_page = manifest_pages
                range_source = "manifest"

        if start_page is None:
            logging.error("Chunk scope requested but no page range could be resolved.")
            return {"result": "ERROR", "gaps": ["missing_chunk_range"], "verify_scope": "chunk"}

        manifest_pages = None
        if manifest_path:
            manifest_pages = self.load_manifest_pages(pathlib.Path(manifest_path), md_path.name)
            if manifest_pages and manifest_pages != (start_page, end_page):
                logging.error(
                    "Chunk range mismatch between chunk metadata and manifest: "
                    f"{start_page}-{end_page} vs {manifest_pages[0]}-{manifest_pages[1]}"
                )
                return {"result": "ERROR", "gaps": ["manifest_range_mismatch"], "verify_scope": "chunk"}

        reader = pypdf.PdfReader(str(pdf_path))
        pdf_pages = len(reader.pages)
        if start_page < 1 or end_page > pdf_pages or start_page > end_page:
            logging.error(f"Chunk page range out of bounds: {start_page}-{end_page} for PDF with {pdf_pages} pages")
            return {"result": "ERROR", "gaps": ["page_range_out_of_bounds"], "verify_scope": "chunk"}

        page_slice = reader.pages[start_page - 1 : end_page]
        pdf_chars = 0
        pdf_images = 0
        for page in page_slice:
            pdf_chars += len(page.extract_text() or "")
            pdf_images += len(page.images)

        stripped_md = self.strip_frontmatter(content)
        md_chars = len(stripped_md)
        md_images = len(re.findall(r"!\[\[(.*?)\]\]|!\[.*?\]\(.*?\)", content))
        expected_pages = end_page - start_page + 1

        section_markers = len(re.findall(r"^## |<!-- PAGE_START_", content, re.MULTILINE))

        if pdf_chars == 0:
            status_ret = "PASS"
            ret_label = "SCANNED"
            retention = None
        else:
            retention = md_chars / pdf_chars * 100
            status_ret = "PASS" if retention >= 70 else ("WARN" if retention >= 50 else "FAIL")
            ret_label = f"{retention:.0f}%"

        if pdf_images == 0:
            status_img = "PASS"
        elif md_images >= pdf_images * 0.8:
            status_img = "PASS"
        elif md_images >= pdf_images * 0.5:
            status_img = "WARN"
        else:
            status_img = "FAIL"

        coverage, status_cov, coverage_reason = self.evaluate_chunk_coverage(
            expected_pages=expected_pages,
            section_markers=section_markers,
            md_chars=md_chars,
            retention=retention,
            status_ret=status_ret,
            md_images=md_images,
        )

        gaps = []
        if status_cov == "FAIL":
            gaps.append(f"page_coverage_{start_page}_{end_page}")
        if status_ret == "FAIL":
            gaps.append(f"text_retention_{start_page}_{end_page}")
        if status_img == "FAIL":
            gaps.append(f"image_coverage_{start_page}_{end_page}")

        if any(status == "FAIL" for status in (status_cov, status_ret, status_img)):
            result = "FAIL"
        elif all(status == "PASS" for status in (status_cov, status_ret, status_img)):
            result = "PASS"
        else:
            result = "WARN"

        safe_print(f"\n  [VERIFY: chunk] {pdf_path.name}")
        safe_print(f"    Scope:  pages {start_page}-{end_page} ({range_source})")
        safe_print(
            f"    Pages:  {expected_pages} expected -> {section_markers} section markers "
            f"({coverage:.1f}%) [{status_cov}]"
        )
        safe_print(
            f"    Text:   {pdf_chars:,} chars -> {md_chars:,} chars MD  "
            f"{'[PASS]' if status_ret == 'PASS' else '[WARN]' if status_ret == 'WARN' else '[FAIL]'} ({ret_label})"
        )
        safe_print(
            f"    Images: {pdf_images} PDF -> {md_images} MD  "
            f"{'[PASS]' if status_img == 'PASS' else '[WARN]' if status_img == 'WARN' else '[FAIL]'}"
        )
        safe_print(f"\n  RESULT: {result}")
        if result != "PASS":
            reasons = []
            if status_cov == "FAIL":
                reasons.append(coverage_reason or "Chunk evidence coverage below threshold")
            if status_ret == "FAIL":
                reasons.append("Chunk text retention below threshold")
            if status_img == "FAIL":
                reasons.append("Chunk image coverage below threshold")
            if reasons:
                safe_print(f"  Reason: {'; '.join(reasons)}")

        return {
            "result": result,
            "gaps": gaps,
            "verify_scope": "chunk",
            "range": [start_page, end_page],
            "range_source": range_source,
            "manifest_match": list(manifest_pages) if manifest_pages else None,
            "coverage_reason": coverage_reason,
        }

    def evaluate_chunk_coverage(
        self,
        expected_pages: int,
        section_markers: int,
        md_chars: int,
        retention: float | None,
        status_ret: str,
        md_images: int,
    ):
        if expected_pages <= 0:
            return 0.0, "FAIL", "Expected page range is invalid"

        marker_coverage = (min(section_markers, expected_pages) / expected_pages * 100)
        chars_per_page = md_chars / expected_pages

        near_empty_threshold = max(120, expected_pages * 80)
        if md_chars < near_empty_threshold:
            return marker_coverage, "FAIL", "Chunk body text is near-empty for the declared page range"

        if section_markers >= expected_pages:
            return marker_coverage, "PASS", "Section markers align with expected pages"

        if status_ret == "PASS" and (chars_per_page >= 400 or md_images > 0):
            return marker_coverage, "PASS", "Strong text or image evidence supports sparse structural markers"

        if status_ret in {"PASS", "WARN"}:
            return marker_coverage, "WARN", "Low section marker density with otherwise plausible chunk evidence"

        return marker_coverage, "FAIL", "Chunk evidence coverage below threshold"

    def verify_with_scope(self, md_path, verify_scope="full-source", manifest_path=None):
        md_path = pathlib.Path(md_path)
        content = md_path.read_text(encoding="utf-8")

        if verify_scope == "package":
            return {"result": "NOT_IMPLEMENTED", "gaps": [], "verify_scope": "package"}

        manifest_contract = re.search(r'^primary_ingest_contract:\s*"manifest"\s*$', content, re.MULTILINE)
        if manifest_contract and verify_scope == "full-source":
            return {"result": "SKIPPED", "gaps": [], "verify_scope": "full-source"}

        pdf_path = self.get_source_pdf_path(content, md_path)
        if not pdf_path:
            return {"result": "ERROR", "gaps": [], "verify_scope": verify_scope}

        if verify_scope == "chunk":
            return self.verify_chunk_scope(pdf_path, md_path, content, manifest_path=manifest_path)

        result = self.verify_full_source(pdf_path, md_path)
        result["verify_scope"] = "full-source"
        return result

    def write_audit_stamp(self, md_path, noises, missing_count, verify_scope="full-source", manifest_path=None):
        today = date.today().strftime("%Y-%m-%d")
        score = 1.0
        if noises > 0:
            score -= min(0.5, noises * 0.05)
        if missing_count > 0:
            score -= min(0.5, missing_count * 0.1)
        score = round(max(0.0, score), 2)
        score_str = f"{score:.2f}"

        if self.hmac_key:
            message = f"{pathlib.Path(md_path).stem}-{score_str}-{today}-v1.0-{verify_scope}".encode("utf-8")
            signature = hmac.new(self.hmac_key, message, hashlib.sha256).hexdigest()
        else:
            signature = "UNSIGNED"
            logging.warning("KIRO_AUDIT_SECRET not set. Audit stamp will be UNSIGNED.")

        status = "PASSED" if score >= 0.9 else "FAILED"
        verify_result = "SKIPPED"
        verify_gaps = []
        verify_meta = self.verify_with_scope(md_path, verify_scope=verify_scope, manifest_path=manifest_path)
        verify_result = verify_meta.get("result", "ERROR")
        verify_gaps = verify_meta.get("gaps", [])

        if verify_result in {"FAIL", "ERROR"}:
            status = "FAILED"
        elif verify_result == "NOT_IMPLEMENTED":
            status = "FAILED"

        stamp_lines = [
            "audit_stamp: true",
            "audit:",
            f"  score: {score_str}",
            f'  date: "{today}"',
            f'  status: "{status}"',
            '  auditor: "v1.0"',
            f'  verify_scope: "{verify_scope}"',
            f'  verify_result: "{verify_result}"',
            f"  verify_gaps: {verify_gaps}",
            f'  signature: "{signature}"',
        ]
        if verify_meta.get("range"):
            stamp_lines.append(f"  verify_range: {verify_meta['range']}")
        if verify_meta.get("range_source"):
            stamp_lines.append(f'  verify_range_source: "{verify_meta["range_source"]}"')
        if verify_meta.get("manifest_match"):
            stamp_lines.append(f"  verify_manifest_range: {verify_meta['manifest_match']}")

        stamp_text = "\n".join(stamp_lines)
        content = pathlib.Path(md_path).read_text(encoding="utf-8")
        frontmatter_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL | re.MULTILINE)

        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            body = content[frontmatter_match.end() :]
            lines = frontmatter.splitlines()
            filtered = []
            skipping_audit = False
            for line in lines:
                stripped = line.strip()
                if stripped == "audit_stamp: true" or stripped == "audit:":
                    skipping_audit = True
                    continue
                if skipping_audit:
                    if line.startswith("  "):
                        continue
                    skipping_audit = False
                if not skipping_audit:
                    filtered.append(line)
            new_frontmatter = "\n".join(line for line in filtered if line.strip()).strip()
            if new_frontmatter:
                new_frontmatter = new_frontmatter + "\n" + stamp_text
            else:
                new_frontmatter = stamp_text
            new_content = "---\n" + new_frontmatter.strip() + "\n---\n" + body
        else:
            new_content = "---\n" + stamp_text + "\n---\n\n" + content

        pathlib.Path(md_path).write_text(new_content, encoding="utf-8")
        return score, status, verify_result


def main():
    parser = argparse.ArgumentParser(description="Audit and standardize Markdown knowledge.")
    parser.add_argument("path", help="Path to Markdown file")
    parser.add_argument("--fix", action="store_true", help="Execute standardization and write audit stamp")
    parser.add_argument("--prefix", help="Prefix for assets (defaults to filename)")
    parser.add_argument("--vault", default="d:/NoteBookLLM_Br/3-resources/raw_assets", help="Path to asset vault")
    parser.add_argument("--verify-scope", choices=VERIFY_SCOPES, default="full-source", help="Verification scope")
    parser.add_argument("--manifest", help="Manifest path for chunk or package verification")
    args = parser.parse_args()

    auditor = MarkdownAuditor()
    if not os.path.exists(args.path):
        logging.error(f"File not found: {args.path}")
        sys.exit(1)

    if args.verify_scope == "package":
        logging.error("package verify scope is not implemented yet.")
        sys.exit(1)

    with open(args.path, "r", encoding="utf-8") as handle:
        text = handle.read()

    noises = auditor.check_ligatures(text)
    missing = auditor.verify_links(args.path, vault_path=args.vault)

    print(f"\n--- Audit Report: {os.path.basename(args.path)} ---")
    print(f"Noise (Ligatures): {noises}")
    print(f"Broken Links: {len(missing)}")
    print(f"Verify Scope: {args.verify_scope}")

    if args.fix:
        if noises > 10:
            logging.error("Too much noise. Fix manually before promotion.")
            sys.exit(1)
        if missing:
            logging.error("Missing assets. Fix links before promotion.")
            sys.exit(1)

        prefix = args.prefix if args.prefix else pathlib.Path(args.path).stem
        auditor.standardize_assets(args.path, prefix, args.vault, dry_run=False)
        score, status, verify_result = auditor.write_audit_stamp(
            args.path,
            noises,
            len(missing),
            verify_scope=args.verify_scope,
            manifest_path=args.manifest,
        )
        logging.info(
            f"Standardization complete. Audit {status} "
            f"(Score: {score}, Verify: {verify_result}, Scope: {args.verify_scope})"
        )
        if status != "PASSED":
            sys.exit(1)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
