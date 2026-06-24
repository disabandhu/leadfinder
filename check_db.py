import sqlite3

conn = sqlite3.connect("data/developers.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM developers")

count = cursor.fetchone()[0]

print("Total developers:", count)

conn.close()