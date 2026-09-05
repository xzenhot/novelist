# Syntax Filter

## Purpose

Select the target sentence structure and register for the chapter, keeping the prophetic voice but modernizing syntax.

## Inputs

- `filters/3/<chapter>.json` — seed (quality parameters).
- `filters/5/<chapter>.json` — theme assignment.
- `.framework/templates/stereotypes/<form>/syntax/` registry and sample files.

## Outputs

- `filters/6/<chapter>.json` — syntax selection record.
- Updated `chapters/<n>/model.json` with a `syntax` object (`form`, `sample`, `readability_bar`).

## Rules

1. Choose a syntax sample that matches the form (novel or poetry) and target register.
2. Set a readability bar that is specific (e.g., "elevated modern prose with clear clause movement").
3. Ensure syntax supports the theme rather than overriding it.

## Hand-off

The writer and poet agents use the syntax selection when composing or rewriting the chapter.
