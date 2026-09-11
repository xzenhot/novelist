# Research Filter — Ridge

## Purpose
Deepen the workshop draft with verified grounding. Flatten workshop scaffolding into continuous prose. Attach era, place, figures, events, sources, and grounding notes to the chapter model.

## Inputs
- `.space/pipeline/ridge/chapters/<n>/chapter.md` — workshop draft
- `.space/pipeline/ridge/chapters/<n>/model.json`
- `.space/backlog/epic/ridge/epic.md`

## Outputs
- `.space/pipeline/ridge/chapters/<n>/chapter.md` — flattened, enriched prose
- Updated chapter `model.json` with grounding fields
- `.space/pipeline/ridge/filters/research/filter-summary.md`

## Rules
- Remove all Workshop / Story / Discussion section headings. Keep only the prose.
- Verify species names (Salim Ali, Grimmett for birds; Pradip Krishen for trees).
- Verify historical claims (Aravalli geology, Mangar Bani history, Supreme Court orders).
- Word target: 4,500 words per chapter.

## Hand-off
The seeds filter reads the flattened research output and curates included characters and quality parameters.
