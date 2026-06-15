import os
import shutil
import sqlite3
import unittest
import subprocess
import sys

# Set environment for testing
TEST_ROOT = os.path.abspath("scratch/test_cleanup_env")
WIKI_PATH = os.path.join(TEST_ROOT, "wiki")
TEST_DB = os.path.join(WIKI_PATH, "wiki_brain.db")

os.environ["WIKI_ROOT_PATH"] = WIKI_PATH
os.environ["WIKI_DB_PATH"] = TEST_DB

class TestWikiCleanup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_ROOT):
            shutil.rmtree(TEST_ROOT)
        os.makedirs(os.path.join(WIKI_PATH, "concepts"), exist_ok=True)
        os.makedirs(os.path.join(WIKI_PATH, "entities"), exist_ok=True)
        os.makedirs(os.path.join(WIKI_PATH, "sources"), exist_ok=True)
        os.makedirs(os.path.join(WIKI_PATH, "synthesis"), exist_ok=True)
        
        # Create minimal DB with one valid atom
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE atoms (file_id TEXT PRIMARY KEY, title TEXT, status TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS atom_search (file_id TEXT, content TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS task_logs (id INTEGER PRIMARY KEY, agent_id TEXT, action TEXT, status TEXT, details TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute("INSERT INTO atoms (file_id, title, status) VALUES ('CONCEPT_Existing', 'Existing', 'VERIFIED')")
        conn.commit()
        conn.close()

        # Create atom files
        # 1. Valid file
        with open(os.path.join(WIKI_PATH, "concepts", "CONCEPT_Existing.md"), "w", encoding="utf-8") as f:
            f.write("---\nstatus: VERIFIED\n---\n# Existing\n## Core Principle\nTest content.")

        # 2. File with broken link
        with open(os.path.join(WIKI_PATH, "concepts", "CONCEPT_Broken.md"), "w", encoding="utf-8") as f:
            f.write("---\nstatus: DRAFT\n---\n# Broken Link\n## Core Principle\nLink to [[NON_EXISTENT_ATOM]]")

        # 3. File missing section
        with open(os.path.join(WIKI_PATH, "concepts", "CONCEPT_Missing.md"), "w", encoding="utf-8") as f:
            f.write("---\nstatus: DRAFT\n---\n# Missing Section\nNo core principle here.")

    def test_01_lint_audit(self):
        """Test if lint_engine.py identifies broken links and missing sections."""
        lint_script = ".agent/skills/wiki-cleanup/scripts/lint_engine.py"
        result = subprocess.run([sys.executable, lint_script], env=os.environ, capture_output=True, text=True, encoding="utf-8")
        
        output = result.stdout
        print(f"\nDEBUG OUTPUT:\n{output}")
        
        self.assertIn("BROKEN_LINK", output)
        self.assertIn("NON_EXISTENT_ATOM", output)
        self.assertIn("TEMPLATE_VIOLATION", output)
        self.assertIn("4F Reflection", output)

    @classmethod
    def tearDownClass(cls):
        # shutil.rmtree(TEST_ROOT)
        pass

if __name__ == "__main__":
    unittest.main()
