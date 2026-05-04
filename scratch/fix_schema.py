import sqlite3
conn = sqlite3.connect('3-resources/wiki/wiki_brain.db')
conn.execute("UPDATE structure SET value='V3.1' WHERE key='schema_version'")
conn.commit()
conn.close()
print("Updated to V3.1")
