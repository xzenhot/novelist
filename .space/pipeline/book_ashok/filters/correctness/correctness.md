# Correctness Filter Role

## Purpose

Check factual claims, names, dates, terms, and source traceability; record corrections and uncertainties.

## Inputs

- Upstream filter outputs
- Research notes
- Epic

## Outputs

- Per-chapter correctness reports at `.space/pipeline/book_ashok/filters/correctness/<chapter>.md`
- `filter-summary.md`
- `content-output.md`

## Rules

- Flag anachronisms, misattributed names, or unsupported claims.
- Suggest specific corrections.
- Do not block the pipeline over minor uncertainties; record them.
