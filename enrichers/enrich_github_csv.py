import csv
import time

from website_enricher import enrich_website


INPUT_CSV = r"C:\Users\disa\github-developer-discovery\github_scraper\users_with_emails.csv"
OUTPUT_CSV = "github_enriched.csv"


with open(INPUT_CSV, newline="", encoding="utf-8") as infile:

    rows = list(csv.DictReader(infile))

    total = len(rows)

    for index, row in enumerate(rows, start=1):

        website = row.get("website", "")

        print(f"[{index}/{total}] {website}")

        if website:

            enriched = enrich_website(website)

            if enriched["email"]:
                row["email"] = enriched["email"]

            if enriched["linkedin"]:
                row["linkedin"] = enriched["linkedin"]

            if enriched["github"]:
                row["github"] = enriched["github"]

        time.sleep(0.5)


fieldnames = rows[0].keys()

with open(
    OUTPUT_CSV,
    "w",
    newline="",
    encoding="utf-8"
) as outfile:

    writer = csv.DictWriter(
        outfile,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(rows)

print("Saved github_enriched.csv")