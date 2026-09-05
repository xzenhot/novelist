---
name: layout-poetry
description: "Use when scaffolding the structural skeleton of a poetry pipeline. USE FOR: creating .space/pipeline/book_<bookname>/ for poetry, seeding model.json, bookseed.txt, progress.json, override.md, metadata code files, one segment per topic, poetry filter folders, and the empty output destination. DO NOT USE FOR: writing poem chapters, editing finished book text, or creating runtime filter outputs."
---

# Layout Poetry - Pipeline Scaffold

You are the structural architect for a poetry book. Your task is to create the mandatory poetry pipeline skeleton that exists before research, filtering, writing, revision, or final assembly begins.

A scaffolded poetry book lives at:

` .space/pipeline/book_<bookname>/ `

Finished content lives at:

` source/books/book_<bookname>/ `

## Core Model

The poetry pipeline is topic-based and segment-based:

`book -> bookseed topics -> chapters -> <n> -> segments -> 1 -> writer/editor/translator`

Each topic from `bookseed.txt` becomes one poetry chapter. Poetry chapters have exactly one segment: `segments/1`. Poetry does not use `mood.json`.

Layout creates the folder tree, required state files, root configuration, progress tracking, and human-editable override file. Runtime filter outputs and finished poem chapters are produced later by workflow execution.

## Canonical Folder Shape

```text
.space/pipeline/book_<bookname>/
|-- model.json
|-- bookseed.txt
|-- progress.json
|-- override.md
|-- metadata_code1.json
|-- filters/
|   |-- research/
|   |-- correctness/
|   |-- theme/
|   |-- syntax/
|   |-- override/
|   `-- quality/
`-- chapters/
    `-- 1/
        `-- segments/
            `-- 1/
                |-- writer/
                |-- editor/
                `-- translator/
```

## Path Invariant

This is mandatory.

- Never create chapter number folders directly under `book_<bookname>/`; they must live under `chapters/`.
- Never create segment number folders directly under `book_<bookname>/` or under a root-level chapter folder; they must live under `chapters/<n>/segments/`.
- The only valid chapter path is `book_<bookname>/chapters/<n>/`.
- The only valid segment path is `book_<bookname>/chapters/<n>/segments/1/`.
- Poetry chapters always have exactly one segment.
- Do not create `mood.json` for poetry chapters.

## Scaffolded Files

Do not scaffold `Template*.json`, `TemplatePrompt*.txt`, or `TemplateSystemPromptText.txt` files. Template files belong to reusable template source or runtime prompt generation, not to a book pipeline scaffold.

A poetry scaffold is driven by these root artifacts:

- `model.json` - form, title, language, register, quality, themes, reference, index, sacred vocabulary, translation guide, and book metadata.
- `bookseed.txt` - human-editable topic list; one topic per line.
- `progress.json` - writing progress for every topic/chapter.
- `override.md` - optional human transformation layer.
- `metadata_code<number>.json` - metadata/code artifact for runtime generation; never overwrite an existing metadata file.
- `filters/` - one folder per poetry filter: `research`, `correctness`, `theme`, `syntax`, `override`, `quality`.
- `chapters/` - one numeric folder per topic, each with `segments/1/` and agent subfolders.

## Template Sources

Use `.framework/templates/stereotypes/poetry/default/` as the default poetry template source when no book-specific template is supplied.

Default seed files:

- `config.json` -> seed `model.json`, then update it with the actual book name, title, form, chapter count, source paths, and user-provided gist/config.
- `bookseed.txt` -> seed topics if the user has not supplied a topic list.
- `progress.json` -> seed progress shape, then reset all generated chapters to `pending`.
- `override.md` -> seed the human-editable override file.
- `ai_studio_code1.json` -> seed the first available `metadata_code<number>.json` if no metadata code file exists.

## Level State Files

Create `model.json` at each chapter folder and each segment folder.

Chapter-level `model.json` minimum shape:

```json
{
  "level": "chapter",
  "state": "scaffolded",
  "chapter_index": 1,
  "chapter_name": "Topic",
  "topic": "Topic"
}
```

Segment-level `model.json` minimum shape:

```json
{
  "level": "segment",
  "state": "returning",
  "chapter_index": 1,
  "segment_index": 1
}
```

## Progress JSON Responsibilities

`progress.json` tracks the writing state of each topic in `bookseed.txt`.

At minimum, it should contain:

- `title`
- `language`
- `source_terms`
- `context`
- `total_chapters`
- `completed_chapters`
- `current_chapter`
- `chapters`

Each `chapters` item should contain:

- `chapter_number`
- `topic`
- `category`
- `status`
- `file_path`
- `completed_date`

For new scaffolds, set every topic `status` to `pending`, `completed_date` to `null`, `completed_chapters` to `0`, and `current_chapter` to `1`.

## Scaffolding Steps

1. Determine `<bookname>`, form (`poetry`), language, register, title, and chapter count.
2. Read or create the topic list. If the user supplied topics, write them to `bookseed.txt`; otherwise seed from the default poetry template and trim to the requested chapter count.
3. Create `.space/pipeline/book_<bookname>/`.
4. Create root `model.json` with `"form": "poetry"`, title, language, register, quality, themes, reference, index, sacred vocabulary, translation guide, and `chapter_count`.
5. Create `bookseed.txt`, `progress.json`, `override.md`, and the first available `metadata_code<number>.json` without overwriting existing metadata files.
6. Create poetry filter folders: `filters/research/`, `filters/correctness/`, `filters/theme/`, `filters/syntax/`, `filters/override/`, and `filters/quality/`.
7. For each topic, create `.space/pipeline/book_<bookname>/chapters/<n>/segments/1/` with `writer/`, `editor/`, and `translator/` subfolders.
8. Create chapter-level and segment-level `model.json` files.
9. Create `source/books/book_<bookname>/chapters/` as the destination for finished poetry chapters.
10. Verify the path invariant, one-segment rule, required state files, root artifacts, and progress tracking before reporting completion.

## Rules

- Every poetry pipeline lives under `.space/pipeline/`; never scaffold at the workspace root.
- Poetry uses `model.json` + `bookseed.txt` as source of truth.
- Poetry does not use `book.json`, `characters.json`, `masterprompt.md`, `workshop_metadata.md`, or `mood.json` unless the user explicitly asks for a hybrid project.
- Poetry filter folders are named, not numbered.
- The default `chapter_count` is 5 unless the user specifies another count.
- Do not overwrite existing book-specific content without first inspecting it.
- Do not delete misplaced legacy folders unless the user approves or the current task explicitly asks for cleanup and the canonical replacement exists.

## Pipeline Chain

```text
layout-poetry -> research -> correctness -> theme -> syntax -> override -> quality -> poet/writer -> final book output
```
