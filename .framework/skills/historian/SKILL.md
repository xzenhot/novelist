---
name: historian
description: 'Collect and organize historical information and data for a novel. Use when the user asks to research a topic, gather historical facts, collect references, find sources, or populate chapters_research for a novel. Pulls from the internet (web search/fetch), static text (.space/context/references), and themes (.space/context/themes), and writes per-chapter research JSON.'
argument-hint: '<bookname> <chapter> | <topic> | -o | -h'
---

# Historian — Research & Data Collection Engine

Collects historical information and data for a novel from three sources — the **internet**, **static text** (library and reference files), and **themes** — and organizes it into per-chapter research files the writing engine can draw on.

## When to Use

- "research this topic", "gather historical facts", "collect references", "find sources"
- "research chapter 3", "populate chapters_research", "what do we know about X"
- "verify historical accuracy", "collect data for the novel"

## The Three Sources

| Source | Where | How to collect |
|--------|-------|----------------|
| **Internet** | web search / fetch | Use web search and page-fetch tools to find authoritative sources (Wikipedia, Banglapedia, archive.org, academic sites). Record the reference name and weblink. |
| **Static text** | `.space/context/references/` | Read the local source texts (e.g. `aurilus.txt`, `gosai_dictionary.txt`) for direct grounding. |
| **Themes** | `.space/context/themes/` | Read the thematic category files for the philosophical lens and lexicon. |

## Output

Research is written to `.space/pipeline/book_<bookname>/chapters_research/<chapter>.json`, where `<chapter>` is `Introduction`, `1..N`, or `Conclusion`.

Each research file records, per chapter:

```json
{
  "sl": 1,
  "name": "The Dawn of Ambition",
  "chapter_title": "সিংহাসনের ছায়া",
  "chapter_summary": "...",
  "further_references": [
    { "no": "1", "reference": "History of the Senas - R.C. Majumdar", "weblink": "https://archive.org/details/historyofbengal01maju" }
  ],
  "included_characters": [ { "sl": 1, "friendly_name": "বল্লাল সেন" } ],
  "historical_accuracy": "...",
  "influence_of_other_works": "...",
  "cultural_relevance": "...",
  "literary_style": "...",
  "narrative_techniques": "...",
  "symbolism_and_motifs": "...",
  "reader_engagement_strategies": "...",
  "ethical_considerations": "...",
  "potential_controversies": "...",
  "diversity_and_inclusion": "...",
  "marketing_and_promotion": "...",
  "significance_of_rise_of_bengal": "..."
}
```

## Commands

```
/historian <bookname> <chapter>   # research one chapter (Introduction, 1..N, Conclusion)
/historian <bookname> <topic>     # research a free-form topic
/historian <bookname> all         # research all chapters in order
/historian <bookname> -o          # list existing research
/historian -h | --help            # show usage
```

## Procedure

1. **Read the layout** — `.space/pipeline/book_<bookname>/book.json` for the chapter's title and summary; `characters.json` for the cast.
2. **Collect from the internet** — search for authoritative sources on the chapter's subject; record each source's name and weblink in `further_references`.
3. **Collect from static text** — read the relevant `.space/context/references/` files; extract facts, quotes, and grounding.
4. **Collect from themes** — read `.space/context/themes/` for the thematic lens and lexicon to apply.
5. **Synthesize** — fill the research fields (historical accuracy, influence of other works, cultural relevance, etc.), distinguishing **documented fact** from **fictional invention**.
6. **Save** — write to `.space/pipeline/book_<bookname>/chapters_research/<chapter>.json`.
7. **Report** — summarize the sources found and the key facts gathered.

## Key Rules

- **Cite every source** — every `further_references` entry needs a name and a weblink (or a local file path for static text).
- **Separate fact from fiction** — mark clearly what is historically documented versus what is invented for the story.
- **Prefer authoritative sources** — Wikipedia, Banglapedia, archive.org, academic works over blogs or forums.
- **Static text first, internet second** — when a local reference already covers the subject, ground in it before searching the web.
- **One research file per chapter** — `Introduction`, `1..N`, `Conclusion`; never overwrite, but update in place if re-researching.
- **Research feeds the writing engine** — the `novelist` skill reads `chapters_research/` before writing each chapter.

## References

- Canonical example: [`.space/pipeline/book_laxman/chapters_research/`](../../../.space/pipeline/book_laxman/chapters_research/)
- Static text: [`.space/context/references/`](../../../.space/context/references/)
- Themes: [`.space/context/themes/`](../../../.space/context/themes/)
- Novel layout & engine: [`novelist` skill](../novelist/SKILL.md) and [`.framework/workflows/novel.md`](../../../.framework/workflows/novel.md)
