# Implementation Guide for the Writer Agent

This guide explains how to use the **writer agent**: a subject-agnostic literary engine that turns backlog epics, workshop narratives, and poetry topic lists into finished book chapters. It weaves three things at runtime: **Context** (reference and grounding), **Style** (the selected voice), and **Theme** (the selected thematic lens).

The authoritative engine lives in `.framework/workflows/book.md`. This guide is a practical map of that workflow, not a replacement for it.

> **Shared rule:** the filter concept is defined in `.framework/rules/filters.md` and applies to all workflows. Every book pipeline passes its material through ordered filters, each owning a folder in the pipeline.

---

## Architecture Overview

| File | Role |
|------|------|
| `.framework/workflows/book.md` | **The writing engine.** Defines commands, scaffolding, filter execution, form selection, config, and writing rules. |
| `.framework/skills/layout-novel/SKILL.md` | **The novel layout authority.** Owns novel scaffold shape, `book.json`, characters, moods, workshop metadata, filters, and chapter/segment path invariants. |
| `.framework/skills/layout-poetry/SKILL.md` | **The poetry layout authority.** Owns poetry scaffold shape, `model.json`, `bookseed.txt`, progress, override, filters, and one-segment chapter layout. |
| `.framework/skills/research/SKILL.md` | **The scaffold research step.** Runs after layout before chapters are written. |
| `.space/backlog/epic/<bookname>/epic.md` | **The backlog epic.** The single source of truth for a novel's story. Created/updated by the bare `/book <bookname> [<gist>]` command. |
| `.space/backlog/epic/<bookname>/book.json` | **The backlog book plan.** The chapter-layout plan (chapters, titles, summaries, characters) plus the authoritative `filter_chain` and `word_target`. Produced by `init`; the blueprint `scaffold` builds from. |
| `.space/pipeline/<bookname>/` | **The book pipeline.** Holds model data, characters, filters, chapter plans, segments, and progress state. |
| `.space/pipeline/<bookname>/model.json` | **The book model.** Records form, gist, title, summary, source paths, stereotype selections, and poetry configuration. |
| `.space/pipeline/<bookname>/bookseed.txt` | **The poetry index.** One topic or term per line; each topic becomes one chapter. |
| `.framework/templates/stereotypes/<form>/` | **The stereotype templates.** Signatures, references, themes, qualities, and syntax samples for each form. |
| `source/books/<bookname>/` | **The finished book.** Chapters in `chapters/`, consolidated `book.md` at the root. |

To write a new book: prepare the backlog with the bare `/book <bookname> [<gist>]` command and `init`/`backlog`, scaffold the pipeline under `.space/pipeline/`, run the filter chain, and write finished output under `source/books/`. The workflow file stays subject-agnostic.

---

## Command System

```text
Usage:
    /book <bookname>                                                     # 1. create backlog epic if missing
    /book <bookname> [<gist>] [form] [refresh]                           # 1. create/update or rewrite the backlog epic (gist merged)
    /book <bookname> init|backlog [<gist>] [<preset>] [form] [refresh]    # 2. configure the backlog (backlog only, no pipeline)
    /book <bookname> scaffold <gist> count|chapter-count <number> [--form novel|poetry]
                                                                            # 3. scaffold the pipeline (requires init)
    /book <bookname> <agentname> <chapter>|<n>|all|continue              # 4. run any registered agent on chapters
    /book <bookname> poet|poetry|poem                                    # run the poet agent (poetry only)
    /book <bookname> write <n>|all|continue                               # 5. write chapters
    /book <bookname> filter <filter>|*|all                               # 6. run filters
    /book <bookname> form <formname>                                     # 7. set/change form
    /book <bookname> config [<key> [<value>]]                            # 8. get/set model config (bare = show config)
    /book <bookname> add <chapter-count> filter <filter>|*|all           # 9. add chapters and run filter(s)
    /book -o | --options                                                 # 10. list books and chapters
    /book -h | --help                                                    # 11. show help
    /book <bookname> layout|pipeline [<count>]                           # 12. re-create book.json from epic.md with 200-word summaries (count defaults to 5)
```

| Command | What it does |
|---------|--------------|
| `<bookname> [<gist>] [form] [refresh]` | Creates, updates, or rewrites `.space/backlog/epic/<bookname>/epic.md` (recording the seed in `gist.md`) and develops it into a rich, detailed narrative foundation. If gist omitted, infers from book name. If `[form]` supplied, changes the book's form. Does **not** scaffold a pipeline. The former `gist` subcommand is merged into this command. |
| `init [<gist>] [<preset>] [form] [refresh]` (alias: `backlog`) | Fully configures the backlog epic folder — `gist.md`, `epic.md`, `book.json` — and derives the ordered filter chain (stored in `book.json`'s `filter_chain`) plus the chapter-layout plan. Fills only gaps unless `refresh` re-grooms every artifact. Must run before `scaffold`. `override.md`/`override.txt` are pipeline-level, not backlog, artifacts. |
| `scaffold <gist> count\|chapter-count <number>` | Creates or repairs `.space/pipeline/<bookname>/` through the scaffold agent (prelayout -> layout skill -> postlayout), gated by the existence of `book.json`. Never creates or modifies `epic.md`. |
| `<agentname> <chapter>\|<n>\|all\|continue` | Runs any registered agent (`.framework/agents/<agentname>/agent.md`) against selected chapters in an existing pipeline. Does not promote output to `source/books/`. |
| `poet` | Invokes the poet agent to produce a single finished poem from the human-authored override file (poetry pipelines only). |
| `chapter <chapter>\|<n>\|all\|continue` | Writes one chapter, a numbered chapter, all chapters, or the remaining missing chapters, routed through the chapter agent. |
| `filter <filter>\|*\|all` | Runs a single filter, or all filters in order, on an existing pipeline. |
| `form <formname>` | Sets or changes the pipeline form (`novel` or `poetry`). |
| `config [<key> [<value>]]` | Gets or sets stereotype/model config such as `signature`, `reference`, `theme_set`, or `syntax`. Bare `config` prints the current configuration. |
| `add <chapter-count> filter <filter>\|*\|all` | Adds more main chapters to an existing book pipeline, then runs the requested filter or full filter chain for the newly added chapters. |
| `options` | Lists available book pipelines and destinations. |
| `help` | Shows command usage. |
| `layout [<count>]` (alias: `pipeline`) | Reads `.space/backlog/epic/<bookname>/epic.md` and re-creates `.space/backlog/epic/<bookname>/book.json` so every chapter is complete, with each `chapter_summary` expanded to a minimum of 200 words (4 bullets of ~50 words each). `<count>` is the number of chapters to lay out, defaulting to `5`. If chapters exceed 10, fill in batches of 10. After writing the backlog `book.json`, clone it to `.space/pipeline/<bookname>/book.json`. |

---

## Command Rules

- **Bare bookname creates backlog epic.** The bare `/book <bookname>` command checks `.space/backlog/epic/<bookname>/epic.md`; if it is missing, create it with an auto-generated gist. It does not scaffold a pipeline.
- **Backlog vs. pipeline boundary.** Commands 1-2 (`<bookname>` with optional gist, `init`/`backlog`) operate only in `.space/backlog/epic/<bookname>/` and never create or modify pipeline files. Commands 3+ (`scaffold` onward) operate only on the pipeline and `source/books/` and never modify backlog files.
- Use the bare `/book <bookname> [<gist>]` command for early backlog work when you want to develop a rich, detailed epic. It creates or updates the epic and never creates `.space/pipeline/<bookname>/`.
- **`init` before `scaffold`.** `scaffold` is gated by the existence of `.space/backlog/epic/<bookname>/book.json`; if it is missing, stop and instruct the user to run `/book <bookname> init` first. Do not silently fall back to a default template.
- Use `scaffold` to create the full pipeline with explicit gist and chapter count. The gist is required and must be a single sentence.
- `scaffold` requires `count` or `chapter-count` followed by the main chapter count. The default comes from `book.json` if it specifies one, otherwise 5.
- Once a pipeline exists, subsequent commands work from pipeline data. Do not re-scaffold from scratch unless explicitly asked.
- `filter` never scaffolds. If the pipeline does not exist, report that the book must be scaffolded first.
- `filter *` and `filter all` mean "run the full ordered filter chain."
- `write continue` resumes from the first missing finished chapter under `source/books/<bookname>/chapters/`.
- A specific chapter request writes only that chapter, even if earlier chapters are incomplete.
- **Agents invoke skills.** Route every skill-backed operation through an agent in `.framework/agents/<name>/agent.md`; never execute a skill directly from the workflow.

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
| **Filter chain** | preset-defined (`layout-novel/SKILL.md`) | preset-defined (`layout-poetry/SKILL.md`) |
| **Word target** | 5,500+ words | 500-800 words |
| **Stereotype templates** | `stereotypes/novel/` | `stereotypes/poetry/` |

---

## Pipeline Layout

Pipeline structure is owned by `.framework/agents/scaffold/agent.md`, which selects `.framework/skills/layout-novel/SKILL.md` for novels and `.framework/skills/layout-poetry/SKILL.md` for poetry. When scaffolding, creating, or repairing `.space/pipeline/<bookname>/`, read and follow the selected form-specific layout skill.

Mandatory path invariant:

- chapters live only at `.space/pipeline/<bookname>/chapters/<n>/`
- segments live only at `.space/pipeline/<bookname>/chapters/<n>/segments/<x>/`
- never create root-level `<n>/` or `<x>/` folders under the book pipeline

`.framework/templates/SCAFFOLD.md` is a short reference note only; do not treat it as the primary scaffold instruction source.

---

## Scaffolding Flow

### The bare bookname command (backlog only)

For `/book <bookname> [<gist>] [form] [refresh]`:

1. Check whether `.space/backlog/epic/<bookname>/epic.md` exists.
2. **If epic doesn't exist:** Create it automatically with auto-generated gist.
3. **If epic exists:** Re-groom it into a coherent foundation (or report it exists and leave it unchanged if no gist/form/refresh is supplied).
4. Stop there. The bare command never creates `.space/pipeline/<bookname>/`, never runs layout, and never runs research.

Backlog preparation continues with `init`/`backlog` (configure the book plan), then `scaffold` builds the pipeline.

### The scaffold command (gated by the book plan)

For `/book <bookname> scaffold <gist> count|chapter-count <number> [--form novel|poetry]`:

1. **Book plan is mandatory.** `.space/backlog/epic/<bookname>/book.json` must exist (run `init` first if missing). Do not silently fall back to a default template.
2. If the pipeline already exists, skip scaffolding and work with the existing data.
3. Determine the form from `--form` or by inference (narrative premise -> novel; topic/term list -> poetry); record it in `model.json`.
4. Validate the gist (single sentence) and determine the chapter count (default from `book.json` if it specifies one, otherwise 5).
5. For a novel, stop if the backlog epic is missing — scaffold never creates or rewrites the epic.
6. Invoke the scaffold agent (`.framework/agents/scaffold/agent.md`); never invoke layout skills directly. The scaffold agent runs the prelayout agent first (`.framework/agents/prelayout/agent.md`), then the form-specific layout skill.
7. Build `filters/filters.json` from `book.json`'s authoritative `filter_chain` — never copy the layout skills' *Preset* sections directly.
8. Apply form-specific initialization in `model.json` and related files; seed `filters/override/filter.md` whenever `override` appears in the chain.
9. Run the postlayout agent (`.framework/agents/postlayout/agent.md`) to generate the dynamic pipeline master prompt from the backlog `override.txt`. A scaffold is not complete until postlayout has run.
10. Do not run filters during scaffold — structure only. After scaffold, run `/book <bookname> filter <filter>|*|all` to populate filter outputs before writing any chapter.

---

## The Bare Bookname Command (gist merged)

For `/book <bookname> [<gist>] [form] [refresh]`:

1. Create or update `.space/backlog/epic/<bookname>/epic.md` and develop it into a well-groomed, detailed narrative foundation.
2. Infer a one-sentence gist from the book name if none is supplied.
3. **Novel:** Develop a rich, well-groomed epic that includes:
   - A compelling premise and historical grounding
   - Detailed character descriptions, motivations, and arcs
   - Thematic threads that weave through the narrative
   - Chapter-by-chapter outline with key scenes and turning points
   - World-building details (settings, era, cultural context)
   - Emotional and philosophical depth
4. **Poetry:** Create a thoughtful epic with thematic grounding, topical structure, and reference to poetic voice/tradition.
5. Do not create `.space/pipeline/<bookname>/`, do not run layout, and do not run research.

Every novel epic should include a metadata block near the top with title, book name, epic path, timestamps, authoring engine, language, genre, era, chapter count, and gist. When the epic changes, keep the metadata block current and regenerate the pipeline gist from the epic.

---

## The Init Command

`/book <bookname> init [<gist>] [<preset>] [form] [refresh]` (alias: `backlog`) fully configures the backlog epic folder and derives the ordered filter chain. Init operates only in the backlog; it never creates or modifies pipeline files.

The three backlog artifacts:

| File | Role |
|------|------|
| `gist.md` | The seed idea — one-sentence gist plus short expansion. |
| `epic.md` | The full narrative foundation — premise, setting, characters, themes, chapter outline. |
| `book.json` | The chapter-layout plan and the authoritative `filter_chain`/`word_target` — the blueprint `scaffold` builds from. |

`override.md` and `override.txt` are **pipeline-level** artifacts, not backlog artifacts. They are created by the scaffold step (`.space/pipeline/<bookname>/override.txt` and `.space/pipeline/<bookname>/filters/override/filter.md`), never in the backlog folder.

Behavior:

1. If the gist is absent, bootstrap the three backlog artifacts; otherwise fill only gaps (`book.json`).
2. If `[<preset>]` is supplied, merge its filter chain into `book.json` as `filter_chain`; otherwise the init agent selects the form-specific default preset (`.framework/skills/layout-novel/SKILL.md` for novel, `.framework/skills/layout-poetry/SKILL.md` for poetry).
3. If `[form]` is supplied and differs from the current form, change it and re-derive `filter_chain`, `word_target`, the `chapters` array, and `all_characters` (novels) / drop it (poetry).
4. With `refresh`, re-groom every backlog artifact from the existing material, reconciling them to the resolved form while preserving the original `Created` timestamp.
5. Do not execute filters; only prepare the filter chain and the chapter-layout plan.

After init, report each artifact as `created` or `existing` plus the ordered filter chain. If the pipeline does not exist yet, the next step is `/book <bookname> scaffold`.

---

## The Add Command

`/book <bookname> add <chapter-count> filter <filter>|*|all` extends an existing book pipeline with more main chapters, then runs the requested filter target for those new chapters.

1. Stop if `.space/pipeline/<bookname>/` does not exist; use `scaffold` first.
2. Treat `<chapter-count>` as the number of additional main chapters to append, not the new total.
3. Update the backlog epic, book plan, and `chapter_count` fields to the new total.
4. Create only the new chapter folders and form-appropriate state files under `.space/pipeline/<bookname>/chapters/<n>/`.
5. Run the requested filter target only for the newly added chapters.

---
## Filter Chains

The filter chain depends on the form, and is declared by the form's preset (the *Preset* section of the form-specific layout skill).

**Novel (preset: `layout-novel/SKILL.md`):**

```text
workshop -> research -> seeds -> correctness -> theme -> syntax
```

| Filter | Agent | Folder | Role file |
|--------|-------|--------|-----------|
| workshop | `.framework/agents/workshop/agent.md` | `filters/workshop/` | `workshop/workshop.md` |
| research | `.framework/agents/research/agent.md` | `filters/research/` | `research/research.md` |
| seeds | `.framework/agents/seeds/agent.md` | `filters/seeds/` | `seeds/seeds.md` |
| correctness | `.framework/agents/correctness/agent.md` | `filters/correctness/` | `correctness/correctness.md` |
| theme | `.framework/agents/theme/agent.md` | `filters/theme/` | `theme/theme.md` |
| syntax | `.framework/agents/syntax/agent.md` | `filters/syntax/` | `syntax/syntax.md` |

**Poetry (preset: `layout-poetry/SKILL.md`):**

```text
workshop -> research -> correctness -> theme -> syntax -> override -> quality
```

| Filter | Agent | Folder | Role file |
|--------|-------|--------|-----------|
| workshop | `.framework/agents/workshop/agent.md` | `filters/workshop/` | `workshop/workshop.md` |
| research | `.framework/agents/research/agent.md` | `filters/research/` | `research/research.md` |
| correctness | `.framework/agents/correctness/agent.md` | `filters/correctness/` | `correctness/correctness.md` |
| theme | `.framework/agents/theme/agent.md` | `filters/theme/` | `theme/theme.md` |
| syntax | `.framework/agents/syntax/agent.md` | `filters/syntax/` | `syntax/syntax.md` |
| override | human-editable `filter.md` | `filters/override/` | `override/override.md` |
| quality | `.framework/agents/quality/agent.md` | `filters/quality/` | `quality/quality.md` |

Each filter reads the pipeline data and any upstream filter output it needs, then writes to its own folder. Run the full chain strictly in order.

After each filter runs against a chapter, the workflow:

1. **Archives the previous draft** — if the filter rewrites `.space/pipeline/<bookname>/chapters/<n>/chapter.md`, the prior version is copied to `.space/pipeline/<bookname>/chapters/<n>/history/` (created if missing) with a timestamped/versioned name. The live `chapter.md` always holds the current state.
2. **Updates the chapter state** — `.space/pipeline/<bookname>/chapters/<n>/model.json` is updated: `state` is set to the filter that just ran, and a `filter_history` array entry records `{ filter, ran_at, output_file }`. All other fields are preserved (merge, never overwrite).

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
source/books/<bookname>/
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

Always inspect the pipeline and `source/books/<bookname>/chapters/` before writing. The agent resumes from existing state and never restarts from the beginning unless explicitly asked.

Use:

- `/book <bookname> write continue` to write the first missing chapter onward.
- `/book <bookname> write all` to write every chapter in canonical order and assemble `book.md`.
- `/book <bookname> filter *` to refresh the full filter chain before chapter writing.

