#!/usr/bin/env python3
"""
AI Enrichment script for Nate B Jones transcripts.
Extracts entities, classifies content, and generates summaries.
"""

import re
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EPISODES_DIR = BASE_DIR / "episodes"

# Known entities for extraction
COMPANIES = [
    "OpenAI",
    "Anthropic",
    "Google",
    "Meta",
    "Microsoft",
    "Amazon",
    "Apple",
    "Nvidia",
    "Tesla",
    "Shopify",
    "Salesforce",
    "Adobe",
    "Notion",
    "Slack",
    "GitHub",
    "Vercel",
    "Stripe",
    "Palantir",
    "Box",
    "Duolingo",
    "Fiverr",
    "DeepMind",
    "Hugging Face",
    "Mistral",
    "Cohere",
    "Perplexity",
    "Cursor",
    "Replit",
    "Zapier",
    "LinkedIn",
    "Twitter",
    "X",
    "YouTube",
    "Netflix",
    "Uber",
    "Airbnb",
    "Databricks",
    "Snowflake",
    "MongoDB",
    "Supabase",
    "AWS",
    "Azure",
    "GCP",
    "IBM",
    "Oracle",
    "SAP",
    "Atlassian",
    "Figma",
    "Canva",
    "Midjourney",
    "Stability AI",
    "Runway",
    "ElevenLabs",
    "Groq",
    "Together AI",
    "Weights & Biases",
    "LangChain",
    "LlamaIndex",
    "Pinecone",
    "Weaviate",
    "Milvus",
    "Chroma",
    "TSMC",
    "Intel",
    "AMD",
    "Qualcomm",
    "Browser Company",
    "Arc",
    "Tailwind",
    "Lovable",
    "Bolt",
    "v0",
]

PEOPLE = [
    "Sam Altman",
    "Dario Amodei",
    "Demis Hassabis",
    "Jensen Huang",
    "Satya Nadella",
    "Sundar Pichai",
    "Mark Zuckerberg",
    "Elon Musk",
    "Jeff Bezos",
    "Tim Cook",
    "Toby Lutke",
    "Andrej Karpathy",
    "Ilya Sutskever",
    "Greg Brockman",
    "Mira Murati",
    "Jan Leike",
    "Yann LeCun",
    "Geoffrey Hinton",
    "Fei-Fei Li",
    "Andrew Ng",
    "Emad Mostaque",
    "Arthur Mensch",
    "Aidan Gomez",
    "Nat Friedman",
    "Daniel Gross",
    "Alexandr Wang",
    "Connor Leahy",
    "Leopold Aschenbrenner",
    "Alex Finn",
    "Nate Jones",
    "Josh Miller",
    "Toby Look",
    "Aaron Levy",
]

PRODUCTS = [
    "ChatGPT",
    "GPT-4",
    "GPT-5",
    "Claude",
    "Claude Code",
    "Gemini",
    "Bard",
    "Copilot",
    "GitHub Copilot",
    "Cursor",
    "Codex",
    "DALL-E",
    "Midjourney",
    "Stable Diffusion",
    "Sora",
    "Runway",
    "Whisper",
    "Perplexity",
    "Notion AI",
    "Grammarly",
    "Jasper",
    "Copy.ai",
    "Writesonic",
    "AutoGPT",
    "AgentGPT",
    "BabyAGI",
    "LangChain",
    "LlamaIndex",
    "Hugging Face",
    "Ollama",
    "LM Studio",
    "Jan",
    "Msty",
    "Arc",
    "Raycast",
    "Alfred",
    "Keyboard Maestro",
    "Shortcuts",
    "Zapier",
    "Make",
    "n8n",
    "Pipedream",
    "IFTTT",
    "MCP",
    "Model Context Protocol",
    "Anthropic API",
    "OpenAI API",
    "Cowork",
    "Claude Cowork",
    "Opus",
    "Sonnet",
    "Haiku",
    "Atlas",
    "Operator",
    "Computer Use",
    "Artifacts",
    "Projects",
    "Nano Banana",
    "NanoBanana Pro",
    "Canvas",
    "o1",
    "o3",
]

MODELS = [
    "GPT-4",
    "GPT-4o",
    "GPT-4 Turbo",
    "GPT-5",
    "GPT-5.1",
    "GPT-5.2",
    "Claude 3",
    "Claude 3.5",
    "Claude 4",
    "Claude Opus",
    "Claude Sonnet",
    "Claude Haiku",
    "Opus 4.5",
    "Sonnet 4",
    "Gemini",
    "Gemini 2",
    "Gemini 3",
    "Gemini Pro",
    "Gemini Ultra",
    "Llama",
    "Llama 2",
    "Llama 3",
    "Llama 3.1",
    "Llama 3.2",
    "Mistral",
    "Mixtral",
    "Command R",
    "Command R+",
    "PaLM",
    "PaLM 2",
    "Chinchilla",
    "Gopher",
    "Falcon",
    "Phi",
    "Phi-2",
    "Phi-3",
    "Qwen",
    "Yi",
    "DeepSeek",
    "o1",
    "o1-mini",
    "o1-preview",
    "o3",
    "o3-mini",
    "SAM",
    "SAM 2",
    "SAM 3",
    "CLIP",
    "BLIP",
    "LLaVA",
    "Whisper",
    "Stable Diffusion",
    "SDXL",
    "Flux",
]

# Content type keywords
CONTENT_TYPE_PATTERNS = {
    "News Roundup": [
        "news",
        "this week",
        "roundup",
        "update",
        "headlines",
        "10 minute",
        "your .* minute",
    ],
    "Deep Dive": [
        "deep dive",
        "breakdown",
        "explained",
        "analysis",
        "why .* matters",
        "the real",
        "truth about",
    ],
    "Tutorial": [
        "how to",
        "tutorial",
        "guide",
        "step by step",
        "demo",
        "walkthrough",
        "build",
        "create",
    ],
    "Framework": [
        "framework",
        "principles",
        "rules",
        "model",
        "mental model",
        "system",
        "approach",
    ],
    "Opinion": [
        "my take",
        "i think",
        "unpopular opinion",
        "hot take",
        "prediction",
        "forecast",
    ],
    "Case Study": [
        "case study",
        "example",
        "real world",
        "how .* uses",
        "inside look",
        "behind the scenes",
    ],
}

# Topic keywords
TOPIC_PATTERNS = {
    "AI Agents": [
        "agent",
        "agents",
        "autonomous",
        "automation",
        "agentic",
        "multi-agent",
    ],
    "AI Strategy": [
        "strategy",
        "strategic",
        "enterprise",
        "business",
        "roi",
        "implementation",
        "adoption",
    ],
    "AI Tools": [
        "tool",
        "tools",
        "cursor",
        "chatgpt",
        "claude",
        "copilot",
        "software",
        "app",
    ],
    "Career": [
        "job",
        "career",
        "hiring",
        "interview",
        "resume",
        "skills",
        "salary",
        "work",
    ],
    "Prompting": [
        "prompt",
        "prompting",
        "prompt engineering",
        "chain of thought",
        "few-shot",
    ],
    "AI News": ["news", "announcement", "launch", "release", "update", "breaking"],
}

# Difficulty indicators
DIFFICULTY_PATTERNS = {
    "Beginner": [
        "beginner",
        "intro",
        "basics",
        "getting started",
        "first",
        "simple",
        "easy",
    ],
    "Intermediate": ["intermediate", "next level", "improve", "better", "optimize"],
    "Advanced": [
        "advanced",
        "expert",
        "deep",
        "technical",
        "architecture",
        "implementation",
    ],
}


def extract_entities(text, entity_list):
    """Extract entities from text."""
    found = []
    text_lower = text.lower()
    for entity in entity_list:
        # Create pattern that matches whole word
        pattern = r"\b" + re.escape(entity.lower()) + r"\b"
        if re.search(pattern, text_lower):
            found.append(entity)
    return found


def classify_content_type(title, text):
    """Classify content type based on title and text patterns."""
    title_lower = title.lower()
    text_lower = text.lower()[:2000]  # Check first 2000 chars

    scores = Counter()
    for content_type, patterns in CONTENT_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, title_lower) or re.search(pattern, text_lower):
                scores[content_type] += 1

    if scores:
        return scores.most_common(1)[0][0]
    return "Deep Dive"  # Default


def classify_topic(title, text):
    """Classify primary topic."""
    title_lower = title.lower()
    text_lower = text.lower()[:3000]

    scores = Counter()
    for topic, patterns in TOPIC_PATTERNS.items():
        for pattern in patterns:
            count = len(re.findall(r"\b" + pattern + r"\b", title_lower))
            count += len(re.findall(r"\b" + pattern + r"\b", text_lower)) // 5
            if count > 0:
                scores[topic] += count

    if scores:
        return scores.most_common(1)[0][0]
    return "AI Strategy"  # Default


def classify_difficulty(title, text):
    """Classify difficulty level."""
    title_lower = title.lower()
    text_lower = text.lower()[:2000]

    for difficulty, patterns in DIFFICULTY_PATTERNS.items():
        for pattern in patterns:
            if re.search(r"\b" + pattern + r"\b", title_lower):
                return difficulty

    # Default based on content complexity
    if any(
        word in text_lower
        for word in ["architecture", "implementation", "system design", "production"]
    ):
        return "Advanced"
    elif any(
        word in text_lower for word in ["getting started", "basics", "introduction"]
    ):
        return "Beginner"
    return "Intermediate"


def classify_audience(title, text):
    """Determine target audience."""
    audiences = []
    text_lower = text.lower()

    if any(
        word in text_lower
        for word in ["engineer", "developer", "code", "programming", "technical"]
    ):
        audiences.append("Engineers")
    if any(
        word in text_lower
        for word in ["executive", "ceo", "cto", "leader", "manager", "business"]
    ):
        audiences.append("Executives")
    if any(word in text_lower for word in ["product", "pm", "product manager"]):
        audiences.append("Product Managers")
    if any(word in text_lower for word in ["founder", "startup", "entrepreneur"]):
        audiences.append("Founders")

    return audiences if audiences else ["General"]


def extract_concepts(text):
    """Extract key concepts from text."""
    concepts = []
    text_lower = text.lower()

    concept_patterns = [
        r"the key (?:insight|takeaway|point) is (.*?)[.\n]",
        r"this means (.*?)[.\n]",
        r"the (?:main|core|central) (?:idea|concept|point) is (.*?)[.\n]",
        r"(?:importantly|crucially|fundamentally)[,]? (.*?)[.\n]",
    ]

    for pattern in concept_patterns:
        matches = re.findall(pattern, text_lower)
        for match in matches[:2]:
            if len(match) > 20 and len(match) < 200:
                concepts.append(match.strip().capitalize())

    return concepts[:5]


def generate_summary(title, text):
    """Generate bullet point summary."""
    summary = []

    # Extract first substantive sentence
    sentences = re.split(r"[.!?]+", text)
    for sent in sentences[:10]:
        sent = sent.strip()
        if len(sent) > 50 and len(sent) < 300:
            summary.append(sent[:200])
            break

    # Look for key phrases
    key_patterns = [
        r"the (?:key|main|important) thing is (.*?)[.\n]",
        r"what this means is (.*?)[.\n]",
        r"the takeaway is (.*?)[.\n]",
    ]

    for pattern in key_patterns:
        matches = re.findall(pattern, text.lower())
        for match in matches[:1]:
            if len(match) > 30:
                summary.append(match.strip().capitalize()[:200])

    return summary[:3]


def enrich_transcript(file_path):
    """Enrich a single transcript file."""
    content = file_path.read_text()

    # Split frontmatter and transcript
    if not content.startswith("---"):
        return None

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None

    frontmatter = parts[1]
    transcript_text = parts[2].strip()

    # Extract title
    title_match = re.search(r'^title:\s*"(.+)"', frontmatter, re.MULTILINE)
    title = title_match.group(1) if title_match else ""

    # Extract entities
    full_text = title + " " + transcript_text
    companies = extract_entities(full_text, COMPANIES)
    people = extract_entities(full_text, PEOPLE)
    products = extract_entities(full_text, PRODUCTS)
    models = extract_entities(full_text, MODELS)

    # Classify
    content_type = classify_content_type(title, transcript_text)
    primary_topic = classify_topic(title, transcript_text)
    difficulty = classify_difficulty(title, transcript_text)
    audience = classify_audience(title, transcript_text)

    # Extract concepts and summary
    concepts = extract_concepts(transcript_text)
    summary = generate_summary(title, transcript_text)

    # Build new frontmatter
    new_frontmatter = frontmatter.rstrip()

    # Remove all AI-generated/enriched fields (both old and new block markers)
    new_frontmatter = re.sub(
        r"\n# AI-(generated fields|enriched metadata).*",
        "",
        new_frontmatter,
        flags=re.DOTALL,
    )
    # Also strip any individual enriched fields that may exist without the block comment
    new_frontmatter = re.sub(r"\ncontent_type:.*?\n", "\n", new_frontmatter)
    new_frontmatter = re.sub(r"\nprimary_topic:.*?\n", "\n", new_frontmatter)
    new_frontmatter = re.sub(
        r"\naudience:.*?(?=\n\w+:|\n---|\Z)", "\n", new_frontmatter, flags=re.DOTALL
    )
    new_frontmatter = re.sub(r"\ndifficulty:.*?\n", "\n", new_frontmatter)
    new_frontmatter = re.sub(
        r"\nentities:.*?(?=\n\w+:|\n---|\Z)", "\n", new_frontmatter, flags=re.DOTALL
    )
    new_frontmatter = re.sub(
        r"\nconcepts:.*?(?=\n\w+:|\n---|\Z)", "\n", new_frontmatter, flags=re.DOTALL
    )
    new_frontmatter = re.sub(
        r"\nchapters:.*?(?=\n\w+:|\n---|\Z)", "\n", new_frontmatter, flags=re.DOTALL
    )
    new_frontmatter = re.sub(
        r"\nsummary:.*?(?=\n\w+:|\n---|\Z)", "\n", new_frontmatter, flags=re.DOTALL
    )
    new_frontmatter = re.sub(
        r"\nkeywords:.*?(?=\n\w+:|\n---|\Z)", "\n", new_frontmatter, flags=re.DOTALL
    )

    # Clean up multiple newlines
    new_frontmatter = re.sub(r"\n{3,}", "\n\n", new_frontmatter)

    # Add enriched fields
    enrichment = f'''

# AI-enriched metadata
content_type: "{content_type}"
primary_topic: "{primary_topic}"
difficulty: "{difficulty}"
audience:
{chr(10).join(f'  - "{a}"' for a in audience)}
entities:
  companies:
{chr(10).join(f'    - "{c}"' for c in companies[:10]) or "    []"}
  people:
{chr(10).join(f'    - "{p}"' for p in people[:10]) or "    []"}
  products:
{chr(10).join(f'    - "{p}"' for p in products[:10]) or "    []"}
  models:
{chr(10).join(f'    - "{m}"' for m in models[:10]) or "    []"}
concepts:
{chr(10).join(f'  - "{c.replace(chr(34), chr(39))}"' for c in concepts) or "  []"}
summary:
{chr(10).join(f'  - "{s.replace(chr(34), chr(39))}"' for s in summary) or "  []"}'''

    new_content = f"---{new_frontmatter}{enrichment}\n---{parts[2]}"

    return new_content


def main():
    print("=== AI Enrichment for Nate B Jones Transcripts ===")

    episodes = list(EPISODES_DIR.iterdir())
    episodes = [e for e in episodes if e.is_dir() and not e.name.startswith(".")]

    print(f"Found {len(episodes)} episodes")

    success = 0
    failed = 0

    for i, episode_dir in enumerate(sorted(episodes), 1):
        transcript_file = episode_dir / "transcript.md"
        if not transcript_file.exists():
            continue

        try:
            enriched = enrich_transcript(transcript_file)
            if enriched:
                transcript_file.write_text(enriched)
                success += 1
            else:
                failed += 1
        except Exception as e:
            print(f"Error on {episode_dir.name}: {e}")
            failed += 1

        if i % 50 == 0:
            print(f"Processed {i}/{len(episodes)}...")

    print("\n=== Complete ===")
    print(f"Enriched: {success}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()
