# Workshop Filter — Ridge

## Purpose
Create the three-section chapter frame (Workshop / Story / Discussion) that becomes the chapter's working scaffold. The Workshop section grounds the narrator at the site; Story carries the main material; Discussion opens the reflective question.

## Inputs
- `.space/pipeline/ridge/chapters/<n>/model.json` — chapter metadata
- `.space/backlog/epic/ridge/epic.md` — story source of truth
- `.space/pipeline/ridge/book.json` — chapter plan and summaries

## Outputs
- `.space/pipeline/ridge/chapters/<n>/chapter.md` — scaffolded three-section draft
- `.space/pipeline/ridge/filters/workshop/filter-summary.md`

## Rules
- Preserve the Workshop / Story / Discussion structure exactly.
- Workshop section: sensory arrival at the site, specific time and season, the human anchor figure.
- Story section: main material — the walk, the encounter, the history, the argument. Minimum 3,000 words.
- Discussion section: the reflective question the chapter leaves open. 300–500 words.
- Do not invent species, events, or facts not grounded in the epic or chapter model.

## Hand-off
The research filter reads the Workshop output and deepens the Story section with verified grounding.
