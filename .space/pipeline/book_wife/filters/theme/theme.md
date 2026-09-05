# Theme Filter

## Purpose

Map the chapter's timeless theme onto a present-day concern, producing a contemporary reading.

## Inputs

- `filters/1/<chapter>.md` — workshop narrative.
- `filters/2/<chapter>.md` — research notes.
- `filters/3/<chapter>.json` — seed (theme, theme_essence, quality parameters).
- `.framework/templates/stereotypes/novel/themes/` or `stereotypes/poetry/themes/` registry.

## Outputs

- `filters/5/<chapter>.json` — theme assignment and contemporary mapping.

## Rules

1. Select or assign a theme consistent with the book's thematic threads.
2. Write a clear `theme_essence` sentence that the chapter must embody.
3. Provide a `contemporary_mapping` that shows why the theme matters now.

## Hand-off

The next filter (`6`) selects syntax to express the assigned theme in a modern voice.
