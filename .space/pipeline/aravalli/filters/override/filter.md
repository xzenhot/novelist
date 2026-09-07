# Override Command File

This is the human-in-the-loop command file for the **poetry pipeline** `aravalli` (`.space/pipeline/aravalli/`). It applies to every **poem** — each with a Question / Oration / Benediction structure — and is read by the override filter and the write/chapter agents.

## Context

- Book: *Aravalli: The Mountain Remembers* (20 poems / topics).
- Form: poetry — each poem is a three-section unit (Question / Oration / Benediction).
- Language: English.
- Master prompt: `.space/pipeline/aravalli/override.txt`.
- Chapter models: `.space/pipeline/aravalli/chapters/<n>/model.json` (one per topic).
- This command file: `.space/pipeline/aravalli/filters/override/filter.md`.

## Instructions

