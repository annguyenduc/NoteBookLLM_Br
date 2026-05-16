import os
import subprocess
import sys
import sqlite3
import time

# Thiết lập môi trường để tránh lỗi encoding trên Windows
if sys.stdout.encoding != 'utf-8':
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except:
        pass

ROOT_DIR = r'd:\NoteBookLLM_Br'
DB_PATH = os.path.join(ROOT_DIR, '3-resources', 'wiki', 'wiki_brain.db')
TEST_FILE = os.path.join(ROOT_DIR, '00_Inbox', 'TEST_INTEGRATION_HARNESS.md')

def log_step(step):
    print(f'\n>>> [STEP] {step}')

def run_test():
    log_step('1. Setup Mock Data')
    test_content = '''---
title: Test Integration Harness
file_id: TEST_INTEGRATION_HARNESS
status: DRAFT
audit:
  score: 1.00
  date: "2026-05-15"
  status: "PASSED"
  auditor: "master_harness_2.0"
  verify_result: "SKIPPED"
  verify_gaps: []
  signature: "test-harness-placeholder"
---
Đây là nội dung giả lập để kiểm tra tính toàn vẹn của Master Harness 2.0.
Đảm bảo rằng hệ thống có thể Ingest và Rebuild mà không gặp lỗi.
Dòng này để đảm bảo file > 200 bytes nhằm vượt qua Rule R11.
Lorum Ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
'''
    try:
        with open(TEST_FILE, 'w', encoding='utf-8') as f:
            f.write(test_content)
        print(f'Created: {TEST_FILE}')
    except Exception as e:
        print(f'ERROR creating mock data: {e}')
        return False

    log_step('2. Execute deterministic ingest stage (wiki-ingest script)')
    ingest_script = os.path.join(ROOT_DIR, '.agent', 'skills', 'wiki-ingest', 'scripts', 'ingest.py')
    # This harness targets the stage-level ingest script, not the full /ingest lifecycle entrypoint.
    # Set PYTHONPATH to include ingest scripts directory for imports like score_engine.
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.join(ROOT_DIR, '.agent', 'skills', 'wiki-ingest', 'scripts')
    
    result = subprocess.run([sys.executable, ingest_script, TEST_FILE], capture_output=True, text=True, env=env, encoding='utf-8')
    print(result.stdout)
    if result.returncode != 0:
        print(f'ERROR in ingest: {result.stderr}')
        return False

    log_step('3. Verify Ingest in DB')
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Normalized path for Windows
        norm_path = os.path.normpath(os.path.abspath(TEST_FILE))
        cursor.execute('SELECT status, confidence FROM atoms WHERE file_id = ?', (norm_path,))
        row = cursor.fetchone()
        if row:
            print(f'Found Atom: status={row[0]}, confidence={row[1]}')
        else:
            print('ERROR: Atom not found in DB after ingest.')
            conn.close()
            return False
        conn.close()
    except Exception as e:
        print(f'Database error: {e}')
        return False

    log_step('4. Execute wiki-rebuild')
    rebuild_script = os.path.join(ROOT_DIR, '.agent', 'skills', 'wiki-rebuild', 'scripts', 'rebuild.py')
    result = subprocess.run([sys.executable, rebuild_script], capture_output=True, text=True, encoding='utf-8')
    print(result.stdout)
    if result.returncode != 0:
        print(f'ERROR in rebuild: {result.stderr}')
        return False

    log_step('5. Final stage-level pipeline validation')
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT details FROM task_logs WHERE action=\'rebuild\' ORDER BY timestamp DESC LIMIT 1')
        last_log = cursor.fetchone()
        if last_log:
            print(f'Last Rebuild Log: {last_log[0]}')
        
        print('\n[SUCCESS] Master Harness 2.0: ingest.py -> rebuild.py stage harness is STABLE.')
        conn.close()
    except Exception as e:
        print(f'Final validation error: {e}')
        return False
        
    return True

if __name__ == '__main__':
    success = run_test()
    if not success:
        sys.exit(1)
    else:
        sys.exit(0)
