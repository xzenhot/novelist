---
name: novelist
description: 'Scaffold and write frame-story novels. Use when the user asks to create a novel, scaffold a novel layout, write novel chapters, continue a novel, or list available novels. The /novel <bookname> <chapter_count> command creates a mandatory layout (book structure) in .space/pipeline/book_<bookname>/.'
argument-hint: '<bookname> <chapter_count> | <chapter> | all | continue | -o | -h'
---

# Novel Writer — Frame-Story Engine

A dynamic, subject-agnostic literary engine that writes **frame-story novels** — interleaving a modern frame (a theatre workshop) with a historical narrative. Every novel begins with a **layout** (its structural skeleton), which is mandatory: no chapter can be written before its layout exists.

## When to Use

- "create a novel", "scaffold a novel", "new novel layout", "set up a novel"
- "write chapter 3", "write all chapters", "continue the novel", "resume the novel"
- "list novels", "what novels exist"

## The Layout (Mandatory)

Every novel must have a **layout** before any chapter is written. The layout is the book's structural skeleton, created by:

```
/novel <bookname> <chapter_count>
```

This creates `.space/pipeline/book_<bookname>/` with the full structure:

```
.space/pipeline/book_<bookname>/
├── book.json              # book structure: title, era, language, chapters[]
├── characters.json        # character list
├── masterprompt.md        # book-specific master prompt
├── workshop.txt           # raw workshop prompt
├── workshop_metadata.md   # workshop metadata (team members)
├── workshop_minutes/      # workshop narratives (Introduction.md, 1..N.md, Conclusion.md)
├── chapter_seeds/         # chapter seeds (Introduction.json, 1..N.json, Conclusion.json)
└── chapters_research/     # per-chapter research (Introduction.json, 1..N.json, Conclusion.json)
```

`<chapter_count>` = **N**, the number of main chapters. The layout always includes an `Introduction` and a `Conclusion` in addition to the N main chapters — **N + 2 chapters total**.

## Commands

```
/novel <bookname> <chapter_count>   # scaffold the layout (mandatory first step)
/novel <bookname> <chapter>         # write one chapter (Introduction, 1..N, Conclusion)
/novel <bookname> all               # write all chapters in order
/novel <bookname> continue          # resume from the first missing chapter
/novel -o | --options               # list available novels
/novel -h | --help                  # show usage
```

## Scaffolding Steps

1. **Create the folders** — `.space/pipeline/book_<bookname>/` and its subfolders `workshop_minutes/`, `chapter_seeds/`, `chapters_research/`.
2. **Create `book.json`** — the book structure with `<chapter_count>` chapters: `Introduction`, `1..N`, `Conclusion`. Each chapter gets a placeholder `chapter_title` and `chapter_summary` (to be filled by the human or generated later).
3. **Create `characters.json`** — initialize as `{"all_characters": []}`.
4. **Create `masterprompt.md`** — the book-specific master prompt (persona, structure, chapter guidelines).
5. **Create `workshop.txt`** — the raw workshop prompt (empty, human fills it).
6. **Create `workshop_metadata.md`** — the workshop team roster (empty template).
7. **Create the output folder** — `source/book_<bookname>/` for finished chapters.

## Key Rules

- **Layout first, always.** `/novel <bookname> <chapter_count>` is the mandatory first step for a new novel. No chapter is written before its layout exists.
- **All layouts live under `.space/pipeline/`.** Never scaffold at the workspace root.
- **`<chapter_count>` drives the structure.** It sets N in `book.json`; `Introduction` and `Conclusion` are always added on top.
- **Finished chapters go to `source/book_<bookname>/`.** The pipeline holds inputs; the source holds outputs.
- **Resume, never restart.** `continue` starts from the first chapter missing in `source/book_<bookname>/`.

## References

- Engine & command spec: [`.framework/workflows/novel.md`](../../../.framework/workflows/novel.md)
- Canonical example layout: [`.space/pipeline/book_laxman/`](../../../.space/pipeline/book_laxman/)
