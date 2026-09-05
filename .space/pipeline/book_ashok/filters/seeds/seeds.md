# Seeds Filter Role

## Purpose

Curate the chapter seed by selecting included characters, quality parameters, mood-shaped summary, and segment structure.

## Inputs

- Research output
- `characters.json`
- `book.json` chapter summaries

## Outputs

- Per-chapter seed files at `.space/pipeline/book_ashok/filters/seeds/<chapter>.json`
- `filter-summary.md`
- `content-output.md`

## Rules

- Select characters relevant to the chapter's events.
- Define quality parameters consistent with the gibran/aurilus stereotype.
- Preserve the chapter mood from the pipeline mood.json.
