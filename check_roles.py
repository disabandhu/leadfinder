import sqlite3

conn = sqlite3.connect("data/developers.db")

cursor = conn.cursor()

cursor.execute("""
SELECT name, role
FROM developers
WHERE role IS NOT NULL
LIMIT 10
""")

for row in cursor.fetchall():
    print(row)

conn.close()