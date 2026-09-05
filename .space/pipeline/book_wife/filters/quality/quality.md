# Quality Filter

## Purpose

Audit the chapter against its seed quality parameters and the book's quality metrics.

## Inputs

- `chapters/<n>/chapter.md` or latest `chapter_v<n>.md`.
- `chapters/<n>/model.json`.
- `filters/3/<chapter>.json` — seed quality parameters.
- `filters/5/<chapter>.json` and `filters/6/<chapter>.json` — theme and syntax selections.

## Outputs

- `filters/8/<chapter>.json` — quality audit result.
- `filters/8/quality_summary.md` — filter-wide summary.
- Updated `chapters/<n>/model.json` `quality_review` object.

## Rules

1. Evaluate against each `quality_parameters` item from the seed.
2. Note strengths, gaps, and required rewrites.
3. With no human override, pass material through with audit notes only.

## Hand-off

When quality passes, the chapter may be written to `source/books/book_<bookname>/chapters/`.
