import requests
import re


EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def enrich_website(url):

    result = {
        "email": "",
        "linkedin": "",
        "github": ""
    }

    if not url:
        return result

    try:

        html = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        ).text

        emails = re.findall(EMAIL_REGEX, html)

        if emails:
            result["email"] = emails[0]

        linkedin_matches = re.findall(
            r"https?://(?:www\.)?linkedin\.com/[^\s\"'>]+",
            html,
            flags=re.I
        )

        if linkedin_matches:
            result["linkedin"] = linkedin_matches[0]

        github_matches = re.findall(
            r"https?://(?:www\.)?github\.com/[^\s\"'>]+",
            html,
            flags=re.I
        )

        if github_matches:
            result["github"] = github_matches[0]

    except Exception:
        pass

    return result