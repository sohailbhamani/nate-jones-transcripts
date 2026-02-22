#!/usr/bin/env python3
"""
Discover new Nate B Jones videos via YouTube RSS feed.
Compares against video_ids.txt and appends new IDs.
No API key needed — RSS is public.
"""

import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

CHANNEL_ID = "UC0C-17n9iuUQPylguM1d-lQ"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

BASE_DIR = Path(__file__).parent.parent
VIDEO_IDS_FILE = BASE_DIR / "video_ids.txt"


def fetch_rss_video_ids(retries=3, backoff=5):
    """Fetch recent video IDs from YouTube RSS feed, with retries."""
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(
                RSS_URL,
                headers={"User-Agent": "NateBJonesTranscripts/1.0"},
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()

            root = ET.fromstring(data)
            ns = {"yt": "http://www.youtube.com/xml/schemas/2015"}

            video_ids = []
            for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                vid_elem = entry.find("yt:videoId", ns)
                if vid_elem is not None and vid_elem.text:
                    video_ids.append(vid_elem.text.strip())

            return video_ids
        except Exception as e:
            last_err = e
            if attempt < retries:
                wait = backoff * attempt
                print(f"  Attempt {attempt} failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)

    raise RuntimeError(f"RSS fetch failed after {retries} attempts: {last_err}")


def load_existing_ids():
    """Load existing video IDs from file."""
    if not VIDEO_IDS_FILE.exists():
        return set()
    with open(VIDEO_IDS_FILE) as f:
        return {line.strip() for line in f if line.strip()}


def main():
    print("=== Nate B Jones Video Discovery (RSS) ===")

    existing = load_existing_ids()
    print(f"Existing videos: {len(existing)}")

    rss_ids = fetch_rss_video_ids()
    print(f"Videos in RSS feed: {len(rss_ids)}")

    new_ids = [vid for vid in rss_ids if vid not in existing]

    if not new_ids:
        print("No new videos found.")
        return

    print(f"New videos found: {len(new_ids)}")
    for vid in new_ids:
        print(f"  + {vid}")

    # Append new IDs to file
    with open(VIDEO_IDS_FILE, "a") as f:
        for vid in new_ids:
            f.write(f"{vid}\n")

    print(f"Appended {len(new_ids)} new video IDs to {VIDEO_IDS_FILE}")


if __name__ == "__main__":
    main()
