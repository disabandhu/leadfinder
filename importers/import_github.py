import csv
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from database.db import insert_developer

CSV_FILE = r"C:\Users\disa\github-developer-discovery\github_scraper\users_with_emails.csv"

with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    count = 0

    for row in reader:

        profile = {
            "source": "github",
            "username": row.get("username", ""),
            "name": row.get("name", ""),
            "bio": row.get("bio", ""),
            "company": row.get("company", ""),
            "location": row.get("location", ""),
            "email": row.get("email", ""),
            "linkedin": "",
            "github": row.get("profile_url", ""),
            "website": ""
        }

        insert_developer(profile)
        count += 1

print(f"Imported {count} GitHub profiles")