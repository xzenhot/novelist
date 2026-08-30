# Novel Scaffolding Logic — v1

This document captures the **scaffolding logic** for a novel pipeline. It is the reference for reproducing the folder/file structure of a book (originally observed in `.space/templates/UJANGARH/book1/`, now canonicalized under `.space/templates/v1/fiction/book/`).

The engine is a **segment-based workflow**: a book is divided into chapters, each chapter into segments, and each segment passes through three agents — **writer → editor → translator**.

---

## OperationState — the authoritative file-name order and meaning

Every file in a book/chapter/segment folder corresponds to a value of the `OperationState` enum. The enum value is the **order** of the file in the workflow, and its comment is the **meaning**. This is the single source of truth for what each file is and when it is produced.

| Value | Name | Meaning (verbatim from the `OperationState` enum) |
|------:|------|---------|
| 0 | `None` | Initial state, no operation performed yet. |
| 4 | `Exception` | If any error happens during the execution of an activity, the error message will be stored in this state. This can be used by model to decide how to fix the error and continue the execution. |
| 10 | `InputModelJson` | Not used so far. |
| 11 | `SelfStateInitialJson` | Initial model, which may be modified. |
| 12 | `SelfStateActivityJson` | StrongType - State checksum. |
| 20 | `TemplateSystemPromptText` | *(no comment in source)* |
| 22 | `TemplateModelJson` | These dictionary comes from initialize section, never updated. Used to pass parameters to template. |
| 23 | `TemplateLayOutShapeJson` | Example Schema for template layout, which may be used by model to understand how to fill the content. |
| 24 | `TemplatePromptInitialText` | Initial template prompt text created by template, first item of an array of prompt text, which may be modified by model. |
| 25 | `TemplatePromptNextText` | Next template prompt text created by template, which may be modified by model. |
| 26 | `TemplatePromptSummaryText` | Summary template prompt text created by template, which may be modified by model. |
| 27 | `TemplatePromptTranslateText` | *(no comment in source)* |
| 30 | `ActualPromptAgentText` | While executing agent, this is the actual prompt text sent to model, which may be modified by model before sending to next agent. |
| 31 | `HumanInTheLoopPromptText` | While executing agent, this is the actual prompt text sent to model with human in the loop, which may be modified by model before sending to next agent. |
| 32 | `ModelDictionaryJson` | Actual parameters used to create actual prompt, which may be modified by model before sending to next agent. |
| 50 | `ReceivedAgentResponseText` | Raw response text received from model, which may be modified by model before sending to next agent. |
| 60 | `ExtractedAgentResponseJson` | Parsed response in json format received from model, which may be modified by model before sending to next agent. |
| 82 | `RunningContentSummaryText` | Calculated summary text based on model response and content, which may be modified by model before sending to next agent. |
| 83 | `TranslatedContentText` | *(no comment in source)* |
| 84 | `ReviwedContentText` | *(no comment in source)* |
| 90 | `ReturningModelJson` | Last object returned from an method of an activity method of a workflow. This is the final output of an activity. This can not be modified. |
| 100 | `FinalContentText` | Final content text after an activity. This is the final output of an activity. This can not be modified. |
| 101 | `TemplatePromptSingleSegmentText` | *(no comment in source)* |

### File-name → state mapping

| File name | State | Value |
|-----------|-------|------:|
| `Exception.txt` | `Exception` | 4 |
| `SelfStateInitialJson.json` | `SelfStateInitialJson` | 11 |
| `SelfStateActivityJson.json` | `SelfStateActivityJson` | 12 |
| `TemplateSystemPromptText.txt` | `TemplateSystemPromptText` | 20 |
| `TemplateModelJson.json` | `TemplateModelJson` | 22 |
| `TemplateLayOutShapeJson.json` | `TemplateLayOutShapeJson` | 23 |
| `TemplatePromptInitialText.txt` | `TemplatePromptInitialText` | 24 |
| `TemplatePromptNextText.txt` | `TemplatePromptNextText` | 25 |
| `TemplatePromptSummaryText.txt` | `TemplatePromptSummaryText` | 26 |
| `TemplatePromptTranslateText.txt` | `TemplatePromptTranslateText` | 27 |
| `ActualPromptAgentText.txt` | `ActualPromptAgentText` | 30 |
| `HumanInTheLoopPromptText.txt` | `HumanInTheLoopPromptText` | 31 |
| `ModelDictionaryJson.json` | `ModelDictionaryJson` | 32 |
| `ReceivedAgentResponseText.txt` | `ReceivedAgentResponseText` | 50 |
| `ExtractedAgentResponseJson.json` | `ExtractedAgentResponseJson` | 60 |
| `RunningContentSummaryText.txt` | `RunningContentSummaryText` | 82 |
| `TranslatedContentText.txt` | `TranslatedContentText` | 83 |
| `ReviwedContentText.txt` | `ReviwedContentText` | 84 |
| `ReturningModelJson.json` | `ReturningModelJson` | 90 |
| `FinalContentText.txt` | `FinalContentText` | 100 |
| `TemplatePromptSingleSegmentText.txt` | `TemplatePromptSingleSegmentText` | 101 |

### Which files are scaffolded vs. runtime

- **Scaffolded (template files, present in the canonical template):** `TemplateSystemPromptText`, `TemplateModelJson`, `TemplateLayOutShapeJson`, `TemplatePromptInitialText`, `TemplatePromptNextText`, `TemplatePromptSummaryText`, `TemplatePromptTranslateText`, `TemplatePromptSingleSegmentText`.
- **Runtime (produced during execution, NOT scaffolded):** `Exception`, `SelfStateInitialJson`, `SelfStateActivityJson`, `ActualPromptAgentText`, `HumanInTheLoopPromptText`, `ModelDictionaryJson`, `ReceivedAgentResponseText`, `ExtractedAgentResponseJson`, `RunningContentSummaryText`, `TranslatedContentText`, `ReviwedContentText`, `ReturningModelJson`, `FinalContentText`.

---

## Folder Hierarchy

```
book_<bookname>/                          # the pipeline root (under .space/pipeline/)
├── TemplateLayOutShapeJson.json          # book layout schema (the seed shape)
├── TemplateMetaJson.json                 # book metadata (Name, Description, Type, InstanceCount)
├── TemplateModelJson.json                # book model (book_summary, chapter_count, ...)
├── TemplatePromptInitialText.txt         # prompt: architect the full book layout from the seed
├── TemplatePromptNextText.txt            # prompt: extend the layout with the next chapters
├── TemplatePromptSummaryText.txt         # prompt: produce a running summary
└── chapter1/ … chapterN/                # one folder per chapter
    ├── TemplateLayOutShapeJson.json      # chapter layout schema (segments, references, characters)
    ├── TemplateMetaJson.json
    ├── TemplateModelJson.json
    ├── TemplatePromptInitialText.txt     # prompt: write the first episode (chapter)
    ├── TemplatePromptNextText.txt        # prompt: write the next episode
    ├── TemplatePromptSingleSegmentText.txt
    ├── TemplatePromptSummaryText.txt
    ├── moods/                            # mood JSON files (default, introduction, conclusion, ...)
    │   ├── default.json
    │   ├── introduction.json
    │   ├── conclusion.json
    │   ├── love.json / fight.json / thriller.json / sadstory.json / ...
    ├── spec/                             # chapter writing spec (optional)
    │   └── default.md
    └── segment1/ … segmentN/             # one folder per segment
        ├── TemplateLayOutShapeJson.json  # segment layout schema (segment_content, total_words)
        ├── TemplateMetaJson.json
        ├── TemplateModelJson.json
        ├── TemplatePromptInitialText.txt
        ├── TemplatePromptNextText.txt
        ├── TemplatePromptSummaryText.txt
        ├── writer/                       # segment writer agent
        │   ├── TemplateLayOutShapeJson.json
        │   ├── TemplateMetaJson.json
        │   ├── TemplateModelJson.json
        │   ├── TemplatePromptInitialText.txt
        │   ├── TemplatePromptNextText.txt
        │   ├── TemplatePromptSingleSegmentText.txt
        │   └── TemplatePromptSummaryText.txt
        ├── editor/                       # segment editor agent
        │   ├── TemplateLayOutShapeJson.json
        │   ├── TemplateMetaJson.json
        │   ├── TemplateModelJson.json
        │   ├── TemplatePromptInitialText.txt
        │   ├── TemplatePromptNextText.txt
        │   └── TemplatePromptSummaryText.txt
        └── translator/                   # segment translator agent
            ├── TemplateLayOutShapeJson.json
            ├── TemplateMetaJson.json
            ├── TemplateModelJson.json
            ├── TemplatePromptInitialText.txt
            ├── TemplatePromptNextText.txt
            ├── TemplatePromptSummaryText.txt
            └── TemplateSystemPromptText.txt
```

---

## JSON Schemas (the `*.json` files)

### 1. Book level — `TemplateLayOutShapeJson.json`

The book layout seed. Holds the book identity, the chapter list, the character roster, and the running history.

```json
{
  "book_name": "SOMEENGLISH",
  "book_long_title": "Provide a long title",
  "generic": "Historical Epic / Nationalist Literature",
  "era": "590AD-625AD",
  "language": "Bengali",
  "target_audience": "general public, history enthusiasts, students",
  "chapter_count": 2,
  "created_at": "2026-04-22",
  "user_name": "pijush",
  "book_summary": "We will get this line from the user",
  "chapters": [
    {
      "chapter_index": 1,
      "name": "Chapter 1",
      "chapter_title": "Title of first part of the chapter",
      "chapter_summary": "Summary of the description of the first part of the chapter."
    }
  ],
  "all_characters": [
    {
      "character_id": 1,
      "full_name": "Name of something",
      "role": "What that character does",
      "identity": { "age": 45, "sex": "Male", "caste": "Brahmin" },
      "psychological_depth": "Fearless warrior, shrewd diplomat."
    }
  ],
  "history": [
    { "chapter_count": 2, "running_summary": "The following chapters" }
  ]
}
```

> Note: `UJANGARH/book1` used `friendly_name`; the canonical `v1/fiction` template uses `full_name`. Use `full_name`.

### 2. Book level — `TemplateMetaJson.json`

```json
{
  "Name": "LAXMANSEN",
  "Description": "The Conquest of Kannauj: ...",
  "Type": "history",
  "InstanceCount": 1
}
```

### 3. Book level — `TemplateModelJson.json`

```json
{
  "book_summary": "",
  "book_template_json": "",
  "chapter_count": 2,
  "chapter_summary_word_count": 400
}
```

### 4. Chapter level — `TemplateLayOutShapeJson.json`

```json
{
  "chapter_index": 1,
  "chapter_segments": [
    {
      "segment_index": 1,
      "name": "segment-1",
      "segment_title": "Goal - What is the aim of the segment",
      "segment_summary": "Create segment Summary with minimum 400 words. Mention the characters to play here."
    }
  ],
  "references": [
    { "no": "1", "reference": "Get the reference from internet", "weblink": "actual url" }
  ],
  "additional_characters": [
    {
      "character_id": 1,
      "full_name": "Name of something",
      "role": "What that character does",
      "identity": { "age": 45, "sex": "Male", "caste": "Brahmin" },
      "psychological_depth": "Fearless warrior, shrewd diplomat."
    }
  ]
}
```

### 5. Chapter level — `TemplateModelJson.json`

```json
{
  "book_summary": "",
  "chapter_summary": "",
  "chapter_template_json": "",
  "number_of_segments": 8,
  "list_of_paragraphs": "8 lines ended by newline"
}
```

### 6. Segment level — `TemplateLayOutShapeJson.json`

The finished segment content shape.

```json
{
  "segment_index": 1,
  "segment_title": "Awakening",
  "segment_mood": "Inspiring, patriotic, hopeful",
  "total_words": 1500,
  "segment_content": "The early part of the twentieth century. India was still bound..."
}
```

### 7. Segment level — `TemplateModelJson.json`

```json
{
  "book_summary": "",
  "chapter_summary": "",
  "segment_index": "",
  "segment_summary": "",
  "segment_template_json": ""
}
```

### 8. Writer agent — `TemplateLayOutShapeJson.json`

The writer's output shape (what the writer returns per segment).

```json
{
  "total_words": "Count of total words. Integer type.",
  "segment_content": "Full content of the segment. This is a long text. String type",
  "language": "The last two sentences of the segment. String type."
}
```

### 9. Writer agent — `TemplateModelJson.json`

```json
{
  "book_summary": "",
  "chapter_summary": "",
  "chapter_index": 1,
  "segment_index": "",
  "segment_summary": "",
  "segment_template_json": "",
  "previous_segment_last_sentences": ""
}
```

### 10. Editor agent — `TemplateLayOutShapeJson.json`

The editor's scoring output shape.

```json
{
  "scores": {
    "language": 0.0,
    "clarity": 0.0,
    "style": 0.0,
    "quality": 0.0,
    "length_score": 0.0
  },
  "total_score_percentage": 0.0,
  "status": "string",
  "critique_en": "Short explanation of the score in English",
  "critique_bn": "Short explanation of the score in Bengali"
}
```

### 11. Translator agent — `TemplateLayOutShapeJson.json`

```json
{
  "source_language": "detected_language",
  "target_language": "target_language",
  "translation": "translated text."
}
```

---

## The Workflow (book → chapter → segment → writer/editor/translator)

1. **Book layout** — `TemplatePromptInitialText.txt` architects the full book (chapters, characters, summaries) from the seed (`book_summary`), returning the book layout JSON.
2. **Chapter** — `TemplatePromptInitialText.txt` writes the first episode; `TemplatePromptNextText.txt` writes subsequent episodes. Each chapter is divided into `number_of_segments` segments.
3. **Segment** — each segment is written by the **writer** agent (`TemplatePromptInitialText.txt` for the first segment, `TemplatePromptNextText.txt` for continuations), then scored by the **editor** agent, then translated by the **translator** agent.
4. **Running summary** — `TemplatePromptSummaryText.txt` merges new text into a running summary at every level (book, chapter, segment).

### Runtime artifacts (produced during execution, not scaffolded)

The `UJANGARH/book1` instance also contained runtime files written during execution — these are **not** part of the scaffold, only the `Template*` files are. See the **OperationState** table above for the authoritative order and meaning of every file. The runtime files are:

- `Exception.txt`, `SelfStateInitialJson.json`, `SelfStateActivityJson.json`
- `ActualPromptAgentText.txt`, `HumanInTheLoopPromptText.txt`, `ModelDictionaryJson.json`
- `ReceivedAgentResponseText.txt`, `ExtractedAgentResponseJson.json`
- `RunningContentSummaryText.txt`, `TranslatedContentText.txt`, `ReviwedContentText.txt`
- `ReturningModelJson.json`, `FinalContentText.txt`
- `_history/` (chat.json, _storage_keys.txt)

---

## Scaffolding Steps (summary)

1. Read the canonical template at `.space/templates/v1/fiction/book/`.
2. Create `.space/pipeline/book_<bookname>/` with the book-level `Template*` files.
3. For each chapter, create `chapterN/` with the chapter-level `Template*` files, plus `moods/` and `spec/`.
4. For each segment, create `segmentN/` with the segment-level `Template*` files, plus `writer/`, `editor/`, `translator/` subfolders (each with their own `Template*` files).
5. Seed `TemplateLayOutShapeJson.json` (book level) with the `<gist>` — book_name, book_long_title, book_summary, chapters, all_characters.
