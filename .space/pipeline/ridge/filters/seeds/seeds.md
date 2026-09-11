# Seeds Filter — Ridge

## Purpose
Curate the chapter seed: select included characters from the roster, set quality parameters, write a mood-shaped chapter summary rich enough to write from, and lay out the segment structure.

## Inputs
- `.space/pipeline/ridge/characters.json`
- `.space/pipeline/ridge/chapters/<n>/chapter.md`
- `.space/pipeline/ridge/chapters/<n>/model.json`
- `.space/pipeline/ridge/chapters/<n>/mood.json`
- `.space/backlog/epic/ridge/epic.md`

## Outputs
- Updated `.space/pipeline/ridge/chapters/<n>/model.json` with included_characters, quality_parameters, chapter_summary, segments
- Segment folders under `chapters/<n>/segments/`
- `.space/pipeline/ridge/filters/seeds/filter-summary.md`

## Rules
- Characters come only from `characters.json` — do not invent new characters.
- Segment count for this book: one segment per chapter (literary non-fiction, single narrative thread).
- Quality parameters must include: philosophical depth, sensory precision, factual grounding, emotional resonance, ecological accuracy.

## Hand-off
The correctness filter reads the seeded model and verifies factual claims in the chapter draft.
