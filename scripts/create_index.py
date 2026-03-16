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


def main():
    videos = []

    for episode_dir in sorted(EPISODES_DIR.iterdir()):
        if not episode_dir.is_dir() or episode_dir.name.startswith("."):
            continue

        transcript_file = episode_dir / "transcript.md"
        if not transcript_file.exists():
            continue

        content = transcript_file.read_text()
        metadata = parse_yaml_frontmatter(content)

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
        videos.append(metadata)

    # Sort by publish date (newest first)
    videos.sort(key=lambda x: x.get("publish_date", ""), reverse=True)

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

    print(f"Created index.json with {len(videos)} videos")
    print(
        f"Date range: {index['date_range']['oldest']} to {index['date_range']['newest']}"
    )


if __name__ == "__main__":
    main()
