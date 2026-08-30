---
name: layout
description: "Use when scaffolding the structural skeleton of a novel pipeline. USE FOR: creating .space/pipeline/book_<bookname>/ from the canonical v1 segment-based template, seeding book layout JSON, defining chapters, characters, chapter folders, segment folders, and the empty output destination. DO NOT USE FOR: writing chapter prose, editing finished book text, or creating runtime activity outputs."
---

# Layout - Novel Pipeline Scaffold

You are the structural architect for a novel. Your task is to create the mandatory pipeline skeleton that exists before writing, editing, translation, or runtime activity begins.

The current canonical scaffold is **v1** and is copied from:

` .space/templates/v1/fiction/book/ `

A scaffolded book lives at:

` .space/pipeline/book_<bookname>/ `

Finished content lives at:

` source/books/book_<bookname>/ `

## Core Model

The v1 novel pipeline is segment-based:

`book -> chapters -> chapter_<n> -> segments -> segment_<x> -> writer/editor/translator`

Each segment passes through three agents:

`writer -> editor -> translator`

Layout creates two required layers: the segment-based `Template*` execution tree, and the root-level novel planning artifacts used by research, character, workshop, and chapter-writing steps. Runtime files are produced later by workflow execution.

## Canonical Folder Shape

```text
.space/pipeline/book_<bookname>/
|-- TemplateLayOutShapeJson.json
|-- TemplateMetaJson.json
|-- TemplateModelJson.json
|-- TemplatePromptInitialText.txt
|-- TemplatePromptNextText.txt
|-- TemplatePromptSummaryText.txt
|-- sample.json
|-- book.json
|-- characters.json
|-- masterprompt.md
|-- workshop_metadata.md
|-- workshop_minutes/
|-- chapter_seeds/
|-- chapters_research/
`-- chapters/
    `-- chapter_1/
        |-- TemplateLayOutShapeJson.json
        |-- TemplateMetaJson.json
        |-- TemplateModelJson.json
        |-- TemplatePromptInitialText.txt
        |-- TemplatePromptNextText.txt
        |-- TemplatePromptSingleSegmentText.txt
        |-- TemplatePromptSummaryText.txt
        |-- moods/
        |-- spec/
        `-- segments/
            `-- segment_1/
                |-- TemplateLayOutShapeJson.json
                |-- TemplateMetaJson.json
                |-- TemplateModelJson.json
                |-- TemplatePromptInitialText.txt
                |-- TemplatePromptNextText.txt
                |-- TemplatePromptSummaryText.txt
                |-- writer/
                |-- editor/
                `-- translator/
```

## Path Invariant

This is mandatory.

- Never create `chapter_<n>/`, `chapter<n>/`, `chapterN/`, or `chapter_1/` directly under `book_<bookname>/`.
- Never create `segment_<x>/`, `segment<x>/`, `segmentN/`, or `segment_1/` directly under `book_<bookname>/` or under a root-level chapter folder.
- The only valid chapter path is `book_<bookname>/chapters/chapter_<n>/`.
- The only valid segment path is `book_<bookname>/chapters/chapter_<n>/segments/segment_<x>/`.
- The only valid writer/editor/translator paths are under `book_<bookname>/chapters/chapter_<n>/segments/segment_<x>/`.
- If an older scaffold contains `book_<bookname>/chapter_<n>/`, treat it as a misplaced legacy duplicate. Migrate or remove it only after confirming the canonical `book_<bookname>/chapters/chapter_<n>/` path exists.

## Scaffolded Files

Scaffold only template files that exist in the canonical template:

- `TemplateSystemPromptText.txt`
- `TemplateModelJson.json`
- `TemplateLayOutShapeJson.json`
- `TemplatePromptInitialText.txt`
- `TemplatePromptNextText.txt`
- `TemplatePromptSummaryText.txt`
- `TemplatePromptTranslateText.txt`
- `TemplatePromptSingleSegmentText.txt`

Not every folder contains every template file. Copy what exists in the matching canonical template folder.
## Root Planning Artifacts

These root-level planning artifacts are also required for a complete novel pipeline. They are scaffold artifacts, not optional generated clutter:

- `book.json` - the book structure, chapter list, chapter summaries, character references, and quality attributes.
- `characters.json` - the character roster extracted from or aligned with the book layout.
- `masterprompt.md` - the book-specific master prompt: identity, central premise, frame, style mandate, section structure, and references.
- `workshop_metadata.md` - workshop team, narrated-story figures, schedule, and grounding notes.
- `workshop_minutes/` - the destination for per-chapter workshop narratives.
- `chapter_seeds/` - the destination for per-chapter character and quality seeds.
- `chapters_research/` - the destination for per-chapter research JSON.

Create these for every novel scaffold. Seed them from the provided gist and from the book-level `TemplateLayOutShapeJson.json`; do not hard-code language, genre, characters, or chapter count.


## Runtime Files

Do not create runtime files during layout unless a later workflow step explicitly produces them:

- `Exception.txt`
- `SelfStateInitialJson.json`
- `SelfStateActivityJson.json`
- `ActualPromptAgentText.txt`
- `HumanInTheLoopPromptText.txt`
- `ModelDictionaryJson.json`
- `ReceivedAgentResponseText.txt`
- `ExtractedAgentResponseJson.json`
- `RunningContentSummaryText.txt`
- `TranslatedContentText.txt`
- `ReviwedContentText.txt`
- `ReturningModelJson.json`
- `FinalContentText.txt`
- `_history/`

## OperationState Map

Use this order and meaning when reasoning about file names:

| Value | State | File |
| ---: | --- | --- |
| 4 | `Exception` | `Exception.txt` |
| 11 | `SelfStateInitialJson` | `SelfStateInitialJson.json` |
| 12 | `SelfStateActivityJson` | `SelfStateActivityJson.json` |
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
| 90 | `ReturningModelJson` | `ReturningModelJson.json` |
| 100 | `FinalContentText` | `FinalContentText.txt` |
| 101 | `TemplatePromptSingleSegmentText` | `TemplatePromptSingleSegmentText.txt` |

## Scaffolding Steps

1. Determine `<bookname>` and `<gist>`. If no gist is supplied, infer a one-line premise from the book name.
2. Read `.space/templates/v1/fiction/book/` as the canonical template.
3. Create `.space/pipeline/book_<bookname>/`.
4. Copy only book-level `Template*` files and `sample.json`, if present, from the template root into the pipeline root.
5. Create the required root planning artifacts: `book.json`, `characters.json`, `masterprompt.md`, `workshop_metadata.md`, `workshop_minutes/`, `chapter_seeds/`, and `chapters_research/`.
6. Create `.space/pipeline/book_<bookname>/chapters/chapter_1/` by copying the canonical `chapters/chapter_1/` template folder.
7. Confirm `.space/pipeline/book_<bookname>/chapters/chapter_1/segments/segment_1/` exists after copying.
8. Confirm `writer/`, `editor/`, and `translator/` exist under the canonical `segment_1/` folder.
9. Seed the book-level `TemplateLayOutShapeJson.json` with the book identity, long title, genre, era, language, target audience, chapter count, summary, chapter list, character list, and history.
10. Seed `book.json` from the same layout data, preserving chapters, characters, and any quality attributes.
11. Seed `characters.json` from the layout character roster.
12. Seed `masterprompt.md` and `workshop_metadata.md` from the book identity, premise, chapter plan, style/register, and character/frame roles.
13. Seed `TemplateModelJson.json` with `book_summary`, `book_template_json`, `chapter_count`, and `chapter_summary_word_count`.
14. Seed `TemplateMetaJson.json` with `Name`, `Description`, `Type`, and `InstanceCount`.
15. Create `source/books/book_<bookname>/` as the destination for finished content.
16. Verify the path invariant and required planning artifacts before reporting completion.

## Book Layout JSON Responsibilities

At minimum, the book-level `TemplateLayOutShapeJson.json` should contain:

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
- The default `chapter_count` is 20 unless the user specifies another count.
- The layout plus root planning artifacts are the source of truth for book structure before writing begins.
- Do not overwrite existing book-specific content without first inspecting it.
- Do not delete misplaced legacy folders unless the user approves or the current task explicitly asks for cleanup and the canonical replacement exists.

## Pipeline Chain

```text
layout -> book architect -> chapter architect -> segment writer -> editor -> translator -> final book output
```

