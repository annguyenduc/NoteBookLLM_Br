import os
import shutil
import sqlite3
import unittest
import subprocess
import sys

# Set environment for testing
TEST_ROOT = os.path.abspath("scratch/test_rebuild_env")
WIKI_PATH = os.path.join(TEST_ROOT, "wiki")
TEST_DB = os.path.join(WIKI_PATH, "wiki_brain.db")

os.environ["WIKI_ROOT_PATH"] = WIKI_PATH
os.environ["WIKI_DB_PATH"] = TEST_DB

class TestWikiRebuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_ROOT):
            shutil.rmtree(TEST_ROOT)
        os.makedirs(os.path.join(WIKI_PATH, "concepts"), exist_ok=True)
        os.makedirs(os.path.join(WIKI_PATH, "entities"), exist_ok=True)
        os.makedirs(os.path.join(WIKI_PATH, "sources"), exist_ok=True)
        os.makedirs(os.path.join(WIKI_PATH, "synthesis"), exist_ok=True)
        os.makedirs(os.path.join(WIKI_PATH, "decisions"), exist_ok=True)
        
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
        cursor.execute("CREATE TABLE IF NOT EXISTS atom_search (file_id TEXT, content TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS task_logs (id INTEGER PRIMARY KEY, details TEXT)")
        conn.commit()
        conn.close()

    def test_01_sync_new_file(self):
        """Test if rebuild.py adds a new file to the DB."""
        # Create a valid file
        concept_file = os.path.join(WIKI_PATH, "concepts", "CONCEPT_Test.md")
        with open(concept_file, "w", encoding="utf-8") as f:
            f.write("---\nstatus: DRAFT\n---\n# Test Concept\nContent more than 200 bytes " * 10)
            
        rebuild_script = ".agent/skills/wiki-rebuild/scripts/rebuild.py"
        subprocess.run([sys.executable, rebuild_script], env=os.environ, capture_output=True)
        
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM atoms WHERE file_id = 'CONCEPT_Test'")
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "DRAFT")
        conn.close()

    def test_02_handle_deletion(self):
        """Test if rebuild.py handles file deletion (Should mark as DEPRECATED)."""
        concept_file = os.path.join(WIKI_PATH, "concepts", "CONCEPT_Test.md")
        os.remove(concept_file)
        
        rebuild_script = ".agent/skills/wiki-rebuild/scripts/rebuild.py"
        subprocess.run([sys.executable, rebuild_script], env=os.environ, capture_output=True)
        
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM atoms WHERE file_id = 'CONCEPT_Test'")
        row = cursor.fetchone()
        
        # CURRENT BEHAVIOR: It will NOT be deprecated. This test will FAIL initially.
        self.assertEqual(row[0], "DEPRECATED", "Atom should be DEPRECATED after file deletion.")
        conn.close()

if __name__ == "__main__":
    unittest.main()
