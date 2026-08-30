# Novelist

A multi-agent literary engine for writing **poetic prose** and **frame-story novels** in the voice of Kahlil Gibran's *The Prophet* (1923), grounded in a reference book (e.g. Marcus Aurelius's *Meditations*, Lalon Shah's Baul tradition).

The system is split into two layers:

- **`.framework/`** — the agents (skills + workflows) that do the work.
- **`.space/`** and **`source/`** — the data: inputs (context, library, pipeline, templates) and outputs (finished chapters).

---

## Architecture

```
novelist/
├── .framework/              # the agents
│   ├── skills/              # on-demand workflows (slash commands)
│   └── workflows/           # the writing engines (poetry.md, reframe.md, novel.md, guide.md)
├── .space/                  # inputs & data
│   ├── context/             # qualities/, references/, themes/, library/
│   ├── library/             # poetry book instances
│   ├── pipeline/            # novel layouts (book_<name>/)
│   └── templates/           # poetry/, stereotypes/, novel/
├── source/                  # finished chapters (book_<name>/)
├── .gitignore
├── LICENSE
└── README.md
```

---

## Skills

Each skill is an on-demand workflow, invoked as a slash command.

| Skill | Command | Purpose |
|-------|---------|---------|
| `poet` | `/poet` | Write, scaffold, revise, and audit Gibran-esque poetic prose books. |
| `novelist` | `/novel` | Scaffold a novel layout and write frame-story chapters. |
| `historian` | `/historian` | Collect historical data from the internet, static text, and themes. |
| `character-builder` | `/character` | Build and manage the character roster (`characters.json`). |
| `workshop-director` | `/workshop` | Conduct workshops that frame each novel chapter. |
| `subject-matter-philosophy` | `/philosophy` | Build the philosophical grounding (quality/seed analysis). |
| `language-construct` | `/language` | Build the language layer (lexicon, register, dialect, stylistic DNA). |

> `story-writer` and `poetry-writer` are legacy aliases of `poet`.

---

## The Two Engines

### 1. Poet — Gibran-esque Poetic Prose

Transforms a list of topics/terms into philosophical poetic prose chapters. Weaves three pillars:

1. **Context** (dynamic) — the reference book and its analysis.
2. **Style** (fixed) — the Gibran-esque voice (Question → Oration → Benediction).
3. **Theme** (dynamic) — the thematic category assigned to each chapter.

- Engine: `.framework/workflows/poetry.md`
- Reframer: `.framework/workflows/reframe.md`
- Inputs: `.space/context/` (qualities, themes, references)
- Template: `.space/templates/poetry/default/`
- Outputs: `source/book_<name>/`

### 2. Novelist — Frame-Story Novels

Writes novels that interleave a modern frame (a theatre workshop) with a historical narrative. Every novel begins with a **layout** (mandatory structural skeleton).

- Engine: `.framework/workflows/novel.md`
- Layout: `.space/pipeline/book_<name>/` (book.json, characters.json, workshop_minutes/, chapter_seeds/, chapters_research/)
- Outputs: `source/book_<name>/`

---

## The Novel Pipeline

The full chain for a frame-story novel:

```
layout → research → characters → workshops → chapters
```

| Step | Skill | Produces |
|------|-------|----------|
| Layout | `novelist` | `.space/pipeline/book_<name>/` |
| Research | `historian` | `chapters_research/<chapter>.json` |
| Characters | `character-builder` | `characters.json` |
| Workshops | `workshop-director` | `workshop_minutes/<chapter>.md` |
| Chapters | `novelist` | `source/book_<name>/<chapter>.md` |

---

## Quick Start

```text
# Poetic prose
/poet <bookname> <quality> <theme> <reference>   # scaffold a new book
/poet <bookname>                                 # write chapters

# Frame-story novel
/novel <bookname> <chapter_count>                # scaffold the layout
/novel <bookname> all                            # write all chapters
```

---

## Data Layout

| Folder | Role |
|--------|------|
| `.space/context/qualities/` | Seed analyses (philosophical grounding) |
| `.space/context/themes/` | Thematic category sets |
| `.space/context/references/` | Source texts and dictionaries |
| `.space/context/library/` | Historical source texts |
| `.space/library/` | Poetry book instances |
| `.space/pipeline/` | Novel layouts (inputs) |
| `.space/templates/` | Canonical templates (poetry, stereotypes, novel) |
| `source/` | Finished chapters (outputs) |
