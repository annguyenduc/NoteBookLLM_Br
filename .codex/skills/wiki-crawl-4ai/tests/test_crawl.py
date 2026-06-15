import os
import shutil
import unittest
import subprocess
import sys

# Set environment for testing
TEST_ROOT = os.path.abspath("scratch/test_crawl_env")
os.makedirs(TEST_ROOT, exist_ok=True)

class TestWikiCrawl4AI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_ROOT):
            shutil.rmtree(TEST_ROOT)
        os.makedirs(TEST_ROOT, exist_ok=True)

    def test_01_crawl_example(self):
        """Test if crawling example.com with screenshot works."""
        crawl_script = ".agent/skills/wiki-crawl-4ai/scripts/crawl4ai_run.py"
        output_file = os.path.join(TEST_ROOT, "example.md")
        screenshot_file = os.path.join(TEST_ROOT, "example.png")
        
        # We'll try to crawl a very simple page
        result = subprocess.run(
            [sys.executable, crawl_script, "--url", "http://example.com", "--output", output_file, "--screenshot", "--headless"],
            capture_output=True,
            text=True,
            encoding="utf-8" # Force UTF-8 for subprocess reading
        )
        
        if result.returncode != 0:
            print(f"DEBUG: Crawl failed: {result.stdout} {result.stderr}")
            self.fail(f"Crawl failed with exit code {result.returncode}")
        
        self.assertTrue(os.path.exists(output_file), "Markdown file was not created.")
        self.assertTrue(os.path.exists(screenshot_file), "Screenshot file was not created.")
        
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Example Domain", content)
            self.assertIn("![Screenshot](example.png)", content)

    @classmethod
    def tearDownClass(cls):
        # shutil.rmtree(TEST_ROOT)
        pass

if __name__ == "__main__":
    unittest.main()
