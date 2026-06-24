import sqlite3

conn = sqlite3.connect("data/developers.db")
cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE developers
    ADD COLUMN role TEXT
    """)
    print("Role column added")
except Exception as e:
    print(e)

conn.commit()
conn.close()