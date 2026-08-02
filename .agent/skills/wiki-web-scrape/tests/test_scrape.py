import os
import shutil
import unittest
import subprocess
import sys

# Set environment for testing
TEST_ROOT = os.path.abspath("scratch/test_scrape_env")
os.environ["WIKI_SCRAPE_OUTPUT"] = TEST_ROOT

class TestWikiWebScrape(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_ROOT):
            shutil.rmtree(TEST_ROOT)
        os.makedirs(TEST_ROOT, exist_ok=True)

    def test_01_scrape_example(self):
        """Test if scraping example.com works (or fails gracefully)."""
        scrape_script = ".agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py"
        output_file = os.path.join(TEST_ROOT, "example.md")
        
        result = subprocess.run(
            [sys.executable, scrape_script, "--url", "http://example.com", "--output", output_file],
            capture_output=True,
            text=True
        )
        
        # If Lightpanda is missing, this should fail with returncode 1
        # But for TDD, we want it to SUCCEED eventually.
        if result.returncode != 0:
            print(f"DEBUG: Scrape failed as expected (RED phase): {result.stdout} {result.stderr}")
            self.fail("Scraping failed. Lightpanda server might be down. Upgrade required for resilience.")
        
        self.assertTrue(os.path.exists(output_file), "Output file was not created.")
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Example Domain", content)

    @classmethod
    def tearDownClass(cls):
        # shutil.rmtree(TEST_ROOT)
        pass

if __name__ == "__main__":
    unittest.main()
