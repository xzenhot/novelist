---
name: layout-poetry
description: "Use when scaffolding or repairing the structural skeleton of a poetry pipeline. Creates .space/pipeline/book_<bookname>/, model.json, bookseed.txt, progress.json, override.md, metadata_code files, named poetry filter folders, one segment per topic, and the empty source/books destination. Does not write poem chapters or runtime filter results."
---

# Layout Poetry - Pipeline Scaffold

You are the structural architect for a poetry pipeline. Create only the scaffold and planning artifacts needed before research, filtering, writing, revision, and final assembly begin.

A scaffolded poetry book lives at:

```text
.space/pipeline/book_<bookname>/
```

Finished content later lives at:

```text
source/books/book_<bookname>/
```

## Source Of Truth

Use this skill together with `.framework/workflows/write.md`. Do not inspect existing book pipelines to discover or imitate layout conventions; existing books may be legacy, experimental, or partially migrated.

Poetry uses these root files as source of truth:

- `model.json` for how to write: form, language, register, quality, themes, reference, index, vocabulary, and translation guide.
- `bookseed.txt` for what to write: one topic per line.

## Canonical Folder Shape

```text
.space/pipeline/book_<bookname>/
|-- model.json
|-- bookseed.txt
|-- progress.json
|-- override.md
|-- metadata_code1.json
|-- filters/
|   |-- filters.json
|   |-- research/
|   |   |-- research.md
|   |   |-- filter.md
|   |   |-- filter-summary.md
|   |   `-- content-output.md
|   |-- correctness/
|   |-- theme/
|   |-- syntax/
|   |-- override/
|   `-- quality/
`-- chapters/
    `-- 1/
        |-- model.json
        `-- segments/
            `-- 1/
                |-- model.json
                |-- writer/
                |-- editor/
                `-- translator/
```

Every filter folder uses the same four-file shape as `research/`, with the role file named after the folder.

## Path Invariant

This is mandatory.

- Chapter folders live only under `.space/pipeline/book_<bookname>/chapters/`.
- Segment folders live only under `.space/pipeline/book_<bookname>/chapters/<chapter>/segments/`.
- Poetry chapters always have exactly one segment: `segments/1/`.
- Writer, editor, and translator folders live only under `segments/1/`.
- Do not create `mood.json` for poetry.
- Do not create `book.json`, `characters.json`, `masterprompt.md`, or `workshop_metadata.md` for poetry unless the user explicitly asks for a hybrid project.

## Topic And Chapter Set

Each non-empty line in `bookseed.txt` becomes one poetry chapter.

If the user supplies topics, preserve their text exactly except for trimming surrounding whitespace. If no topic list is supplied, derive a concise ordered topic list from the gist or book name and the requested chapter count.

The default `chapter_count` is 5 unless the user specifies another count.

## Root Files

Create these at the pipeline root.

### `model.json`

Minimum fields:

- `form`: `poetry`
- `book_name`
- `book_long_title`
- `language`
- `register`
- `quality`
- `themes`
- `reference`
- `index`
- `sacred_vocabulary`
- `translation_guide`
- `chapter_count`
- `source_terms`
- `created_at`

### `bookseed.txt`

One topic per line, in the exact writing order.

### `progress.json`

Track one entry per topic.

Minimum fields:

- `title`
- `language`
- `source_terms`
- `context`
- `total_chapters`
- `completed_chapters`
- `current_chapter`
- `chapters`

Each progress chapter must include:

- `chapter_number`
- `topic`
- `category`
- `status`
- `file_path`
- `completed_date`

For a new scaffold, set all statuses to `pending`, `completed_chapters` to `0`, `current_chapter` to `1`, and `completed_date` to `null`.

### `override.md`

Create as the human-editable transformation layer. Leave it empty unless the user supplies override text.

### `metadata_code<number>.json`

Create the first available `metadata_code<number>.json`. Never overwrite an existing metadata file.

## Chapter And Segment State

Create `model.json` in every chapter folder and every segment folder.

Chapter-level `model.json` minimum shape:

```json
{
  "level": "chapter",
  "state": "scaffolded",
  "chapter_index": 1,
  "chapter_name": "Topic",
  "topic": "Topic",
  "segments": [1]
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

## Filter Registry

Create `.space/pipeline/book_<bookname>/filters/filters.json` with this poetry chain in order:

```text
research -> correctness -> theme -> syntax -> override -> quality
```

Each registry entry must include:

- `order`
- `name`
- `folder`
- `role_file`
- `summary_file`
- `output_file`
- `description`
- `agent`

For each named filter folder, scaffold only:

- `<filter>.md`
- `filter.md`
- `filter-summary.md`
- `content-output.md`

Leave runtime content empty unless the active workflow explicitly runs that filter.

## Source Destination

Create:

```text
source/books/book_<bookname>/chapters/
```

Do not write poem chapters or `book.md` during layout.

## Verification

Before reporting completion, verify:

- Root files exist: `model.json`, `bookseed.txt`, `progress.json`, `override.md`, and one `metadata_code<number>.json`.
- `filters/filters.json` exists and names all six poetry filters in order.
- Every filter folder has its role file, `filter.md`, `filter-summary.md`, and `content-output.md`.
- Every topic has one numeric chapter folder.
- Every chapter has `model.json` and `segments/1/model.json`.
- Every `segments/1/` has `writer/`, `editor/`, and `translator/` folders.
- No `mood.json` files exist in poetry chapter folders.
- No chapter or segment folders were created outside the canonical paths.
- `source/books/book_<bookname>/chapters/` exists and contains no unfinished generated prose unless a later workflow created it.
