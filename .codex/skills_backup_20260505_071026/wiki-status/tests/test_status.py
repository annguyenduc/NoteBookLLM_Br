import os
import shutil
import sqlite3
import unittest
import subprocess
import sys

# Set environment for testing
TEST_ROOT = os.path.abspath("scratch/test_status_env")
WIKI_PATH = os.path.join(TEST_ROOT, "wiki")
TEST_DB = os.path.join(WIKI_PATH, "wiki_brain.db")

os.environ["WIKI_ROOT_PATH"] = WIKI_PATH
os.environ["WIKI_DB_PATH"] = TEST_DB

class TestWikiStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_ROOT):
            shutil.rmtree(TEST_ROOT)
        os.makedirs(os.path.join(WIKI_PATH, "concepts"), exist_ok=True)
        
        # Create minimal DB
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE atoms (file_id TEXT PRIMARY KEY, title TEXT, status TEXT)")
        cursor.execute("CREATE TABLE edges (source_id TEXT, target_id TEXT, edge_type TEXT, confidence REAL)")
        cursor.execute("CREATE TABLE task_logs (id INTEGER PRIMARY KEY, agent_id TEXT, action TEXT, status TEXT, details TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
        
        cursor.execute("INSERT INTO atoms (file_id, title, status) VALUES ('CONCEPT_Test', 'Test', 'VERIFIED')")
        cursor.execute("INSERT INTO task_logs (agent_id, action, status, details) VALUES ('@tester', 'test', 'success', 'Sample log')")
        
        conn.commit()
        conn.close()

    def test_01_dashboard(self):
        """Test if dashboard.py prints stats correctly."""
        # Dashboard calls vault_health and lint_engine, which might fail if not careful
        # But we mostly want to check if it reads the DB stats
        status_script = ".agent/skills/wiki-status/scripts/dashboard.py"
        # We use a dummy lint/health script path to avoid side effects if needed, 
        # but let's see if it works as is
        result = subprocess.run([sys.executable, status_script], env=os.environ, capture_output=True, text=True, encoding="utf-8")
        
        output = result.stdout
        # print(f"DEBUG OUTPUT:\n{output}")
        
        self.assertIn("Tong so Atoms:     1", output)
        self.assertIn("VERIFIED    : 1", output)
        self.assertIn("Sample log", output)

    @classmethod
    def tearDownClass(cls):
        # shutil.rmtree(TEST_ROOT)
        pass

if __name__ == "__main__":
    unittest.main()
