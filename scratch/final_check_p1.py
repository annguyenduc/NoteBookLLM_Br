import sqlite3

def final_check():
    conn = sqlite3.connect('3-resources/wiki/wiki_brain.db')

    # Tables
    tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
    print('TABLES:', tables)

    # atoms columns
    cols = [r[1] for r in conn.execute('PRAGMA table_info(atoms)').fetchall()]
    required = ['confidence','learning_source','status','human_review_flag']
    for c in required:
        print(f'  {c}: {"OK" if c in cols else "MISSING"}')

    # schema version
    ver = conn.execute("SELECT value FROM structure WHERE key='schema_version'").fetchone()
    print('VERSION:', ver[0] if ver else 'NOT SET')
    conn.close()

if __name__ == "__main__":
    final_check()
