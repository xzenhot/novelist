# Implementation Guide for the Writer Agent

This guide explains how to use the **writer agent**: a subject-agnostic literary engine that turns backlog epics, workshop narratives, and poetry topic lists into finished book chapters. It weaves three things at runtime: **Context** (reference and grounding), **Style** (the selected voice), and **Theme** (the selected thematic lens).

The authoritative engine lives in `.framework/workflows/write.md`. This guide is a practical map of that workflow, not a replacement for it.

> **Shared rule:** the filter concept is defined in `.framework/rules/filters.md` and applies to all workflows. Every book pipeline passes its material through ordered filters, each owning a folder in the pipeline.

---

## Architecture Overview

| File | Role |
|------|------|
| `.framework/workflows/write.md` | **The writing engine.** Defines commands, scaffolding, filter execution, form selection, config, and writing rules. |
| `.framework/skills/layout/SKILL.md` | **The layout authority.** Owns scaffold shape, templates, level state files, planning artifacts, OperationState mapping, and chapter/segment path invariants. |
| `.framework/skills/research/SKILL.md` | **The scaffold research step.** Runs after layout before chapters are written. |
| `.space/backlog/epic/<bookname>/epic.md` | **The backlog epic.** The single source of truth for a novel's story. Can be created independently with `gist`. |
| `.space/pipeline/book_<bookname>/` | **The book pipeline.** Holds model data, characters, filters, chapter plans, segments, and progress state. |
| `.space/pipeline/book_<bookname>/model.json` | **The book model.** Records form, gist, title, summary, source paths, stereotype selections, and poetry configuration. |
| `.space/pipeline/book_<bookname>/bookseed.txt` | **The poetry index.** One topic or term per line; each topic becomes one chapter. |
| `.framework/templates/stereotypes/<form>/` | **The stereotype templates.** Signatures, references, themes, qualities, and syntax samples for each form. |
| `source/books/book_<bookname>/` | **The finished book.** Chapters in `chapters/`, consolidated `book.md` at the root. |

To write a new book, scaffold a new pipeline under `.space/pipeline/` and write finished output under `source/books/`. The workflow file stays subject-agnostic.

---

## Command System

```text
Usage:
       /write <bookname> gist [<gist>]                                      # create backlog epic only
       /write <bookname> scaffold <gist> count|chapter-count <number> [--form novel|poetry]
       /write <bookname> chapter <chapter>|<n>|all|continue                 # write chapters
       /write <bookname> filter <filter>|*|all                              # run filters
       /write <bookname> form <formname>                                    # set/change form
       /write <bookname> config [<key> [<value>]]                           # get/set model config
       /write <bookname> config show                                        # show model config
       /write -h | --help                                                   # show help
       /write -o | --options                                                # list books and chapters
```

| Command | What it does |
|---------|--------------|
| `gist [<gist>]` | Creates or updates only `.space/backlog/epic/<bookname>/epic.md`. It does **not** scaffold a pipeline. |
| `scaffold <gist> count|chapter-count <number>` | Creates or repairs the canonical v1 segment-based pipeline using the layout skill, then runs research. |
| `chapter <chapter>\|<n>\|all\|continue` | Writes one chapter, a numbered chapter, all chapters, or the remaining missing chapters. |
| `filter <filter>\|*\|all` | Runs a single filter, or all filters in order, on an existing pipeline. |
| `form <formname>` | Sets or changes the pipeline form (`novel` or `poetry`). |
| `config [<key> [<value>]]` | Gets or sets stereotype/model config such as `signature`, `reference`, `theme_set`, or `syntax`. |
| `config show` | Prints the current model configuration. |
| `options` | Lists available book pipelines and destinations. |
| `help` | Shows command usage. |

---

## Command Rules

- Use `gist` for early backlog work only. It creates or updates the epic and never creates `.space/pipeline/book_<bookname>/`.
- Use `scaffold` to create the full pipeline. The gist is required and must be a single sentence.
- `scaffold` requires `count` or `chapter-count` followed by the main chapter count. If no count is provided by the user, the workflow default is 5.
- Once a pipeline exists, subsequent commands work from pipeline data. Do not re-scaffold from scratch unless explicitly asked.
- `filter` never scaffolds. If the pipeline does not exist, report that the book must be scaffolded first.
- `filter *` and `filter all` mean "run the full ordered filter chain."
- `chapter continue` resumes from the first missing finished chapter under `source/books/book_<bookname>/chapters/`.
- A specific chapter request writes only that chapter, even if earlier chapters are incomplete.

---

## The Form Discriminator

A book is either a **novel** (prose) or **poetry** (verse). The form is stored in the pipeline's `form` field and drives source-of-truth files, filter order, chapter structure, word target, and stereotype templates.

```json
// model.json
"form": "novel"
```

| Signal | Novel | Poetry |
|---|---|---|
| **`form` field** | `"novel"` | `"poetry"` |
| **Source of truth** | `epic.md` | `model.json` + `bookseed.txt` |
| **Chapter structure** | Workshop / Story / Discussion | Question / Oration / Benediction |
| **Segments per chapter** | many (`segments/1`, `segments/2`, ...) | exactly one (`segments/1`) |
| **`mood.json`** | present per chapter | absent |
| **Filter chain** | 8 filters | 6 filters |
| **Word target** | 5,500+ words | 500-800 words |
| **Stereotype templates** | `stereotypes/novel/` | `stereotypes/poetry/` |

---

## Pipeline Layout

Pipeline structure is owned by `.framework/skills/layout/SKILL.md`. When scaffolding, creating, or repairing `.space/pipeline/book_<bookname>/`, read and follow the layout skill.

Mandatory path invariant:

- chapters live only at `.space/pipeline/book_<bookname>/chapters/<n>/`
- segments live only at `.space/pipeline/book_<bookname>/chapters/<n>/segments/<x>/`
- never create root-level `<n>/` or `<x>/` folders under the book pipeline

`.framework/templates/SCAFFOLD.md` is a short reference note only; do not treat it as the primary scaffold instruction source.

---

## Scaffolding Flow

For `/write <bookname> scaffold <gist> count|chapter-count <number> [--form novel|poetry]`:

1. Check whether `.space/pipeline/book_<bookname>/` exists.
2. If it exists, work with the existing pipeline data.
3. If it does not exist, determine the form from `--form` or by inference.
4. Validate that the gist is a single sentence.
5. Determine the chapter count; default to 5 if the user supplied no count.
6. For a novel, create or read `.space/backlog/epic/<bookname>/epic.md`.
7. Summarize the epic into an indicative single-sentence gist and a 5-10 sentence `book_summary`.
8. Run the layout skill to create or repair the canonical pipeline.
9. Apply form-specific initialization in `model.json` and related files.
10. Run the research skill before writing any chapter.

---

## The Gist Command

For `/write <bookname> gist [<gist>]`:

1. Create or update `.space/backlog/epic/<bookname>/epic.md`.
2. Infer a one-sentence gist from the book name if none is supplied.
3. For a novel, create or update the epic from the gist.
4. For poetry, create or update a minimal epic placeholder.
5. Do not create `.space/pipeline/book_<bookname>/`, do not run layout, and do not run research.

Every novel epic should include a metadata block near the top with title, book name, epic path, timestamps, authoring engine, language, genre, era, chapter count, and gist. When the epic changes, keep the metadata block current and regenerate the pipeline gist from the epic.

---

## Filter Chains

The filter chain depends on the form.

**Novel (8 filters):**

```text
workshop -> research -> seeds -> correctness -> theme -> syntax -> override -> quality
```

| Filter | Agent | Folder |
|--------|-------|--------|
| workshop | `.framework/agents/workshop/agent.md` | `filters/1_workshop/` |
| research | `.framework/agents/research/agent.md` | `filters/2_research/` |
| seeds | `.framework/agents/seeds/agent.md` | `filters/3_seeds/` |
| correctness | `.framework/agents/correctness/agent.md` | `filters/4_correctness/` |
| theme | `.framework/agents/theme/agent.md` | `filters/5_theme/` |
| syntax | `.framework/agents/syntax/agent.md` | `filters/6_syntax/` |
| override | `.framework/agents/override/agent.md` | `filters/7_override/` |
| quality | `.framework/agents/quality/agent.md` | `filters/8_quality/` |

**Poetry (6 filters):**

```text
research -> correctness -> theme -> syntax -> override -> quality
```

| Filter | Skill | Folder |
|--------|-------|--------|
| research | `.framework/skills/research/SKILL.md` | `filters/research/` |
| correctness | `.framework/skills/correctness/SKILL.md` | `filters/correctness/` |
| theme | `.framework/skills/theme/SKILL.md` | `filters/theme/` |
| syntax | `.framework/skills/syntax/SKILL.md` | `filters/syntax/` |
| override | human-editable `override.md` | `filters/override/` |
| quality | `.framework/skills/quality/SKILL.md` | `filters/quality/` |

Each filter reads the pipeline data and any upstream filter output it needs, then writes to its own folder. Run the full chain strictly in order.

---

## Stereotype Selection

Every chapter is rendered in a form-specific stereotype:

- **Signature:** `stereotypes/<form>/signatures/`
- **Reference:** `stereotypes/<form>/references/`
- **Theme set:** `stereotypes/<form>/themes/`
- **Quality profile:** `stereotypes/<form>/qualities/`
- **Syntax sample:** `stereotypes/<form>/syntax/`

Read the `registry.md` in each folder to discover available options, then read the chosen file for the full definition. Selections must be mutually consistent: same form, and where possible the same author or tradition.

---

## Writing Rules

### Novel

Novel workshop files contain three sections:

1. **Section 1 - Workshop:** the modern frame scene.
2. **Section 2 - Story:** the main historical or fictional story.
3. **Section 3 - Discussion:** the characters' response.

Preserve all three sections. Keep Section 1 and Section 3 unchanged. Rewrite Section 2 in the selected style and target language, using the epic, filter outputs, included characters, and quality parameters as source material.

### Poetry

Each poetry chapter is a single **Question -> Oration -> Benediction** unit, generated from one topic in `bookseed.txt`, grounded in `model.json`, and rendered in the selected poetic voice.

For both forms:

- Use the output language from the pipeline, user request, or config.
- Do not assume Bengali, English, or any other language by default.
- Write in a serious, image-rich literary register unless the pipeline overrides it.
- Meet the configured word target: default 5,500+ words for novel Story sections, 500-800 words for poetry.
- Count words after writing and expand if the chapter is too short.
- End chapters with a running summary or narrative handoff that sustains curiosity.

---

## Output Layout

Finished chapters live in a `chapters/` subfolder, and the consolidated book lives at the book root.

```text
source/books/book_<bookname>/
|-- book.md
`-- chapters/
    |-- Introduction.md
    |-- 1.md ... N.md
    `-- Conclusion.md
```

For poetry, chapter filenames follow the generated topic/chapter naming from `bookseed.txt`.

After all chapters are written, assemble `book.md` at the book root:

1. Open with the book title (`book_long_title`) and gist epigraph.
2. Append every chapter in order.
3. Separate chapters with `---` dividers.
4. Ensure both Introduction and Conclusion exist for novel output.

---

## Progress Tracking

Always inspect the pipeline and `source/books/book_<bookname>/chapters/` before writing. The agent resumes from existing state and never restarts from the beginning unless explicitly asked.

Use:

- `/write <bookname> chapter continue` to write the first missing chapter onward.
- `/write <bookname> chapter all` to write every chapter in canonical order and assemble `book.md`.
- `/write <bookname> filter *` to refresh the full filter chain before chapter writing.

