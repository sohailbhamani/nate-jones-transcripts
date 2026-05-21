#!/usr/bin/env python3
"""
Discover new Nate B Jones videos via YouTube Data API v3.

Replaces the prior RSS-based discovery, which started 404/500ing for most
channels as YouTube tightened its RSS surface. Uses the channel's uploads
playlist (UU<channel_id_suffix>) — the conventional playlist that
contains every public upload in chronological order — and reads up to
50 most-recent videos per run.

Auth: prefers OAuth refresh-token (YOUTUBE_REFRESH_TOKEN +
YOUTUBE_CLIENT_ID + YOUTUBE_CLIENT_SECRET). Falls back to YOUTUBE_API_KEY
if OAuth isn't configured. The API key path is preserved so older setups
keep working, but it's IP-restricted and fails from GitHub Actions
runners — OAuth is the supported path.

Quota cost: 1 unit per run (playlistItems.list = 1 unit). Negligible
against the 10,000 unit daily quota.
"""

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CHANNEL_ID = "UC0C-17n9iuUQPylguM1d-lQ"
UPLOADS_PLAYLIST = "UU" + CHANNEL_ID[2:]

BASE_DIR = Path(__file__).parent.parent
VIDEO_IDS_FILE = BASE_DIR / "video_ids.txt"

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")
YOUTUBE_REFRESH_TOKEN = os.environ.get("YOUTUBE_REFRESH_TOKEN", "")
YOUTUBE_CLIENT_ID = os.environ.get("YOUTUBE_CLIENT_ID", "")
YOUTUBE_CLIENT_SECRET = os.environ.get("YOUTUBE_CLIENT_SECRET", "")


def _get_oauth_access_token():
    """Exchange refresh token for a short-lived access token. Returns None if OAuth env not set."""
    if not (YOUTUBE_REFRESH_TOKEN and YOUTUBE_CLIENT_ID and YOUTUBE_CLIENT_SECRET):
        return None
    body = urllib.parse.urlencode(
        {
            "client_id": YOUTUBE_CLIENT_ID,
            "client_secret": YOUTUBE_CLIENT_SECRET,
            "refresh_token": YOUTUBE_REFRESH_TOKEN,
            "grant_type": "refresh_token",
        }
    ).encode()
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read()).get("access_token")
    except Exception as e:
        print(f"  Warning: OAuth token exchange failed: {e}")
        return None


def fetch_recent_video_ids(max_results=50, retries=3, backoff=5):
    """Hit playlistItems.list on the channel's uploads playlist, retrying transient failures."""
    oauth_token = _get_oauth_access_token()
    if not (oauth_token or YOUTUBE_API_KEY):
        raise RuntimeError(
            "No YouTube auth configured. Set OAuth (YOUTUBE_REFRESH_TOKEN + "
            "YOUTUBE_CLIENT_ID + YOUTUBE_CLIENT_SECRET) or YOUTUBE_API_KEY."
        )

    if oauth_token:
        qs = urllib.parse.urlencode(
            {
                "part": "contentDetails",
                "playlistId": UPLOADS_PLAYLIST,
                "maxResults": max_results,
            }
        )
        headers = {"Authorization": f"Bearer {oauth_token}"}
    else:
        qs = urllib.parse.urlencode(
            {
                "part": "contentDetails",
                "playlistId": UPLOADS_PLAYLIST,
                "maxResults": max_results,
                "key": YOUTUBE_API_KEY,
            }
        )
        headers = {}
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?{qs}"

    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
            return [
                item["contentDetails"]["videoId"]
                for item in data.get("items", [])
                if item.get("contentDetails", {}).get("videoId")
            ]
        except urllib.error.HTTPError as e:
            last_err = e
            if attempt < retries and (e.code in (429,) or 500 <= e.code < 600):
                wait = backoff * attempt
                print(f"  Attempt {attempt} HTTP {e.code}: {e}. Retrying in {wait}s...")
                time.sleep(wait)
                continue
            break
        except Exception as e:
            last_err = e
            if attempt < retries:
                wait = backoff * attempt
                print(f"  Attempt {attempt} error: {e}. Retrying in {wait}s...")
                time.sleep(wait)
                continue
    raise RuntimeError(f"YouTube API failed after {retries} attempts: {last_err}")


def load_existing_ids():
    if not VIDEO_IDS_FILE.exists():
        return set()
    with open(VIDEO_IDS_FILE) as f:
        return {line.strip() for line in f if line.strip()}


def main():
    print("=== Nate B Jones Video Discovery (YouTube Data API v3) ===")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Uploads playlist: {UPLOADS_PLAYLIST}")

    existing = load_existing_ids()
    print(f"Existing videos: {len(existing)}")

    api_ids = fetch_recent_video_ids()
    print(f"Videos from API: {len(api_ids)}")

    new_ids = [vid for vid in api_ids if vid not in existing]
    if not new_ids:
        print("No new videos found.")
        return

    print(f"New videos found: {len(new_ids)}")
    for vid in new_ids:
        print(f"  + {vid}")

    with open(VIDEO_IDS_FILE, "a") as f:
        for vid in new_ids:
            f.write(f"{vid}\n")

    print(f"Appended {len(new_ids)} new video IDs to {VIDEO_IDS_FILE}")


if __name__ == "__main__":
    main()
