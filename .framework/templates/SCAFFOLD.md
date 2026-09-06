# Scaffold Reference

The authoritative scaffold rules live in `.framework/skills/layout-novel/SKILL.md` for novels and `.framework/skills/layout-poetry/SKILL.md` for poetry. `.framework/agent.md` selects the correct one by form.

This file is only a short reference note.

## Current Invariants

- New book pipelines live under `.space/pipeline/<bookname>/`.
- Finished book output lives under `source/books/<bookname>/`.
- Chapter folders use numeric level names: `chapters/<n>/`.
- Segment folders use numeric level names: `chapters/<n>/segments/<x>/`.
- Do not create chapter number folders directly under `<bookname>/`.
- Do not create segment number folders outside `chapters/<n>/segments/`.
- Do not scaffold `Template*.json`, `TemplatePrompt*.txt`, or `TemplateSystemPromptText.txt` into a book pipeline.
- Include `model.json` at book, chapter, and segment levels; it is a level state file, not a template file.
- Create root planning artifacts: `book.json`, `characters.json`, `masterprompt.md`, `workshop_metadata.md`, and `filters/`.

