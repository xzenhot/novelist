---
name: subject-matter-philosophy
description: 'Build the philosophical grounding (quality/seed analysis) for a subject matter. Use when the user asks to analyze a reference book, define a philosophical framework, extract themes and metaphor families, create a quality file, or establish the subject-matter philosophy for a book. Produces a quality file in .space/context/qualities/ that the writer engine uses to ground every chapter.'
argument-hint: '<subject> [reference_file] | -o | -h'
---

# Subject-Matter Philosophy — Quality & Seed Analysis Engine

Builds the **philosophical grounding** for a subject matter — the seed analysis that tells the writer engine *what* a reference book is about, *how* it thinks, and *which* themes and metaphors to weave into every chapter. This is the "quality" file in `.space/context/qualities/`.

## When to Use

- "analyze this reference book", "define the philosophy", "extract themes and metaphors"
- "create a quality file", "build the seed analysis", "establish the subject-matter philosophy"
- "what are the core themes", "what metaphor families does this work use"

## What a Quality File Is

A quality file is a **seed analysis of a reference book** — the philosophical foundation the writer engine reads to render chapters in the target voice. It lives at `.space/context/qualities/<subject>.md` and is registered in `.space/context/qualities/registry.md`.

## The Quality File Structure

Each quality file follows this shape (see `aurilus.md` for the canonical example):

1. **Document Overview** — source, work, author, genre, structure.
2. **Quality Metrics Analysis** — rated dimensions:
   - Philosophical Depth
   - Metaphorical Richness
   - Human Context & Accessibility
   - Relevance to Civilization
   - Literary Quality
   - Ethical Framework Quality
3. **Civilizational Context** — the historical moment and the work's place in it.
4. **Metaphorical Landscape** — primary conceptual frameworks and recurring imagery patterns.
5. **Philosophical Innovations** — what the work contributes to its tradition.
6. **Relevance Patterns for Modern Adaptation** — themes ripe for the target voice.
7. **Linguistic/Stylistic DNA** — signature constructions and how they translate to the target style.
8. **Quality Assessment Summary** — overall rating and why the text endures.
9. **Recommendations for Seed Topics** — concrete chapter topics derived from the work.

## Commands

```
/philosophy <subject> [reference_file]   # build a quality file for a subject
/philosophy <subject> -o                 # show the existing quality file
/philosophy -o | --options               # list available qualities
/philosophy -h | --help                  # show usage
```

## Procedure

1. **Read the reference** — the source text in `.space/context/references/` (e.g. `aurilus.txt`, `gosai_dictionary.txt`). If no reference file is given, ask which one to analyze.
2. **Analyze the work** — extract:
   - Identity, genre, structure
   - Core philosophical themes
   - Dominant metaphor families and recurring imagery
   - Quality metrics (rate each dimension)
   - Signature stylistic constructions
3. **Write the quality file** — `.space/context/qualities/<subject>.md`, following the nine-section structure above.
4. **Register it** — add a row to `.space/context/qualities/registry.md` (name, reference work, author, genre, language, status).
5. **Report** — summarize the core themes, metaphor families, and quality ratings.

## Key Rules

- **One quality = one reference book.** Each file analyzes a single source text.
- **Quality files are read-only inputs** — the writer engine reads them; it never modifies them.
- **Themes live separately** — thematic categories derived from a quality belong in `.space/context/themes/`, not in the quality file itself.
- **References live separately** — the source text belongs in `.space/context/references/`, not in the quality file.
- **Rate every dimension** — philosophical depth, metaphorical richness, accessibility, relevance, literary quality, ethical framework.
- **Extract metaphor families** — nature, theatrical, architectural, fire/element, body/medical, etc., with concrete examples.
- **Recommend seed topics** — end with concrete chapter topics the writer can turn into chapters.

## References

- Canonical example: [`.space/context/qualities/aurilus.md`](../../../.space/context/qualities/aurilus.md)
- Quality registry: [`.space/context/qualities/registry.md`](../../../.space/context/qualities/registry.md)
- Themes: [`.space/context/themes/`](../../../.space/context/themes/)
- References: [`.space/context/references/`](../../../.space/context/references/)
- Writer engine: [`poet` skill](../poet/SKILL.md)
