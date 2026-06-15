import os
import shutil
import sqlite3
import unittest
import subprocess
import sys

# Set environment for testing
TEST_ROOT = os.path.abspath("scratch/test_ingest_env")
TEST_DB = os.path.join(TEST_ROOT, "test_wiki.db")
os.environ["WIKI_DB_PATH"] = TEST_DB

class TestWikiIngest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_ROOT):
            shutil.rmtree(TEST_ROOT)
        os.makedirs(TEST_ROOT, exist_ok=True)
        
        # Create minimal DB schema
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atoms (
                file_id TEXT PRIMARY KEY,
                title TEXT,
                type TEXT,
                status TEXT,
                confidence REAL,
                learning_source INTEGER,
                file_hash TEXT,
                agent_id TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS review_queue (
                item_id TEXT,
                reason TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS task_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT,
                action TEXT,
                target_file TEXT,
                status TEXT,
                details TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS edges (
                source_id TEXT,
                target_id TEXT,
                edge_type TEXT
            )
        """)
        # Needed for score_engine if it queries other tables
        cursor.execute("CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT)")
        conn.commit()
        conn.close()

    def setUp(self):
        # Create a dummy file for ingestion (> 200 bytes)
        self.sample_file = os.path.join(TEST_ROOT, "sample.md")
        with open(self.sample_file, "w", encoding="utf-8") as f:
            f.write("This is a sample document for ingestion testing. " * 10)
        
    def test_01_routing(self):
        """Test if magika_router correctly identifies the file."""
        router_script = ".agent/skills/wiki-ingest/scripts/magika_router.py"
        result = subprocess.run(
            [sys.executable, router_script, self.sample_file],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("markdown", result.stdout.lower())

    def test_02_ingest_new_file(self):
        """Test if ingest.py successfully creates a DRAFT atom."""
        ingest_script = ".agent/skills/wiki-ingest/scripts/ingest.py"
        result = subprocess.run(
            [sys.executable, ingest_script, self.sample_file],
            capture_output=True,
            text=True,
            env=os.environ
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS", result.stdout)
        
        # Verify in DB
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM atoms WHERE file_id LIKE ?", (f"%{os.path.basename(self.sample_file)}%",))
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "DRAFT")
        conn.close()

    def test_03_duplicate_detection(self):
        """Test if ingest.py skips duplicate files."""
        ingest_script = ".agent/skills/wiki-ingest/scripts/ingest.py"
        # Run second time
        result = subprocess.run(
            [sys.executable, ingest_script, self.sample_file],
            capture_output=True,
            text=True,
            env=os.environ
        )
        self.assertIn("Duplicate content detected", result.stdout)

    @classmethod
    def tearDownClass(cls):
        # shutil.rmtree(TEST_ROOT)
        pass

if __name__ == "__main__":
    unittest.main()
