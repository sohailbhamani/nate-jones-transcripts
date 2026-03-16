#!/usr/bin/env python3
"""
Backfill YouTube descriptions into existing transcript frontmatter.
Fetches description from YouTube Data API v3 and adds it to transcript.md files
that don't already have a description field.

Usage:
    YOUTUBE_API_KEY=xxx python scripts/backfill_descriptions.py [--dry-run]
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")
BASE_DIR = Path(__file__).parent.parent
EPISODES_DIR = BASE_DIR / "episodes"

# YouTube API allows up to 50 IDs per request
BATCH_SIZE = 50


def get_descriptions_batch(video_ids):
    """Fetch descriptions for up to 50 video IDs in one API call."""
    if not YOUTUBE_API_KEY:
        raise RuntimeError("YOUTUBE_API_KEY environment variable not set")

    params = urllib.parse.urlencode(
        {
            "part": "snippet",
            "id": ",".join(video_ids),
            "key": YOUTUBE_API_KEY,
        }
    )
    url = f"https://www.googleapis.com/youtube/v3/videos?{params}"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    results = {}
    for item in data.get("items", []):
        vid = item["id"]
        desc = item["snippet"].get("description", "")
        results[vid] = desc

    return results


def extract_video_id(content):
    """Extract video_id from frontmatter."""
    match = re.search(r'^video_id:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    return match.group(1).strip() if match else None


def has_description(content):
    """Check if frontmatter already has a description field."""
    # Look for description: in the frontmatter (between --- markers)
    fm_match = re.match(r"^---\n(.*?\n)---", content, re.DOTALL)
    if not fm_match:
        return False
    frontmatter = fm_match.group(1)
    return bool(re.search(r"^description:", frontmatter, re.MULTILINE))


def add_description(content, description):
    """Insert description field after the author line in frontmatter."""
    if not description:
        desc_yaml = 'description: ""'
    else:
        lines = description.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        desc_yaml = "description: |\n" + "\n".join(f"  {line}" for line in lines)

    # Insert after author: line
    content = re.sub(
        r'(^author:\s*"[^"]*")\n',
        rf"\1\n{desc_yaml}\n",
        content,
        count=1,
        flags=re.MULTILINE,
    )
    return content


def main():
    dry_run = "--dry-run" in sys.argv

    # Find all episodes missing descriptions
    episodes = sorted(EPISODES_DIR.glob("*/transcript.md"))
    print(f"Scanning {len(episodes)} episodes...")

    needs_backfill = []
    for ep in episodes:
        content = ep.read_text()
        if has_description(content):
            continue
        video_id = extract_video_id(content)
        if video_id:
            needs_backfill.append((ep, video_id))

    print(f"Episodes needing description: {len(needs_backfill)}")
    if not needs_backfill:
        print("Nothing to do.")
        return

    if dry_run:
        for ep, vid in needs_backfill:
            print(f"  Would backfill: {ep.parent.name} ({vid})")
        return

    # Batch fetch descriptions
    updated = 0
    for i in range(0, len(needs_backfill), BATCH_SIZE):
        batch = needs_backfill[i : i + BATCH_SIZE]
        video_ids = [vid for _, vid in batch]

        print(f"\nFetching batch {i // BATCH_SIZE + 1} ({len(batch)} videos)...")
        try:
            descriptions = get_descriptions_batch(video_ids)
        except Exception as e:
            print(f"  ERROR fetching batch: {e}")
            continue

        for ep, vid in batch:
            desc = descriptions.get(vid)
            if desc is None:
                print(f"  SKIP {ep.parent.name}: video not found on YouTube")
                continue

            content = ep.read_text()
            new_content = add_description(content, desc)
            ep.write_text(new_content)
            updated += 1
            if desc:
                print(f"  OK {ep.parent.name}: {len(desc)} chars")
            else:
                print(f"  OK {ep.parent.name}: empty description")

        # Rate limit between batches
        if i + BATCH_SIZE < len(needs_backfill):
            time.sleep(1)

    print(f"\nDone. Updated {updated}/{len(needs_backfill)} episodes.")


if __name__ == "__main__":
    main()
