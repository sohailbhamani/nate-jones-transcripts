#!/usr/bin/env python3
"""
fix_unknown_episodes.py
Renames unknown-* episode dirs to proper YYYY-MM-DD-slug format
using YouTube Data API v3 for metadata.

Auth: prefers OAuth (YOUTUBE_REFRESH_TOKEN + YOUTUBE_CLIENT_ID +
YOUTUBE_CLIENT_SECRET) because the long-lived API key is IP-restricted
and fails from GitHub Actions runners. Falls back to YOUTUBE_API_KEY
if OAuth is not configured.

Usage: doppler run --project moltbot --config dev -- python fix_unknown_episodes.py <repo_dir>
"""

import os
import re
import sys
import time
import requests
from pathlib import Path

_access_token_cache = {"token": None, "expires_at": 0}


def _get_oauth_access_token():
    """Refresh-token -> access-token exchange, cached until ~5s before expiry."""
    refresh = os.environ.get("YOUTUBE_REFRESH_TOKEN", "")
    cid = os.environ.get("YOUTUBE_CLIENT_ID", "")
    cs = os.environ.get("YOUTUBE_CLIENT_SECRET", "")
    if not (refresh and cid and cs):
        return None

    now = time.time()
    if _access_token_cache["token"] and _access_token_cache["expires_at"] - 5 > now:
        return _access_token_cache["token"]

    try:
        r = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": cid,
                "client_secret": cs,
                "refresh_token": refresh,
                "grant_type": "refresh_token",
            },
            timeout=15,
        )
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(f"  Warning: OAuth token exchange failed: {e}")
        return None

    _access_token_cache["token"] = data["access_token"]
    _access_token_cache["expires_at"] = now + int(data.get("expires_in", 3600))
    return _access_token_cache["token"]


def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:60]


def _oembed(video_id):
    """Quotaless title + author from YouTube oEmbed. No publish_date."""
    try:
        r = requests.get(
            "https://www.youtube.com/oembed",
            params={
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "format": "json",
            },
            timeout=10,
        )
        r.raise_for_status()
        data = r.json()
        return {
            "title": data.get("title", ""),
            "channel": data.get("author_name", ""),
        }
    except Exception:
        return None


def get_yt_metadata(video_id, api_key, max_retries=3):
    """YouTube Data API with retry + oEmbed fallback.

    Previously: single API call, any failure → unknown-<id> dir forever.
    Now: retries transient failures (quota 403, rate 429, 5xx) with backoff,
    then falls back to oEmbed so at least the title is recovered.
    """
    last_err = None
    oauth_token = _get_oauth_access_token()
    if oauth_token or api_key:
        url = "https://www.googleapis.com/youtube/v3/videos"
        if oauth_token:
            params = {"part": "snippet", "id": video_id}
            headers = {"Authorization": f"Bearer {oauth_token}"}
        else:
            params = {"part": "snippet", "id": video_id, "key": api_key}
            headers = {}
        for attempt in range(max_retries):
            try:
                r = requests.get(url, params=params, headers=headers, timeout=10)
                r.raise_for_status()
                items = r.json().get("items", [])
                if not items:
                    break  # video may be unlisted/age-gated — try oEmbed
                snippet = items[0]["snippet"]
                return {
                    "title": snippet["title"],
                    "publish_date": snippet["publishedAt"][:10],
                    "channel": snippet["channelTitle"],
                    "tags": snippet.get("tags", []),
                }
            except requests.exceptions.HTTPError as e:
                last_err = e
                code = e.response.status_code if e.response is not None else 0
                if code in (403, 429) or 500 <= code < 600:
                    wait = (2**attempt) + 0.5
                    print(
                        f"  API {code} on {video_id}, retry {attempt + 1}/{max_retries} in {wait}s"
                    )
                    time.sleep(wait)
                    continue
                break
            except requests.exceptions.RequestException as e:
                last_err = e
                wait = (2**attempt) + 0.5
                print(
                    f"  API error on {video_id}: {e}, retry {attempt + 1}/{max_retries} in {wait}s"
                )
                time.sleep(wait)
                continue
        if last_err is not None:
            print(f"  YouTube API exhausted for {video_id}: {last_err}")

    oe = _oembed(video_id)
    if oe and oe.get("title"):
        print(f"  oEmbed fallback for {video_id}: '{oe['title']}'")
        return {
            "title": oe["title"],
            "publish_date": "",
            "channel": oe.get("channel", ""),
            "tags": [],
        }

    print(f"  SKIP {video_id}: API + oEmbed both failed")
    return None


def fix_repo(repo_dir, api_key):
    episodes_dir = Path(repo_dir) / "episodes"
    unknowns = sorted(
        [d for d in episodes_dir.iterdir() if d.name.startswith("unknown-")]
    )
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
        date = meta.get("publish_date") or "undated"
        slug = slugify(title)
        new_name = f"{date}-{slug}"
        new_dir = episodes_dir / new_name

        # Update frontmatter in transcript.md
        content = re.sub(
            r'title:\s*"Unknown"',
            f'title: "{title.replace(chr(34), chr(39))}"',
            content,
        )
        if meta.get("publish_date"):
            content = re.sub(
                r'publish_date:\s*"unknown"', f'publish_date: "{date}"', content
            )
        if meta.get("channel"):
            content = re.sub(
                r'author:\s*"[^"]*"', f'author: "{meta["channel"]}"', content
            )
        md.write_text(content)

        # Rename directory, or delete unknown-* if it's a duplicate of an existing named dir.
        if new_dir.exists():
            named_md = new_dir / "transcript.md"
            if named_md.exists() and named_md.stat().st_size > 100:
                # Named version already has content — unknown-* is stale residue.
                import shutil

                shutil.rmtree(ep_dir)
                print(f"  DELETED {ep_dir.name} (duplicate of existing {new_name})")
            else:
                print(
                    f"  CONFLICT {new_name} exists but has no transcript, manual review"
                )
        else:
            ep_dir.rename(new_dir)
            print(f"  FIXED {ep_dir.name} -> {new_name}")

        time.sleep(0.3)

    print("Done.")


if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    api_key = os.environ.get("YOUTUBE_API_KEY", "")
    has_oauth = all(
        os.environ.get(k)
        for k in ("YOUTUBE_REFRESH_TOKEN", "YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET")
    )
    if not (api_key or has_oauth):
        print(
            "ERROR: need YOUTUBE_API_KEY or full OAuth set "
            "(YOUTUBE_REFRESH_TOKEN + YOUTUBE_CLIENT_ID + YOUTUBE_CLIENT_SECRET)"
        )
        sys.exit(1)
    fix_repo(repo, api_key)
