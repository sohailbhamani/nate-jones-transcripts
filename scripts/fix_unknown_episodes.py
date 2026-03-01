#!/usr/bin/env python3
"""
fix_unknown_episodes.py
Renames unknown-* episode dirs to proper YYYY-MM-DD-slug format
using YouTube Data API v3 for metadata.
Usage: doppler run --project moltbot --config dev -- python fix_unknown_episodes.py <repo_dir>
"""
import os
import re
import sys
import time
import json
import requests
from pathlib import Path

def slugify(title):
    s = title.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s[:60]

def get_yt_metadata(video_id, api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"part": "snippet", "id": video_id, "key": api_key}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    items = r.json().get("items", [])
    if not items:
        return None
    snippet = items[0]["snippet"]
    return {
        "title": snippet["title"],
        "publish_date": snippet["publishedAt"][:10],
        "channel": snippet["channelTitle"],
        "tags": snippet.get("tags", []),
    }

def fix_repo(repo_dir, api_key):
    episodes_dir = Path(repo_dir) / "episodes"
    unknowns = sorted([d for d in episodes_dir.iterdir() if d.name.startswith("unknown-")])
    print(f"Found {len(unknowns)} unknown episodes in {repo_dir}")

    for ep_dir in unknowns:
        # Extract video_id from transcript.md
        md = ep_dir / "transcript.md"
        if not md.exists():
            print(f"  SKIP {ep_dir.name} — no transcript.md")
            continue
        content = md.read_text()
        m = re.search(r'video_id:\s*["\']?([A-Za-z0-9_-]{11})', content)
        if not m:
            print(f"  SKIP {ep_dir.name} — no video_id found")
            continue
        video_id = m.group(1)

        meta = get_yt_metadata(video_id, api_key)
        if not meta:
            print(f"  SKIP {video_id} — not found on YouTube")
            continue

        title = meta["title"]
        date = meta["publish_date"]
        slug = slugify(title)
        new_name = f"{date}-{slug}"
        new_dir = episodes_dir / new_name

        # Update frontmatter in transcript.md
        content = re.sub(r'title:\s*"Unknown"', f'title: "{title.replace(chr(34), chr(39))}"', content)
        content = re.sub(r'publish_date:\s*"unknown"', f'publish_date: "{date}"', content)
        content = re.sub(r'author:\s*"[^"]*"', f'author: "{meta["channel"]}"', content)
        md.write_text(content)

        # Rename directory
        if new_dir.exists():
            print(f"  CONFLICT {new_name} already exists, skipping rename")
        else:
            ep_dir.rename(new_dir)
            print(f"  FIXED {ep_dir.name} -> {new_name}")

        time.sleep(0.3)

    print("Done.")

if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("ERROR: YOUTUBE_API_KEY not set")
        sys.exit(1)
    fix_repo(repo, api_key)
