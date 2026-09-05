# Quality Filter Role

## Purpose

Quality audit result. Final gate before chapter writing and promotion.

## Inputs

- All upstream filter outputs
- `filter.md` human instructions
- `model.json` quality parameters

## Outputs

- Per-chapter quality audits at `.space/pipeline/book_ashok/filters/quality/<chapter>.md`
- `filter-summary.md`
- `content-output.md`

## Rules

- If `filter.md` is empty, pass material through unchanged.
- Report pass/fail status and block promotion on fail unless a human override is recorded.
