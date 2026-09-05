# Override Filter Role

## Purpose

Human-in-the-loop transformation layer. Apply any special instructions written in this folder's `filter.md`.

## Inputs

- All upstream filter outputs
- `filter.md` human instructions

## Outputs

- Transformed per-chapter outputs at `.space/pipeline/book_ashok/filters/override/<chapter>.md`
- `filter-summary.md`
- `content-output.md`

## Rules

- If `filter.md` is empty, pass material through unchanged.
- Otherwise apply the human instructions strictly.
