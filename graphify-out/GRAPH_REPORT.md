# Graph Report - /mnt/data/dev/nate-jones-transcripts/.  (2026-04-10)

## Corpus Check
- Large corpus: 646 files · ~1,550,915 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 71 nodes · 91 edges · 14 communities detected
- Extraction: 69% EXTRACTED · 31% INFERRED · 0% AMBIGUOUS · INFERRED: 28 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `enrich_transcript()` - 10 edges
2. `download_video()` - 6 edges
3. `main()` - 5 edges
4. `main()` - 5 edges
5. `save_transcript()` - 4 edges
6. `main()` - 4 edges
7. `extract_keywords()` - 3 edges
8. `get_topics_for_episode()` - 3 edges
9. `parse_frontmatter()` - 3 edges
10. `update_frontmatter()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `enrich_transcript()` --calls--> `extract_entities()`  [INFERRED]
  /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py → /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py  _Bridges community 12 → community 5_
- `enrich_transcript()` --calls--> `classify_content_type()`  [INFERRED]
  /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py → /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py  _Bridges community 10 → community 5_
- `enrich_transcript()` --calls--> `classify_topic()`  [INFERRED]
  /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py → /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py  _Bridges community 9 → community 5_
- `enrich_transcript()` --calls--> `classify_difficulty()`  [INFERRED]
  /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py → /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py  _Bridges community 8 → community 5_
- `enrich_transcript()` --calls--> `classify_audience()`  [INFERRED]
  /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py → /mnt/data/dev/nate-jones-transcripts/scripts/enrich.py  _Bridges community 11 → community 5_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.18
Nodes (15): download_video(), get_transcript(), get_video_metadata(), load_progress(), main(), Get transcript using Supadata API., Save transcript in rich format with YAML frontmatter., Download a single video's transcript and metadata. (+7 more)

### Community 1 - "Community 1"
Cohesion: 0.29
Nodes (9): extract_keywords(), get_topics_for_episode(), main(), parse_frontmatter(), Parse YAML frontmatter from markdown content., Update frontmatter with new fields., Extract keywords from transcript content., Determine which topic index files this episode should appear in. (+1 more)

### Community 2 - "Community 2"
Cohesion: 0.29
Nodes (9): add_description(), extract_video_id(), get_descriptions_batch(), has_description(), main(), Fetch descriptions for up to 50 video IDs in one API call., Extract video_id from frontmatter., Check if frontmatter already has a description field. (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.47
Nodes (5): fetch_rss_video_ids(), load_existing_ids(), main(), Fetch recent video IDs from YouTube RSS feed, with retries., Load existing video IDs from file.

### Community 4 - "Community 4"
Cohesion: 0.6
Nodes (4): fix_repo(), get_yt_metadata(), Get YouTube video metadata. Returns None if API fails., slugify()

### Community 5 - "Community 5"
Cohesion: 0.5
Nodes (4): enrich_transcript(), extract_concepts(), Extract key concepts from text., Enrich a single transcript file.

### Community 6 - "Community 6"
Cohesion: 0.5
Nodes (3): generate_summary(), main(), Generate bullet point summary.

### Community 7 - "Community 7"
Cohesion: 0.67
Nodes (3): main(), parse_yaml_frontmatter(), Extract YAML frontmatter from markdown file.

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (2): classify_difficulty(), Classify difficulty level.

### Community 9 - "Community 9"
Cohesion: 1.0
Nodes (2): classify_topic(), Classify primary topic.

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (2): classify_content_type(), Classify content type based on title and text patterns.

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (2): classify_audience(), Determine target audience.

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (2): extract_entities(), Extract entities from text.

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (0):

## Knowledge Gaps
- **27 isolated node(s):** `Extract keywords from transcript content.`, `Determine which topic index files this episode should appear in.`, `Parse YAML frontmatter from markdown content.`, `Update frontmatter with new fields.`, `Load progress from file.` (+22 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 8`** (2 nodes): `classify_difficulty()`, `Classify difficulty level.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 9`** (2 nodes): `classify_topic()`, `Classify primary topic.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (2 nodes): `classify_content_type()`, `Classify content type based on title and text patterns.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (2 nodes): `classify_audience()`, `Determine target audience.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (2 nodes): `extract_entities()`, `Extract entities from text.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `update_readme.py`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `enrich_transcript()` connect `Community 5` to `Community 6`, `Community 8`, `Community 9`, `Community 10`, `Community 11`, `Community 12`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `enrich_transcript()` (e.g. with `extract_entities()` and `classify_content_type()`) actually correct?**
  _`enrich_transcript()` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `download_video()` (e.g. with `get_video_metadata()` and `get_transcript()`) actually correct?**
  _`download_video()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `main()` (e.g. with `parse_frontmatter()` and `extract_keywords()`) actually correct?**
  _`main()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `main()` (e.g. with `has_description()` and `extract_video_id()`) actually correct?**
  _`main()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `save_transcript()` (e.g. with `slugify()` and `download_video()`) actually correct?**
  _`save_transcript()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Extract keywords from transcript content.`, `Determine which topic index files this episode should appear in.`, `Parse YAML frontmatter from markdown content.` to the rest of the system?**
  _27 weakly-connected nodes found - possible documentation gaps or missing edges._
