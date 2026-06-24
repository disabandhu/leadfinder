from fastapi import FastAPI
import sqlite3

app = FastAPI()


def get_connection():
    return sqlite3.connect("data/developers.db")


@app.get("/")
def home():
    return {
        "message": "LeadFinder API Running"
    }


@app.get("/stats")
def stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM developers")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM developers WHERE source='github'"
    )
    github_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM developers WHERE source='devto'"
    )
    devto_count = cursor.fetchone()[0]

    conn.close()

    return {
        "total_profiles": total,
        "github_profiles": github_count,
        "devto_profiles": devto_count
    }


@app.get("/search")
def search(q: str):

    conn = get_connection()
    cursor = conn.cursor()

    term = f"%{q}%"

    cursor.execute("""
    SELECT
        name,
        username,
        role,
        company,
        location,
        email,
        linkedin,
        github,
        website,
        source
    FROM developers
    WHERE
        role LIKE ?
        OR bio LIKE ?
        OR company LIKE ?
        OR location LIKE ?
        OR username LIKE ?
        OR name LIKE ?
    ORDER BY
        CASE
            WHEN role LIKE ? THEN 1
            WHEN bio LIKE ? THEN 2
            ELSE 3
        END
    LIMIT 50
    """, (
        term,
        term,
        term,
        term,
        term,
        term,
        term,
        term
    ))

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "name": row[0],
            "username": row[1],
            "role": row[2],
            "company": row[3],
            "location": row[4],
            "email": row[5],
            "linkedin": row[6],
            "github": row[7],
            "website": row[8],
            "source": row[9]
        }
        for row in rows
    ]


@app.get("/search_role")
def search_role(q: str):

    conn = get_connection()
    cursor = conn.cursor()

    term = f"%{q}%"

    cursor.execute("""
    SELECT
        name,
        username,
        role,
        company,
        location,
        email,
        linkedin,
        github,
        website,
        source
    FROM developers
    WHERE role LIKE ?
    LIMIT 50
    """, (term,))

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "name": row[0],
            "username": row[1],
            "role": row[2],
            "company": row[3],
            "location": row[4],
            "email": row[5],
            "linkedin": row[6],
            "github": row[7],
            "website": row[8],
            "source": row[9]
        }
        for row in rows
    ]