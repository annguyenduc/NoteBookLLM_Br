import unittest
import os
import shutil
import pathlib
from datetime import date, timedelta
from promote import promote

class TestPromote(unittest.TestCase):
    def setUp(self):
        # Create test environment
        self.test_root = pathlib.Path("00_Inbox/Converted_Sources/TEST_PROMOTE")
        self.test_root.mkdir(parents=True, exist_ok=True)
        
        self.md_file = self.test_root / "RAW_TEST_FILE.md"
        self.pdf_file = pathlib.Path("00_Inbox/test_source.pdf")
        
        # Create a dummy PDF
        with open(self.pdf_file, "w") as f:
            f.write("%PDF-1.4 dummy")
            
        # Target directories
        self.ingest_dir = pathlib.Path("3-resources/raw_ingest")
        self.sources_dir = pathlib.Path("3-resources/raw_sources")

    def create_md(self, status="PASSED", audit_date=None):
        if not audit_date:
            audit_date = date.today().strftime("%Y-%m-%d")
        
        content = f"""# TEST
Source PDF: test_source.pdf
audit:
  score: 0.95
  date: "{audit_date}"
  status: "{status}"
  auditor: "v1.0"
---
Body content here.
"""
        with open(self.md_file, "w", encoding="utf-8") as f:
            f.write(content)

    def test_promote_success(self):
        """PASSED + fresh date -> promotes successfully"""
        self.create_md(status="PASSED")
        success = promote(str(self.md_file))
        self.assertTrue(success)
        self.assertTrue((self.ingest_dir / "RAW_TEST_FILE.md").exists())
        self.assertTrue((self.sources_dir / "test_source.pdf").exists())
        self.assertFalse(self.test_root.exists())

    def test_promote_stale_date(self):
        """PASSED + stale date (8 days ago) -> blocked"""
        stale_date = (date.today() - timedelta(days=8)).strftime("%Y-%m-%d")
        self.create_md(status="PASSED", audit_date=stale_date)
        success = promote(str(self.md_file))
        self.assertFalse(success)
        self.assertTrue(self.md_file.exists())

    def test_promote_failed_status(self):
        """FAILED status -> blocked"""
        self.create_md(status="FAILED")
        success = promote(str(self.md_file))
        self.assertFalse(success)
        self.assertTrue(self.md_file.exists())

    def test_promote_dry_run(self):
        """--dry-run -> prints plan, moves nothing"""
        self.create_md(status="PASSED")
        success = promote(str(self.md_file), dry_run=True)
        self.assertTrue(success)
        self.assertTrue(self.md_file.exists())
        self.assertTrue(self.pdf_file.exists())

    def test_promote_missing_pdf(self):
        """Missing PDF -> promotes MD only, prints warning"""
        self.create_md(status="PASSED")
        os.remove(self.pdf_file) # Remove PDF
        success = promote(str(self.md_file))
        self.assertTrue(success)
        self.assertTrue((self.ingest_dir / "RAW_TEST_FILE.md").exists())
        self.assertFalse((self.sources_dir / "test_source.pdf").exists())

    def tearDown(self):
        # Cleanup
        for p in [self.test_root, self.pdf_file, 
                  self.ingest_dir / "RAW_TEST_FILE.md", 
                  self.sources_dir / "test_source.pdf"]:
            p = pathlib.Path(p)
            if p.exists():
                if p.is_dir():
                    shutil.rmtree(p)
                else:
                    os.remove(p)

if __name__ == "__main__":
    unittest.main()
