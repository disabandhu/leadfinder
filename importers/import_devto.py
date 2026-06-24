import csv
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from enrichers.role_parser import extract_role

from database.db import insert_developer

CSV_FILE = r"C:\Users\disa\dev_leads\developers.csv"

with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    count = 0

    for row in reader:
        bio = row.get("github_bio", "")
        role = extract_role(bio)

        profile = {
            "source": "devto",
            "username": row.get("username", ""),
            "name": row.get("name", ""),
            "bio": row.get("github_bio", ""),
            "role": role,
            "company": row.get("github_company", ""),
            "location": row.get("location", ""),
            "email": row.get("emails", ""),
            "linkedin": row.get("linkedin_links", ""),
            "github": row.get("github_links", ""),
            "website": row.get("website", "")
        }

        insert_developer(profile)
        count += 1

print(f"Imported {count} Dev.to profiles")