import os
import sys
import unittest
import pypdf
from pathlib import Path

# Add scripts to path so we can import verify_convert
sys.path.append(str(Path(__file__).parent.parent / "scripts"))
import verify_convert

class TestVerifyConvert(unittest.TestCase):
    def setUp(self):
        self.test_pdf = "test_temp.pdf"
        self.test_md = "test_temp.md"
        
    def tearDown(self):
        if os.path.exists(self.test_pdf): os.remove(self.test_pdf)
        if os.path.exists(self.test_md): os.remove(self.test_md)

    def create_dummy_pdf(self, pages=1, images=0):
        writer = pypdf.PdfWriter()
        for i in range(pages):
            writer.add_blank_page(width=72, height=72)
        # Adding images is complex with pypdf without external assets, 
        # so we'll mock the image count if needed for specific tests
        with open(self.test_pdf, "wb") as f:
            writer.write(f)

    def write_md(self, content):
        with open(self.test_md, "w", encoding="utf-8") as f:
            f.write(content)

    def test_text_pdf_pass(self):
        self.create_dummy_pdf(pages=2)
        # 2 pages -> 2 sections (100% coverage)
        # Dummy content
        self.write_md("---\nfile_id: test\n---\n\n## Section 1\nContent 1\n## Section 2\nContent 2")
        # Since pypdf extract_text on blank pages is empty, pdf_chars=0, status=INFO
        res = verify_convert.verify(self.test_pdf, self.test_md)
        self.assertTrue(res)

    def test_missing_sections_warn(self):
        self.create_dummy_pdf(pages=10)
        # 10 pages -> 2 sections (20% coverage -> FAIL/WARN)
        self.write_md("---\n---\n\n## S1\n## S2")
        # coverage = 2/10 = 20% -> status X
        res = verify_convert.verify(self.test_pdf, self.test_md)
        self.assertFalse(res) # Should be FAIL due to 20% coverage

    def test_gap_detection(self):
        self.create_dummy_pdf(pages=1)
        # One long section, one very short section
        content = "---\n---\n\n## Long Section\n" + ("A" * 1000) + "\n## Short Section\nB"
        self.write_md(content)
        # avg = (1000 + 1) / 2 = 500. Short = 1 < 0.2*500 (100). Flagged!
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            res = verify_convert.verify(self.test_pdf, self.test_md)
        output = f.getvalue()
        self.assertIn("Short Section", output)
        self.assertFalse(res) # WARN/FAIL due to gaps

if __name__ == "__main__":
    unittest.main()
