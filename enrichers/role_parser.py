import re


def extract_role(bio):

    if not bio:
        return ""

    bio = bio.strip()

    # Common separators

    for sep in [" @ ", " at ", "|", "\n"]:

        if sep.lower() in bio.lower():

            parts = re.split(
                re.escape(sep),
                bio,
                maxsplit=1,
                flags=re.IGNORECASE
            )

            return parts[0].strip()

    # Remove common fluff

    bio = re.sub(
        r"\bfrom\s+.*$",
        "",
        bio,
        flags=re.IGNORECASE
    )

    bio = re.sub(
        r"\bstudied\s+.*$",
        "",
        bio,
        flags=re.IGNORECASE
    )

    bio = re.sub(
        r"\ba\s+passionate\s+",
        "",
        bio,
        flags=re.IGNORECASE
    )

    bio = bio.strip()

    return bio[:80]