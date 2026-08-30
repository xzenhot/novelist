---
name: layout
description: "Use when scaffolding the structural skeleton of a novel — the layout that defines chapters, characters, and the workshop structure before any chapter is written. USE FOR: creating a book pipeline (book.json, characters.json, masterprompt.md, workshop_metadata.md, and the empty folders), defining the chapter list and structure. DO NOT USE FOR: writing chapter prose (use narrative), or building the character roster in detail (use character-builder)."
---

# Layout — The Novel's Structural Skeleton

You are a structural architect. Your task is to scaffold the **layout** of a novel — the mandatory structural skeleton that must exist before any chapter is written.

## What a Layout Holds

A layout lives at `.space/pipeline/book_<bookname>/` and contains:

- **`book.json`** — the book's structure (chapter titles and summaries).
- **`characters.json`** — the character roster.
- **`masterprompt.md`** — the book-specific master prompt.
- **`workshop_metadata.md`** — workshop metadata (team members).
- **`workshop_minutes/`** — the workshop narratives (empty at scaffold).
- **`chapter_seeds/`** — per-chapter seeds (characters + quality parameters).
- **`chapters_research/`** — per-chapter research (empty at scaffold).

Plus an output folder `source/books/book_<bookname>/` for finished chapters.

## Scaffolding Steps

1. Create `.space/pipeline/book_<bookname>/` and its subfolders.
2. Create `book.json` — the chapter list and structure.
3. Create `characters.json` — the character roster.
4. Create `masterprompt.md` — the book-specific master prompt.
5. Create `workshop_metadata.md` — workshop metadata.
6. Create `source/books/book_<bookname>/` — the output destination.

## Rules

- **Every book lives under `.space/pipeline/`** — never at the workspace root.
- **No chapter can be written before its layout exists.**
- **The layout is the single source of truth** for the book's structure.

## The Pipeline Chain

```
layout → research → characters → workshops → chapters
```
