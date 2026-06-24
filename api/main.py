from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
def home():
    return {"message": "LeadFinder API Running"}


@app.get("/search")
def search(q: str):

    conn = sqlite3.connect("data/developers.db")

    cursor = conn.cursor()

    search_term = f"%{q}%"

    cursor.execute("""
        SELECT
            name,
            username,
            company,
            location,
            email,
            linkedin,
            github,
            source
        FROM developers
        WHERE
            name LIKE ?
            OR bio LIKE ?
            OR company LIKE ?
        LIMIT 50
    """, (
        search_term,
        search_term,
        search_term
    ))

    rows = cursor.fetchall()

    conn.close()

    results = []

    for row in rows:
        results.append({
            "name": row[0],
            "username": row[1],
            "company": row[2],
            "location": row[3],
            "email": row[4],
            "linkedin": row[5],
            "github": row[6],
            "source": row[7]
        })

    return results