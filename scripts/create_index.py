#!/usr/bin/env python3
"""Create index.json from all downloaded transcripts."""

import json

import yaml
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EPISODES_DIR = BASE_DIR / "episodes"
INDEX_FILE = BASE_DIR / "index.json"


def parse_yaml_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    if not content.startswith("---"):
        return {}

    # Find end of frontmatter
    end_match = content.find("\n---", 3)
    if end_match == -1:
        return {}

    yaml_content = content[4:end_match]

    try:
        return yaml.safe_load(yaml_content) or {}
    except yaml.YAMLError:
        return {}


def derive_from_folder(folder_name):
    """Derive publish_date and title from folder name like '2025-06-21-should-you-learn-to-code'."""
    parts = folder_name.split("-", 3)
    if len(parts) >= 4 and len(parts[0]) == 4:
        date = f"{parts[0]}-{parts[1]}-{parts[2]}"
        title = parts[3].replace("-", " ").title()
        return date, title
    return None, folder_name.replace("-", " ").title()


def main():
    videos = []
    skipped = 0

    for episode_dir in sorted(EPISODES_DIR.iterdir()):
        if not episode_dir.is_dir() or episode_dir.name.startswith("."):
            continue

        transcript_file = episode_dir / "transcript.md"
        if not transcript_file.exists():
            continue

        content = transcript_file.read_text()
        metadata = parse_yaml_frontmatter(content)

        # Derive missing fields from folder name
        folder_date, folder_title = derive_from_folder(episode_dir.name)
        if not metadata.get("title") and folder_title:
            metadata["title"] = folder_title
        if not metadata.get("publish_date") and folder_date:
            metadata["publish_date"] = folder_date

        # Get transcript length
        transcript_start = content.find("\n---", 3)
        if transcript_start != -1:
            transcript_text = content[transcript_start + 4 :].strip()
            # Skip the title line
            if transcript_text.startswith("#"):
                transcript_text = (
                    transcript_text.split("\n", 1)[1] if "\n" in transcript_text else ""
                )
            metadata["transcript_chars"] = len(transcript_text)

        metadata["folder"] = episode_dir.name

        # Skip entries with no usable data or unresolved metadata
        if not metadata.get("video_id"):
            skipped += 1
            print(f"  Skipped (no video_id): {episode_dir.name}")
            continue
        if metadata.get("publish_date") == "unknown" or metadata.get("title") == "Unknown":
            skipped += 1
            print(f"  Skipped (unresolved metadata): {episode_dir.name}")
            continue

        videos.append(metadata)

    # Sort by publish date (newest first), entries without dates go last
    videos.sort(key=lambda x: x.get("publish_date") or "0000-00-00", reverse=True)

    index = {
        "total_videos": len(videos),
        "date_range": {
            "newest": videos[0].get("publish_date") if videos else None,
            "oldest": videos[-1].get("publish_date") if videos else None,
        },
        "videos": videos,
    }

    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)

    print(f"Created index.json with {len(videos)} videos ({skipped} skipped)")
    print(f"Date range: {index['date_range']['oldest']} to {index['date_range']['newest']}")


if __name__ == "__main__":
    main()
