---
name: layout
description: "Use when scaffolding the structural skeleton of a novel pipeline. USE FOR: creating .space/pipeline/book_<bookname>/ from the canonical v1 segment-based template, seeding book planning JSON, defining chapters, characters, chapter folders, segment folders, and the empty output destination. DO NOT USE FOR: writing chapter prose, editing finished book text, or creating runtime activity outputs."
---

# Layout - Novel Pipeline Scaffold

You are the structural architect for a novel. Your task is to create the mandatory pipeline skeleton that exists before writing, editing, translation, or runtime activity begins.

The current canonical scaffold is **v1** and is copied from:

` .framework/templates/novel/ `

A scaffolded book lives at:

` .space/pipeline/book_<bookname>/ `

Finished content lives at:

` source/books/book_<bookname>/ `

## Core Model

The v1 novel pipeline is segment-based:

`book -> chapters -> <n> -> segments -> <x> -> writer/editor/translator`

Each segment passes through three agents:

`writer -> editor -> translator`

Layout creates the folder tree, required state files for each structural level, and root-level planning artifacts used by research, character, workshop, and chapter-writing steps. Runtime content files are produced later by workflow execution.

## Canonical Folder Shape

```text
.space/pipeline/book_<bookname>/
|-- book.json
|-- characters.json
|-- masterprompt.md
|-- workshop_metadata.md
|-- filters/
|   |-- 1_workshop/
|   |-- 2_research/
|   |-- 3_seeds/
|   |-- 4_correctness/
|   |-- 5_theme/
|   |-- 6_syntax/
|   |-- 7_override/
|   `-- 8_quality/
`-- chapters/
    `-- 1/
        |-- moods/
        `-- segments/
            `-- 1/
                |-- writer/
                |-- editor/
                `-- translator/
```

> **Note on `moods/`:** the `moods/` folder applies only to **segment-based story/novel writing** (the frame-story novel workflow). Poetry does not use moods — a poetry chapter has only `segments/`, no `moods/`. When scaffolding a poetry book, omit the `moods/` folder.

## Path Invariant

This is mandatory.

- Never create chapter number folders directly under `book_<bookname>/`; they must live under `chapters/`.
- Never create segment number folders directly under `book_<bookname>/` or under a root-level chapter folder; they must live under `chapters/<n>/segments/`.
- The only valid chapter path is `book_<bookname>/chapters/<n>/`.
- The only valid segment path is `book_<bookname>/chapters/<n>/segments/<x>/`.
- The only valid writer/editor/translator paths are under `book_<bookname>/chapters/<n>/segments/<x>/`.
- If an older scaffold contains `book_<bookname>/chapter_<n>/`, treat it as a misplaced legacy duplicate. If it contains `chapters/chapter_<n>/` or `segments/segment_<x>/`, rename those level folders to numeric names after confirming there is no collision.

## Scaffolded Files

Do not scaffold `Template*.json`, `TemplatePrompt*.txt`, or `TemplateSystemPromptText.txt` files. Template files belong to the reusable template source or runtime prompt generation, not to a book pipeline scaffold.

A book pipeline scaffold is driven by the root planning artifacts below.

## Level State Files

This JSON file is scaffolded at each structural level and is not a `Template*.json` file:

- `model.json` - the model/state returned upward from the level after work is produced or summarized.

Create this file at the book root, every chapter folder, and every segment folder. At the book level it maintains book state; at the chapter level it maintains chapter state; at the segment level it maintains segment state. Do not place level state files directly under `writer/`, `editor/`, or `translator/` unless a later agent workflow explicitly owns that agent-level state.

## Root Planning Artifacts

These root-level planning artifacts are also required for a complete novel pipeline. They are scaffold artifacts, not optional generated clutter:

- `book.json` - the book structure, chapter list, chapter summaries, character references, and quality attributes.
- `characters.json` - the character roster extracted from or aligned with the book layout.
- `masterprompt.md` - the book-specific master prompt: identity, central premise, frame, style mandate, section structure, and references.
- `workshop_metadata.md` - workshop team, narrated-story figures, schedule, and grounding notes.
- `filters/` - one folder per pipeline filter, ordered and prefixed (`1_workshop/`, `2_research/`, `3_seeds/`, `4_correctness/`, `5_theme/`, `6_syntax/`, `7_override/`, `8_quality/`), each the scratch space where that filter records its working artifacts.

Create these for every novel scaffold. Seed them from the provided gist and book identity; do not hard-code language, genre, characters, or chapter count.

The content inside the `filters/` folders (seeds, research notes, workshop narratives) is **runtime content**, produced by the later workflow steps that run each filter — not by layout. Layout creates only the empty filter folders.


## Runtime Files

Do not create runtime files during layout unless a later workflow step explicitly produces them:

- `Exception.txt`
- `ActualPromptAgentText.txt`
- `HumanInTheLoopPromptText.txt`
- `ModelDictionaryJson.json`
- `ReceivedAgentResponseText.txt`
- `ExtractedAgentResponseJson.json`
- `RunningContentSummaryText.txt`
- `TranslatedContentText.txt`
- `ReviwedContentText.txt`
- `FinalContentText.txt`
- `_history/`

## OperationState Map

Use this order and meaning when reasoning about file names:

| Value | State | File |
| ---: | --- | --- |
| 4 | `Exception` | `Exception.txt` |
| 20 | `TemplateSystemPromptText` | `TemplateSystemPromptText.txt` |
| 22 | `TemplateModelJson` | `TemplateModelJson.json` |
| 23 | `TemplateLayOutShapeJson` | `TemplateLayOutShapeJson.json` |
| 24 | `TemplatePromptInitialText` | `TemplatePromptInitialText.txt` |
| 25 | `TemplatePromptNextText` | `TemplatePromptNextText.txt` |
| 26 | `TemplatePromptSummaryText` | `TemplatePromptSummaryText.txt` |
| 27 | `TemplatePromptTranslateText` | `TemplatePromptTranslateText.txt` |
| 30 | `ActualPromptAgentText` | `ActualPromptAgentText.txt` |
| 31 | `HumanInTheLoopPromptText` | `HumanInTheLoopPromptText.txt` |
| 32 | `ModelDictionaryJson` | `ModelDictionaryJson.json` |
| 50 | `ReceivedAgentResponseText` | `ReceivedAgentResponseText.txt` |
| 60 | `ExtractedAgentResponseJson` | `ExtractedAgentResponseJson.json` |
| 82 | `RunningContentSummaryText` | `RunningContentSummaryText.txt` |
| 83 | `TranslatedContentText` | `TranslatedContentText.txt` |
| 84 | `ReviwedContentText` | `ReviwedContentText.txt` |
| 90 | `ReturningModelJson` | `model.json` |
| 100 | `FinalContentText` | `FinalContentText.txt` |
| 101 | `TemplatePromptSingleSegmentText` | `TemplatePromptSingleSegmentText.txt` |

## Scaffolding Steps

1. Determine `<bookname>` and `<gist>`. If no gist is supplied, infer a one-line premise from the book name.
2. Read `.framework/templates/novel/` as the canonical template (moods live in `templates/novel/moods/`).
3. Create `.space/pipeline/book_<bookname>/`.
4. Exclude `Template*.json`, `TemplatePrompt*.txt`, and `TemplateSystemPromptText.txt`; include or create the level state JSON file.
5. Create the required book-level state file: `model.json`.
6. Create the required root planning artifacts: `book.json`, `characters.json`, `masterprompt.md`, `workshop_metadata.md`, and `filters/`.
7. Create `.space/pipeline/book_<bookname>/chapters/1/` by copying the canonical `moods/` folder shape, excluding `Template*.json`, `TemplatePrompt*.txt`, and `TemplateSystemPromptText.txt`.
8. Confirm `.space/pipeline/book_<bookname>/chapters/1/segments/1/` exists after copying.
9. Confirm `writer/`, `editor/`, and `translator/` exist under the canonical segment folder.
10. Create chapter-level state files in each `<n>/` and segment-level state files in each `<x>/`.
11. Seed `book.json` with the book identity, long title, genre, era, language, target audience, chapter count, summary, chapter list, character list, and history.
12. Seed `characters.json` from the layout character roster.
13. Seed `masterprompt.md` and `workshop_metadata.md` from the book identity, premise, chapter plan, style/register, and character/frame roles.
14. Create `source/books/book_<bookname>/` as the destination for finished content.
15. Verify the path invariant, required state files, and required planning artifacts before reporting completion.

## Book JSON Responsibilities

At minimum, the book-level `book.json` should contain:

- `book_name`
- `book_long_title`
- `generic`
- `era`
- `language`
- `target_audience`
- `chapter_count`
- `created_at`
- `user_name`
- `book_summary`
- `chapters`
- `all_characters`
- `history`

The `chapters` array should use `chapter_index`, `name`, `chapter_title`, and `chapter_summary`.

The `all_characters` array should use `character_id`, `full_name`, `role`, `identity`, and either `psychological_depth` or another clearly named depth field. Prefer `full_name`; older UJANGARH templates used `friendly_name`, but v1 uses `full_name`.

## Rules

- Every book pipeline lives under `.space/pipeline/`; never scaffold at the workspace root.
- Use the hardcoded v1 canonical template unless the user explicitly changes the template version.
- The default `chapter_count` is 5 unless the user specifies another count.
- The layout plus level state files and root planning artifacts are the source of truth for book structure before writing begins.
- Do not overwrite existing book-specific content without first inspecting it.
- Do not delete misplaced legacy folders unless the user approves or the current task explicitly asks for cleanup and the canonical replacement exists.

## Pipeline Chain

```text
layout -> book architect -> chapter architect -> segment writer -> editor -> translator -> final book output
```










