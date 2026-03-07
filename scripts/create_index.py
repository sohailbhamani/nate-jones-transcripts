#!/usr/bin/env python3
"""
Build index.json from episode transcript.md files (YAML frontmatter).
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EPISODES_DIR = BASE_DIR / "episodes"
INDEX_FILE = BASE_DIR / "index.json"


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}
    
    yaml_text = match.group(1)
    data = {}
    
    # Simple YAML parsing for basic fields
    for line in yaml_text.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value and value != 'null':
                data[key] = value
    
    return data


def build_index():
    """Build index from transcript.md files."""
    episodes = []
    
    for ep_dir in EPISODES_DIR.iterdir():
        if not ep_dir.is_dir():
            continue
            
        transcript_file = ep_dir / "transcript.md"
        if not transcript_file.exists():
            continue
        
        try:
            content = transcript_file.read_text()
            metadata = parse_frontmatter(content)
            
            if metadata.get('video_id'):
                episodes.append({
                    'video_id': metadata.get('video_id'),
                    'title': metadata.get('title', 'Unknown'),
                    'published': metadata.get('publish_date', 'unknown'),
                    'url': metadata.get('youtube_url', ''),
                    'duration': metadata.get('duration', 'unknown'),
                    'view_count': metadata.get('view_count', 0),
                    'author': metadata.get('author', 'Nate B Jones'),
                })
        except Exception as e:
            print(f"Error parsing {ep_dir.name}: {e}")
            continue
    
    # Sort by published date
    episodes.sort(key=lambda x: x.get('published', ''), reverse=True)
    
    # Write index
    index_data = {
        'episodes': episodes,
        'count': len(episodes),
        'last_updated': str(Path.now()) if hasattr(Path, 'now') else 'unknown'
    }
    
    with open(INDEX_FILE, 'w') as f:
        json.dump(index_data, f, indent=2)
    
    print(f"Built index.json with {len(episodes)} episodes")
    if episodes:
        print(f"Latest: {episodes[0]['published']} - {episodes[0]['title'][:50]}")


if __name__ == "__main__":
    build_index()
