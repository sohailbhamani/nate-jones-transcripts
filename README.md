# Nate B Jones Transcripts

Transcript archive of [Nate B Jones](https://www.youtube.com/@NateBJones) YouTube videos.

## Stats

- **Videos Downloaded**: 446
- **Date Range**: May 21, 2024 - Feb 21, 2026
- **Sync**: Automated via GitHub Actions (midnight + noon CST)
- **Last Updated**: Feb 27, 2026

## Structure

```
nate-jones-transcripts/
├── README.md
├── index.json                    # Master index of all videos
├── video_ids.txt                 # All video IDs (one per line)
├── .github/
│   ├── CODEOWNERS                # Require owner review on PRs
│   └── workflows/
│       ├── daily-sync.yml        # Automated transcript pipeline (2x daily)
│       └── lint.yml              # Ruff lint check on PRs
├── index/                        # Topic-based index
│   ├── README.md                 # All topics with episode counts
│   └── ...                       # Topic files
├── episodes/
│   └── YYYY-MM-DD-video-title/
│       └── transcript.md         # YAML frontmatter + full transcript
└── scripts/
    ├── discover.py               # RSS-based new video discovery
    ├── download.py               # Download transcripts (Supadata API)
    ├── enrich.py                 # AI enrichment (entities, topics, etc.)
    ├── create_index.py           # Generates index.json
    ├── build_index.py            # Builds topic index files
    └── update_readme.py          # Updates README stats
```

## Transcript Format

Each `transcript.md` contains:

```yaml
---
title: "Video Title"
video_id: "abc123"
youtube_url: "https://www.youtube.com/watch?v=abc123"
publish_date: "2026-01-14"
duration: "32:18"
duration_seconds: 1938
view_count: 10000
author: "Nate B Jones"

yt_tags:
  - "AI"
  - "Product Management"

# AI-enriched metadata
content_type: "Deep Dive"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Product Managers"
entities:
  companies:
    - "OpenAI"
  people:
    - "Sam Altman"
  products:
    - "ChatGPT"
  models:
    - "GPT-4"
concepts:
  - "Key insight extracted from transcript"
summary:
  - "First key point"
  - "Second key point"
---

# Video Title

[Full transcript text here]
```

## Topic Index

Browse episodes by topic via the [`index/`](index/) folder.

## Usage

### Search transcripts
```bash
grep -r "Claude Code" episodes/
```

### Use index.json
```python
import json
with open('index.json') as f:
    data = json.load(f)
for video in data['videos']:
    print(f"{video['publish_date']}: {video['title']}")
```

### Filter by enriched metadata
```python
# Find all deep dives for product managers
deep_dives = [v for v in data['videos']
              if v.get('content_type') == 'Deep Dive'
              and 'Product Managers' in v.get('audience', [])]

# Find videos mentioning OpenAI
openai_vids = [v for v in data['videos']
               if 'OpenAI' in v.get('entities', {}).get('companies', [])]
```

### Download more videos
```bash
# Set your Supadata API key
export SUPADATA_API_KEY="your_key_here"

# Download next batch
python scripts/download.py 100
```

## Attribution

This repo was bootstrapped from [kani3894/nate-jones-transcripts](https://github.com/kani3894/nate-jones-transcripts), which did the heavy lifting of archiving the first 431 episodes (May 2024 - Jan 2026). That repo hasn't been updated since January 2026, so we built this one to keep the archive current with automated daily sync and enrichment. Thank you to [@kani3894](https://github.com/kani3894) for building the original archive — without their work, this repo wouldn't exist.

## Credits

- Content by [Nate B Jones](https://www.youtube.com/@NateBJones) — subscribe to his channel if you find this useful
- Original transcript archive by [@kani3894](https://github.com/kani3894)
- Transcripts via [Supadata API](https://supadata.ai)
- Metadata via YouTube Data API v3
