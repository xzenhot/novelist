# Correctness Filter

## Purpose

Verify every fact, term, and claim in the chapter material. Flag uncertainties and record corrections.

## Inputs

- `filters/1/<chapter>.md` — workshop narrative.
- `filters/2/<chapter>.md` — per-chapter research.
- `filters/3/<chapter>.json` — chapter seed (quality parameters and summary).
- External sources as needed.

## Outputs

- `filters/4/<chapter>.json` — per-chapter correctness result with:
  - `status`
  - `corrections`
  - `flagged_uncertainties`
- `filters/4/correctness_summary.md` — filter-wide summary.

## Rules

1. Verify factual claims; do not pass unchecked assertions.
2. Note archetypal or fictional framing explicitly.
3. Distinguish between confirmed facts, plausible inference, and uncertainty.

## Hand-off

The next filter (`5`) applies the thematic lens on top of corrected material.
