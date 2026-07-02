---
layout: default
title: Scoring System
---

# Scoring System

After fetching content from all sources, Horizon uses an AI model to score each
item on two independent 0-10 scales: direct AI relevance and importance. An
item must pass the relevance gate before importance can qualify it for the
daily summary.

## Pipeline

1. **Batch processing** — Items are scored in batches of 10 with a progress bar. Failed items receive a score of 0.
2. **Content preparation** — For each item, the content is truncated (800 chars if comments are present, 1000 otherwise) and engagement metrics are assembled from metadata (HN score, Reddit upvote ratio, etc.).
3. **AI analysis** — The prepared content is sent to the configured AI model (temperature 0.3) with a system prompt defining the scoring criteria.
4. **Response parsing** — The AI response is parsed as JSON (with fallbacks for
   code-block-wrapped JSON). Each item gets `ai_relevance_score`,
   `ai_relevance_reason`, `ai_score`, `ai_reason`, `ai_summary`, and `ai_tags`.
   Missing relevance data fails closed with a relevance score of 0.
5. **Retry** — Failed AI calls are retried up to 3 times with exponential backoff (2-10 seconds).

## AI Relevance Gate

`ai_relevance_score` measures whether AI is the central subject:

- **8-10**: Directly about AI/ML models, agents, AI research, AI-native tools,
  AI infrastructure, safety, policy, industry, or materially AI-driven uses.
- **4-7**: AI-adjacent; AI is only a use case, customer, or secondary angle.
- **0-3**: General technology, science, business, or software news.

Popularity never increases relevance. General software releases, games,
payments, cloud services, and biology stories do not pass merely because they
mention AI or agents.

## Importance Scale

| Score | Tier | Description |
|-------|------|-------------|
| 9-10 | Groundbreaking | Major breakthroughs, paradigm shifts, major version releases, significant research breakthroughs |
| 7-8 | High Value | Important developments, technical deep-dives, novel approaches, insightful analysis, valuable tools |
| 5-6 | Interesting | Incremental improvements, useful tutorials, moderate community interest |
| 3-4 | Low Priority | Minor updates, common knowledge, overly promotional |
| 0-2 | Noise | Spam, off-topic, trivial updates |

## Scoring Factors

The AI evaluates each item based on:

- **Technical depth and novelty** — original ideas, new techniques, research contributions
- **Potential impact** — how broadly this affects software engineering, AI/ML, or systems research
- **Quality of writing/presentation** — clarity, structure, thoroughness
- **Community discussion** — insightful comments, diverse viewpoints, substantive debates
- **Engagement signals** — high upvotes/favorites paired with substantive discussion (not just raw numbers)

Engagement metadata is source-specific: HN provides score and comment count, Reddit provides upvote ratio and comment count.

## Filtering

After scoring, items are filtered first by
`filtering.ai_relevance_threshold` (default: `8.0`), then by
`filtering.ai_score_threshold` (default: `7.0`) and sorted by importance.
Optional balanced digest quotas are then applied before enrichment.

```json
{
  "filtering": {
    "ai_relevance_threshold": 8.0,
    "ai_score_threshold": 7.0,
    "time_window_hours": 24,
    "max_items": 20,
    "category_groups": {
      "ai": {
        "limit": 5,
        "categories": ["ai-news", "ai-tools", "machine-learning"]
      }
    }
  }
}
```

`category_groups` limits each configured category group independently.
`max_items` caps the merged result. Both fields are optional; without them,
scoring and filtering behave as before.

Items scoring 9.0 or above are featured in the "Today's Highlights" section of the summary.

## Enrichment

Items that pass the score threshold and any balanced digest limits go through a second AI pass for enrichment (`src/ai/enricher.py`):

1. **Concept extraction** — AI identifies 1-3 technical concepts in the item that may need explanation.
2. **Web search** — Each concept is searched via DuckDuckGo to gather grounding context.
3. **Structured analysis** — The item content and search results are sent to AI, which produces:
   - `whats_new` — what specifically happened or changed
   - `why_it_matters` — significance and impact
   - `key_details` — notable technical details or caveats
   - `background` — background knowledge for readers without deep domain expertise

These fields are combined into a `detailed_summary` stored in the item's metadata and used in the final daily summary.
