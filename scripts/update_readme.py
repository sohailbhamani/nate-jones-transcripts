#!/usr/bin/env python3
"""Update README.md stats from actual episode data."""

import re
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
README_FILE = BASE_DIR / "README.md"
EPISODES_DIR = BASE_DIR / "episodes"


def main():
    import re as _re

    episodes = sorted(
        d.name
        for d in EPISODES_DIR.iterdir()
        if d.is_dir()
        and not d.name.startswith(".")
        and _re.match(r"^\d{4}-\d{2}-\d{2}", d.name)
    )

    if not episodes:
        print("No episodes found")
        return

    total = len(episodes)
    oldest = episodes[0][:10]
    newest = episodes[-1][:10]

    # Format dates nicely (2026-02-13 -> Feb 13, 2026)
    def fmt(date_str):
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%b %-d, %Y")

    today = datetime.now(timezone.utc).strftime("%b %-d, %Y")

    readme = README_FILE.read_text()

    readme = re.sub(
        r"- \*\*Videos Downloaded\*\*:.*",
        f"- **Videos Downloaded**: {total}",
        readme,
    )
    readme = re.sub(
        r"- \*\*Date Range\*\*:.*",
        f"- **Date Range**: {fmt(oldest)} - {fmt(newest)}",
        readme,
    )
    readme = re.sub(
        r"- \*\*Last Updated\*\*:.*",
        f"- **Last Updated**: {today}",
        readme,
    )

    README_FILE.write_text(readme)
    print(f"README updated: {total} videos, {fmt(oldest)} - {fmt(newest)}")


if __name__ == "__main__":
    main()
