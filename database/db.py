import sqlite3

DB_PATH = "data/developers.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def insert_developer(profile):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO developers (
        source,
        username,
        name,
        bio,
        company,
        location,
        email,
        linkedin,
        github,
        website,
        last_updated
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
    """, (
        profile.get("source"),
        profile.get("username"),
        profile.get("name"),
        profile.get("bio"),
        profile.get("company"),
        profile.get("location"),
        profile.get("email"),
        profile.get("linkedin"),
        profile.get("github"),
        profile.get("website")
    ))

    conn.commit()
    conn.close()