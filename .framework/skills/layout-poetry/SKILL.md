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

### `filters/override/filter.md` — the override command file

The poetry override, like the novel override, is **a filter-file command layer**, not a pipeline-root file. Do **not** create a pipeline-root `override.md`. The `override` filter lives in `filters/override/` and its command file `filters/override/filter.md` is seeded at scaffold from `.framework/agents/override/agent.md` (dynamically customized for the poetry form and the pipeline's actual context), with an empty `## Instructions` section for the human.

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

**Override command file (poetry customization):** the `override` filter is the one structural exception. Its exact seeding content is **dynamically derived at scaffold time** from `.framework/agents/override/agent.md` plus the poetry stereotype index at `.framework/templates/stereotypes/poetry/readme.md` — do not treat this paragraph as the fixed recipe. Before you create the override file, read both and let them govern the shape:

1. **Read `.framework/agents/override/agent.md`** — the base content for the command file: the override command file is `.space/pipeline/book_<bookname>/filters/override/filter.md`, and it is generated/refreshed from the chapter (or poem) models' context so the human instructions are grounded in what the poems actually contain.
2. **Read `.framework/templates/stereotypes/poetry/readme.md`** — the master index of the poetry stereotype folder, for the identity wording and conventions of the poetry form.
3. **Seed `.space/pipeline/book_<bookname>/filters/override/filter.md`**, customized for poetry: identity "poetry pipeline", applies to every **poem** (Question/Oration/Benediction), model updates on the poem chapter models under `chapters/<n>/`, instruction scope "every poem" (each topic in `bookseed.txt`).
4. **Do not create a pipeline-root `override.md`.** All forms share the single override command file at `filters/override/filter.md`.
5. Align with whatever the readme's sub-indexes declare (singer/signature set, reference texts, syntax samples, theme sets under `signatures/`, `references/`, `syntax/`, `themes/`) — the override layer must not contradict the stereotype set the pipeline will use.
6. Leave the trailing `## Instructions` section empty below the `---` line and never overwrite existing human instructions there.

## Source Destination

Create:

```text
source/books/book_<bookname>/chapters/
```

Do not write poem chapters or `book.md` during layout.

## Verification

Before reporting completion, verify:

- Root files exist: `model.json`, `bookseed.txt`, `progress.json`, and one `metadata_code<number>.json`.
- `filters/override/filter.md` exists — the override command file (no pipeline-root `override.md`).
- `filters/filters.json` exists and names all six poetry filters in order.
- Every filter folder has its role file, `filter.md`, `filter-summary.md`, and `content-output.md`.
- Every topic has one numeric chapter folder.
- Every chapter has `model.json` and `segments/1/model.json`.
- Every `segments/1/` has `writer/`, `editor/`, and `translator/` folders.
- No `mood.json` files exist in poetry chapter folders.
- No chapter or segment folders were created outside the canonical paths.
- `source/books/book_<bookname>/chapters/` exists and contains no unfinished generated prose unless a later workflow created it.

