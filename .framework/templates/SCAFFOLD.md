# Scaffold Reference

The authoritative scaffold rules live in `.framework/skills/layout/SKILL.md`.

This file is only a short reference note.

## Current Invariants

- New book pipelines live under `.space/pipeline/book_<bookname>/`.
- Finished book output lives under `source/books/book_<bookname>/`.
- Chapter folders use numeric level names: `chapters/<n>/`.
- Segment folders use numeric level names: `chapters/<n>/segments/<x>/`.
- Do not create chapter number folders directly under `book_<bookname>/`.
- Do not create segment number folders outside `chapters/<n>/segments/`.
- Do not scaffold `Template*.json`, `TemplatePrompt*.txt`, or `TemplateSystemPromptText.txt` into a book pipeline.
- Include `SelfStateInitialJson.json`, `SelfStateActivityJson.json`, and `ReturningModelJson.json` at book, chapter, and segment levels; they are level state files, not template files.
- Create root planning artifacts: `book.json`, `characters.json`, `masterprompt.md`, `workshop_metadata.md`, `workshop_minutes/`, `chapter_seeds/`, and `chapters_research/`.
