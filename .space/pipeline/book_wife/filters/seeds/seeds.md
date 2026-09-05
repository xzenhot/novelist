# Seeds Filter

## Purpose

Produce per-chapter character and quality seeds: who appears and what quality bar the chapter must meet.

## Inputs

- `filters/1/<chapter>.md` — the workshop narrative.
- `filters/2/<chapter>.md` — the per-chapter research.
- `.space/pipeline/book_<bookname>/characters.json` — the full character roster.

## Outputs

- `filters/3/<chapter>.json` — per-chapter seed JSON containing:
  - `included_characters`
  - `quality_parameters`
  - `chapter_summary`
  - `theme` and `theme_essence`

## Rules

1. Only include characters relevant to the chapter.
2. Define quality parameters that are specific and measurable.
3. Align the chapter theme with the epic's thematic threads.

## Hand-off

The writer agent uses seeds to compose the chapter; the `theme` and `syntax` filters use the seed quality parameters for later passes.
