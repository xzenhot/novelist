---
name: layout-novel
description: "Use when scaffolding or repairing the structural skeleton of a novel pipeline. Creates .space/pipeline/book_<bookname>/, root planning JSON/Markdown, named filter folders, chapter folders, segment folders, and the empty source/books destination. Does not write finished prose or runtime filter results."
---

# Layout Novel - Pipeline Scaffold

You are the structural architect for a novel pipeline. Create only the scaffold and planning artifacts needed before workshop, research, writing, editing, translation, filtering, and final assembly begin.

A scaffolded novel lives at:

```text
.space/pipeline/book_<bookname>/
```

Finished content later lives at:

```text
source/books/book_<bookname>/
```

## Source Of Truth

Use this skill together with `.framework/workflows/write.md`. Do not inspect existing book pipelines such as `.space/pipeline/book_wife/` to discover or imitate layout conventions; existing books may be legacy, experimental, or partially migrated.

If this skill conflicts with `.framework/workflows/write.md`, prefer the workflow for command semantics and filter-chain naming, then update this skill. Do not resolve conflicts by sampling another book pipeline.

For novel story content, use the backlog epic:

```text
.space/backlog/epic/<bookname>/epic.md
```

The epic is the narrative source of truth. The scaffold may summarize and structure it, but must not invent a different story.

## Canonical Folder Shape

```text
.space/pipeline/book_<bookname>/
|-- model.json
|-- book.json
|-- characters.json
|-- masterprompt.md
|-- workshop_metadata.md
|-- progress.json
|-- filters/
|   |-- filters.json
|   |-- workshop/
|   |   |-- workshop.md
|   |   |-- filter.md
|   |   |-- filter-summary.md
|   |   `-- content-output.md
|   |-- research/
|   |-- seeds/
|   |-- correctness/
|   |-- theme/
|   |-- syntax/
|   |-- override/
|   `-- quality/
`-- chapters/
    |-- Introduction/
    |   |-- model.json
    |   |-- mood.json
    |   |-- chapter.md
    |   `-- segments/
    |       `-- 1/
    |           |-- model.json
    |           |-- writer/
    |           |-- editor/
    |           `-- translator/
    |-- 1/
    |-- ...
    `-- Conclusion/
```

Every filter folder uses the same four-file shape as `workshop/`, with the role file named after the folder, for example `research/research.md`.

## Path Invariant

This is mandatory.

- Chapter folders live only under `.space/pipeline/book_<bookname>/chapters/`.
- Segment folders live only under `.space/pipeline/book_<bookname>/chapters/<chapter>/segments/`.
- Writer, editor, and translator folders live only under `.space/pipeline/book_<bookname>/chapters/<chapter>/segments/<segment>/`.
- Do not create root-level chapter folders under `.space/pipeline/book_<bookname>/`.
- Do not create `chapter_<n>` or `segment_<n>` folders in new scaffolds; use `1`, `2`, etc.
- If repairing legacy folders, rename only after confirming there is no collision and no user-authored content will be overwritten.

## Chapter Set

For novels, scaffold this order:

```text
Introduction -> 1..N -> Conclusion
```

`N` is the requested main `chapter_count`; default to 5 when the command gives no count.

Each chapter gets exactly one initial segment, `segments/1/`. Later workflows may add more segments if explicitly required.

Each chapter gets one `mood.json` selected from `.framework/templates/moods/`:

- `Introduction`: use `introduction.json`
- `Conclusion`: use `conclusion.json`
- Numbered chapters: use an appropriate mood for the chapter arc, or `default.json` when no stronger choice is justified

Do not copy a mood-template directory into the pipeline.

## Root Files

Create these at the pipeline root.

### `model.json`

Minimum fields:

- `form`: `novel`
- `gist`
- `epic_path`
- `book_long_title`
- `book_summary`
- `language`
- `genre`
- `era`
- `chapter_count`
- `stereotype`
- `syntax`

### `book.json`

Minimum fields:

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

Each `chapters` item must include:

- `chapter_index`
- `name`
- `chapter_title`
- `chapter_summary`

Each `all_characters` item must include:

- `character_id`
- `full_name`
- `role`
- `identity`
- `psychological_depth` or another clearly named depth field

### `characters.json`

Use the same character roster as `book.json`, expanded only when useful for later chapter planning.

### `masterprompt.md`

Record the book identity, premise, epic source path, form, language, style mandate, chapter structure, and central conflict.

### `workshop_metadata.md`

Record the workshop frame, recurring workshop roles, narrated-story figures, schedule/sequence notes, and grounding notes.

### `progress.json`

Track Introduction, every numbered chapter, and Conclusion.

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

For a new scaffold, set all statuses to `pending`, `completed_chapters` to `0`, and `completed_date` to `null`.

## Chapter And Segment State

Create `model.json` in every chapter folder and every segment folder.

Chapter-level `model.json` should include the chapter identity and initial planning data:

- `chapter_index`
- `chapter_name`
- `state`
- `chapter_title`
- `subject`
- `era`
- `place`
- `figures`
- `events`
- `grounding_notes`
- `sources`
- `included_characters`
- `quality_parameters`
- `chapter_summary`
- `mood`
- `segments`
- `stereotype`
- `theme`
- `syntax`
- `workshop_file`
- `research_file`

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

Before creating the filter registry, read `.space/backlog/epic/<bookname>/preset.md`. If it does not exist, invoke the configure agent (`.framework/agents/configure/agent.md`) to create it from the form-specific default template. The configure agent will also create/confirm the preset file.

Use the ordered filter/agent list declared in the resulting preset as the canonical filter chain. If for any reason the preset cannot be read or created, fall back to the default novel chain:

```text
workshop -> research -> seeds -> correctness -> theme -> syntax -> override -> quality
```

Create `.space/pipeline/book_<bookname>/filters/filters.json` with the selected chain in order.

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

**Override command file (novel customization):** the `override` filter is the one structural exception. Its exact seeding content is **dynamically derived at scaffold time** from the novel stereotype index at `.framework/templates/stereotypes/novel/readme.md` — do not treat this paragraph as the fixed recipe. Before you create the override files, read that readme and let it govern the shape:

1. **Read `.framework/templates/stereotypes/novel/readme.md`** — the master index of the novel stereotype folder. It tells you the canonical contents and conventions: the `qualities/` (seed analyses), `references/` (source texts), `signatures/` (prose voices), `syntax/`, and `themes/` sub-indexes. Use the readme's published conventions as the source of truth for how a novel pipeline's override layer is structured.
2. **Seed the pipeline override command file from the readme's declared structure.** The human-facing command file for a novel pipeline is `.space/pipeline/book_<bookname>/filters/override/filter.md` — recreate it with the agent-driven role content (see step 3) and leave the `## Instructions` section empty for the human below the `---` line.
3. **Derive the role content from `.framework/agents/override/agent.md`**, customized to the novel form per the readme conventions: identity "novel pipeline", applies to every chapter (Workshop/Story/Discussion), command file at `.space/pipeline/book_<bookname>/filters/override/filter.md`, model updates on `.space/pipeline/book_<bookname>/chapters/<n>/model.json`, instruction scope "every chapter" (`Introduction`, `1..N`, `Conclusion`).
4. **Align with whatever the readme's sub-indexes declare** (the prose voice/signature set, reference texts, syntax samples, and theme sets under `signatures/`, `references/`, `syntax/`, `themes/`) — the override layer must not contradict the stereotype set the pipeline will use.
5. Leave the trailing `## Instructions` section empty below the `---` line and never overwrite existing human instructions there.

**Important:** Only create filter folders and registry entries for filters named in the selected preset. Do not create folders for default filters that the preset omits. The order must match the preset exactly.

## Source Destination

Create:

```text
source/books/book_<bookname>/chapters/
```

Do not write finished chapters or `book.md` during layout.

## Verification

Before reporting completion, verify:

- Root files exist: `model.json`, `book.json`, `characters.json`, `masterprompt.md`, `workshop_metadata.md`, `progress.json`.
- `filters/filters.json` exists and names the filters selected from `preset.md` (or all eight default novel filters if no preset exists) in the exact order declared.
- Every filter folder selected from the preset has its role file, `filter.md`, `filter-summary.md`, and `content-output.md`.
- Every chapter in `Introduction -> 1..N -> Conclusion` has `model.json`, `mood.json`, `chapter.md`, and `segments/1/model.json`.
- Every `segments/1/` has `writer/`, `editor/`, and `translator/` folders.
- No chapter or segment folders were created outside the canonical paths.
- `source/books/book_<bookname>/chapters/` exists and contains no unfinished generated prose unless a later workflow created it.
