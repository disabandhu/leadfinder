import sqlite3

conn = sqlite3.connect("data/developers.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS developers (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source TEXT,

    username TEXT UNIQUE,

    name TEXT,

    bio TEXT,

    company TEXT,

    location TEXT,

    email TEXT,

    linkedin TEXT,

    github TEXT,

    website TEXT,

    last_updated TEXT
)
""")

conn.commit()
conn.close()

print("Database created")