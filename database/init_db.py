import sqlite3

conn = sqlite3.connect("data/developers.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE developers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source TEXT,
    username TEXT UNIQUE,

    name TEXT,
    role TEXT,
    bio TEXT,

    company TEXT,
    location TEXT,

    email TEXT,
    linkedin TEXT,

    github TEXT,
    website TEXT
)
""")

conn.commit()
conn.close()

print("Database created")