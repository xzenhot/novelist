# Override Filter

## Purpose

Apply human-in-the-loop edits and transformations that no automated filter can decide.

## Inputs

- `filters/7/override.md` — the human-editable command file.
- `chapters/<n>/chapter.md` or upstream filter outputs as referenced in the command file.

## Outputs

- Updated chapter content or model fields as directed.
- A record of applied overrides in the chapter's `model.json` (`override` object).

## Rules

1. This filter is driven entirely by `filters/7/override.md`.
2. With no human instructions, pass material through unchanged.
3. Apply instructions precisely; do not reinterpret beyond what is written.

## Hand-off

The next filter (`8`) audits the final result, including any overrides.
