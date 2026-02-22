#!/usr/bin/env python3
"""
Build topic index for Nate B Jones transcripts.
Creates index/ folder with topic-specific markdown files.
"""

import yaml
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EPISODES_DIR = BASE_DIR / "episodes"
INDEX_DIR = BASE_DIR / "index"

# Topic keywords mapping - maps keywords to canonical topic names
TOPIC_KEYWORDS = {
    "AI Agents": [
        "agent",
        "agents",
        "agentic",
        "autonomous",
        "automation",
        "multi-agent",
    ],
    "AI Strategy": [
        "strategy",
        "strategic",
        "enterprise",
        "business strategy",
        "adoption",
        "implementation",
    ],
    "AI Tools": ["tool", "tools", "cursor", "chatgpt", "claude", "copilot", "software"],
    "Prompting": [
        "prompt",
        "prompting",
        "prompt engineering",
        "chain of thought",
        "few-shot",
    ],
    "AI News": ["news", "announcement", "launch", "release", "update", "breaking"],
    "Career": ["job", "career", "hiring", "interview", "resume", "skills", "salary"],
    "Product Management": ["product", "pm", "product manager", "roadmap", "feature"],
    "Startups": ["startup", "founder", "entrepreneur", "founding", "venture"],
    "Leadership": ["leader", "leadership", "executive", "ceo", "cto", "manager"],
    "OpenAI": ["openai", "chatgpt", "gpt-4", "gpt-5", "sam altman", "o1", "o3"],
    "Anthropic": ["anthropic", "claude", "dario amodei", "sonnet", "opus", "haiku"],
    "Google": ["google", "gemini", "deepmind", "sundar pichai", "bard"],
    "Microsoft": ["microsoft", "copilot", "satya nadella", "azure", "bing"],
    "Meta": ["meta", "facebook", "llama", "mark zuckerberg", "instagram"],
    "Coding": [
        "code",
        "coding",
        "programming",
        "developer",
        "engineer",
        "cursor",
        "copilot",
    ],
    "Workflows": ["workflow", "automation", "process", "efficiency", "productivity"],
    "Frameworks": ["framework", "model", "mental model", "principles", "system"],
    "Deep Dives": ["deep dive", "breakdown", "explained", "analysis"],
    "Tutorials": ["how to", "tutorial", "guide", "demo", "walkthrough"],
}


def extract_keywords(title, text, entities):
    """Extract keywords from transcript content."""
    keywords = set()
    title_lower = title.lower()
    text_lower = text.lower()[:5000]

    # Add from topic mapping
    for topic, terms in TOPIC_KEYWORDS.items():
        for term in terms:
            if term.lower() in title_lower or term.lower() in text_lower:
                keywords.add(topic.lower().replace(" ", "-"))
                break

    # Add company entities as keywords
    if entities and isinstance(entities, dict):
        for company in entities.get("companies", []) or []:
            keywords.add(company.lower().replace(" ", "-"))
        for product in entities.get("products", []) or []:
            keywords.add(product.lower().replace(" ", "-"))

    return sorted(list(keywords))


def get_topics_for_episode(keywords, entities, content_type, primary_topic):
    """Determine which topic index files this episode should appear in."""
    topics = set()

    # Add primary topic
    if primary_topic:
        topics.add(primary_topic.lower().replace(" ", "-"))

    # Add content type
    if content_type:
        topics.add(content_type.lower().replace(" ", "-"))

    # Add from keywords
    for kw in keywords:
        topics.add(kw)

    # Add company topics
    if entities and isinstance(entities, dict):
        for company in entities.get("companies", []) or []:
            company_lower = company.lower()
            if company_lower in [
                "openai",
                "anthropic",
                "google",
                "microsoft",
                "meta",
                "nvidia",
            ]:
                topics.add(company_lower)

    return topics


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    try:
        data = yaml.safe_load(parts[1]) or {}
        return data, parts[2]
    except yaml.YAMLError:
        return {}, content


def update_frontmatter(file_path, new_fields):
    """Update frontmatter with new fields."""
    content = file_path.read_text()
    if not content.startswith("---"):
        return

    parts = content.split("---", 2)
    if len(parts) < 3:
        return

    yaml_str = parts[1]

    # Check if keywords already exist
    if "keywords:" in yaml_str:
        return  # Already has keywords

    # Add keywords before the closing ---
    keywords_yaml = "keywords:\n" + "\n".join(
        f'  - "{k}"' for k in new_fields.get("keywords", [])
    )

    new_yaml = yaml_str.rstrip() + "\n" + keywords_yaml
    new_content = f"---{new_yaml}\n---{parts[2]}"

    file_path.write_text(new_content)


def main():
    print("=== Building Topic Index ===")

    # Create index directory
    INDEX_DIR.mkdir(exist_ok=True)

    # Collect all episodes and their topics
    topic_episodes = defaultdict(list)
    all_episodes = []

    for episode_dir in sorted(EPISODES_DIR.iterdir()):
        if not episode_dir.is_dir() or episode_dir.name.startswith("."):
            continue

        transcript_file = episode_dir / "transcript.md"
        if not transcript_file.exists():
            continue

        content = transcript_file.read_text()
        metadata, transcript_text = parse_frontmatter(content)

        if not metadata.get("title"):
            continue

        # Extract keywords if not present
        keywords = metadata.get("keywords", [])
        if not keywords:
            keywords = extract_keywords(
                metadata.get("title", ""), transcript_text, metadata.get("entities", {})
            )
            # Update the file with keywords
            update_frontmatter(transcript_file, {"keywords": keywords})
            metadata["keywords"] = keywords

        # Get topics for this episode
        topics = get_topics_for_episode(
            keywords,
            metadata.get("entities", {}),
            metadata.get("content_type", ""),
            metadata.get("primary_topic", ""),
        )

        episode_info = {
            "title": metadata.get("title", ""),
            "folder": episode_dir.name,
            "date": metadata.get("publish_date", ""),
            "duration": metadata.get("duration", ""),
        }

        all_episodes.append(episode_info)

        for topic in topics:
            topic_episodes[topic].append(episode_info)

    print(f"Processed {len(all_episodes)} episodes")
    print(f"Found {len(topic_episodes)} topics")

    # Create topic index files
    for topic, episodes in sorted(topic_episodes.items()):
        topic_file = INDEX_DIR / f"{topic}.md"

        # Sort episodes by date (newest first)
        episodes_sorted = sorted(
            episodes, key=lambda x: x.get("date", ""), reverse=True
        )

        lines = [
            f"# {topic.replace('-', ' ').title()}",
            "",
            f"Episodes discussing **{topic.replace('-', ' ').title()}** ({len(episodes)} episodes):",
            "",
        ]

        for ep in episodes_sorted:
            date_str = f" ({ep['date']})" if ep.get("date") else ""
            lines.append(
                f"- [{ep['title']}](../episodes/{ep['folder']}/transcript.md){date_str}"
            )

        topic_file.write_text("\n".join(lines) + "\n")

    # Create index README
    readme_lines = [
        "# Nate B Jones Podcast Index",
        "",
        f"Index of {len(all_episodes)} episodes across {len(topic_episodes)} topics.",
        "",
        "## Topics",
        "",
    ]

    # Sort topics by episode count
    sorted_topics = sorted(
        topic_episodes.items(), key=lambda x: len(x[1]), reverse=True
    )

    for topic, episodes in sorted_topics:
        topic_title = topic.replace("-", " ").title()
        readme_lines.append(f"- [{topic_title}]({topic}.md) ({len(episodes)} episodes)")

    readme_lines.extend(
        [
            "",
            "## Search",
            "",
            "```bash",
            "# Search all transcripts",
            'grep -r "your search term" ../episodes/',
            "```",
        ]
    )

    (INDEX_DIR / "README.md").write_text("\n".join(readme_lines) + "\n")

    print(f"\nCreated {len(topic_episodes)} topic files in index/")
    print("Created index/README.md")


if __name__ == "__main__":
    main()
