import sqlite3

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def deprecate_empty():
    conn = sqlite3.connect(DB_PATH)
    empty_synthesis = [
        'SYNTHESIS_Agentic_Orchestration_Frameworks',
        'SYNTHESIS_EXCEL_Mastery',
        'SYNTHESIS_Second_Brain_Standard_Spec',
        'SYNTHESIS_SQL_Mastery',
        'SYNTHESIS_THINK_Analytical_Thinking',
        'SYNTHESIS_ULTIMATE_Second_Brain_Spec',
        'SYNTHESIS_Wiki_Audit_20260501',
        'SYNTHESIS_Wiki_Intelligence_Architecture',
    ]
    placeholders = ','.join('?' * len(empty_synthesis))
    # Note: Added empty string and None checks
    count = conn.execute(f'''
        UPDATE atoms SET status='DEPRECATED'
        WHERE file_id IN ({placeholders})
        AND (content IS NULL OR content = '[NO CONTENT IN DB]' OR content = '')
    ''', empty_synthesis).rowcount
    conn.commit()
    conn.close()
    print(f"Deprecated: {count} empty synthesis atoms")

if __name__ == "__main__":
    deprecate_empty()
