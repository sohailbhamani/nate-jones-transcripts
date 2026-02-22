#!/usr/bin/env python3
"""
Smart YouTube transcript downloader using Supadata API (paid)
and YouTube Data API v3 for metadata.
"""

import json
import os
import random
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent.parent
EPISODES_DIR = BASE_DIR / "episodes"
VIDEO_IDS_FILE = BASE_DIR / "video_ids.txt"
PROGRESS_FILE = BASE_DIR / "progress.json"

# YouTube Data API
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")

# Supadata API
SUPADATA_API_KEY = os.environ.get("SUPADATA_API_KEY", "")
SUPADATA_ENDPOINT = "https://api.supadata.ai/v1/transcript"

# Rate limiting - lighter since Supadata handles YouTube-side throttling
MIN_DELAY = 1  # Minimum seconds between requests
MAX_DELAY = 2  # Maximum seconds between requests
BATCH_SIZE = 50  # Videos before taking a short break
BATCH_BREAK_MIN = 30  # 30 seconds break
BATCH_BREAK_MAX = 60  # 1 minute break


def load_progress():
    """Load progress from file."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": [], "failed": [], "last_run": None}


def save_progress(progress):
    """Save progress to file."""
    progress["last_run"] = datetime.now().isoformat()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text[:80].strip("-")


def get_video_metadata(video_id):
    """Get video metadata via YouTube Data API v3."""
    if not YOUTUBE_API_KEY:
        print("  Warning: No YOUTUBE_API_KEY, using minimal metadata")
        return None

    try:
        params = urllib.parse.urlencode(
            {
                "part": "snippet,contentDetails,statistics",
                "id": video_id,
                "key": YOUTUBE_API_KEY,
            }
        )
        url = f"https://www.googleapis.com/youtube/v3/videos?{params}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())

        items = data.get("items", [])
        if not items:
            return None

        item = items[0]
        snippet = item["snippet"]
        stats = item.get("statistics", {})
        content = item.get("contentDetails", {})

        # Parse ISO 8601 duration (PT1H2M3S)
        duration_str = content.get("duration", "PT0S")
        duration_match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration_str)
        if duration_match:
            h = int(duration_match.group(1) or 0)
            m = int(duration_match.group(2) or 0)
            s = int(duration_match.group(3) or 0)
            duration_seconds = h * 3600 + m * 60 + s
            duration_formatted = f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
        else:
            duration_seconds = 0
            duration_formatted = "0:00"

        # Parse publish date
        pub_date = snippet.get("publishedAt", "")[:10]

        return {
            "title": snippet.get("title", ""),
            "video_id": video_id,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "duration_seconds": duration_seconds,
            "duration": duration_formatted,
            "view_count": int(stats.get("viewCount", 0)),
            "publish_date": pub_date,
            "description": snippet.get("description", ""),
            "author": snippet.get("channelTitle", "Nate B Jones"),
            "keywords": snippet.get("tags", []),
        }
    except Exception as e:
        print(f"  Warning: Could not get metadata: {e}")
        return None


def get_transcript(video_id):
    """Get transcript using Supadata API."""
    if not SUPADATA_API_KEY:
        raise Exception("SUPADATA_API_KEY environment variable not set")

    url = f"{SUPADATA_ENDPOINT}?url=https://youtu.be/{video_id}"
    req = urllib.request.Request(
        url,
        headers={
            "x-api-key": SUPADATA_API_KEY,
            "User-Agent": "IdeaFunnel/1.0",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise Exception("RATE_LIMITED: Too many requests")
        elif e.code == 401:
            raise Exception("Invalid Supadata API key")
        else:
            raise Exception(f"Supadata API error: {e.code} - {e.read().decode()}")
    except urllib.error.URLError as e:
        raise Exception(f"Network error: {e}")

    content = data.get("content", [])
    if not content:
        raise Exception("No transcript content returned")

    full_text = " ".join(seg.get("text", "") for seg in content)
    segments = [
        {
            "text": seg.get("text", ""),
            "start": seg.get("offset", 0) / 1000,
            "duration": seg.get("duration", 0) / 1000,
        }
        for seg in content
    ]

    return {
        "full_text": full_text,
        "segments": segments,
        "segment_count": len(content),
    }


def save_transcript(metadata, transcript):
    """Save transcript in rich format with YAML frontmatter."""
    slug = slugify(metadata.get("title", metadata["video_id"]))
    date_prefix = metadata.get("publish_date", "unknown")
    folder_name = f"{date_prefix}-{slug}"

    episode_dir = EPISODES_DIR / folder_name
    episode_dir.mkdir(parents=True, exist_ok=True)

    yaml_content = f'''---
title: "{metadata.get("title", "Unknown").replace('"', '\\"')}"
video_id: "{metadata["video_id"]}"
youtube_url: "{metadata.get("url", "")}"
publish_date: "{metadata.get("publish_date", "unknown")}"
duration: "{metadata.get("duration", "unknown")}"
duration_seconds: {metadata.get("duration_seconds", 0)}
view_count: {metadata.get("view_count", 0)}
author: "{metadata.get("author", "Nate B Jones")}"

yt_tags:
{chr(10).join(f'  - "{tag}"' for tag in metadata.get("keywords", [])) or "  []"}

# AI-generated fields (to be enriched later)
content_type: null
primary_topic: null
audience: []
difficulty: null
entities:
  companies: []
  people: []
  products: []
  models: []
concepts: []
chapters: []
summary: []
---

# {metadata.get("title", "Unknown")}

{transcript["full_text"]}
'''

    output_file = episode_dir / "transcript.md"
    with open(output_file, "w") as f:
        f.write(yaml_content)

    return str(episode_dir)


def download_video(video_id, index, total):
    """Download a single video's transcript and metadata."""
    print(f"\n[{index}/{total}] Processing {video_id}...")

    # Get metadata first
    print("  Getting metadata...")
    metadata = get_video_metadata(video_id)
    if not metadata:
        metadata = {
            "video_id": video_id,
            "url": f"https://www.youtube.com/watch?v={video_id}",
        }

    # Small delay before transcript request
    time.sleep(random.uniform(1, 2))

    # Get transcript
    print("  Getting transcript...")
    transcript = get_transcript(video_id)

    # Save
    print(
        f"  Got {transcript['segment_count']} segments ({len(transcript['full_text'])} chars)"
    )
    output_path = save_transcript(metadata, transcript)
    print(f"  Saved to: {output_path}")

    return metadata.get("title", video_id)


def main():
    # Parse arguments
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    print("=== Nate B Jones Transcript Downloader (Supadata) ===")
    print(f"Rate limiting: {MIN_DELAY}-{MAX_DELAY}s between videos")
    print(
        f"Batch breaks: {BATCH_BREAK_MIN}-{BATCH_BREAK_MAX}s every {BATCH_SIZE} videos"
    )
    print(f"Limit: {limit} videos")
    print()

    # Load video IDs
    if not VIDEO_IDS_FILE.exists():
        print(f"ERROR: {VIDEO_IDS_FILE} not found. Run the bootstrap script first.")
        sys.exit(1)

    with open(VIDEO_IDS_FILE) as f:
        all_video_ids = [line.strip() for line in f if line.strip()]

    # Load progress
    progress = load_progress()
    completed = set(progress["completed"])

    # Filter to remaining videos
    remaining = [vid for vid in all_video_ids if vid not in completed]
    to_process = remaining[:limit]

    print(f"Total videos: {len(all_video_ids)}")
    print(f"Already completed: {len(completed)}")
    print(f"Remaining: {len(remaining)}")
    print(f"Processing this run: {len(to_process)}")
    print()

    if not to_process:
        print("Nothing to process!")
        return

    # Process videos
    success_count = 0
    for i, video_id in enumerate(to_process, 1):
        try:
            download_video(video_id, i, len(to_process))

            progress["completed"].append(video_id)
            save_progress(progress)
            success_count += 1

            # Rate limiting
            if i < len(to_process):
                if i % BATCH_SIZE == 0:
                    break_time = random.uniform(BATCH_BREAK_MIN, BATCH_BREAK_MAX)
                    print(f"\n=== Batch break: {break_time:.0f}s ===")
                    time.sleep(break_time)
                else:
                    delay = random.uniform(MIN_DELAY, MAX_DELAY)
                    print(f"  Waiting {delay:.1f}s...")
                    time.sleep(delay)

        except Exception as e:
            error_msg = str(e)
            print(f"  ERROR: {error_msg}")

            if "RATE_LIMITED" in error_msg:
                print("\n!!! RATE LIMITED - STOPPING IMMEDIATELY !!!")
                print("Wait before trying again.")
                progress["failed"].append(
                    {
                        "id": video_id,
                        "reason": error_msg,
                        "time": datetime.now().isoformat(),
                    }
                )
                save_progress(progress)
                break
            else:
                progress["failed"].append(
                    {
                        "id": video_id,
                        "reason": error_msg,
                        "time": datetime.now().isoformat(),
                    }
                )
                save_progress(progress)

    print("\n=== Complete ===")
    print(f"Successfully downloaded: {success_count}")
    print(f"Total completed: {len(progress['completed'])}")
    print(f"Failed: {len(progress['failed'])}")


if __name__ == "__main__":
    main()
