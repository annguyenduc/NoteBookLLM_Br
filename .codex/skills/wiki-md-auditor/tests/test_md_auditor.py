import unittest
import os
import shutil
import pathlib
from md_auditor import MarkdownAuditor

class TestMarkdownAuditor(unittest.TestCase):
    def setUp(self):
        self.test_dir = pathlib.Path(__file__).parent / "data"
        self.test_dir.mkdir(exist_ok=True)
        self.img_dir = self.test_dir / "images"
        self.img_dir.mkdir(exist_ok=True)
        
        # Create a sample MD with ligatures and broken links
        self.bad_md = self.test_dir / "bad_file.md"
        with open(self.bad_md, "w", encoding="utf-8") as f:
            f.write("# Test File\n")
            f.write("This is an e?ciency test with bad font.\n") # Ligature: ?
            f.write("![Existing](images/valid.png)\n")
            f.write("![Broken](images/missing.png)\n")
            
        # Create existing image
        (self.img_dir / "valid.png").touch()
        
        self.auditor = MarkdownAuditor()

    def test_ligature_detection(self):
        with open(self.bad_md, "r", encoding="utf-8") as f:
            content = f.read()
        noise_count = self.auditor.check_ligatures(content)
        self.assertGreater(noise_count, 0, "Should detect at least one ligature artifact")

    def test_link_verification(self):
        missing_links = self.auditor.verify_links(self.bad_md)
        self.assertIn("images/missing.png", missing_links)
        self.assertNotIn("images/valid.png", missing_links)

    def test_prefix_standardization(self):
        # Setup mock for move
        output_md = self.test_dir / "HD_test_file.md"
        shutil.copy(self.bad_md, output_md)
        
        prefix = "TEST_DOC"
        vault = self.test_dir / "vault"
        self.auditor.standardize_assets(output_md, prefix, vault, dry_run=False)
        
        with open(output_md, "r", encoding="utf-8") as f:
            content = f.read()
        
        self.assertIn(f"![[{prefix}_fig_00.png]]", content)
        self.assertTrue((vault / f"{prefix}_fig_00.png").exists())

    def tearDown(self):
        # Clean up test data if needed
        pass

if __name__ == "__main__":
    unittest.main()
