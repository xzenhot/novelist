# Novelist

A multi-agent literary engine for writing **poetic prose** and **frame-story novels** in the voice of Kahlil Gibran's *The Prophet* (1923), grounded in a reference book (e.g. Marcus Aurelius's *Meditations*, Lalon Shah's Baul tradition).

The system is split into two layers:

- **`.framework/`** — the agents (skills + workflows) that do the work.
- **`.space/`** and **`source/`** — the data: inputs (context, pipeline, templates) and outputs (finished chapters).

---

## Architecture

```
novelist/
├── .framework/              # the agents
│   ├── agents/              # role agents (poet, editor, translator, character, …)
│   ├── skills/              # on-demand workflows (slash commands)
│   ├── workflows/           # the writing engines (poetry.md, reframe.md, novel.md, guide.md)
│   ├── streams/             # narrative streams (novel, poetry, story, play, feature)
│   ├── rules/               # shared rules
│   └── templates/           # canonical templates (poetry, stereotypes, novel)
├── .space/                  # inputs & data
│   ├── context/             # qualities/, references/, themes/
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

## The Writing Agents

The `.framework/` layer is organized into four kinds of agents:

| Kind | Location | Role |
|------|----------|------|
| **Workflows** | `.framework/workflows/` | The top-level writing engines that orchestrate a whole book. |
| **Skills** | `.framework/skills/` | On-demand, single-purpose workflows invoked as slash commands. |
| **Role agents** | `.framework/agents/` | Specialized roles (poet, editor, translator, character, …). |
| **Streams** | `.framework/streams/` | Narrative streams (novel, poetry, story, play, feature). |

### Workflows (`.framework/workflows/`)

| Workflow | Purpose |
|----------|---------|
| `poetry.md` | The **writer** engine — transforms topics/terms into Gibran-esque poetic prose chapters. |
| `reframe.md` | The **reframer** engine — reshapes finished chapters (voice, register, dialect) while preserving their core. |
| `novel.md` | The **novel-writer** engine — turns workshop narratives into frame-story novel chapters. |
| `guide.md` | Implementation guide for the writer agent. |

### Skills (`.framework/skills/`)

Each skill is a single-purpose workflow with a `SKILL.md` that defines when to use it and what it produces.

| Skill | Purpose |
|-------|---------|
| `layout` | Scaffold the structural skeleton of a novel pipeline (`.space/pipeline/book_<name>/`). |
| `narrative` | Write/revise frame-story novel chapters (Workshop / Story / Discussion). |
| `poeticprose` | Write/revise Gibran-esque philosophical poetic prose. |
| `research` | Gather, organize, and verify source material (qualities, themes, references). |
| `history` | Gather and weave historical material into a narrative. |
| `philosophy` | Build the philosophical grounding (seed/quality analysis). |
| `theme` | Define and weave thematic categories into chapters. |
| `revision` | Revise, tighten, audit, or transform already-written chapters. |
| `translation` | Translate/localize literary text across languages. |
| `dialogue` | Write and polish spoken exchanges between characters. |
| `pacing` | Control rhythm, tempo, tension, and cliffhangers. |
| `contemporary` | Write the modern frame scenes of a frame-story. |
| `geography` | Build the physical and cultural sense of place. |
| `indian` | Ground a story in Indian cultural, historical, and literary context. |
| `mythology` | Draw on myth, legend, folklore, and sacred narrative. |

### Role Agents (`.framework/agents/`)

| Agent | Role |
|-------|------|
| `poet` | The poetic-prose voice. |
| `editor` | Revision and tightening. |
| `translator` | Cross-language rendering. |
| `character` | Character roster and depth. |
| `review` | Audit and review. |
| `reference` | Source-text grounding. |
| `discovery` | Material discovery. |
| `place` | Setting and geography. |
| `prose` | Prose craft. |
| `time` | Era and chronology. |

### Streams (`.framework/streams/`)

| Stream | Purpose |
|--------|---------|
| `novel` | Frame-story novel stream. |
| `poetry` | Poetic-prose stream. |
| `story` | Short-story stream. |
| `play` | Dramatic/play stream. |
| `feature` | Feature-writing stream. |

---

## The Two Engines

### 1. Poet — Gibran-esque Poetic Prose

Transforms a list of topics/terms into philosophical poetic prose chapters. Weaves three pillars:

1. **Context** (dynamic) — the reference book and its analysis.
2. **Style** (fixed) — the Gibran-esque voice (Question → Oration → Benediction).
3. **Theme** (dynamic) — the thematic category assigned to each chapter.

- Engine: `.framework/workflows/poetry.md`
- Reframer: `.framework/workflows/reframe.md`
- Inputs: `.framework/templates/stereotypes/poetry/` (qualities, themes, references, signatures)
- Template: `.framework/templates/stereotypes/poetry/default/`
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
| `.framework/templates/novel/qualities/` | Seed analyses (philosophical grounding) |
| `.framework/templates/novel/themes/` | Thematic category sets |
| `.framework/templates/novel/references/` | Source texts and dictionaries |
| `.space/pipeline/` | Novel layouts (inputs) |
| `.framework/templates/` | Canonical templates (poetry, stereotypes, novel) |
| `source/` | Finished chapters (outputs) |

